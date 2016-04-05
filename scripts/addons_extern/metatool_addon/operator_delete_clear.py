#bl_info = {
#    "name": "Display Delete & Clear Menu",
#    "author": "mkbreuer",
#    "version": (0, 1, 1),
#    "blender": (2, 7, 2),
#    "location": "3D View",
#    "description": "[X] Delete & Clear Tools",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "User Display"}



import bpy, re
from bpy import *

###### -----------#####################################################################################################################
######  Operator  #####################################################################################################################
######  Operator  #####################################################################################################################
###### -----------#####################################################################################################################


#######  Delete all Material  #######-------------------------------------------------------                  
#######  Delete all Material  #######-------------------------------------------------------        

class deleteMat(bpy.types.Operator):
    """delete materials with an value slider"""
    bl_idname = "material.remove"
    bl_label = "Delete all Material"
    bl_options = {'REGISTER', 'UNDO'}

    deleteMat = bpy.props.IntProperty(name="Delete all Material", description="How many times?", default=100, min=1, soft_max=5000, step=1)
    
    def execute(self, context):        
        for i in range(self.deleteMat):      
            bpy.ops.object.material_slot_remove()
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)  

bpy.utils.register_class(deleteMat)

######------------#####################################################################################################################
######  Sub Menu  #####################################################################################################################
######  Sub Menu  #####################################################################################################################
######------------#####################################################################################################################

#######  Clean Up Mesh  #######-------------------------------------------------------                  
#######  Clean Up Mesh  #######-------------------------------------------------------        


class VIEW3D_PIE_Delete(bpy.types.Menu):
    bl_label = "Delete Menu [X]"
    bl_idname = "pie.obm_delete"   
   
    def draw(self, context):
        layout = self.layout

        layout.operator("object.delete","Delete", icon ="X")
        layout.operator("ba.delete_scene_obs") 
        layout.operator("material.remove", text="Clear Materials")

   

bpy.utils.register_class(VIEW3D_PIE_Delete)


class CLEANUP(bpy.types.Menu):
    bl_label = "Clean Up Mesh"
    bl_idname = "cleanup"
    
    def draw(self, context):
        layout = self.layout
             
        layout.label("Clean Up Mesh")
        
        layout.separator()        
            
        layout.operator("mesh.fill_holes") 
        layout.operator("mesh.delete_loose")

        layout.operator("mesh.edge_collapse")            


bpy.utils.register_class(CLEANUP)



class CLEANVERT(bpy.types.Menu):
    bl_label = "Delete Vertices"
    bl_idname = "mesh.cleanvert"
    
    def draw(self, context):
        layout = self.layout
        #layout.label("Delete Vertices")
        
        layout.operator("mesh.delete", "Vertices", icon="SNAP_VERTEX").type="VERT"
        layout.operator("mesh.dissolve_verts")
        layout.operator("mesh.remove_doubles")

bpy.utils.register_class(CLEANVERT)



class CLEANEDGE(bpy.types.Menu):
    bl_label = "Delete Edge"
    bl_idname = "mesh.cleanedge"
    
    def draw(self, context):
        layout = self.layout
        #layout.label("Delete Edges")
            
        layout.operator("mesh.delete", "Edges", icon="SNAP_EDGE").type="EDGE"
        layout.operator("mesh.dissolve_edges")
        layout.operator("mesh.delete_edgeloop", text="Remove Edge Loop")
            
bpy.utils.register_class(CLEANEDGE)


class CLEANFACE(bpy.types.Menu):
    bl_label = "Delete Faces"
    bl_idname = "mesh.cleanface"
    
    def draw(self, context):
        layout = self.layout
        #layout.label("Delete Faces")
         
        layout.operator("mesh.delete", "Faces", icon="SNAP_FACE").type="FACE"
        layout.operator("mesh.dissolve_faces")
        layout.operator("mesh.delete", "Remove only Faces").type="ONLY_FACE"            
            
bpy.utils.register_class(CLEANFACE)            


class CLEANDISSOLVE(bpy.types.Menu):
    bl_label = "Delete Dissolve"
    bl_idname = "mesh.cleandissolve"
    
    def draw(self, context):
        layout = self.layout
        #layout.label("Dissolve")

        layout.operator("mesh.dissolve_limited", icon="MATCUBE")		
        layout.operator("mesh.dissolve_degenerate")
        layout.operator("mesh.delete", "Remove Edge & Faces").type="EDGE_FACE"
            
bpy.utils.register_class(CLEANDISSOLVE)



#######  Clear Parenting  #######-------------------------------------------------------                  
#######  Clear Parenting  #######-------------------------------------------------------        

class CLEARPARENT(bpy.types.Menu):
    bl_label = "Clear Parenting"
    bl_idname = "clearparent"
        
    def draw(self, context):
        layout = self.layout
        
        layout.operator_enum("object.parent_clear", "type")
        
bpy.utils.register_class(CLEARPARENT)


#######  Clear Tracking  #######-------------------------------------------------------                  
#######  Clear Tracking  #######-------------------------------------------------------        

class CLEARTRACK(bpy.types.Menu):
    bl_label = "Clear Tracking"
    bl_idname = "cleartrack"
       
    def draw(self, context):
        layout = self.layout
        
        layout.operator_enum("object.track_clear", "type")
        
bpy.utils.register_class(CLEARTRACK)


#######  ReUndo  #######-------------------------------------------------------                  
#######  ReUndo  #######-------------------------------------------------------        

class VIEW3D_HTK_ReUndo(bpy.types.Menu):
    bl_label = "Hisrory Menu [X]"
    bl_idname = "htk_reundo"   
   
    def draw(self, context):
        layout = self.layout
        
        layout.operator("ed.undo", text="Undo", icon ="TRIA_LEFT")
        layout.operator("ed.redo", text="Redo", icon ="TRIA_RIGHT")
        layout.operator("ed.undo_history", icon ="TRIA_DOWN") 
    
bpy.utils.register_class(VIEW3D_HTK_ReUndo)    


######  Repeat History  ######-------------------------------------------------------                                                    
######  Repeat History  ######-------------------------------------------------------                                                    

def draw_delete_history_tools(context, layout):
    settings = context.tool_settings
    layout.operator_context = 'INVOKE_REGION_WIN'

    # Special Menu
            
    layout.operator("ed.undo", text="Undo", icon ="TRIA_LEFT")
    layout.operator("ed.redo", text="Redo", icon ="TRIA_RIGHT")
    layout.operator("ed.undo_history", icon ="TRIA_DOWN") 



######--------################################################################################################################
######  Menu  ################################################################################################################
######  Menu  ################################################################################################################
######------ -################################################################################################################

####### Delete & Clear Menu -------------------------------------------------        
####### Delete & Clear Menu -------------------------------------------------

class VIEW3D_HTK_Delete(bpy.types.Menu):
    bl_label = "Delete & Clear Menu [X]"
    bl_idname = "htk_delete"   
   
    def draw(self, context):
        layout = self.layout
        

####### Object mode -------------------------------------------------        
####### Object mode -------------------------------------------------
       
        ob = context       
        if ob.mode == 'OBJECT':
                           
            layout.operator("object.delete")
                 

            layout.separator()

            layout.operator("material.remove", text="Clear Materials")


            layout.separator()  

            layout.operator("ba.delete_scene_obs")                 

            
          

####### Edit mode -------------------------------------------------        
####### Edit mode -------------------------------------------------


        elif ob.mode == 'EDIT_MESH':

            layout.operator("mesh.delete", "Vertices", icon="SNAP_VERTEX").type="VERT"
            layout.operator("mesh.dissolve_verts")
            layout.operator("mesh.remove_doubles")

            layout.separator()
            
            layout.operator("mesh.delete", "Edges", icon="SNAP_EDGE").type="EDGE"
            layout.operator("mesh.dissolve_edges")
            layout.operator("mesh.delete_edgeloop", text="Remove Edge Loop")
            
            layout.separator()
            
            layout.operator("mesh.delete", "Faces", icon="SNAP_FACE").type="FACE"
            layout.operator("mesh.dissolve_faces")
            layout.operator("mesh.delete", "Remove only Faces").type="ONLY_FACE"            
            
            
            layout.separator()

            layout.operator("mesh.dissolve_limited", icon="MATCUBE")		
            layout.operator("mesh.dissolve_degenerate")
            layout.operator("mesh.delete", "Remove Edge & Faces").type="EDGE_FACE"
            
            layout.separator() 
                        
            layout.menu("cleanup", text="Clean Up Mesh", icon = "RIGHTARROW_THIN") 
            
            layout.separator() 
                        
            layout.operator("mesh.reveal", text="Clear Hide", icon = "RESTRICT_VIEW_OFF") 
                      
            layout.separator()
            
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################
            
               

####### Curve menu ------------------------------------------------        
####### Curve menu ------------------------------------------------

        if ob.mode == 'EDIT_CURVE':

            layout.operator("curve.delete", "Vertices", icon="PARTICLE_TIP").type="VERT"
            layout.operator("curve.delete", "Segment", icon="IPO_EASE_IN_OUT").type="SEGMENT"

            layout.separator() 
                        
            layout.operator("curve.reveal", text="Clear Hide", icon = "RESTRICT_VIEW_OFF")            

            layout.separator()
            
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################
            
                                    

####### Surface menu ----------------------------------------------
####### Surface menu ----------------------------------------------
       
        if ob.mode == 'EDIT_SURFACE':

            layout.operator("curve.delete", "Vertices", icon="PARTICLE_TIP").type="VERT"
            layout.operator("curve.delete", "Segments", icon="IPO_EASE_IN_OUT").type="SEGMENT"

            layout.separator() 
                        
            layout.operator("curve.reveal", text="Clear Hide", icon = "RESTRICT_VIEW_OFF") 
     
            layout.separator()
            
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################
                              
        
####### Metaball menu ---------------------------------------------
####### Metaball menu ---------------------------------------------
                
        if ob.mode == 'EDIT_METABALL':
           
            layout.operator("mball.delete_metaelems", icon="META_BALL")

            layout.separator() 
            
            layout.operator("mball.reveal_metaelems", text="Clear Hide", icon = "RESTRICT_VIEW_OFF") 
            
            layout.separator()
            
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################
            


####### Lattice menu ----------------------------------------------
####### Lattice menu ----------------------------------------------
         
        elif ob.mode == 'EDIT_LATTICE':
           
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################
            

                        
####### Particle menu ---------------------------------------------
####### Particle menu ---------------------------------------------
           
        if  context.mode == 'PARTICLE':

            layout.operator("particle.delete")

            layout.separator()

            layout.operator("particle.remove_doubles")
            
            layout.separator()

            layout.menu("VIEW3D_MT_particle_showhide", text = "Clear Hide", icon = "RESTRICT_VIEW_OFF")                        
            
            layout.separator()
            
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################                    



####### Weight paint menu -----------------------------------------
####### Weight paint menu -----------------------------------------
                   
        ob = context  
        if ob.mode == 'PAINT_WEIGHT':

            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################              


####### Vertex paint menu -----------------------------------------
####### Vertex paint menu -----------------------------------------
                                    
        elif ob.mode == 'PAINT_VERTEX':
            
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################



####### Texture paint menu ----------------------------------------
####### Texture paint menu ----------------------------------------
                       
        elif ob.mode == 'PAINT_TEXTURE':
            
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################
            

            
####### Sculpt menu -----------------------------------------------
####### Sculpt menu -----------------------------------------------
                        
        elif ob.mode == 'SCULPT':
             
            props = layout.operator("paint.hide_show", text="Clear All Hide", icon = "RESTRICT_VIEW_OFF")
            props.action = 'SHOW'
            props.area = 'ALL'
            
            layout.separator()

            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################
            

                        
####### Armature menu ---------------------------------------------
####### Armature menu ---------------------------------------------
        
     
        elif ob.mode == 'EDIT_ARMATURE':
            
            layout.operator("armature.delete", text = "Selected Bone(s)", icon = "RIGHTARROW_THIN")

            layout.separator()
            
            layout.operator("sketch.delete", text = "Sketch Delete", icon = "RIGHTARROW_THIN")  
            
            layout.separator()
                         
            layout.operator("armature.parent_clear", icon = "RIGHTARROW_THIN").type='CLEAR'

            layout.separator()
            
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################

            
            
####### Pose mode menu --------------------------------------------
####### Pose mode menu --------------------------------------------
            
        if context.mode == 'POSE':
            arm = context.active_object.data 

            layout.operator("anim.keyframe_clear_v3d", text = "Clear Keyframe")
            layout.operator("pose.paths_clear", text = "Clear Motion Path")

            layout.separator()

            layout.menu("VIEW3D_MT_pose_transform", text="Clear Location")  
            layout.menu("clearparent", text="Clear Parenting")
            layout.operator("pose.constraints_clear", text="Clear Constraint")            

            layout.separator()
              
            layout.operator("pose.reveal", text = "Clear Hide", icon = "RESTRICT_VIEW_OFF") 

            layout.separator()
            
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################



######------------################################################################################################################
######  Registry  ################################################################################################################
######  Registry  ################################################################################################################
######------------################################################################################################################


def abs(val):
    if val > 0:
        return val
    return -val


def register():
     
    bpy.utils.register_class(VIEW3D_HTK_Delete)
    
    #bpy.utils.register_module(__name__)      
   


def unregister():

    bpy.utils.unregister_class(VIEW3D_HTK_Delete)    

    bpy.utils.unregister_module(__name__)  



if __name__ == "__main__":
    register() 	

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_HTK_Delete.bl_idname)
  
  
           


















