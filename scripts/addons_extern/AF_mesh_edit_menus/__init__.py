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
# by meta-androcto, parts based on work by Erich Toven #

bl_info = {
    "name": "AF: Edit Mesh Menu's",
    "author": "Meta Androcto, ",
    "version": (0, 2),
    "blender": (2, 75, 0),
    "location": "View3D > Edit Mesh Menu's",
    "description": "View3D > Edit Mesh Menu's",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6"\
        "/Py/Scripts",
    "tracker_url": "",
    "category": "Addon Factory"}


if "bpy" in locals():
    import importlib
    importlib.reload(VIEW3D_MT_edit_mesh)
    importlib.reload(VIEW3D_MT_edit_mesh_delete)
    importlib.reload(VIEW3D_MT_edit_mesh_showhide)
    importlib.reload(VIEW3D_MT_edit_mesh_vertices)
    importlib.reload(VIEW3D_MT_select_edit_mesh)


else:
    from . import VIEW3D_MT_edit_mesh
    from . import VIEW3D_MT_edit_mesh_delete
    from . import VIEW3D_MT_edit_mesh_showhide
    from . import VIEW3D_MT_edit_mesh_vertices
    from . import VIEW3D_MT_select_edit_mesh

import bpy
# Addons Preferences
class AddonPreferences(bpy.types.AddonPreferences):
	bl_idname = __name__
	
	def draw(self, context):
		layout = self.layout
		layout.label(text="----Mesh Edit Menu's----")
		layout.label(text="Experimental extra Functions in the edit mesh menu's")
		layout.label(text="New features have the Plugin icon")
		layout.label(text="Mesh, Select, Show Hide & more ")

def register():
    bpy.utils.register_module(__name__)
    # Add "Extras" menu to the "Add Mesh" menu
    bpy.types.VIEW3D_MT_edit_mesh.append(VIEW3D_MT_edit_mesh.menu)
    bpy.types.VIEW3D_MT_edit_mesh_delete.append(VIEW3D_MT_edit_mesh_delete.menu)
    bpy.types.VIEW3D_MT_edit_mesh_showhide.append(VIEW3D_MT_edit_mesh_showhide.menu)
    bpy.types.VIEW3D_MT_edit_mesh_vertices.append(VIEW3D_MT_edit_mesh_vertices.menu)
    bpy.types.VIEW3D_MT_select_edit_mesh.append(VIEW3D_MT_select_edit_mesh.menu)


def unregister():
	bpy.utils.unregister_module(__name__)
    # Remove "Extras" menu from the "Add Mesh" menu.
	bpy.types.VIEW3D_MT_edit_mesh.remove(VIEW3D_MT_edit_mesh.menu)
	bpy.types.VIEW3D_MT_edit_mesh_delete.remove(VIEW3D_MT_edit_mesh_delete.menu)
	bpy.types.VIEW3D_MT_edit_mesh_showhide.remove(VIEW3D_MT_edit_mesh_showhide.menu)
	bpy.types.VIEW3D_MT_edit_mesh_vertices.remove(VIEW3D_MT_edit_mesh_vertices.menu)
	bpy.types.VIEW3D_MT_select_edit_mesh.remove(VIEW3D_MT_select_edit_mesh.menu)


if __name__ == "__main__":
    register()
