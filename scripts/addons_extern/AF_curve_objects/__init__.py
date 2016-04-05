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
from .object_tube_and_pipe import __init__
from .object_tube_and_pipe import Makemesh
from .object_tube_and_pipe import Pipe
from .object_tube_and_pipe import Tube

bl_info = {
    "name": "AF: Curve Objects",
    "author": "Multiple Authors",
    "version": (0, 1),
    "blender": (2, 74, 0),
    "location": "View3D > Add > Curve",
    "description": "Add extra curve object types",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/"
                "Scripts/Curve/Curve_Objects",
    "category": "Addon Factory"}

if "bpy" in locals():
    import importlib
    importlib.reload(sapling)
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
    importlib.reload(add_surface_plane_cone)
    importlib.reload(curve_edit_outline)
    importlib.reload(DialScale)
    importlib.reload(add_iterative_tree)
    importlib.reload(curve_convert0_7)
    importlib.reload(bevel_curve)


else:
    from . import sapling
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
    from . import add_surface_plane_cone
    from . import curve_edit_outline
    from . import DialScale
    from . import add_iterative_tree
    from . import curve_convert0_7
    from . import bevel_curve

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
        layout.operator("object.curve_outline",
            text="Outline")
        layout.operator("curve.dial_scale",
            text="Dial/Scale")



# Define "Extras" menu
def menu(self, context):

	layout = self.layout
	col = layout.column()
	self.layout.separator()
	layout.label(text="AF: Curve Objects", icon="OUTLINER_OB_CURVE")
	self.layout.menu("curve_plants_add", text="Plants", icon="CURVE_DATA")
	self.layout.menu("curve_knots_add", text="Knots", icon='CURVE_DATA')
	self.layout.operator("mesh.curveaceous_galore", text="Curves Galore!", icon="CURVE_DATA")
	self.layout.operator("curve.spirals", text="Spirals", icon="CURVE_DATA")
	self.layout.operator("curve.curlycurve", text="Curly Curve", icon="CURVE_DATA")
	self.layout.operator("curve.formulacurves", text="Formula Curve", icon="CURVE_DATA")
	self.layout.operator("curve.wires", text="Curve Wires", icon="CURVE_DATA")
	self.layout.operator("curve.dial_scale", text="Dial/Scale", icon="CURVE_DATA")
	self.layout.separator()
	layout.label(text="Curve Utils")
	self.layout.operator("curve.simplify", text="Curve Simplify", icon="CURVE_DATA")
	self.layout.operator("object.curve_outline", text="Curve Outline", icon="CURVE_DATA")

def menu_surface(self, context):

	layout = self.layout
	col = layout.column()
	self.layout.separator()
	layout.label(text="Surface Factory")
	self.layout.operator("object.add_surface_wedge", text="Wedge", icon="MOD_CURVE")
	self.layout.operator("object.add_surface_cone", text="Cone", icon="MOD_CURVE")
	self.layout.operator("object.add_surface_star", text="Star", icon="MOD_CURVE")
	self.layout.operator("object.add_surface_plane", text="Plane", icon="MOD_CURVE")
	self.layout.operator("curve.smooth_x_times", text="Special Smooth", icon="MOD_CURVE")

class CurveObjectPrefs(bpy.types.AddonPreferences):
    bl_idname = __name__

    bpy.types.Scene.Enable_Tab_01 = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.Enable_Tab_02 = bpy.props.BoolProperty(default=False)

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "Enable_Tab_01", text="info", icon="INFO")   
        if context.scene.Enable_Tab_01:
            row = layout.row()
            layout.label(text="----Add Curve Objects----")
            layout.label(text="Merges most Curve Object Addons into One")
            layout.label(text="Includes Add Surface Shapes")

        layout.prop(context.scene, "Enable_Tab_02", text="Curve Objects", icon="INFO")  
        if context.scene.Enable_Tab_02:
            row = layout.row()
            layout.label(text="Add Plants: Sapling & Ivy Gen, Add Iterative Tree(panel)")
            layout.label(text="Add Knots: Celtic, TorusKnot+ & Braid")
            layout.label(text="Curves_Galore: 2d curve shapes")
            layout.label(text="Spirals: Create Spiral curve type")
            layout.label(text="Curly Curve: Florishes & Curls")
            layout.label(text="Formular Curve: Math based curve")
            layout.label(text="Curve Wires: String a wire between 2 objects")
            layout.label(text="Dial Scale: Clock Face or Scale")
            layout.label(text="Curve Simplify: Simplify Curves")
            layout.label(text="Curve Outline: Create duplicate curve outline")
            layout.label(text="Tubes & Pipes: Create Solid Tubes & Pipes(panel)")
            layout.label(text="Curve Converter: Curve to Mesh re-editing(panel)")
            layout.label(text="Bevel Curve Tool(panel)")

def register():
    bpy.utils.register_module(__name__)
    # Add "Extras" menu to the "Add Mesh" menu
    bpy.types.INFO_MT_curve_add.append(menu)
    bpy.types.INFO_MT_surface_add.append(menu_surface)
    bpy.types.GRAPH_MT_channel.append(curve_simplify.menu_func)
    bpy.types.DOPESHEET_MT_channel.append(curve_simplify.menu_func)


def unregister():
    bpy.utils.unregister_module(__name__)
    # Remove "Extras" menu from the "Add Mesh" menu.
    bpy.types.INFO_MT_curve_add.remove(menu)
    bpy.types.INFO_MT_surface_add.remove(menu_surface)
    bpy.types.GRAPH_MT_channel.remove(curve_simplify.menu_func)
    bpy.types.DOPESHEET_MT_channel.remove(curve_simplify.menu_func)

if __name__ == "__main__":
    register()