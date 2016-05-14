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


class DropdownMetaTool_RELATION_Props(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.metawindowtool_relation
    """
    # TAB Relations
    display_tab_relations = bpy.props.BoolProperty(name="Relations", description="Display Relations Tools", default=True)
    display_tab_relagroup = bpy.props.BoolProperty(name="Group", description="Display Group Tools", default=False)
    display_tab_relaparent = bpy.props.BoolProperty(name="Parent", description="Display Parent Tools", default=False)
    display_tab_relaconstraint = bpy.props.BoolProperty(name="Constraint", description="Display Constraint Tools", default=False)


#############################################################
###-----------------  Relations  -------------------------###
###-----------------  Relations  -------------------------###
#############################################################

# Sub Location
class SubLoc_RELA():
    """Relation Tools"""
    bl_category = "META"
    #bl_region_type = 'TOOLS'
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(cls, context):
        return context.scene.osc_relation

# Sub Panel


class META_TAB_RELA(SubLoc_RELA, bpy.types.Panel):
    """Relation Tools"""
    bl_idname = """meta.relations"""
    bl_label = """[RELATION]"""

    def draw(self, context):
        lt = context.window_manager.metawindowtool_relation
        active_obj = context.active_object
        layout = self.layout


# -------------------------------------------------------
# Relations  #######-------------------------------------------------------
# Relations  #######-------------------------------------------------------
# -------------------------------------------------------

        col = layout.column(align=True)

        if lt.display_tab_relations:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_tab_relations", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_tab_relations", text="", icon='TRIA_RIGHT')

        row.label("Relations...")

        if lt.display_tab_relations:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.menu("VIEW3D_MT_make_links", text="Make Links", icon="LINKED")
            row = col_top.row(align=True)
            row.menu("VIEW3D_MT_make_single_user", text="Make Single User", icon="UNLINKED")

            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("object.visual_transform_apply", icon="NDOF_DOM")

            row = col_top.row(align=True)
            row.operator("object.duplicates_make_real", icon="MOD_PARTICLES")
            row.operator("help_operator", text="", icon="INFO")

            row = col_top.row(align=True)
            row.operator("object.set_instance", text="Set as Instance", icon="LINK_AREA")


# Group  ######-------------------------------------
# Group  ######-------------------------------------

            split = col.split(percentage=0.15, align=True)

            if lt.display_tab_relagroup:
                split.prop(lt, "display_tab_relagroup", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                split.prop(lt, "display_tab_relagroup", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

            spread_op = split.operator("group.create", text="Group", icon="STICKY_UVS_LOC")

            if lt.display_tab_relagroup:
                box = col.column(align=True).box().column()

                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("group.create", text="Group to Selected")
                row = col_top.row(align=True)
                row.operator("group.objects_remove", text="Remove Group from Selected")

                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("group.objects_add_active", text="Group to Active")
                row = col_top.row(align=True)
                row.operator("group.objects_remove_active", text="Remove Group from Active")


# Parent  ######-------------------------------------
# Parent  ######-------------------------------------

            split = col.split(percentage=0.15, align=True)

            if lt.display_tab_relaparent:
                split.prop(lt, "display_tab_relaparent", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                split.prop(lt, "display_tab_relaparent", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

            spread_op = split.operator("object.parent_set", text="Parent", icon="CONSTRAINT")

            if lt.display_tab_relaparent:
                box = col.column(align=True).box().column()

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("object.parent_clear").type = "CLEAR"
                row = col_top.row(align=True)
                row.operator("object.parent_clear", text="Clear Inverse").type = "CLEAR_INVERSE"
                row = col_top.row(align=True)
                row.operator("object.parent_clear", text="Clear Keep Transform").type = "CLEAR_KEEP_TRANSFORM"


# Constraint  ######-------------------------------------
# Constraint  ######-------------------------------------

            split = col.split(percentage=0.15, align=True)

            if lt.display_tab_relaconstraint:
                split.prop(lt, "display_tab_relaconstraint", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                split.prop(lt, "display_tab_relaconstraint", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

            spread_op = split.operator_menu_enum("object.constraint_add", "type", text="  Constraint", icon="CONSTRAINT_DATA")

            if lt.display_tab_relaconstraint:
                box = col.column(align=True).box().column()

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("lookat.it", text="Look @ Obj")
                row.operator("lookat.cursor", text="Look @ Cursor")

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.label(text="to Selected:", icon="LAYER_ACTIVE")

                row = col_top.row(align=True)
                row.operator("track.to", text="Track To")
                row.operator("damped.track", text="Damped Track")
                row.operator("lock.track", text="Lock Track")

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.label(text="to CursorPos+Empty:", icon="LAYER_ACTIVE")

                row = col_top.row(align=True)
                row.operator("track.toempty", text="Track To")
                row.operator("damped.trackempty", text="Damped Track")
                row.operator("lock.trackempty", text="Lock Track")


############------------############
############  REGISTER  ############
############------------############


def register():

    # bpy.utils.register_class(META_TAB_RELA)

    bpy.utils.register_class(DropdownMetaTool_RELATION_Props)
    bpy.types.WindowManager.metawindowtool_relation = bpy.props.PointerProperty(type=DropdownMetaTool_RELATION_Props)

    bpy.utils.register_module(__name__)


def unregister():

    # bpy.utils.unregister_class(META_TAB_RELA)

    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
