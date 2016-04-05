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

bl_info = {
    "name": "oenvoyage Toolset",
    "author": "Olivier Amrein",
    "version": (0, 2, 0),
    "blender": (2, 70),
    "location": "Everywhere!",
    "description": "A collection of tools and settings to improve productivity (based on Amaranth)",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Scene"}


import bpy
from bpy.types import Operator, AddonPreferences, Panel, Menu
from bpy.props import BoolProperty
from datetime import datetime, timedelta

# Preferences
class OenvoyageToolsetPreferences(AddonPreferences):
    bl_idname = __name__
    use_render_estimate = BoolProperty(
            name="Estimate Render time",
            description="show the panel with render estimation",
            default=True,
            )

    def draw(self, context):
        layout = self.layout

        layout.label(
            text="Here you can enable or disable specific tools, "
                 "in case they interfere with others or are just plain annoying")

        split = layout.split(percentage=0.25)

        col = split.column()
        sub = col.column(align=True)
        sub.label(text="Render Options", icon="RENDER_STILL")
        sub.prop(self, "use_render_estimate")

# Properties
def init_properties():

    scene = bpy.types.Scene
    
    scene.average_rendertime = bpy.props.FloatProperty(min=0, default=5, max = 200)

def clear_properties():
    props = (
        "use_render_estimate",
    )
    
    wm = bpy.context.window_manager
    for p in props:
        if p in wm:
            del wm[p]


# FEATURE: Estimate Time to Render an Animation
def hours_float_to_str(rendertime): 
    hours_int = int(rendertime)    
        
    left_mins = (rendertime - hours_int)*60
    if left_mins > 0:
        return "%d:%02d" % (hours_int,left_mins)
    else:
        return hours_int
 
def estimate_render_animation_time(self, context):
    preferences = context.user_preferences.addons[__name__].preferences
    
    if preferences.use_render_estimate:
        layout = self.layout
        scene = context.scene
            
        total_frames = scene.frame_end - scene.frame_start
        
        avg = scene.average_rendertime 
        estimated_rendertime = total_frames * avg/60

        rendertime_in_hours = hours_float_to_str(estimated_rendertime)
        
        estimated_finish_time = datetime.now() + timedelta(hours=estimated_rendertime)
        formatted_finish_time = '{:%a, %d %b @ %H:%M}'.format(estimated_finish_time)

        row = layout.row()
        split =layout.split()
        split.label("Average rendertime: ")
        
        split.prop(scene,"average_rendertime", text="mins")

        row = layout.row()
        row = row.label("Expected rendertime for %s frames is:"  % total_frames)
        row = layout.row()
        row = row.label("%s hours (ETA %s)"  % (rendertime_in_hours,formatted_finish_time))
# // FEATURE: Estimate Time to Render an Animation

# make a quick OpenGL render

# PIE menu

class VIEW3D_PIE_oenvoyage(Menu):
    bl_label = "Oenvoyage PIE"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        pie.operator("view3d.manipulator_set", icon='MAN_TRANS', text="Translate").type = 'TRANSLATE'
        aa = 10
        if aa == 12:
            pie.operator("view3d.view_selected")
        pie.prop(context.space_data, "show_manipulator")



class render_Quick_OpenGL(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "view3d.render_quickopengl"
    bl_label = "OpenGL Quick render"

    @classmethod
    def poll(cls, context):
        return 1

    def execute(self, context):
        render = context.scene.render
        space = bpy.context.space_data
        
        # pre preview
        space.show_only_render = True
        bpy.ops.render.opengl(animation = True)

        # post preview 
        space.show_only_render = False

        return {'FINISHED'}
    

# FEATURE: Select camera target (TrackTo like constraints)
class SelectCameraTarget(bpy.types.Operator):
    bl_idname = "view3d.select_camera_target"
    bl_label = "Select Camera Target"

    @classmethod
    def poll(cls, context):
        return context.active_object.type == 'CAMERA'

    def execute(self, context):
        if context.active_object.constraints:
            for const in context.active_object.constraints:
                print(const.type)
                if const.type in ('DAMPED_TRACK','LOCKED_TRACK','TRACK_TO'):
                    if const.target:
                        bpy.ops.object.select_all()
                        const.target.select = True
                        bpy.context.scene.objects.active = const.target
                    else:
                        self.report({'WARNING'},"No target for constraint found")
        else:
            self.report({'WARNING'},"No constraints found")

        return {'FINISHED'}


# FEATURE: Additional options in W special key
def special_key_options(self, context):

    obj = context.active_object
    scene = context.scene
    layout = self.layout
    
    if obj.type =='CAMERA':
        layout.separator()
        layout.operator("view3d.select_camera_target", icon="CONSTRAINT")   

    layout.operator("view3d.render_quickopengl",icon='RENDER_ANIMATION')   


# // FEATURE: Additional options in W


# FEATURE: Motion paths buttons in W special key
def motion_path_buttons(self, context):

    obj = context.active_object
    scene = context.scene

    self.layout.separator()
    if obj.motion_path:
        self.layout.operator("object.paths_update", text="Update Object Paths")
        self.layout.operator("object.paths_clear", text="Clear Object Paths")
    else:
        self.layout.operator("object.paths_calculate", text="Calculate Object Paths")
# // FEATURE: Motion paths buttons in W

addon_keymaps = []

def register():

    init_properties()

    bpy.utils.register_class(OenvoyageToolsetPreferences)

    # register Operators
    bpy.utils.register_class(SelectCameraTarget)
    bpy.utils.register_class(render_Quick_OpenGL)

    # register menus
    bpy.utils.register_class(VIEW3D_PIE_oenvoyage)

    
    # UI: Register the panels
    bpy.types.RENDER_PT_render.append(estimate_render_animation_time)
    bpy.types.VIEW3D_MT_object_specials.append(special_key_options)
    bpy.types.VIEW3D_MT_object_specials.append(motion_path_buttons)
    
    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(name='Object Non-modal')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'Q', 'PRESS', shift=True)
        kmi.properties.name = 'VIEW3D_PIE_oenvoyage'

        
        addon_keymaps.append(km)

def unregister():

    bpy.utils.unregister_class(OenvoyageToolsetPreferences)

    # unregister Operators
    bpy.utils.unregister_class(SelectCameraTarget)
    bpy.utils.unregister_class(render_Quick_OpenGL)

    # runegister menus
    bpy.utils.unregister_class(VIEW3D_PIE_oenvoyage)

    # UI: Unregister the panels
    bpy.types.RENDER_PT_render.remove(estimate_render_animation_time)
    bpy.types.VIEW3D_MT_object_specials.remove(special_key_options)
    bpy.types.VIEW3D_MT_object_specials.remove(motion_path_buttons)
    
    clear_properties()

if __name__ == "__main__":
    register()