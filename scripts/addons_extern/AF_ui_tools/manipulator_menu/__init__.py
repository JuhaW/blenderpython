# re creating the functionality of the manipulator menu from 2.49
#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANSPACEILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "3d View: Manipulator Menu",
    "author": "MichaelW",
    "version": (1, 2, 1),
    "blender": (2, 61, 0),
    "location": "View3D > Ctrl Space ",
    "description": "Menu to change the manipulator type and/or disable it",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/"
                "Scripts/3D_interaction/Manipulator_Menu",
    "tracker_url": "https://developer.blender.org/T22092",
    "category": "3D View"}

import bpy
from bpy.props import BoolProperty, EnumProperty, StringProperty
from .utils import AddonPreferences, SpaceProperty


def main(context):
    bpy.context.space_data.manipulator = False


class ManipListMenu(bpy.types.Menu):
    bl_label = "ManipulatorType"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        props = layout.operator("view3d.enable_manipulator",text ='Translate', icon='MAN_TRANS')
        props.translate = True

        props = layout.operator("view3d.enable_manipulator",text ='Rotate', icon='MAN_ROT')
        props.rotate = True

        props = layout.operator("view3d.enable_manipulator",text ='Scale', icon='MAN_SCALE')
        props.scale = True
        layout.separator()

        props = layout.operator("view3d.enable_manipulator",text ='Combo', icon='MAN_SCALE')
        props.scale = True
        props.rotate = True
        props.translate = True

        layout.separator()

        props = layout.operator("view3d.enable_manipulator",text ='Hide', icon='MAN_SCALE')
        props.scale = False
        props.rotate = False
        props.translate = False

        layout.separator()


class ManipEnum(bpy.types.Operator):
    """Copy of Antony/Sergey's manip pie from official pie addon."""

    bl_label = "Set Manipulator"
    bl_idname = "manip.enum"
    bl_options = {'INTERNAL'}

    type = EnumProperty(
        name="Type",
        items=(('TRANSLATE', "Translate", "Use the manipulator for movement transformations"),
               ('ROTATE', "Rotate", "Use the manipulator for rotation transformations"),
               ('SCALE', "Scale", "Use the manipulator for scale transformations"),
               ),
        )

    def execute(self, context):
        # show manipulator if user selects an option
        context.space_data.show_manipulator = True

        context.space_data.transform_manipulators = {self.type}

        return {'FINISHED'}


class ManipPieMenu(bpy.types.Menu):
    """New pie-style menu, copied from Antony/Sergey's official pie addon."""

    bl_label = "ManipulatorType"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator("manip.enum", text="Translate", icon='MAN_TRANS').type = 'TRANSLATE'
        pie.operator("manip.enum", text="Rotate", icon='MAN_ROT').type = 'ROTATE'
        pie.operator("manip.enum", text="Scale", icon='MAN_SCALE').type = 'SCALE'
        pie.prop(context.space_data, "show_manipulator")


# =============================================================================
#  USER PREFERENCES
# =============================================================================

def update_prefs(self, context):
    """Function to toggle keymaps and menu style."""
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if wm.keyconfigs.addon:
        for km in addon_keymaps:
            for kmi in km.keymap_items:
                km.keymap_items.remove(kmi)

            wm.keyconfigs.addon.keymaps.remove(km)

    addon_keymaps.clear()

    if kc:
        # Manip Pie
        if self.use_pie_prop:
            km = wm.keyconfigs.active.keymaps['Object Non-modal']

            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu':
                    if kmi.properties.name == "ManipListMenu":
                        km.keymap_items.remove(kmi)
                        break

            # Manip Menu
            kmi = km.keymap_items.new('wm.call_menu_pie', 'SPACE', 'PRESS', ctrl=True)
            kmi.properties.name = "ManipPieMenu"

        else:
            km = wm.keyconfigs.active.keymaps['Object Non-modal']

            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu_pie':
                    if kmi.properties.name == "ManipPieMenu":
                        km.keymap_items.remove(kmi)
                        break

            # Multiselect_Menu
            kmi = km.keymap_items.new('wm.call_menu', 'SPACE', 'PRESS', ctrl=True)
            kmi.properties.name = "ManipListMenu"


class ManipPreferences(
        AddonPreferences,
        bpy.types.PropertyGroup,
        bpy.types.AddonPreferences):
    """Addon preferences displayed in the user preferences after activation."""

    bl_idname = __name__

    use_pie_prop = BoolProperty(
        name="Toggle Pie",
        description="Toggle between pie-style menu and classic list-style menu",
        default=False,
        update=update_prefs)

    def draw(self, context):
        layout = self.layout
        col = layout.column()

        col.prop(self, "use_pie_prop")


classes = [
    ManipListMenu,
    ManipEnum,
    ManipPieMenu,
    ManipPreferences
    ]


addon_keymaps = []


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    wm = bpy.context.window_manager

    # Remove default keymaps
    for kmi in wm.keyconfigs.active.keymaps['3D View'].keymap_items:
        if kmi.idname == 'wm.context_toggle':
            if kmi.properties.data_path == "space_data.show_manipulator":
                wm.keyconfigs.active.keymaps['3D View'].keymap_items.remove(kmi)
                break

    for kmi in wm.keyconfigs.active.keymaps['Object Non-modal'].keymap_items:
        if kmi.idname == 'wm.call_menu_pie':
            if kmi.properties.name == "VIEW3D_PIE_manipulator":
                wm.keyconfigs.active.keymaps['Object Non-modal'].keymap_items.remove(kmi)
                break

    # add new manip keybinding
    km = wm.keyconfigs.active.keymaps['Object Non-modal']
    kmi = km.keymap_items.new('wm.call_menu', 'SPACE', 'PRESS', ctrl=True)
    kmi.properties.name = "ManipListMenu"


def unregister():
    for cls in classes[::-1]:
        bpy.utils.unregister_class(cls)
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps['Object Non-modal']

    for kmi in km.keymap_items:
        if kmi.idname == 'wm.call_menu':
            if kmi.properties.name == "ManipListMenu":
                km.keymap_items.remove(kmi)
                break

    for kmi in km.keymap_items:
        if kmi.idname == 'wm.call_menu_pie':
            if kmi.properties.name == "ManipPieMenu":
                km.keymap_items.remove(kmi)
                break

    km = wm.keyconfigs.addon.keymaps['3D View']
    kmi = km.keymap_items.new('wm.context_toggle', 'SPACE', 'PRESS', ctrl=True)
    kmi.properties.data_path = "space_data.show_manipulator"

    km = wm.keyconfigs.addon.keymaps['Object Non-modal']
    kmi = km.keymap_items.new('wm.call_menu_pie', 'SPACE', 'PRESS', ctrl=True)
    kmi.properties.name = "VIEW3D_PIE_manipulator"


if __name__ == "__main__":
    register
