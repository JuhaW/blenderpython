# bl_info = {
#    "name": "Spacebar Curve & Surface",
#    "author": "Multiple Authors, mkbreuer",
#    "version": (0, 1, 0),
#    "blender": (2, 7, 2),
#    "location": "View3D",
#    "description": "",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "User Menu"}


import bpy
from bpy import *


#############################################################################################################################################################
#############################################################################################################################################################
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ###
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ###
#############################################################################################################################################################
#############################################################################################################################################################

class CurveSubdivide(bpy.types.Menu):
    bl_label = "Curve Subdivide"
    bl_idname = "space_curvesubdivide"

    def draw(self, context):
        layout = self.layout

        layout.operator("curve.subdivide", text="1 Cut").number_cuts = 1
        layout.operator("curve.subdivide", text="2 Cuts").number_cuts = 2
        layout.operator("curve.subdivide", text="3 Cuts").number_cuts = 3
        layout.operator("curve.subdivide", text="4 Cuts").number_cuts = 4
        layout.operator("curve.subdivide", text="5 Cuts").number_cuts = 5
        layout.operator("curve.subdivide", text="6 Cuts").number_cuts = 6

bpy.utils.register_class(CurveSubdivide)


class CurveTools(bpy.types.Menu):
    bl_label = "Curve Tools"
    bl_idname = "space_curvetools"

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'INVOKE_REGION_WIN'
        scene = context.scene
        toolsettings = context.tool_settings

        edit_object = context.edit_object

        if edit_object.type == 'CURVE':

            layout.operator("transform.tilt", icon="FILE_REFRESH")
            layout.operator("curve.tilt_clear")

        layout.separator()

        layout.operator_menu_enum("curve.handle_type_set", "type", icon="IPO_BEZIER")
        layout.operator("curve.normals_make_consistent")

        layout.separator()

        layout.operator("curve.switch_direction", icon="ARROW_LEFTRIGHT")

        layout.operator("curve.spline_weight_set")

        edit_object = context.edit_object
        if edit_object.type == 'CURVE':

            layout.operator("curve.radius_set")

        layout.separator()

        layout.operator("curve.cyclic_toggle")


bpy.utils.register_class(CurveTools)

#############################################################################################################################################################
#############################################################################################################################################################
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
#############################################################################################################################################################
#############################################################################################################################################################

# Curve & Surface Menu  ######-------------------------------------------------------
# Curve & Surface Menu  ######-------------------------------------------------------


class VIEW3D_Space_CurveSurface(bpy.types.Menu):
    bl_label = "Curve & Surface"
    bl_idname = "space_curvesurface"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_CURVE' or 'EDIT_SURFACE'))

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'INVOKE_REGION_WIN'
        scene = context.scene
        toolsettings = context.tool_settings

        # Setting Menu
        layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")

        layout.separator()

        # Select Menu
        layout.menu("space_selection", icon='RESTRICT_SELECT_OFF')
        layout.menu("space_special", "Smooth Curve")

        layout.separator()

        layout.operator("curve.duplicate_move", "Duplicate")
        layout.operator("curve.extrude_move", "Extrude & Move")

        layout.separator()

        # layout.operator("curve.subdivide")

        layout.menu("space_curvesubdivide", icon="IPO_QUINT")

        layout.separator()

        layout.operator("curve.split")

        edit_object = context.edit_object
        if edit_object.type == 'CURVE':

            layout.operator("object._curve_outline", text="Outline")

        layout.operator("curve.separate")
        layout.operator("curve.make_segment")

        layout.separator()

        layout.menu("space_curvetools")

        layout.separator()

        layout.menu("VIEW3D_MT_hook")

        layout.separator()

        layout.menu("VIEW3D_MT_edit_curve_showhide", icon="VISIBLE_IPO_ON")


###########################################################################################################################################################
###########################################################################################################################################################
# Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register
# Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register
###########################################################################################################################################################
###########################################################################################################################################################


def register():

    bpy.utils.register_class(VIEW3D_Space_CurveSurface)

    # bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_class(VIEW3D_Space_CurveSurface)

    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_Space_CurveSurface.bl_idname)
