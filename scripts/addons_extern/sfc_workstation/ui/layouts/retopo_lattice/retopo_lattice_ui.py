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

class DropdownRetopoLATTICEToolProps(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.retopowindowlattice
    """
    display_selectionlatt = bpy.props.BoolProperty(name = "Selection", description = "Display Selection Tools", default = False)
    display_alignlatt = bpy.props.BoolProperty(name = "Align", description = "Display Align Tools", default = False)
    display_orientlatt = bpy.props.BoolProperty(name = "Origin & Snap to", description = "Display Origin & Snap to Tools", default = False)
    display_shadinglatt = bpy.props.BoolProperty(name = "Visualization", description = "Display Visualization Tools", default = False)
    display_transformlatt = bpy.props.BoolProperty(name = "Transform", description = "Display Selection Tools", default = False)
    display_view = bpy.props.BoolProperty(name = "View", description = "Display View Tools", default = False)

bpy.utils.register_class(DropdownRetopoLATTICEToolProps)
bpy.types.WindowManager.retopowindowlattice = bpy.props.PointerProperty(type = DropdownRetopoLATTICEToolProps)





def draw_retopo_lattice_ui(self, context, layout):
     ###space### 
     lt = context.window_manager.retopowindowlattice        
     layout = self.layout
     obj = context.object


     box = layout.box()
     row = box.row(1)  
     sub = row.row(1)
     sub.scale_x = 7
     sub.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
     sub.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
     sub.operator("view3d.pivot_active", "", icon="ROTACTIVE")
     sub.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
     sub.operator("view3d.pivot_median", "", icon="ROTATECENTER")  

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

#########################           
### Lattice Selection ###
#########################

     if lt.display_selectionlatt:
         box = layout.box()
         row = box.row(1)                       
         row.prop(lt, "display_selectionlatt", text="", icon='TRIA_DOWN')
         row.label("Selections...")

     else:
         box = layout.box()
         row = box.row(1)              
         row.prop(lt, "display_selectionlatt", text="", icon='TRIA_RIGHT')    
         row.label("Selections...")

         row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")  
         row.operator("view3d.select_border", text="", icon="BORDER_RECT")        

     if lt.display_selectionlatt:

         col = layout.column(align=True)                          
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.row(align=True)
         row.operator("view3d.select_border", text="Border", icon="BORDER_RECT") 
         row.operator("view3d.select_circle", text="Circle", icon="BORDER_LASSO")              


         col = layout.column(align=True)
         box = col.column(align=True).box().column(True)
         col_top = box.column(align=True)
        
         row = col_top.row(align=True) 
         row.operator("lattice.select_mirror", text="Mirror")
         row.operator("lattice.select_random", text="Random")

         col_top = box.column(align=True)
         row = col_top.row(align=True)            
         row.operator("lattice.select_all").action = 'TOGGLE'
         row.operator("lattice.select_all", text="Inverse").action = 'INVERT'

         col_top = box.column(align=True)
         row = col_top.row(align=True)
         row.operator("lattice.select_ungrouped", text="Ungrouped Verts")                


#####################           
### Lattice Pivot ###
#####################

     if lt.display_orientlatt:
         box = layout.box()
         row = box.row(1)                       
         row.prop(lt, "display_orientlatt", text="", icon='TRIA_DOWN')
         row.label("Pivot...")

     else:
         box = layout.box()
         row = box.row(1)              
         row.prop(lt, "display_orientlatt", text="", icon='TRIA_RIGHT')    
         row.label("Pivot...")
         
         row.menu("origin.setupmenu_edm", "", icon="LAYER_ACTIVE")
         row.menu("wkst.snaptocursor","", icon="FORCE_FORCE")
         row.menu("wkst.snaptoselect","", icon="RESTRICT_SELECT_OFF")  

     if lt.display_orientlatt:           
        
         col = layout.column(align=True) 
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)
         row = col_top.row(align=True) 
         row.operator("object.origin_obm", "Ob-Mode", icon = "OBJECT_DATAMODE")
         row.operator("object.origin_edm", "Ed-Mode", icon = "EDITMODE_HLT")                                             

         col = layout.column(align=True)  
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)
         
         row = col_top.row(align=True)
         row.menu("wkst.snaptocursor","Cursor to... ", icon="FORCE_FORCE")     
                   
         row = col_top.row(align=True)
         row.menu("wkst.snaptoselect","Selection to... ", icon="RESTRICT_SELECT_OFF")
          


######################### 
### Lattice Transform ###
#########################
                    
     if lt.display_transformlatt:
         box = layout.box()
         row = box.row(1)                         
         row.prop(lt, "display_transformlatt", text="", icon='TRIA_DOWN')
         row.label("Transform...")        

     else:
         box = layout.box()
         row = box.row(1)              
         row.prop(lt, "display_transformlatt", text="", icon='TRIA_RIGHT')    
         row.label("Transform...")

         row.menu("VIEW3D_MT_mirror","", icon="ARROW_LEFTRIGHT") 
         row.menu("wkst.normal_transform_menu","", icon="AXIS_SIDE")  
         row.menu("wkst.transform_menu","", icon="MANIPUL")   
 

     if lt.display_transformlatt:

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
         row.operator("lattice.flip", text="FlipX").axis = "U"
         row.operator("lattice.flip", text="FlipY").axis = "V"
         row.operator("lattice.flip", text="FlipZ").axis = "W"

         row = col_top.row(align=True)         
         row.operator("object.mirror1",text="MX", icon='ARROW_LEFTRIGHT')
         row.operator("object.mirror2",text="MY", icon='ARROW_LEFTRIGHT')
         row.operator("object.mirror3",text="MZ", icon='ARROW_LEFTRIGHT')            

         col = layout.column(align=True)                      
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)
         
         row = col_top.row(align=True)
         row.operator("transform.push_pull", text="Push/Pull")        
         row.operator("transform.tosphere", "to Sphere")            
         



#####################            
### Lattice Align ###
#####################

     if lt.display_alignlatt:
         box = layout.box()
         row = box.row(1)                       
         row.prop(lt, "display_alignlatt", text="", icon='TRIA_DOWN')
         row.label("Align...")  

     else:
         box = layout.box()
         row = box.row(1)              
         row.prop(lt, "display_alignlatt", text="", icon='TRIA_RIGHT')
    
         row.label("Align...")      
         sub = row.row(1)
         sub.scale_x = 0.35             
         sub.operator("mesh.face_align_x", "X", icon='TRIA_RIGHT')
         sub.operator("mesh.face_align_y", "Y", icon='TRIA_UP')           
         sub.operator("mesh.face_align_z", "Z", icon='SPACE3') 

     if lt.display_alignlatt:

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


     col = layout.column(align=True) 
     box = col.column(align=True).box().column()       
     col_top = box.column(align=True)                    

     row = col_top.row(align=True)

     row.prop(context.object.data, "use_outside")
     row.prop_search(context.object.data, "vertex_group", context.object, "vertex_groups", text="")   

     col = layout.column(align=True) 
     box = col.column(align=True).box().column()       
     col_top = box.column(align=True)                    

     row = col_top.row(align=True)
     row.prop(context.object.data, "points_u", text="X")
     row.prop(context.object.data, "points_v", text="Y")
     row.prop(context.object.data, "points_w", text="Z")
 
     row = col_top.row(align=True)
     row.prop(context.object.data, "interpolation_type_u", text="")
     row.prop(context.object.data, "interpolation_type_v", text="")
     row.prop(context.object.data, "interpolation_type_w", text="")  

     col = layout.column(align=True) 
     box = col.column(align=True).box().column()       
     col_top = box.column(align=True)                    

     row = col_top.row(align=True)
     row.operator("lattice.make_regular", "Make Regular", icon ="LATTICE_DATA")


#############################
### Lattice Visualization ###  
#############################
   
     ###space1###
     #col = layout.column(align=True)        
     if lt.display_shadinglatt:
         ###space2###         
         box = layout.box()
         row = box.row(1)                    
         row.prop(lt, "display_shadinglatt", text="", icon='TRIA_DOWN')
         row.label("Visual...")        

     else:
         box = layout.box()
         row = box.row(1)        
         row.prop(lt, "display_shadinglatt", text="", icon='TRIA_RIGHT')        
         row.label("Visual...")        

         row.menu("wkst.display_menu", text="", icon ="UI") 
         row.menu("wkst.meshdisplay_menu", text="", icon ="META_CUBE")     
         row.operator("object.wire_all", text="", icon='WIRE')
  
     
     ###space1###                  
     if lt.display_shadinglatt:
         col = layout.column(align=True) 
         ###space2### 
         box = col.column(align=True).box().column()
         col_top = box.column(align=True)

         row = col_top.row(align=True)
         row.operator("wm.context_toggle", text="Xray", icon='META_CUBE').data_path = "object.show_x_ray"

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


     ###--------------------- 







#####  Mirror XYZ Local  #########################################################################################        

class loop4(bpy.types.Operator):
    """mirror over X axis / local"""                 
    bl_idname = "object.loops4"          
    bl_label = "mirror selected on X axis > local"                  
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(True, False, False), constraint_orientation='LOCAL')
       
        return {'FINISHED'}
        

class loop5(bpy.types.Operator):
    """mirror over Y axis / local"""                
    bl_idname = "object.loops5"         
    bl_label = "mirror selected on Y axis > local"                 
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(False, True, False), constraint_orientation='LOCAL')
        
        return {'FINISHED'}        


class loop6(bpy.types.Operator):
    """mirror over Z axis / local"""                 
    bl_idname = "object.loops6"        
    bl_label = "mirror selected on Z axis > local"                  
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(False, False, True), constraint_orientation='LOCAL')
        
        return {'FINISHED'}


######################################################################################################################################################
############------------############
############  REGISTER  ############
############------------############
######################################################################################################################################################



# registering and menu integration
def register():

    bpy.utils.register_module(__name__)



    
# unregistering and removing menus
def unregister():

    bpy.utils.unregister_module(__name__) 

    
    try:
        del bpy.types.WindowManager.retopowindowlattice
    except:
        pass


if __name__ == "__main__":
    register()

