# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


"""
使い方はREADME.md参照
"""


from collections import OrderedDict
import argparse
import inspect
import os
import re
import sys
import xml.etree.ElementTree as etree

try:
    import bpy  # blender module
except ImportError:
    print("\nERROR: this script must run from inside Blender")
    import sys
    sys.exit()
import bpy.types
import bpy.ops
import bgl
import blf
import gpu
import mathutils.noise

sys.path.append(os.path.dirname(__file__))
from . import bgl_functions


REPLACE_MOD = True


class Null:
    def __bool__(self):
        return False


bl_to_py_types = {
    'boolean': 'bool',
    'string': 'str',
    'integer': 'int'
}


def get_itertext(element, _bullet='', _head=True, _parents=None):
    """Create text iterator.

    The iterator loops over the element and all subelements in document
    order, returning all inner text.

    """
    tag = element.tag
    if not isinstance(tag, str) and tag is not None:
        return

    if _parents is None:
        _parents = []

    if tag == 'paragraph' and not _head:
        yield '\n'

    if tag == 'bullet_list':
        _bullet = element.get('bullet', '')

    if _bullet and tag == 'paragraph':
        yield _bullet + ' '
        _bullet = ''
        _head = False

    def ignore_text(string):
        if string and string.startswith('\n'):
            if set(string) == {'\n', ' '} or set(string) == {'\n'}:
                return True
        return False

    if ignore_text(element.text):
        pass
    elif element.tag == 'reference':
        if len(element) == 0:
            if element.text:
                yield element.text
                _head = False
        else:
            if element[0].tag == 'emphasis':
                # anyでreftitle="bpy.types.KeyMapItem.any"となる不具合？
                # int, floatでも同様の不一致
                pass
            else:
                t = None
                if element[0].tag == 'literal_emphasis':
                    # FIX bmesh.types.BMLayerAccessVert.string, int, float, ...
                    # 他にも bpy.types.PropertyGroupItem.string, ... とか
                    if element.get('reftitle', '').startswith(
                            ('bmesh.types.BMLayerAccess',
                             'bpy.types.PropertyGroupItem')):
                        d = {'int': 'int',
                             'float': 'float',
                             'string': 'str'}
                        t = d.get(element[0].text)
                if t:
                    yield t
                    _head = False
                    return
                else:
                    t = element.get('reftitle')
                    if t:
                        yield t
                        _head = False
                        return
                    else:
                        t = element.get('refuri')
                        if t:
                            yield t
                            _head = False
                        else:
                            raise ValueError()
    else:
        if element.text:
            # ENUM名は ' で囲む
            wrap_quote = False
            if element.tag == 'literal':
                bullet_elem = None
                tags = []
                for elem in _parents[::-1]:
                    tags.append(elem.tag)
                    if elem.tag == 'bullet_list':
                        bullet_elem = elem
                        break
                if tags[:3] == ['paragraph', 'list_item', 'bullet_list']:
                    if bullet_elem.get('bullet') == '*':
                        wrap_quote = True
            if wrap_quote:
                yield "'{}':".format(element.text)
                _head = False
            else:
                yield element.text
                _head = False

    _parents.append(element)

    for elem in element:
        for t in get_itertext(elem, _bullet, _head, _parents[:]):
            if t:
                yield t
                _head = False
        if elem.tail:
            # ignore_tail = elem.tag in ('field_list', 'field', 'field_body',
            #                            'bullet_list', 'list_item', 'paragraph')
            # if not ignore_tail:
            if not ignore_text(elem.tail):
                yield elem.tail
                _head = False


def subdivide_type_string(type_string):
    """:rtype: (str, str, str)
    """
    default = option = ''
    m = re.match('(.*), (\(.*\))$', type_string)
    if m:
        type_string, option = m.groups()
    m = re.match('(.*), default (.*)$', type_string)
    if m:
        type_string, default = m.groups()

    return type_string, default, option


def get_array_type(prop):
    array_type = ''
    if prop.type == 'FLOAT' and prop.array_length:
        if prop.subtype in ('COORDS', 'TRANSLATION', 'DIRECTION',
                            'VELOCITY', 'ACCELERATION',  'XYZ',
                            'XYZ_LENGTH'):
            array_type = 'Vector'
        elif prop.subtype == 'MATRIX':
            array_type = 'Matrix'
        elif prop.subtype == 'EULER':
            array_type = 'Euler'
        elif prop.subtype == 'QUATERNION':
            array_type = 'Quaternion'
        elif prop.subtype in ('COLOR', 'COLOR_GAMMA'):
            array_type = 'Color'
    return array_type


def get_pytype(parser, param_name='', is_output=False):
    """typeを表す文字列をpycharmが理解できるものに変換する"""
    type_string = None
    for kind, param_str in parser.params:
        if param_name:
            if kind == 'type ' + param_name:
                type_string = param_str
                break
        else:
            if (is_output and kind == 'rtype' or
                    not is_output and kind == 'type'):
                type_string = param_str
                break
    if type_string is None:
        raise ValueError()
    type_string = subdivide_type_string(type_string)[0]

    prop = None
    if parser.module == 'bpy.types':
        if '.' in parser.fullname:
            class_name, class_attr = parser.fullname.split('.')
        else:
            class_name = parser.fullname
            class_attr = ''
        if class_name and class_attr:
            try:
                cls = getattr(bpy.types, class_name)
                if param_name:
                    func = cls.bl_rna.functions[class_attr]
                    prop = func.parameters[param_name]
                    # 関数の返り値はprop.is_outputが真になっている
                elif is_output:
                    for prop in cls.bl_rna.functions[class_attr].parameters:
                        if prop.is_output:
                            break
                    else:
                        raise ValueError()
                elif class_attr:
                    prop = cls.bl_rna.properties[class_attr]
            except:
                pass
    elif parser.module.startswith('bpy.ops.'):
        func_name = parser.fullname
        if func_name and param_name:
            b, o, m = parser.module.split('.')
            mod = getattr(bpy.ops, m)
            try:
                func = getattr(mod, func_name).get_rna()
                prop = func.bl_rna.properties[param_name]
            except:
                pass
        # NOTE: bpy.opsではis_outputに該当するプロパティーは無い

    bl_type_collection_fixed = ''  # elem of collection
    array_num = 0
    array_type = ''
    value_range = ''
    m = re.match('(Enumerator|enum) in ', type_string)
    if m:
        py_type = 'str'
    else:
        m = re.match('([\w.]+) array of (.+) items( in (?P<range>\[.*\]))?',
                     type_string)
        if m:
            bl_type = m.group(1)
            array_num = int(m.group(2))
            value_range = m.group('range')
            if prop:
                array_type = get_array_type(prop)
        else:
            m = re.match('([\w.]+) in (?P<range>\[.*\])', type_string)
            if m:
                bl_type = m.group(1)
                value_range = m.group('range')
            else:
                # collection (type付き)
                m = re.match('([\w.]+) ([\w.]+) of ([\w.]+)', type_string)
                if m:
                    bl_type = m.group(1)
                    bl_type_collection_fixed = m.group(3)
                else:
                    # collection (type無し)
                    m = re.match('([\w.]+) of ([\w.]+)', type_string)
                    if m:
                        bl_type = m.group(1)
                        bl_type_collection_fixed = m.group(2)
                    else:
                        bl_type = type_string
        py_type = bl_to_py_types.get(bl_type, bl_type)

    if value_range:
        min_max = value_range[1:-1].split(', ')
        # 10000000 より大きいならinf
    else:
        min_max = []

    if array_type:
        py_type = 'mathutils.' + array_type
    elif array_num:
        py_type = 'collections.Sequence[{}]'.format(py_type)

    if py_type == 'sequence':
        py_type = 'collections.Sequence'

    return py_type


def title_indent(title, string, separate=': '):
    # 'param hoge' ['comment1', 'comment2']
    # -> ['param hoge: comment1', '    comment2']
    ls = string.split('\n')
    if ls:
        if title:
            title += separate
        return [title + ls[0]] + ['    ' + s for s in ls[1:]]
    else:
        return []


class AttributeParser(list):
    def __init__(self, parser, element):
        """
        :type parser: ModuleParser | CallableParser
        :type element: xml.etree.ElementTree.Element
        """
        super().__init__()
        self.parser = parser  # 親
        self.element = element

        self.type = ''
        self.module = ''  # Element.get()で取得 e.g. 'bpy.types'
        self.fullname = ''  # Element.get()で取得 e.g. 'Object.active_material'
        self.name = ''
        self.docstrings = ''  # 文字列終端に改行文字は無い
        # [['param', 'string'], ['type', 'string'], ...]
        # stringが空文字になる事は無い
        # 文字列終端に改行文字は無い
        self.params = []
        # class用
        self.args = []
        self.bases = []
        # data用
        self.value = Null
        """:type: Null | str"""

    def get(self, name):
        for p in self:
            if p.name == name:
                return p

    def modify_type_params(self):
        """pycharmが理解できる型にする。self.paramsを上書きする"""
        module = self.module

        # return
        i = 0
        num = len(self.params)
        while i < num:
            kind, param_str = self.params[i]
            if kind.startswith('type') or kind == 'rtype':
                m = re.match('type (\w+)', kind)
                if m:
                    param_name = m.group(1)
                else:
                    param_name = ''
                is_output = kind == 'rtype'
                py_type = get_pytype(self, param_name, is_output)
                if py_type:
                    if REPLACE_MOD:
                        py_type = re.sub('(^|(?<=\W)){}\.(\w+)'.format(module),
                                         '\g<2>', py_type)
                    # default False, (readonly) とか付いてる場合でも追加される
                    # one of... は bge.texture の enum系。無駄なので排除
                    if (param_str != py_type and
                            bl_to_py_types.get(param_str) != py_type and
                            not py_type.startswith('one of...')):
                        orig_type = '(type: ' + param_str + ')'
                        for p in self.params:
                            if p[0] == 'param ' + param_name:
                                p[1] += '\n' + orig_type
                                break
                        else:
                            if kind == 'type':
                                self.docstrings += '\n' + orig_type
                            else:
                                self.params.insert(i,
                                    ['param ' + param_name, orig_type])
                                i += 1
                                num += 1
                    self.params[i][1] = py_type

            elif kind in ('value', 'default'):
                # typeが見付からなかったら追加
                for k, l in self.params:
                    if k.startswith(('param', 'return')):
                        print(self.name, self.params)
                        raise ValueError()  # attributeである事を想定する
                for k, l in self.params:
                    if k == 'type':
                        break
                else:
                    try:
                        name = type(eval(param_str)).__qualname__
                    except:
                        name = ''
                    if name:
                        self.params.insert(i, ['type', name])
                        i += 1
                        num += 1

            i += 1

    def _parse_params_field_body(self, params, element, field_name):
        # field - field_body - paragraph
        # field - field_body - bullet_list - list_item - paragraph

        if field_name == 'Parameters':
            def parse(paragraph_elem):
                t = ''.join(get_itertext(paragraph_elem))
                m = re.match('(\w+) --[ \n](.*)', t, re.DOTALL)
                if m:
                    name, param_str = m.groups()
                    type_str = ''
                else:
                    m = re.match('(\w+) \((.*)\) --[ \n](.*)', t, re.DOTALL)
                    if m:
                        name, type_str, param_str = m.groups()
                    else:
                        # 書式不明で判別不能。
                        # bge.types.KX_ConstraintWrapper.setParam(axis, value0, value1)
                        # bgl.glClearAccum(red, green, blue, alpha)
                        m = re.match('(.*?) --[ \n](.*)', t, re.DOTALL)
                        name, param_str = m.groups()
                        type_str = ''

                param_str = param_str.strip('\n')
                if param_str:
                    params.append(['param ' + name, param_str])
                type_str = type_str.strip('\n')
                if type_str:
                    params.append(['type ' + name, type_str])

            for elem in element:
                if elem.tag == 'paragraph':
                    parse(elem)
                elif elem.tag == 'bullet_list':
                    for list_item_elem in elem:
                        for paragraph_elem in list_item_elem:
                            parse(paragraph_elem)

        elif field_name.startswith('Return ') and field_name != 'Return type':
            # bpy.types.Object.camera_fit_coords()
            # 複数の要素をtupleで返す
            def parse(paragraph_elem):
                return ''.join(get_itertext(paragraph_elem)).strip('\n')

            return_str = field_name[7:]
            for elem in element:
                if elem.tag == 'paragraph':
                    if return_str:
                        return_str += '\n'
                    return_str += parse(elem)
            if return_str:
                params.append(['return', return_str])
                params.append(['rtype', 'tuple'])

        elif field_name in ('Type', 'Return type', 'Rtype vert', 'Returns'):
            if field_name == 'Type':
                type_kind = 'type'
            elif field_name == 'Returns':
                type_kind = 'return'
            else:
                type_kind = 'rtype'
            t = ''
            for elem in element:
                if elem.tag not in ('paragraph', 'bullet_list'):
                    continue  # このif文は必要か？
                type_str = ''.join(get_itertext(elem)).strip('\n')
                if type_str:
                    t += ('\n' if t else '') + type_str
            if t:
                params.append([type_kind, t])

        elif field_name in ('Value', 'Default'):
            for elem in element:
                if elem.tag not in ('paragraph', 'bullet_list'):
                    continue
                value_str = ''.join(get_itertext(elem)).strip('\n')
                if value_str:
                    params.append([field_name.lower(), value_str])

        else:
            # 'File', 'Raises ValueError'
            for elem in element:
                if elem.tag not in ('paragraph', 'bullet_list'):
                    continue
                other_str = ''.join(get_itertext(elem)).strip('\n')
                if other_str:
                    params.append([field_name, other_str])

    def parse_params(self, element):
        """docstringsの :param や :type 等"""
        for field_elem in element:
            field_name = ''
            for elem in field_elem:
                if elem.tag == 'field_name':
                    field_name = elem.text
                elif elem.tag == 'field_body':
                    self._parse_params_field_body(
                        self.params, elem, field_name)

    def format_docstrings(self):
        """
        :rtype: list[str]
        """

        # ここでは文字列の終端に'\n'を入れながら作業する
        docstrings = self.docstrings + '\n'

        param_string = ''
        for kind, param_str in self.params:
            if kind.startswith('param') or kind == 'return':
                if param_str[0] == '*':
                    # 最初からenumの場合は改行してインデントを合わせる
                    param_string += '\n'.join(
                        title_indent(':' + kind, '\n' + param_str, ':'))
                else:
                    param_string += '\n'.join(
                        title_indent(':' + kind, param_str))
                param_string += '\n'
            elif kind.startswith('type') or kind == 'rtype':
                ls = param_str.split('\n')
                param_string += ':' + kind + ': ' + ls[0] + '\n'
                for line in ls[1:]:
                    param_string += '    ' + line + '\n'
        if param_string:
            docstrings += '\n' + param_string

        docstrings = docstrings.strip('\n')

        if not docstrings:
            return []

        if docstrings.count('\n') == 0:
            docstrings = '"""' + docstrings + '"""'
        else:
            if docstrings.startswith((':', '*')):
                docstrings = '"""\n' + docstrings
            else:
                docstrings = '"""' + docstrings
            docstrings += '\n"""'
        return docstrings.split('\n')

    def parse(self):
        pass

    def format(self):
        return []


class DataParser(AttributeParser):
    """'attribute' と 'data' を処理
    """
    def parase_defalut_value(self):
        self.value = Null
        # self.value_kind = ''

        params = self.params
        if not params:
            return

        # vaule, default の param から取得
        for kind, param_str in params:
            if kind in ('value', 'default'):
                if '\n' in param_str:
                    raise ValueError()  # 見つかったら対応する
                # self.value_kind = kind
                try:
                    eval(param_str)
                    self.value = param_str
                except:
                    pass
                return

        # type の param から取得
        for kind, param_str in params:
            if kind == 'type':
                _, default, _ = subdivide_type_string(param_str)
                if default:
                    # self.value_kind = 'type'
                    try:
                        eval(default)
                        self.value = default
                    except:
                        pass
                else:
                    py_type = get_pytype(self)
                    if py_type:
                        if py_type == 'str':
                            self.value = '""'
                        # else:
                        #     m = re.match('(.*?) or None', py_type)
                        #     if m:
                        #         py_type = m.group(1)
                        #     try:
                        #         # self.value = str(eval(py_type + '()'))
                        #         self.value = repr(eval(py_type + '()'))
                        #     except:
                        #         pass

    def parse(self, modify=True):
        """メソッド以外のクラス／インスタンス属性"""
        self.type = self.element.get('desctype')
        for elem in self.element:
            if elem.tag == 'desc_signature':
                self.module = elem.get('module', '')
                self.fullname = elem.get('fullname', '')
                for ele in elem:
                    if ele.tag == 'desc_name':
                        self.name = ele.text
            elif elem.tag == 'desc_content':
                for ele in elem:
                    # docstring
                    if ele.tag == 'paragraph':
                        self.docstrings += ''.join(get_itertext(ele)) + '\n'
                    # enum
                    elif ele.tag == 'bullet_list':
                        self.docstrings += ''.join(get_itertext(ele)) + '\n'
                    # Type
                    elif ele.tag == 'field_list':
                        self.parse_params(ele)
        self.docstrings = re.sub('\n+', '\n', self.docstrings).strip('\n')

        self.parase_defalut_value()
        if modify:
            self.modify_type_params()

        self.parser.append(self)

    def format(self):
        """
        :rtype: list[str]
        """
        text_lines = []
        if self.value is Null:
            value = 'None'
        else:
            value = self.value
        text_lines.append('{} = {}'.format(self.name, value))
        text_lines.extend(self.format_docstrings())
        return text_lines


class CallableParser(AttributeParser):
    """'class', 'function', 'method', 'classmethod', 'staticmethod' を処理
    """
    def parse_args(self, element):
        """def hoge(a, b=1, *c, **d) ここの引数リスト"""
        if element.tag != 'desc_parameterlist':
            raise ValueError()
        ls = []
        for ele in element:
            if ele.tag == 'desc_parameter':
                ls.append(''.join(get_itertext(ele)))
            elif ele.tag == 'desc_optional':
                for e in ele:
                    if e.tag == 'desc_parameter':
                        t = ''.join(get_itertext(e))
                        u = t.split('=')
                        ls.append('='.join([u[0] + ':"Optional"'] + u[1:]))
        return ls

    def parse(self, is_method=False, modify=True):
        """クラス、関数、メソッド"""
        element = self.element

        root_name = ''
        parser = self.parser
        while parser is not None:
            if parser.parser is None:
                root_name = parser.name
                break
            parser = parser.parser

        if is_method:
            self.type = 'method'
        else:
            self.type = element.get('desctype')

        for elem in element:
            # 継承とか引数
            if elem.tag == 'desc_signature':
                self.module = elem.get('module', '')
                self.fullname = elem.get('fullname', '')
                for ele in elem:
                    if ele.tag == 'desc_name':
                        if root_name == 'bgl':
                            # <desc_name>glAccum(op, value):</desc_name>
                            m = re.match('(\w+)\s*\((.*)\):$', ele.text)
                            if m:
                                self.name = m.group(1)
                                self.args = m.group(2).split(', ')
                            else:
                                self.name = ele.text
                        else:
                            self.name = ele.text
                    elif ele.tag == 'desc_parameterlist':
                        self.args = self.parse_args(ele)

            # docstringsとかparam
            elif elem.tag == 'desc_content':
                for ele in elem:
                    # docstrings
                    if ele.tag == 'paragraph':
                        self.docstrings += ''.join(get_itertext(ele)) + '\n'

                    # 引数の詳細
                    elif ele.tag == 'field_list':
                        self.parse_params(ele)

                    # クラス／インスタンス属性 (クラスのみ)
                    elif ele.tag == 'desc':
                        if self.type == 'class':
                            dt = ele.get('desctype')
                            if dt in ('attribute', 'data'):
                                DataParser(self, ele).parse()
                            elif dt in ('function', 'method', 'classmethod',
                                        'staticmethod'):
                                CallableParser(self, ele).parse(
                                    is_method=True)

                    elif ele.tag == 'note':
                        t = ''.join(get_itertext(ele)).strip(' ')
                        # 最初に余分なスペースがある > strip()
                        if t:
                            ls = title_indent('<Note>', t, ' ')
                            self.docstrings += '\n'.join(ls) + '\n'

                    elif ele.tag == 'seealso':
                        t = ''.join(get_itertext(ele))
                        if t:
                            ls = title_indent('<See also>', t, ' ')
                            self.docstrings += '\n'.join(ls) + '\n'

                    elif ele.tag == 'bullet_list':
                        # freestyle.types.IntegrationType
                        t = ''.join(get_itertext(ele))
                        if t:
                            self.docstrings += t + '\n'
        self.docstrings = re.sub('\n+', '\n', self.docstrings).strip('\n')

        if self.type == 'class':
            if self.args and not self.params:
                self.bases = self.args
                self.args = []

        if modify:
            self.modify_type_params()

        self.parser.append(self)

    def format(self):
        text_lines = []
        # self.argsに'cls','self'が入っていた場合は適切に除去する

        if self.type == 'class':
            if self.bases:
                text_lines.append(
                    'class {}({}):'.format(self.name, ', '.join(self.bases)))
            else:
                text_lines.append('class {}:'.format(self.name))
        elif self.type == 'function':
            args = ', '.join(self.args)
            text_lines.append('def {}({}):'.format(self.name, args))
        elif self.type == 'method':
            if self.args and self.args[0] == 'self':
                # freestyle.pyChainSilhouetteGenericIterator
                args = ', '.join(self.args)
            else:
                args = ', '.join(['self'] + self.args)
            text_lines.append('def {}({}):'.format(self.name, args))
        elif self.type == 'classmethod':
            if self.args and self.args[0] == 'cls':
                args = ', '.join(self.args)
            else:
                args = ', '.join(['cls'] + self.args)
            text_lines.append('@classmethod')
            text_lines.append('def {}({}):'.format(self.name, args))
        elif self.type == 'staticmethod':
            args = ', '.join(self.args)
            text_lines.append('@staticmethod')
            text_lines.append('def {}({}):'.format(self.name, args))
        else:
            raise ValueError("unkown: '{}': {}.{}".format(self.type, self.module, self.fullname) )

        docstring_lines = self.format_docstrings()
        if self.type == 'class' and self.args:
            # TODO: __init__を使うべきか
            args = ', '.join(['cls'] + self.args)
            text_lines.append('    def __new__({}):'.format(args))
            if docstring_lines:
                text_lines.extend([' ' * 8 + line for line in docstring_lines])
            text_lines.append(' ' * 8 + 'return super().__new__(cls)')
        else:
            if docstring_lines:
                text_lines.extend([' ' * 4 + line for line in docstring_lines])
            if (self.type == 'function' and
                    self.module.startswith('bpy.ops')):
                text_lines.append(' ' * 4 + "return {'FINISHED'}")
            elif not docstring_lines:
                text_lines.append(' ' * 4 + '""""""')

        for parser in self:
            text_lines.append('')
            text_lines.extend(['    ' + line for line in parser.format()])

        return text_lines


class CommentParser(AttributeParser):
    def __init__(self, strings):
        super().__init__(None, None)
        self.strings = strings

    def format(self):
        return ['# ' + line for line in self.strings]


op_1st_param = [
    'param args',
    '\n'.join(
        ['(override_context, execution_context, undo)',
         'override_context (dict)',
         "execution_context (str) -- enum in ['INVOKE_DEFAULT', "
         "'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', "
         "'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', "
         "'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', "
         "'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']",
         'undo (bool)'
         ])
]

# EnumPropertyItem region_type_items[]
region_type_list = ['WINDOW','HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS',
                    'TOOL_PROPS', 'PREVIEW']

# EnumPropertyItem region_draw_mode_items[]
region_draw_mode_list = ['POST_PIXEL', 'POST_VIEW', 'PRE_VIEW']

# bge.texture
bge_texture_values = {
    'IMB_BLEND_ADD': 1,
    'IMB_BLEND_ADD_ALPHA': 7,
    'IMB_BLEND_COLOR': 23,
    'IMB_BLEND_COLORBURN': 10,
    'IMB_BLEND_COLORDODGE': 12,
    'IMB_BLEND_COPY': 1000,
    'IMB_BLEND_COPY_ALPHA': 1002,
    'IMB_BLEND_COPY_RGB': 1001,
    'IMB_BLEND_DARKEN': 5,
    'IMB_BLEND_DIFFERENCE': 18,
    'IMB_BLEND_ERASE_ALPHA': 6,
    'IMB_BLEND_EXCLUSION': 19,
    'IMB_BLEND_HARDLIGHT': 9,
    'IMB_BLEND_HUE': 20,
    'IMB_BLEND_LIGHTEN': 4,
    'IMB_BLEND_LINEARBURN': 11,
    'IMB_BLEND_LINEARLIGHT': 17,
    'IMB_BLEND_LUMINOSITY': 22,
    'IMB_BLEND_MIX': 0,
    'IMB_BLEND_MUL': 3,
    'IMB_BLEND_OVERLAY': 8,
    'IMB_BLEND_PINLIGHT': 15,
    'IMB_BLEND_SATURATION': 21,
    'IMB_BLEND_SCREEN': 13,
    'IMB_BLEND_SOFTLIGHT': 14,
    'IMB_BLEND_SUB': 2,
    'IMB_BLEND_VIVIDLIGHT': 16,
    'SOURCE_EMPTY': 0,
    'SOURCE_ERROR': -1,
    'SOURCE_PLAYING': 2,
    'SOURCE_READY': 1,
    'SOURCE_STOPPED': 3,
}


class ModuleParser(list):
    """
    treeを解析する
    """
    def __init__(self, name, tree):
        super().__init__()
        self.parser = None  # 変更不可。AttributeParserとの互換性の為
        self.name = name
        self.tree = tree
        self.type = 'module'

    def get(self, name):
        """
        :rtype: DataParser | CallableParser
        """
        for p in self:
            if p.name == name:
                return p

    def _modify_bgl(self):
        # see alsoの削除
        for parser in self:
            parser.docstrings = re.sub('<See also>.*?(\n|$)', '',
                                       parser.docstrings)
            parser.docstrings = parser.docstrings.rstrip('\n')

        # 関数群の挿入
        path = os.path.dirname(os.path.abspath(__file__))
        if sys.path[0] != path:
            sys.path.insert(0, path)
        bgl_funcs = bgl_functions.functions
        i = 0
        n = len(self)
        while i < n:
            parser = self[i]
            if parser.name in bgl_funcs:
                self[:] = self[:i] + self[i + 1:]
                n -= 1
                for func in bgl_funcs[parser.name]:
                    p = CallableParser(self, None)
                    p.type = 'function'
                    p.module = 'bgl'
                    p.name = p.fullname = func.__name__
                    p.args = str(inspect.signature(func))[1: -1].split(', ')
                    p.docstrings = inspect.getdoc(func)
                    self.insert(i, p)
                    i += 1
                    n += 1
            else:
                i += 1

        # bglモジュールから定数の追加
        for attr in dir(bgl):
            ob = getattr(bgl, attr)
            if isinstance(ob, int):
                p = DataParser(self, None)
                p.type = 'value'
                p.module = 'bgl'
                p.name = p.fullname = attr
                p.params = [['type', 'int'],
                            ['value', str(ob)]]
                p.value = ob
                self.append(p)

    def _modify_draw_handler_add(self, parser):
        # bpy_rna_callback.c参照
        parser.type = 'classmethod'
        parser.args = ['func', 'args', 'region_type', 'draw_mode']
        parser.params = [
            ['param func', 'Draw function'],
            ['type func', 'collections.Callable'],
            ['param args', 'function arguments'],
            ['type args', 'hupre'],
            ['param region_type',
             'enum in [{}]'.format(
                 ', '.join(["'" + s + "'" for s in region_type_list]))],
            ['type region_type', 'str'],
            ['param draw_mode',
             'enum in [{}]'.format(
                 ', '.join(["'" + s + "'" for s in region_draw_mode_list]))],
            ['type draw_mode', 'str'],
            ['return', 'handle object'],
            ['rtype', 'PyCapsule']
        ]

    def _modify_draw_handler_remove(self, parser):
        parser.type = 'classmethod'
        parser.args = ['handle', 'region_type']
        parser.params = [
            ['param handle', 'handle object'],
            ['type handle', 'PyCapsule'],
            ['param region_type',
             'enum in [{}]'.format(
                 ', '.join(["'" + s + "'" for s in region_type_list]))],
            ['type region_type', 'str'],
        ]

    def _modify_enum_values(self, mod):
        mod_attrs = dir(mod)
        for parser in self:
            if isinstance(parser, DataParser):
                if parser.name in mod_attrs:
                    value = getattr(mod, parser.name)
                    if isinstance(value, int):
                        # parser.docstrings = ''
                        if parser.params:
                            for p in parser.params:
                                if parser.docstrings:
                                    parser.docstrings += '\n'
                                parser.docstrings += ':{}: {}'.format(*p)
                        parser.value = str(value)
                        parser.params = [['type', 'int']]

    def modify(self):
        """
        不具合や記述間違いの修正
        """
        name = self.name

        m = re.match('bpy\.types\.(\w+)', name)
        if m:
            # 'data' -> 'property'
            if hasattr(bpy.types, m.group(1)):
                ob = getattr(bpy.types, m.group(1))
                ob_parser = self.get(m.group(1))
                for attr in dir(ob):
                    if attr.startswith('_'):
                        continue
                    if isinstance(getattr(ob, attr), property):
                        prop_parser = ob_parser.get(attr)
                        if prop_parser is not None:
                            prop_parser.type = 'property'

            # draw_handler_add(), draw_handler_remove()
            for parser in self:
                for p in parser:
                    if p.name == 'draw_handler_add':
                        self._modify_draw_handler_add(p)
                    elif p.name == 'draw_handler_remove':
                        self._modify_draw_handler_remove(p)

        if name.startswith('bpy.ops'):
            for parser in self:
                if parser.type == 'function':
                    parser.params.insert(0, op_1st_param)
                    parser.args.insert(0, '*args')
                    t = '(type: enum set in {{{}}})'.format(
                        "'RUNNING_MODAL', 'CANCELLED', 'FINISHED', "
                        "'PASS_THROUGH'")
                    parser.params.append(['return', t])
                    parser.params.append(['rtype', 'set[str]'])

        # bmesh.xmlでfrom_edit_mesh()がmethodになっている為
        for parser in self:
            if parser.type == 'method':
                parser.type = 'function'

        # 引数の記述漏れ
        if name == 'bpy.props':
            for parser in self:
                if parser.name == 'RemoveProperty':
                    for i in range(len(parser.args)):
                        if parser.args[i] == 'attr=':
                            parser.args[i] = 'attr=""'
                            break

        # SyntaxError: non-default argument follows default argument
        if name == 'bpy.types.UILayout':
            parser = self.get('UILayout')
            p = parser.get('template_list')
            args = p.args
            for i in range(len(args)):
                if args[i] == 'list_id=""':
                    args[i] = 'list_id'
                    break

        # float('inf')
        if name == 'bge.types.KX_Camera':
            parser = self.get('KX_Camera')
            p = parser.get('getScreenRay')
            args = p.args
            for i in range(len(args)):
                if args[i] == 'dist=inf':
                    args[i] = 'dist=float("inf")'
                    break

        # bpy.data.user_map()の引数が構文エラーを起こす
        # 時々は元の引数に変更がないか確認する
        if name == 'bpy.types.BlendData':
            parser = self.get('BlendData')
            p = parser.get('user_map')
            if p is not None:
                # >>> p.args
                # ['subset:"Optional"=(id1',
                #  'id2:"Optional"',
                #  '...):"Optional"',
                #  'key_types={..}',
                #  'value_types={..}']
                p.args = ["user_map:'[id1, id2, ...]'=[]",
                          'key_types=set()',
                          'value_types=set()']

        # 直前の引数に初期値があるので構文エラーとなる
        if name == 'bpy.types.RenderEngine':
            parser = self.get('RenderEngine')
            p = parser.get('camera_model_matrix')
            if p is not None:
                args = p.args
                for i in range(len(args)):
                    if args[i] == 'r_model_matrix':
                        args[i] = 'r_model_matrix=None'
                        break

        # 変数の前に'logic.'を追加
        if name == 'bge.types.KX_GameObject':
            parser = self.get('KX_GameObject')
            p = parser.get('playAction')
            args = p.args
            for i in range(len(args)):
                if args[i] == 'play_mode=KX_ACTION_MODE_PLAY':
                    args[i] = 'play_mode=logic.KX_ACTION_MODE_PLAY'
                if args[i] == 'blend_mode=KX_ACTION_BLEND_BLEND':
                    args[i] = 'blend_mode=logic.KX_ACTION_BLEND_BLEND'

        if name == 'bge.render':
            parser = self.get('offScreenCreate')
            if parser is not None:
                args = parser.args
                if args == ['width,height[,samples=0]'
                            '[,target=bge.render.RAS_OFS_RENDER_BUFFER]']:
                    args[:] = ['width', 'height', 'samples=0',
                               'target=RAS_OFS_RENDER_BUFFER']
                else:
                    raise ValueError('更新があったので確認せよ')

        # 面倒な事になるのでデフォルトの引数を文字列に直す
        if name == 'bpy.types.bpy_struct':
            parser = self.get('bpy_struct')
            for p in parser:
                if p.name in ('keyframe_delete', 'keyframe_insert'):
                    args = p.args
                    for i in range(len(args)):
                        if args[i] == 'frame=bpy.context.scene.frame_current':
                            args[i] = 'frame="bpy.context.scene.frame_current"'

        # どっかで引数の初期値にこの値を使うから
        if name == 'bpy.app':
            for parser in self:
                if parser.name in (
                        'build_options', 'count', 'driver_namespace', 'ffmpeg',
                        'index', 'handlers', 'ocio', 'oiio', 'sdl',
                        'translations', 'openvdb', 'alembic'):
                    continue
                value = getattr(bpy.app, parser.name)
                if isinstance(value, str):
                    parser.value = '"' + value + '"'
                else:
                    parser.value = str(value)

        if name == 'mathutils':
            # Matrix.col, Matrix.row
            parser = self.get('Matrix')
            for p in parser:
                if p.docstrings:
                    p.docstrings += '\n'
                p.docstrings += '(type: Matrix Access)'
                if p.name in ('col', 'row'):
                    for i, (kind, s) in enumerate(p.params):
                        if kind == 'type':
                            p.params[i][1] = 'collections.Sequence[Vector]'

            parser = self.get('Vector')
            p = parser.get('Range')
            p.args = ['start=0', 'stop=0', 'step=1']

            # # Quaternion.axisの初期値がVectorを使うのでその対処
            # if 0:  # 順番を入れ替える方法
            #     i = self.index(parser)
            #     j = self.index(self.get('Quaternion'))
            #     self[i], self[j] = self[j], self[i]
            # else:  # Noneに置き換える
            #     parser = self.get('Quaternion')
            #     p = parser.get('axis')
            #     p.value = 'None'

        if name == 'mathutils.noise':
            for parser in self:
                parser.args = [arg.replace('noise.types.', 'types.')
                               for arg in parser.args]
                parser.args = [arg.replace('noise.distance_metrics.',
                                           'distance_metrics.')
                               for arg in parser.args]

        # bgl
        if name == 'bgl':
            self._modify_bgl()

        # (ﾉ`Д´)ﾉ.:･┻┻

        # freestyle
        if name == 'freestyle.types':
            parser = self.get('IntegrationType')
            for i, name in enumerate(('MEAN', 'MIN', 'MAX', 'FIRST', 'LAST')):
                p = DataParser(parser, None)
                p.type = 'data'
                p.module = 'freestyle.types'
                p.name = name
                p.fullname = 'IntegrationType.' + name
                p.value = str(i)
                p.params = [['type', 'int']]
                parser.append(p)
        if name == 'freestyle.shaders':
            parser = self.get('SmoothingShader')
            p = parser.get('carricature_factor=1.0)')
            p.name = '__init__'
            p.fullname = 'SmoothingShader.__init__'
            p.args = [
                'num_iterations=100', 'factor_point=0.1',
                'factor_curvature=0.0', 'factor_curvature_difference=0.2',
                'aniso_point=0.0', 'aniso_normal=0.0', 'aniso_curvature=0.0',
                'carricature_factor=1.0']
        if name == 'freestyle.utils':
            parser = self.get('pairwise')
            parser.args = [
                'iterable',
                "types=\"{<class 'StrokeVertexIterator'>, <class 'Stroke'>}\""
                ]

        # bpy_extras
        if name == 'bpy_extras.io_utils':
            parser = self.get('path_reference_copy')
            parser.args = ['copy_set', 'report="<built-in function print>"']

        # bmesh
        if name == 'bmesh.ops':
            # 引数のthicknessが２つある
            parser = self.get('wireframe')
            parser.args = sorted(set(parser.args), key=parser.args.index)
            d = OrderedDict()
            for p in parser.params:
                if p[0] not in d:
                    d[p[0]] = p
            parser.params = list(d.values())

        # bge
        if name == 'bge.texture':
            # 定数を最初に
            self[:] = [p for p in self if isinstance(p, DataParser)] + \
                      [p for p in self if not isinstance(p, DataParser)]
            # 2.75時点ではドキュメントが未完の為、paramの記述が無い。
            # bases を args へ移動
            v = bpy.app.version
            if v[0] == 2 and v[1] == 75 and v[2] == 0:
                for parser in self:
                    if parser.type == 'class':
                        parser.args = parser.bases
                        parser.bases = []

        # 定数の値の追加。（この処理が無くても問題は無い）
        if name == 'bge.texture':
            for parser in self:
                if parser.name in bge_texture_values:
                    parser.value = bge_texture_values[parser.name]
                    if not parser.params:
                        parser.params = [['type', 'int']]
        if name == 'blf':
            blf_attrs = dir(blf)
            for parser in self:
                if isinstance(parser, DataParser):
                    if parser.name in blf_attrs:
                        value = getattr(blf, parser.name)
                        if isinstance(value, int):
                            parser.docstrings = ''
                            parser.value = str(value)
                            parser.params = [['type', 'int']]

        if name == 'gpu':
            # gpu。コロンイラネ
            parser = self.get('GPU_DYNAMIC_MIST_ENABLE:')
            if parser is not None:
                parser.name = parser.name[:-1]
            # int型の定値
            self._modify_enum_values(gpu)

        # blf.word_wrap
        if name == 'blf':
            if hasattr(blf, 'word_wrap') and self.get('word_wrap') is None:
                func = blf.word_wrap
                p = CallableParser(self, None)
                p.type = 'function'
                p.module = 'blf'
                p.name = p.fullname = func.__name__
                p.args = str(inspect.signature(func))[1: -1].split(', ')
                p.docstrings = inspect.getdoc(func)
                p.params = [
                    ['param fontid',
                     'The id of the typeface as returned by :func:`blf.load`, '
                     'for default font use 0.'],
                    ['type fontid', 'int'],
                    ['param wrap_width',
                     'The width (in pixels) to wrap words at.'],
                    ['type wrap_width', 'int'],
                ]
                self.append(p)
            if hasattr(blf, 'WORD_WRAP') and self.get('WORD_WRAP') is None:
                p = DataParser(self, None)
                p.type = 'data'
                p.module = 'blf'
                p.name = p.fullname = 'WORD_WRAP'
                p.params = [['type', 'int']]
                p.value = str(blf.WORD_WRAP)
                for i, p_ in self:
                    if p_.name == 'SHADOW':
                        self.insert(i + 1, p)
                        break

    def _parse_context(self, element):
        parser = CallableParser(self, element)
        parser.type = 'class'
        parser.module = 'bpy.types'
        parser.fullname = 'Context'
        parser.name = 'Context'
        parser.bases = ['bpy_struct']
        parser.docstrings = '\n'.join([
            'Current windowmanager and data context',
            '',
            'The context members available depend on the area of blender '
            'which is currently being accessed.',
            'Note that all context values are readonly, but may be modified '
            'through the data api or by running operators',
        ])
        for elem in element:
            if elem.tag == 'section':
                for ele in elem:
                    if ele.tag == 'title':
                        text = ['< {} >'.format(''.join(get_itertext(ele)))]
                        parser.append(CommentParser(text))
                    elif ele.tag == 'paragraph':
                        text = ''.join(get_itertext(ele)).split('\n')
                        parser.append(CommentParser(text))
                    elif ele.tag == 'desc':
                        desctype = ele.get('desctype')
                        if desctype in ('attribute', 'data'):
                            p = DataParser(parser, ele)
                            p.parse(modify=False)
                            p.type = 'data'
                            p.module = 'bpy.types'
                            p.fullname = 'Context.' + p.name
                            p.modify_type_params()

        p = CallableParser(None, None)
        p.type = 'method'
        p.module = 'bpy.types'
        p.fullname = 'Context.copy'
        p.name = 'copy'
        p.params = [['rtype', 'dict']]
        parser.append(p)

        self.append(parser)

    def _parse_desc(self, element):
        desctype = element.get('desctype')
        if desctype in ('attribute', 'data'):
            DataParser(self, element).parse()
        elif desctype in ('class', 'function', 'method',
                          'classmethod', 'staticmethod'):

            CallableParser(self, element).parse()

    def _parse_section(self, element):
        if self.name == 'bpy.context':
            self._parse_context(element)
        else:
            for elem in element:
                if elem.tag == 'section':
                    self._parse_section(elem)
                elif elem.tag == 'desc':
                    self._parse_desc(elem)

    def parse(self):
        for elem in self.tree:
            if elem.tag == 'section':
                self._parse_section(elem)
            elif elem.tag == 'desc':
                self._parse_desc(elem)
        self.modify()

    def format(self):
        text_lines = []
        prev_type = None
        for parser in self:
            if prev_type is not None:
                if CallableParser in (type(parser), prev_type):
                    text_lines.extend(['', ''])
                else:
                    text_lines.extend([''])
            text_lines.extend(parser.format())
            prev_type = type(parser)

        return text_lines


def make_xml_trees(names):
    """継承順でソートしたElementTreeが値の辞書を返す
    :rtype: OrderedDict[str, xml.etree.ElementTree]
    """

    trees = {}
    for name in names:
        print('read {}'.format(name + '.xml'))
        with open(name + '.xml', encoding='utf-8') as f:
            text = f.read()
            trees[name] = etree.fromstring(text)

    # sort
    def get_order_bpy_types(name):
        if name in ('bpy_struct', 'bpy_prop_collection'):
            s = str(['bpy_struct', 'bpy_prop_collection'].index(name))
            return 0, s
        else:
            if hasattr(bpy.types, name):
                base = getattr(bpy.types, name).bl_rna.base
                if base:
                    return get_order_bpy_types(base.identifier)[0] + 1, name
                else:
                    return 0, name
            else:
                return 99, name

    bge_order = {}
    def get_order_bge_types(name):
        if name in bge_order:
            return bge_order[name], name
        else:
            tree = trees['bge.types.' + name]
            for element in tree.findall(".//paragraph"):
                if element.text.startswith('base class ---'):
                    elem = element.find('.//literal')
                    i, _ = get_order_bge_types(elem.text)
                    bge_order[name] = i + 1
                    return bge_order[name], name
            else:
                return 0, name

    bpy_types = []
    bge_types = []
    others = []
    for name in names:
        if re.match('bpy\.types\.\w+$', name):
            bpy_types.append(name.split('.')[-1])
        elif name.startswith('bge.types.'):
            bge_types.append(name.split('.')[-1])
        else:
            others.append(name)
    bpy_types.sort(key=get_order_bpy_types)
    bge_types.sort(key=get_order_bge_types)
    sorted_names = (sorted(others) +
                    ['bpy.types.' + n for n in bpy_types] +
                    ['bge.types.' + n for n in bge_types]
                    )

    return OrderedDict([[k, trees[k]] for k in sorted_names])


def is_target_xml(name):
    if name in ('bpy', 'bpy.data', 'bpy.types', 'bge.types', 'bpy_extras',
                'freestyle'):  # 'bpy.context',
        return False
    elif name in ['change_log', 'contents', 'include__bmesh']:
        return False
    elif name.startswith('info_'):
        return False
    else:
        return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input",
                        dest="input_dir",
                        type=str,
                        default='sphinx-out',
                        help="Path of the xml files",
                        required=False)
    parser.add_argument("-o", "--output",
                        dest="output_dir",
                        type=str,
                        default='blpy',
                        help="Path of the python files",
                        required=False)
    argv = []
    if "--" in sys.argv:
        argv = sys.argv[sys.argv.index("--") + 1:]  # get all args after "--"

    args = parser.parse_args(argv)

    input = os.path.abspath(args.input_dir)
    output = os.path.abspath(args.output_dir)

    os.chdir(input)
    names = [n for n in [os.path.splitext(f)[0] for f in os.listdir('.')
                         if f.endswith('.xml')]
             if is_target_xml(n)]
    xml_trees = make_xml_trees(names)
    ls = list(xml_trees.keys())
    names.sort(key=ls.index)

    # 解析
    print('parse ...')
    parsers = OrderedDict()
    for name, tree in xml_trees.items():
        parser = ModuleParser(name, tree)
        parser.parse()
        parsers[name] = parser

    # mathutils.noise.types,distance_metricsモジュールが存在しないので追加
    # mathutils.noise.types
    parser = ModuleParser('mathutils.noise.types', None)
    parsers[parser.name] = parser
    obs = [(attr, getattr(mathutils.noise.types, attr))
           for attr in dir(mathutils.noise.types)
           if not attr.startswith('_')]
    obs = [o for o in obs if isinstance(o[1], int)]
    obs.sort(key=lambda x: x[1])
    for name, value in obs:
        p = DataParser(parser, None)
        p.type = 'data'
        p.module = 'mathutils.noise.types'
        p.name = p.fullname = name
        p.params = [['type', 'int']]
        p.value = str(value)
        parser.append(p)
    # mathutils.noise.distance_metrics
    parser = ModuleParser('mathutils.noise.distance_metrics', None)
    parsers[parser.name] = parser
    obs = [(attr, getattr(mathutils.noise.distance_metrics, attr))
           for attr in dir(mathutils.noise.distance_metrics)
           if not attr.startswith('_')]
    obs = [o for o in obs if isinstance(o[1], int)]
    obs.sort(key=lambda x: x[1])
    for name, value in obs:
        p = DataParser(parser, None)
        p.type = 'data'
        p.module = 'mathutils.noise.distance_metrics'
        p.name = p.fullname = name
        p.params = [['type', 'int']]
        p.value = str(value)
        parser.append(p)

    def test_dir(name):
        if name == 'mathutils.noise':
            return True
        is_dir = False
        for other in xml_trees:
            if other != name:
                if other.startswith(name + '.'):
                    is_dir = True
        return is_dir

    # bpy.types, bge.types
    for mod in ('bpy', 'bge'):
        out = os.path.join(output, mod, 'types.py')
        try:
            os.makedirs(os.path.dirname(out))
        except FileExistsError:
            pass
        with open(out, 'w', encoding='utf-8') as f:
            print('write {}'.format(out))
            # if mod == 'bpy':
            #     f.write('import bpy\n\n\n')
            if mod == 'bge':
                f.write('from . import logic\n')
            for name, parser in parsers.items():
                if name == 'bpy.types.Context':
                    parser = parsers['bpy.context']
                if name.startswith(mod + '.types.'):
                    # これらはblender上でオブジェクトを確認出来ない
                    if name.startswith(
                            ('bpy.types.help',
                             'bpy.types.object',
                             'bpy.types.uv',
                             'bpy.types.view3d',
                             'bpy.types.scenemassive',
                             # 'bpy.types.uvtools',
                             )):
                        continue
                    if f.tell() != 0:
                        f.write('\n\n')
                    f.write('\n'.join(parser.format()))
                    f.write('\n')

    # other
    for name, parser in parsers.items():
        if name.startswith(('bpy.context', 'bpy.types.', 'bge.types.')):
            continue
        path = os.path.join(output, *name.split('.'))
        is_dir = test_dir(name)
        if is_dir:
            dir_name = path
            out = os.path.join(path, '__init__.py')
        else:
            dir_name = os.path.dirname(path)
            out = path + '.py'
        try:
            os.makedirs(dir_name)
        except FileExistsError:
            pass
        with open(out, 'w', encoding='utf-8') as f:
            print('write {}'.format(out))
            if name == 'bpy.props':
                f.write('import sys\n\n\n')
            elif name in ('bmesh', 'bpy.utils', 'mathutils'):
                ls = [n[len(name) + 1:].split('.')[0]
                      for n in names if n.startswith(name + '.')]
                for n in sorted(set(ls), key=ls.index):
                    m = n.split('.')[0]
                    f.write('from . import {}\n'.format(m))
                if name == 'bpy.utils':
                    f.write('import bpy\n')
                elif name == 'mathutils':
                    f.write('import sys\n')
                f.write('\n\n')
            elif name == 'mathutils.noise':
                f.write('from . import types\n')
                f.write('from . import distance_metrics\n\n\n')
            elif name == 'freestyle.utils':
                f.write('from . import ContextFunctions\n')
                f.write('from freestyle.types import '
                        'StrokeVertexIterator, Interface0DIterator\n\n\n')
            elif name in ('freestyle.functions', 'freestyle.predicates'):
                f.write('from .types import IntegrationType\n\n\n')
            elif name == 'mathutils.bvhtree':
                f.write('import sys\n\n\n')

            # if name in ('bmesh.types', 'freestyle.types'):
            #     f.write('from mathutils import Vector\n\n\n')

            # 本文
            f.write('\n'.join(parser.format()))
            f.write('\n')

    # __init__.py
    out = os.path.join(output, 'bpy', '__init__.py')
    with open(out, 'w', encoding='utf-8') as f:
        print('write {}'.format(out))
        name = 'bpy'
        ls = [n[len(name) + 1:].split('.')[0]
              for n in names if n.startswith(name + '.')
              if n not in ('bpy.context', 'bpy.data')]
        for n in sorted(set(ls), key=ls.index):
            m = n.split('.')[0]
            f.write('from . import {}\n'.format(m))
        f.write('\n\n')
        f.write('context = types.Context()\n')
        f.write('data = types.BlendData()\n\n')

    out = os.path.join(output, 'bpy', 'ops', '__init__.py')
    with open(out, 'w', encoding='utf-8') as f:
        print('write {}'.format(out))
        for name in sorted(parsers):
            m = re.match('bpy\.ops\.(\w+)', name)
            if m:
                f.write('from . import {}\n'.format(m.group(1)))
        f.write('\n')

    for name in ('bpy_extras', 'bge', 'freestyle', 'idprop'):
        out = os.path.join(output, *name.split('.'))
        out = os.path.join(out, '__init__.py')
        with open(out, 'w', encoding='utf-8') as f:
            print('write {}'.format(out))
            ls = [n[len(name) + 1:].split('.')[0]  # TODO
                  for n in parsers if n.startswith(name + '.')]
            for n in sorted(set(ls)):
                f.write('from . import {}\n'.format(n))
            f.write('\n')


if __name__ == '__main__':
    main()
