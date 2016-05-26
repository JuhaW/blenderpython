import bpy
from bpy import*

######################################################################################################################################################
#######-------------#################
#######  Operators  #################
#######-------------#################
######################################################################################################################################################

#####  Edit  ############################################################################################
#####  Edit  ############################################################################################


class CleanDelete(bpy.types.Menu):
    """Clean Up Mesh"""
    bl_label = "Clean Up & Delete Mesh"
    bl_idname = 'mesh.cleandelete'

    def draw(self, context):
        layout = self.layout

        layout.operator("mesh.delete", "Vertices", icon="SNAP_VERTEX").type = "VERT"
        layout.operator("mesh.dissolve_verts")
        layout.operator("mesh.remove_doubles")

        layout.separator()

        layout.operator("mesh.delete", "Edges", icon="SNAP_EDGE").type = "EDGE"
        layout.operator("mesh.dissolve_edges")
        layout.operator("mesh.delete_edgeloop", text="Remove Edge Loop")

        layout.separator()

        layout.operator("mesh.delete", "Faces", icon="SNAP_FACE").type = "FACE"
        layout.operator("mesh.dissolve_faces")
        layout.operator("mesh.delete", "Remove only Faces").type = "ONLY_FACE"

        layout.separator()

        layout.operator("mesh.dissolve_limited", icon="MATCUBE")
        layout.operator("mesh.dissolve_degenerate")
        layout.operator("mesh.delete", "Remove Edge & Faces").type = "EDGE_FACE"

        layout.separator()

        layout.operator("mesh.fill_holes", icon="RETOPO")
        layout.operator("mesh.delete_loose")
        layout.operator("mesh.edge_collapse")
        layout.operator("mesh.vert_connect_nonplanar")

        layout.separator()
        layout.operator("meshlint.select", "Meshlint > Mesh Data")


class ObjClearDelete(bpy.types.Menu):
    """Clear Menu"""
    bl_label = "Clear Menu"
    bl_idname = 'object.cleandelete'

    def draw(self, context):
        layout = self.layout

        layout.operator("object.hide_view_clear", text="Clear Hide")
        layout.operator("material.remove", text="Clear Materials")

        layout.separator()

        layout.menu("VIEW3D_MT_object_clear", text="Clear Location")
        layout.menu("clearparent", text="Clear Parenting")
        layout.menu("cleartrack", text="Clear Tracking")

        layout.separator()

        layout.operator("object.constraints_clear", text="Clear Constraint")
        layout.operator("anim.keyframe_clear_v3d", text="Clear Keyframe")
        layout.operator("object.game_property_clear")


#####  Pivot Align XYZ  ###############################################################################################
#####  Pivot Align XYZ  ###############################################################################################

class alignxy(bpy.types.Operator):
    """align selected to XY-axis / depend by pivot"""
    bl_label = "align selected face to XY axis"
    bl_idname = "mesh.face_align_xy"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.transform.resize(value=(0, 0, 1), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}


class alignxz(bpy.types.Operator):
    """align selected to XZ-axis / depend by pivot"""
    bl_label = "align xz"
    bl_idname = "mesh.face_align_xz"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.transform.resize(value=(0, 1, 0), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}


class alignyz(bpy.types.Operator):
    """align selected to yz-axis / depend by pivot"""
    bl_label = "align yz"
    bl_idname = "mesh.face_align_yz"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.transform.resize(value=(1, 0, 0), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}


#####  Flat Align XYZ  ###############################################################################################
#####  Flat Align XYZ  ###############################################################################################

class alignx(bpy.types.Operator):
    """align selected to X-axis / depend by pivot"""
    bl_label = "align selected face to X axis"
    bl_idname = "mesh.face_align_x"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}


class aligny(bpy.types.Operator):
    """align selected to Y-axis / depend by pivot"""
    bl_label = "align y"
    bl_idname = "mesh.face_align_y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}


class alignz(bpy.types.Operator):
    """align selected to Z-axis / depend by pivot"""
    bl_label = "align z"
    bl_idname = "mesh.face_align_z"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}


#####  Material  ###############################################################################################
#####  Material  ###############################################################################################

class deleteMat(bpy.types.Operator):
    """delete material slots"""
    bl_idname = "material.remove"
    bl_label = "Delete all Material"
    bl_options = {'REGISTER', 'UNDO'}

    deleteMat = bpy.props.IntProperty(name="Delete all Material", description="How many times?", default=100, min=1, soft_max=1000, step=1)

    def execute(self, context):

        for i in range(self.deleteMat):

            bpy.ops.object.material_slot_remove()

        return {'FINISHED'}


class MetaObjMaterial(bpy.types.Operator):
    """add a new material and enable color object in options"""
    bl_idname = "meta.newmaterial"
    bl_label = "Add Material"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.assign_material()
        bpy.context.object.active_material.use_object_color = True
        return {'FINISHED'}

bpy.utils.register_class(MetaObjMaterial)


#####  -  ###############################################################################################
#####  -  ###############################################################################################

class CurveDirection(bpy.types.Operator):
    """change curve direction / click 1x or 2x times"""
    bl_idname = "meta.curvedirection"
    bl_label = "Curve Direction"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.select_all()
        bpy.ops.curve.switch_direction()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}

bpy.utils.register_class(CurveDirection)


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
