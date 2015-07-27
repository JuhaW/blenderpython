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
    "category": "Add Curve"}

if "bpy" in locals():
    import importlib
    importlib.reload(sapling)
#    importlib.reload(utils)
    importlib.reload(add_curve_aceous_galore)
    importlib.reload(add_curve_spirals)
    importlib.reload(add_curve_torus_knots)
    importlib.reload(add_curve_braid)
    importlib.reload(add_curve_curly)
    importlib.reload(add_curve_celtic_links)
    importlib.reload(add_curve_formulacurves)
    importlib.reload(add_curve_wires)
    importlib.reload(add_curve_ivygen)
    importlib.reload(curve_simplify)


else:
    from . import sapling
#    from . import utils
    from . import add_curve_aceous_galore
    from . import add_curve_spirals
    from . import add_curve_torus_knots
    from . import add_curve_braid
    from . import add_curve_curly
    from . import add_curve_celtic_links
    from . import add_curve_formulacurves
    from . import add_curve_wires
    from . import add_curve_ivygen
    from . import curve_simplify


import bpy

class INFO_MT_curve_plants_add(bpy.types.Menu):
    # Define the "Extras" menu
    bl_idname = "curve_plants_add"
    bl_label = "Plants"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator("curve.tree_add",
            text="Sapling 3")
        self.layout.operator("curve.ivy_gen", text="Add Ivy to Mesh").updateIvy = True

class INFO_MT_curve_knots_add(bpy.types.Menu):
    # Define the "Extras" menu
    bl_idname = "curve_knots_add"
    bl_label = "Plants"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator("curve.torus_knot_plus",
            text="Torus Knot Plus")
        layout.operator("curve.celtic_links",
            text="Celtic Links")
        layout.operator("mesh.add_braid",
            text="Braid Knot")

class INFO_MT_curve_extras_add(bpy.types.Menu):
    # Define the "Extras" menu
    bl_idname = "curve_extra_objects_add"
    bl_label = "Extra Objects"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator("mesh.curveaceous_galore",
            text="Curves Galore!")
        layout.operator("curve.spirals",
            text="Spirals")
        layout.operator("curve.curlycurve",
            text="Curly Curve")
        layout.operator("curve.formulacurves",
            text="Formula Curve")
        layout.operator("curve.wires",
            text="Curve Wires")
        layout.separator()
        layout.label(text="Curve Utils")
        layout.operator("curve.simplify",
            text="Simplify Curves")

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
		layout.label(text="Curve Factory")
		self.layout.menu("curve_plants_add", text="Plants", icon="CURVE_DATA")
		self.layout.menu("curve_knots_add", text="Knots", icon='CURVE_DATA')
		self.layout.operator("mesh.curveaceous_galore", text="Curves Galore!", icon="CURVE_DATA")
		self.layout.operator("curve.spirals", text="Spirals", icon="CURVE_DATA")
		self.layout.operator("curve.curlycurve", text="Curly Curve", icon="CURVE_DATA")
		self.layout.operator("curve.formulacurves", text="Formula Curve", icon="CURVE_DATA")
		self.layout.operator("curve.wires", text="Curve Wires", icon="CURVE_DATA")
		self.layout.separator()
		layout.label(text="Curve Utils")
		self.layout.operator("curve.simplify", text="Curve Simplify", icon="CURVE_DATA")

	if (context.user_preferences.addons["Addon_Factory"].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', text = 'Toggle Curve Factory', icon='VISIBLE_IPO_ON').id = __name__.split('.')[-1]

