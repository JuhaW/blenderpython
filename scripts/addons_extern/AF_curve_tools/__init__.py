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
    "name": "AF: Curve Tools",
    "author": "Multiple Authors",
    "version": (0, 1),
    "blender": (2, 77, 0),
    "location": "View3D > Toolshelf",
    "description": "Add extra curve object types",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/"
                "Scripts/Curve/Curve_Objects",
    "category": "Addon Factory"}

if "bpy" in locals():
    import importlib
    importlib.reload(add_curve_ChangeMultipleOrigin)
    importlib.reload(add_curve_select_tool)
    importlib.reload(bevel_curve)
    importlib.reload(curve_convert0_8)
    importlib.reload(curve_edit_outline)
    importlib.reload(curve_simplify)

else:
    from . import add_curve_ChangeMultipleOrigin
    from . import add_curve_select_tool
    from . import bevel_curve
    from . import curve_convert0_8
    from . import curve_edit_outline
    from . import curve_simplify

import bpy

class CurveExtraToolPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Tools"
    bl_label = "Curve Extra Tools"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout

        obj = context.active_object
        col = self.layout.column()
        if context.mode == 'OBJECT':
            col.label(text="Bevel Curve:")
            col.operator("curve.new_beveled_curve")
            col.label(text="Edit:")
            col.operator("curve.add_bevel_to_curve")
            col.operator("curve.edit_bevel_curve")
            col.operator("curve.hide_bevel_objects")

        if obj and obj.type =='CURVE':
            col.label(text="Bevel Curve Convert:")
            col.operator("curve.convert_beveled_curve_to_meshes")
            col.operator("curve.convert_beveled_curve_to_separated_meshes")
            col.operator("curve.convert_beveled_curve_to_merged_mesh")
            col.operator("curve.convert_beveled_curve_to_union_mesh")
            #c.operator("curve.convert_to_mesh_with_options")
            col.label(text="Edit Outline:")
            col.operator("object.curve_outline")
            col.label(text="Properties:")
            col.prop(obj.data, "resolution_u")
            col.label(text="Simplify:")
            col.operator("curve.simplify")
            col.label(text="Set Multi Origin:")
            col.operator("object.change_multiple_curve_origin")
        if context.mode =='EDIT_CURVE':
            col.operator("curve.finish_edit_bevel")
            col.label(text="Selection:")
            col.operator('curve.select_point', text='Select previous').action = 'PREVIOUS'
            col.operator('curve.select_point', text='Select next').action = 'NEXT'
            col.operator('curve.select_point', text='Select first').action = 'FIRST'
            col.operator('curve.select_point', text='Select last').action = 'LAST'

class CurveToolsPrefs(bpy.types.AddonPreferences):
    bl_idname = __name__

    bpy.types.Scene.Enable_Tab_01 = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.Enable_Tab_02 = bpy.props.BoolProperty(default=False)

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "Enable_Tab_01", text="info", icon="INFO")   
        if context.scene.Enable_Tab_01:
            row = layout.row()
            layout.label(text="----Curve Tools----")
            layout.label(text="Extended Curve Tools")

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
            layout.label(text="Tubes & Pipes: Create Solid Tubes & Pipes(panel)")

def register():
    bpy.utils.register_module(__name__)
    # Add "Extras" menu to the "Add Mesh" menu



def unregister():
    bpy.utils.unregister_module(__name__)
    # Remove "Extras" menu from the "Add Mesh" menu.


if __name__ == "__main__":
    register()