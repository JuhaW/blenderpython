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
    "name": "Sculpt Brushes (Sculpt: D, C, S, G)",
    # "description": "",
    # "category": "User Interface"
}


from types import MethodType

import bpy

# import piemenus


class Empty:
    pass


class EmptyMenu:
    def __init__(self, context):
        pass


class SculptBrushDraw:
    idname = "sculpt_brush_draw"
    label = "Brush Select"
    quick_action = 'FIXED'
    quick_action_index = 0
    icon_scale = 2.5
    icon_expand = 1.0
    radius = 0
    item_order = 'OFFICIAL'

    brush_types = ['DRAW', 'CLAY', 'CLAY_STRIPS', 'INFLATE', 'BLOB',
                   'LAYER', 'CREASE']

    keymap_items = [["Sculpt", {"type": 'D', "value": 'PRESS'}]]

    @classmethod
    def gen_submenu(cls, context, sculpt_tool, sculpt_tool_name):
        menu = type("SubMenu", (EmptyMenu,), {})
        menu.idname = "sculpt_brush_submenu_" + sculpt_tool
        menu.label = sculpt_tool_name
        menu.quick_action = 'FIXED'
        menu.radius = cls.radius
        menu.icon_scale = cls.icon_scale
        menu.icon_expand = cls.icon_expand
        menu.item_order = cls.item_order
        brushes = [b for b in bpy.data.brushes if b.use_paint_sculpt and
                   b.sculpt_tool == sculpt_tool]
        brush = context.tool_settings.sculpt.brush
        if brush in brushes:
            i = brushes.index(brush)
        else:
            i = 0
        menu.quick_action_index = i
        menu.items = []
        for brush in brushes:
            if sculpt_tool == 'DRAW':
                icon = 'BRUSH_SCULPT_DRAW'
            else:
                icon = 'BRUSH_' + sculpt_tool
            item = Empty()
            item.label = brush.name
            item.icon = icon
            item.execute = ('brush = bpy.data.brushes[self.label]\n'
                            'context.tool_settings.sculpt.brush = brush')
            menu.items.append(item)
        return menu

    def __init__(self, context):
        self.items = []
        self.menus = {}

        def execute(self, context, event):
            if not self.menu or event.type not in (
                    'LEFTMOUSE', 'SPACE', 'RET', 'NUMPAD_ENTER'):
                bpy.ops.paint.brush_select(
                    True, paint_mode='SCULPT',
                    sculpt_tool=self.sculpt_tool)
                self.menu = ""

        prop = bpy.types.Brush.bl_rna.properties['sculpt_tool']
        for brush_type in self.brush_types:
            enum_item = prop.enum_items[brush_type]
            item = Empty()
            item.label = enum_item.name
            item.description = "Release key: decide, Press LeftMouse: sub menu"
            item.icon = enum_item.icon
            item.sculpt_tool_name = enum_item.name
            item.sculpt_tool = enum_item.identifier
            item.main_menu = self
            item.execute = MethodType(execute, item)

            num = 0
            for brush in bpy.data.brushes:
                if (brush.use_paint_sculpt and
                        brush.sculpt_tool == enum_item.identifier):
                    num += 1
            if num > 1:
                dyn_menu = self.gen_submenu(
                    context, enum_item.identifier,  enum_item.name)
                piemenus.register_menu(__name__, dyn_menu)
                dyn_menus[dyn_menu.idname] = dyn_menu
                item.menu = dyn_menu.idname
            else:
                item.menu = ""

            self.items.append(item)

        while len(self.items) % 4:
            self.items.append(None)


class SculptBrushClay(SculptBrushDraw):
    idname = "sculpt_brush_clay"
    quick_action_index = 1

    keymap_items = [["Sculpt", {"type": 'C', "value": 'PRESS'}]]


class SculptBrushSmooth(SculptBrushDraw):
    idname = "sculpt_brush_smooth"
    quick_action_index = 0

    brush_types = ['SMOOTH', 'FLATTEN', 'FILL', 'SCRAPE', 'PINCH']

    keymap_items = [["Sculpt", {"type": 'S', "value": 'PRESS'}]]


class SculptBrushGrub(SculptBrushDraw):
    idname = "sculpt_brush_grub"
    quick_action_index = 0

    brush_types = ['GRAB', 'ROTATE', 'THUMB', 'SNAKE_HOOK', 'NUDGE', 'MASK']

    keymap_items = [["Sculpt", {"type": 'G', "value": 'PRESS'}]]


pie_menus = [
    SculptBrushDraw,
    SculptBrushClay,
    SculptBrushSmooth,
    SculptBrushGrub,
]

dyn_menus = {}


keymap_items = []


def register():
    # piemenus.register_addon()

    # for menu in pie_menus:
    #     if hasattr(menu, "keymap_items"):
    #         for km_name, kwargs in menu.keymap_items:
    #             km = piemenus.get_keymap(km_name)
    #             if km:
    #                 kmi = km.keymap_items.new("wm.pie_menu", **kwargs)
    #                 kmi.properties.menu = menu.idname
    #                 keymap_items.append((km, kmi))
    pass


def unregister():
    # piemenus.unregister_addon()

    for km, kmi in keymap_items:
        km.keymap_items.remove(kmi)
    keymap_items.clear()
