#bl_info = {
#    "name": "Spacebar Edge_A",
#    "author": "Multiple Authors, mkbreuer",
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
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ###  
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ###  
#############################################################################################################################################################
#############################################################################################################################################################

#######  Cad XVT  #######-------------------------------------------------------                  
#######  Cad XVT  #######-------------------------------------------------------        

class XVTMenu(bpy.types.Menu):
    bl_label = "Cad XVT"
    bl_idname = "edge_cadxvt"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        scene = context.scene

        layout.operator("bpt.smart_vtx",text="Auto XVT", icon="GRID")
        layout.operator("mesh.intersections", text="X Intersection").mode = 1        
        layout.operator("mesh.intersections", text="V Intersection").mode =-1
        layout.operator("mesh.intersections", text="T Intersection").mode = 0

bpy.utils.register_class(XVTMenu)  


#############################################################################################################################################################
#############################################################################################################################################################
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
#############################################################################################################################################################
#############################################################################################################################################################

#######  Edge Edit  #######-------------------------------------------------------                  
#######  Edge Edit  #######-------------------------------------------------------        

class VIEW3D_Space_Edge_one_edm(bpy.types.Menu):
    bl_label = "Edge Edit"
    bl_idname = "space_edge_one_edm" 
    
    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_MESH'))    

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'INVOKE_REGION_WIN'
        with_freestyle = bpy.app.build_options.freestyle
        scene = context.scene

        layout.operator("mesh.edge_face_add", icon = "SNAP_FACE")
                       
        layout.separator()

        layout.operator("mesh.bevel", icon = "SPHERECURVE").vertex_only = False
        layout.operator("mesh.edge_split")
        layout.operator("mesh.bridge_edge_loops")
        
        layout.separator()
        
        layout.operator("transform.edge_slide", icon = "PARTICLE_POINT")            
        layout.operator("mesh.offset_edges",text="Edge Offset", icon="PARTICLE_PATH")
        layout.operator("object.mesh_edge_lengthchange", "Edge Length", icon="PARTICLE_TIP")

        layout.separator()

        layout.menu("VIEW3D_MT_edit_mesh_edgetools", text="Edge Tools", icon = "OUTLINER_DATA_MESH")
        layout.operator('mesh.edge_roundifier') 
        
        layout.separator()

        layout.menu("edge_cadxvt", icon = "OUTLINER_DATA_LATTICE")
        layout.menu("VIEW3D_MT_edit_mesh_tinycad")  

        layout.separator()
        
        layout.operator("mesh.edge_rotate", text="Rotate Edge CW", icon = "FILE_REFRESH").use_ccw = False
        layout.operator("mesh.edge_rotate", text="Rotate Edge CCW").use_ccw = True
        
        layout.separator()

        layout.operator("mesh.region_to_loop", icon = "RESTRICT_SELECT_OFF")
        layout.operator("mesh.loop_to_region")           



###########################################################################################################################################################
###########################################################################################################################################################
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register 
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register 
###########################################################################################################################################################
###########################################################################################################################################################


def register():

    bpy.utils.register_class(VIEW3D_Space_Edge_one_edm)
    
    #bpy.utils.register_module(__name__)       


def unregister():
  
    bpy.utils.unregister_class(VIEW3D_Space_Edge_one_edm)
    
    bpy.utils.unregister_module(__name__)       

if __name__ == "__main__":
    register() 	

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_Space_Edge_one_edm.bl_idname)


















