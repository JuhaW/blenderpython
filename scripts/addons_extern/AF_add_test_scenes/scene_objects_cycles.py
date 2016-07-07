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


class add_scene(bpy.types.Operator):
    bl_idname = "objects_cycles.add_scene"
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
        scene.name = "scene_object_cycles"

# render settings
        render = scene.render
        render.resolution_x = 1920
        render.resolution_y = 1080
        render.resolution_percentage = 50

# add new world
        world = bpy.data.worlds.new("Cycles_Object_World")
        scene.world = world
        world.use_sky_blend = True
        world.use_sky_paper = True
        world.horizon_color = (0.004393, 0.02121, 0.050)
        world.zenith_color = (0.03335, 0.227, 0.359)
        world.light_settings.use_ambient_occlusion = True
        world.light_settings.ao_factor = 0.25

# add camera
        bpy.ops.object.camera_add(location=(7.48113, -6.50764, 5.34367), rotation=(1.109319, 0.010817, 0.814928))
        cam = bpy.context.active_object.data
        cam.lens = 35
        cam.draw_size = 0.1
        bpy.ops.view3d.viewnumpad(type='CAMERA')

# add point lamp
        bpy.ops.object.lamp_add(type="POINT", location=(4.07625, 1.00545, 5.90386), rotation=(0.650328, 0.055217, 1.866391))
        lamp1 = bpy.context.active_object.data
        lamp1.name = "Point_Right"
        lamp1.energy = 1.0
        lamp1.distance = 30.0
        lamp1.shadow_method = "RAY_SHADOW"
        lamp1.use_sphere = True

# add point lamp2
        bpy.ops.object.lamp_add(type="POINT", location=(-0.57101, -4.24586, 5.53674), rotation=(1.571, 0, 0.785))
        lamp2 = bpy.context.active_object.data
        lamp2.name = "Point_Left"
        lamp2.energy = 1.0
        lamp2.distance = 30.0


### add cube
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.subdivide(number_cuts=2)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.ops.object.shade_smooth()
        cube = bpy.context.active_object
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
# add cube material
        cubeMaterial = blend_data.materials.new("Cycles_Cube_Material")
        bpy.ops.object.material_slot_add()
        cube.material_slots[0].material = cubeMaterial
# Diffuse
        cubeMaterial.preview_render_type = "CUBE"
        cubeMaterial.diffuse_color = (1.000, 0.373, 0.00)
# Cycles 
        cubeMaterial.use_nodes = True


### add monkey
        bpy.ops.mesh.primitive_monkey_add(location=(-0.32639, 0.08901, 1.49976))
        bpy.ops.transform.rotate(value=(1.15019), axis=(0, 0, 1))
        bpy.ops.transform.rotate(value=(-0.683882), axis=(0, 1, 0))
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.ops.object.shade_smooth()
        monkey = bpy.context.active_object
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
# add monkey material
        monkeyMaterial = blend_data.materials.new("Cycles_Monkey_Material")
        bpy.ops.object.material_slot_add()
        monkey.material_slots[0].material = monkeyMaterial
# Diffuse
        monkeyMaterial.preview_render_type = "MONKEY"
        monkeyMaterial.diffuse_color = (0.239, 0.288, 0.288)
# Cycles
        monkeyMaterial.use_nodes = True


### add plane
        bpy.ops.mesh.primitive_plane_add(radius=50, view_align=False, enter_editmode=False, location=(0, 0, -1))
        bpy.ops.object.editmode_toggle()
        bpy.ops.transform.rotate(value=-0.8, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.ops.object.editmode_toggle()
        plane = bpy.context.active_object
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
# add plane material
        planeMaterial = blend_data.materials.new("Cycles_Plane_Material")
        bpy.ops.object.material_slot_add()
        plane.material_slots[0].material = planeMaterial
# Diffuse
        planeMaterial.preview_render_type = "FLAT"
        planeMaterial.diffuse_color = (0.2, 0.2, 0.2)
# Cycles
        planeMaterial.use_nodes = True


# Back to Scene
        sc = bpy.context.scene

        return {'FINISHED'}

#### REGISTER ####

def register():
    bpy.utils.register_module(__name__)

    bpy.types.INFO_MT_add.append(menu_func)


def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.INFO_MT_add.remove(menu_func)


if __name__ == '__main__':
    register()
