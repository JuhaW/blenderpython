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
# Contributed to by
# meta-androcto #

bl_info = {
    "name": "AF: Edit Tools",
    "author": "various",
    "version": (0, 1),
    "blender": (2, 76, 0),
    "location": "View3D > Toolshelf > Tools & Specials (W-key)",
    "description": "Add extra mesh edit tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Addon Factory"}


if "bpy" in locals():
    import importlib
    importlib.reload(face_inset_fillet)
    importlib.reload(mesh_filletplus)
    importlib.reload(mesh_vertex_chamfer)
    importlib.reload(mesh_mextrude_plus)
    importlib.reload(mesh_offset_edges)
    importlib.reload(pkhg_faces)
    importlib.reload(mesh_edge_roundifier)
    importlib.reload(mesh_cut_faces)
    importlib.reload(split_solidify)
    importlib.reload(mesh_to_wall)
    importlib.reload(mesh_edges_length)
    importlib.reload(random_vertices)
    importlib.reload(mesh_fastloop)

else:
    from . import face_inset_fillet
    from . import mesh_filletplus
    from . import mesh_vertex_chamfer
    from . import mesh_mextrude_plus
    from . import mesh_offset_edges
    from . import pkhg_faces
    from . import mesh_edge_roundifier
    from . import mesh_cut_faces
    from . import split_solidify
    from . import mesh_to_wall
    from . import mesh_edges_length
    from . import random_vertices
    from . import mesh_fastloop

import bpy
from bpy.props import BoolProperty
### ------ MENUS ====== ###


class VIEW3D_MT_edit_mesh_extras(bpy.types.Menu):
    # Define the "Extras" menu
    bl_idname = "VIEW3D_MT_edit_mesh_extras"
    bl_label = "Edit Tools"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        mode = context.tool_settings.mesh_select_mode
        if mode[0]:
            split = layout.split()
            col = split.column()
            col.label(text="Vert")
            col.operator("mesh.vertex_chamfer",
                         text="Vertex Chamfer")
            col.operator("mesh.random_vertices",
                         text="Random Vertices")

            row = split.row(align=True)
            col = split.column()
            col.label(text="Utilities")
            col.operator("object_ot.fastloop",
                         text="Fast loop")
            col.operator('mesh.flip_normals', text='Normals Flip')
            col.operator('mesh.remove_doubles', text='Remove Doubles')
            col.operator('mesh.subdivide', text='Subdivide')
            col.operator('mesh.dissolve_limited', text='Dissolve Limited')

        elif mode[1]:
            split = layout.split()
            col = split.column()
            col.label(text="Edge")
            col.operator("fillet.op0_id",
                         text="Edge Fillet Plus")
            col.operator("mesh.offset_edges",
                         text="Offset Edges")
            col.operator("mesh.edge_roundifier",
                         text="Edge Roundify")
            col.operator("object.mesh_edge_length_set",
                         text="Set Edge Length")
            col.operator("bpt.mesh_to_wall",
                         text="Edge(s) to Wall")

            row = split.row(align=True)
            col = split.column()
            col.label(text="Utilities")
            col.operator("object_ot.fastloop",
                         text="Fast loop")
            col.operator('mesh.flip_normals', text='Normals Flip')
            col.operator('mesh.remove_doubles', text='Remove Doubles')
            col.operator('mesh.remove_doubles', text='Remove Doubles')
            col.operator('mesh.subdivide', text='Subdivide')
            col.operator('mesh.dissolve_limited', text='Dissolve Limited')

        elif mode[2]:
            split = layout.split()
            col = split.column()
            col.label(text="Face")
            col.operator("object.mextrude",
                         text="Multi Extrude")
            col.operator("faceinfillet.op0_id",
                         text="Face Inset Fillet")
            col.operator("mesh.add_faces_to_object",
                         text="PKHG Faces")
            col.operator("mesh.ext_cut_faces",
                         text="Cut Faces")
            col.operator("sp_sol.op0_id",
                         text="Split Solidify")

            row = split.row(align=True)
            col = split.column()
            col.label(text="Utilities")
            col.operator("object_ot.fastloop",
                         text="Fast loop")
            col.operator('mesh.flip_normals', text='Normals Flip')
            col.operator('mesh.remove_doubles', text='Remove Doubles')
            col.operator('mesh.subdivide', text='Subdivide')
            col.operator('mesh.dissolve_limited', text='Dissolve Limited')

class EditToolsPanel(bpy.types.Panel):
    bl_label = 'Mesh Edit Tools'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = 'mesh_edit'
    bl_category = 'Tools'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        scene = context.scene
        VERTDROP = scene.UTVertDrop
        EDGEDROP = scene.UTEdgeDrop
        FACEDROP = scene.UTFaceDrop
        UTILSDROP = scene.UTUtilsDrop
        view = context.space_data
        toolsettings = context.tool_settings
        layout = self.layout

        # Vert options
        box1 = self.layout.box()
        col = box1.column(align=True)
        row = col.row(align=True)
        row.prop(scene, "UTVertDrop", icon="TRIA_DOWN")
        if not VERTDROP:
            row.menu("VIEW3D_MT_Select_Vert", icon="VERTEXSEL", text="")
        if VERTDROP:
            row = col.row(align=True)
            row.alignment = 'CENTER'
            row.label(text="Vert Tools:", icon="VERTEXSEL")
            row = layout.split(0.70)
            row.operator('mesh.vertex_chamfer', text='Chamfer')
            row.operator('help.vertexchamfer', text='?')
            row = layout.split(0.70)
            row.operator('mesh.random_vertices', text='Random Vertices')
            row.operator('help.random_vert', text='?')

        # Edge options
        box1 = self.layout.box()
        col = box1.column(align=True)
        row = col.row(align=True)
        row.prop(scene, "UTEdgeDrop", icon="TRIA_DOWN")
        if not EDGEDROP:
            row.menu("VIEW3D_MT_Select_Edge", icon="EDGESEL", text="")
        if EDGEDROP:
            layout = self.layout
            row = layout.row()
            row.label(text="Edge Tools:", icon="EDGESEL")
            row = layout.split(0.70)
            row.operator('fillet.op0_id', text='Fillet plus')
            row.operator('help.edge_fillet', text='?')
            row = layout.split(0.70)
            row.operator('mesh.offset_edges', text='Offset Edges')
            row.operator('help.offset_edges', text='?')
            row = layout.split(0.70)
            row.operator('mesh.edge_roundifier', text='Roundify')
            row.operator('help.roundify', text='?')
            row = layout.split(0.70)
            row.operator('object.mesh_edge_length_set', text='Set Edge Length')
            row.operator('help.roundify', text='?')
            row = layout.split(0.70)
            row.operator('bpt.mesh_to_wall', text='Mesh to wall')
            row.operator('help.wall', text='?')

        # Face options
        box1 = self.layout.box()
        col = box1.column(align=True)
        row = col.row(align=True)
        row.prop(scene, "UTFaceDrop", icon="TRIA_DOWN")

        if not FACEDROP:
            row.menu("VIEW3D_MT_Select_Face", icon="FACESEL", text="")

        if FACEDROP:
            layout = self.layout
            row = layout.row()
            row.label(text="Face Tools:", icon="FACESEL")
            row = layout.split(0.70)
            row.operator('object.mextrude', text='Multi Extrude')
            row.operator('help.mextrude', text='?')
            row = layout.split(0.70)
            row.operator('faceinfillet.op0_id', text='Inset Fillet')
            row.operator('help.face_inset', text='?')
            row = layout.split(0.70)
            row.operator('mesh.add_faces_to_object', text='Face Extrude')
            row.operator('help.pkhg', text='?')
            row = layout.split(0.70)
            row.operator('mesh.ext_cut_faces', text='Cut Faces')
            row.operator('help.cut_faces', text='?')
            row = layout.split(0.70)
            row.operator('sp_sol.op0_id', text='Split Solidify')
            row.operator('help.solidify', text='?')

        # Utils options
        box1 = self.layout.box()
        col = box1.column(align=True)
        row = col.row(align=True)
        row.prop(scene, "UTUtilsDrop", icon="TRIA_DOWN")

        if not UTILSDROP:
            row.menu("VIEW3D_MT_Edit_MultiMET", icon="LOOPSEL", text="")

        if UTILSDROP:
            layout = self.layout
            row = layout.row()
            row.label(text="Utilities:")
            row = layout.row()
            row = layout.split(0.70)
            row.operator('object_ot.fastloop', text='Fast Loop')
            row.operator('help.random_vert', text='?')
            row = layout.row()
            row.operator('mesh.flip_normals', text='Normals Flip')
            row = layout.row()
            row.operator('mesh.remove_doubles', text='Remove Doubles')
            row = layout.row()
            row.operator('mesh.subdivide', text='Subdivide')
            row = layout.row()
            row.operator('mesh.dissolve_limited', text='Dissolve Limited')


# ********** Edit Multiselect **********
class VIEW3D_MT_Edit_MultiMET(bpy.types.Menu):
    bl_label = "Multi Select"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        prop = layout.operator("wm.context_set_value", text="Vertex Select",
                               icon='VERTEXSEL')
        prop.value = "(True, False, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Edge Select",
                               icon='EDGESEL')
        prop.value = "(False, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Face Select",
                               icon='FACESEL')
        prop.value = "(False, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Vertex & Edge Select",
                               icon='EDITMODE_HLT')
        prop.value = "(True, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Vertex & Face Select",
                               icon='ORTHO')
        prop.value = "(True, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Edge & Face Select",
                               icon='SNAP_FACE')
        prop.value = "(False, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Vertex & Edge & Face Select",
                               icon='SNAP_VOLUME')
        prop.value = "(True, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

class VIEW3D_MT_Select_Vert(bpy.types.Menu):
    bl_label = "Select Vert"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        prop = layout.operator("wm.context_set_value", text="Vertex Select",
                               icon='VERTEXSEL')
        prop.value = "(True, False, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Vertex & Edge Select",
                               icon='EDITMODE_HLT')
        prop.value = "(True, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Vertex & Face Select",
                               icon='ORTHO')
        prop.value = "(True, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

class VIEW3D_MT_Select_Edge(bpy.types.Menu):
    bl_label = "Select Edge"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        prop = layout.operator("wm.context_set_value", text="Edge Select",
                               icon='EDGESEL')
        prop.value = "(False, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Vertex & Edge Select",
                               icon='EDITMODE_HLT')
        prop.value = "(True, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Edge & Face Select",
                               icon='SNAP_FACE')
        prop.value = "(False, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

class VIEW3D_MT_Select_Face(bpy.types.Menu):
    bl_label = "Select Face"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        prop = layout.operator("wm.context_set_value", text="Face Select",
                               icon='FACESEL')
        prop.value = "(False, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Vertex & Face Select",
                               icon='ORTHO')
        prop.value = "(True, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Edge & Face Select",
                               icon='SNAP_FACE')
        prop.value = "(False, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

# Addons Preferences

class AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        layout = self.layout
        layout.label(text="----Mesh Edit Tools----")
        layout.label(text="Collection of extra Mesh Edit Functions")
        layout.label(text="Edit Mode toolshelf or W key specials")

# Define "Extras" menu


def menu_func(self, context):
    self.layout.menu('VIEW3D_MT_edit_mesh_extras', icon='PLUGIN')


def register():
    bpy.types.Scene.UTVertDrop = bpy.props.BoolProperty(
        name="Vert",
        default=False,
        description="Vert Tools")
    bpy.types.Scene.UTEdgeDrop = bpy.props.BoolProperty(
        name="Edge",
        default=False,
        description="Edge Tools")
    bpy.types.Scene.UTFaceDrop = bpy.props.BoolProperty(
        name="Face",
        default=False,
        description="Face Tools")
    bpy.types.Scene.UTUtilsDrop = bpy.props.BoolProperty(
        name="Utils",
        default=False,
        description="Misc Utils")
    bpy.utils.register_module(__name__)
    wm = bpy.context.window_manager

    # Add "Extras" menu to the "Add Mesh" menu
    bpy.types.VIEW3D_MT_edit_mesh_specials.append(menu_func)


def unregister():
    del bpy.types.Scene.UTVertDrop
    del bpy.types.Scene.UTEdgeDrop
    del bpy.types.Scene.UTFaceDrop
    del bpy.types.Scene.UTUtilsDrop
    wm = bpy.context.window_manager
    bpy.utils.unregister_module(__name__)

    # Remove "Extras" menu from the "Add Mesh" menu.
    bpy.types.VIEW3D_MT_edit_mesh_specials.remove(menu_func)


if __name__ == "__main__":
    register()
