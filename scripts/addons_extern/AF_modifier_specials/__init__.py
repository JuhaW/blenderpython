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
    "name": "AF: Modifier Specials",
    "author": "Meta Androcto, ",
    "version": (0, 2),
    "blender": (2, 75, 0),
    "location": "View3D > Add > Scene Elements",
    "description": "Modifiers Specials Menu",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6"\
        "/Py/Scripts",
    "tracker_url": "",
    "category": "Addon Factory"}


if "bpy" in locals():
    import importlib
    importlib.reload(DATA_PT_modifiers)
    importlib.reload(mirror_tools)

else:
    from . import DATA_PT_modifiers
    from . import mirror_tools

import bpy

# Addons Preferences
class AddonPreferences(bpy.types.AddonPreferences):
	bl_idname = __name__
	
	def draw(self, context):
		layout = self.layout
		layout.label(text="----Modifier Specials----")
		layout.label(text="Prototype/Experimental")
		layout.label(text="Quick access to common Modifier settings")
		layout.label(text="Includes some batch operations for subsurf")
		layout.label(text="Includes Apply/Delete All")
		layout.label(text="Includes View & Expand All")

def register():
	bpy.utils.register_module(__name__)
    # Add "Extras" menu to the "Add Mesh" menu
	bpy.types.DATA_PT_modifiers.prepend(DATA_PT_modifiers.menu)


def unregister():
	bpy.types.DATA_PT_modifiers.remove(DATA_PT_modifiers.menu)


    # Remove "Extras" menu from the "Add Mesh" menu.
	bpy.utils.unregister_module(__name__)
if __name__ == "__main__":
    register()

