#bl_info = {
#    "name": "Spacebar Edge_B",
#    "author": "Multiply Authors, mkbreuer",
#    "version": (0, 1, 0),
#    "blender": (2, 7, 2),
#    "location": "View3D",
#    "description": "",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "User Menu"}



import bpy
from bpy import *

#############################################################################################################################################################
#############################################################################################################################################################
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
#############################################################################################################################################################
#############################################################################################################################################################
  
class VIEW3D_Space_Edge_two_edm(bpy.types.Menu):
    bl_label = "Edge Visual"
    bl_idname = "space_edge_two_edm"  

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_MESH'))    

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        mesh = context.active_object.data
        scene = context.scene		
	
        with_freestyle = bpy.app.build_options.freestyle

        layout.operator("mesh.mark_seam", icon = "UV_EDGESEL").clear = False
        layout.operator("mesh.mark_seam", text="Clear Seam").clear = True

        layout.separator()

        layout.operator("mesh.mark_sharp", icon = "SNAP_EDGE").clear = False
        layout.operator("mesh.mark_sharp", text="Clear Sharp").clear = True

        layout.separator()

        layout.operator("transform.edge_crease")
        layout.operator("transform.edge_bevelweight")

        layout.separator()

        if with_freestyle and not scene.render.use_shading_nodes:
            layout.operator("mesh.mark_freestyle_edge").clear = False
            layout.operator("mesh.mark_freestyle_edge", text="Clear Freestyle Edge").clear = True

        layout.separator()            

        layout.prop(mesh, "show_extra_edge_length", text="Edge Length Info", icon="INFO")
        layout.prop(mesh, "show_extra_edge_angle", text="Edge Angle Info", icon="INFO")
		


###########################################################################################################################################################
###########################################################################################################################################################
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register 
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register 
###########################################################################################################################################################
###########################################################################################################################################################


def register():

    bpy.utils.register_class(VIEW3D_Space_Edge_two_edm)
    
    #bpy.utils.register_module(__name__)         

def unregister():
  
    bpy.utils.unregister_class(VIEW3D_Space_Edge_two_edm)
    
    bpy.utils.unregister_module(__name__)         

if __name__ == "__main__":
    register() 	

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_Space_Edge_two_edm.bl_idname)








