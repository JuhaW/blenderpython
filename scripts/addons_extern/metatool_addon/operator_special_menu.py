bl_info = {
    "name": "Display Special Menu",
    "author": "Multiple Authors, mkbreuer",
    "version": (0, 1, 1),
    "blender": (2, 7, 2),
    "location": "View3D",
    "description": "Special Menu (W)",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "User Display"}


import bpy
import re
from bpy import *


######------------#####################################################################################################################
######  Sub Menu  #####################################################################################################################
######  Sub Menu  #####################################################################################################################
######------------#####################################################################################################################

# Subdivide #######------------------------------------------------
# Subdivide #######------------------------------------------------

class SubdivideCUT(bpy.types.Menu):
    bl_label = "Subdivide"
    bl_idname = "htk_subdivide"

    def draw(self, context):
        layout = self.layout

        layout.operator("mesh.subdivide", text="1-Cut").number_cuts = 1
        layout.operator("mesh.subdivide", text="2-Cuts").number_cuts = 2
        layout.operator("mesh.subdivide", text="3-Cuts").number_cuts = 3
        layout.operator("mesh.subdivide", text="4-Cuts").number_cuts = 4
        layout.operator("mesh.subdivide", text="5-Cuts").number_cuts = 5
        layout.operator("mesh.subdivide", text="6-Cuts").number_cuts = 6

bpy.utils.register_class(SubdivideCUT)


# Subdivide #######------------------------------------------------
# Subdivide #######------------------------------------------------

class CurveSmooth(bpy.types.Menu):
    bl_label = "Curve Smooth"
    bl_idname = "htk_smooth"

    def draw(self, context):
        layout = self.layout

        layout.operator("curve.smooth")
        layout.operator("curve.smooth_weight")
        layout.operator("curve.smooth_radius")
        layout.operator("curve.smooth_tilt")

bpy.utils.register_class(CurveSmooth)


# BoolTool ############------------------
# BoolTool ############------------------

class BoolToolMenu(bpy.types.Menu):
    bl_label = "BoolTool"
    bl_idname = "htk_booltool"

    def draw(self, context):
        layout = self.layout

        layout.operator("btool.boolean_union", text="Union Brush", icon="ROTATECOLLECTION")
        layout.operator("btool.boolean_inters", text="Intersection Brush", icon="ROTATECENTER")
        layout.operator("btool.boolean_diff", text="Difference Brush", icon="ROTACTIVE")

        layout.separator()

        layout.operator("btool.boolean_union_direct", text="Union Brush", icon="ROTATECOLLECTION")
        layout.operator("btool.boolean_inters_direct", text="Intersection Brush", icon="ROTATECENTER")
        layout.operator("btool.boolean_diff_direct", text="Difference Brush", icon="ROTACTIVE")

        layout.separator()

        layout.operator("btool.draw_polybrush", icon="LINE_DATA")

bpy.utils.register_class(BoolToolMenu)


# Flymode  ##################-------------------------------------------------------
# Flymode  ##################-------------------------------------------------------

class Navigatestop(bpy.types.Operator):
    bl_idname = "view3d.fast_navigate_stop_new"
    bl_label = "Navigate Stop"

    def execute(self, context):
        bpy.ops.view3d.fast_navigate_stop()
        bpy.context.space_data.viewport_shade = 'SOLID'

        return {'FINISHED'}

bpy.utils.register_class(Navigatestop)


class View3D_Modifly(bpy.types.Menu):
    bl_label = "Flymode"
    bl_idname = "htk_modifly"

    def draw(self, context):
        active_obj = context.active_object
        layout = self.layout

        scene = context.scene

        layout.operator("view3d.fast_navigate_operator", icon="MOD_SOFT")
        layout.operator("view3d.fast_navigate_stop_new")

        layout.separator()

        layout.prop(scene, "OriginalMode", "")

        layout.prop(scene, "FastMode", "")

        layout.separator()

        layout.prop(scene, "EditActive", "Edit mode")

        layout.separator()

        layout.prop(scene, "Delay")
        layout.prop(scene, "DelayTimeGlobal")

        layout.separator()

        layout.prop(scene, "ShowParticles")
        layout.prop(scene, "ParticlesPercentageDisplay")

bpy.utils.register_class(View3D_Modifly)


# Menus Relations  #######-------------------------------------------------------
# Menus Relations  #######-------------------------------------------------------

class VIEW3D_MT_Relation_Menu(bpy.types.Menu):
    bl_label = "Relation Menu"
    bl_idname = "htk_relation"

    def draw(self, context):
        layout = self.layout

        obj = context
        if obj and obj.mode == 'OBJECT':

            layout.menu("htk_parent", icon="CONSTRAINT")
            layout.menu("htk_group")
            layout.menu("htk_constraint")

            layout.separator()

            layout.menu("VIEW3D_MT_make_links", text="M.Links", icon="LINKED")
            layout.menu("VIEW3D_MT_make_single_user", text="Single User")

            layout.separator()

            layout.operator("object.visual_transform_apply", icon="NDOF_DOM")

            layout.separator()

            layout.operator("object.duplicates_make_real")

            layout.separator()

            layout.operator("help.relation", text="make single from dupli", icon="INFO")

        obj = context
        if obj and obj.mode == 'EDIT_ARMATURE':
            layout.menu("VIEW3D_MT_edit_armature_parent", icon='CONSTRAINT')

        obj = context
        if obj and obj.mode == 'POSE':
            arm = context.active_object.data

            layout.menu("VIEW3D_MT_object_parent", icon='CONSTRAINT')
            layout.menu("VIEW3D_MT_pose_ik")
            layout.menu("VIEW3D_MT_pose_constraints")

bpy.utils.register_class(VIEW3D_MT_Relation_Menu)


class help_text(bpy.types.Operator):
    bl_idname = "help.relation"
    bl_label = ''

    def draw(self, context):
        layout = self.layout
        layout.label('1. parent selected to activ')
        layout.label('2. apply Make Duplicates Real')
        layout.label('3. clear Parent / 4. to Join > selected Linked Object Data')

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=300)

bpy.utils.register_class(help_text)


# Menus Constraint  ######-------------------------------------
# Menus Constraint  ######-------------------------------------

class VIEW3D_MT_Constraint_Menu(bpy.types.Menu):
    bl_label = "Constraint Menu"
    bl_idname = "htk_constraint"

    def draw(self, context):
        layout = self.layout

        layout.operator_menu_enum("object.constraint_add", "type", text="  Constraint", icon="CONSTRAINT_DATA")
        #layout.operator("object.track_set",text=">>>  Track  <<<")

        layout.separator()

        layout.label(text="to Selected:", icon="LAYER_ACTIVE")
        layout.operator("track.to", text="-> Track To")
        layout.operator("damped.track", text="-> Damped Track")
        layout.operator("lock.track", text="-> Lock Track")

        layout.separator()

        layout.label(text="to CursorPos+Empty:", icon="LAYER_ACTIVE")
        layout.operator("track.toempty", text="-> Track To")
        layout.operator("damped.trackempty", text="-> Damped Track")
        layout.operator("lock.trackempty", text="-> Lock Track")

bpy.utils.register_class(VIEW3D_MT_Constraint_Menu)


# Menus Parent  ######-------------------------------------
# Menus Parent  ######-------------------------------------

class VIEW3D_MT_Parent_Menu(bpy.types.Menu):
    bl_label = "Parent Menu"
    bl_idname = "htk_parent"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.parent_set", text="Set")

        layout.separator()

        layout.operator("object.parent_clear").type = "CLEAR"
        layout.operator("object.parent_clear", text="Clear Inverse").type = "CLEAR_INVERSE"
        layout.operator("object.parent_clear", text="Clear Keep Transform").type = "CLEAR_KEEP_TRANSFORM"

bpy.utils.register_class(VIEW3D_MT_Parent_Menu)


# Menus Group  ######-------------------------------------
# Menus Group  ######-------------------------------------

class VIEW3D_MT_Group_Menu(bpy.types.Menu):
    bl_label = "Group Menu"
    bl_idname = "htk_group"

    def draw(self, context):
        layout = self.layout

        layout.operator("group.create", text="Group")
        layout.operator("group.objects_add_active", text="-> to Active")

        layout.separator()

        layout.operator("group.objects_remove", text="Remove")
        layout.operator("group.objects_remove_active", text="-> from Active")

bpy.utils.register_class(VIEW3D_MT_Group_Menu)


# Menus Sculpt  #######-------------------------------------------------------
# Menus Sculpt  #######-------------------------------------------------------

class VIEW3D_SculptBrush(bpy.types.Menu):
    bl_label = "Sculpt Brushes"
    bl_idname = "htk_sculpt"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("paint.brush_select", text='Blob', icon='BRUSH_BLOB').sculpt_tool = 'BLOB'

        # layout.separator()

        layout.operator("paint.brush_select", text="Clay", icon='BRUSH_CLAY').sculpt_tool = 'CLAY'
        layout.operator("paint.brush_select", text='Claystrips', icon='BRUSH_CREASE').sculpt_tool = 'CLAY_STRIPS'

        # layout.separator()

        layout.operator("paint.brush_select", text="Crease", icon='BRUSH_CREASE').sculpt_tool = 'CREASE'

        layout.operator("paint.brush_select", text='Brush', icon='BRUSH_SCULPT_DRAW').sculpt_tool = 'DRAW'
        layout.operator("paint.brush_select", text='Fill/Deepen', icon='BRUSH_FILL').sculpt_tool = 'FILL'

        layout.operator("paint.brush_select", text='Flatten', icon='BRUSH_FLATTEN').sculpt_tool = 'FLATTEN'
        layout.operator("paint.brush_select", text='Grab', icon='BRUSH_GRAB').sculpt_tool = 'GRAB'

        layout.operator("paint.brush_select", text='Inflate/Deflate', icon='BRUSH_INFLATE').sculpt_tool = 'INFLATE'
        layout.operator("paint.brush_select", text='Layer', icon='BRUSH_LAYER').sculpt_tool = 'LAYER'

        layout.operator("paint.brush_select", text='Mask', icon='BRUSH_MASK').sculpt_tool = 'MASK'
        layout.operator("paint.brush_select", text='Nudge', icon='BRUSH_NUDGE').sculpt_tool = 'NUDGE'

        layout.operator("paint.brush_select", text='Pinch/Magnify', icon='BRUSH_PINCH').sculpt_tool = 'PINCH'
        layout.operator("paint.brush_select", text='Twist', icon='BRUSH_ROTATE').sculpt_tool = 'ROTATE'

        layout.operator("paint.brush_select", text='Scrape/Peaks', icon='BRUSH_SCRAPE').sculpt_tool = 'SCRAPE'
        layout.operator("paint.brush_select", text='Polish', icon='BRUSH_FLATTEN')

        layout.operator("paint.brush_select", text='Smooth', icon='BRUSH_SMOOTH').sculpt_tool = 'SMOOTH'
        layout.operator("paint.brush_select", text='Snakehook', icon='BRUSH_SNAKE_HOOK').sculpt_tool = 'SNAKE_HOOK'

        layout.operator("paint.brush_select", text='Thumb', icon='BRUSH_THUMB').sculpt_tool = 'THUMB'

bpy.utils.register_class(VIEW3D_SculptBrush)


# Menus Texture  #######-------------------------------------------------------
# Menus Texture  #######-------------------------------------------------------

class VIEW3D_TextureBrush(bpy.types.Menu):
    bl_label = "Texture Brushes"
    bl_idname = "htk_texture"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        #layout.operator("paint.brush_select", text='Brush', icon='BRUSH_TEXDRAW').texture_paint_tool= 'BRUSH'
        layout.operator("paint.brush_select", text='Clone', icon='BRUSH_CLONE').texture_paint_tool = 'CLONE'

        layout.operator("paint.brush_select", text='Draw', icon='BRUSH_TEXDRAW').texture_paint_tool = 'DRAW'
        layout.operator("paint.brush_select", text='Fill', icon='BRUSH_TEXFILL').texture_paint_tool = 'FILL'

        layout.operator("paint.brush_select", text='Mask', icon='BRUSH_TEXMASK').texture_paint_tool = 'MASK'
        layout.operator("paint.brush_select", text='Smear', icon='BRUSH_SMEAR').texture_paint_tool = 'SMEAR'

        layout.operator("paint.brush_select", text='Soften', icon='BRUSH_SOFTEN').texture_paint_tool = 'SOFTEN'
        layout.operator("paint.brush_select", text='TexDraw', icon='BRUSH_TEXDRAW').texture_paint_tool = 'TEXDRAW'

bpy.utils.register_class(VIEW3D_TextureBrush)


# Menus Vertex Paint  #######-------------------------------------------------------
# Menus Vertex Paint  #######-------------------------------------------------------

class VIEW3D_VertexBrush(bpy.types.Menu):
    bl_label = "Vertex Brushes"
    bl_idname = "htk_vertex"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("paint.brush_select", text='Add', icon='BRUSH_ADD').vertex_paint_tool = 'ADD'
        layout.operator("paint.brush_select", text='Blur', icon='BRUSH_MIX').vertex_paint_tool = 'BLUR'

        layout.operator("paint.brush_select", text='Darken', icon='BRUSH_DARKEN').vertex_paint_tool = 'DARKEN'
        layout.operator("paint.brush_select", text='Lighten', icon='BRUSH_LIGHTEN').vertex_paint_tool = 'LIGHTEN'

        layout.operator("paint.brush_select", text='Mix', icon='BRUSH_MIX').vertex_paint_tool = 'MIX'
        layout.operator("paint.brush_select", text='Multiply', icon='BRUSH_MULTIPLY').vertex_paint_tool = 'MUL'

        layout.operator("paint.brush_select", text='Substract', icon='BRUSH_SUBTRACT').vertex_paint_tool = 'SUB'

bpy.utils.register_class(VIEW3D_VertexBrush)


# Menus Weights  #######-------------------------------------------------------
# Menus Weights  #######-------------------------------------------------------

class VIEW3D_Paint_Weight(bpy.types.Menu):
    bl_label = "Weights"

    def draw(self, context):
        layout = self.layout

        layout.operator("paint.weight_from_bones", text="Assign Automatic From Bones").type = 'AUTOMATIC'
        layout.operator("paint.weight_from_bones", text="Assign From Bone Envelopes").type = 'ENVELOPES'

        layout.separator()

        layout.operator("object.vertex_group_normalize_all", text="Normalize All")
        layout.operator("object.vertex_group_normalize", text="Normalize")
        layout.operator("object.vertex_group_mirror", text="Mirror")
        layout.operator("object.vertex_group_invert", text="Invert")

        layout.separator()

        layout.operator("object.vertex_group_clean", text="Clean")
        layout.operator("object.vertex_group_quantize", text="Quantize")
        layout.operator("object.vertex_group_levels", text="Levels")
        layout.operator("object.vertex_group_blend", text="Blend")

        layout.separator()

        layout.operator("object.vertex_group_transfer_weight", text="Transfer Weights")
        layout.operator("object.vertex_group_limit_total", text="Limit Total")
        layout.operator("object.vertex_group_fix", text="Fix Deforms")

        layout.separator()

        layout.operator("paint.weight_set")

bpy.utils.register_class(VIEW3D_Paint_Weight)


class VIEW3D_WeightBrush(bpy.types.Menu):
    bl_label = "Weight Brushes"
    bl_idname = "htk_weight"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.menu("htk_vertex", icon='BRUSH_DATA')
        layout.menu("VIEW3D_MT_brush")

bpy.utils.register_class(VIEW3D_WeightBrush)


# Menus Armature  #######-------------------------------------------------------
# Menus Armature  #######-------------------------------------------------------

class VIEW3D_MT_EditArmatureTK(bpy.types.Menu):
    bl_label = "Armature Tools"

    def draw(self, context):
        layout = self.layout

        # Edit Armature

        layout.operator("transform.transform", text="Scale Envelope Distance").mode = 'BONE_SIZE'

        layout.operator("transform.transform", text="Scale B-Bone Width").mode = 'BONE_SIZE'

        layout.separator()

        layout.operator("armature.extrude_move")

        layout.operator("armature.extrude_forked")

        layout.operator("armature.duplicate_move")
        layout.operator("armature.merge")
        layout.operator("armature.fill")
        layout.operator("armature.delete")
        layout.operator("armature.separate")

        layout.separator()

        layout.operator("armature.subdivide", text="Subdivide")
        layout.operator("armature.switch_direction", text="Switch Direction")

bpy.utils.register_class(VIEW3D_MT_EditArmatureTK)


class VIEW3D_MT_ArmatureName(bpy.types.Menu):
    bl_label = "Armature Name"

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'EXEC_AREA'

        layout.operator("armature.autoside_names", text="AutoName Left/Right").type = 'XAXIS'
        layout.operator("armature.autoside_names", text="AutoName Front/Back").type = 'YAXIS'
        layout.operator("armature.autoside_names", text="AutoName Top/Bottom").type = 'ZAXIS'
        layout.operator("armature.flip_names")

bpy.utils.register_class(VIEW3D_MT_ArmatureName)


class VIEW3D_MT_ArmatureCut(bpy.types.Menu):
    bl_label = "Subdivide"

    def draw(self, context):
        layout = self.layout

        layout.operator("armature.subdivide", text="1 Cut").number_cuts = 1
        layout.operator("armature.subdivide", text="2 Cut").number_cuts = 2
        layout.operator("armature.subdivide", text="3 Cut").number_cuts = 3
        layout.operator("armature.subdivide", text="4 Cut").number_cuts = 4
        layout.operator("armature.subdivide", text="5 Cut").number_cuts = 5
        layout.operator("armature.subdivide", text="6 Cut").number_cuts = 6

bpy.utils.register_class(VIEW3D_MT_ArmatureCut)


# Menus Pose  #######-------------------------------------------------------
# Menus Pose  #######-------------------------------------------------------

class VIEW3D_MT_PoseCopy(bpy.types.Menu):
    bl_label = "Pose Copy"

    def draw(self, context):
        layout = self.layout

        layout.operator("pose.copy")
        layout.operator("pose.paste")
        layout.operator("pose.paste", text="Paste X-Flipped Pose").flipped = True

        layout.separator()

bpy.utils.register_class(VIEW3D_MT_PoseCopy)


class VIEW3D_MT_PoseNames(bpy.types.Menu):
    bl_label = "Pose Copy"

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'EXEC_AREA'
        layout.operator("pose.autoside_names", text="AutoName Left/Right").axis = 'XAXIS'
        layout.operator("pose.autoside_names", text="AutoName Front/Back").axis = 'YAXIS'
        layout.operator("pose.autoside_names", text="AutoName Top/Bottom").axis = 'ZAXIS'

        layout.operator("pose.flip_names")

bpy.utils.register_class(VIEW3D_MT_PoseNames)


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

        layout.operator("render.play_rendered_anim", icon='TRIA_RIGHT')

        layout.separator()

        layout.operator("screen.frame_jump", text="Jump REW", icon='REW').end = False
        layout.operator("screen.keyframe_jump", text="Previous FR", icon='PREV_KEYFRAME').next = False
        layout.operator("screen.animation_play", text="Reverse", icon='PLAY_REVERSE').reverse = True

        layout.operator("screen.animation_play", text="PLAY", icon='PLAY')

        layout.operator("screen.animation_play", text="Stop", icon='PAUSE')

        layout.operator("screen.keyframe_jump", text="Next FR", icon='NEXT_KEYFRAME').next = True
        layout.operator("screen.frame_jump", text="Jump FF", icon='FF').end = True

bpy.utils.register_class(VIEW3D_AnimationPlayer)


# Lock View  #######-------------------------------------------------------
# Lock View  #######-------------------------------------------------------

class VIEW3D_LockView(bpy.types.Menu):
    bl_label = "Lock View to..."
    bl_idname = "htk_lockview"

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

        view = context.space_data

        layout.label("To Object:")

        layout.prop(view, "lock_object", text="")

        lock_object = view.lock_object
        if lock_object:
            if lock_object.type == 'ARMATURE':
                layout.prop_search(view, "lock_bone", lock_object.data,
                                   "edit_bones" if lock_object.mode == 'EDIT'
                                   else "bones",
                                   text="")
        else:
            layout.prop(view, "lock_cursor", text="Lock to Cursor")

        layout.prop(view, "lock_camera")


bpy.utils.register_class(VIEW3D_LockView)


# Render Menu  #######-------------------------------------------------------
# Render Menu  #######-------------------------------------------------------

class VIEW3D_RenderView(bpy.types.Menu):
    bl_label = "Render Menu"
    bl_idname = "htk_rendermenu"

    @classmethod
    def poll(cls, context):
        # add more special types
        return context.object

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        obj = context.object

        layout.operator("render.render", text="Still", icon='RENDER_STILL')
        layout.operator("render.render", text="Animation", icon='RENDER_ANIMATION').animation = True

        layout.separator()

        layout.operator("render.opengl", text="Still_OpenGL", icon='RENDER_STILL')
        layout.operator("render.opengl", text="Anim_OpenGL", icon='RENDER_ANIMATION').animation = True
        layout.menu("INFO_MT_opengl_render")

        layout.separator()

        layout.operator("render.view_show")

        layout.separator()

        props = layout.operator("object.isolate_type_render")
        props = layout.operator("object.hide_render_clear_all")

        layout.separator()

        if not scene.use_preview_range:
            layout.prop(scene, "frame_start", text="Start Frame")
            layout.prop(scene, "frame_end", text="End Frame")
        else:
            layout.prop(scene, "frame_preview_start", text="Start Frame")
            layout.prop(scene, "frame_preview_end", text="End Frame")

        layout.separator()

        view = context.space_data

        layout.prop(view, "use_render_border")
        layout.operator("view3d.render_border", text="Draw Render Border...")


bpy.utils.register_class(VIEW3D_RenderView)


# Render Menu  #######-------------------------------------------------------
# Render Menu  #######-------------------------------------------------------

class VIEW3D_SpecialExtras(bpy.types.Menu):
    bl_label = "Type Special"
    bl_idname = "htk_specialextras"

    @classmethod
    def poll(cls, context):
        # add more special types
        return context.object

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        obj = context.object

        # layout.separator()

        if obj.type == 'CAMERA':
            layout.operator_context = 'INVOKE_REGION_WIN'

            if obj.data.type == 'PERSP':
                props = layout.operator("wm.context_modal_mouse", text="Camera Lens Angle")
                props.data_path_iter = "selected_editable_objects"
                props.data_path_item = "data.lens"
                props.input_scale = 0.1
                if obj.data.lens_unit == 'MILLIMETERS':
                    props.header_text = "Camera Lens Angle: %.1fmm"
                else:
                    props.header_text = "Camera Lens Angle: %.1f\u00B0"

            else:
                props = layout.operator("wm.context_modal_mouse", text="Camera Lens Scale")
                props.data_path_iter = "selected_editable_objects"
                props.data_path_item = "data.ortho_scale"
                props.input_scale = 0.01
                props.header_text = "Camera Lens Scale: %.3f"

            if not obj.data.dof_object:
                #layout.label(text="Test Has DOF obj");
                props = layout.operator("wm.context_modal_mouse", text="DOF Distance")
                props.data_path_iter = "selected_editable_objects"
                props.data_path_item = "data.dof_distance"
                props.input_scale = 0.02
                props.header_text = "DOF Distance: %.3f"

            layout.separator()

            view3d = context.space_data.region_3d
            cam = context.scene.camera.data

            if view3d.view_perspective == 'CAMERA':
                layout = self.layout

                layout.operator("view3d.render_border_camera", text="Camera as Render Border", icon="FULLSCREEN_ENTER")

                if cam.show_passepartout:
                    layout.prop(cam, "passepartout_alpha", text="Passepartout")
                else:
                    layout.prop(cam, "show_passepartout")

        if obj.type in {'CURVE', 'FONT'}:
            layout.operator_context = 'INVOKE_REGION_WIN'

            props = layout.operator("wm.context_modal_mouse", text="Extrude Size")
            props.data_path_iter = "selected_editable_objects"
            props.data_path_item = "data.extrude"
            props.input_scale = 0.01
            props.header_text = "Extrude Size: %.3f"

            props = layout.operator("wm.context_modal_mouse", text="Width Size")
            props.data_path_iter = "selected_editable_objects"
            props.data_path_item = "data.offset"
            props.input_scale = 0.01
            props.header_text = "Width Size: %.3f"

        if obj.type == 'EMPTY':
            layout.operator_context = 'INVOKE_REGION_WIN'

            props = layout.operator("wm.context_modal_mouse", text="Empty Draw Size")
            props.data_path_iter = "selected_editable_objects"
            props.data_path_item = "empty_draw_size"
            props.input_scale = 0.01
            props.header_text = "Empty Draw Size: %.3f"

        if obj.type == 'LAMP':
            lamp = obj.data

            layout.operator_context = 'INVOKE_REGION_WIN'

            if scene.render.use_shading_nodes:
                try:
                    value = lamp.node_tree.nodes["Emission"].inputs["Strength"].default_value
                except AttributeError:
                    value = None

                if value is not None:
                    props = layout.operator("wm.context_modal_mouse", text="Strength")
                    props.data_path_iter = "selected_editable_objects"
                    props.data_path_item = "data.node_tree.nodes[\"Emission\"].inputs[\"Strength\"].default_value"
                    props.header_text = "Lamp Strength: %.3f"
                    props.input_scale = 0.1
                del value

                if lamp.type == 'AREA':
                    props = layout.operator("wm.context_modal_mouse", text="Size X")
                    props.data_path_iter = "selected_editable_objects"
                    props.data_path_item = "data.size"
                    props.header_text = "Lamp Size X: %.3f"

                    if lamp.shape == 'RECTANGLE':
                        props = layout.operator("wm.context_modal_mouse", text="Size Y")
                        props.data_path_iter = "selected_editable_objects"
                        props.data_path_item = "data.size_y"
                        props.header_text = "Lamp Size Y: %.3f"

                elif lamp.type in {'SPOT', 'POINT', 'SUN'}:
                    props = layout.operator("wm.context_modal_mouse", text="Size")
                    props.data_path_iter = "selected_editable_objects"
                    props.data_path_item = "data.shadow_soft_size"
                    props.header_text = "Lamp Size: %.3f"
            else:
                props = layout.operator("wm.context_modal_mouse", text="Energy")
                props.data_path_iter = "selected_editable_objects"
                props.data_path_item = "data.energy"
                props.header_text = "Lamp Energy: %.3f"

                if lamp.type in {'SPOT', 'AREA', 'POINT'}:
                    props = layout.operator("wm.context_modal_mouse", text="Falloff Distance")
                    props.data_path_iter = "selected_editable_objects"
                    props.data_path_item = "data.distance"
                    props.input_scale = 0.1
                    props.header_text = "Lamp Falloff Distance: %.1f"

            if lamp.type == 'SPOT':
                layout.separator()
                props = layout.operator("wm.context_modal_mouse", text="Spot Size")
                props.data_path_iter = "selected_editable_objects"
                props.data_path_item = "data.spot_size"
                props.input_scale = 0.01
                props.header_text = "Spot Size: %.2f"

                props = layout.operator("wm.context_modal_mouse", text="Spot Blend")
                props.data_path_iter = "selected_editable_objects"
                props.data_path_item = "data.spot_blend"
                props.input_scale = -0.01
                props.header_text = "Spot Blend: %.2f"

                if not scene.render.use_shading_nodes:
                    props = layout.operator("wm.context_modal_mouse", text="Clip Start")
                    props.data_path_iter = "selected_editable_objects"
                    props.data_path_item = "data.shadow_buffer_clip_start"
                    props.input_scale = 0.05
                    props.header_text = "Clip Start: %.2f"

                    props = layout.operator("wm.context_modal_mouse", text="Clip End")
                    props.data_path_iter = "selected_editable_objects"
                    props.data_path_item = "data.shadow_buffer_clip_end"
                    props.input_scale = 0.05
                    props.header_text = "Clip End: %.2f"


bpy.utils.register_class(VIEW3D_SpecialExtras)


class DynDetailMenu(bpy.types.Menu):
    bl_label = "Detail Size"
    bl_idname = "view3d.dyn_detail"

    @classmethod
    def poll(cls, context):
        return (context.sculpt_object and context.tool_settings.sculpt)

    def draw(self, context):
        layout = self.layout

        toolsettings = context.tool_settings
        sculpt = toolsettings.sculpt
        settings = self.paint_settings(context)
        brush = settings.brush

        layout.operator("sculpt.dynamic_topology_toggle", icon='X', text="Disable Dyntopo")
        layout.operator("sculpt.dynamic_topology_toggle", icon='SCULPT_DYNTOPO', text="Enable Dyntopo")

        """
        col = layout.column()
        col.active = context.sculpt_object.use_dynamic_topology_sculpting
        sub = col.column(align=True)
        sub.active = (brush and brush.sculpt_tool != 'MASK')
        if (sculpt.detail_type_method == 'CONSTANT'):
            row = sub.row(align=True)
            row.prop(sculpt, "constant_detail")
            row.operator("sculpt.sample_detail_size", text="", icon='EYEDROPPER')
        else:
            sub.prop(sculpt, "detail_size")
        sub.prop(sculpt, "detail_refine_method", text="")
        sub.prop(sculpt, "detail_type_method", text="")
        col.separator()
        col.prop(sculpt, "use_smooth_shading")
        col.operator("sculpt.optimize")
        if (sculpt.detail_type_method == 'CONSTANT'):
            col.operator("sculpt.detail_flood_fill")
        col.separator()
        col.prop(sculpt, "symmetrize_direction")
        col.operator("sculpt.symmetrize")
        """


bpy.utils.register_class(DynDetailMenu)


######--------################################################################################################################
######  Menu  ################################################################################################################
######  Menu  ################################################################################################################
######------ -################################################################################################################


# Special Menu #######------------------------------------------------
# Special Menu #######------------------------------------------------

class VIEW3D_HTK_Special(bpy.types.Menu):
    bl_label = "Special Menu [w]"
    bl_idname = "htk_special"

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'


##########--------------##########
##########  Objectmode  ##########
##########--------------##########

        ob = context
        if ob.mode == 'OBJECT':

            layout.operator("wm.search_menu", text="Search", icon='VIEWZOOM')
            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")

            layout.separator()

            layout.operator("object.join", text="Join Object", icon='AUTOMERGE_ON')
            layout.operator("object.set_instance", text="Set as Instance")

            layout.separator()

            layout.operator("object.duplicate_move", text="Duplicate Objects")
            layout.operator("object.duplicate_move_linked", text="Duplicate Linked Objects")

            layout.separator()

            layout.operator("mesh.intersect_meshes", text="Intersection Line", icon="GROUP")
            layout.operator("object.editnormals_transfer", text="Transfer Normals", icon="SNAP_NORMAL")

            layout.separator()

            layout.operator("object.convert", text="Convert to Mesh", icon="OUTLINER_DATA_MESH").target = "MESH"
            layout.operator("object.convert", text="Convert to Curve", icon="OUTLINER_DATA_CURVE").target = "CURVE"

            layout.separator()

            layout.menu("htk_modispace", text="Modifier", icon='MODIFIER')
            layout.menu("htk_relation", text="Relations", icon='LINK_AREA')

            layout.menu("htk_booltool", text="BoolTools", icon='GROUP')
            layout.operator("cgcookie.polystrips", icon='IPO_BEZIER')
            layout.operator("cgcookie.retop_contour", text="Contour Retopogly", icon='MESH_UVSPHERE')

            layout.separator()

            layout.menu("htk_modifly", text="Flymode", icon='MOD_SOFT')

            layout.separator()

            #layout.menu("VIEW3D_MT_object_specials", text = "Special Render", icon = "LONGDISPLAY")
            layout.menu("htk_specialextras", icon='LAMP_DATA')
            layout.menu("htk_rendermenu", icon='SCENE')

            layout.separator()
            layout.menu("htk_player", text="Play Animation", icon='TRIA_RIGHT')
            layout.operator("render.play_rendered_anim", icon='TRIA_RIGHT')

            layout.separator()

            layout.menu("htk_lockview", icon='NDOF_DOM')

            layout.separator()

            layout.operator("scene.refresh", text="Refresh!", icon='FILE_REFRESH')

            scene = context.scene

            layout.prop(scene, "frame_current", text="Current Frame")


##########------------##########
##########  Editmode  ##########
##########------------##########

        elif ob.mode == 'EDIT_MESH':

            layout.operator("wm.search_menu", text="Search", icon='VIEWZOOM')
            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")

            layout.separator()

            layout.menu("VIEW3D_MT_edit_mesh_looptools", icon='RIGHTARROW_THIN')

            layout.separator()

            #layout.operator("mesh.subdivide", text="Subdivide").smoothness = 0.0
            layout.menu("htk_subdivide", text="Subdivide", icon='PARTICLE_POINT')
            layout.operator("mesh.unsubdivide", text="Un-Subdivide")
            layout.operator("mesh.subdivide", text="Subdivide Smooth").smoothness = 1.0

            layout.separator()

            layout.operator("mesh.merge", text="Merge...", icon="FULLSCREEN_EXIT")
            layout.operator("mesh.remove_doubles")

            layout.separator()

            layout.operator("mesh.spin", icon="ANIM_DATA")
            layout.operator("mesh.screw")

            layout.separator()

            props = layout.operator("mesh.knife_tool", text="Knife", icon="LINE_DATA")
            props.use_occlude_geometry = True
            props.only_selected = False
            props = layout.operator("mesh.knife_tool", text="Select")
            props.use_occlude_geometry = False
            props.only_selected = True
            layout.operator("mesh.knife_project")

            layout.separator()

            layout.operator("mesh.bisect")

            layout.separator()

            layout.operator("mesh.bevel", text="Bevel", icon="SPHERECURVE")
            layout.operator("mesh.inset")
            layout.operator("mesh.bridge_edge_loops")

            layout.separator()

            layout.operator("mesh.vertices_smooth", text="Vertices Smooth", icon="CURVE_DATA")
            layout.operator("mesh.vertices_smooth_laplacian", text="Laplacian Smooth")

            layout.separator()

            layout.operator_menu_enum("mesh.separate", "type", text="Separate")

            layout.separator()

            layout.operator("mesh.symmetrize")
            layout.operator("mesh.symmetry_snap")

            layout.separator()

            layout.operator("mesh.blend_from_shape")
            layout.operator("mesh.shape_propagate_to_all")
            layout.operator("mesh.shortest_path_select")
            layout.operator("mesh.sort_elements")


##########---------##########
##########  Curve  ##########
##########---------##########

        if ob.mode == 'EDIT_CURVE':

            # Setting Menu
            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")

            layout.separator()

            layout.menu("htk_curvesubdivide", icon="IPO_QUINT")

            layout.separator()

            layout.operator("curve.duplicate_move", "Duplicate")
            layout.operator("curve.extrude_move", "Extrude & Move")

            layout.separator()

            layout.menu("htk_smooth", "Smooth Curve")

            layout.separator()

            layout.operator("curve.split", icon="FULLSCREEN_ENTER")
            layout.operator("curve.separate")
            layout.operator("curve.make_segment")

            layout.separator()

            layout.operator_menu_enum("curve.handle_type_set", "type", icon="IPO_BEZIER")
            layout.operator("curve.normals_make_consistent")

            layout.separator()

            layout.operator("curve.switch_direction", icon="ARROW_LEFTRIGHT")
            layout.operator("curve.spline_weight_set")

            edit_object = context.edit_object
            if edit_object.type == 'CURVE':

                layout.operator("curve.radius_set")

            layout.separator()

            layout.operator("curve.cyclic_toggle")

            layout.separator()

            layout.menu("htk_modispace", text="Modifier", icon='RIGHTARROW_THIN')

            layout.separator()

            layout.menu("VIEW3D_MT_hook", icon="HOOK")

            layout.separator()

            layout.menu("VIEW3D_MT_edit_curve_showhide", icon="VISIBLE_IPO_ON")


##########-----------##########
##########  Surface  ##########
##########-----------##########

        if ob.mode == 'EDIT_SURFACE':

            # Setting Menu
            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")

            layout.separator()

            layout.menu("htk_curvesubdivide", icon="IPO_QUINT")

            layout.separator()

            layout.operator("curve.duplicate_move", "Duplicate")
            layout.operator("curve.extrude_move", "Extrude & Move")

            layout.separator()

            layout.menu("htk_smooth", "Smooth Curve")

            layout.separator()

            layout.operator("curve.split", icon="FULLSCREEN_ENTER")
            layout.operator("curve.separate")
            layout.operator("curve.make_segment")

            layout.separator()

            layout.operator("curve.switch_direction", icon="ARROW_LEFTRIGHT")
            layout.operator("curve.spline_weight_set")

            edit_object = context.edit_object
            if edit_object.type == 'CURVE':

                layout.operator("curve.radius_set")

            layout.separator()

            layout.operator("curve.cyclic_toggle")

            layout.separator()

            layout.menu("htk_modispace", text="Modifier")

            layout.separator()

            layout.menu("VIEW3D_MT_hook", icon="HOOK")

            layout.separator()

            layout.menu("VIEW3D_MT_edit_curve_showhide", icon="VISIBLE_IPO_ON")


##########------------##########
##########  Metaball  ##########
##########------------##########

        if ob.mode == 'EDIT_METABALL':

            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")

            layout.operator("mball.duplicate_metaelems")


##########-----------##########
##########  Lattice  ##########
##########-----------##########

        elif ob.mode == 'EDIT_LATTICE':

            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")

            layout.menu("VIEW3D_MT_TransformMenu", icon='SOLO_OFF')


##########------------##########
##########  Particle  ##########
##########------------##########

        if context.mode == 'PARTICLE':

            # Brush Menu
            #layout.menu("VIEW3D_ParticleBrush", text = "Brushes", icon='BRUSH_DATA')

            # layout.separator()

            layout.menu("VIEW3D_Paint_Particle", text="Hair Particles", icon='PARTICLEMODE')


##########---------------##########
##########  Weightpaint  ##########
##########---------------##########

        ob = context
        if ob.mode == 'PAINT_WEIGHT':

            layout.menu("htk_vertex", icon='BRUSH_DATA')
            layout.menu("VIEW3D_MT_brush")

            layout.separator()

            layout.menu("VIEW3D_Paint_Weight", icon='WPAINT_HLT')


##########---------------##########
##########  Vertexpaint  ##########
##########---------------##########

        elif ob.mode == 'PAINT_VERTEX':

            layout.menu("htk_vertex", icon='BRUSH_DATA')
            layout.menu("VIEW3D_MT_brush")

            layout.separator()

            layout.operator("paint.vertex_color_set", text="Set Color ", icon='VPAINT_HLT')
            layout.operator("paint.vertex_color_smooth", text="Smooth Color ")
            layout.operator("mesh.connected_vertex_colors", text="Connected Vertex Colors")

            layout.separator()

            layout.operator("paint.vertex_color_dirt", text="Dirt Color ", icon='TPAINT_HLT')

            layout.operator("paint.worn_edges", text="Worn Edges")


##########----------------##########
##########  Texturepaint  ##########
##########----------------##########

        elif ob.mode == 'PAINT_TEXTURE':

            layout.menu("htk_texture", icon='BRUSH_DATA')
            layout.menu("VIEW3D_MT_brush")


##########--------------##########
##########  Sculptmode  ##########
##########--------------##########

        elif ob.mode == 'SCULPT':

            layout.menu("view3d.dyn_detail")

            layout.separator()

            layout.menu("htk_sculpt", icon='BRUSH_DATA')
            layout.menu("VIEW3D_MT_brush")

            layout.separator()

            props = layout.operator("paint.hide_show", text="Box Hide", icon="BORDER_RECT")
            props.action = 'HIDE'
            props.area = 'INSIDE'

            props = layout.operator("paint.hide_show", text="Box Show")
            props.action = 'SHOW'
            props.area = 'INSIDE'

            layout.separator()

            props = layout.operator("paint.mask_flood_fill", text="Fill Mask", icon="BORDER_RECT")
            props.mode = 'VALUE'
            props.value = 1

            props = layout.operator("paint.mask_flood_fill", text="Clear Mask")
            props.mode = 'VALUE'
            props.value = 0

            layout.operator("paint.mask_flood_fill", text="Invert Mask").mode = 'INVERT'

            layout.separator()

            props = layout.operator("paint.hide_show", text="Show All", icon="RESTRICT_VIEW_OFF")
            props.action = 'SHOW'
            props.area = 'ALL'

            props = layout.operator("paint.hide_show", text="Hide Masked", icon="RESTRICT_VIEW_ON")
            props.area = 'MASKED'
            props.action = 'HIDE'


##########------------##########
##########  Armature  ##########
##########------------##########

        elif ob.mode == 'EDIT_ARMATURE':

            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")

            layout.separator()

            layout.menu("VIEW3D_MT_ArmatureCut")

            layout.separator()

            layout.menu("VIEW3D_MT_edit_armature_roll", icon='BONE_DATA')

            layout.menu("VIEW3D_MT_EditArmatureTK", icon='ARMATURE_DATA')

            layout.separator()

            layout.menu("VIEW3D_MT_edit_armature_parent", icon='CONSTRAINT')

            layout.separator()

            layout.menu("VIEW3D_MT_ArmatureName")

            layout.menu("VIEW3D_MT_bone_options_toggle", text="Bone Settings")


##########------------##########
##########  Posemode  ##########
##########------------##########

        if context.mode == 'POSE':

            arm = context.active_object.data

            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")

            layout.separator()

            if arm.draw_type in {'BBONE', 'ENVELOPE'}:
                layout.operator("transform.transform", text="Scale Envelope Distance").mode = 'BONE_SIZE'

            layout.menu("VIEW3D_MT_object_animation", icon="CLIP")
            layout.menu("VIEW3D_MT_pose_propagate")
            layout.menu("VIEW3D_MT_pose_slide")
            layout.menu("htk_player", text="Play Animation", icon="TRIA_RIGHT")
            layout.menu("VIEW3D_MT_object_specials", text="Special Render", icon="SCENE")

            layout.separator()

            layout.operator("pose.copy", icon="COPYDOWN")
            layout.operator("pose.paste", icon="PASTEDOWN")
            layout.operator("pose.paste", text="Paste X-Flipped Pose", icon="PASTEFLIPDOWN").flipped = True

            layout.separator()

            layout.menu("VIEW3D_MT_pose_library", icon="POSE_HLT")
            layout.menu("VIEW3D_MT_pose_motion")
            layout.menu("VIEW3D_MT_pose_group")

            layout.separator()

            layout.menu("VIEW3D_MT_object_parent", icon="CONSTRAINT_BONE")
            layout.menu("VIEW3D_MT_pose_constraints")
            layout.menu("VIEW3D_MT_pose_ik")

            layout.separator()

            layout.operator("pose.flip_names", icon="ARROW_LEFTRIGHT")
            layout.operator("pose.quaternions_flip")

            layout.separator()

            layout.operator_context = 'INVOKE_AREA'
            layout.operator("pose.bone_layers", text="Change Bone Layers...", icon="NLA")
            layout.operator("armature.armature_layers", text="Change Armature Layers...")

            layout.separator()

            layout.menu("VIEW3D_MT_bone_options_toggle", text="Bone Settings", icon="SCRIPTWIN")

            layout.separator()

            layout.menu("VIEW3D_MT_pose_showhide")

            layout.separator()

            scene = context.scene
            layout.prop(scene, "frame_current", text="Set Current Frame")

######------------################################################################################################################
######  Registry  ################################################################################################################
######  Registry  ################################################################################################################
######------------################################################################################################################


def abs(val):
    if val > 0:
        return val
    return -val


def register():

    bpy.utils.register_class(VIEW3D_HTK_Special)


def unregister():

    bpy.utils.unregister_class(VIEW3D_HTK_Special)

    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_HTK_Special.bl_idname)
