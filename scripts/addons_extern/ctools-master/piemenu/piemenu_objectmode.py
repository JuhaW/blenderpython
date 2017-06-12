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
    "name": "Object Mode (Object Non-modal: TAB)",
    # "description": "",
    # "category": "User Interface"
}


import inspect

import bpy

from ..utils import addongroup

import pie_menu


class PieMenuObjectModeSetAddonPreferences(
    pie_menu.PieMenuPreferences, addongroup.AddonGroup,
        bpy.types.PropertyGroup):
    bl_idname = __name__

    def reset_menus(self):
        self.menus.clear()
        self.menus.add()
        p = self["menus"][0]
        p.update(object_mode)

    def draw(self, context):
        pie_menu.PieMenuPreferences.draw(self, context)
        addongroup.AddonGroup.draw(self, context)


def init(self, context):
    self.menu_items.clear()
    # order = {'OBJECT': 0,
    #          'EDIT': 4,
    #          'POSE': 2,
    #          'SCULPT': 1,
    #          'VERTEX_PAINT': 5,
    #          'WEIGHT_PAINT': 6,
    #          'TEXTURE_PAINT': 2,
    #          'PARTICLE_EDIT': 3,
    #          'GPENCIL_EDIT': 7,
    #          }

    def get_enum_items(obj, prop_name):
        prop = obj.bl_rna.properties[prop_name]
        return list(prop.enum_items)

    actob = context.active_object

    i = 0
    for enum_item in get_enum_items(bpy.types.Object, 'mode'):
        if enum_item.identifier == 'POSE':
            if not (actob and actob.type == 'ARMATURE'):
                continue
        elif enum_item.identifier == 'EDIT':
            if not (actob and actob.type in (
                    'MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE',
                    'LATTICE')):
                continue
        elif enum_item.identifier in ('SCULPT', 'VERTEX_PAINT',
                                      'WEIGHT_PAINT', 'TEXTURE_PAINT'):
            if not (actob and actob.type == 'MESH'):
                continue
        elif enum_item.identifier == 'GPENCIL_EDIT':
            if not context.gpencil_data:
                continue
        elif enum_item.identifier == 'PARTICLE_EDIT':
            use_particle = False
            if actob:
                if actob.particle_systems:
                    use_particle = True
                else:
                    for mod in actob.modifiers:
                        if mod.type in ('CLOTH', 'SOFT_BODY'):
                            use_particle = True
                            break
            if not use_particle:
                continue

        item = self.menu_items.add()
        item.label = enum_item.name
        item.icon = enum_item.icon
        text = "object.mode_set(mode='{}', toggle=True)"
        item.execute_string = text.format(enum_item.identifier)
        item["mode"] = enum_item.identifier

        i += 1

    if context.object:
        if context.object.type in ('EMPTY', 'CAMERA', 'LAMP', 'SPEAKER'):
            self.quick_action_index = 0
        else:
            for i, item in enumerate(self.menu_items):
                if item["mode"] == 'EDIT':
                    self.quick_action_index = i
                    break


object_mode = {
    "name": "object_mode",
    "label": "Object Mode",
    "quick_action": pie_menu.EnumQuickAction['FIXED'],
    "init_string":
        "\n".join([t[4:] for t in inspect.getsource(init).split("\n")[1:]])
}


menu_keymap_items = {
    "object_mode": [["Object Non-modal", {"type": 'TAB', "value": 'PRESS'}]]
}


classes = [
    PieMenuObjectModeSetAddonPreferences
]


@PieMenuObjectModeSetAddonPreferences.register_addon
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    addon_prefs = PieMenuObjectModeSetAddonPreferences.get_instance()
    if "menus" not in addon_prefs:
        addon_prefs.reset_menus()

    pie_menu.register_addon(addon_prefs)

    for idname, km_items in menu_keymap_items.items():
        for km_name, kwargs in km_items:
            km = pie_menu.get_keymap(km_name)
            if km:
                kmi = km.keymap_items.new("wm.pie_menu", **kwargs)
                kmi.properties.menu = idname


@PieMenuObjectModeSetAddonPreferences.unregister_addon
def unregister():
    addon_prefs = PieMenuObjectModeSetAddonPreferences.get_instance()
    pie_menu.unregister_addon(addon_prefs)
    for cls in classes[::-1]:
        bpy.utils.unregister_class(cls)
