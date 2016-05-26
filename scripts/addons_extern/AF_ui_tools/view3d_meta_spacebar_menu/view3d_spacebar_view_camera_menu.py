# bl_info = {
#    "name": "Spacebar View & Camera",
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


# 3D Navigation  ######-------------------------------------------------------
# 3D Navigation  ######-------------------------------------------------------

class VIEW3D_3DNaviMenu(bpy.types.Menu):
    bl_label = "3D Navigation"
    bl_idname = "3dnavimenu"

    def draw(self, context):
        layout = self.layout

        layout.menu("navimenu", text="View Rotation", icon="NDOF_TURN")

        layout.separator()

        layout.operator("view3d.viewnumpad", text="Camera").type = 'CAMERA'
        layout.operator("view3d.viewnumpad", text="Top").type = 'TOP'
        layout.operator("view3d.viewnumpad", text="Bottom").type = 'BOTTOM'
        layout.operator("view3d.viewnumpad", text="Front").type = 'FRONT'
        layout.operator("view3d.viewnumpad", text="Back").type = 'BACK'
        layout.operator("view3d.viewnumpad", text="Right").type = 'RIGHT'
        layout.operator("view3d.viewnumpad", text="Left").type = 'LEFT'

        layout.separator()

        layout.menu("VIEW3D_MT_view_align_selected", text="View around Active")


# Camera View  ######-------------------------------------------------------
# Camera View  ######-------------------------------------------------------

class VIEW3D_CameraViewMenu(bpy.types.Menu):
    bl_label = "Camera View"
    bl_idname = "cameraviewmenu"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.camera_add")

        layout.separator()

        layout.operator("view3d.viewnumpad", text="Active Camera").type = 'CAMERA'
        layout.operator("view3d.object_as_camera")

        layout.operator("view3d.camera_to_view", text="Active Camera to View")
        layout.operator("view3d.camera_to_view_selected", text="Active Camera to Selected")

        layout.separator()

        layout.operator("view3d.zoom_camera_1_to_1", text="Zoom Camera 1:1", icon='RIGHTARROW_THIN')


# Border Menu  ######-------------------------------------------------------
# Border Menu  ######-------------------------------------------------------

class VIEW3D_BorderMenu(bpy.types.Menu):
    bl_label = "Border Menu"
    bl_idname = "bordermenu"

    def draw(self, context):
        layout = self.layout
        view = context.space_data

        layout.prop(view, "use_render_border", text="Render Border")
        layout.operator("view3d.render_border", text="Draw Render Border...")
        layout.operator("view3d.clip_border", text="Draw Clipping Border...")


# Navigation  ######-------------------------------------------------------
# Navigation  ######-------------------------------------------------------

class VIEW3D_NaviMenu(bpy.types.Menu):
    bl_label = "Navigation"
    bl_idname = "navimenu"

    def draw(self, context):
        from math import pi
        layout = self.layout

        layout.operator_enum("view3d.view_orbit", "type")

        layout.separator()

        layout.operator("view3d.view_roll", text="Roll Left").angle = pi / -12.0
        layout.operator("view3d.view_roll", text="Roll Right").angle = pi / 12.0

        layout.separator()

        layout.operator_enum("view3d.view_pan", "type")

        layout.separator()

        layout.operator("view3d.zoom", text="Zoom In").delta = 1
        layout.operator("view3d.zoom", text="Zoom Out").delta = -1


# Lock View  ######-------------------------------------------------------
# Lock View  ######-------------------------------------------------------

class VIEW3D_LockMenu(bpy.types.Menu):
    bl_label = "Lock View"
    bl_idname = "lockmenu"

    def draw(self, context):
        layout = self.layout
        view = context.space_data

        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("view3d.view_lock_to_active")
        layout.operator("view3d.view_lock_clear")

        layout.separator()

        layout.label(text="View to Object:")
        layout.prop(view, "lock_object", text="")


# View Menu  ######-------------------------------------------------------
# View Menu  ######-------------------------------------------------------

class VIEW3D_MT_VIEWMENU(bpy.types.Menu):
    bl_idname = "view_setup"
    bl_label = "View Setup"

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

        view = context.space_data

        obj = context.active_object
        toolsettings = context.tool_settings

        layout.operator("view3d.view_all", icon="VIEWZOOM")
        layout.operator("view3d.view_center_cursor", text="View to Cursor")
        layout.operator("view3d.view_selected", text="View to Selected")
        layout.operator("view3d.zoom_border", text="Zoom with Border", icon="BORDERMOVE")

        layout.separator()

        layout.operator("view3d.localview", text="View Global/Local")
        layout.operator("view3d.view_persportho", text="View Persp/Ortho")

        layout.separator()
        layout.menu("VIEW3D_MT_object_showhide", icon="RESTRICT_VIEW_OFF")
        layout.operator("view3d.layers", text="Show All Layers").nr = 0

        layout.separator()

        layout.operator("lookat.it", text="Look @ Obj")
        layout.operator("lookat.cursor", text="Look @ Cursor")

        layout.separator()

        layout.operator("view3d.fly")
        layout.operator("view3d.walk")

        layout.separator()

        layout.menu("3dnavimenu", icon="MANIPUL")

        layout.menu("lockmenu")

        layout.separator()

        layout.operator("screen.region_quadview", text="Quad View", icon="SPLITSCREEN")
        layout.operator("screen.screen_full_area", text="Full Screen", icon="GO_LEFT")
        layout.operator("screen.area_dupli", text="Duplicate Window", icon="SCREEN_BACK")

bpy.utils.register_class(VIEW3D_MT_VIEWMENU)


# View & Camera  ######-------------------------------------------------------
# View & Camera  ######-------------------------------------------------------

class VIEW3D_Space_CamView(bpy.types.Menu):
    """Align Camera & View"""
    bl_label = "View & Camera"
    bl_idname = "space_camview"

    def draw(self, context):
        from math import pi
        layout = self.layout
        view = context.space_data

        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("view3d.view_all", icon="VIEWZOOM")
        layout.operator("view3d.view_center_cursor", text="View to Cursor")
        layout.operator("view3d.view_selected", text="View to Selected")
        layout.operator("view3d.zoom_border", text="Zoom with Border", icon="BORDERMOVE")

        layout.separator()

        layout.operator("view3d.localview", text="View Global/Local")
        layout.operator("view3d.view_persportho", text="View Persp/Ortho")

        layout.separator()
        layout.menu("VIEW3D_MT_object_showhide", icon="RESTRICT_VIEW_OFF")
        layout.operator("view3d.layers", text="Show All Layers").nr = 0

        layout.separator()

        layout.operator("lookat.it", text="Look @ Obj")
        layout.operator("lookat.cursor", text="Look @ Cursor")

        layout.separator()

        layout.menu("bordermenu", icon="RENDER_REGION")
        layout.menu("cameraviewmenu", icon="OUTLINER_DATA_CAMERA")

        layout.separator()

        layout.menu("3dnavimenu", icon="MANIPUL")

        layout.menu("lockmenu")

        layout.separator()

        layout.operator("screen.animation_play", text="Playback Animation", icon="TRIA_RIGHT")

        layout.separator()

        layout.operator("view3d.fly")
        layout.operator("view3d.walk")


###############################################################################################################################################################
###############################################################################################################################################################
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ###
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ###
###############################################################################################################################################################
###############################################################################################################################################################


def register():

    bpy.utils.register_class(VIEW3D_NaviMenu)
    bpy.utils.register_class(VIEW3D_LockMenu)

    bpy.utils.register_class(VIEW3D_BorderMenu)
    bpy.utils.register_class(VIEW3D_CameraViewMenu)
    bpy.utils.register_class(VIEW3D_3DNaviMenu)

    bpy.utils.register_class(VIEW3D_Space_CamView)


def unregister():

    bpy.utils.unregister_class(VIEW3D_Space_CamView)


if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_Space_CamView.bl_idname)
