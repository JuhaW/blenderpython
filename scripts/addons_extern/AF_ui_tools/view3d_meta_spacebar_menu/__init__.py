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
    "name": "Meta Spacebar Menu",
    "author": "mkbreuer",
    "version": (0, 1, 1),
    "blender": (2, 7, 2),
    "location": "View3D / Key:",
    "description": "Meta Spacebar Menus",
    "warning": "",
    "wiki_url": "",
    "category": "User Menu",
}


import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'view3d_meta_spacebar_menu'))


if "bpy" in locals():
    import imp

    imp.reload(view3d_spacebar_main_menu)
    imp.reload(view3d_spacebar_file_menu)

    imp.reload(view3d_spacebar_view_camera_menu)
    imp.reload(view3d_spacebar_window_menu)

    imp.reload(view3d_spacebar_3dview_menu)
    imp.reload(view3d_spacebar_object_mesh_menu)

    imp.reload(view3d_spacebar_align_menu)
    imp.reload(view3d_spacebar_modifier_menu)

    imp.reload(view3d_spacebar_curve_surface_menu)
    imp.reload(view3d_spacebar_delete_clear_menu)

    imp.reload(view3d_spacebar_edge_visual_menu)
    imp.reload(view3d_spacebar_edges_edit_menu)

    imp.reload(view3d_spacebar_face_edit_menu)
    imp.reload(view3d_spacebar_face_visual_menu)

    imp.reload(view3d_spacebar_vertices_edit_menu)
    imp.reload(view3d_spacebar_selection_menu)

    imp.reload(view3d_spacebar_special_menu)

    print("Reloaded multifiles")


else:
    from . import view3d_spacebar_main_menu, view3d_spacebar_file_menu, view3d_spacebar_special_menu
    from . import view3d_spacebar_view_camera_menu, view3d_spacebar_window_menu, view3d_spacebar_3dview_menu, view3d_spacebar_object_mesh_menu
    from . import view3d_spacebar_align_menu, view3d_spacebar_modifier_menu, view3d_spacebar_curve_surface_menu, view3d_spacebar_delete_clear_menu
    from . import view3d_spacebar_edge_visual_menu, view3d_spacebar_edges_edit_menu, view3d_spacebar_face_edit_menu, view3d_spacebar_face_visual_menu
    from . import view3d_spacebar_vertices_edit_menu, view3d_spacebar_selection_menu

    print("Imported multifiles")


import view3d_spacebar_main_menu
import view3d_spacebar_file_menu

import view3d_spacebar_view_camera_menu
import view3d_spacebar_window_menu

import view3d_spacebar_3dview_menu
import view3d_spacebar_object_mesh_menu

import view3d_spacebar_align_menu
import view3d_spacebar_modifier_menu

import view3d_spacebar_curve_surface_menu
import view3d_spacebar_delete_clear_menu

import view3d_spacebar_edge_visual_menu
import view3d_spacebar_edges_edit_menu

import view3d_spacebar_face_edit_menu
import view3d_spacebar_face_visual_menu

import view3d_spacebar_vertices_edit_menu
import view3d_spacebar_selection_menu

import view3d_spacebar_special_menu

import bpy


def register():

    view3d_spacebar_main_menu.register()
    view3d_spacebar_file_menu.register()

    view3d_spacebar_view_camera_menu.register()
    view3d_spacebar_window_menu.register()

    view3d_spacebar_3dview_menu.register()
    view3d_spacebar_object_mesh_menu.register()

    view3d_spacebar_align_menu.register()
    view3d_spacebar_modifier_menu.register()

    view3d_spacebar_curve_surface_menu.register()
    view3d_spacebar_delete_clear_menu.register()

    view3d_spacebar_edge_visual_menu.register()
    view3d_spacebar_edges_edit_menu.register()

    view3d_spacebar_face_edit_menu.register()
    view3d_spacebar_face_visual_menu.register()

    view3d_spacebar_vertices_edit_menu.register()
    view3d_spacebar_selection_menu.register()

    view3d_spacebar_special_menu.register()

    bpy.utils.register_module(__name__)


def unregister():

    view3d_spacebar_main_menu.unregister()
    view3d_spacebar_file_menu.unregister()

    view3d_spacebar_view_camera_menu.unregister()
    view3d_spacebar_window_menu.unregister()

    view3d_spacebar_3dview_menu.unregister()
    view3d_spacebar_object_mesh_menu.unregister()

    view3d_spacebar_align_menu.unregister()
    view3d_spacebar_modifier_menu.unregister()

    view3d_spacebar_curve_surface_menu.unregister()
    view3d_spacebar_delete_clear_menu.unregister()

    view3d_spacebar_edge_visual_menu.unregister()
    view3d_spacebar_edges_edit_menu.unregister()

    view3d_spacebar_face_edit_menu.unregister()
    view3d_spacebar_face_visual_menu.unregister()

    view3d_spacebar_vertices_edit_menu.unregister()
    view3d_spacebar_selection_menu.unregister()

    view3d_spacebar_special_menu.unregister()

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
