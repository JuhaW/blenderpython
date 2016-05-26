#  Authored by Joel Daniels, 2014.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#  As a necessary part of its function, files this script creates are
#  also removed from the hard disk.  User assumes liability for setting
#  paths in any way that interferes with user or system files.

import bpy
import bmesh
import os
from extensions_framework import util as efutil

bl_info = {
    "name": "Ghost Frames",
    "author": "Joel Daniels",
    "version": (0, 0, 2),
    "blender": (2, 7, 2),
    "location": "3D View > UI",
    "description": "Onion skinning tool that creates OpenGL renders from the perspective of the active camera and sets them as background images",
    "warning": "Set the output path carefully! When using the 'Remove Ghost Frames' operator, everything in this directory will be cleared!",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Animation"}


def realpath(path):
    return os.path.realpath(efutil.filesystem_path(path))


class OBJECT_OT_GhostFrames(bpy.types.Operator):
    bl_idname = "ghost.ghost_frames"
    bl_label = "Ghost Frames"

    def execute(self, context):
        scene = context.scene

        if scene.camera is None:
            self.report({'ERROR'}, "No camera in the scene!")
            return {'CANCELLED'}
        else:
            for window in context.window_manager.windows:
                screen = window.screen
                for area in screen.areas:
                    if area.type == 'VIEW_3D':
                        space = area.spaces[0]
                        view_orig = space.region_3d.view_perspective
                        space.region_3d.view_perspective = 'CAMERA'
                        break

            image_names = []

            # Find output path.
            output_path = realpath(bpy.context.user_preferences.addons['ghost_frames'].preferences.ghostframes_path)
            if output_path == '' or output_path == (os.path.sep).join(bpy.app.binary_path.split(os.path.sep)[:-1]):
                self.report({'ERROR'}, "No output path selected in user preferences!")
                return {'CANCELLED'}
            if not os.path.exists(output_path):
                os.mkdir(output_path)

            # Create subdirectory. Make it, if it doesn't exist.
            output_path = os.path.join(output_path, "ghost_frames")
            if not os.path.exists(output_path):
                os.mkdir(output_path)
            for i in os.listdir(output_path):
                os.remove(os.path.join(output_path, i))

            # Render frames.
            current_frame = scene.frame_current
            filepath_place_holder = scene.render.filepath
            transp_place_holder = scene.render.alpha_mode
            color_place_holder = scene.render.image_settings.color_mode
            format_place_holder = scene.render.image_settings.file_format
            scene.render.image_settings.file_format = 'PNG'
            scene.render.image_settings.color_mode = 'RGBA'
            scene.render.alpha_mode = 'TRANSPARENT'
            if not scene.ghosting.current_only:
                frame_list = [frame for frame in range(scene.ghosting.frame_start, (scene.ghosting.frame_end + 1), scene.ghosting.frame_step)]
            else:
                frame_list = [scene.frame_current]
            for frame in frame_list:
                scene.frame_set(frame)
                scene.render.filepath = os.path.join(output_path, str(frame))
                bpy.ops.render.opengl(write_still=True, view_context=False)
                image_names.append(str(frame) + scene.render.file_extension)

            # Set background images.
            for img in image_names:
                img_path = os.path.join(output_path, img)
                b_img = space.background_images.new()
                img_data = bpy.data.images.load(img_path)
                b_img.image = img_data
                b_img.view_axis = 'CAMERA'
                b_img.draw_depth = scene.ghosting.orientation
                b_img.opacity = scene.ghosting.opacity

            # Settings.
            space.show_background_images = True
            space.region_3d.view_perspective = view_orig
            scene.render.filepath = filepath_place_holder  # Reset to the user's filepath
            scene.render.alpha_mode = transp_place_holder
            scene.frame_set(current_frame)
            scene.render.image_settings.file_format = format_place_holder
            scene.render.image_settings.color_mode = color_place_holder

        return {'FINISHED'}


class OBJECT_OT_RemoveGhostFrames(bpy.types.Operator):
    bl_idname = "ghost.remove_imgs"
    bl_label = "Remove Ghost Frames"

    def execute(self, context):
        for window in context.window_manager.windows:
            screen = window.screen
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    space = area.spaces[0]
                    for b_img in space.background_images:
                        if b_img:
                            img = b_img.image
                            if img is not None:
                                b_img.image = None
                                img.user_clear()
                                bpy.data.images.remove(img)
                                space.background_images.remove(b_img)
        return {'FINISHED'}


class OBJECT_OT_RemoveCurrentGhostFrame(bpy.types.Operator):
    bl_idname = "ghost.remove_current"
    bl_label = "Remove Current Ghost Frame"

    def execute(self, context):
        scene = context.scene
        for window in context.window_manager.windows:
            screen = window.screen
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    space = area.spaces[0]
                    for b_img in space.background_images:
                        if b_img:
                            img = b_img.image
                            if img is not None:
                                if img.name == str(scene.frame_current) + scene.render.file_extension:
                                    b_img.image = None
                                    img.user_clear()
                                    bpy.data.images.remove(img)
                                    space.background_images.remove(b_img)
        return {'FINISHED'}

#------------------------------------
# User preferences UI
#------------------------------------


class GhostFramesPreferencesPanel(bpy.types.AddonPreferences):
    bl_idname = __module__
    ghostframes_path = bpy.props.StringProperty(name="Ghost Frames Path",
                                                description="Path to save ghost frames",
                                                subtype='DIR_PATH',
                                                default="")

    def draw(self, context):
        self.layout.label("Select this path carefully!")
        self.layout.prop(self, "ghostframes_path")


#------------------------------------
# Viewport panel.
#------------------------------------
class VIEW3D_PT_GhostFrames(bpy.types.Panel):
    bl_label = "Ghost Frames"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.operator("ghost.ghost_frames", icon='GHOST_ENABLED')
        layout.prop(scene.ghosting, "current_only")
        row = layout.row(align=True)
        row.active = scene.ghosting.current_only == False
        row.prop(scene.ghosting, "frame_start")
        row.prop(scene.ghosting, "frame_end")
        layout.prop(scene.ghosting, "frame_step")
        layout.prop(scene.ghosting, "orientation")
        layout.prop(scene.ghosting, "opacity")
        layout.operator("ghost.remove_imgs", icon='GHOST_DISABLED')
        layout.operator("ghost.remove_current")


class OBJECT_GhostFramesProps(bpy.types.PropertyGroup):
    frame_start = bpy.props.IntProperty(name="Start Frame",
                                        description="",
                                        default=1)

    frame_end = bpy.props.IntProperty(name="End Frame",
                                      description="",
                                      default=250)

    frame_step = bpy.props.IntProperty(name="Frame Step",
                                       default=1,
                                       min=1)

    current_only = bpy.props.BoolProperty(name="Current Frame Only",
                                          description="",
                                          default=True)

    orientation = bpy.props.EnumProperty(name="Orientation",
                                         description="Front / back placement of images in viewport",
                                         items=[
                                             ('BACK', "Back", "Put images behind objects"),
                                             ('FRONT', "Front", "Put images in front of objects")],
                                         default='BACK')

    opacity = bpy.props.FloatProperty(name="Opacity",
                                      description="Opacity of images",
                                      default=0.5,
                                      min=0,
                                      max=1)


def register():
    bpy.utils.register_class(GhostFramesPreferencesPanel)
    bpy.utils.register_class(OBJECT_OT_GhostFrames)
    bpy.utils.register_class(OBJECT_GhostFramesProps)
    bpy.utils.register_class(OBJECT_OT_RemoveGhostFrames)
    bpy.utils.register_class(OBJECT_OT_RemoveCurrentGhostFrame)
    bpy.utils.register_class(VIEW3D_PT_GhostFrames)
    bpy.types.Scene.ghosting = bpy.props.PointerProperty(type=OBJECT_GhostFramesProps)


def unregister():
    bpy.utils.unregister_class(GhostFramesPreferencesPanel)
    bpy.utils.unregister_class(OBJECT_OT_GhostFrames)
    bpy.utils.unregister_class(OBJECT_GhostFramesProps)
    bpy.utils.unregister_class(OBJECT_OT_RemoveGhostFrames)
    bpy.utils.unregister_class(OBJECT_OT_RemoveCurrentGhostFrame)
    bpy.utils.unregister_class(VIEW3D_PT_GhostFrames)

if __name__ == "__main__":
    register()
