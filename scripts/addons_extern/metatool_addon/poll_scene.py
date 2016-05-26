# bl_info = {
#    "name": "MetaToolkit Extension",
#    "author": "marvin.k.breuer",
#    "version": (0, 1, 0),
#    "blender": (2, 72, 0),
#    "location": "View3D > Toolbar",
#    "warning": "",
#    "description": "MetaToolkit Extension",
#    "wiki_url": "",
#    "category": "User Panel",
#}


import bpy
from bpy import *

# property group containing all properties for the gui in the panel
# Dropdown Arrow ### general display properties = arrow tooltips


class DropdownMetaToolProps(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.metawindowtool
    """
    # Scene Tools
    display_tab_nav = bpy.props.BoolProperty(name="Navigation", description="Display Navigation Tools", default=False)
    display_tab_view = bpy.props.BoolProperty(name="3D View", description="Display 3D View Tools", default=False)
    display_tab_cam = bpy.props.BoolProperty(name="Camera View", description="Display Camera & View Tools", default=False)
    display_tab_light = bpy.props.BoolProperty(name="Lightning", description="Display Lightning Tools", default=False)
    display_tab_anim = bpy.props.BoolProperty(name="Animation", description="Display Animation Tools & Key Mover in Timeline ", default=False)
    display_tab_render = bpy.props.BoolProperty(name="Animation", description="Display Animation Tools & Key Mover in Timeline ", default=False)


#########################################################
###----------------  VISUAL  -------------------------###
###----------------  VISUAL  -------------------------###
#########################################################

# Sub Location
class SubLoc_SCENE():
    """Scene Tools"""
    bl_category = "SCENE"
    #bl_region_type = 'TOOLS'
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(cls, context):
        return context.scene.osc_scene

# Sub Panel


class META_TAB_Scene(SubLoc_SCENE, bpy.types.Panel):
    """Scene Tools"""
    #bl_idname = "scene.tools"
    bl_label = "[SCENE]"

    def draw(self, context):
        lt = context.window_manager.metawindowtool
        view = context.space_data
        obj = bpy.context.scene.objects.active
        scene = context.scene
        toolsettings = context.tool_settings
        screen = context.screen
        layout = self.layout
        self.scn = context.scene

# -------------------------------------------------------
# 3D Navigation  #######-------------------------------------------------------
# 3D Navigation  #######-------------------------------------------------------
# -------------------------------------------------------

        col = layout.column(align=True)
        split = col.split()  # percentage=0.15)

        if lt.display_tab_nav:
            split.prop(lt, "display_tab_nav", text="...3D Nav...", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "display_tab_nav", text="...3D Nav...", icon='RIGHTARROW')

        #spread_op = split.operator("", text="", icon="")

        if lt.display_tab_nav:

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)

            row.operator("view3d.viewnumpad", text="Front").type = 'FRONT'
            row.operator("view3d.viewnumpad", text="Back").type = 'BACK'

            row = col_top.row(align=True)
            row.operator("view3d.viewnumpad", text="Left").type = 'LEFT'
            row.operator("view3d.viewnumpad", text="Right").type = 'RIGHT'

            row = col_top.row(align=True)
            row.operator("view3d.viewnumpad", text="Top").type = 'TOP'
            row.operator("view3d.viewnumpad", text="Bottom").type = 'BOTTOM'


# -------------------------------------------------------
# 3D View  #######-------------------------------------------------------
# 3D View  #######-------------------------------------------------------
# -------------------------------------------------------

        #col = layout.column(align=True)
        split = col.split()  # percentage=0.15)

        if lt.display_tab_view:
            split.prop(lt, "display_tab_view", text="...3D View...", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "display_tab_view", text="...3D View...", icon='RIGHTARROW')

        #spread_op = split.operator("", text="", icon="")

        if lt.display_tab_view:
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("view3d.localview", text="View Global/Local")
            row = col_top.row(align=True)
            row.operator("view3d.view_persportho", text="View Persp/Ortho")

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("lookat.it", text="Look @ Obj")
            row = col_top.row(align=True)
            row.operator("lookat.cursor", text="Look @ Cursor")
            row = col_top.row(align=True)
            row.label("local y-axis")

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.label(text="View to Object:")
            row = col_top.row(align=True)
            row.prop(view, "lock_object", text="")
            row = col_top.row(align=True)
            row.operator("view3d.view_center_cursor", text="to Cursor")
            row = col_top.row(align=True)
            row.operator("view3d.view_selected", text="to Selected")


# -------------------------------------------------------
# Lightning  #######-------------------------------------------------------
# Lightning  #######-------------------------------------------------------
# -------------------------------------------------------

        #col = layout.column(align=True)
        split = col.split()  # percentage=0.15)

        if lt.display_tab_light:
            split.prop(lt, "display_tab_light", text="...Studio...", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "display_tab_light", text="...Studio...", icon='RIGHTARROW')

        #spread_op = split.operator("", text="", icon="")

        if lt.display_tab_light:
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.operator("object.lamp_add", text="", icon="LAMP_POINT").type = 'POINT'
            row.operator("object.lamp_add", text="", icon="LAMP_SUN").type = 'SUN'
            row.operator("object.lamp_add", text="", icon="LAMP_SPOT").type = 'SPOT'
            row.operator("object.lamp_add", text="", icon="LAMP_HEMI").type = 'HEMI'
            row.operator("object.lamp_add", text="", icon="LAMP_AREA").type = 'AREA'

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.1
            row.operator("object.trilighting_new", text="Tri-Lighting", icon="LAMP")

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.menu("INFO_MT_add", text="Create", icon="OUTLINER_DATA_SURFACE")
            row.menu("INFO_MT_add", text="Create", icon="OUTLINER_DATA_SURFACE")

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)

            row.operator("animation.silhouette_on", icon='GHOST_ENABLED')
            row.operator("animation.silhouette_half")
            row.operator("animation.silhouette_off")


# -------------------------------------------------------
# Camera  #######-------------------------------------------------------
# Camera  #######-------------------------------------------------------
# -------------------------------------------------------

        #col = layout.column(align=True)
        split = col.split()  # percentage=0.15)

        if lt.display_tab_cam:
            split.prop(lt, "display_tab_cam", text="...Camera...", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "display_tab_cam", text="...Camera...", icon='RIGHTARROW')

        #spread_op = split.operator("", text="", icon="")

        if lt.display_tab_cam:

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("object.camera_add", icon="CAMERA_DATA")
            row.prop(context.object.data, "draw_size", text="Size")

            row = col_top.row(align=True)
            row.operator("object.build_dolly_rig", "Rig Dolly")
            row.operator("object.build_crane_rig", "Rig Crane")

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("view3d.viewnumpad", text="Active Cam").type = 'CAMERA'
            row.operator("view3d.object_as_camera", "Obj as Cam")

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("view3d.camera_to_view", text="Cam to View")
            row.operator("view3d.camera_to_view_selected", text="Cam to Selected")

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.prop(context.space_data, "lock_camera")

            if (context.active_object is not None):
                if (context.active_object.type != 'CAMERA'):
                    buf = context.active_object.name

                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)

                    #row = layout.row(align=False)
                    row.operator("object.rotate_around", icon='OUTLINER_DATA_CAMERA')
                    row.label(buf, icon='MESH_DATA')
                    row = col_top.row(align=True)
                    row.prop(scene, "use_cursor")

                    row = col_top.row(align=True)
                    row.prop(scene, "camera")
                    #row = layout.row()
                    #row.prop(scene, "frame_start")
                    #row.prop(scene, "frame_end")

                    row = col_top.row(align=True)
                    row.prop(scene, "camera_revol_x")
                    row.prop(scene, "camera_revol_y")
                    row.prop(scene, "camera_revol_z")

                    row = col_top.row(align=True)
                    row.prop(scene, "inverse_x")
                    row.prop(scene, "inverse_y")
                    row.prop(scene, "inverse_z")

                    row = col_top.row(align=True)
                    row.prop(scene, "back_forw")
                else:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    buf = "No valid object selected"
                    row.label(buf, icon='MESH_DATA')

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.column_flow(2)

            row.prop(context.object.data, "show_guide", text="Composition guides")
            row.prop(context.object.data, "show_limits", text="Limits")
            row.prop(context.object.data, "show_mist", text="Mist")
            row.prop(context.object.data, "show_sensor", text="Sensor")
            row.prop(context.object.data, "show_name", text="Name")
            row.prop(context.object.data, "show_passepartout", text="Passepartout")
            row.prop(context.object.data, "passepartout_alpha", text="Alpha", slider=True)


# -------------------------------------------------------
# Animation  #######-------------------------------------------------------
# Animation  #######-------------------------------------------------------
# -------------------------------------------------------

        #col = layout.column(align=True)
        split = col.split()  # percentage=0.15)

        if lt.display_tab_anim:
            split.prop(lt, "display_tab_anim", text="...Animation...", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "display_tab_anim", text="...Animation...", icon='RIGHTARROW')

        #spread_op = split.operator("", text="", icon="")

        if lt.display_tab_anim:

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.operator("screen.frame_jump", text="", icon='REW').end = False
            row.operator("screen.keyframe_jump", text="", icon='PREV_KEYFRAME').next = False

            if not screen.is_animation_playing:
                # if using JACK and A/V sync:
                #   hide the play-reversed button
                #   since JACK transport doesn't support reversed playback
                if scene.sync_mode == 'AUDIO_SYNC' and context.user_preferences.system.audio_device == 'JACK':
                    row.operator("screen.animation_play", text="", icon='PLAY')
                else:
                    row.operator("screen.animation_play", text="", icon='PLAY_REVERSE').reverse = True
                    row.operator("screen.animation_play", text="", icon='PLAY')
            else:
                row.operator("screen.animation_play", text="", icon='PAUSE')

            row.operator("screen.keyframe_jump", text="", icon='NEXT_KEYFRAME').next = True
            row.operator("screen.frame_jump", text="", icon='FF').end = True

            if context.mode == "OBJECT" or context.mode == "POSE":

                if context.active_object and context.active_object.type in {'MESH', 'CURVE', 'SURFACE', 'ARMATURE', 'META', 'LATTICE'}:

                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)

                    row.operator("anim.keyframe_insert_menu", icon='ZOOMIN', text="")
                    row.operator("anim.keyframe_delete_v3d", icon='ZOOMOUT', text="")
                    row.prop_search(context.scene.keying_sets_all, "active", context.scene, "keying_sets_all", text="")
                    row.operator("anim.keyframe_insert", text="", icon='KEY_HLT')
                    row.operator("anim.keyframe_delete", text="", icon='KEY_DEHLT')

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.prop(scene, "use_preview_range", text="", toggle=True)
            row.prop(scene, "lock_frame_selection_to_range", text="", toggle=True)

            row.prop(scene, "frame_current", text="")

            row = col_top.row(align=True)
            if not scene.use_preview_range:
                row.prop(scene, "frame_start", text="Start")
                row.prop(scene, "frame_end", text="End")
            else:
                row.prop(scene, "frame_preview_start", text="Start")
                row.prop(scene, "frame_preview_end", text="End")

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("object.paths_calculate", text="Calculate Motion Path", icon="ANIM_DATA")
            row = col_top.row(align=True)
            row.operator("object.paths_clear", text="Clear Path Catch", icon="PANEL_CLOSE")

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("nla.bake", text="Bake new Action", icon="ACTION_TWEAK")

# -------------------------------------------------------
# Render  #######-------------------------------------------------------
# Render  #######-------------------------------------------------------
# -------------------------------------------------------

        #col = layout.column(align=True)
        split = col.split()  # percentage=0.15)

        if lt.display_tab_render:
            split.prop(lt, "display_tab_render", text="...Render...", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "display_tab_render", text="...Render...", icon='RIGHTARROW')

        #spread_op = split.operator("", text="", icon="")

        if lt.display_tab_render:

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("render.render", text="Still", icon='RENDER_STILL')
            row.operator("render.render", text="Animation", icon='RENDER_ANIMATION').animation = True

            row = col_top.row(align=True)
            row.operator("render.opengl", text="Still_OpGL", icon='RENDER_STILL')
            row.operator("render.opengl", text="Anim_OpGL", icon='RENDER_ANIMATION').animation = True

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.operator("render.play_rendered_anim", text="Play rendered Animation", icon='PLAY')


############------------############
############  REGISTER  ############
############------------############


def register():

    bpy.utils.register_class(DropdownMetaToolProps)
    bpy.types.WindowManager.metawindowtool = bpy.props.PointerProperty(type=DropdownMetaToolProps)

    # bpy.utils.register_class(META_TAB_Scene)

    bpy.utils.register_module(__name__)


def unregister():
    # bpy.utils.unregister_class(META_TAB_Scene)
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
