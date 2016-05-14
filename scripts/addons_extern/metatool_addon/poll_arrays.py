# bl_info = {
#    "name": "Extension Add",
#    "author": "marvin.k.breuer",
#    "version": (0, 1, 0),
#    "blender": (2, 72, 0),
#    "location": "View3D > Toolbar",
#    "warning": "",
#    "description": "Toolkit Extension",
#    "wiki_url": "",
#    "category": "User Panel",
#}


import bpy
from bpy import *

# property group containing all properties for the gui in the panel
# Dropdown Arrow ### general display properties = arrow tooltips


class DropdownMetaTool_ARRAY_Props(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.metawindowtool_array
    """
    # Expand
    display_tab_array = bpy.props.BoolProperty(name="Expand", description="Display Tools", default=False)
    display_tab_arraycurve = bpy.props.BoolProperty(name="Expand", description="Display Tools", default=False)
    display_tab_arraycircle = bpy.props.BoolProperty(name="Expand", description="Display Tools", default=False)


###########################################################################################
#########################################################
###-----------------  ARRAYS  ------------------------###
###-----------------  ARRAYS  ------------------------###
#########################################################

# Sub Location
class SubLoc_Array():
    """Array Tools"""
    bl_category = "META"
    #bl_region_type = 'TOOLS'
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(cls, context):
        return context.scene.osc_arrays


# Sub Panel
class META_TAB_Array(SubLoc_Array, bpy.types.Panel):
    """Array Tools"""
    bl_idname = "meta.array"
    bl_label = "[ARRAY]"

    def draw(self, context):
        lt = context.window_manager.metawindowtool_array
        layout = self.layout
        active_obj = context.active_object


# -------------------------------------------------------
# Array Tools  #######-------------------------------------------------------
# Array Tools  #######-------------------------------------------------------
# -------------------------------------------------------

        col = layout.column(align=True)

        if lt.display_tab_array:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_tab_array", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_tab_array", text="", icon='TRIA_RIGHT')

        row.label("ArrayTools...")

        if lt.display_tab_array:

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("object.simplearewo", text="Arewo Offset")
            row.operator("object.cursor_array", text="2 Cursor")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.add_2array", text="2d Grid")
            row.operator("object.add_3array", text="3d Grid")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            mifthTools = bpy.context.scene.mifthTools

            row.operator("mft.clonetoselected", text="CloneToSelected")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("mft.radialclone", text="Radial Clone")

            row = col_top.row(align=True)
            row.prop(mifthTools, "radialClonesAxis", text='')
            row.prop(mifthTools, "radialClonesAxisType", text='')


# Curve  ######--------------------------------------
# Curve  ######--------------------------------------

            if lt.display_tab_arraycurve:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_tab_arraycurve", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_tab_arraycurve", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

            row.label("CurveAray...")

            if lt.display_tab_arraycurve:

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("object.loops12", text="", icon="CURVE_BEZCURVE")
                row.operator("object.loops13", text="Beziér Curve",)

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("object.loops10", text="", icon="CURVE_BEZCIRCLE")
                row.operator("object.loops11", text="Beziér Circle",)


# Empty  ######--------------------------------------
# Empty  ######-------------------------------------

            if lt.display_tab_arraycircle:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_tab_arraycircle", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_tab_arraycircle", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

            row.label("EmptyArray...")

            if lt.display_tab_arraycircle:

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("objects.circle_array_operator1", text="1/4-90°", icon="MOD_ARRAY")
                row.operator("objects.circle_array_operator2", text="1/6-60°", icon="MOD_ARRAY")

                row = col_top.row(align=True)
                row.operator("objects.circle_array_operator3", text="1/8-45°", icon="MOD_ARRAY")
                row.operator("objects.circle_array_operator4", text="1/12-30°", icon="MOD_ARRAY")


############------------############
############  REGISTER  ############
############------------############


def register():
    bpy.utils.register_class(DropdownMetaTool_ARRAY_Props)
    bpy.types.WindowManager.metawindowtool_array = bpy.props.PointerProperty(type=DropdownMetaTool_ARRAY_Props)

    bpy.utils.register_class(META_TAB_Array)


def unregister():
    bpy.utils.unregister_class(META_TAB_Array)


if __name__ == "__main__":
    register()
