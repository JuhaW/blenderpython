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
        
            
        layout.separator()

        layout.operator("mesh.tris_convert_to_quads", icon="OUTLINER_OB_LATTICE")
        layout.operator("mesh.quads_convert_to_tris", icon="OUTLINER_OB_MESH")
        layout.operator("mesh.vert_connect_nonplanar", icon="OUTLINER_OB_MESH")

bpy.utils.register_class(CLEANUP)


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
            
    col = layout.column(align=True)
    row = col.row(align=True)
        
    row.operator("ed.undo_history", text="History")
    row.operator("ed.undo", text="", icon="LOOP_BACK")
    row.operator("ed.redo", text="", icon="LOOP_FORWARDS")




######---------################################################################################################################
######  Panel  ################################################################################################################
######  Panel  ################################################################################################################
######---------################################################################################################################


# Sub Location
class SubLoc_Delete():
    """Delete & Clear Menu [X]"""
    bl_category="META"
    #bl_region_type = 'TOOLS'
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'   

    @classmethod
    def poll(cls, context):
        return context.scene.osc_clean


class VIEW3D_MTK_Delete(SubLoc_Delete, bpy.types.Panel):
    bl_label = "[DELETE]"
    bl_idname = "mtk_delete"   
   
    def draw(self, context):
        lt = context.window_manager.metawindowtool
        layout = self.layout
        

####### Object mode -------------------------------------------------        
####### Object mode -------------------------------------------------
       
        ob = context       
        if ob.mode == 'OBJECT':
                           
            box = layout.box()
            row = box.row(True) 
            row.operator("object.delete")
            row = box.row(True)
            row.operator("ba.delete_scene_obs") 
            
            box = layout.box()
            row = box.row(True)  
            row.menu("VIEW3D_MT_object_showhide", "Clear Hide")
            row = box.row(True)               
            row.operator("material.remove", text="Clear Materials")
            row = box.row(True)               
            row.operator("object.vertex_group_remove", "Clear Vertex Group").all = True
            

            box = layout.box()
            row = box.row(True) 
            scn = context.scene          
            row.operator("ba.delete_data_obs","Clear Orphan")
            row = box.row(True)         
            row.prop(scn, "mod_list")
            

            box = layout.box()
            row = box.row(True) 
            row.menu("VIEW3D_MT_object_clear", text="Clear Location")
            row = box.row(True)  
            row.menu("clearparent", text="Clear Parenting")
            row = box.row(True)  
            row.menu("cleartrack", text="Clear Tracking")
            
            box = layout.box()
            row = box.row(True)             
            row.operator("object.constraints_clear", text="Clear Constraint")
            row = box.row(True)  
            row.operator("anim.keyframe_clear_v3d", text = "Clear Keyframe")#
            row = box.row(True)                          
            row.operator("object.game_property_clear")      

            box = layout.box()
            row = box.row(True) 
            row.operator("meshlint.select", "Meshlint > Object Data")

            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################
            
          

####### Edit mode -------------------------------------------------        
####### Edit mode -------------------------------------------------


        elif ob.mode == 'EDIT_MESH':

            box = layout.box()
            row = box.row(True) 
            row.scale_y = 1.5            
            row.operator("meshlint.select", "Meshlint > Object Data", icon = "ERROR")

            box = layout.box()
            row = box.row(True)    
            row.menu("VIEW3D_MT_edit_mesh_showhide", "Show / Hide", icon = "RESTRICT_VIEW_OFF")



            box = layout.box()
            row = box.column(1)
            row.scale_y = 1.25
            row.operator("mesh.delete", "Vertices", icon="SNAP_VERTEX").type="VERT"
            row = box.column(1)
            row.operator("mesh.dissolve_verts")
            row.operator("mesh.remove_doubles")

            box = layout.box()
            row = box.column(1)
            row.scale_y = 1.25
            row.operator("mesh.delete", "Edges", icon="SNAP_EDGE").type="EDGE"
            row = box.column(1)
            row.operator("mesh.dissolve_edges")
            row.operator("mesh.delete_edgeloop", text="Remove Edge Loop")

            box = layout.box()
            row = box.column(1)
            row.scale_y = 1.25
            row.operator("mesh.delete", "Faces", icon="SNAP_FACE").type="FACE"
            row = box.column(1)
            row.operator("mesh.dissolve_faces")
            row.operator("mesh.delete", "Remove only Faces").type="ONLY_FACE"

            box = layout.box()
            row = box.column(1)
            row.scale_y = 1.25          
            row.operator("mesh.dissolve_limited", icon="MATCUBE")
            row = box.column(1)	
            row.operator("mesh.dissolve_degenerate")
            row.operator("mesh.delete", "Remove Edge & Faces").type="EDGE_FACE"

            box = layout.box()
            row = box.column(1)   
            row.operator("mesh.delete_loose", text="Loose", icon = "STICKY_UVS_DISABLE")
            row.operator("mesh.fill_holes")            
            row = box.column(1)   
            row.operator("mesh.dissolve_degenerate")
            row.operator("mesh.vert_connect_nonplanar")
            

                
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################
            
               

####### Curve menu ------------------------------------------------        
####### Curve menu ------------------------------------------------

        if ob.mode == 'EDIT_CURVE':
            
            box = layout.box()
            row = box.row(True) 
            row.operator("curve.delete", "Vertices", icon="PARTICLE_TIP").type="VERT"
            row = box.row(True) 
            row.operator("curve.delete", "Segment", icon="IPO_EASE_IN_OUT").type="SEGMENT"
            row = box.row(True)                        
            row.operator("curve.reveal", text="Clear Hide", icon = "RESTRICT_VIEW_OFF")
           
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################
            
                                    

####### Surface menu ----------------------------------------------
####### Surface menu ----------------------------------------------
       
        if ob.mode == 'EDIT_SURFACE':

            box = layout.box()
            row = box.row(True) 
            row.operator("curve.delete", "Vertices", icon="PARTICLE_TIP").type="VERT"
            row = box.row(True)
            row.operator("curve.delete", "Segments", icon="IPO_EASE_IN_OUT").type="SEGMENT"
            row = box.row(True)
            row.operator("curve.reveal", text="Clear Hide", icon = "RESTRICT_VIEW_OFF")
            
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################
                              
        
####### Metaball menu ---------------------------------------------
####### Metaball menu ---------------------------------------------
                
        if ob.mode == 'EDIT_METABALL':
            
            box = layout.box()
            row = box.row(True)           
            row.operator("mball.delete_metaelems", icon="META_BALL")
            row = box.row(True)             
            row.operator("mball.reveal_metaelems", text="Clear Hide", icon = "RESTRICT_VIEW_OFF")

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

            box = layout.box()
            row = box.row(True)
            row.operator("particle.delete")
            row = box.row(True)
            row.operator("particle.remove_doubles")
            row = box.row(True)
            row.menu("VIEW3D_MT_particle_showhide", text = "Clear Hide", icon = "RESTRICT_VIEW_OFF")                        

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
            
            box = layout.box()
            row = box.row(True)   
            props = row.operator("paint.hide_show", text="Clear All Hide", icon = "RESTRICT_VIEW_OFF")
            props.action = 'SHOW'
            props.area = 'ALL'

            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################
            

                        
####### Armature menu ---------------------------------------------
####### Armature menu ---------------------------------------------
        
     
        elif ob.mode == 'EDIT_ARMATURE':
            box = layout.box()
            row = box.row(True)            
            row.operator("armature.delete", text = "Selected Bone(s)")
            row = box.row(True)   
            row.operator("sketch.delete", text = "Sketch Delete")
            row = box.row(True)  
            row.operator("armature.parent_clear").type='CLEAR'
            ##########################################
            draw_delete_history_tools(context, layout)
            ##########################################

            
            
####### Pose mode menu --------------------------------------------
####### Pose mode menu --------------------------------------------
            
        if context.mode == 'POSE':
            arm = context.active_object.data 
            box = layout.box()
            row = box.row(True)
            row.operator("anim.keyframe_clear_v3d", text = "Clear Keyframe")
            row = box.row(True)
            row.operator("pose.paths_clear", text = "Clear Motion Path")
            row = box.row(True)
            row.menu("VIEW3D_MT_pose_transform", text="Clear Location")
            row = box.row(True)  
            row.menu("clearparent", text="Clear Parenting")
            row = box.row(True)
            row.operator("pose.constraints_clear", text="Clear Constraint") 
            row = box.row(True)           
            row.operator("pose.reveal", text = "Clear Hide", icon = "RESTRICT_VIEW_OFF")             
            
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
     
    bpy.utils.register_class(VIEW3D_MTK_Delete)
    
    #bpy.utils.register_module(__name__)      


def unregister():

    bpy.utils.unregister_class(VIEW3D_MTK_Delete)    

    bpy.utils.unregister_module(__name__)  


if __name__ == "__main__":
    register() 	


































