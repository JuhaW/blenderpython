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


from collections import OrderedDict
import enum
# import importlib
# import inspect
import os
import math
import re

import bpy
import blf
from bpy import props

# from ..utils import addongroup
from ..utils import vaprops
from ..utils import vawm

# from . import stubs
from . import oputils
from . import operators as ops
from . import custom_icons
from .stubs import cross2d

try:
    import pie_menu
except:
    pie_menu = None


translate_iface = bpy.app.translations.pgettext_iface


class EnumItemType(enum.IntEnum):
    OPERATOR = 0
    MENU = 1
    ADVANCED = 2
    SPACER = 3


class EnumDrawType(enum.IntEnum):
    SIMPLE = 0
    BOX = 1
    CIRCLE = 2

    SIMPLE_BOX = 3
    SIMPLE_CIRCLE = 4


class EnumQuickAction(enum.IntEnum):
    NONE = 0
    LAST = 1
    FIXED = 2


class EnumHighlight(enum.IntEnum):
    NONE = 0
    LAST = 1
    FIXED = 2


all_icon_identifiers = {
    item.identifier: item.value for item in
    bpy.types.UILayout.bl_rna.functions['prop'].parameters['icon'].enum_items}


def indented_layout(layout):
    sp = layout.split(0.025)
    sp.column()
    return sp.column()


def draw_separator(layout):
    row = layout.row()
    # row.active = False  # To make the color thinner
    row.label("…" * 200)


def draw_property(layout, obj, attr, text=None, unset=False,
                  paste=False, context_attr="", active=None):
    p = obj.bl_rna.properties[attr]
    if p.type in {'BOOLEAN', 'FLOAT', 'INT'} and not p.is_array:
        split = False
    else:
        split = True
    # is_property_set() is always True if property has get function
    is_property_set = attr in obj

    row = layout.row()
    if active is not None:
        row.active = active
    else:
        if unset and not is_property_set:
            row.active = False
    if split and text != "":
        sp = row.split(1 / 3)  # 基本的にこの比率
        row1 = sp.row()
        text_ = p.name if text is None else text
        row1.label(translate_iface(text_) + ":")
        row2 = sp.row()
        row2_sub = row2.row(align=True)
        row2_sub.prop(obj, attr, text="")
    else:
        row2 = row.row()
        row2_sub = row2.row(align=True)
        kwargs = {} if text is None else {"text": text}
        row2_sub.prop(obj, attr, **kwargs)
    if paste:
        op = row2_sub.operator(ops.WM_OT_pie_menu_text_paste.bl_idname,
                               text="", icon='PASTEDOWN')
        op.data_path = context_attr + "." + attr
    if unset and is_property_set:
        row2_sub = row2.row()
        row2_sub.alignment = 'RIGHT'
        op = row2_sub.operator(ops.WM_OT_pie_menu_property_unset.bl_idname,
                               text="", icon='X', emboss=False)
        op.data = context_attr
        op.property = attr


# if "OperatorArgument" not in locals():

class _OperatorArgument:
    attrs = []

    def draw_ui(self, context, layout):
        """
        :type context: bpy.types.Context
        :type layout: bpy.types.UILayout
        """
        box = layout.box()
        box.context_pointer_set("operator_argument", self)
        row = box.row()
        sub = row.row()
        sub.prop(self, self.name)
        if self.is_property_set(self.name):
            sub = row.row()
            sub.alignment = 'RIGHT'
            op = sub.operator(ops.WM_OT_pie_menu_property_unset.bl_idname,
                              text="", icon='PANEL_CLOSE', emboss=False)
            op.data = "operator_argument"
            op.property = self.name
        else:
            box.active = False


class OperatorArgument(_OperatorArgument, bpy.types.PropertyGroup):
    pass


class ExecuteString:
    def exec_string_data(self, string, context, event):
        """data: function or str"""
        if not string:
            return None

        if event is None:
            event = oputils.events.get(context.window.as_pointer())
        kwargs = {"self": self, "context": context, "event": event}
        return oputils.execute(string, kwargs)

    def exec_string(self, key, context, event):
        string = getattr(self, key)
        if string:
            return self.exec_string_data(string, context, event)


def verify_operator_string(text):
    return re.match("\w+\.\w+$", text) is not None


def ensure_operator_args(item, clear=False):
    if not verify_operator_string(item.operator):
        return
    op_rna = oputils.get_operator_rna(item.operator)
    if not op_rna:
        return
    bl_rna = op_rna.bl_rna

    props = [p for p in bl_rna.properties if p.identifier != "rna_type"]
    if clear:
        item.operator_arguments.clear()
        for i in range(len(props)):
            item.operator_arguments.add()
    else:
        n = len(item.operator_arguments) - len(props)
        if n < 0:
            for i in range(-n):
                item.operator_arguments.add()
        for i, prop in enumerate(props):
            name = bl_rna.identifier + "." + prop.identifier
            if name in item.operator_arguments:
                j = item.operator_arguments.find(name)
                if i != j:
                    item.operator_arguments.move(j, i)
        if n > 0:
            for i in range(n):
                item.operator_arguments.remove(
                    len(item.operator_arguments) - 1)
    for arg_item, prop in zip(item.operator_arguments, props):
        # attr: e.g. "MESH_OT_delete.type"
        name = bl_rna.identifier + "." + prop.identifier
        if arg_item.name != name:
            for key in arg_item.keys():
                del arg_item[key]
        arg_item.name = name
        p = vaprops.bl_prop_to_py_prop(prop, modify_enum=True)
        setattr(OperatorArgument, name, p)


def _prop_label_get(self, key):
    if self.type in {'OPERATOR', 'ADVANCED'}:
        if key in self:
            return self[key]
        else:
            if self.type == 'OPERATOR':
                text = self.operator
                if not verify_operator_string(text):
                    return ""
            else:
                text = self.execute_string
            if text:
                op_rna = oputils.get_operator_rna(text)
                if op_rna:
                    return op_rna
        return ""
    else:
        return self.get(key, "")


def prop_label_get(self):
    result = _prop_label_get(self, "label")
    if isinstance(result, str):
        return result
    else:
        label = result.bl_rna.name
        if self.translate:
            label = translate_iface(label, "Operator")
        return label


def prop_label_set(self, value):
    self["label"] = value


def prop_description_get(self):
    result = _prop_label_get(self, "description")
    if isinstance(result, str):
        return result
    else:
        description = result.bl_rna.description
        if self.translate:
            description = translate_iface(description, "*")
        return description


def prop_description_set(self, value):
    self["description"] = value


def prop_poll_get(self):
    result = _prop_label_get(self, "poll_string")
    if isinstance(result, str):
        return result
    else:
        m, f = result.bl_rna.identifier.split("_OT_")
        return "return bpy.ops.{}.{}.poll()".format(m.lower(), f)


def prop_poll_set(self, value):
    self["poll_string"] = value


def prop_ensure_argument_get(self):
    ensure_operator_args(self)
    return "updated operator_arguments"


def prop_operator_get(self):
    if "operator" in self:
        return self["operator"]
    else:
        return ""


def prop_operator_set(self, value):
    if "operator" in self:
        if self["operator"] != value:
            self.operator_arguments.clear()
    self["operator"] = value


def prop_operator_update(self, context):
    ensure_operator_args(self)


class _PieMenuItem(ExecuteString):
    active = props.BoolProperty(
        name="Active",
        description="Activate or deactivate item",
        default=True,
    )
    show_expanded = props.BoolProperty()

    type = props.EnumProperty(
        name="Type",
        items=[('OPERATOR', "Operator", ""),
               ('MENU', "Menu", ""),
               ('ADVANCED', "Advanced", ""),
               ('SPACER', "Spacer", "")],
        default='ADVANCED',
    )

    poll_string = props.StringProperty(
        name="Poll",
        get=prop_poll_get,
        set=prop_poll_set,
    )
    execute_string = props.StringProperty(
        name="Execute",
    )

    # operator_arguments更新用
    ensure_argument = props.StringProperty(
        get=prop_ensure_argument_get,
    )

    operator = props.StringProperty(
        name="Operator",
        description="e.g. 'transform.translate'",
        get=prop_operator_get,
        set=prop_operator_set,
        update=prop_operator_update
    )
    # operator_arguments = props.CollectionProperty(
    #     type=OperatorArgument)
    operator_arguments = []  # ↑継承で上書きする場合に問題が発生する

    label = props.StringProperty(
        name="Label",
        description="Item label",
        get=prop_label_get,
        set=prop_label_set,
    )
    description = props.StringProperty(
        name="Description",
        get=prop_description_get,
        set=prop_description_set,
    )
    icon = props.StringProperty(
        name="Icon",
        description="Item icon"
    )

    menu = props.StringProperty(
        name="Menu",
    )
    undo_push = props.BoolProperty(
        name="Undo Push",
    )
    shortcut = props.StringProperty(
        "Shortcut",
    )
    translate = props.BoolProperty(
        name="Translate",
        default=True,
    )

    # 描画時に使う
    enabled = props.BoolProperty()

    @property
    def icon_box_rect(self):
        return self.get("icon_box_rect", [])

    @icon_box_rect.setter
    def icon_box_rect(self, value):
        self["icon_box_rect"] = value

    @property
    def text_box_rect(self):
        return self.get("text_box_rect", [])

    @text_box_rect.setter
    def text_box_rect(self, value):
        self["text_box_rect"] = value

    def get_execute_string(self):
        if self.type == 'OPERATOR':
            if not verify_operator_string(self.operator):
                return ""
            arg_string_list = []
            for arg in self.operator_arguments:
                if arg.name in arg:
                    value = getattr(arg, arg.name)
                    if isinstance(value, str):
                        value = "'" + value + "'"
                    else:
                        value = str(value)
                    arg_name = "".join(arg.name.split("."))[1:]
                    arg_string_list.append(arg_name + "=" + value)
            text = self.operator + "(" + ", ".join(arg_string_list) + ")"
            return text
        elif self.type == 'ADVANCED':
            return self.execute_string
        else:
            return ""

    def draw_ui(self, context, layout, menu, index, sub_item_type=""):
        if self.show_expanded:
            main_layout = layout.box().column()
        else:
            main_layout = layout.column()
        main_layout.context_pointer_set("pie_menu_item", self)

        row = main_layout.row()

        pcol = custom_icons.preview_collections["main"]

        if not sub_item_type:
            icon = 'TRIA_DOWN' if self.show_expanded else 'TRIA_RIGHT'
            sub = row.row()
            sub.alignment = 'LEFT'
            sub.prop(self, "show_expanded", text="", icon=icon, emboss=False)
            sub.prop(self, "active", text="")

            # draw direction icon

            items = {}
            i = 0
            for item in menu.menu_items:
                if item.active:
                    items[item] = i
                    i += 1
                if i == 16:
                    break

            if self not in items:
                icon = pcol["empty"]
                sub.label(text="", icon_value=icon.icon_id)
            else:
                num = len(items)
                if num <= 4:
                    num = 4
                    names = list(range(0, 16, 4))
                elif num <= 8:
                    num = 8
                    names = list(range(0, 16, 2))
                else:
                    num = 16
                    names = list(range(0, 16, 1))
                item_indices = menu.calc_item_indices(menu.item_order, num)
                name = str(names[item_indices.index(items[self])])
                icon = pcol[name]
                sub.label(text="", icon_value=icon.icon_id)

        sp = row.split(0.2)
        if not self.active:
            sp.active = False
        sub1 = sp.row()
        sp_sub = sp.split(0.5)
        sub2 = sp_sub.row()
        sub3 = sp_sub.row(align=True)
        sub3_1 = sub3.row(align=True)
        sub3_1.alignment = 'LEFT'
        sub3_2 = sub3.row(align=True)
        sub3_3 = sub3.row(align=True)

        sub1.prop(self, "type", text="")
        if self.type != 'SPACER':
            draw_property(sub2, self, "label", "", unset=True,
                          context_attr="pie_menu_item", active=True)
            if self.icon in all_icon_identifiers:
                icon_value = all_icon_identifiers[self.icon]
            elif self.icon in pcol:
                icon_value = pcol[self.icon].icon_id
            elif self.icon.endswith((".png", ".jpg")):
                try:
                    preview = pcol.load(self.icon, self.icon, 'IMAGE')
                    icon_value = preview.icon_id
                except:
                    # no exception ?
                    icon_value = pcol["empty"].icon_id
                    sub3_2.alert = True
            else:
                if self.icon:
                    sub3_2.alert = True
                icon_value = pcol["empty"].icon_id
            sub3_1.label(text="", icon_value=icon_value)
            sub3_2.prop(self, "icon", text="")
            sub3_3.operator(ops.WM_OT_pie_menu_item_icon_search.bl_idname,
                            text="", icon='VIEWZOOM')

            op = sub3_3.operator(
                ops.WM_OT_pie_menu_item_icon_file_search.bl_idname,
                text="", icon='FILE_IMAGE')
            op.display_type = 'THUMBNAIL'
            # if self.icon and os.path.exists(self.icon):
            if self.icon:
                op.filepath = self.icon

        sub = row.row(align=True)
        sub.alignment = 'RIGHT'
        sub1 = sub.row(align=True)
        op = sub1.operator(ops.WM_OT_pie_menu_item_copy.bl_idname, text="",
                           icon='COPYDOWN')
        sub2 = sub.row(align=True)
        op = sub2.operator(ops.WM_OT_pie_menu_item_paste.bl_idname, text="",
                           icon='PASTEDOWN')

        if not sub_item_type:
            # sub = row.row(align=True)
            # sub.alignment = 'RIGHT'
            sub1 = sub.row(align=True)
            op = sub1.operator(ops.WM_OT_pie_menu_item_move.bl_idname, text="",
                               icon='TRIA_UP')
            op.direction = -1
            sub2 = sub.row(align=True)
            op = sub2.operator(ops.WM_OT_pie_menu_item_move.bl_idname, text="",
                               icon='TRIA_DOWN')
            op.direction = 1

            # sub = row.row(align=True)
            # sub.alignment = 'RIGHT'
            sub.operator(ops.WM_OT_pie_menu_item_remove.bl_idname, text="",
                         icon='X')

        if not self.show_expanded:
            return

        column = main_layout.column()

        if self.type == 'SPACER':
            return
        elif self.type == 'MENU':
            column.prop(self, "menu")
        elif self.type == 'OPERATOR':
            _ = self.ensure_argument
            row = column.row()
            is_valid = verify_operator_string(self.operator)
            if self.operator != "":
                if not is_valid:
                    row.alert = True
            sub = row.row(align=True)
            sub1 = sub.row(align=True)
            if self.operator and not oputils.get_operator_rna(self.operator):
                sub1.alert = True
            sub1.prop(self, "operator")
            # 重いのでコメントアウト
            # sub.operator(ops.WM_OT_pie_menu_item_operator_search.bl_idname,
            #              text="", icon='VIEWZOOM')

            if is_valid and self.operator_arguments:
                box = column.box()
                flow = box.column_flow(2)
                for arg in self.operator_arguments:
                    arg.draw_ui(context, flow)
        else:
            draw_property(column, self, "execute_string", "Execute",
                          paste=True, context_attr="pie_menu_item")
            draw_property(column, self, "poll_string", "Poll", unset=True,
                          paste=True, context_attr="pie_menu_item",
                          active=True)

            draw_property(column, self, "description", unset=True, paste=True,
                          context_attr="pie_menu_item", active=True)
            column.prop(self, "menu")
            column.prop(self, "undo_push")
            column.prop(self, "shortcut")
            # draw_property(column, self, "translate", unset=True,
            #               context_attr="pie_menu_item")
            column.prop(self, "translate")

        for key in ["shift", "ctrl"]:
            if hasattr(self, key):
                sub_item = getattr(self, key)
                row = main_layout.row()
                icon = 'TRIA_DOWN' if sub_item.show_expanded else 'TRIA_RIGHT'
                sub = row.row()
                sub.alignment = 'LEFT'
                sub.prop(sub_item, "show_expanded", text="", icon=icon,
                         emboss=False)
                sub.prop(sub_item, "active", text="")
                sub = row.row()
                if not sub_item.active:
                    sub.active = False
                sub.label(key.title() + ":", translate=False)
                if sub_item.show_expanded:
                    column = main_layout.column()
                    col = indented_layout(column)
                    sub_item.draw_ui(context, col, menu, index,
                                     sub_item_type=key)

    def poll(self, context, event=None):
        if self.poll_string:
            return bool(self.exec_string("poll_string", context, event))
        else:
            return True

    def execute(self, context, event=None):
        if self.type == 'OPERATOR':
            text = self.get_execute_string()
            return self.exec_string_data(text, context, event)
        elif self.type == 'ADVANCED':
            return self.exec_string("execute_string", context, event)
        else:
            return None


class PieMenuSubItem(_PieMenuItem, bpy.types.PropertyGroup):
    active = props.BoolProperty(
        name="Active",
        description="Activate or deactivate item",
        default=False,
    )
    operator_arguments = props.CollectionProperty(
        type=OperatorArgument)



class PieMenuItem(_PieMenuItem, bpy.types.PropertyGroup):
    operator_arguments = props.CollectionProperty(
        type=OperatorArgument)
    shift = props.PointerProperty(type=PieMenuSubItem)
    ctrl = props.PointerProperty(type=PieMenuSubItem)


def prop_idname_get(self):
    return self.name


def prop_idname_set(self, value):
    self.name = value


def prop_draw_type_get(self):
    if "draw_type" in self:
        return self["draw_type"]
    else:
        if pie_menu and pie_menu.addon_preferences:
            draw_type = pie_menu.addon_preferences.draw_type
        else:
            draw_type = self.bl_rna.properties["draw_type"].default
        if draw_type == 'SIMPLE_BOX':
            if self.icon_scale > 1.0:
                draw_type = 'BOX'
            else:
                draw_type = 'SIMPLE'
        elif draw_type == 'SIMPLE_CIRCLE':
            if self.icon_scale > 1.0:
                draw_type = 'CIRCLE'
            else:
                draw_type = 'SIMPLE'

        return EnumDrawType[draw_type].value


def prop_draw_type_set(self, value):
    self["draw_type"] = value


def prop_radius_get(self):
    if "radius" in self:
        return self["radius"]
    else:
        if pie_menu and pie_menu.addon_preferences:
            radius = pie_menu.addon_preferences.menu_radius
        else:
            radius = self.bl_rna.properties["radius"].default
        return radius


def prop_radius_set(self, value):
    self["radius"] = value


class _PieMenu(ExecuteString):
    # {idname: index, ...}
    _last_item_index = {}

    idname = props.StringProperty(
        name="ID Name",
        get=prop_idname_get,
        set=prop_idname_set
    )

    active = props.BoolProperty(
        name="Active",
        description="Activate or deactivate menu",
        default=True
    )
    show_expanded = props.BoolProperty()

    poll_string = props.StringProperty(
        name="Poll",
        description="e.g.\nreturn context.mode == 'EDIT_MESH'",
    )
    init_string = props.StringProperty(
        name="Init",
    )

    label = props.StringProperty(
        name="Label",
        description="Menu title",
    )
    draw_type = props.EnumProperty(
        name="Draw Type",
        items=[('SIMPLE', "Simple", ""),
               ('BOX', "Box", ""),
               ('CIRCLE', "Circle", "")],
        default='BOX',
        get=prop_draw_type_get,
        set=prop_draw_type_set
    )
    icon_scale = props.FloatProperty(
        name="Icon Scale",
        default=1.0,
        min=1.0,
        max=10.0,
    )
    icon_expand = props.FloatProperty(
        name="Icon Expand",
        default=0.0,
        min=-1.0,
        max=1.0,
    )
    radius = props.IntProperty(
        name="Radius",
        description="Pie menu size in pixels",
        min=0,
        default=0,
        get=prop_radius_get,
        set=prop_radius_set
    )
    quick_action = props.EnumProperty(
        name="Quick Action",
        items=[('NONE', "None", ""),
               ('LAST', "Last", ""),
               ('FIXED', "Fixed", "")],
        default='NONE',
    )
    quick_action_index = props.IntProperty(
        name="Quick Action Index",
        description="",
        min=0,
        max=16,
        default=0,
    )
    highlight = props.EnumProperty(
        name="Highlight",
        items=[('NONE', "None", ""),
               ('LAST', "Last", ""),
               ('FIXED', "Fixed", "")],
        default='NONE',
    )
    highlight_index = props.IntProperty(
        name="Highlight Index",
        description="",
        min=0,
        max=16,
        default=0,
    )
    translate = props.BoolProperty(
        name="Translate",
        default=True,
    )

    items_num = props.EnumProperty(
        name="Number of Items",
        items=[('4', "4", ""),
               ('8', "8", ""),
               ('16', "16", "")],
        default='8',
    )
    # menu_items = props.CollectionProperty(
    #     name="Items", type=PieMenuItem)
    menu_items = []  # ↑継承で上書きする場合に問題が発生する
    item_order = props.EnumProperty(
        name="Item Order",
        items=[('CW', "Clockwise", "[0, 1, 2, 3, 4, 5, 6, 7]"),
               ('CW6', "Clockwise 6",
                "[4, 5, 6, 7, 0, 1, 2, 3] Start from six o'clock"),
               ('OFFICIAL', "Official", "[3, 5, 1, 7, 2, 6, 0, 4]"),
               ('MODIFIED', "Modified", "[3, 7, 1, 5, 2, 4, 0, 6]"),
               ],
        default='OFFICIAL',
    )

    next = props.StringProperty(
        name="Next Menu",
        description="Shortcut: wheel down",
    )
    prev = props.StringProperty(
        name="Previous Menu",
        description="Shortcut: wheel up",
    )

    # 上書き
    radius_ = props.IntProperty()
    quick_action_index_ = props.IntProperty()
    highlight_index_ = props.IntProperty()

    # 描画時に使用
    active_index = props.IntProperty(default=-1)
    active_item_index = props.IntProperty(default=-1)  # -1: None
    is_valid_click = props.BoolProperty(default=True)
    co = props.FloatVectorProperty(subtype='XYZ', size=2)
    current_items_type = props.StringProperty()  # "", "shift", "ctrl", "alt", "oskey"

    @property
    def item_boundary_angles(self):
        return self["item_boundary_angles"]

    @item_boundary_angles.setter
    def item_boundary_angles(self, value):
        self["item_boundary_angles"] = value

    @property
    def current_items(self):
        mod = self.current_items_type

        items = []
        for item in self.menu_items:
            if item.active:
                if mod == "shift" and item.shift.active:
                    items.append(item.shift)
                elif mod == "ctrl" and item.ctrl.active:
                    items.append(item.ctrl)
                else:
                    items.append(item)

        ls = []
        for i in self["current_items_indices"]:
            if i == -1:
                ls.append(None)
            else:
                item = items[i]
                if item.type == 'SPACER':
                    ls.append(None)
                else:
                    ls.append(item)
        return ls

    def poll(self, context, event=None):
        if self.poll_string:
            return bool(self.exec_string("poll_string", context, event))
        else:
            return True

    def init(self, context):
        if self.init_string:
            self.exec_string("init_string", context, None)

    @staticmethod
    def calc_item_indices(item_order, num):
        def sort_cw():
            for n in (4, 8, 16):
                if num <= n:
                    return list(range(num)) + [-1] * (n - num)

        def sort_cw6():
            indices = sort_cw()
            n = int(len(indices) / 2)
            indices = indices[n:] + indices[:n]
            return indices

        def sort_official_modified(modified=False):
            if modified:
                if num <= 4:
                    order = [3, 1, 2, 0]
                elif num <= 8:
                    order = [3, 7, 1, 5, 2, 4, 0, 6]
                else:  # if num <= 16:
                    order = [3, 15, 7, 11, 1, 9, 5, 13, 2, 12, 4, 8, 0, 10, 6,
                             14]
            else:
                if num <= 4:
                    order = [3, 1, 2, 0]
                elif num <= 8:
                    order = [3, 5, 1, 7, 2, 6, 0, 4]
                else:  # if num <= 16:
                    order = [3, 15, 5, 11, 1, 9, 7, 13, 2, 12, 6, 8, 0, 10, 4,
                             14]

            indices = list(range(num)) + [-1] * (len(order) - num)

            return [indices[i] for i in order]

        if num > 16:
            raise ValueError()
        if item_order == 'CW':
            indices = sort_cw()
        elif item_order == 'CW6':
            indices = sort_cw6()
        elif item_order == 'OFFICIAL':
            indices = sort_official_modified()
        else:  # elif self.item_order == 'MODIFIED':
            indices = sort_official_modified(True)

        return indices

    def update_current_items(self, context, op):
        mod = op.last_modifier()
        self.current_items_type = mod

        items = []
        for item in self.menu_items:
            if item.active:
                if mod == "shift" and item.shift.active:
                    items.append(item.shift)
                elif mod == "ctrl" and item.ctrl.active:
                    items.append(item.ctrl)
                else:
                    items.append(item)
        items = items[:16]

        num = len(items)
        indices = self.calc_item_indices(self.item_order, num)
        self["current_items_indices"] = indices

        # quick_action_index, highlight_index
        if num <= 4:
            n = 4
        elif num <= 8:
            n = 8
        else:  # if num <= 16:
            n = 16
        indices_ = self.calc_item_indices(self.item_order, n)
        for attr in ["quick_action_index", "highlight_index"]:
            index = getattr(self, attr)
            if 0 <= index < num:
                setattr(self, attr + "_", indices_.index(index))

        # poll()
        for i in indices:
            if i != -1:
                item = items[i]
                item.enabled = item.poll(context)

        # calc boundaries
        num = len(indices)
        pie_angle = math.pi * 2 / num
        item_boundary_angles = [[0.0, 0.0] for i in range(num)]
        current_items = self.current_items
        for i, item in enumerate(current_items):
            if not item:
                continue
            angle = math.pi * 0.5 - pie_angle * i
            if angle < -1e-5:
                angle += math.pi * 2
            # CCW side
            for k in range(1, num + 1):
                if current_items[i - k]:
                    ang = angle + pie_angle * k * 0.5
                    item_boundary_angles[i][0] = ang
                    break
            # CW side
            for k in range(1, num + 1):
                if current_items[(i + k) % num]:
                    ang = angle - pie_angle * k * 0.5
                    item_boundary_angles[i][1] = ang
                    break

        self.item_boundary_angles = item_boundary_angles

    def correct_radius(self):
        """Item同士が重ならないようにMenu半径を大きくする。
        値は redius_ に格納する
        """

        addon_prefs = pie_menu.addon_preferences
        radius = self.get("radius", addon_prefs.menu_radius)

        current_items = self.current_items
        if len(current_items) == 0:
            return

        pie_angle = math.pi * 2 / len(current_items)
        widget_unit = vawm.widget_unit()

        if self.draw_type == 'SIMPLE':
            n = len(current_items) / 4
            r = widget_unit * (n - 0.5) + addon_prefs.item_min_space * n
            self.radius_ = max(r, radius)
        else:
            icon_box_size = widget_unit * self.icon_scale
            if self.draw_type == 'CIRCLE':
                # >>> (r + icon_size / 2) * math.sin(pie_angle / 2) = \
                # (icon_size + item_min_space) / 2
                r = (icon_box_size + addon_prefs.item_min_space) / 2 / \
                    math.sin(pie_angle / 2) - icon_box_size / 2
                self.radius_ = max(r, radius)
            else:  # 'BOX'
                # >>> (r + icon_size / 2) * math.sin(pie_angle) = \
                # icon_size + item_min_space
                r = (icon_box_size + addon_prefs.item_min_space) / \
                    math.sin(pie_angle) - icon_box_size / 2
                self.radius_ = max(r, radius)

    def calc_active(self, mco):
        """:rtype: (int, int)"""
        addon_prefs = pie_menu.addon_preferences

        current_items = self.current_items

        if not current_items:
            return -1, -1

        vec = mco - self.co
        if vec.length < addon_prefs.menu_radius_center:
            active_index = -1
        else:
            idx = 0
            for i, item in enumerate(current_items):
                if not item:
                    continue
                idx = i
                a1, a2 = self.item_boundary_angles[i]
                a1 += 1e-4
                a2 -= 1e-4
                v1 = (math.cos(a1), math.sin(a1))
                v2 = (math.cos(a2), math.sin(a2))
                if cross2d(v2, vec) >= 0 and cross2d(vec, v1) >= 0:
                    active_index = i
                    break
            else:
                active_index = idx

        active_item_index = -1
        if active_index == -1:
            if self.quick_action == 'LAST':
                last_item_index = self.get_last_item_index()
                if 0 <= last_item_index < len(current_items):
                    item = current_items[last_item_index]
                    if item:
                        active_item_index = last_item_index
            elif self.quick_action == 'FIXED':
                if 0 <= self.quick_action_index_ < len(current_items):
                    item = current_items[self.quick_action_index_]
                    if item:
                        active_item_index = self.quick_action_index_
        else:
            item = current_items[active_index]
            if item:
                active_item_index = active_index

        return active_index, active_item_index

    def update_active(self, mco, mco_press):
        """active_indexとactive_itemを更新。
        """
        self.active_index, self.active_item_index = self.calc_active(mco)
        if mco_press is not None:
            i, _ = self.calc_active(mco_press)
            self.is_valid_click = i == self.active_index
        else:
            self.is_valid_click = True

    def get_last_item_index(self):
        return self._last_item_index.get(self.idname, -1)

    def set_last_item_index(self, index):
        self._last_item_index[self.idname] = index

    def clear_last_item_idnex(self):
        if self.idname in self._last_item_index:
            del self._last_item_index[self.idname]

    def draw_ui(self, context, layout):
        if self.show_expanded:
            main_layout = layout.box().column()
        else:
            main_layout = layout.column()
        main_layout.context_pointer_set("pie_menu", self)

        row = main_layout.row()
        icon = 'TRIA_DOWN' if self.show_expanded else 'TRIA_RIGHT'
        sub = row.row()
        sub.alignment = 'LEFT'
        sub.prop(self, "show_expanded", text="", icon=icon, emboss=False)
        sub.prop(self, "active", text="")
        sub = row.row()
        if not self.active:
            sub.active = False
        sub.prop(self, "label", text="")
        sub2 = sub.row()
        """:type: bpy.types.UILayout"""
        if not self.idname:
            sub2.alert = True
        sub2.prop(self, "name", text="ID Name")

        sub = row.row(align=True)
        sub.alignment = 'RIGHT'
        sub1 = sub.row(align=True)
        op = sub1.operator(ops.WM_OT_pie_menu_menu_copy.bl_idname, text="",
                           icon='COPYDOWN')
        sub2 = sub.row(align=True)
        op = sub2.operator(ops.WM_OT_pie_menu_menu_paste.bl_idname, text="",
                           icon='PASTEDOWN')
        sub1 = sub.row(align=True)
        op = sub1.operator(ops.WM_OT_pie_menu_menu_move.bl_idname, text="",
                           icon='TRIA_UP')
        op.direction = -1
        sub2 = sub.row(align=True)
        op = sub2.operator(ops.WM_OT_pie_menu_menu_move.bl_idname, text="",
                           icon='TRIA_DOWN')
        op.direction = 1
        sub.operator(ops.WM_OT_pie_menu_menu_remove.bl_idname, text="",
                     icon='X')

        if not self.show_expanded:
            return

        column = main_layout.column()

        row = column.row()
        split = row.split()
        sp_column1 = split.column()
        sp_column2 = split.column()

        draw_property(sp_column1, self, "draw_type",
                      unset=True, context_attr="pie_menu")
        draw_property(sp_column1, self, "icon_scale")
        draw_property(sp_column1, self, "icon_expand")
        draw_property(sp_column1, self, "radius",
                      unset=True, context_attr="pie_menu")

        draw_property(sp_column1, self, "translate")
        draw_property(sp_column1, self, "item_order")

        sp_column2.label("Quick Action:")
        draw_property(sp_column2, self, "quick_action", text="",
                      context_attr="pie_menu")
        sub = sp_column2.row()
        if self.quick_action != 'FIXED':
            sub.active = False
        draw_property(sub, self, "quick_action_index", context_attr="pie_menu")

        sp_column2.label("Highlight:")
        draw_property(sp_column2, self, "highlight", text="",
                      context_attr="pie_menu")
        sub = sp_column2.row()
        if self.highlight != 'FIXED':
            sub.active = False
        draw_property(sub, self, "highlight_index", context_attr="pie_menu")

        draw_separator(column)

        draw_property(column, self, "poll_string", "Poll Function", paste=True,
                      context_attr="pie_menu")
        draw_property(column, self, "init_string", "Init Function", paste=True,
                      context_attr="pie_menu")

        draw_separator(column)

        column = main_layout.column()
        for i, item in enumerate(self.menu_items):
            col = column.column()
            item.draw_ui(context, col, self, i)
        row = column.row()
        row.alignment = 'LEFT'
        op = row.operator(ops.WM_OT_pie_menu_item_add.bl_idname,
                          text="Add Item", icon='ZOOMIN')


class PieMenu(_PieMenu, bpy.types.PropertyGroup):
    menu_items = props.CollectionProperty(
        name="Items", type=PieMenuItem)

    @classmethod
    def new_class(cls):
        type("PieMenu", (_PieMenu, bpy.types.PropertyGroup), {})


def draw_menus(self, context, layout):
    menus_layout = layout.column()
    menus_layout.context_pointer_set("addon_preferences", self)

    for menu in self.menus:
        col = menus_layout.column()
        menu.draw_ui(context, col)

    row = menus_layout.row()
    sub = row.row()
    sub.alignment = 'LEFT'
    op = sub.operator(ops.WM_OT_pie_menu_menu_add.bl_idname, text="Add Menu",
                      icon='ZOOMIN')

    sub = row.row()
    sub.alignment = 'RIGHT'
    op = sub.operator(ops.WM_OT_pie_menu_menus_reset.bl_idname,
                      text="Reset Menus")


def new_classes():
    class OperatorArgument(_OperatorArgument, bpy.types.PropertyGroup):
        pass

    class PieMenuSubItem(_PieMenuItem, bpy.types.PropertyGroup):
        active = props.BoolProperty(
            name="Active",
            description="Activate or deactivate item",
            default=False,
        )
        operator_arguments = props.CollectionProperty(
            type=OperatorArgument)

    class PieMenuItem(_PieMenuItem, bpy.types.PropertyGroup):
        operator_arguments = props.CollectionProperty(
            type=OperatorArgument)
        shift = props.PointerProperty(type=PieMenuSubItem)
        ctrl = props.PointerProperty(type=PieMenuSubItem)

    namespace = OrderedDict([
        ("menu_items",
         props.CollectionProperty(name="Items", type=PieMenuItem)),
    ])
    PieMenu = type("PieMenu", (_PieMenu, bpy.types.PropertyGroup), namespace)
    return OperatorArgument, PieMenuSubItem, PieMenuItem, PieMenu
