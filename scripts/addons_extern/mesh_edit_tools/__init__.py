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
    "name": "Edit Tools",
    "author": "various",
    "version": (0, 1),
    "blender": (2, 71, 0),
    "location": "View3D > Toolshelf > Addons Tab & Specials (W-key)",
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

import bpy

class VIEW3D_MT_edit_mesh_extras(bpy.types.Menu):
    # Define the "Extras" menu
    bl_idname = "VIEW3D_MT_edit_mesh_extras"
    bl_label = "Edit Tools"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator("object.mextrude",
            text="Multi Extrude")
        layout.operator("faceinfillet.op0_id",
            text="Face Inset Fillet")
        layout.operator("mesh.add_faces_to_object",
            text="PKHG Faces")
        layout.operator("fillet.op0_id",
            text="Edge Fillet Plus")
        layout.operator("mesh.offset_edges",
            text="Offset Edges")
        layout.operator("mesh.vertex_chamfer",
            text="Vertex Chamfer")
        layout.operator("mesh.edge_roundifier",
            text="Edge Roundify")
        layout.operator("mesh.ext_cut_faces",
            text="Cut Faces")
        layout.operator("sp_sol.op0_id",
            text="Split Solidify")
        layout.operator("bpt.mesh_to_wall",
            text="Edge(s) to Wall")
        layout.operator("object.mesh_edge_length_set",
            text="Set Edge Length")



class ExtrasPanel(bpy.types.Panel):
    bl_label = 'Mesh Edit Tools'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = 'mesh_edit'
    bl_category = 'Tools'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Face Tools:", icon="FACESEL")
        row = layout.split(0.70)
        row.operator('object.mextrude', text = 'Multi Extrude')
        row.operator('help.mextrude', text = '', icon = 'INFO')
        row = layout.split(0.70)
        row.operator('faceinfillet.op0_id', text = 'Inset Fillet')
        row.operator('help.face_inset', text = '', icon = 'INFO')
        row = layout.split(0.70)
        row.operator('mesh.add_faces_to_object', text = 'Face Extrude')
        row.operator('help.pkhg', text = '', icon = 'INFO')
        row = layout.split(0.70)
        row.operator('mesh.ext_cut_faces', text = 'Cut Faces')
        row.operator('help.cut_faces', text = '', icon = 'INFO')
        row = layout.row()
        row.operator('sp_sol.op0_id', text = 'Split Solidify')
        row = layout.row()
        row.label(text="Edge Tools:", icon="EDGESEL")
        row = layout.split(0.70)
        row.operator('fillet.op0_id', text = 'Fillet plus')
        row.operator('help.edge_fillet', text = '', icon = 'INFO')
        row = layout.split(0.70)
        row.operator('mesh.offset_edges', text = 'Offset Edges')
        row.operator('help.offset_edges', text = '', icon = 'INFO')
        row = layout.split(0.70)
        row.operator('mesh.edge_roundifier', text = 'Roundify')
        row.operator('help.roundify', text = '', icon = 'INFO')
        row = layout.row()
        row.operator('object.mesh_edge_length_set', text = 'Set Edge Length')
        row = layout.row()
        row.operator('bpt.mesh_to_wall', text = 'Extrude Flat')
        row = layout.row()
        row.label(text="Vert Tools:", icon="VERTEXSEL")
        row = layout.split(0.70)
        row.operator('mesh.vertex_chamfer', text = 'Chamfer')
        row.operator('help.vertexchamfer', text = '', icon = 'INFO')
        row = layout.row()
        row.label(text="Utilities:")
        row = layout.row()
        row.operator('mesh.flip_normals', text = 'Normals Flip')
        row = layout.row()
        row.operator('mesh.remove_doubles', text = 'Remove Doubles')

'''
# Multi Extrude Panel

class ExtrudePanel(bpy.types.Panel):
    bl_label = 'Multi Extrude Plus'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Addons'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        row = layout.split(0.80)
        row.operator('object.mextrude', text = 'Multi Face Extrude')
        row.operator('help.mextrude', text = '', icon = 'INFO')
        row = layout.split(0.80)
        row.operator('object.mesh2bones', text = 'Add Armature')
        row.operator('help.addarm', text = '', icon = 'INFO')
'''

# Define "Extras" menu
def menu_func(self, context):
    self.layout.menu('VIEW3D_MT_edit_mesh_extras', icon='PLUGIN')


def register():
    bpy.utils.register_module(__name__)

    # Add "Extras" menu to the "Add Mesh" menu
    bpy.types.VIEW3D_MT_edit_mesh_specials.append(menu_func)


def unregister():
    bpy.utils.unregister_module(__name__)

    # Remove "Extras" menu from the "Add Mesh" menu.
    bpy.types.VIEW3D_MT_edit_mesh_specials.remove(menu_func)

if __name__ == "__main__":
    register()
