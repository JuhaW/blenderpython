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
# Contributed to by
# testscreenings, Alejandro Omar Chocano Vasquez, Jimmy Hazevoet, Adam Newgas, meta-androcto #


bl_info = {
    "name": "Objects",
    "author": "Multiple Authors",
    "version": (0, 1),
    "blender": (2, 74, 0),
    "location": "View3D > Add > Curve",
    "description": "Add extra curve object types",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/"
                "Scripts/Curve/Curve_Objects",
    "category": "Add Surface"}

from . import add_surface_plane_cone


import bpy

def IsMenuEnable(self_id):
	for id in bpy.context.user_preferences.addons["Addon_Factory"].preferences.disabled_menu.split(','):
		if (id == self_id):
			return False
	else:
		return True
# Register all operators and panels

# Define "Extras" menu
def menu(self, context):
	if (IsMenuEnable(__name__.split('.')[-1])):
		layout = self.layout
		col = layout.column()
		self.layout.separator()
		layout.label(text="Surface Factory")
		self.layout.operator("object.add_surface_wedge", text="Wedge", icon="MOD_CURVE")
		self.layout.operator("object.add_surface_cone", text="Cone", icon="MOD_CURVE")
		self.layout.operator("object.add_surface_star", text="Star", icon="MOD_CURVE")
		self.layout.operator("object.add_surface_plane", text="Plane", icon="MOD_CURVE")
		self.layout.operator("curve.smooth_x_times", text="Special Smooth", icon="MOD_CURVE")




	if (context.user_preferences.addons["Addon_Factory"].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', text = 'Toggle Surface Factory', icon='VISIBLE_IPO_ON').id = __name__.split('.')[-1]

