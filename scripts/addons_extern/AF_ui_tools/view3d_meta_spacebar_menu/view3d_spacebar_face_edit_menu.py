#bl_info = {
#    "name": "Spacebar Face_A",
#    "author": "MKB",
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


#############################################################################################################################################################
#############################################################################################################################################################
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
#############################################################################################################################################################
#############################################################################################################################################################
  
######  Face Edit  ##################-------------------------------------------------------                         
######  Face Edit  ##################-------------------------------------------------------                         
  
class VIEW3D_Space_Face_one_edm(bpy.types.Menu):
    bl_label = "Face Edit"
    bl_idname = "space_face_one_edm"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_MESH'))
        
    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        scene = context.scene

        layout.operator("mesh.edge_face_add", icon = "SNAP_FACE")

        layout.separator()        
        
        layout.operator("mesh.fill", icon = "ORTHO")
        layout.operator("mesh.fill_grid")
        
        layout.operator("mesh.beautify_fill")

        layout.separator()
        
        layout.menu("VIEW3D_MT_edit_mesh_extrude", icon = "CLIPUV_HLT")

        layout.operator("mesh.poke",  text="Poke Inset")        
        
        layout.operator("mesh.inset",  text="Face Inset")

        layout.operator("faceinfillet.op0_id",  text="Face Inset Fillet")
        
        layout.operator('object.mextrude', text="Multi Face Extrude")
    
        layout.operator("mesh.extrude_along_curve", text="Extrude Along Curve")
      
        layout.separator()      
        
        layout.operator("mesh.face_split_by_edges")  
      
        layout.separator()
                      
        layout.operator("mesh.bevel", icon = "SPHERECURVE").vertex_only = False
        layout.operator("mesh.solidify")
        layout.operator("mesh.intersect")
        layout.operator("mesh.wireframe")        
		
        layout.separator()	
            
        layout.operator("mesh.rot_con", "Rotate Face", icon ="SNAP_FACE")
        layout.operator("fan.move_faces_along_normals_operator", "Along Normals", icon ="SNAP_NORMAL")
        layout.operator("bpt.boolean_2d_union", text= "Union 2d Faces", icon="MESH_GRID")
        
        layout.separator()

        layout.operator("mesh.quads_convert_to_tris", icon="OUTLINER_DATA_MESH")
        layout.operator("mesh.tris_convert_to_quads", icon="OUTLINER_DATA_LATTICE") 

###########################################################################################################################################################
###########################################################################################################################################################
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register 
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register 
###########################################################################################################################################################
###########################################################################################################################################################

def register():

    bpy.utils.register_class(VIEW3D_Space_Face_one_edm)    

def unregister():
  
    bpy.utils.unregister_class(VIEW3D_Space_Face_one_edm) 

    bpy.utils.unregister_module(__name__)         

if __name__ == "__main__":
    register() 	

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_Space_Face_one_edm.bl_idname)
         








