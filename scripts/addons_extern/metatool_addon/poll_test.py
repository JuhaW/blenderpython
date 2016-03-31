#bl_info = {
#    "name": "Extension Add",
#    "author": "marvin.k.breuer",
#    "version": (0, 1, 0),
#    "blender": (2, 72, 0),
#    "location": "View3D > Toolbar",
#    "warning": "",
#    "description": "Toolkit Extension",
#    "wiki_url": "",
#    "category": "User Panel",
#}


import bpy
from bpy import *


#######################################################
###-----------------  ADD  -------------------------###
###-----------------  ADD  -------------------------###
#######################################################


# Sub Location
class SubLoc_Test():
    """Add Tools"""
    bl_category="META"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D' 

    @classmethod
    def poll(cls, context):
        return context.scene.osc_test #and context.mode == ('OBJECT')

## Sub Panel
class META_TAB_Test(SubLoc_Test, bpy.types.PropertyGroup):
    """Add Tools"""
    bl_idname = "add_tools"
    bl_label = "[Add Tools]"


    def draw(self, context):
        lt = context.window_manager.metawindowtool        
        layout = self.layout
        
        obj = context.object
        scene = context.scene
        
        ###---###---###---###
        
        col = layout.column()
        row = col.row(align=True) 

        ###space1###
        if lt.display_geometry:
            ###space2###       
            box = layout.box()
            row = box.row()                       
            row.prop(lt, "display_geometry", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()              
            row.prop(lt, "display_geometry", text="", icon='TRIA_RIGHT')
    
        row.label("Geometry...")
        op = row.menu("INFO_MT_add",text="", icon="OBJECT_DATAMODE")        

        ###space1###     
        if lt.display_geometry:
        
            ###space2### 
            if context.mode == 'OBJECT':
                col = layout.column(align=True)  
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                
                row = col_top.row(align=True) 
                row.alignment = 'CENTER'
                row.menu("INFO_MT_mesh_add",text="",icon='OUTLINER_OB_MESH')              
                row.menu("INFO_MT_curve_add",text="",icon='OUTLINER_OB_CURVE')
                row.menu("INFO_MT_surface_add",text="",icon='OUTLINER_OB_SURFACE')
                row.menu("INFO_MT_metaball_add",text="",icon="OUTLINER_OB_META")
                row.operator("object.lamp_add",icon='OUTLINER_OB_LAMP',text="")
                row.operator("object.speaker_add",icon='OUTLINER_OB_SPEAKER',text="")
                row.operator_menu_enum("object.effector_add", "type", text="",icon="SOLO_ON") 
                #row.menu("INFO_MT_add",text="", icon="OBJECT_DATAMODE")  
                        
                row = col_top.row(align=True) 
                row.alignment = 'CENTER'
                
                row.operator("object.empty_add",text="",icon="OUTLINER_OB_EMPTY")          
                row.operator("object.add",text="",icon="OUTLINER_OB_LATTICE").type="LATTICE"
                row.operator("object.text_add",text="",icon="OUTLINER_OB_FONT")
                row.operator("object.camera_add",icon='OUTLINER_OB_CAMERA',text="")   
                row.operator("object.armature_add",text="",icon="OUTLINER_OB_ARMATURE")
  
        
############------------############
############  REGISTER  ############
############------------############


def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()


















