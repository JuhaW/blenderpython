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

from .align_tools import VIEW3D_MT_align_tools

if "bpy" in locals():
    import importlib
    importlib.reload(analyse_dicom_3d_models)
    importlib.reload(display_tools)
    importlib.reload(curve_convert0_7)
    importlib.reload(bevel_curve)
    importlib.reload(Auto_Mirror)

else:
    from . import analyse_dicom_3d_models
    from . import display_tools
    from . import curve_convert0_7
    from . import bevel_curve
    from . import Auto_Mirror


bl_info = {
    "name": "Toolshelf Panels",
    "author": "Meta Androcto, ",
    "version": (0, 2),
    "blender": (2, 75, 0),
    "location": "View3D > Toolshelf",
    "description": "Add extra menus to Toolshelf.",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6"\
        "/Py/Scripts",
    "tracker_url": "",
    "category": "Addon Factory"}

import bpy

# Addons Preferences
class AddonPreferences1(bpy.types.AddonPreferences):
	bl_idname = __name__
	
	def draw(self, context):
		layout = self.layout
		layout.label(text="Tools Shelf Panels")
		layout.label(text="----Tools Tab---")
		layout.label(text="Align & Advanced Align")
		layout.label(text="Selection Tools")
		layout.label(text="Modify Tools: Trim, Intersect, Bisect")
		layout.label(text="Transform Extended")
		layout.label(text="Display Tools: Set up Object display")
		layout.label(text="Curve Converter: Curve to Mesh re-editing")
		layout.label(text="Bevel Curve Tool")

def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
