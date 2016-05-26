# bl_info = {
#    "name": "Spacebar Vertices",
#    "author": "MKB",
#    "version": (0, 1, 0),
#    "blender": (2, 7, 2),
#    "location": "View3D",
#    "description": "",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "User Menu"}


import bpy
import re
from bpy import *


#############################################################################################################################################################
#############################################################################################################################################################
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ###
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ###
#############################################################################################################################################################
#############################################################################################################################################################

# Vertex Group  #######-------------------------------------------------------
# Vertex Group  #######-------------------------------------------------------

class VGroupMenu(bpy.types.Menu):
    bl_label = "Vertex Group"
    bl_idname = "vgroupmenu"

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("object.vertex_group_select", text="Select Group", icon="RESTRICT_SELECT_OFF")
        layout.operator("object.vertex_group_deselect", text="Deselect Group", icon="RESTRICT_SELECT_ON")

        layout.separator()

        layout.operator("object.vertex_group_assign", text="Assign Group", icon="ZOOMIN")
        layout.operator("object.vertex_group_remove_from", text="Remove Group", icon="ZOOMOUT")

        layout.separator()

        layout.operator("object.vertex_group_add", icon='GROUP_VERTEX', text="Add Vertex Group")
        layout.operator("object.vertex_group_remove", icon='GROUP_VERTEX', text="Remove Vertex Group").all = False

bpy.utils.register_class(VGroupMenu)


# Additional  #######-------------------------------------------------------
# Additional  #######-------------------------------------------------------

class VertAdditionalMenu(bpy.types.Menu):
    bl_label = "Additional"
    bl_idname = "vert_additionalmenu"

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("mesh.convex_hull")
        layout.operator("mesh.blend_from_shape")
        layout.operator("mesh.shape_propagate_to_all")
        layout.operator("object.vertex_group_blend")

bpy.utils.register_class(VertAdditionalMenu)


#############################################################################################################################################################
#############################################################################################################################################################
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
#############################################################################################################################################################
#############################################################################################################################################################

# Vertices Menu  #######-------------------------------------------------------
# Vertices Menu  #######-------------------------------------------------------


class VIEW3D_Space_Vertice_edm(bpy.types.Menu):
    bl_label = "Vertices"
    bl_idname = "space_vertice_edm"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_MESH'))

    def draw(self, context):
        settings = context.tool_settings
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("mesh.vertex_distribute", text="Distribute", icon="PARTICLE_POINT")
        layout.operator("mesh.vertex_align", text="Align First to Last")

        layout.separator()

        layout.operator("mesh.merge", icon="AUTOMERGE_ON")
        layout.operator("mesh.vert_connect", text="Connect")
        layout.operator("mesh.fill_holes")

        layout.separator()

        layout.operator("mesh.rip_move", icon="FULLSCREEN_ENTER")
        layout.operator("mesh.rip_move_fill")
        layout.operator("mesh.rip_edge_move")

        layout.separator()

        layout.operator("mesh.split", icon="RETOPO")
        layout.operator("mesh.vert_connect_nonplanar")
        layout.operator_menu_enum("mesh.separate", "type")

        layout.separator()

        layout.operator("mesh.bevel", icon="SPHERECURVE").vertex_only = True
        layout.operator("transform.vert_slide", text="Vertices Slide")
        layout.operator("mesh.edgetune", text="Edgetune Slide", icon="PARTICLE_POINT")

        layout.separator()

        layout.operator("mesh.vertices_smooth", icon="CURVE_DATA")
        layout.operator("mesh.vertices_smooth_laplacian", text="Smooth Laplacian")

        layout.separator()

        layout.operator("mesh.mark_sharp", text="Mark Sharp").use_verts = True
        op = layout.operator("mesh.mark_sharp", text="Clear Sharp")
        op.use_verts = True
        op.clear = True

        layout.separator()

        layout.menu("vert_additionalmenu", icon="RESTRICT_SELECT_OFF")

        layout.separator()

        layout.menu("VIEW3D_MT_hook", icon="HOOK")

        layout.separator()

        layout.menu("vgroupmenu", icon="GROUP_VERTEX")
        layout.menu("MESH_MT_vertex_group_specials", icon='DOWNARROW_HLT', text="Vertex Group Specials")


###########################################################################################################################################################
###########################################################################################################################################################
# Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register
# Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register
###########################################################################################################################################################
###########################################################################################################################################################


def register():
    bpy.utils.register_class(VIEW3D_Space_Vertice_edm)


def unregister():
    bpy.utils.unregister_class(VIEW3D_Space_Vertice_edm)

if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_Space_Vertice_edm.bl_idname)
