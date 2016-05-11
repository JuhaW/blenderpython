#bl_info = {
#    "name": "Spacebar Selections",
#    "author": "Multiple Authors, mkbreuer",
#    "version": (0, 1, 0),
#    "blender": (2, 7, 2),
#    "location": "3D View",
#    "description": "",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "User Menu"}




import bpy
from bpy import *


#############################################################################################################################################################
#############################################################################################################################################################
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ###  
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ###  
#############################################################################################################################################################
#############################################################################################################################################################

#######  Additional  #######-------------------------------------------------------                  
#######  Additional  #######-------------------------------------------------------        

class AdditionalMenu(bpy.types.Menu):
    bl_label = "Additional Mesh Selection"
    bl_idname = "additionalmenu"
        
    def draw(self, context):
        layout = self.layout
          
        layout.operator("mesh.edges_select_sharp", text="Sharp", icon="SNAP_EDGE")                          
        layout.operator("mesh.select_random", text="Random", icon ="ANIM_DATA")
        layout.operator("mesh.select_nth",text="Nth Selected" ,icon="RNDCURVE")                            

        layout.separator()

        layout.operator("mesh.region_to_loop", text = "Edge Boundry Loop")
        layout.operator("mesh.loop_to_region", text = "Edge Loop Inner-Region") 
                   
bpy.utils.register_class(AdditionalMenu)


#######  Vertex Group  #######-------------------------------------------------------                  
#######  Vertex Group  #######-------------------------------------------------------        

class VGroupMenu(bpy.types.Menu):
    bl_label = "Vertex Group"
    bl_idname = "vgroupmenu"
        
    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("object.vertex_group_select", text="Select Group", icon="RESTRICT_SELECT_OFF")
        layout.operator("object.vertex_group_deselect", text="Deselect Group", icon="RESTRICT_SELECT_ON")    
            
        layout.separator()
            
        layout.operator("object.vertex_group_assign", text="Assign Group", icon="ZOOMIN")
        layout.operator("object.vertex_group_remove_from", text="Remove Group", icon="ZOOMOUT") 
            
        layout.separator()
                      
        layout.operator("object.vertex_group_add",icon='GROUP_VERTEX',text="Add Vertex Group")
        layout.operator("object.vertex_group_remove",icon='GROUP_VERTEX',text="Remove Vertex Group").all=False           
            
bpy.utils.register_class(VGroupMenu)            


#############################################################################################################################################################
#############################################################################################################################################################
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
#############################################################################################################################################################
#############################################################################################################################################################

######  Selection Menu  #######-------------------------------------------------------
######  Selection Menu  #######-------------------------------------------------------

class VIEW3D_Space_Selection(bpy.types.Menu):
    bl_label = "Selection"
    bl_idname = "space_selection"   


    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'


####### Object menu ------------------------------------------------        
####### Object menu ------------------------------------------------

        ob = context
        if ob.mode == 'OBJECT':

            layout.operator("view3d.select_border", icon ="BORDER_RECT")
            layout.operator("view3d.select_circle", icon ="BORDER_LASSO")
            layout.operator("object.select_all")             

            layout.separator()

            layout.operator("object.select_linked", text="Linked", icon = "LINKED") 
            layout.operator("object.select_grouped", text="Group")        
            layout.operator("object.select_by_type", text="Type")        

            layout.separator()

            layout.operator("object.select_by_layer", text="Layer", icon = "SEQ_SEQUENCER")
            layout.operator("object.select_pattern", text="Name")
            layout.operator("object.select_camera", text="Camera")

            layout.separator()

            layout.operator("object.select_random", text="Random", icon = "RNDCURVE")            
            layout.operator("object.select_all", text="Inverse").action = 'INVERT'
            layout.operator("object.select_mirror", text="Mirror")
       

####### Edit menu ------------------------------------------------        
####### Edit menu ------------------------------------------------

        elif ob.mode == 'EDIT_MESH':

            layout.operator("view3d.select_border", icon ="BORDER_RECT")
            layout.operator("view3d.select_circle", icon ="BORDER_LASSO")
            layout.operator("mesh.select_all") 
        
            
            layout.separator()
        
            layout.operator("mesh.select_linked",text="Linked", icon = "LINKED")
            layout.operator("mesh.select_similar",text="Similar")              
            layout.operator("mesh.select_all", text="Inverse").action = 'INVERT'  

            layout.separator()
                        
            layout.operator("mesh.select_face_by_sides",text="By Side", icon = "SNAP_FACE")
            layout.operator("mesh.select_axis", text="Active Side")
            layout.operator("mesh.faces_select_linked_flat", text="Linked Faces") 
            
            layout.separator()
            
            layout.operator("mesh.select_loose",text="Loose", icon="STICKY_UVS_DISABLE")
            if context.scene.tool_settings.mesh_select_mode[2] is False:
                layout.operator("mesh.select_non_manifold", text="Non Manifold")  
            layout.operator("mesh.select_interior_faces", text="Interior Faces")                         
           
            layout.separator()
                            
            layout.menu("additionalmenu", text ="Additional", icon="RESTRICT_SELECT_OFF")   

            layout.separator()
                            
            layout.operator("mesh.loop_multi_select",text="Edge Loop  [ALT+]", icon="ZOOMOUT").ring=False
            layout.operator("mesh.e2e_evnfe", text="Edge Loop+")                     

            layout.separator()
            
            layout.operator("mesh.loop_multi_select",text="Edge Ring  [ALT+CTRL]", icon="COLLAPSEMENU").ring=True
            layout.operator("mesh.e2e_efnve", text="Edge Ring+")

            layout.separator()
      
            layout.menu("vgroupmenu", icon="GROUP_VERTEX")
            layout.menu("MESH_MT_vertex_group_specials", icon='DOWNARROW_HLT', text="Vertex Group Specials")                          		

                               

####### Curve menu ------------------------------------------------        
####### Curve menu ------------------------------------------------

        if ob.mode == 'EDIT_CURVE':
            
            layout.operator("view3d.select_border", icon ="BORDER_RECT")
            layout.operator("view3d.select_circle", icon ="BORDER_LASSO")
            layout.operator("curve.select_all").action = 'TOGGLE'            

            layout.separator()

            layout.operator("curve.select_linked", text="Linked", icon = "LINKED") 
            layout.operator("curve.select_all", text="Inverse").action = 'INVERT'
            layout.operator("curve.select_nth",text="Nth Selected") 
            layout.operator("curve.select_random") 
            
            layout.separator()

            layout.operator("curve.de_select_first", text = "Select First", icon = "TRIA_UP") 
            layout.operator("curve.de_select_last", text = "Select Last", icon = "TRIA_DOWN") 
    
            layout.separator()
                        
            layout.operator("curve.select_next", icon = "TRIA_RIGHT") 
            layout.operator("curve.select_previous", icon = "TRIA_LEFT") 


            layout.separator()

            layout.operator("curve.select_more", text="More", icon="ZOOMIN") 
            layout.operator("curve.select_less", text="Less", icon="ZOOMOUT")




####### Surface menu ----------------------------------------------
####### Surface menu ----------------------------------------------
       
        if ob.mode == 'EDIT_SURFACE':
            
            layout.operator("view3d.select_border", icon ="BORDER_RECT")
            layout.operator("view3d.select_circle", icon ="BORDER_LASSO")
            layout.operator("curve.select_all").action = 'TOGGLE'            

            layout.separator()

            layout.operator("curve.select_linked", text="Linked", icon = "LINKED") 
            layout.operator("curve.select_all", text="Inverse").action = 'INVERT'
            layout.operator("curve.select_nth",text="Nth Selected") 
            layout.operator("curve.select_random") 
            
            layout.separator()

            layout.operator("curve.select_more", text="More", icon="ZOOMIN") 
            layout.operator("curve.select_less", text="Less", icon="ZOOMOUT")

         

####### Metaball menu ---------------------------------------------
####### Metaball menu ---------------------------------------------

        if ob.mode == 'EDIT_METABALL':
            
            layout.operator("view3d.select_border", icon ="BORDER_RECT")
            layout.operator("view3d.select_circle", icon ="BORDER_LASSO")
            layout.operator("mball.select_all").action = 'TOGGLE'
            
            layout.separator()
            
            layout.operator_menu_enum("mball.select_similar", "type", text="Similar") 
            layout.operator("mball.select_all", text="Inverse").action = 'INVERT'
            layout.operator("mball.select_random_metaelems") 



####### Lattice menu ----------------------------------------------
####### Lattice menu ----------------------------------------------
   
        elif ob.mode == 'EDIT_LATTICE':
            
            layout.operator("view3d.select_border", icon ="BORDER_RECT")
            layout.operator("view3d.select_circle", icon ="BORDER_LASSO")
            layout.operator("lattice.select_all").action = 'TOGGLE'
            
            layout.separator()

            layout.operator("lattice.select_mirror", text="Mirror", icon = "ARROW_LEFTRIGHT")
            layout.operator("lattice.select_all", text="Inverse").action = 'INVERT'
            layout.operator("lattice.select_random") 

            layout.separator()

            layout.menu("vgroupmenu", icon="GROUP_VERTEX")   
            
            layout.separator()

            layout.operator("lattice.select_ungrouped", text="Ungrouped Verts")
            
            

####### Particle menu ---------------------------------------------
####### Particle menu ---------------------------------------------                       

        if  context.mode == 'PARTICLE':
       
            layout.operator("view3d.select_border", icon ="BORDER_RECT")
            layout.operator("particle.select_all", icon="RESTRICT_SELECT_OFF").action = 'TOGGLE'

            layout.separator()

            layout.operator("particle.select_tips", text = "Tips", icon = "IPO_EASE_OUT")  
            layout.operator("particle.select_roots", text = "Roots")

            layout.separator()

            layout.operator("particle.select_linked", text="Linked", icon = "LINKED") 
            layout.operator("particle.select_all", text="Inverse").action = 'INVERT'

            layout.separator()

            layout.operator("particle.select_more", text="More", icon="ZOOMIN")
            layout.operator("particle.select_less", text="Less", icon="ZOOMOUT")
      


####### Weight paint menu -----------------------------------------
####### Weight paint menu -----------------------------------------

        ob = context
        if ob.mode == 'PAINT_WEIGHT':

            layout.operator("wm.search_menu", text="Search", icon='VIEWZOOM')           
            


####### Vertex paint menu -----------------------------------------
####### Vertex paint menu -----------------------------------------
       
        elif ob.mode == 'PAINT_VERTEX':

            layout.operator("wm.search_menu", text="Search", icon='VIEWZOOM')
            

####### Texture paint menu ----------------------------------------
####### Texture paint menu ----------------------------------------

        elif ob.mode == 'PAINT_TEXTURE':

            layout.operator("wm.search_menu", text="Search", icon='VIEWZOOM')


####### Sculpt menu -----------------------------------------------
####### Sculpt menu -----------------------------------------------           

        elif ob.mode == 'SCULPT':

            layout.operator("wm.search_menu", text="Search", icon='VIEWZOOM')


####### Armature menu ---------------------------------------------
####### Armature menu --------------------------------------------- 

        elif ob.mode == 'EDIT_ARMATURE':

            arm = context.active_object.data 

            layout.operator("view3d.select_border", icon ="BORDER_RECT")
            layout.operator("view3d.select_circle", icon ="BORDER_LASSO")
            layout.operator("armature.select_all").action = 'TOGGLE'
            
            layout.separator()
            
            layout.operator("armature.select_mirror", text="Mirror", icon = "ARROW_LEFTRIGHT").extend = False
            layout.operator("armature.select_all", text="Inverse").action = 'INVERT'

            layout.separator()

            layout.operator("armature.select_hierarchy", text="Parent", icon="BONE_DATA").direction = 'PARENT'
 
            props = layout.operator("armature.select_hierarchy", text="Extend Parent")
            props.extend = True
            props.direction = 'PARENT'
                        
            layout.operator("armature.select_hierarchy", text="Child", icon="CONSTRAINT_BONE").direction = 'CHILD'

            props = layout.operator("armature.select_hierarchy", text="Extend Child")
            props.extend = True
            props.direction = 'CHILD'

            layout.separator()  

            layout.operator_menu_enum("armature.select_similar", "type", text="Similar")
            layout.operator("object.select_pattern", text="Select Pattern...")
            
            layout.separator()

            layout.operator("armature.select_more", text="More", icon="ZOOMIN")
            layout.operator("armature.select_less", text="Less", icon="ZOOMOUT")
            
                        

####### Pose mode menu --------------------------------------------
####### Pose mode menu -------------------------------------------- 

        if context.mode == 'POSE':

            arm = context.active_object.data   
    
            layout.operator("view3d.select_border", icon ="BORDER_RECT")
            layout.operator("view3d.select_circle", icon ="BORDER_LASSO")
            layout.operator("pose.select_all").action = 'TOGGLE'
            
            layout.separator()

            layout.operator("pose.select_all", text="Inverse").action = 'INVERT'
            layout.operator("pose.select_mirror", text="Flip Active")
            layout.operator("pose.select_constraint_target", text="Constraint Target", icon ="LINK_AREA")
            layout.operator("pose.select_linked", text="CONSTRAINT_BONE", icon="CONSTRAINT") 

            layout.separator()

            layout.operator("pose.select_hierarchy", text="Parent", icon ="BONE_DATA").direction = 'PARENT'
            props = layout.operator("pose.select_hierarchy", text="Extend Parent")
            props.extend = True
            props.direction = 'PARENT'
            
            layout.separator()
                                    
            layout.operator("pose.select_hierarchy", text="Child", icon ="CONSTRAINT_BONE").direction = 'CHILD'

            props = layout.operator("pose.select_hierarchy", text="Extend Child")
            props.extend = True
            props.direction = 'CHILD'

            layout.separator()

            layout.operator_menu_enum("pose.select_grouped", "type", text="Grouped", icon ="GROUP_BONE")
            layout.operator("object.select_pattern", text="Select Pattern...")
            
      
###########################################################################################################################################################
###########################################################################################################################################################
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register 
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register 
###########################################################################################################################################################
###########################################################################################################################################################

def abs(val):
    if val > 0:
        return val
    return -val      

def register():

    bpy.utils.register_class(VIEW3D_Space_Selection) 

    #bpy.utils.register_module(__name__)         


def unregister():
    
    bpy.utils.unregister_class(VIEW3D_Space_Selection)    

    bpy.utils.unregister_module(__name__)  

if __name__ == "__main__":
    register() 	

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_Space_Selection.bl_idname)
  
  
           




















