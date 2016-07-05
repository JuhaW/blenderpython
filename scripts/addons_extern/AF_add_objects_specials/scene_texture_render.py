'''
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
    "name": "Scene Lighting Presets",
    "author": "meta-androcto",
    "version": (0,1),
    "blender": (2, 63, 0),
    "location": "View3D > Tool Shelf > Scene Lighting Presets",
    "description": "Creates Scenes with Lighting presets",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.5/Py/Scripts/",
    "tracker_url": "",
    "category": "Object"}
'''
import bpy
import mathutils
import math
from math import pi
from bpy.props import *
from mathutils import Vector

class TopViewpoint1(bpy.types.Operator):
    bl_idname = 'opr.top_viewpoint1'
    bl_label = 'Top Viewpoint'
    bl_description = 'View from the Top'

    def execute(self, context):
        bpy.ops.view3d.viewnumpad(type='TOP')
        return {'FINISHED'}

class add_scene(bpy.types.Operator):
    bl_idname = "objects_texture.add_scene"
    bl_label = "Create test scene"
    bl_description = "Cycles Scene with Objects"
    bl_register = True
    bl_undo = True

    def execute(self, context):
        blend_data = context.blend_data
        ob = bpy.context.active_object

# add new scene

        bpy.ops.scene.new(type="NEW")
        scene = bpy.context.scene
        bpy.context.scene.render.engine = 'CYCLES'
        scene.name = "scene_texture_cycles"
# render settings
        render = scene.render
        render.resolution_x = 1080
        render.resolution_y = 1080
        render.resolution_percentage = 100
# add new world
        world = bpy.data.worlds.new("Cycles_Textures_World")
        scene.world = world
        world.use_sky_blend = True
        world.use_sky_paper = True
        world.horizon_color = (0.004393, 0.02121, 0.050)
        world.zenith_color = (0.03335, 0.227, 0.359)
        world.light_settings.use_ambient_occlusion = True
        world.light_settings.ao_factor = 0.5
# add camera
        bpy.ops.view3d.viewnumpad(type='TOP')
        bpy.ops.object.camera_add(location=(0, 0, 2.19), rotation=(0, 0, 0), view_align = True)
        cam = bpy.context.active_object.data
        cam.lens = 35
        cam.draw_size = 0.1



# add plane

        bpy.ops.mesh.primitive_plane_add(enter_editmode=True, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.ops.mesh.subdivide(number_cuts=10, smoothness=0)
        bpy.ops.uv.unwrap(method='CONFORMAL', margin=0.001)
        bpy.ops.object.editmode_toggle()

        plane = bpy.context.active_object
# add new material
        planeMaterial = blend_data.materials.new("Cycles_Plane_Material")
        bpy.ops.object.material_slot_add()
        plane.material_slots[0].material = planeMaterial


# Material settings
        planeMaterial.use_nodes = True

        planeMaterial.diffuse_color = (0.2, 0.2, 0.2)
        planeMaterial.specular_color = (0.604, 0.465, 0.136)
        planeMaterial.specular_intensity = 0.3
        planeMaterial.ambient = 0
        planeMaterial.use_cubic = True
        planeMaterial.use_transparency = False
        planeMaterial.alpha = 0
        planeMaterial.use_transparent_shadows = True
        sc = bpy.context.scene
        bpy.ops.view3d.viewnumpad(type='CAMERA')
        return {'FINISHED'}


def register():
    bpy.utils.register_module(__name__)

    bpy.types.INFO_MT_add.append(menu_func)


def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.INFO_MT_add.remove(menu_func)


if __name__ == '__main__':
    register()
