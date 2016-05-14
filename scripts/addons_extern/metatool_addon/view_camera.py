# bl_info = {
#    "name": "Display View & Camera Menu",
#    "author": "Multiple Authors, mkbreuer",
#    "version": (0, 1, 0),
#    "blender": (2, 7, 2),
#    "location": "View3D",
#    "description": "[ALT+ONE] Tools for View & Camera",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "User Display"}


import bpy
from bpy import *

######------------#####################################################################################################################
######  Sub Menu  #####################################################################################################################
######  Sub Menu  #####################################################################################################################
######------------#####################################################################################################################

# AnimationPlayer  #######-------------------------------------------------------
# AnimationPlayer  #######-------------------------------------------------------


class VIEW3D_AnimationPlayer(bpy.types.Menu):
    bl_label = "Animation Player"
    bl_idname = "htk_player"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        toolsettings = context.tool_settings
        screen = context.screen

        layout.operator("screen.frame_jump", text="Jump REW", icon='REW').end = False
        layout.operator("screen.keyframe_jump", text="Previous FR", icon='PREV_KEYFRAME').next = False
        layout.operator("screen.animation_play", text="Reverse", icon='PLAY_REVERSE').reverse = True

        layout.operator("screen.animation_play", text="PLAY", icon='PLAY')

        layout.operator("screen.animation_play", text="Stop", icon='PAUSE')

        layout.operator("screen.keyframe_jump", text="Next FR", icon='NEXT_KEYFRAME').next = True
        layout.operator("screen.frame_jump", text="Jump FF", icon='FF').end = True

bpy.utils.register_class(VIEW3D_AnimationPlayer)


# 3D Navigation  #######-------------------------------------------------------
# 3D Navigation  #######-------------------------------------------------------

class VIEW3D_3DNaviMenu(bpy.types.Menu):
    bl_label = "3D Navigation"
    bl_idname = "3dnavimenu"

    def draw(self, context):
        layout = self.layout

        layout.operator("view3d.viewnumpad", text="Camera").type = 'CAMERA'
        layout.operator("view3d.viewnumpad", text="Top").type = 'TOP'
        layout.operator("view3d.viewnumpad", text="Bottom").type = 'BOTTOM'
        layout.operator("view3d.viewnumpad", text="Front").type = 'FRONT'
        layout.operator("view3d.viewnumpad", text="Back").type = 'BACK'
        layout.operator("view3d.viewnumpad", text="Right").type = 'RIGHT'
        layout.operator("view3d.viewnumpad", text="Left").type = 'LEFT'


bpy.utils.register_class(VIEW3D_3DNaviMenu)


# Border  #######-------------------------------------------------------
# Border  #######-------------------------------------------------------

class VIEW3D_BorderMenu(bpy.types.Menu):
    bl_label = "Border..."
    bl_idname = "bordermenu"

    def draw(self, context):
        layout = self.layout
        view = context.space_data

        layout.prop(view, "use_render_border", text="Render Border")
        layout.operator("view3d.render_border", text="Draw Render Border...")
        layout.operator("view3d.clip_border", text="Draw Clipping Border...")

bpy.utils.register_class(VIEW3D_BorderMenu)


# Camera View  #######-------------------------------------------------------
# Camera View  #######-------------------------------------------------------

class VIEW3D_CameraViewMenu(bpy.types.Menu):
    bl_label = "Camera View"
    bl_idname = "cameraviewmenu"

    def draw(self, context):
        layout = self.layout

        layout.prop(context.space_data, "lock_camera")

        layout.separator()

        layout.operator("view3d.zoom_camera_1_to_1", text="Zoom Camera 1:1")

        layout.separator()

        layout.operator("view3d.viewnumpad", text="Active Camera").type = 'CAMERA'
        layout.operator("view3d.object_as_camera")

        layout.operator("view3d.camera_to_view", text="Align Active Camera to View")
        layout.operator("view3d.camera_to_view_selected", text="Align Active Camera to Selected")

        layout.separator()

        layout.operator("object.build_dolly_rig")
        layout.operator("object.build_crane_rig")

bpy.utils.register_class(VIEW3D_CameraViewMenu)


# Navigation  #######-------------------------------------------------------
# Navigation  #######-------------------------------------------------------

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

bpy.utils.register_class(VIEW3D_NaviMenu)


######-------------------#############################################################################################################
######  View & Cam Menu  #############################################################################################################
######  View & Cam Menu  #############################################################################################################
######-------------------#############################################################################################################


class VIEW3D_PieViewMenu(bpy.types.Menu):
    """View"""
    bl_label = "View Menu"
    bl_idname = "meta_pieviewmenu"

    def draw(self, context):
        from math import pi
        layout = self.layout
        view = context.space_data

        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.prop(view, "lens")

        layout.separator()

        layout.menu("3dnavimenu", icon="MANIPUL")
        layout.menu("navimenu", text="View Rotation", icon="NDOF_TURN")
        layout.menu("VIEW3D_MT_view_align_selected", text="View around Active")

        layout.separator()

        layout.operator("view3d.layers", text="Show All Layers").nr = 0

        layout.separator()

        layout.operator("lookat.it", text="Look @ Object (Y-Axis)")
        layout.operator("lookat.cursor", text="Look @ Cursor (Y-Axis)")

        layout.separator()

        layout.operator("view3d.view_lock_to_active")
        layout.operator("view3d.view_lock_clear")

        layout.separator()

        layout.label(text="Lock to Object:")
        layout.prop(view, "lock_object", text="")

        layout.separator()

        layout.prop(view, "lock_cursor", text="Lock to Cursor")
        layout.prop(view, "lock_camera")


######------------################################################################################################################
######  Registry  ################################################################################################################
######  Registry  ################################################################################################################
######------------################################################################################################################


def register():

    bpy.utils.register_class(VIEW3D_PieViewMenu)
    # bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_class(VIEW3D_PieViewMenu)
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_PieViewMenu.bl_idname)
