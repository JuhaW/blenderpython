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
# by meta-androcto, parts based on work by Saidenka #

bl_info = {
    "name": "AF: Properties Panels",
    "author": "Meta Androcto, ",
    "version": (0, 2),
    "blender": (2, 75, 0),
    "location": "View3D > Properties Panels",
    "description": "Properties Panels Extended",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6"\
        "/Py/Scripts",
    "tracker_url": "",
    "category": "Addon Factory"}

if "bpy" in locals():
    import importlib
    importlib.reload(VIEW3D_PT_view3d_cursor)
    importlib.reload(VIEW3D_PT_view3d_name)
    importlib.reload(VIEW3D_PT_view3d_properties)
    importlib.reload(VIEW3D_PT_view3d_shading)
    importlib.reload(OBJECT_PT_context_object)
    importlib.reload(quick_prefs)
    importlib.reload(easy_lightmap)

else:
    from . import VIEW3D_PT_view3d_cursor
    from . import VIEW3D_PT_view3d_name
    from . import VIEW3D_PT_view3d_properties
    from . import VIEW3D_PT_view3d_shading
    from . import OBJECT_PT_context_object
    from . import quick_prefs
    from . import easy_lightmap

import bpy
from bpy.props import StringProperty, BoolProperty, IntProperty
from subprocess import Popen, PIPE
##############
## REGISTER ##
##############
class EasyLightMapProperties(bpy.types.PropertyGroup):
    
    bake_path = StringProperty(name="Bake folder:", default="", subtype="DIR_PATH", description="Path for saving baked maps.")
    image_w = IntProperty(name="Width", default=1024, min=1, description="Image width")
    image_h = IntProperty(name="Height", default=1024, min=1, description="Image height")
    check_uv = BoolProperty(name="Check/Create UV Layers", default=True, description="Create two uv layers if there is not any.")
    bake_diffuse = BoolProperty(name="Bake diffuse color", default=False, description="Bake material diffuse color into map.")
    bake_textures = BoolProperty(name="Bake textures", default=False, description="Bake material textures into map.")


# Addons Preferences
class AddonPreferences(bpy.types.AddonPreferences):
	bl_idname = __name__

	view_savedata = bpy.props.StringProperty(name="View Saved Data", default="")
	
	def draw(self, context):
		layout = self.layout
		layout.label(text="Save your Views to addons preferences")
		layout.label(text="Per Session ues only")
		layout.label(text="Save User Settings to store permenantly")
		layout.prop(self, 'view_savedata')
		box = layout.box()
		box.label(text = 'Preferences')
	
		layout.label(text="----Properties Panels----")
		layout.label(text="Adds additional features & concepts")
		layout.label(text="Quick Prefs, Easy Light Map, Shading & more")


def register():
    """ Register """
    bpy.utils.register_class(EasyLightMapProperties)
    bpy.types.Scene.easyLightMap = bpy.props.PointerProperty(type=EasyLightMapProperties)
    windowManager = bpy.types.WindowManager
    # Add "Extras" menu to the "Properties" menu
    bpy.types.VIEW3D_PT_view3d_cursor.append(VIEW3D_PT_view3d_cursor.menu)
    bpy.types.VIEW3D_PT_view3d_name.prepend(VIEW3D_PT_view3d_name.menu)
    bpy.types.VIEW3D_PT_view3d_properties.append(VIEW3D_PT_view3d_properties.menu)
    bpy.types.VIEW3D_PT_view3d_shading.append(VIEW3D_PT_view3d_shading.menu)

    bpy.utils.register_module(__name__)
def unregister():

    bpy.types.VIEW3D_PT_view3d_cursor.remove(VIEW3D_PT_view3d_cursor.menu)
    bpy.types.VIEW3D_PT_view3d_name.remove(VIEW3D_PT_view3d_name.menu)
    bpy.types.VIEW3D_PT_view3d_properties.remove(VIEW3D_PT_view3d_properties.menu)
    bpy.types.VIEW3D_PT_view3d_shading.remove(VIEW3D_PT_view3d_shading.menu)

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()

