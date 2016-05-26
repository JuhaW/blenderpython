import bpy
from bpy import*

######################################################################################################################################################
#######-------------#################
#######  Operators  #################
#######-------------#################
######################################################################################################################################################

# Menus Add  #######-------------------------------------------------------
# Menus Add  #######-------------------------------------------------------


class VIEW3D_MT_add_menus(bpy.types.Menu):
    bl_label = "Add Menu"

    def draw(self, context):
        self.draw_menus(self.layout, context)

    @staticmethod
    def draw_menus(layout, context):
        obj = context.active_object
        mode_string = context.mode
        edit_object = context.edit_object

        if mode_string == 'OBJECT':
            layout.menu("INFO_MT_add", text="Add")
        elif mode_string == 'EDIT_MESH':
            layout.menu("INFO_MT_mesh_add", text="Add")
        elif mode_string == 'EDIT_CURVE':
            layout.menu("INFO_MT_curve_add", text="Add")
        elif mode_string == 'EDIT_SURFACE':
            layout.menu("INFO_MT_surface_add", text="Add")
        elif mode_string == 'EDIT_METABALL':
            layout.menu("INFO_MT_metaball_add", text="Add")
        elif mode_string == 'EDIT_ARMATURE':
            layout.menu("INFO_MT_edit_armature_add", text="Add")


class VIEW3D_MT_add_menus(bpy.types.Menu):
    bl_label = "Add Menu"
    bl_idname = "x_deletemode"

    def draw(self, context):
        self.draw_menus(self.layout, context)

    @staticmethod
    def draw_menus(layout, context):
        obj = context.active_object
        mode_string = context.mode
        edit_object = context.edit_object

        if mode_string == 'OBJECT':
            layout.menu("object.delete", "", icon="PANEL_CLOSE")
        elif mode_string == 'EDIT_MESH':
            layout.menu("mesh.cleandelete", "", icon="PANEL_CLOSE")
        elif mode_string == 'EDIT_CURVE':
            layout.menu("curve.delete", "", icon="PANEL_CLOSE")
        elif mode_string == 'EDIT_SURFACE':
            layout.menu("curve.delete", "", icon="PANEL_CLOSE")
        elif mode_string == 'EDIT_METABALL':
            layout.menu("mball.delete_metaelems", "", icon="PANEL_CLOSE")
        elif mode_string == 'EDIT_ARMATURE':
            layout.menu("armature.delete", "", icon="PANEL_CLOSE")


#####  Single Geometry  ###############################################################################################
#####  Single Geometry  ###############################################################################################

class SINGLEVERTEX(bpy.types.Operator):
    """Add a single 1pt Vertex to Cursor"""
    bl_idname = "mesh.singlevertex"
    bl_label = "Single Vertex"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.mesh.merge(type='CENTER')
        return {'FINISHED'}


class SINGLELINE(bpy.types.Operator):
    """Add a single 2pt Line to Cursor"""
    bl_idname = "mesh.singleline"
    bl_label = "Single Line"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.mesh.merge(type='CENTER')
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror": False}, TRANSFORM_OT_translate={"value": (0, 2, 0), "constraint_axis": (False, True, False), "constraint_orientation": 'GLOBAL', "mirror": False, "proportional": 'DISABLED', "proportional_edit_falloff": 'SMOOTH', "proportional_size": 1, "snap": False, "snap_target": 'CLOSEST', "snap_point": (0, 0, 0), "snap_align": False, "snap_normal": (0, 0, 0), "texture_space": False, "remove_on_cancel": False, "release_confirm": False})
        bpy.ops.mesh.select_linked(limit=False)

        return {'FINISHED'}


class SINGLEPLANE(bpy.types.Operator):
    """Add a single 4pt Plane to Cursor"""
    bl_idname = "mesh.singleplane"
    bl_label = "Single Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {'FINISHED'}


#####  Curve  ###############################################################################################
#####  Curve  ###############################################################################################

class FullCurve(bpy.types.Operator):
    """Add A full Bevel Curve"""
    bl_idname = "view3d.fullcurve"
    bl_label = "A full Bevel Curve"

    def execute(self, context):

        bpy.ops.curve.primitive_bezier_curve_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.ops.transform.resize(value=(5, 5, 5), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.context.object.data.fill_mode = 'FULL'
        bpy.context.object.data.bevel_resolution = 8
        bpy.context.object.data.resolution_u = 10
        bpy.context.object.data.bevel_depth = 0.2
        return {'FINISHED'}


#####  Modifier  ###############################################################################################
#####  Modifier  ###############################################################################################

class FullShrink(bpy.types.Operator):
    """add shrink modifier with vertex group"""
    bl_idname = "view3d.fullshrink"
    bl_label = "Shrinkwrap"

    def execute(self, context):

        # bpy.ops.object.vertex_group_remove(all=False)
        bpy.ops.object.modifier_add(type='SHRINKWRAP')
        bpy.ops.object.vertex_group_add()
        bpy.ops.object.vertex_group_assign()
        bpy.context.object.modifiers["Shrinkwrap"].vertex_group = "Group"
        bpy.ops.view3d.display_modifiers_cage_on()

        return {'FINISHED'}


class HalfShrink(bpy.types.Operator):
    """Add a shrink modifier with cage on"""
    bl_idname = "view3d.halfshrink"
    bl_label = "Shrinkwrap"

    def execute(self, context):

        bpy.ops.object.modifier_add(type='SHRINKWRAP')
        bpy.ops.view3d.display_modifiers_cage_on()

        return {'FINISHED'}


#####  Mirror Modifier  ############################################################################################
#####  Mirror Modifier  ############################################################################################

class FullMIRROR(bpy.types.Operator):
    """Add a x mirror modifier"""
    bl_idname = "view3d.fullmirror"
    bl_label = "Mirror X"

    def execute(self, context):

        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.ops.view3d.display_modifiers_cage_on()
        bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}


class FullMIRRORY(bpy.types.Operator):
    """Add a y mirror modifier"""
    bl_idname = "view3d.fullmirrory"
    bl_label = "Mirror Y"

    def execute(self, context):

        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_x = False
        bpy.context.object.modifiers["Mirror"].use_y = True
        bpy.ops.view3d.display_modifiers_cage_on()
        bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}


class FullMIRRORZ(bpy.types.Operator):
    """Add a z mirror modifier"""
    bl_idname = "view3d.fullmirrorz"
    bl_label = "Mirror Z"

    def execute(self, context):

        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_x = False
        bpy.context.object.modifiers["Mirror"].use_z = True
        bpy.ops.view3d.display_modifiers_cage_on()
        bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}


#####  Texture  ############################################################################################
#####  Texture  ############################################################################################

class addtex(bpy.types.Operator):
    """add texture"""
    bl_idname = "add.texturenew"
    bl_label = "Add Texture"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.texture.new()

        return {'FINISHED'}


######################################################################################################################################################
############------------############
############  REGISTER  ############
############------------############
######################################################################################################################################################


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
