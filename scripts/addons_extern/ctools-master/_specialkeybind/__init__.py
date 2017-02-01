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


bl_info = {
    'name': 'Special Keybind',
    'author': 'chromoly',
    'version': (0, 0, 1),
    'blender': (2, 78, 0),
    'location': '',
    'description': '',
    'warning': '',
    'wiki_url': '',
    'category': 'User Interface'
}


import ctypes as ct
import os
import traceback
import types

import bpy

try:
    importlib.reload(addongroup)
    importlib.reload(registerinfo)
    importlib.reload(structures)
except NameError:
    from ..utils import addongroup
    from ..utils import registerinfo
    from ..utils import structures
from .. import listvalidkeys


USE_CTRL = True

FILE_NAME = 'special_keybind.py'


class LeftSelectionHelperPreferences(
    addongroup.AddonGroupPreferences,
    registerinfo.AddonRegisterInfo,
    bpy.types.PropertyGroup if '.' in __name__ else
    bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        file_path = os.path.join(bpy.utils.user_resource('CONFIG'),
                                 FILE_NAME)
        row.label('Config File: {}'.format(file_path), translate=False)

        split = layout.split()
        col = split.column()
        col.operator(SCREEN_OT_edit_keybind.bl_idname, text='Edit')

        col = split.column()
        col = split.column()

        self.layout.separator()
        super().draw(context)


template_docstring = \
"""\"\"\"
有効な修飾キー:
    any, shift, ctrl, alt, oskey
有効なイベントタイプ:
    https://www.blender.org/api/blender_python_api_2_78a_release/bpy.types.Event.html#bpy.types.Event.type
終了用のキー:
    ESC, ctrl + G, ctrl + SPACE / shift + SPACE

keybind = {キーマップ名: [[キー, オペレーター[, 引数[, 最後にだけ一致]]], ...], ...}
\"\"\"

"""
template_keybind = \
"""keybind = {{
    '*': [
        ['ESC', '{idname}', {{}}, True],
        ['ctrl + G', '{idname}', {{}}, True],
        ['any + RIGHTMOUSE', '{idname}', {{}}, True],
    ],

    'Window': [
        ['S', 'wm.search_menu'],
    ],
    'Screen': [
        ['F', 'screen.screen_full_area'],
    ],
    '3D View': [
        ['S', 'wm.call_menu', {{'name': 'VIEW3D_MT_Space_Dynamic_Menu'}}],
        ['G', 'transform.translate'],  # test
    ],

}}
"""


def get_template():
    return template_docstring + template_keybind.format(
        idname=SCREEN_OT_special_keybind.bl_idname)


class SCREEN_OT_edit_keybind(bpy.types.Operator):
    """User Preferencesのボタンから起動。TextObjectを作る"""
    bl_idname = 'screen.edit_keybind'
    bl_label = 'Edit Keybind'
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        file_path = os.path.join(bpy.utils.user_resource('CONFIG'),
                                 FILE_NAME)

        for text in bpy.data.texts:
            if text.filepath == file_path:
                break
        else:
            try:
                with open(file_path, 'a', encoding='utf-8'):
                    pass
            except:
                traceback.print_exc()
                return {'CANCELLED'}
            text = bpy.data.texts.load(file_path)

        self.report({'INFO'}, "See '{}' in the text editor".format(FILE_NAME))

        # write template
        if not text.as_string().strip():
            text.clear()
            text.write(template)

        return {'FINISHED'}


def event_to_srting(event):
    if isinstance(event, bpy.types.Event):
        event_type = event.type
        mods = event.shift, event.ctrl, event.alt, event.oskey
    else:
        event_type, mods = event

    enum_items = bpy.types.Event.bl_rna.properties['type'].enum_items
    names = {e.identifier: e.name for e in enum_items}

    keys = []
    for name, enable in zip(['Shift', 'Ctrl', 'Alt', 'OSKey'], mods):
        if enable:
            keys.append(name)
    keys.append(names[event_type])
    return ' + '.join(keys)


# def info_header_draw(self, context):
#     win_key = context.window.as_pointer()
#     if win_key not in SCREEN_OT_special_keybind.operators:
#         info_header_draw._draw(self, context)
#         return
#
#     layout = self.layout
#
#     row = layout.row(align=True)
#     row.template_header()
#
#     op = SCREEN_OT_special_keybind.operators[win_key]
#     text = ', '.join([event_to_srting(ev) for ev in op.key_history])
#     row = layout.row()
#     if text:
#         row.label(text, translate=False)
#     else:
#         if USE_CTRL:
#             row.label('Exit: Ctrl + G / Ctrl + Space / ESC')
#         else:
#             row.label('Exit: Ctrl + G / Shift + Space / ESC')


class SCREEN_OT_special_keybind(bpy.types.Operator):
    bl_idname = 'screen.special_keybind'
    bl_label = 'Special Keybind'
    bl_options = {'REGISTER', 'GRAB_CURSOR', 'BLOCKING'}

    operators = {}

    @classmethod
    def kill(cls):
        for op in cls.operators.values():
            op.terminate = True
        cls.operators.clear()

    @classmethod
    def register(cls):
        def fget(self):
            win_key = bpy.context.window.as_pointer()
            return win_key in cls.operators

        bpy.types.WindowManager.use_special_keybind = bpy.props.BoolProperty(
            name='Special Keybind',
            get=fget
        )

    @classmethod
    def unregister(cls):
        del bpy.types.WindowManager.use_special_keybind
        cls.operators.clear()

    def __init__(self):
        self.op_key = ('NONE', (False,) * 4)  # 起動時のショートカット
        self.config = None
        self.key_history = []
        self.terminate = False

    def cancel(self, context):
        win_key = bpy.context.window.as_pointer()
        if win_key in self.operators:
            del self.operators[win_key]
        self.redraw_info(context)

    def redraw_info(self, context):
        for area in context.screen.areas:
            if area.type == 'INFO':
                break
        else:
            return

        win_key = context.window.as_pointer()
        if win_key not in SCREEN_OT_special_keybind.operators:
            area.header_text_set()
            area.tag_redraw()
            return

        enum_items = bpy.types.Event.bl_rna.properties['type'].enum_items
        event_type_names = {elem.identifier: elem.name for elem in enum_items}

        op = SCREEN_OT_special_keybind.operators[win_key]
        text_list = []
        for event_type, modifiers in op.key_history:
            keys = []
            for i, name in enumerate(['shift', 'ctrl', 'alt', 'oskey']):
                if modifiers[i]:
                    keys.append(name)
            # keys.append(event_type_names[event_type])
            keys.append(event_type)
            text_list.append(' + '.join(keys))
        text = ', '.join(text_list)
        area.header_text_set('>>> ' + text)
        area.tag_redraw()

    def get_active_area_region(self, context, event):
        win = context.window
        x, y = event.mouse_x, event.mouse_y
        for area in context.screen.areas:
            if area.x <= x < area.x + area.width:
                if area.y <= y < area.y + area.height:
                    for region in area.regions:
                        if region.x <= x < region.x + region.width:
                            if region.y <= y < region.y + region.height:
                                return area, region
        return None, None

    def set_active_area_region(self, context, area, region):
        """
        :type context: bpy.types.Context
        :type area: bpy.types.Area
        :type region: bpy.types.Region
        :rtype: (bpy.types.Area, bpy.types.Region)
        """
        py_dict_bak = structures.context_py_dict_set(context, None)
        area_bak = context.area
        region_bak = context.region

        ctx_p = ct.cast(context.as_pointer(), ct.POINTER(structures.bContext))
        ctx = ctx_p.contents
        if area:
            ctx.wm.area = ct.cast(area.as_pointer(),
                                  ct.POINTER(structures.ScrArea))
        else:
            ctx.wm.area = None
        if region:
            ctx.wm.region = ct.cast(region.as_pointer(),
                                    ct.POINTER(structures.ARegion))
        else:
            ctx.wm.region = None

        if region:
            win_p = ctx.wm.window
            if win_p:
                win = win_p.contents
                event = win.eventstate.contents
                event.mval[0] = event.x - region.x
                event.mval[1] = event.y - region.y

        structures.context_py_dict_set(context, py_dict_bak)
        return area_bak, region_bak

    def format_event(self, event):
        modifiers = [False] * 4
        for i, attr in enumerate(['shift', 'ctrl', 'alt', 'oskey']):
            if getattr(event, attr):
                modifiers[i] = True
        return [event.type, modifiers]

    def modal(self, context, event):
        wm = context.window_manager
        win_key = bpy.context.window.as_pointer()

        if self.terminate or win_key not in self.operators:
            self.cancel(context)
            return {'FINISHED'}

        if event.type in {'MOUSEMOVE', 'INBETWEEN_MOUSEMOVE'}:
            return {'PASS_THROUGH'}

        if event.type in {'LEFT_SHIFT', 'RIGHT_SHIFT', 'LEFT_CTRL',
                          'RIGHT_CTRL', 'LEFT_ALT', 'RIGHT_ALT',
                          'OSKEY'}:
            return {'RUNNING_MODAL'}
        if event.value != 'PRESS':
            return {'RUNNING_MODAL'}

        current_key = self.format_event(event)

        # 起動時と同じキーを押したら終了
        # if current_key == self.op_key:
        #     self.cancel(context)

        self.key_history.append(current_key)

        self.redraw_info(context)

        area, region = self.get_active_area_region(context, event)
        area_bak, region_bak = self.set_active_area_region(
            context, area, region)

        def is_matched(history, keys, options):
            import itertools

            if history == keys:
                return True

            only_last = False
            if options and len(options) == 2:
                only_last = options[1]
            if only_last:
                history = history[-1:]

            for hist, op_key in itertools.zip_longest(
                    history, keys, fillvalue=None):
                if hist is None:
                    return False
                elif op_key[0] != hist[0]:
                    return False
                elif op_key[1] is None:  # 'any'
                    continue
                elif op_key[1] != hist[1]:
                    return False
            return True

        finish = False

        items = []
        if '*' in self.config:
            items.extend(self.config['*'])
        for km in listvalidkeys.context_keymaps(context):
            if not listvalidkeys.keymap_poll(context, km):
                continue
            if km.name in self.config:
                items.extend(self.config[km.name])

        for key, idname, *options in items:
            if not is_matched(self.key_history, key, options):
                continue
            mod, func = idname.split('.')
            op = getattr(getattr(bpy.ops, mod), func)
            if op.poll():
                if options:
                    kwargs = options[0]
                    result = op('INVOKE_DEFAULT', **kwargs)
                else:
                    result = op('INVOKE_DEFAULT')
                if 'PASS_THROUGH' not in result:
                    finish = True
                    break

        # オペレーターで変更されなかった場合に元に戻す
        if context.area == area and context.region == region:
            self.set_active_area_region(context, area_bak, region_bak)

        if finish or self.terminate or win_key not in self.operators:
            self.cancel(context)
            return {'FINISHED'}

        return {'RUNNING_MODAL'}

    def get_config(self):
        file_path = os.path.join(bpy.utils.user_resource('CONFIG'), FILE_NAME)
        found = True
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        except:
            found = False
            # traceback.print_exc()

        config = None
        if found:
            mod = types.ModuleType('tmp')
            error = False
            try:
                exec(text, mod.__dict__)
            except:
                traceback.print_exc()
                error = True
            if not error and 'keybind' in mod.__dict__:
                if isinstance(mod.keybind, dict):
                    config = mod.keybind

        if not config:
            mod = types.ModuleType('tmp')
            text = get_template()
            exec(text, mod.__dict__)
            config = mod.keybind

        # 書式を揃える
        for name in list(config.keys()):
            config[name] = [list(item) for item in config[name]]
        for items in config.values():
            for item in items:
                keys = item[0]
                key_elems = []
                for s in keys.strip().split(','):
                    ls = [t.strip() for t in s.strip().split('+')]
                    modifiers = [t.lower() for t in ls[:-1]]
                    if 'any' in modifiers:
                        modifiers_ = None
                    else:
                        modifiers_ = [False] * 4
                        for i, m in enumerate(
                                ['shift', 'ctrl', 'alt', 'oskey']):
                            if m in modifiers:
                                modifiers_[i] = True
                    key_elems.append([ls[-1].upper(), modifiers_])
                item[0] = key_elems

        return config

    def invoke(self, context, event):
        if context.area.type in {'CONSOLE', 'TEXT_EDITOR'}:
            op_key = self.format_event(event)
            if op_key == ['SPACE', [False, False, False, False]]:
                return {'CANCELLED', 'PASS_THROUGH'}

        wm = context.window_manager
        win_key = context.window.as_pointer()
        if win_key in self.operators:
            self.cancel(context)
            return {'FINISHED'}
        else:
            self.operators[win_key] = self
            mod = event.shift, event.ctrl, event.alt, event.oskey
            self.op_key = self.format_event(event)
            self.config = self.get_config()
            wm.modal_handler_add(self)
            self.redraw_info(context)
            return {'RUNNING_MODAL'}


# class VIEW3D_OT_toggle_manipulator_active(bpy.types.Operator):
#     bl_idname = 'view3d.toggle_manipulator_active'
#     bl_label = 'Toggle Manipulator'
#
#     handle_size = 0.25
#     active = False
#
#     def execute(self, context):
#         cls = self.__class__
#
#         U = bpy.context.user_preferences
#         if cls.active:
#             U.view.manipulator_handle_size = cls.handle_size
#         else:
#             cls.handle_size = U.view.manipulator_handle_size
#         cls.active ^= True
#
#         # return bpy.ops.view3d.manipulator(context.copy(), 'INVOKE_DEFAULT')


def add_keymaps():
    context = bpy.context

    # Space Menu
    km = LeftSelectionHelperPreferences.get_keymap('Window')
    km.keymap_items.new('wm.search_menu', 'SPACE', 'PRESS', ctrl=True, alt=True)

    km = LeftSelectionHelperPreferences.get_keymap('3D View')
    kmi = km.keymap_items.new('wm.call_menu', 'SPACE', 'PRESS', ctrl=True,
                              alt=True)
    kmi.properties.name = 'VIEW3D_MT_Space_Dynamic_Menu'

    # Manipulator Toggle
    km = LeftSelectionHelperPreferences.get_keymap('3D View')
    kmi = km.keymap_items.new('view3d.toggle_manipulator_active', 'SPACE',
                              'PRESS')

    # Selection
    km = LeftSelectionHelperPreferences.get_keymap('Clip Editor')
    km.keymap_items.new('clip.select', 'SELECTMOUSE', 'PRESS', alt=True)

    # km = LeftSelectionHelperPreferences.get_keymap('Mask Editing')
    # km.keymap_items.new('mask.slide_point', 'SELECT_MOUSE', 'PRESS')
    # km.keymap_items.new('mask.slide_spline_curvature', 'SELECT_MOUSE', 'PRESS')

    # # Cursor
    # km = LeftSelectionHelperPreferences.get_keymap('Paint Curve')
    # kmi = km.keymap_items.new('paintcurve.cursor', 'ACTION_MOUSE', 'PRESS', alt=True)
    # km = LeftSelectionHelperPreferences.get_keymap('3D View')
    # kmi = km.keymap_items.new('view3d.cursor3d', 'ACTION_MOUSE', 'PRESS', alt=True)
    # km = LeftSelectionHelperPreferences.get_keymap('UV Editor')
    # kmi = km.keymap_items.new('uv.cursor_set', 'ACTION_MOUSE', 'PRESS', alt=True)
    # km = LeftSelectionHelperPreferences.get_keymap('Mask Editing')
    # kmi = km.keymap_items.new('uv.cursor_set', 'ACTION_MOUSE', 'PRESS',
    #                           alt=True)
    # km = LeftSelectionHelperPreferences.get_keymap('Graph Editor')
    # kmi = km.keymap_items.new('graph.cursor_set', 'ACTION_MOUSE', 'PRESS',
    #                           alt=True)
    # km = LeftSelectionHelperPreferences.get_keymap('Clip Editor')
    # kmi = km.keymap_items.new('clip.cursor_set', 'ACTION_MOUSE', 'PRESS',
    #                           alt=True)


@bpy.app.handlers.persistent
def replace_keymap_items(scene):
    # keyconfigs = bpy.context.window_manager.keyconfigs
    # for kc in [keyconfigs.active, keyconfigs.addon]:
    #     if not USE_CTRL or not kc:
    #         continue
    #     for km in kc.keymaps:
    #         if km.is_modal:
    #             continue
    #         for kmi in km.keymap_items:
    #             if kmi.idname == SCREEN_OT_special_keybind.bl_idname:
    #                 continue
    #             if kmi.type == 'SPACE' and kmi.value == 'PRESS':
    #                 mod = kmi.any, kmi.shift, kmi.ctrl, kmi.alt, kmi.oskey
    #                 if mod == (False, True, False, False, False):
    #                     if kmi.active:
    #                         kmi.active = False
    #                         disable_keymap_items.append((km, kmi))
    #                 elif mod == (False, False, True, False, False):
    #                     kmi.shift = True
    #                     kmi.ctrl = False
    #                     edited_keymap_items.append((km, kmi))
    bpy.app.handlers.scene_update_pre.remove(replace_keymap_items)


classes = [
    LeftSelectionHelperPreferences,
    SCREEN_OT_special_keybind,
    SCREEN_OT_edit_keybind,
    # VIEW3D_OT_toggle_manipulator_active,
]


disable_keymap_items = []
edited_keymap_items = []


@LeftSelectionHelperPreferences.register_addon
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    # add_keymaps()

    # U = bpy.context.user_preferences
    # VIEW3D_OT_toggle_manipulator_active.handle_size = \
    #     U.view.manipulator_handle_size

    km = LeftSelectionHelperPreferences.get_keymap('Screen Editing')
    if km:
        if USE_CTRL:
            kmi = km.keymap_items.new(SCREEN_OT_special_keybind.bl_idname,
                                      'SPACE', 'PRESS', ctrl=True)
        else:
            kmi = km.keymap_items.new(SCREEN_OT_special_keybind.bl_idname,
                                      'SPACE', 'PRESS', shift=True)
    bpy.app.handlers.scene_update_pre.append(replace_keymap_items)


@LeftSelectionHelperPreferences.unregister_addon
def unregister():
    for cls in classes[::-1]:
        bpy.utils.unregister_class(cls)

    U = bpy.context.user_preferences
    # U.view.manipulator_handle_size = \
    #     VIEW3D_OT_toggle_manipulator_active.handle_size

    if replace_keymap_items in bpy.app.handlers.scene_update_pre:
        bpy.app.handlers.scene_update_pre.append(replace_keymap_items)

    for km, kmi in disable_keymap_items:
        kmi.active = True
    disable_keymap_items.clear()
    for km, kmi in edited_keymap_items:
        kmi.shift = False
        kmi.ctrl = True
    edited_keymap_items.clear()
