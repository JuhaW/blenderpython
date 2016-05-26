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


class DropdownMetaTool_Mat_Props(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.metawindowtool_mat
    """
    # TAB Material
    display_tab_material = bpy.props.BoolProperty(name="Material Tools", description="Display Material Tools", default=False)
    display_tab_matoption = bpy.props.BoolProperty(name="Material Option", description="Display Material Option", default=False)
    display_tab_matclean = bpy.props.BoolProperty(name="Clean Material", description="Display Clean Material Tools", default=False)
    display_tab_matwireset = bpy.props.BoolProperty(name="Wireset", description="Display Wireset Tools", default=False)
    display_tab_matrandom = bpy.props.BoolProperty(name="Random Face", description="Display Random Face Tools", default=False)
    display_tab_node = bpy.props.BoolProperty(name="Random Face", description="Display Random Face Tools", default=False)


###########################################################
###----------------  MATERIAL  -------------------------###
###----------------  MATERIAL  -------------------------###
###########################################################

# Sub Location
class SubLoc_MATERIAL():
    """Material Tools"""
    bl_category = "META"
    #bl_region_type = 'TOOLS'
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(cls, context):
        return context.scene.osc_material

# Sub Panel


class META_TAB_MATERIAL(SubLoc_MATERIAL, bpy.types.Panel):
    """Material Tools"""
    bl_idname = "meta.materialtools"
    bl_label = "[MATERIAL]"
    #bl_context = "mesh_edit"

    def draw(self, context):
        lt = context.window_manager.metawindowtool_mat
        wm = context.window_manager
        scn = context.scene
        layout = self.layout


# -------------------------------------------------------
# Material Tools  #######-------------------------------------------------------
# Material Tools  #######-------------------------------------------------------
# -------------------------------------------------------

        col = layout.column(align=True)

        if lt.display_tab_material:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_tab_material", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_tab_material", text="", icon='TRIA_RIGHT')

        row.label("MatTools...")

        if lt.display_tab_material:
            col = layout.column(align=True)
            wm = bpy.context.window_manager
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            layout.operator_context = 'INVOKE_REGION_WIN'

            row = col_top.row(align=True)
            row.template_ID(context.object, "active_material", new="material.new")
            #row.operator("view3d.assign_material", text="New", icon='ZOOMIN')
            #row.operator("object.material_slot_remove", text="Delete", icon="ZOOMOUT")

            row = col_top.row(align=True)
            row.menu("VIEW3D_MT_assign_material", text="Assign Material", icon='ZOOMIN')
            row = col_top.row(align=True)
            row.menu("VIEW3D_MT_select_material", text="Select by Material", icon='HAND')

            obj = context.object
            row = col_top.row(align=True)
            row.operator("meta.newmaterial", text="ObjColor", icon='ZOOMIN')
            row.prop(obj, "color", text="")


# Material Option  ######-------------------------------------------------
# Material Option  ######-------------------------------------------------

            split = col.split()  # percentage=0.15)

            if lt.display_tab_matoption:
                split.prop(lt, "display_tab_matoption", text="Mat Options", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                split.prop(lt, "display_tab_matoption", text="Mat Options", icon='DISCLOSURE_TRI_RIGHT_VEC')

            #split.operator("view3d.replace_material", text='Replace Material', icon='ARROW_LEFTRIGHT')

            if lt.display_tab_matoption:
                wm = bpy.context.window_manager
                box = col.column(align=True).box().column()

                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("view3d.material_to_texface", text="Material to Texface", icon='MATERIAL_DATA')

                row = col_top.row(align=True)
                row.operator("view3d.texface_to_material", text="Texface to Material", icon='MATERIAL_DATA')

                row = col_top.row(align=True)
                row.operator("view3d.fake_user_set", text='Set Fake User', icon='UNPINNED')

                row = col_top.row(align=True)
                row.operator("object.materials_to_data", text="Data", icon="MATERIAL_DATA")
                row.operator("object.materials_to_object", text="Object", icon="MATERIAL_DATA")


# Clean Material  ######-------------------------------------------------
# Clean Material  ######-------------------------------------------------

            split = col.split()  # percentage=0.15)

            if lt.display_tab_matclean:
                split.prop(lt, "display_tab_matclean", text="Remove Mat", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                split.prop(lt, "display_tab_matclean", text="Remove Mat", icon='DISCLOSURE_TRI_RIGHT_VEC')

            #split.operator("view3d.replace_material", text='Replace Material', icon='ARROW_LEFTRIGHT')

            if lt.display_tab_matclean:

                box = col.column(align=True).box().column()

                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("object.clean_images")

                row = col_top.row(align=True)
                row.operator("object.clean_materials")

                #row = col_top.row(align=True)
                #row.operator("view3d.clean_material_slots", text="Clean Material Slots", icon='CANCEL')

                row = col_top.row(align=True)
                row.operator("view3d.material_remove", text="Remove until 1 Slots", icon='CANCEL')

                row = col_top.row(align=True)
                row.operator("material.remove", text="Remove all Slot Mat", icon='CANCEL')


# Node Materials  ######-------------------------------------------------
# Node Materials  ######-------------------------------------------------

            split = col.split()  # percentage=0.15)

            if lt.display_tab_node:
                split.prop(lt, "display_tab_node", text="Node Presets", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                split.prop(lt, "display_tab_node", text="Node Presets", icon='DISCLOSURE_TRI_RIGHT_VEC')

            #spread_op = split.operator("assign_method", text="")

            if lt.display_tab_node:
                wm = bpy.context.window_manager
                box = col.column(align=True).box().column()

                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("materials.rgbcmyw", text="RGB / CMYK", icon='ZOOMIN')

                row = col_top.row(align=True)
                row.operator("node.idgenerator", text="Add ID Color Node", icon='ZOOMIN')

                row = col_top.row(align=True)
                row.operator("mat.cellook", text="Cellook Material", icon='ZOOMIN')


# Random Face Materials  ######-------------------------------------------------
# Random Face Materials  ######-------------------------------------------------

            split = col.split()  # percentage=0.15)

            if lt.display_tab_matrandom:
                split.prop(lt, "display_tab_matrandom", text="Random Face", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                split.prop(lt, "display_tab_matrandom", text="Random Face", icon='DISCLOSURE_TRI_RIGHT_VEC')

            #spread_op = split.operator("assign_method", text="")

            if lt.display_tab_matrandom:
                wm = bpy.context.window_manager
                box = col.column(align=True).box().column()

                col_top = box.column(align=True)

                row = col_top.row(align=True)

                props = context.scene.face_assigner  # Create reference material assigner property group

                row = col_top.row(align=True)
                row.label(text="skip to apply")

                row = col_top.row(align=True)
                row.prop(props, "rand_seed")  # Create randomization seed property on column

                row = col_top.row(align=True)
                row.label(text="material prefix:")

                row = col_top.row(align=True)
                row.prop(props, "mat_prefix", text="")  # Material prefix property too

                row = col_top.row(align=True)
                row.label(text="assignment method:")

                row = col_top.row(align=True)
                row.prop(props, "assign_method", text="")  # Material assignment method prop


# Setup Wire Render  ######-------------------------------------------------
# Setup Wire Render  ######-------------------------------------------------

            split = col.split()  # percentage=0.15)

            if lt.display_tab_matwireset:
                split.prop(lt, "display_tab_matwireset", text="Mat Wire Render", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                split.prop(lt, "display_tab_matwireset", text="Mat Wire Render", icon='DISCLOSURE_TRI_RIGHT_VEC')

            #split.operator("scene.wire_render", text="Setup Wire Render")

            if lt.display_tab_matwireset:
                wm = bpy.context.window_manager
                box = col.column(align=True).box().column()

                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("scene.wire_render", text="Apply Color Setup", icon="EYEDROPPER")

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.prop(wm, 'col_clay')
                row.prop(wm, 'col_wire')

                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.prop(wm, 'selected_meshes')

                row = col_top.row(align=True)
                row.prop(wm, 'shadeless_mat')

                row = col_top.row(align=True)
                row.prop(wm, 'wire_view')

                row = col_top.row(align=True)
                row.prop(wm, 'wire_object')

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("render.render", text="Render Still", icon='RENDER_STILL')


############------------############
############  REGISTER  ############
############------------############


def register():
    # bpy.utils.register_class(META_TAB_MATERIAL)
    bpy.utils.register_class(DropdownMetaTool_Mat_Props)

    bpy.types.WindowManager.metawindowtool_mat = bpy.props.PointerProperty(type=DropdownMetaTool_Mat_Props)

    bpy.utils.register_module(__name__)


def unregister():
    # bpy.utils.unregister_class(META_TAB_MATERIAL)
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
