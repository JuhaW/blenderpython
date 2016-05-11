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
    "name": "MetaTool ",
    "author": "mkbreuer / multi authors for addon",
    "version": (0, 1, 6),
    "blender": (2, 7, 4),
    "location": "View3D",
    "description": "Collection of addons from far and wide, criss and cross",
    "warning": "use with your own risk, can become addictive",
    "wiki_url": "http://www.blenderartists.org/forum/forumdisplay.php?48-Released-Scripts-and-Themes",
    "category": "Tools",
}


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'metatool_addon'))
    
    
if "bpy" in locals():
    import imp

    ### MetaToolkit ###
    imp.reload(view3d_MetaTool_Panel)
    imp.reload(view3d_MT_add_operator)
    imp.reload(view3d_MT_add_special)
    imp.reload(view3d_MT_array_operator)    
    imp.reload(view3d_MT_edit_operator)
    imp.reload(view3d_MT_orientation_operator)
    imp.reload(view3d_MT_custom_geometry) 


    #add
    imp.reload(add_nikitron)
    imp.reload(add_boxcamera)

    #anim
    imp.reload(anim_keymover)  
    imp.reload(anim_rigcamera)     
    imp.reload(anim_turnaround_camera)         

    #copy
    imp.reload(copy_attributes)
    imp.reload(copy_datablock_tools)
    imp.reload(copy_mifth_cloning)
    imp.reload(copy_replicator)

    #curve
    imp.reload(curve_bezier_curve_split)      
    imp.reload(curve_convert) 
    imp.reload(curve_mesh_extrude_along_curve)
    imp.reload(curve_outline)  

    #delete
    imp.reload(delete_clear_all_transform)
    imp.reload(delete_edgesplit)
    imp.reload(delete_from_all_scenes) 
    imp.reload(delete_orphan_slayer) 

    #edit
    imp.reload(edit_boolean_2d_union)  
    imp.reload(edit_easy_lattice)
    imp.reload(edit_booleans)
    imp.reload(edit_edger)
    imp.reload(edit_edgeroundifier)        
    imp.reload(edit_edges_vtx_intersection)
    imp.reload(edit_face_hole) 
    imp.reload(edit_face_inset_fillet)
    imp.reload(edit_faces_along_normals)   
    imp.reload(edit_make_planar)  
    imp.reload(edit_mechappo)
    imp.reload(edit_mesh_bsurfaces)
    imp.reload(edit_mesh_cut_faces)
    imp.reload(edit_mesh_edgetools)
    imp.reload(edit_mesh_filletplus)
    imp.reload(edit_mextrude_plus)
    imp.reload(edit_mesh_offset_edges) 
    imp.reload(edit_mesh_vertex_tools)
    imp.reload(edit_multiedit)
    imp.reload(edit_object_intersection)
    imp.reload(edit_perpendicular_bisector)
    imp.reload(edit_rotation_constrained) 
    imp.reload(edit_smart_edges_intersect)
    imp.reload(edit_transfer_normals)
    imp.reload(edit_wazou_menu) 
    imp.reload(edit_tubetool)

                
    #im-export
    imp.reload(io_export_selected) 
    imp.reload(io_vismaya)
   
    #light
    imp.reload(light_silhouette)
    imp.reload(light_trilighting)

    #material
    imp.reload(mat_material_utils)
    imp.reload(mat_mesh_face_random)
    imp.reload(mat_to_cellook)
    imp.reload(mat_wire_materials)


    #modifier
    imp.reload(mod_automirror)
    imp.reload(mod_circle_array)
    imp.reload(mod_follow_path_operator)
    imp.reload(mod_taper_curve)

    #node
    imp.reload(node_rgb_cmyk)
    imp.reload(node_sibl_envo)

    #operator
    imp.reload(operator_delete_clear)
    imp.reload(operator_edit_menu)
    imp.reload(operator_orientation)
    imp.reload(operator_special)
    imp.reload(operator_special_menu)
    imp.reload(operator_submenus)
    imp.reload(operator_adding)      
    imp.reload(operator_align_menu)
    imp.reload(operator_selection)
    imp.reload(operator_particle)
    imp.reload(operator_editor)

    #place
    imp.reload(place_1d_scripts)
    imp.reload(place_align_by_faces)
    imp.reload(place_distribute_objects)
    imp.reload(place_drop_to_ground)
    imp.reload(place_lookatit)   
    imp.reload(place_object_advanced_align_tools0_8)
    imp.reload(place_sgrouper) 
    imp.reload(place_simple_align)
    imp.reload(place_snap_to_center_offset)

    ### extend panel ###   

    imp.reload(poll_arewo)
    imp.reload(poll_arrays)
    imp.reload(poll_cleanup)
    imp.reload(poll_fast_texture_editor)
    imp.reload(poll_layer_manager)
    imp.reload(poll_materials)
    imp.reload(poll_path_editor)
    imp.reload(poll_psl_snapshot)
    imp.reload(poll_quickprefs)
    imp.reload(poll_relations)
    imp.reload(poll_supergrouper)
    imp.reload(poll_uvs)
    imp.reload(poll_vfxtoolbox)
    imp.reload(poll_scene)   
    imp.reload(poll_editing)

    #rename
    imp.reload(rename_objects)
    imp.reload(rename_ue_tools)

    #sculpt         
    imp.reload(sculpt_brush_quickset)
    imp.reload(sculpt_ice_tools)
    imp.reload(sculpt_retopo_mt)   

    #select
    imp.reload(select_meshlint)   
    imp.reload(select_multiselect)
    imp.reload(select_topokit_2)

    #snap
    imp.reload(edit_snap_utilities)
    imp.reload(snap_shotmesh)
    
    #uv
    imp.reload(uv_copy_paste_uvs)
    imp.reload(uv_equalize)
    imp.reload(uv_reproject_image)
    imp.reload(uv_sure_uvwbox)
    imp.reload(uv_tube_unwrap)
    imp.reload(uv_utility)

    #vertex paint
    imp.reload(vert_balance_vertex_groups)
    imp.reload(vert_connected_vertex_colors)
    imp.reload(vert_height)
    imp.reload(vert_randomvertexcolors)
    imp.reload(vert_visiblevertices)
    imp.reload(vert_worn_edges)
    imp.reload(vert_face_size_layer)
    imp.reload(vert_mesh_curves)

    #view
    imp.reload(view_display_tools)
    imp.reload(view_camera)     

    #weight paint
    imp.reload(weight_only_selected_vertices)
    imp.reload(weight_slope)

     
    print("Reloaded multifiles")


######################################################################
######################################################################


else: 

    from . import  view3d_MetaTool_Panel
    from . import  view3d_MT_add_operator 
    from . import  view3d_MT_add_special
    from . import  view3d_MT_array_operator
    from . import  view3d_MT_edit_operator
    from . import  view3d_MT_orientation_operator
    from . import  view3d_MT_custom_geometry


    #add 
    from . import  add_nikitron
    from . import  add_boxcamera

    #anim
    from . import  anim_keymover  
    from . import  anim_rigcamera     
    from . import  anim_turnaround_camera         

    #copy
    from . import  copy_attributes
    from . import  copy_datablock_tools
    from . import  copy_mifth_cloning
    from . import  copy_replicator

    #curve
    from . import  curve_bezier_curve_split      
    from . import  curve_convert 
    from . import  curve_mesh_extrude_along_curve
    from . import  curve_outline  

    #delete
    from . import  delete_clear_all_transform
    from . import  delete_edgesplit
    from . import  delete_from_all_scenes 
    from . import  delete_orphan_slayer 

    #edit
    from . import  edit_boolean_2d_union  
    from . import  edit_easy_lattice
    from . import  edit_booleans
    from . import  edit_edger
    from . import  edit_edgeroundifier        
    from . import  edit_edges_vtx_intersection
    from . import  edit_face_hole 
    from . import  edit_face_inset_fillet
    from . import  edit_faces_along_normals   
    from . import  edit_make_planar  
    from . import  edit_mechappo
    from . import  edit_mesh_bsurfaces
    from . import  edit_mesh_cut_faces
    from . import  edit_mesh_edgetools
    from . import  edit_mesh_filletplus
    from . import  edit_mextrude_plus
    from . import  edit_mesh_offset_edges 
    from . import  edit_mesh_vertex_tools
    from . import  edit_multiedit
    from . import  edit_object_intersection
    from . import  edit_perpendicular_bisector
    from . import  edit_rotation_constrained 
    from . import  edit_smart_edges_intersect
    from . import  edit_transfer_normals
    from . import  edit_wazou_menu 
    from . import  edit_tubetool

                
    #im-export
    from . import  io_export_selected 
    from . import  io_vismaya
   
    #light
    from . import  light_silhouette
    from . import  light_trilighting

    #material
    from . import  mat_material_utils
    from . import  mat_mesh_face_random
    from . import  mat_to_cellook
    from . import  mat_wire_materials

    #modifier
    from . import  mod_automirror
    from . import  mod_circle_array
    from . import  mod_follow_path_operator
    from . import  mod_taper_curve

    #node
    from . import  node_rgb_cmyk
    from . import  node_sibl_envo

    #operator
    from . import  operator_delete_clear
    from . import  operator_edit_menu
    from . import  operator_orientation
    from . import  operator_special
    from . import  operator_special_menu
    from . import  operator_submenus
    from . import  operator_adding      
    from . import  operator_align_menu
    from . import  operator_selection
    from . import  operator_particle
    from . import  operator_editor

    #place
    from . import  place_1d_scripts
    from . import  place_align_by_faces
    from . import  place_distribute_objects
    from . import  place_drop_to_ground
    from . import  place_lookatit   
    from . import  place_object_advanced_align_tools0_8
    from . import  place_sgrouper 
    from . import  place_simple_align
    from . import  place_snap_to_center_offset

    ### extend panel ###   

    from . import  poll_arewo
    from . import  poll_arrays
    from . import  poll_cleanup
    from . import  poll_fast_texture_editor
    from . import  poll_layer_manager
    from . import  poll_materials
    from . import  poll_path_editor
    from . import  poll_psl_snapshot
    from . import  poll_quickprefs
    from . import  poll_relations
    from . import  poll_supergrouper
    from . import  poll_uvs
    from . import  poll_vfxtoolbox
    from . import  poll_scene   
    from . import  poll_editing

    #rename
    from . import  rename_objects
    from . import  rename_ue_tools

    #sculpt         
    from . import  sculpt_brush_quickset
    from . import  sculpt_ice_tools
    from . import  sculpt_retopo_mt   

    #select
    from . import  select_meshlint   
    from . import  select_multiselect
    from . import  select_topokit_2

    #snap
    from . import  edit_snap_utilities
    from . import  snap_shotmesh
    
    #uv
    from . import  uv_copy_paste_uvs
    from . import  uv_equalize
    from . import  uv_reproject_image
    from . import  uv_sure_uvwbox
    from . import  uv_tube_unwrap
    from . import  uv_utility

    #vertex paint
    from . import  vert_balance_vertex_groups
    from . import  vert_connected_vertex_colors
    from . import  vert_height
    from . import  vert_randomvertexcolors
    from . import  vert_visiblevertices
    from . import  vert_worn_edges
    from . import  vert_face_size_layer
    from . import  vert_mesh_curves

    #view
    from . import  view_display_tools  
    from . import  view_camera

    #weight paint
    from . import  weight_only_selected_vertices
    from . import  weight_slope
            
    print("Imported multifiles")


######################################################################
######################################################################

### MetaToolkit ###
import view3d_MetaTool_Panel
import view3d_MT_add_operator
import view3d_MT_add_special
import view3d_MT_array_operator    
import view3d_MT_edit_operator
import view3d_MT_orientation_operator
import view3d_MT_custom_geometry

    
    #add   
import add_nikitron
import add_boxcamera

    #anim
import anim_keymover  
import anim_rigcamera     
import anim_turnaround_camera         

    #copy
import copy_attributes
import copy_datablock_tools
import copy_mifth_cloning
import copy_replicator

    #curve
import curve_bezier_curve_split      
import curve_convert 
import curve_mesh_extrude_along_curve
import curve_outline  

    #delete
import delete_clear_all_transform
import delete_edgesplit
import delete_from_all_scenes 
import delete_orphan_slayer 

    #edit
import edit_boolean_2d_union  
import edit_easy_lattice
import edit_booleans
import edit_edger
import edit_edgeroundifier        
import edit_edges_vtx_intersection
import edit_face_hole 
import edit_face_inset_fillet
import edit_faces_along_normals   
import edit_make_planar  
import edit_mechappo
import edit_mesh_bsurfaces
import edit_mesh_cut_faces
import edit_mesh_edgetools
import edit_mesh_filletplus
import edit_mextrude_plus
import edit_mesh_offset_edges 
import edit_mesh_vertex_tools
import edit_multiedit
import edit_object_intersection
import edit_perpendicular_bisector
import edit_rotation_constrained 
import edit_smart_edges_intersect
import edit_transfer_normals
import edit_wazou_menu 
import edit_tubetool

                
    #im-export
import io_export_selected 
import io_vismaya
   
    #light
import light_silhouette
import light_trilighting

    #material
import mat_material_utils
import mat_mesh_face_random
import mat_to_cellook
import mat_wire_materials


    #modifier
import mod_automirror
import mod_circle_array
import mod_follow_path_operator
import mod_taper_curve

    #node
import node_rgb_cmyk
import node_sibl_envo

    #operator
import operator_delete_clear
import operator_edit_menu
import operator_orientation
import operator_special
import operator_special_menu
import operator_submenus
import operator_adding      
import operator_align_menu
import operator_selection
import operator_particle
import operator_editor


    #place
import place_1d_scripts
import place_align_by_faces
import place_distribute_objects
import place_drop_to_ground
import place_lookatit   
import place_object_advanced_align_tools0_8
import place_sgrouper 
import place_simple_align
import place_snap_to_center_offset

    ### extend panel ###   

import poll_arewo
import poll_arrays
import poll_cleanup
import poll_fast_texture_editor
import poll_layer_manager
import poll_materials
import poll_path_editor
import poll_psl_snapshot
import poll_quickprefs
import poll_relations
import poll_supergrouper
import poll_uvs
import poll_vfxtoolbox
import poll_scene   
import poll_editing

    #rename
import rename_objects
import rename_ue_tools

    #sculpt         
import sculpt_brush_quickset
import sculpt_ice_tools
import sculpt_retopo_mt   

    #select
import select_meshlint   
import select_multiselect
import select_topokit_2

#snap
import edit_snap_utilities
import snap_shotmesh

    
    #uv
import uv_copy_paste_uvs
import uv_equalize
import uv_reproject_image
import uv_sure_uvwbox
import uv_tube_unwrap
import uv_utility

#vertex paint
import vert_balance_vertex_groups
import vert_connected_vertex_colors
import vert_height
import vert_randomvertexcolors
import vert_visiblevertices
import vert_worn_edges
import vert_face_size_layer
import vert_mesh_curves

#view
import view_display_tools  
import view_camera

#weight paint
import weight_only_selected_vertices
import weight_slope


import bpy



######################################################################
######################################################################

def register():

   ### MetaToolkit ###
   view3d_MetaTool_Panel.register()
   view3d_MT_add_operator.register()
   view3d_MT_add_special.register()
   view3d_MT_array_operator.register()   
   view3d_MT_edit_operator.register()
   view3d_MT_orientation_operator.register()
   view3d_MT_custom_geometry.register()
   
  
    #add   
   add_nikitron.register()
   add_boxcamera.register()

    #anim
   anim_keymover.register()  
   anim_rigcamera.register()     
   anim_turnaround_camera.register()        

    #copy
   copy_attributes.register()
   copy_datablock_tools.register()
   copy_mifth_cloning.register()
   copy_replicator.register()

    #curve
   curve_bezier_curve_split.register()      
   curve_convert.register() 
   curve_mesh_extrude_along_curve.register()
   curve_outline.register()  

    #delete
   delete_clear_all_transform.register()
   delete_edgesplit.register()
   delete_from_all_scenes.register()
   delete_orphan_slayer.register()

    #edit
   edit_boolean_2d_union.register()
   edit_easy_lattice.register()
   edit_booleans.register()
   edit_edger.register()
   edit_edgeroundifier.register()        
   edit_edges_vtx_intersection.register()
   edit_face_hole.register() 
   edit_face_inset_fillet.register()
   edit_faces_along_normals.register()   
   edit_make_planar.register()  
   edit_mechappo.register()
   edit_mesh_bsurfaces.register()
   edit_mesh_cut_faces.register()
   edit_mesh_edgetools.register()
   edit_mesh_filletplus.register()
   edit_mextrude_plus.register()
   edit_mesh_offset_edges.register() 
   edit_mesh_vertex_tools.register()
   edit_multiedit.register()
   edit_object_intersection.register()
   edit_perpendicular_bisector.register()
   edit_rotation_constrained.register() 
   edit_smart_edges_intersect.register()
   edit_transfer_normals.register()
   edit_wazou_menu.register() 
   edit_tubetool.register() 

                
    #im-export
   io_export_selected.register() 
   io_vismaya.register()
   
    #light
   light_silhouette.register()
   light_trilighting.register()

    #material
   mat_material_utils.register()
   mat_mesh_face_random.register()
   mat_to_cellook.register()
   mat_wire_materials.register()


    #modifier
   mod_automirror.register()
   mod_circle_array.register()
   mod_follow_path_operator.register()
   mod_taper_curve.register()

    #node
   node_rgb_cmyk.register()
   node_sibl_envo.register()

    #operator
   operator_delete_clear.register()
   operator_edit_menu.register()
   operator_orientation.register()
   operator_special.register()
   operator_special_menu.register()
   operator_submenus.register()
   operator_adding.register()
   operator_align_menu.register()
   operator_selection.register()
   operator_particle.register()
   operator_editor.register()


    #place
   place_1d_scripts.register()
   place_align_by_faces.register()
   place_distribute_objects.register()
   place_drop_to_ground.register()
   place_lookatit.register()
   place_object_advanced_align_tools0_8.register()
   place_sgrouper.register()
   place_simple_align.register()
   place_snap_to_center_offset.register()

    ### extend panel ###   

   poll_arewo.register()
   poll_arrays.register()
   poll_cleanup.register()
   poll_fast_texture_editor.register()
   poll_layer_manager.register()
   poll_materials.register()
   poll_path_editor.register()
   poll_psl_snapshot.register()
   poll_quickprefs.register()
   poll_relations.register()
   poll_supergrouper.register()
   poll_uvs.register()
   poll_vfxtoolbox.register()
   poll_scene.register()
   poll_editing.register()

    #rename
   rename_objects.register()
   rename_ue_tools.register()

    #sculpt         
   sculpt_brush_quickset.register()
   sculpt_ice_tools.register()
   sculpt_retopo_mt.register()

    #select
   select_meshlint.register()   
   select_multiselect.register()
   select_topokit_2.register()

    #snap
   edit_snap_utilities.register()
   snap_shotmesh.register()
    
    #uv
   uv_copy_paste_uvs.register()
   uv_equalize.register()
   uv_reproject_image.register()
   uv_sure_uvwbox.register()
   uv_tube_unwrap.register()
   uv_utility.register()

    #vertex paint
   vert_balance_vertex_groups.register()
   vert_connected_vertex_colors.register()
   vert_height.register()
   vert_randomvertexcolors.register()
   vert_visiblevertices.register()
   vert_worn_edges.register()
   vert_face_size_layer.register()
   vert_mesh_curves.register()

    #view
   view_display_tools.register()
   view_camera.register()


    #weight paint
   weight_only_selected_vertices.register()
   weight_slope.register()


   bpy.utils.register_module(__name__)
   
   
   
 
def unregister():

   ### MetaToolkit ###
   view3d_MetaTool_Panel.unregister()
   view3d_MT_add_operator.unregister()
   view3d_MT_add_special.unregister()
   view3d_MT_array_operator.unregister()   
   view3d_MT_edit_operator.unregister()
   view3d_MT_orientation_operator.unregister()       
   view3d_MT_custom_geometry.unregister()    
  
    #add   
   add_nikitron.unregister()
   add_boxcamera.unregister()

    #anim
   anim_keymover.unregister()  
   anim_rigcamera.unregister()     
   anim_turnaround_camera.unregister()        

    #copy
   copy_attributes.unregister()
   copy_datablock_tools.unregister()
   copy_mifth_cloning.unregister()
   copy_replicator.unregister()

    #curve
   curve_bezier_curve_split.unregister()      
   curve_convert.unregister() 
   curve_mesh_extrude_along_curve.unregister()
   curve_outline.unregister()  

    #delete
   delete_clear_all_transform.unregister()
   delete_edgesplit.unregister()
   delete_from_all_scenes.unregister()
   delete_orphan_slayer.unregister()

    #edit
   edit_boolean_2d_union.unregister()
   edit_easy_lattice.unregister()
   edit_booleans.unregister()
   edit_edger.unregister()
   edit_edgeroundifier.unregister()        
   edit_edges_vtx_intersection.unregister()
   edit_face_hole.unregister() 
   edit_face_inset_fillet.unregister()
   edit_faces_along_normals.unregister()   
   edit_make_planar.unregister()  
   edit_mechappo.unregister()
   edit_mesh_bsurfaces.unregister()
   edit_mesh_cut_faces.unregister()
   edit_mesh_edgetools.unregister()
   edit_mesh_filletplus.unregister()
   edit_mextrude_plus.unregister()
   edit_mesh_offset_edges.unregister() 
   edit_mesh_vertex_tools.unregister()
   edit_multiedit.unregister()
   edit_object_intersection.unregister()
   edit_perpendicular_bisector.unregister()
   edit_rotation_constrained.unregister() 
   edit_smart_edges_intersect.unregister()
   edit_transfer_normals.unregister()
   edit_wazou_menu.unregister() 
   edit_tubetool.unregister() 

                
    #im-export
   io_export_selected.unregister() 
   io_vismaya.unregister()
   
    #light
   light_silhouette.unregister()
   light_trilighting.unregister()

    #material
   mat_material_utils.unregister()
   mat_mesh_face_random.unregister()
   mat_to_cellook.unregister()
   mat_wire_materials.unregister()

    #modifier
   mod_automirror.unregister()
   mod_circle_array.unregister()
   mod_follow_path_operator.unregister()
   mod_taper_curve.unregister()

    #node
   node_rgb_cmyk.unregister()
   node_sibl_envo.unregister()

    #operator
   operator_delete_clear.unregister()
   operator_edit_menu.unregister()
   operator_orientation.unregister()
   operator_special.unregister()
   operator_special_menu.unregister()
   operator_submenus.unregister()
   operator_adding.unregister()
   operator_align_menu.unregister()
   operator_selection.unregister()
   operator_particle.unregister()
   operator_editor.unregister()

    #place
   place_1d_scripts.unregister()
   place_align_by_faces.unregister()
   place_distribute_objects.unregister()
   place_drop_to_ground.unregister()
   place_lookatit.unregister()
   place_object_advanced_align_tools0_8.unregister()
   place_sgrouper.unregister()
   place_simple_align.unregister()
   place_snap_to_center_offset.unregister()

    ### extend panel ###   

   poll_arewo.unregister()
   poll_arrays.unregister()
   poll_cleanup.unregister()
   poll_fast_texture_editor.unregister()
   poll_layer_manager.unregister()
   poll_materials.unregister()
   poll_path_editor.unregister()
   poll_psl_snapshot.unregister()
   poll_quickprefs.unregister()
   poll_relations.unregister()
   poll_supergrouper.unregister()
   poll_uvs.unregister()
   poll_vfxtoolbox.unregister()
   poll_scene.unregister()
   poll_editing.unregister()

    #rename
   rename_objects.unregister()
   rename_ue_tools.unregister()

    #sculpt         
   sculpt_brush_quickset.unregister()
   sculpt_ice_tools.unregister()
   sculpt_retopo_mt.unregister()

    #select
   select_meshlint.unregister()   
   select_multiselect.unregister()
   select_topokit_2.unregister()

    #snap
   edit_snap_utilities.unregister()
   snap_shotmesh.unregister() 
      
    #uv
   uv_copy_paste_uvs.unregister()
   uv_equalize.unregister()
   uv_reproject_image.unregister()
   uv_sure_uvwbox.unregister()
   uv_tube_unwrap.unregister()
   uv_utility.unregister()

    #vertex paint
   vert_balance_vertex_groups.unregister()
   vert_connected_vertex_colors.unregister()
   vert_height.unregister()
   vert_randomvertexcolors.unregister()
   vert_visiblevertices.unregister()
   vert_worn_edges.unregister()
   vert_face_size_layer.unregister()
   vert_mesh_curves.unregister()
   
    #view
   view_display_tools.unregister()
   view_camera.unregister()
   
    #weight paint
   weight_only_selected_vertices.unregister()
   weight_slope.unregister()
   
   
          
   bpy.utils.unregister_module(__name__)
 
    
if __name__ == "__main__":
    register()



