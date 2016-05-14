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


#########################################################
###----------------  VISUAL  -------------------------###
###----------------  VISUAL  -------------------------###
#########################################################

# Sub Location
class SubLoc_VISUAL():
    """Visual Tools"""
    bl_category = "META"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(cls, context):
        return context.scene.osc_visual

# Sub Panel


class META_TAB_VISUAL(SubLoc_VISUAL, bpy.types.Panel):
    """Visual Tools"""
    #bl_idname = "Visual Tools"
    bl_label = "[VISUALISATION]"

    def draw(self, context):
        active_obj = context.active_object
        layout = self.layout

        col = layout.column(align=True)

        row = col.row(align=True)
        row.operator("object.wire_all", text="Wire All", icon='WIRE')

        row = col.row(align=True)
        row.operator("view3d.display_wire_on", "Wire On", icon='WIRE')
        row.operator("view3d.display_wire_off", "Wire Off", icon='SOLID')

        row = col.row(align=True)
        row.operator("view3d.display_shadeless_on", "Shadeless On", icon='SMOOTH')
        row.operator("view3d.display_shadeless_off", "Shadeless Off", icon='SOLID')

        row = col.row(align=True)
        row.operator("view3d.display_bounds_on", "Bounds On", icon='ROTATE')
        row.operator("view3d.display_bounds_off", "Bounds Off", icon='BBOX')

        row = col.row(align=True)
        row.operator("view3d.display_double_sided_on", "DSided On", icon='OUTLINER_OB_MESH')
        row.operator("view3d.display_double_sided_off", "DSided Off", icon='MESH_DATA')

        row = col.row(align=True)
        row.operator("view3d.display_x_ray_on", "XRay On", icon='GHOST_ENABLED')
        row.operator("view3d.display_x_ray_off", "XRay Off", icon='GHOST_DISABLED')

        row = col.row(align=True)
        row.separator()

        row = col.row(align=True)
        scene = context.scene
        row.prop(scene, "BoundingMode")


############------------############
############  REGISTER  ############
############------------############


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
