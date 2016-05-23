# view3d_multiselect_menu.py (c) 2011 Sean Olson (liquidApe)
# Original Script by: Mariano Hidalgo (uselessdreamer)
# contributed to by: Crouch, sim88, sam, meta-androcto, Michael W and Italic_
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
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    'name': 'Multiselect Menu',
    'author': 'italic, Sean Olson (liquidApe)',
    'version': (2, 0),
    'blender': (2, 7, 6),
    'location': 'View3D > Mouse > Menu ',
    'warning': '',
    'description': 'Added options for multiselect to the ctrl-tab menu',
    'category': '3D View'}

import bpy

from bpy.types import Menu, PropertyGroup, Operator
from bpy.props import BoolProperty
from .utils import AddonPreferences


class VIEW3D_MT_Multiselect_Menu(Menu):
    """Basic list-style menu for multiselect modes."""

    bl_label = "MultiSelect Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("multi.vert",
                        text="Vertex",
                        icon='VERTEXSEL')

        layout.operator("multi.edge",
                        text="Edge",
                        icon='EDGESEL')

        layout.operator("multi.face",
                        text="Face",
                        icon='FACESEL')

        layout.separator()
        layout.operator("multi.vertedge",
                        text="Vertex/Edge",
                        icon='EDITMODE_HLT')

        layout.operator("multi.vertface",
                        text="Vertex/Face",
                        icon='ORTHO')

        layout.operator("multi.edgeface",
                        text="Edge/Face",
                        icon='SNAP_FACE')

        layout.separator()
        layout.operator("multi.vertedgeface",
                        text="Vertex/Edge/Face",
                        icon='SNAP_VOLUME')

        layout.separator()


class VIEW3D_MT_Multiselect_Menu_Pie(Menu):
    """Individual selection modes, with subpie for multiselect modes."""

    bl_label = "Multiselect Pie"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # 1 (position 4)
        pie.operator("multi.vert",
                     text="Vertex Select",
                     icon='VERTEXSEL')

        # 2 (position 6)
        pie.operator("multi.edge",
                     text="Edge Select",
                     icon='EDGESEL')

        # 3 (position 2)
        pie.operator("multi.face",
                     text="Face Select",
                     icon='FACESEL')

        # 4 (position 8)
        pie.operator("wm.call_menu_pie",
                     text="Multiselect",
                     icon='FACESEL').name = "MultiPie"


class MultiPie(Menu):
    """Subpie for multiple selection modes."""

    bl_label = "Multiselect Options"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # 1 (position 4)
        pie.operator("multi.vertedge",
                     text="Vertex/Edge",
                     icon='EDITMODE_HLT')

        # 2 (position 6)
        pie.operator("multi.vertface",
                     text="Vertex/Face",
                     icon='ORTHO')

        # 3 (position 2)
        pie.operator("multi.edgeface",
                     text="Edge/Face",
                     icon='SNAP_FACE')

        # 4 (position 8)
        pie.operator("multi.vertedgeface",
                     text="Vert/Edge/Face",
                     icon='SNAP_VOLUME')


class SelModeVert(Operator):
    """Vertex select mode."""

    bl_idname = "multi.vert"
    bl_label = "Vertex Select Mode"

    def execute(self, context):
        wm = bpy.ops.wm
        wm.context_set_value(data_path="tool_settings.mesh_select_mode",
                             value="(True, False, False)")
        return {'FINISHED'}


class SelModeEdge(Operator):
    """Edge select mode."""

    bl_idname = "multi.edge"
    bl_label = "Edge Select Mode"

    def execute(self, context):
        wm = bpy.ops.wm
        wm.context_set_value(data_path="tool_settings.mesh_select_mode",
                             value="(False, True, False)")
        return {'FINISHED'}


class SelModeFace(Operator):
    """Face select mode."""

    bl_idname = "multi.face"
    bl_label = "Face Select Mode"

    def execute(self, context):
        wm = bpy.ops.wm
        wm.context_set_value(data_path="tool_settings.mesh_select_mode",
                             value="(False, False, True)")
        return {'FINISHED'}


class SelModeVertEdge(Operator):
    """Vertex and edge select mode."""

    bl_idname = "multi.vertedge"
    bl_label = "Vert/Edge Select Mode"

    def execute(self, context):
        wm = bpy.ops.wm
        wm.context_set_value(data_path="tool_settings.mesh_select_mode",
                             value="(True, True, False)")
        return {'FINISHED'}


class SelModeVertFace(Operator):
    """Vertex and face select mode."""

    bl_idname = "multi.vertface"
    bl_label = "Vert/Face Select Mode"

    def execute(self, context):
        wm = bpy.ops.wm
        wm.context_set_value(data_path="tool_settings.mesh_select_mode",
                             value="(True, False, True)")
        return {'FINISHED'}


class SelModeEdgeFace(Operator):
    """Edge and face select mode."""

    bl_idname = "multi.edgeface"
    bl_label = "Edge/Face Select Mode"

    def execute(self, context):
        wm = bpy.ops.wm
        wm.context_set_value(data_path="tool_settings.mesh_select_mode",
                             value="(False, True, True)")
        return {'FINISHED'}


class SelModeVertEdgeFace(Operator):
    """Vertex, edge and face select mode."""

    bl_idname = "multi.vertedgeface"
    bl_label = "Vert/Edge/Face Select Mode"

    def execute(self, context):
        wm = bpy.ops.wm
        wm.context_set_value(data_path="tool_settings.mesh_select_mode",
                             value="(True, True, True)")
        return {'FINISHED'}


def update_Prefs(self, context):
    """Function to toggle keymaps and menu style."""
    wm = bpy.context.window_manager
    km = wm.keyconfigs.user.keymaps['Mesh']

    if wm.keyconfigs.user:
        # Multiselect Pie
        if self.pie_toggle:
            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu' and \
                        kmi.properties.name == "VIEW3D_MT_Multiselect_Menu":
                    km.keymap_items.remove(kmi)
                    break

            # Multiselect_Menu
            kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS', ctrl=True)
            kmi.properties.name = "VIEW3D_MT_Multiselect_Menu_Pie"

        else:
            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu_pie' and \
                        kmi.properties.name == "VIEW3D_MT_Multiselect_Menu_Pie":
                    km.keymap_items.remove(kmi)
                    break

            # Multiselect_Menu
            kmi = km.keymap_items.new('wm.call_menu', 'TAB', 'PRESS', ctrl=True)
            kmi.properties.name = "VIEW3D_MT_Multiselect_Menu"


class MultiSelectPreferences(
        AddonPreferences, PropertyGroup,
        bpy.types.AddonPreferences):
    """Addon preferences displayed in the user preferences after activation."""

    bl_idname = __name__

    pie_toggle = BoolProperty(
        name="Use Pie",
        description="Toggle between pie-style and classic list-style menus",
        default=False,
        update=update_Prefs)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(self, "pie_toggle")


classes = [
    VIEW3D_MT_Multiselect_Menu,
    VIEW3D_MT_Multiselect_Menu_Pie,
    MultiPie,
    MultiSelectPreferences,
    SelModeVert,
    SelModeEdge,
    SelModeFace,
    SelModeVertEdge,
    SelModeVertFace,
    SelModeEdgeFace,
    SelModeVertEdgeFace,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    wm = bpy.context.window_manager
    km = wm.keyconfigs.user.keymaps['Mesh']

    # remove default keybinding
    for kmi in km.keymap_items:
        if kmi.idname == 'wm.call_menu' and \
                kmi.properties.name == "VIEW3D_MT_edit_mesh_select_mode":
            km.keymap_items.remove(kmi)
            break

    # add multiselect keybinding
    kmi = km.keymap_items.new('wm.call_menu', 'TAB', 'PRESS', ctrl=True)
    kmi.properties.name = "VIEW3D_MT_Multiselect_Menu"


def unregister():
    for cls in classes[::-1]:
        bpy.utils.unregister_class(cls)

    wm = bpy.context.window_manager
    km = wm.keyconfigs.user.keymaps['Mesh']

    # remove multiselect keybinding
    for kmi in km.keymap_items:
        if kmi.idname == 'wm.call_menu_pie' or kmi.idname == 'wm.call_menu':
            if kmi.properties.name == "VIEW3D_MT_Multiselect_Menu_Pie" or \
                    kmi.properties.name == "VIEW3D_MT_Multiselect_Menu":
                km.keymap_items.remove(kmi)
                continue

    # replace default keymap
    kmi = km.keymap_items.new('wm.call_menu', 'TAB', 'PRESS', ctrl=True)
    kmi.properties.name = "VIEW3D_MT_edit_mesh_select_mode"


if __name__ == "__main__":
    register()
