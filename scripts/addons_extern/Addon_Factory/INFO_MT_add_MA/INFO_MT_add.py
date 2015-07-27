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
# by meta-androcto, parts based on work by Erich Toven #

bl_info = {
    "name": "Scene Elements",
    "author": "Meta Androcto, ",
    "version": (0, 2),
    "blender": (2, 75, 0),
    "location": "View3D > Add > Scene Elements",
    "description": "Add Scenes & Lights, Objects.",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6"\
        "/Py/Scripts",
    "tracker_url": "http://projects.blender.org/tracker/index.php?"\
        "func=detail&aid=32682",
    "category": "Object"}


if "bpy" in locals():
    import importlib
    importlib.reload(scene_camera)
    importlib.reload(scene_lighting)
    importlib.reload(scene_materials)
    importlib.reload(scene_objects)
    importlib.reload(scene_objects_cycles)
    importlib.reload(pixelate_3d)
    importlib.reload(object_add_chain)
    importlib.reload(drop_to_ground)
    importlib.reload(circle_array)
    importlib.reload(crear_cuerda)
    importlib.reload(dupli_spin)
    importlib.reload(aggregate_mesh)

else:
    from . import scene_camera
    from . import scene_lighting
    from . import scene_materials
    from . import scene_objects
    from . import scene_objects_cycles
    from . import pixelate_3d
    from . import object_add_chain
    from . import oscurart_chain_maker
    from . import drop_to_ground
    from . import circle_array
    from . import crear_cuerda
    from . import dupli_spin
    from . import aggregate_mesh

import bpy

class create_menu(bpy.types.Panel):
    bl_label = 'Add Factory'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Create"
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        layout.operator('mesh.primitive_chain_add', icon='LINKED')
        layout.operator('mesh.primitive_oscurart_chain_add', icon='LINKED')
        layout.operator('object.pixelate', icon='MESH_GRID')
        layout.operator("object.drop_on_active",
            text="Drop To Ground", icon='MESH_PLANE')
        layout.operator("objects.circle_array_operator",
            text="Circle Array", icon='MOD_ARRAY')
        layout.operator("object.procedural_dupli_spin",
            text="Dupli Splin", icon='MOD_ARRAY')

class INFO_MT_mesh_chain_add(bpy.types.Menu):
    # Define the "mesh objects" menu
    bl_idname = "INFO_MT_mesh_chain"
    bl_label = "Chains"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator('mesh.primitive_chain_add', icon='LINKED')
        layout.operator('mesh.primitive_oscurart_chain_add', icon='LINKED')


class INFO_MT_array_mods_add(bpy.types.Menu):
    # Define the "mesh objects" menu
    bl_idname = "INFO_MT_array_mods"
    bl_label = "Array Mods"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        self.layout.menu("INFO_MT_mesh_chain", icon="LINKED")
        layout.operator("objects.circle_array_operator",
            text="Circle Array", icon='MOD_ARRAY')
        layout.operator("object.procedural_dupli_spin",
            text="Dupli Spin", icon='MOD_ARRAY')
        layout.operator("object.agregar",
            text="Aggregate Mesh", icon='MOD_ARRAY')

class INFO_MT_quick_tools_add(bpy.types.Menu):
    # Define the "mesh objects" menu
    bl_idname = "INFO_MT_quick_tools"
    bl_label = "Quick Tools"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator("object.drop_on_active",
            text="Drop To Ground")
        layout.operator('object.pixelate', icon='MESH_GRID')
        layout.operator("ball.rope",
            text="Wrecking Ball", icon='PHYSICS')


class INFO_MT_scene_elements_add(bpy.types.Menu):
    # Define the "mesh objects" menu
    bl_idname = "INFO_MT_scene_elements"
    bl_label = "Test scenes"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator("camera.add_scene",
            text="Scene_Camera")
        layout.operator("materials.add_scene",
            text="Scene_Objects_BI")
        layout.operator("plane.add_scene",
            text="Scene_Plane")
        layout.operator("objects_cycles.add_scene",
            text="Scene_Objects_Cycles")

class INFO_MT_mesh_lamps_add(bpy.types.Menu):
    # Define the "mesh objects" menu
    bl_idname = "INFO_MT_scene_lamps"
    bl_label = "Lighting Sets"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator("object.add_single_spot",
            text="Add Single Spot")
        layout.operator("object.add_basic_3point",
            text="Add 3 Point Spot Setup")
        layout.operator("object.add_basic_2point",
            text="Add 2 Point Setup")
        layout.operator("object.add_area_3point",
            text="Add 3 Point Setup")

def IsMenuEnable(self_id):
	for id in bpy.context.user_preferences.addons["Addon_Factory"].preferences.disabled_menu.split(','):
		if (id == self_id):
			return False
	else:
		return True
# Define "Extras" menu
def menu(self, context):
	if (IsMenuEnable(__name__.split('.')[-1])):
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'
		self.layout.separator()
		layout.label(text="Add Factory")
		self.layout.menu("INFO_MT_scene_elements", icon="SCENE_DATA")
		self.layout.menu("INFO_MT_scene_lamps", icon="LAMP_SPOT")
		self.layout.menu("INFO_MT_array_mods", icon="MOD_ARRAY")
		self.layout.menu("INFO_MT_quick_tools", icon="MOD_BUILD")
	if (context.user_preferences.addons["Addon_Factory"].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', text= "Toggle Add Factory", icon='VISIBLE_IPO_ON').id = __name__.split('.')[-1]

def register():
    bpy.utils.register_module(__name__)
    # Add "Extras" menu to the "Add Mesh" menu
    bpy.types.INFO_MT_add.append(menu_func)

def unregister():
    bpy.utils.unregister_module(__name__)
    # Remove "Extras" menu from the "Add Mesh" menu.
    bpy.types.INFO_MT_add.remove(menu_func)

if __name__ == "__main__":
    register()
