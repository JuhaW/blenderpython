# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {
    "name": "Floating Sliders",
    "author": "Bassam Kurdali",
    "version": (0, 9, 1),
    "blender": (2, 7, 0),
    "location": "View3D",
    "description": "Sliders for 3D View",
    "warning": "May be incompatible with some keymaps",
    "wiki_url": "http://wiki.tube.freefac.org/wiki/Popup_Slider",
    "tracker_url": "",
    "category": "Animation"}

import bpy
import bgl
import blf
from bpy_extras import view3d_utils

handle = None
active_prop = ""
keyframed = False
animated = False


def is_animated(context, prop):
    ''' Check if the properties are animated for color/ behavior needs '''
    scene = context.scene
    object = context.active_object
    bone = context.active_pose_bone

    animated = keyframed = False
    if object.animation_data and object.animation_data.action:
        for fcurve in object.animation_data.action.fcurves:
            if bone.name and prop in fcurve.data_path:
                animated = True
                for key in fcurve.keyframe_points:
                    if scene.frame_current == key.co[0]:
                        keyframed = True
                        break
                break
    return (animated, keyframed)


def locator(context, x_offset, y_offset, slider_width, slider_height):
    ''' get location and properties of slider for drawing and interaction '''
    region = context.region
    rv3d = context.space_data.region_3d
    bone = context.active_pose_bone
    locmat = context.active_object.matrix_world * bone.matrix
    location = view3d_utils.location_3d_to_region_2d(
        region, rv3d, locmat.to_translation())
    x0 = int(1 * location[0])
    y0 = int(1 * location[1])
    items = (
        item for item in bone.keys()
        if not item.startswith('_') and type(bone[item]) is float)
    x_start = x0 + x_offset
    y_start = y0 + y_offset
    y_min = y_start - slider_height // 2
    y_max = y_start + slider_height // 2
    x_end = x_start + slider_width
    return (x0, y0, x_start, x_end, y_start, y_min, y_max, bone, items)


def draw_callback(x_offset, y_offset, slider_width, slider_height):
    ''' draw sliders on the screen conditionally '''
    context = bpy.context
    area = context.area
    region = context.region
    rv3d = context.space_data.region_3d
    anim_color =\
        context.user_preferences.themes[0].user_interface.wcol_state.inner_anim
    key_color =\
        context.user_preferences.themes[0].user_interface.wcol_state.inner_key
    if area.type == 'VIEW_3D':
        if context.mode == 'POSE' and context.active_pose_bone:

            x0, y0, x_start, x_end, y_start, y_min, y_max, bone, items =\
                locator(
                    context, x_offset, y_offset, slider_width, slider_height)
            bgl.glEnable(bgl.GL_BLEND)

            font_id = 0  # XXX, need to find out how best to get this.

            for index, prop in enumerate(items):
                animated, keyframed = is_animated(context, prop)
                prop_min = bone["_RNA_UI"][prop]["min"]
                prop_max = bone["_RNA_UI"][prop]["max"]
                offset = index * 40

                bgl.glColor4f(1.0, 1.0, 1.0, 0.5)
                # draw some text
                blf.position(font_id, x_end + 10, y_start - offset, 0)
                blf.size(font_id, 12, 72)
                if animated:
                    color = key_color if keyframed else anim_color
                    bgl.glColor4f(color[0], color[1], color[2], 0.9)
                blf.draw(font_id, '{} {:.3f}'.format(prop, bone[prop]))

                bgl.glColor4f(1.0, 1.0, 1.0, 0.5)
                bgl.glLineWidth(1)

                bgl.glBegin(bgl.GL_LINE_STRIP)
                bgl.glVertex2i(x_start, y_start - offset)
                bgl.glVertex2i(x_end, y_start - offset)
                bgl.glEnd()

                bgl.glLineWidth(2)

                bgl.glBegin(bgl.GL_LINE_STRIP)
                bgl.glVertex2i(x_start, y_min - offset)
                bgl.glVertex2i(x_start, y_max - offset)
                bgl.glEnd()

                bgl.glBegin(bgl.GL_LINE_STRIP)
                bgl.glVertex2i(x_end, y_min - offset)
                bgl.glVertex2i(x_end, y_max - offset)
                bgl.glEnd()

                bgl.glColor4f(1.0, 0.0, 0.0, 0.8)
                bgl.glLineWidth(3)

                bgl.glBegin(bgl.GL_LINE_STRIP)
                percent = (bone[prop] - prop_min) / (prop_max - prop_min)
                value = x_start + int(percent * slider_width)
                bgl.glVertex2i(value - 2, y_start - 2 - offset)
                bgl.glVertex2i(value + 2, y_start - 2 - offset)
                bgl.glVertex2i(value + 2, y_start + 2 - offset)
                bgl.glVertex2i(value - 2, y_start + 2 - offset)
                bgl.glEnd()
            # restore opengl defaults
            bgl.glLineWidth(1)
            bgl.glDisable(bgl.GL_BLEND)
            bgl.glColor4f(0.0, 0.0, 0.0, 1.0)


def set_value(context, bone, prop, x_mouse, x_start, x_end):
    ''' set property value from slider location '''
    old_value = bone[prop]
    prop_min = bone["_RNA_UI"][prop]["min"]
    prop_max = bone["_RNA_UI"][prop]["max"]
    raw_value = (x_mouse - x_start) / (x_end - x_start)
    value = prop_min + raw_value * (prop_max - prop_min)
    value = min(prop_max, max(prop_min, value))  # limit by minmax
    if value != old_value:
        bone[prop] = value
    if abs(value - old_value) >= 0.005:
        context.active_object.update_tag({'OBJECT'})
        context.scene.update()


def fallback_interaction(context):
    '''Fall back in case pass through doesn't automatically '''
    result = {'PASS_THROUGH'}
    if bpy.ops.view3d.manipulator.poll():
        result = bpy.ops.view3d.manipulator('INVOKE_DEFAULT')
    if result == {'PASS_THROUGH'}:
        if context.user_preferences.inputs.select_mouse == 'LEFT':
            bpy.ops.view3d.select('INVOKE_DEFAULT')
        else:
            bpy.ops.view3d.cursor3d('INVOKE_DEFAULT')


class EditProps(bpy.types.Operator):
    '''Edit the Properties of the Active Bone'''
    bl_idname = "view3d.edit_props"
    bl_label = "Edit Active Bone Props"
    bl_options = {'UNDO'}
    in_some_slider = bpy.props.BoolProperty(default=False)
    slider_index = bpy.props.IntProperty(default=-1)
    myprop = bpy.props.StringProperty(default='')
    invokement = bpy.props.EnumProperty(items=(
        ('click', 'click', 'click'),
        ('press', 'press', 'press'),
        ('tweak', 'tweak', 'tweak')))

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D' and context.mode == 'POSE'

    def modal(self, context, event):
        if context.mode != 'POSE' or not context.active_pose_bone:
            fallback_interaction(context)
            return {'PASS_THROUGH', 'CANCELLED'}
        context.area.tag_redraw()
        x_offset = 20
        y_offset = -20
        slider_width = 100
        slider_height = 10
        x0, y0, x_start, x_end, y_start, y_min, y_max, bone, items =\
            locator(
                context, x_offset, y_offset, slider_width, slider_height)
        x_mouse = event.mouse_region_x
        y_mouse = event.mouse_region_y
        in_some_slider = self.properties.in_some_slider
        slider_index = self.properties.slider_index
        if not in_some_slider:
            for index, prop in enumerate(items):
                offset = index * 40
                if y_mouse > y_min - offset and y_mouse < y_max - offset and \
                        x_mouse >= x_start and x_mouse <= x_end:
                    set_value(context, bone, prop, x_mouse, x_start, x_end)
                    self.properties.myprop = prop
                    self.properties.in_some_slider = True
                    self.properties.slider_index = index
                    break

        if self.properties.in_some_slider:
            prop = self.properties.myprop
            set_value(context, bone, prop, x_mouse, x_start, x_end)
        else:
            fallback_interaction(context)
            return {'PASS_THROUGH', 'CANCELLED'}

        if event.type == 'LEFTMOUSE' and event.value == 'RELEASE':
            return {'FINISHED'}

        elif event.type in {'ESC', 'RIGHTMOUSE'}:
            return {'CANCELLED'}
        else:
            return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run operator")
            return {'CANCELLED'}


class BasicMenu(bpy.types.Menu):
    bl_idname = "POSE_MT_Keyframe_Slider"
    bl_label = "Keyframe:"

    @classmethod
    def poll(cls, context):
        return context.mode == 'POSE'

    def draw(self, context):
        global active_prop, keyframed, animated
        layout = self.layout
        bone = context.active_pose_bone
        object = context.active_object
        # layout.prop(bone, '["{}"]'.format(active_prop), text='')
        if keyframed:
            insert = layout.operator(
                'view3d.menu_props', text='  Replace')
            insert.myprop = active_prop
            insert.operation = 'insert_keyframe'
            delete = layout.operator(
                'view3d.menu_props', text='  Delete')
            delete.myprop = active_prop
            delete.operation = 'delete_keyframe'
        else:
            insert = layout.operator(
                'view3d.menu_props', text='  Insert')
            insert.myprop = active_prop
            insert.operation = 'insert_keyframe'


class KeyframeProp(bpy.types.Operator):
    '''Keyframe the property of the Active Bone'''
    bl_idname = "view3d.menu_props"
    bl_label = "Menu Active Bone Props"
    myprop = bpy.props.StringProperty(default="")
    bl_options = {'UNDO'}
    operation = bpy.props.EnumProperty(items=[
        ('insert_keyframe', 'Insert Keyframe', 'Insert Keyframe at frame'),
        ('delete_keyframe', 'Delete Keyframe', 'Delete Current Keyframe')])

    @classmethod
    def poll(cls, context):
        return context.mode == 'POSE' and context.active_pose_bone

    def invoke(self, context, event):
        global active_prop, animated, keyframed
        object = context.active_object

        x_offset = 20
        y_offset = -20
        slider_width = 100
        slider_height = 10
        x0, y0, x_start, x_end, y_start, y_min, y_max, bone, items = locator(
            context, x_offset, y_offset, slider_width, slider_height)
        x_mouse = event.mouse_region_x
        y_mouse = event.mouse_region_y
        animated = False
        keyframed = False
        for index, prop in enumerate(items):
            offset = index * 40
            if y_mouse > y_min - offset and y_mouse < y_max - offset and \
                    x_mouse >= x_start and x_mouse <= x_end:
                self.properties.myprop = prop
                # check if bone is animated
                animated, keyframed = is_animated(context, prop)
                active_prop = prop
                bpy.ops.wm.call_menu(name=BasicMenu.bl_idname)
                return {'FINISHED'}
        return {'PASS_THROUGH', 'CANCELLED'}

    def draw(self, context):
        pass

    def execute(self, context):
        bone = context.active_pose_bone
        prop = self.properties.myprop
        operation = self.properties.operation
        if operation == 'insert_keyframe':
            bone.keyframe_insert('["{}"]'.format(prop))
        elif operation == 'delete_keyframe':
            bone.keyframe_delete('["{}"]'.format(prop))
        else:
            pass
        return {'FINISHED'}


def register():
    global handle

    handle = bpy.types.SpaceView3D.draw_handler_add(
        draw_callback, (20, -20, 100, 10), 'WINDOW', 'POST_PIXEL')
    bpy.utils.register_class(BasicMenu)
    bpy.utils.register_class(KeyframeProp)
    bpy.utils.register_class(EditProps)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if not kc:
        kc = wm.keyconfigs.user
        if not kc:
            kc = wm.keyconfigs.default

    if 'Pose' in kc.keymaps:
        km = kc.keymaps['Pose']
    else:
        km = kc.keymaps.new(name='Pose')
    kmi = km.keymap_items.new(
        EditProps.bl_idname, 'LEFTMOUSE', 'PRESS', head=True)
    kmi = km.keymap_items.new(
        KeyframeProp.bl_idname, 'RIGHTMOUSE', 'PRESS', head=True)


def unregister():
    global handle

    wm = bpy.context.window_manager
    for kc in (wm.keyconfigs.addon, wm.keyconfigs.user, wm.keyconfigs.default):
        if kc:
            for km in kc.keymaps:
                for kmi in km.keymap_items:
                    if kmi.idname in (EditProps.bl_idname, KeyframeProp.bl_idname):
                        km.keymap_items.remove(kmi)

    bpy.types.SpaceView3D.draw_handler_remove(handle, 'WINDOW')
    bpy.utils.unregister_class(EditProps)
    bpy.utils.unregister_class(KeyframeProp)
    bpy.utils.unregister_class(BasicMenu)

if __name__ == '__main__':
    register()
