#bl_info = {
#    "name": "Spacebar Special",
#    "author": "Multiple Authors, mkbreuer",
#    "version": (0, 1, 0),
#    "blender": (2, 7, 2),
#    "location": "View3D",
#    "description": "",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "User Menu"}




import bpy, re
from bpy import *


#########################################################################################################################################################
#########################################################################################################################################################
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus   
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus   
#########################################################################################################################################################
#########################################################################################################################################################


######  Subdivide  ##################-------------------------------------------------------                         
######  Subdivide  ##################-------------------------------------------------------                         

class SubdivideCUT(bpy.types.Menu):
    bl_label = "Subdivide"
    bl_idname = "space_subdivide"
    
    def draw(self, context):
        layout = self.layout

        layout.operator("mesh.subdivide",text="1-Cut").number_cuts=1
        layout.operator("mesh.subdivide",text="2-Cuts").number_cuts=2
        layout.operator("mesh.subdivide",text="3-Cuts").number_cuts=3
        layout.operator("mesh.subdivide",text="4-Cuts").number_cuts=4
        layout.operator("mesh.subdivide",text="5-Cuts").number_cuts=5
        layout.operator("mesh.subdivide",text="6-Cuts").number_cuts=6 

bpy.utils.register_class(SubdivideCUT)




######  Flymode  ##################-------------------------------------------------------                         
######  Flymode  ##################-------------------------------------------------------                         

class Navigatestop(bpy.types.Operator):
    bl_idname = "view3d.fast_navigate_stop_new"
    bl_label = "Navigate Stop"

    def execute(self, context):
        bpy.ops.view3d.fast_navigate_stop()
        bpy.context.space_data.viewport_shade = 'SOLID'
       
        return {'FINISHED'}

bpy.utils.register_class(Navigatestop)     

class View3D_Modifly(bpy.types.Menu):
    bl_label = "Flymode"
    bl_idname = "space_modifly"
    
    def draw(self, context):
        active_obj = context.active_object
        layout = self.layout
        
        scene = context.scene

        layout.operator("view3d.fast_navigate_operator", icon = "MOD_SOFT")
        layout.operator("view3d.fast_navigate_stop_new")
        
        layout.separator()
                
        layout.prop(scene,"OriginalMode", "")
     
        layout.prop(scene,"FastMode", "")
        
        layout.separator()
        
        layout.prop(scene,"EditActive", "Edit mode")
        
        layout.separator()
        
        layout.prop(scene,"Delay")
        layout.prop(scene,"DelayTimeGlobal")

        layout.separator()
        
        layout.prop(scene,"ShowParticles")
        layout.prop(scene,"ParticlesPercentageDisplay")

bpy.utils.register_class(View3D_Modifly)         



#############################################################################################################################################################
#############################################################################################################################################################
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
#############################################################################################################################################################
#############################################################################################################################################################
  
######  Special Menu  ######-------------------------------------------------------   
######  Special Menu  ######-------------------------------------------------------   

class VIEW3D_Space_Special(bpy.types.Menu):
    bl_label = "Special Edit"
    bl_idname = "space_special"    

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'


##########--------------##########
##########  Objectmode  ##########
##########--------------##########  

        ob = context
        if ob.mode == 'OBJECT':

    
            layout.operator("object.join", text="Join Object", icon='AUTOMERGE_ON')
            layout.operator("object.set_instance", text="Set as Instance") 

            layout.separator()
                         
            layout.operator("object.duplicate_move", text="Duplicate Objects")
            layout.operator("object.duplicate_move_linked", text="Duplicate Linked Objects")


            layout.separator()
            
            layout.operator("mesh.intersect_meshes",text="Intersection Line", icon="GROUP")
            layout.operator("object.editnormals_transfer",text="Transfer Normals", icon="SNAP_NORMAL")  

            layout.separator()
                
            layout.operator("object.convert",text="Convert to Mesh", icon = "OUTLINER_DATA_MESH").target="MESH"
            layout.operator("object.convert",text="Convert to Curve", icon = "OUTLINER_DATA_CURVE").target="CURVE"  

            layout.separator()

            layout.menu("htk_modispace", text="Modifier", icon='MODIFIER')                
            layout.menu("htk_relation", text="Relations", icon='LINK_AREA')

            layout.menu("htk_booltool", text="BoolTools", icon='GROUP')
            layout.operator("cgcookie.polystrips", icon='IPO_BEZIER') 
            layout.operator("cgcookie.retop_contour", text="Contour Retopogly", icon='MESH_UVSPHERE')     
            
            layout.separator()             
            
            props = layout.operator("object.isolate_type_render")
            props = layout.operator("object.hide_render_clear_all")

            layout.separator()  

            layout.menu("VIEW3D_AnimationPlayer", text="Play Animation", icon = "TRIA_RIGHT") 
         

##########------------##########
##########  Editmode  ##########
##########------------##########

        elif ob.mode == 'EDIT_MESH':


            layout.menu("space_modifier")  
            layout.menu("VIEW3D_MT_edit_mesh_looptools")
        
            layout.separator() 
        
            layout.menu("space_subdivide", text="Subdivide", icon='PARTICLE_POINT') 
            layout.operator("mesh.unsubdivide", text="Un-Subdivide")                                   
            layout.operator("mesh.subdivide", text="Subdivide Smooth").smoothness = 1.0

            layout.separator()

            layout.operator("mesh.merge", text="Merge...", icon = "FULLSCREEN_EXIT")
            layout.operator("mesh.remove_doubles")

            layout.separator()

            props = layout.operator("mesh.knife_tool", text="Knife", icon = "LINE_DATA")
            props.use_occlude_geometry = True
            props.only_selected = False
            props = layout.operator("mesh.knife_tool", text="Select")
            props.use_occlude_geometry = False
            props.only_selected = True
            layout.operator("mesh.knife_project")
          
            layout.separator() 
            
            layout.operator("mesh.bisect")  

            layout.separator()              
            
            layout.operator("mesh.bevel", text="Bevel", icon = "SPHERECURVE")        
            layout.operator("mesh.inset")        
            layout.operator("mesh.bridge_edge_loops")     
        
            layout.separator()        
        
            layout.operator("mesh.vertices_smooth", text="Vertices Smooth", icon = "CURVE_DATA")        
            layout.operator("mesh.vertices_smooth_laplacian", text="Laplacian Smooth")            

            layout.separator()               
            layout.operator_menu_enum("mesh.separate", "type", text="Separate")

            layout.separator()
            
            layout.operator("mesh.symmetrize")
            layout.operator("mesh.symmetry_snap")

            layout.separator() 
                  
            layout.operator("mesh.blend_from_shape")
            layout.operator("mesh.shape_propagate_to_all")
            layout.operator("mesh.shortest_path_select")
            layout.operator("mesh.sort_elements")
            

##########---------##########
##########  Curve  ##########
##########---------##########            
        
        if ob.mode == 'EDIT_CURVE':

            #layout.operator("curve.subdivide")
            #layout.operator("curve.switch_direction")
            #layout.operator("curve.spline_weight_set")
            #layout.operator("curve.radius_set")
            layout.operator("curve.smooth")
            layout.operator("curve.smooth_weight")
            layout.operator("curve.smooth_radius")
            layout.operator("curve.smooth_tilt") 
                          

##########-----------##########
##########  Surface  ##########
##########-----------########## 
 
        if ob.mode == 'EDIT_SURFACE':

            #layout.operator("curve.subdivide")
            #layout.operator("curve.switch_direction")
            #layout.operator("curve.spline_weight_set")
            #layout.operator("curve.radius_set")
            layout.operator("curve.smooth")
            layout.operator("curve.smooth_weight")
            layout.operator("curve.smooth_radius")
            layout.operator("curve.smooth_tilt") 
                          
                          
##########------------##########
##########  Metaball  ##########
##########------------##########                 
        
        if ob.mode == 'EDIT_METABALL':

            layout.operator("mball.duplicate_metaelems", icon='PLUS')       

        
##########-----------##########
##########  Lattice  ##########
##########-----------##########
        
        elif ob.mode == 'EDIT_LATTICE':

            layout.menu("VIEW3D_MT_TransformMenu", icon='SOLO_OFF')  
                   

##########------------##########
##########  Particle  ##########
##########------------##########
   
        if  context.mode == 'PARTICLE':

            layout.menu("VIEW3D_MT_brush", icon='BRUSH_DATA') 


##########---------------##########
##########  Weightpaint  ##########
##########---------------##########

        ob = context
        if ob.mode == 'PAINT_WEIGHT':
      
            layout.operator("mesh.weightlifterweight", text="Weight Lifter", icon='PLUGIN')

            layout.operator("mesh.slope2vgroup", text="Slope 2 VertGroup", icon='PLUGIN')
            layout.operator("mesh.height2vgroup", text="Height 2 VertGroup", icon='PLUGIN')        
            
            layout.separator()  
  
            layout.operator("mesh.visiblevertices", text="Visible Vertices in Cam View", icon='PLUGIN')

                                        

##########---------------##########
##########  Vertexpaint  ##########
##########---------------##########   
         
        elif ob.mode == 'PAINT_VERTEX':

            #layout.operator("paint.vertex_color_set")

            layout.operator("paint.vertex_color_set", text="Set Color ", icon='VPAINT_HLT')
            layout.operator("paint.vertex_color_smooth", text="Smooth Color ")

            layout.operator("mesh.connected_vertex_colors", text="Connected Vertex Colors")
            
            layout.separator()        
    
            layout.operator("paint.vertex_color_dirt", text="Dirt Color ", icon='TPAINT_HLT')

            layout.operator("paint.worn_edges", text="Worn Edges")
        
         
                        

##########----------------##########
##########  Texturepaint  ##########
##########----------------##########            

        elif ob.mode == 'PAINT_TEXTURE':
            
            layout.menu("VIEW3D_MT_brush", icon='BRUSH_DATA')
            


##########--------------##########
##########  Sculptmode  ##########
##########--------------##########            

        elif ob.mode == 'SCULPT':
    
           props = layout.operator("paint.hide_show", text="Box Hide", icon = "BORDER_RECT")
           props.action = 'HIDE'
           props.area = 'INSIDE'
        
           props = layout.operator("paint.hide_show", text="Box Show")
           props.action = 'SHOW'
           props.area = 'INSIDE' 

           layout.separator()
        
           props = layout.operator("paint.mask_flood_fill", text="Fill Mask", icon = "BORDER_RECT")
           props.mode = 'VALUE'
           props.value = 1
               
           props = layout.operator("paint.mask_flood_fill", text="Clear Mask")
           props.mode = 'VALUE'
           props.value = 0
        
           layout.operator("paint.mask_flood_fill", text="Invert Mask").mode='INVERT' 
       
           layout.separator()

           props = layout.operator("paint.hide_show", text="Show All", icon = "RESTRICT_VIEW_OFF")
           props.action = 'SHOW'
           props.area = 'ALL'
        
           props = layout.operator("paint.hide_show", text="Hide Masked", icon = "RESTRICT_VIEW_ON")
           props.area = 'MASKED'
           props.action = 'HIDE'
        

##########------------##########
##########  Armature  ##########
##########------------##########            

        elif ob.mode == 'EDIT_ARMATURE':

            layout.operator_context = 'INVOKE_REGION_WIN'

            layout.operator("armature.subdivide", text="Subdivide")
            layout.operator("armature.switch_direction", text="Switch Direction")

            layout.separator()

            layout.operator_context = 'EXEC_REGION_WIN'
            layout.operator("armature.autoside_names", text="AutoName Left/Right").type = 'XAXIS'
            layout.operator("armature.autoside_names", text="AutoName Front/Back").type = 'YAXIS'
            layout.operator("armature.autoside_names", text="AutoName Top/Bottom").type = 'ZAXIS'
            layout.operator("armature.flip_names", text="Flip Names")




##########------------##########
##########  Posemode  ##########
##########------------##########            

        if context.mode == 'POSE':
            
            arm = context.active_object.data  
             
            layout.operator("paint.weight_from_bones", text="Assign Automatic from Bones").type = 'AUTOMATIC'
            layout.operator("paint.weight_from_bones", text="Assign from Bone Envelopes").type = 'ENVELOPES'

            layout.separator()

            layout.operator("pose.select_constraint_target")
            layout.operator("pose.flip_names")
            layout.operator("pose.paths_calculate")
            layout.operator("pose.paths_clear")
            layout.operator("pose.user_transforms_clear")
            layout.operator("pose.user_transforms_clear", text="Clear User Transforms (All)").only_selected = False
            layout.operator("pose.relax")

            layout.separator()

            layout.operator_menu_enum("pose.autoside_names", "axis")
           


###########################################################################################################################################################
###########################################################################################################################################################
### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator  
### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator 
###########################################################################################################################################################
###########################################################################################################################################################


def abs(val):
    if val > 0:
        return val
    return -val


def register():
        
    bpy.utils.register_class(VIEW3D_Space_Special)

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_class(VIEW3D_Space_Special)

    bpy.utils.unregister_module(__name__)  


if __name__ == "__main__":
    register() 	

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_Space_Special.bl_idname)
  
  
  
   








































