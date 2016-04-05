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

#bl_info = {
#    "name": "SFC Retopo",
#    "author": "mkbreuer",
#    "version": (0, 1, 0),
#    "blender": (2, 76, 0),
#    "location": "View3D > Toolbar > SFC Retopo",
#    "warning": "",
#    "description": "Toolkit for the Main Panel",
#    "wiki_url": "",
#    "category": "",
#}



import bpy
from bpy import*


############----------------------############
############  Props for DROPDOWN  ############
############----------------------############

class DropdownRetopoXToolProps(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.retopowindowx
    """
    display_curvemodifier = bpy.props.BoolProperty(name = "Modifier Tools", description = "Display Modifier Tools", default = False)
    display_curvealign = bpy.props.BoolProperty(name = "Align", description = "Display Align Tools", default = False)
    display_curveedit = bpy.props.BoolProperty(name = "Editing", description = "Display Editing Tools", default = False)
    display_curvetools = bpy.props.BoolProperty(name = "Curve", description = "Display Curve Tools", default = False)
    display_curvevisual = bpy.props.BoolProperty(name = "Shading", description = "Display Shading Tools", default = False)    
    display_curveselect = bpy.props.BoolProperty(name = "Selection", description = "Display Selection Tools", default = False)    
    display_curvetransform = bpy.props.BoolProperty(name = "Transform", description = "Display Transform Tools", default = False)    
    display_curvepivot = bpy.props.BoolProperty(name = "Pivot & Origin", description = "Display Pivot & Origin Tools", default = False)    
    display_curvegeo = bpy.props.BoolProperty(name = "Shape Geometry", description = "Display Shape Geometry Tools", default = False)    
    display_view = bpy.props.BoolProperty(name = "View", description = "Display View Tools", default = False)    

bpy.utils.register_class(DropdownRetopoXToolProps)
bpy.types.WindowManager.retopowindowx = bpy.props.PointerProperty(type = DropdownRetopoXToolProps)



############-----------------------------############
############  DROPDOWN Layout for PANEL  ############
############-----------------------------############


def draw_retopo_curve_ui(self, context, layout):
     lt = context.window_manager.retopowindowx
     obj = context.object
 
     layout.operator_context = 'INVOKE_REGION_WIN'
     col = layout.column(align=True)


###################            
### Curve Add ###
###################

     box=layout.box().column(True)       
     row=box.row(align=True)         
     row.alignment = 'CENTER'               

     sub = row.row(1)
     sub.scale_x = 1.2      
     sub.operator("curve.primitive_bezier_curve_add",icon='CURVE_BEZCURVE',text="")
     sub.operator("curve.primitive_bezier_circle_add",icon='CURVE_BEZCIRCLE',text="")
     sub.operator("curve.primitive_nurbs_curve_add",icon='CURVE_NCURVE',text="")
     sub.operator("curve.primitive_nurbs_circle_add",icon='CURVE_NCIRCLE',text="")
     sub.operator("curve.primitive_nurbs_path_add",icon='CURVE_PATH',text="") 
     row.operator("object.curv_to_2d",text="2d") 
     row.operator("object.curv_to_3d",text="3d")  



###################            
### Curve Pivot ###
###################

     box = layout.box()
     row = box.row(1)  
     sub = row.row(1)
     sub.scale_x = 7
     sub.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
     sub.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
     sub.operator("view3d.pivot_active", "", icon="ROTACTIVE")
     sub.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
     sub.operator("view3d.pivot_median", "", icon="ROTATECENTER")  
     row.operator("curve.delete", "", icon = "PANEL_CLOSE") 

     
     
############ 
### View ###
############

     ###space###
     if lt.display_view:
         ###space###       
         box = layout.box()
         row = box.row(1)                       
         row.prop(lt, "display_view", text="", icon='TRIA_DOWN')
         row.label("View...")
         
     else:
         box = layout.box()
         row = box.row(1)              
         row.prop(lt, "display_view", text="", icon='TRIA_RIGHT')        
         row.label("View...")
         
         row.operator("view3d.view_all","", icon = "ZOOM_OUT" )               
         row.operator("view3d.view_selected","", icon = "ZOOM_IN" )
         row.operator("view3d.zoom_border","", icon = "BORDERMOVE" )    


     ###space###
     if lt.display_view:

         col = layout.column(align=True) 
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.column(align=True)  
         row.operator("view3d.view_all","All", icon = "ZOOM_OUT" )               
         row.operator("view3d.view_center_cursor", text="Cursor", icon = "ZOOM_PREVIOUS")  
         row.operator("view3d.view_selected","Selected", icon = "ZOOM_IN")       
         row.operator("view3d.zoom_border","Zoom Border", icon = "BORDERMOVE" )

         col = layout.column(align=True) 
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.row(align=True) 
         row.operator("view3d.localview", text="Global/Local")
         row.operator("view3d.view_persportho", text="Persp/Ortho") 

         col = layout.column(align=True) 
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.row(align=True)
         row.label(text="View to Object:")
         row = col_top.row(align=True)
         row.prop(context.space_data, "lock_object", text="")


#######################            
### Curve Selection ###
#######################

     ###space### 
     if lt.display_curveselect:
         box = layout.box()
         row = box.row(1)                       
         row.prop(lt, "display_curveselect", text="", icon='TRIA_DOWN')
         row.label("Select...")
     
     else:
         box = layout.box()
         row = box.row(1)              
         row.prop(lt, "display_curveselect", text="", icon='TRIA_RIGHT')    
         row.label("Select...")

         row.menu("VIEW3D_MT_edit_curve_showhide", "", icon = "VISIBLE_IPO_ON") 
         row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")  
         row.operator("view3d.select_border", text="", icon="BORDER_RECT")        
    

     if lt.display_curveselect:

         col = layout.column(align=True)                          
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.row(align=True)
         row.operator("view3d.select_border", text="Border", icon="BORDER_RECT") 
         row.operator("view3d.select_circle", text="Circle", icon="BORDER_LASSO")              


         col = layout.column(align=True)
         box = col.column(align=True).box().column(1)
         col_top = box.column(align=True)

         row = col_top.row(align=True)  
         row.menu("VIEW3D_MT_edit_curve_showhide",  icon = "VISIBLE_IPO_ON") 
         
         row = col_top.row(align=True) 
         row.operator("curve.select_all", text="Inverse").action = 'INVERT'
         row.operator("curve.select_random", text="Random") 

         col_top = box.column(align=True)
         row = col_top.row(align=True)
         row.operator("curve.select_linked", text="Linked")             
         row.operator("curve.select_nth", text="Checker")
        

         col_top = box.column(align=True)
         row = col_top.row(align=True) 
         row.operator("curve.de_select_first", text="First")
         row.operator("curve.de_select_last", text="Last")
        
         col_top = box.column(align=True)
         row = col_top.row(align=True)             
         row.operator("curve.select_next", text="Next")
         row.operator("curve.select_previous", text="Previous")


################### 
### Curve Pivot ###     
### Curve Pivot ###   
################### 

     ###space###        
     if lt.display_curvepivot:
         ###space###         
         box = layout.box()
         row = box.row(1)                    
         row.prop(lt, "display_curvepivot", text="", icon='TRIA_DOWN')
         row.label("Pivot...")

     else:
         box = layout.box()
         row = box.row(1)  
         row.prop(lt, "display_curvepivot", text="", icon='TRIA_RIGHT')
         row.label("Pivot...")

         row.menu("origin.setupmenu_edm", "", icon="LAYER_ACTIVE")
         row.menu("wkst.snaptocursor","", icon="FORCE_FORCE")
         row.menu("wkst.snaptoselect","", icon="RESTRICT_SELECT_OFF")

     ###space###
     if lt.display_curvepivot:
         col = layout.column(align=True)                                                                   
         box = col.column(align=True).box().column()       
         col_top = box.column(align=True)
         row = col_top.row(align=True)  
         row.operator("object.origin_obm", "OB-Mode", icon = "OBJECT_DATAMODE")
         row.operator("object.origin_edm", "ED-Mode", icon = "EDITMODE_HLT")
          
         col = layout.column(align=True)                                                                   
         box = col.column(align=True).box().column()       
         col_top = box.column(align=True)

         row = col_top.row(align=True)
         row.menu("wkst.snaptocursor","Cursor to... ", icon="FORCE_FORCE")     
                   
         row = col_top.row(align=True)
         row.menu("wkst.snaptoselect","Selection to... ", icon="RESTRICT_SELECT_OFF")


####################### 
### Curve Transform ###
#######################

     ###space###                       
     if lt.display_curvetransform:
         box = layout.box()
         row = box.row(1)                         
         row.prop(lt, "display_curvetransform", text="", icon='TRIA_DOWN')
         row.label("Transform...")        

     else:
         box = layout.box()
         row = box.row(1)              
         row.prop(lt, "display_curvetransform", text="", icon='TRIA_RIGHT')    
         row.label("Transform...")

         row.menu("VIEW3D_MT_mirror","", icon="ARROW_LEFTRIGHT") 
         row.menu("wkst.normal_transform_menu","", icon="AXIS_SIDE")  
         row.menu("wkst.transform_menu","", icon="MANIPUL")     
 

     if lt.display_curvetransform:

         col = layout.column(align=True)               
         box = col.column(align=True).box().column()       
         col_top = box.column(align=True)  
     
         row = col_top.row(align=True)
         row.operator("transform.translate",text="(G)", icon="MAN_TRANS")
         row.operator("transform.rotate", text="(R)", icon="MAN_ROT")
         row.operator("transform.resize", text="(S)", icon="MAN_SCALE") 

         col = layout.column(align=True)          
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.row(align=True)         
         row.operator("object.mirror1",text="MX", icon='ARROW_LEFTRIGHT')
         row.operator("object.mirror2",text="MY", icon='ARROW_LEFTRIGHT')
         row.operator("object.mirror3",text="MZ", icon='ARROW_LEFTRIGHT')            

         col = layout.column(align=True)                      
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)
         
         row = col_top.row(align=True)
         row.operator("transform.push_pull", text="Push/Pull")
         row.operator("object.vertex_warp", text="Warp")

         row = col_top.row(align=True)
         row.operator("object.vertex_random", text="Randomize")           
         row.operator("transform.tosphere", "to Sphere")            

         col = layout.column(align=True)                      
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)
         
         row = col_top.column(align=True)
         row.operator("transform.translate", text="Move Texture Space").texture_space = True
         row.operator("transform.resize", text="Scale Texture Space").texture_space = True      



  
################### 
### Curve Align ###     
################### 

     ###space###        
     if lt.display_curvealign:
         ###space###         
         box = layout.box()
         row = box.row(1)                    
         row.prop(lt, "display_curvealign", text="", icon='TRIA_DOWN')
         row.label("Align...")

     else:
         box = layout.box()
         row = box.row(1)  
         row.prop(lt, "display_curvealign", text="", icon='TRIA_RIGHT')
         row.label("Align...")
         
         sub = row.row(1)
         sub.scale_x = 0.35             
         sub.operator("mesh.face_align_x", "X", icon='TRIA_RIGHT')
         sub.operator("mesh.face_align_y", "Y", icon='TRIA_UP')           
         sub.operator("mesh.face_align_z", "Z", icon='SPACE3') 

 
     ###space###
     if lt.display_curvealign:
         ###space###    

         box = layout.box().row()
         row = box.column(1) 
         row.label("Align") 
         row.label("to") 
         row.label("Axis") 

         row = box.column(1)
         row.operator("mesh.face_align_xy", "Xy", icon='TRIA_RIGHT_BAR')
         row.operator("mesh.face_align_yz", "Zy", icon='TRIA_UP_BAR')           
         row.operator("mesh.face_align_xz", "Zx", icon='TRIA_LEFT_BAR')

         row = box.column(1)
         row.operator("mesh.face_align_x", "X", icon='TRIA_RIGHT')
         row.operator("mesh.face_align_y", "Y", icon='TRIA_UP')           
         row.operator("mesh.face_align_z", "Z", icon='SPACE3')


######################            
### Curve Geometry ###
###################### 

     ###space###         
     if lt.display_curvegeo:
         box = layout.box()
         row = box.row(1)                                    
         row.prop(lt, "display_curvegeo", text="", icon='TRIA_DOWN')
         row.label("Curve...")
         
     else: 
         box = layout.box()
         row = box.row(1)                       
         row.prop(lt, "display_curvegeo", text="", icon='TRIA_RIGHT')        
         row.label("Curve...")

         sub = row.row(1)
         sub.scale_x = 0.4    
         sub.prop(context.object.data, "resolution_u", text="")                   
         row.menu("wkst.curve_edit_menu","", icon="CURVE_BEZCIRCLE")              
            
    
     if lt.display_curvegeo:           
         col = layout.column(align=True)
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.column(align=True)  
         row.operator("curve.spline_type_set", "Set Spline Type", icon="IPO_BEZIER")           
         row.operator("curve.switch_direction", text="Switch Direction", icon = "ARROW_LEFTRIGHT")                   
         row.operator("curve.cyclic_toggle","Open / Close Curve", icon="MOD_CURVE")  
                  
         ###--------------------- 

         col = layout.column(align=True)
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.row(align=True)
         row.alignment = 'CENTER'  
         row.label("Handles") 
        
         row = col_top.row(align=True)                            
         row.operator("curve.handle_to_free","Free")                         
         row.operator("curve.handle_to_automatic","Auto")
         
         row = col_top.row(align=True)                                                   
         row.operator("curve.handle_to_vector","Vector") 
         row.operator("curve.handle_to_aligned","Aligned")

         ###---------------------            		

         col = layout.column(align=True)
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.row(align=True)
         row.alignment = 'CENTER' 
         row.label("Subdivide")   
         
         row = col_top.row(align=True) 
         row.operator("curve.subdivide", text="1").number_cuts=1        
         row.operator("curve.subdivide", text="2").number_cuts=2
         row.operator("curve.subdivide", text="3").number_cuts=3
         row.operator("curve.subdivide", text="4").number_cuts=4
         row.operator("curve.subdivide", text="5").number_cuts=5        
         row.operator("curve.subdivide", text="6").number_cuts=6  

         ###--------------------- 
         
         col = layout.column(align=True)
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.row(align=True)  
         row.operator("curve.extrude_move", text="Extrude")
         row.operator("curve.make_segment",  text="Weld") 

         row = col_top.row(align=True)             
         row.operator("curve.split",  text="Split")          
         row.operator("curve.bezier_spline_divide", text='Divide') 
                  
         row = col_top.row(align=True)             
         row.operator("curve.separate",  text="Separate")         
         row.operator("curve.bezier_points_fillet", text='Fillet') 
     
         row = col_top.row(align=True)
         row.operator("transform.vertex_random") 
         row.operator("object._curve_outline",  text="Outline")             

         row = col_top.row(align=True) 
         row.operator("transform.tilt", text="Tilt")                                     
         row.operator("curve.radius_set", "Radius")                 

         ###--------------------- 
         
         col = layout.column(align=True)
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)
                  
         row = col_top.row(align=True)          
         row.operator("curve.smooth", icon ="SMOOTHCURVE")             
         row.operator("curve.normals_make_consistent", icon ="SNAP_NORMAL")

         ###--------------------- 
         
         #col = layout.column(align=True)
         #box = col.column(align=True).box().column()
         #col_top = box.column(align=True)
        
         #row = col_top.row(align=True) 
         #row.operator("curve.surfsk_first_points", text="Set First Points")
         #row = col_top.row(align=True) 
         #row.operator("curve.surfsk_reorder_splines", text="Reorder Splines")

         ###--------------------- 
         
         col = layout.column(align=True) 
         box = col.column(align=True).box().column()       
         col_top = box.column(align=True) 

         row = col_top.row(align=True)
         row.alignment = 'CENTER' 
         row.label("Bevel Curve") 
         
         row = col_top.row(align=True)        
         row.prop(context.object.data, "fill_mode", text="")           
         row.prop(context.object.data, "use_fill_deform")

         col = layout.column(align=True) 
         box = col.column(align=True).box().column()       
         col_top = box.column(align=True) 
         
         row = col_top.row(align=True)
         row.operator("object.wire_all", text="", icon='WIRE')
         row.prop(context.object.data, "bevel_depth", text="Bevel Depth")
         
         row = col_top.row(align=True)
         row.prop(context.object.data, "resolution_u", text="Rings")          
         row.prop(context.object.data, "bevel_resolution", text="Loops")

         row = col_top.row(align=True)
         row.prop(context.object.data, "offset")
         row.prop(context.object.data, "extrude","Height")

         ###--------------------- 
          
         col = layout.column(align=True) 
         box = col.column(align=True).box().column()       
         col_top = box.column(align=True) 
         
         row = col_top.row(align=True) 
         row.label(text="Bevel Factor:")
     
         row.active = (context.object.data.bevel_depth > 0 or context.object.data.bevel_object is not None)

         row = col_top.row(align=True) 
         row.prop(context.object.data, "bevel_factor_start", text="Start") 
         row.prop(context.object.data, "bevel_factor_end", text="End")  

         row = col_top.row(align=True) 
         row.prop(context.object.data, "bevel_factor_mapping_start", text="")
         row.prop(context.object.data, "bevel_factor_mapping_end", text="")
                  
         row = col_top.row(align=True)                      
         sub = row.row()
         sub.active = context.object.data.taper_object is not None
         sub.prop(context.object.data, "use_map_taper")

         sub = row.row()
         sub.active = context.object.data.bevel_object is not None
         sub.prop(context.object.data, "use_fill_caps")

         ###---------------------          

         col = layout.column(align=True) 
         box = col.column(align=True).box().column()       
         col_top = box.column(align=True) 
         
         row = col_top.row(align=True)  
         row.label(text="Taper Object:")
         row.prop(context.object.data, "taper_object", text="")
         
         row = col_top.row(align=True) 
         row.label(text="Bevel Object:")
         row.prop(context.object.data, "bevel_object", text="")

         ###---------------------          

         col = layout.column(align=True) 
         box = col.column(align=True).box().column()       
         col_top = box.column(align=True) 

         row = col_top.row(align=True) 
         row.alignment = 'CENTER' 
         row.label(text="Path / Curve-Deform")

         row = col_top.row(align=True)
         row.prop(context.object.data, "use_radius")
         row.prop(context.object.data, "use_stretch")
         row.prop(context.object.data, "use_deform_bounds")
         
         row = col_top.row(align=True)
         row.alignment = 'CENTER' 
         row.label(text="Twisting")

         row = col_top.row(align=True) 
         row.active = (context.object.data.dimensions == '2D' or (context.object.data.bevel_object is None and context.object.data.dimensions == '3D'))
         row.prop(context.object.data,"twist_mode", text="")
         row.prop(context.object.data, "twist_smooth", text="Smooth")


###################            
### Curve Tools ###
################### 

     ###space###         
     if lt.display_curvetools:
         box = layout.box()
         row = box.row(1)                                    
         row.prop(lt, "display_curvetools", text="", icon='TRIA_DOWN')
         row.label("CurveT2...")
         
     else: 
         box = layout.box()
         row = box.row(1)                       
         row.prop(lt, "display_curvetools", text="", icon='TRIA_RIGHT')        
         row.label("CurveT2...")
         
         row.operator("curve.spline_type_set", "", icon="IPO_BEZIER") 
         row.menu("wkst.ct2d_menu", text = "", icon ="DISCLOSURE_TRI_DOWN")
         row.menu("wkst.ct2_menu", text = "", icon ="ANIM_DATA") 


     if lt.display_curvetools:           
         col = layout.column(align=True) 
         box = col.column(align=True).box().column()       
         col_top = box.column(align=True) 
         
         row = col_top.row(align=True)
         row.alignment = "CENTER"
         row.label("", icon ="INFO")               
         
         row = col_top.row(align=True)
         row.operator("curvetools2.operatorcurveinfo", text = "Curve")                        
         row.operator("curvetools2.operatorsplinesinfo", text = "Splines")
         row.operator("curvetools2.operatorsegmentsinfo", text = "Segments")
         
         col_top = box.column(align=True) 
         col_top = box.column(align=True) 
         col_top = box.column(align=True) 
         
         row = col_top.row(align=True) 
         row.operator("curvetools2.operatorselectioninfo", text = "Selection Info:")
         row.prop(context.scene.curvetools, "NrSelectedObjects", text = "")   

         row = col_top.row(align=True) 
         row.operator("curvetools2.operatorcurvelength", text = "Calc Length")
         row.prop(context.scene.curvetools, "CurveLength", text = "")
 
         #row = col_top.row(align=True) 
         #row.operator("curvetools2.operatorsplinessetresolution", text = "Set Resolution", icon = "FILE_TICK")
         #row.prop(context.scene.curvetools, "SplineResolution", text = "")           
        
         ###--------------------------                     
        
         col = layout.column(align=True)
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)
        
         row = col_top.row(align=True)
         row.operator("object.wire_all", text="", icon='WIRE') 
         row.prop(context.object.data, "resolution_u", text="Set Resolution")
         #row.operator("curvetools2.operatorsplinessetresolution", text = "Set resolution")
         #row.prop(context.scene.curvetools, "SplineResolution", text = "") 

         row = col_top.row(align=True) 
         row.operator("curve.open_circle", text = "Open/Close", icon = "MOD_CURVE")  
         #row.operator("curvetools2.operatororigintospline0start", text = "Origin 2 Start" ,icon = "PARTICLE_TIP")
         row.operator("curve.switch_direction_obm","Direction" ,icon = "ARROW_LEFTRIGHT")    

         ###--------------------------
        
         col = layout.column(align=True)
         box = col.column(align=True).box().column()            
         col_top = box.column(align=True)

         row = col_top.row(align=True)
         row.alignment = "CENTER" 
         row.label("Optimize Tools for BezièrCurve", icon="LAMP")

         row = col_top.row(align=True) 
         row.operator("curvetools2.operatorsplinesjoinneighbouring", text = "Join neighbouring splines", icon ="AUTOMERGE_ON")

         row = col_top.row(align=True)
         row.prop(context.scene.curvetools, "SplineJoinDistance", text = "Threshold join")

         col_top = box.column(align=True)
         col_top = box.column(align=True)

         row = col_top.row(align=True) 
         row.prop(context.scene.curvetools, "SplineJoinStartEnd", text = "Only at start & end")

         row = col_top.row(align=0.5) 
         row.prop(context.scene.curvetools, "SplineJoinMode", text = "Join")

         ###--------------------------   

         col_top = box.column(align=True)

         row = col_top.row(align=True)             
         row.operator("curvetools2.operatorsplinesremovezerosegment", text = "del 0-segments", icon ="DISCLOSURE_TRI_DOWN")
         row.operator("curvetools2.operatorsplinesremoveshort", text = "del short splines", icon ="DISCLOSURE_TRI_DOWN")

         row = col_top.row(align=True)
         row.prop(context.scene.curvetools, "SplineRemoveLength", text = "Threshold remove")



###################### 
### Curve Modifier ###     
###################### 

     ###space###       
     if lt.display_curvemodifier:
         ###space###         
         box = layout.box()
         row = box.row(1)                    
         row.prop(lt, "display_curvemodifier", text="", icon='TRIA_DOWN')
         row.label("Modifier...")   

     else:
         box = layout.box()
         row = box.row(1)  
         row.prop(lt, "display_curvemodifier", text="", icon='TRIA_RIGHT')
         row.label("Modifier...")        
         
         row.operator_menu_enum("object.modifier_add", "type","", icon = 'MODIFIER')
         row.menu("modifiers.viewport_edm","",icon = 'RESTRICT_VIEW_OFF')   
         row.operator("view3d.display_modifiers_delete","", icon = 'X')                   
     
     ###space###
     if lt.display_curvemodifier:
         ###space###
         col = layout.column(align=True)          
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)
         row = col_top.row(align=True)

         row.label("SubSurf Levels")
    
         row = col_top.row(align=True)
         row.operator("view3d.modifiers_subsurf_level_0")
         row.operator("view3d.modifiers_subsurf_level_1")
         row.operator("view3d.modifiers_subsurf_level_2")
         row.operator("view3d.modifiers_subsurf_level_3")
         row.operator("view3d.modifiers_subsurf_level_4")
         row.operator("view3d.modifiers_subsurf_level_5")
         row.operator("view3d.modifiers_subsurf_level_6")

         ###--------------------- 
                  
         col = layout.column(align=True)          
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)
         
         row = col_top.row(align=True)
         row.label("Mirror Modifier / all enabled")         
         
         row = col_top.row(align=True)    
         row.operator("view3d.fullmirror", text="X-Clip")
         row.operator("view3d.fullmirrory", text="Y-Clip")
         row.operator("view3d.fullmirrorz", text="Z-Clip")

         ###--------------------- 
        
         col = layout.column(align=True)          
         box = col.column(align=True).box().column()       
         col_top = box.column(align=True)

         row = col_top.row(align=True)
         row.operator("view3d.display_modifiers_viewport_on",icon = 'RESTRICT_VIEW_OFF')
         row.operator("view3d.display_modifiers_edit_on", icon = 'EDITMODE_HLT')
         row.operator("view3d.display_modifiers_cage_on",icon = 'OUTLINER_OB_MESH')

         row = col_top.row(align=True)
         row.operator("view3d.display_modifiers_viewport_off",icon = 'VISIBLE_IPO_OFF')         
         row.operator("view3d.display_modifiers_edit_off",icon = 'SNAP_VERTEX')  
         row.operator("view3d.display_modifiers_cage_off",icon = 'OUTLINER_DATA_MESH')

         ###--------------------- 

         col = layout.column(align=True)          
         box = col.column(align=True).box().column()       
         col_top = box.column(align=True)

         row = col_top.row(align=True)
         row.label("Move over the Modifier Stack")

         row = col_top.row(align=True)
         row.operator("view3d.display_modifiers_expand", icon = 'DISCLOSURE_TRI_DOWN_VEC')
         row.operator("view3d.display_modifiers_collapse", icon = 'DISCLOSURE_TRI_RIGHT_VEC')  



###########################
### Curve Visualization ###  
###########################
   
     ###space###      
     if lt.display_curvevisual:
         ###space###         
         box = layout.box()
         row = box.row(1)                    
         row.prop(lt, "display_curvevisual", text="", icon='TRIA_DOWN')
     
     else:
         box = layout.box()
         row = box.row(1)        
         row.prop(lt, "display_curvevisual", text="", icon='TRIA_RIGHT')        
         row.label("Visual...")    

         row.menu("wkst.display_menu", text="", icon ="UI")              
         row.menu("wkst.meshdisplay_menu", text="", icon ="META_CUBE")    
         row.operator("object.wire_all", text="", icon='WIRE')

       
     ###space###                  
     if lt.display_curvevisual:
         ###space### 
         col = layout.column(align=True) 
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.row(align=True)
         row.operator("wm.context_toggle", text="Xray", icon='META_CUBE').data_path = "object.show_x_ray"
         row.operator("object.wire_all", text="Wire all", icon='WIRE')

         col = layout.column(align=True) 
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.row(align=True)
         row.prop(context.active_object.data, "show_handles", text="Handles")
         row.prop(context.active_object.data, "show_normal_face", text="Normals")
         row = col_top.row(align=True)
         row.prop(context.scene.tool_settings, "normal_size", text="Normal Size")

         col = layout.column(align=True) 
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.row(align=True)
         row.prop(context.space_data.fx_settings, "use_ssao", text="AOccl", icon="GROUP")
         row.prop(context.space_data, "use_matcap", icon ="MATCAP_22")         
         if context.space_data.use_matcap:
             row = col_top.row(align=True)
             row.scale_y = 0.2
             row.scale_x = 0.5
             row.template_icon_view(context.space_data, "matcap_icon") 

         col = layout.column(align=True) 
         box = col.column(align=True).box().column()       
         col_top = box.column(align=True)                    

         row = col_top.row(align=True)
         row.prop(context.space_data, "show_only_render", text="Render", icon ="RESTRICT_RENDER_ON")
         row.prop(context.space_data, "show_floor", text="Grid", icon ="GRID")    
        
         row = col_top.row(align=True)
         row.prop(context.space_data, "show_world", "World" ,icon ="WORLD")
        
         sub = row.row(1)
         sub.scale_x = 0.335
         sub.prop(context.space_data, "show_axis_x", text="X", toggle=True)
         sub.prop(context.space_data, "show_axis_y", text="Y", toggle=True)
         sub.prop(context.space_data, "show_axis_z", text="Z", toggle=True)





     col = layout.column(align=True) 
     box = col.column(align=True).box().column()       
     col_top = box.column(align=True)                    

     row = col_top.row(align=True)
     row.prop(context.object.data, "dimensions", expand=True)


     
#####  Mirror XYZ Local  ##########        

class loop4(bpy.types.Operator):
    """mirror over X axis / local"""                 
    bl_idname = "object.loops4"          
    bl_label = "mirror selected on X axis > local"                  
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(True, False, False), constraint_orientation='LOCAL')
       
        return {'FINISHED'}

                         
############------------############
############  REGISTER  ############
############------------############

# registering and menu integration
def register():

    bpy.utils.register_module(__name__)

# unregistering and removing menus
def unregister():

    bpy.utils.unregister_module(__name__)
    
    try:
        del bpy.types.WindowManager.retopowindowtool
    except:
        pass


if __name__ == "__main__":
    register()


