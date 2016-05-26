# bl_info = {
#    "name": "Spacebar File",
#    "author": "Multiple Authors, mkbreuer",
#    "version": (0,1),
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


# File Menu  ##################-------------------------------------------------------
# File Menu  ##################-------------------------------------------------------

class VIEW3D_Space_File(bpy.types.Menu):
    bl_label = "File Menu"
    bl_idname = "space_file"

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.read_homefile", text="New", icon='NEW')
        layout.operator("wm.open_mainfile", text="Open...", icon='FILE_FOLDER')
        layout.menu("INFO_MT_file_open_recent", icon='OPEN_RECENT')
        layout.operator("wm.revert_mainfile", icon='FILE_REFRESH')
        layout.operator("wm.recover_last_session", icon='RECOVER_LAST')
        layout.operator("wm.recover_auto_save", text="Recover Auto Save...", icon='RECOVER_AUTO')

        layout.separator()

        layout.operator_context = 'EXEC_AREA' if context.blend_data.is_saved else 'INVOKE_AREA'
        layout.operator("wm.save_mainfile", text="Save", icon='FILE_TICK')

        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.save_as_mainfile", text="Save As...", icon='SAVE_AS')
        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.save_as_mainfile", text="Save Copy...", icon='SAVE_COPY').copy = True

        layout.separator()

        layout.operator("screen.userpref_show", text="User Preferences...", icon='PREFERENCES')

        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.save_homefile", icon='SAVE_PREFS')
        layout.operator("wm.read_factory_settings", icon='LOAD_FACTORY')

        layout.separator()

        layout.operator_context = 'EXEC_AREA'
        if bpy.data.is_dirty and context.user_preferences.view.use_quit_dialog:
            layout.operator_context = 'INVOKE_SCREEN'  # quit dialog
        layout.operator("wm.quit_blender", text="Quit", icon='QUIT')


# Import-Export Menu  ##################-------------------------------------------------------
# Import-Export Menu  ##################-------------------------------------------------------

class VIEW3D_Space_ImExport(bpy.types.Menu):
    bl_label = "Im-Export"
    bl_idname = "space_imexport"

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.menu("INFO_MT_file_import", icon='IMPORT')
        layout.menu("INFO_MT_file_export", icon='EXPORT')
        layout.menu("OBJECT_MT_selected_export", text="Export Selected", icon='EXPORT')

        layout.separator()

        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.link", text="Link", icon='LINK_BLEND')
        layout.operator("wm.append", text="Append", icon='APPEND_BLEND')

        layout.separator()

        layout.operator("object.make_local")
        layout.operator("object.proxy_make")

        layout.separator()

        layout.menu("INFO_MT_file_external_data", icon='EXTERNAL_DATA')


###########################################################################################################################################################
###########################################################################################################################################################
# Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register
# Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register
###########################################################################################################################################################
###########################################################################################################################################################


def register():

    bpy.utils.register_class(VIEW3D_Space_File)
    bpy.utils.register_class(VIEW3D_Space_ImExport)


def unregister():

    bpy.utils.unregister_class(VIEW3D_Space_File)
    bpy.utils.unregister_class(VIEW3D_Space_ImExport)

    # bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    # bpy.ops.wm.call_menu(name=VIEW3D_Space_File.bl_idname)
    bpy.ops.wm.call_menu(name=VIEW3D_Space_ImExport.bl_idname)
