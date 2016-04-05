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

#############################################################
###---------------  MANAGEMENT  --------------------------###
###---------------  MANAGEMENT  --------------------------###
#############################################################

# Sub Location
class SubLoc_MANAGE():
    """Im-Export Tools"""
    bl_category="META"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D' 

    @classmethod
    def poll(cls, context):
        return context.scene.osc_manager and context.mode == ('OBJECT')
        

## Sub Panel
class META_TAB_MANAGE(SubLoc_MANAGE, bpy.types.Panel):
    """Im-Export Tools"""
    bl_label = "[Im-Export]"
    bl_idname = "management_layers"


    def draw(self, context):
        lt = context.window_manager.metawindowtool
        layout = self.layout
        
        obj = context.object
        scene = context.scene
        
        ###---###---###---###

###########################-------------------------------------------------------
#######  Im-Export  #######-------------------------------------------------------  
#######  Im-Export  #######-------------------------------------------------------
###########################-------------------------------------------------------
      
        col = layout.column(align=True)
        split = col.split()#percentage=0.15)
                
        if lt.display_tab_imexport:
            split.prop(lt, "display_tab_imexport", text="...Im-Export...", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "display_tab_imexport", text="...Im-Export...", icon='RIGHTARROW')
            
        #spread_op = split.operator("", text="", icon="")
        
        if lt.display_tab_imexport:
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.menu("INFO_MT_file_import", icon='IMPORT')
            row = col_top.row(align=True)
            row.menu("INFO_MT_file_export", icon='EXPORT')
            row = col_top.row(align=True)
            row.menu("OBJECT_MT_selected_export", text="Export Selected",icon='EXPORT')

            row = col_top.row(align=True)
            row.label(text="------------------------------------------------------------------------------------------------------------")
             
            row = col_top.row(align=True)
           
            col_top = box.column(align=True)
            
            row = col_top.row(align=True)            
            row.operator_context = 'INVOKE_AREA'
            row.operator("wm.link", text="Link", icon='LINK_BLEND')
            row.operator("wm.append", text="Append", icon='APPEND_BLEND')
                       
            col_top = box.column(align=True)
            
            row = col_top.row(align=True)
            row.operator("object.make_local")
            row.operator("object.proxy_make")

            row = col_top.row(align=True)
            row.label(text="------------------------------------------------------------------------------------------------------------")
            
            col_top = box.column(align=True)
            
            row = col_top.row(align=True)
            row.operator("object.join",text="Join Objects")              
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.convert",text="Convert to Mesh").target="MESH"
            row = col_top.row(align=True)
            row.operator("object.convert",text="Convert to Curve").target="CURVE"              
           

            split = col.split()#percentage=0.15)
                
            if lt.display_tab_imexfolder:
                split.prop(lt, "display_tab_imexfolder", text="...Folder...", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                split.prop(lt, "display_tab_imexfolder", text="...Folder...", icon='DISCLOSURE_TRI_RIGHT_VEC')
            
            #spread_op = split.operator("", text="", icon="")
        
            if lt.display_tab_imexfolder:

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("productionfolder_scene.selected",text="Production Folder",icon="FILE_FOLDER")
                
                row = col_top.row(align=True)                  
                row.operator("production_scene.selected",text="Save Production Scene", icon="FILE_TICK")                                        

                row = col_top.row(align=True)                    
                row.operator("file.production_folder", text="Show Production Folder", icon= "GO_LEFT")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("image.imagesave",text="Collect Image Folder", icon ="IMAGE_COL")                    
                                 
            
            
            #col = layout.column(align=True)
            split = col.split()#percentage=0.15)
                
            if lt.display_tab_imexmanage:
                split.prop(lt, "display_tab_imexmanage", text="...Pack & Pathes...", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                split.prop(lt, "display_tab_imexmanage", text="...Pack & Pathes...", icon='DISCLOSURE_TRI_RIGHT_VEC')
            
            #spread_op = split.operator("", text="", icon="")
        
            if lt.display_tab_imexmanage:                    

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                pack_all = box.row()
                pack_all.operator("file.pack_all")
                pack_all.active = not bpy.data.use_autopack

                unpack_all = box.row()
                unpack_all.operator("file.unpack_all")
                unpack_all.active = not bpy.data.use_autopack

                icon = 'CHECKBOX_HLT' if bpy.data.use_autopack else 'CHECKBOX_DEHLT'
                row.operator("file.autopack_toggle", text="autom. Pack into .blend",icon=icon)        

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("file.make_paths_relative")
        
                row = col_top.row(align=True)
                row.operator("file.make_paths_absolute")

                row = col_top.row(align=True)    
                row.operator("file.report_missing_files")
        
                row = col_top.row(align=True)
                row.operator("file.find_missing_files")


        
############------------############
############  REGISTER  ############
############------------############


def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
        
        
        
        
       











