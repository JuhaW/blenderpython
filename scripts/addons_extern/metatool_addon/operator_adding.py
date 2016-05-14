import bpy
from bpy import*

######################################################################################################################################################
#######-------------#################
#######  Operators  #################
#######-------------#################
######################################################################################################################################################


#####  Add Geometry  ###############################################################################################
#####  Add Geometry  ###############################################################################################

class SINGLEVERTEX(bpy.types.Operator):
    """Add a single Vertex in Editmode"""
    bl_idname = "mesh.singlevertex"
    bl_label = "Single Vertex"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.mesh.merge(type='CENTER')

        return {'FINISHED'}


class SINGLELINE(bpy.types.Operator):
    """Add a single Line in Editmode"""
    bl_idname = "mesh.singleline"
    bl_label = "Single Line"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.mesh.merge(type='CENTER')
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror": False}, TRANSFORM_OT_translate={"value": (0, 2, 0), "constraint_axis": (False, True, False), "constraint_orientation": 'GLOBAL', "mirror": False, "proportional": 'DISABLED', "proportional_edit_falloff": 'SMOOTH', "proportional_size": 1, "snap": False, "snap_target": 'CLOSEST', "snap_point": (0, 0, 0), "snap_align": False, "snap_normal": (0, 0, 0), "texture_space": False, "remove_on_cancel": False, "release_confirm": False})
        bpy.ops.mesh.select_linked_pick(deselect=False, limit=False)

        return {'FINISHED'}


class SINGLEPLANE(bpy.types.Operator):
    """Add a single Plane in Editmode"""
    bl_idname = "mesh.singleplane"
    bl_label = "Single Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {'FINISHED'}


class SINGLEPLANE_X(bpy.types.Operator):
    """Add a vertical Plane in Editmode"""
    bl_idname = "mesh.singleplane_x"
    bl_label = "Single Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {'FINISHED'}


class SINGLEPLANE_Y(bpy.types.Operator):
    """Add a vertical Plane in Editmode"""
    bl_idname = "mesh.singleplane_y"
    bl_label = "Single Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {'FINISHED'}


class SINGLEPLANE_Z(bpy.types.Operator):
    """Add a vertical Plane in Editmode"""
    bl_idname = "mesh.singleplane_z"
    bl_label = "Single Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}


class EMPTYROOMCEN(bpy.types.Operator):
    """Add a object without a mesh in editmode to center"""
    bl_idname = "mesh.emptyroom_cen"
    bl_label = "Retopo CenterRoom"

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_center()
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.delete(type='VERT')
        return {'FINISHED'}


class EMPTYXROOMCEN(bpy.types.Operator):
    """Add a object without a mesh in editmode and add a x mirror modifier to center"""
    bl_idname = "mesh.emptyxroom_cen"
    bl_label = "Retopo X-CenterRoom"

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_center()
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.delete(type='VERT')
        bpy.ops.view3d.fullmirror()

        return {'FINISHED'}


class EMPTYROOM(bpy.types.Operator):
    """Add a object without a mesh in editmode to selected"""
    bl_idname = "mesh.emptyroom_sel"
    bl_label = "Retopo SelectRoom"

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.delete(type='VERT')
        return {'FINISHED'}


class EMPTYXROOM(bpy.types.Operator):
    """Add a object without a mesh in editmode and add a x mirror modifier to selected"""
    bl_idname = "mesh.emptyxroom_sel"
    bl_label = "Retopo X-SelectRoom"

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.delete(type='VERT')
        bpy.ops.view3d.fullmirror()

        return {'FINISHED'}


class FullCurve(bpy.types.Operator):
    """Add A full Bevel Curve"""
    bl_idname = "view3d.fullcurve"
    bl_label = "A full Bevel Curve"

    def execute(self, context):

        bpy.ops.curve.primitive_bezier_curve_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        bpy.ops.transform.resize(value=(5, 5, 5), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.context.object.data.fill_mode = 'FULL'
        bpy.context.object.data.bevel_resolution = 8
        bpy.context.object.data.resolution_u = 10
        bpy.context.object.data.bevel_depth = 0.2
        return {'FINISHED'}


import bpy
import mathutils
import math
import re
from mathutils.geometry import intersect_line_plane
from mathutils import Vector
from math import radians
from bpy import*


############  Objectmode Operator  ############


# further function for BoundingBoxSource
class BoundingBox (bpy.types.Operator):
    """create a bound boxes for selected object"""
    bl_idname = "object.bounding_boxers"
    bl_label = "BBox"
    bl_options = {'REGISTER', 'UNDO'}

    bbox_subdiv = bpy.props.IntProperty(name="Subdivide", description="How often?", default=0, min=0, soft_max=10, step=1)

    bbox_wire = bpy.props.BoolProperty(name="Wire only", description="Delete Face", default=False)

    bbox_origin = bpy.props.BoolProperty(name="Origin Center", description="Origin to BBox-Center", default=False)

    bbox_freeze = bpy.props.BoolProperty(name="Freeze Selection", description="Hide from selection", default=False)

    def execute(self, context):

        bpy.ops.object.bounding_box_source()
        bpy.ops.object.select_pattern(pattern="_bbox_edit", case_sensitive=False, extend=False)

        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

        for obj in bpy.context.selected_objects:
            bpy.context.scene.objects.active = obj

            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.normals_make_consistent()

            for i in range(self.bbox_subdiv):
                bpy.ops.mesh.subdivide(number_cuts=1)

            for i in range(self.bbox_wire):
                bpy.ops.mesh.delete(type='ONLY_FACE')

            bpy.ops.object.editmode_toggle()

            for i in range(self.bbox_origin):
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

            for i in range(self.bbox_freeze):
                bpy.context.object.hide_select = True

            bpy.context.object.name = "_bbox"

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)


# BoundingBoxSource from nikitron
class BoundingBoxSource (bpy.types.Operator):
    """Make bound boxes for selected objects"""
    bl_idname = "object.bounding_box_source"
    bl_label = "Bounding boxes"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        objects = bpy.context.selected_objects
        i = 0
        for a in objects:
            self.make_it(i, a)
            i += 1

        return {'FINISHED'}

    def make_it(self, i, obj):
        box = bpy.context.selected_objects[i].bound_box
        mw = bpy.context.selected_objects[i].matrix_world
        name = ('_bbox_edit')  # name = (bpy.context.selected_objects[i].name + '_bbox')
        me = bpy.data.meshes.new(name)  # bpy.data.meshes.new(name + 'Mesh')
        ob = bpy.data.objects.new(name, me)

        ob.location = mw.translation
        ob.scale = mw.to_scale()
        ob.rotation_euler = mw.to_euler()
        ob.show_name = False
        bpy.context.scene.objects.link(ob)
        loc = []
        for ver in box:
            loc.append(mathutils.Vector((ver[0], ver[1], ver[2])))
        me.from_pydata((loc), [], ((0, 1, 2, 3), (0, 1, 5, 4), (4, 5, 6, 7), (6, 7, 3, 2), (0, 3, 7, 4), (1, 2, 6, 5)))
        me.update(calc_edges=True)
        return


class FullCurve(bpy.types.Operator):
    """Add A full Bevel Curve"""
    bl_idname = "view3d.fullcurve"
    bl_label = "A full Bevel Curve"
    bl_options = {'REGISTER', 'UNDO'}

    curve_subdiv = bpy.props.IntProperty(name="Subdivide", description="How often?", default=0, min=0, soft_max=10, step=1)

    def execute(self, context):

        bpy.ops.curve.primitive_bezier_curve_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        bpy.ops.transform.resize(value=(5, 5, 5), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.context.object.data.fill_mode = 'FULL'
        bpy.context.object.data.bevel_resolution = 4
        bpy.context.object.data.resolution_u = 10
        bpy.context.object.data.bevel_depth = 0.2

        bpy.ops.object.editmode_toggle()

        bpy.context.object.data.show_normal_face = False

        for i in range(self.curve_subdiv):
            bpy.ops.curve.subdivide(number_cuts=1)

        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


class FullCircleCurve(bpy.types.Operator):
    """Add A full Bevel Circle Curve"""
    bl_idname = "view3d.fullcirlcecurve"
    bl_label = "A full Bevel CircleCurve"
    bl_options = {'REGISTER', 'UNDO'}

    curve_subdiv = bpy.props.IntProperty(name="Subdivide", description="How often?", default=0, min=0, soft_max=10, step=1)

    curve_cycle = bpy.props.BoolProperty(name="Open?", description="Open", default=False)

    def execute(self, context):

        bpy.ops.curve.primitive_bezier_circle_add(view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        bpy.ops.transform.resize(value=(5, 5, 5), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.context.object.data.fill_mode = 'FULL'
        bpy.context.object.data.bevel_resolution = 4
        bpy.context.object.data.resolution_u = 10
        bpy.context.object.data.bevel_depth = 0.2

        bpy.ops.object.editmode_toggle()

        bpy.context.object.data.show_normal_face = False

        for i in range(self.curve_subdiv):
            bpy.ops.curve.subdivide(number_cuts=1)

        for i in range(self.curve_cycle):
            bpy.ops.curve.cyclic_toggle(direction='CYCLIC_U')

        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


# Menu for Objectmode
class CustomAddMenu_OBM(bpy.types.Menu):
    bl_label = "Custom"
    bl_idname = "OBJECT_MT_custom_Add_menu"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.bounding_boxers", "BBox", icon="BBOX")

        layout.separator()

        layout.operator("view3d.fullcurve", "Bevel Curve", icon="CURVE_BEZCURVE")
        layout.operator("view3d.fullcirlcecurve", "Bevel Circle", icon="CURVE_BEZCIRCLE")


############  Draw Menu  ############


# add a menu to objectmode
def draw_item_OBM(self, context):
    layout = self.layout
    layout.menu(CustomAddMenu_OBM.bl_idname, icon="ROTATE")


# add a menu to editmode
def draw_item_EDM(self, context):
    layout = self.layout
    if context.mode == 'EDIT_MESH':
        layout.menu(CustomAddMenu_EDM.bl_idname, icon="ROTATE")


# add single operator
def draw_item_Vert(self, context):
    layout = self.layout
    if context.mode == 'EDIT_MESH':
        layout.operator("mesh.singlevertex", text="Vertex", icon="STICKY_UVS_DISABLE")


# add a menu to objectmode
def draw_item_Curve(self, context):
    layout = self.layout
    if context.mode == 'OBJECT':
        layout.separator()

        layout.operator("view3d.fullcurve", "Bevel Curve", icon="CURVE_BEZCURVE")
        layout.operator("view3d.fullcirlcecurve", "Bevel Circle", icon="CURVE_BEZCIRCLE")

        layout.separator()

        obj = context.active_object
        if obj:
            obj_type = obj.type

            if obj_type in {'CURVE'}:
                layout.operator("curve.bevelcurve", "Add Curve as Bevel", icon="CURVE_BEZCIRCLE")
                layout.operator("curve.tapercurve", "Add Curve as Taper", icon="CURVE_BEZCURVE")


# add single operator
def draw_item(self, context):
    self.layout.operator("object.bounding_boxers", "BBox", icon="BBOX")


######################################################################################################################################################
############------------############
############  REGISTER  ############
############------------############
######################################################################################################################################################

def register():

    bpy.utils.register_class(BoundingBoxSource)
    bpy.utils.register_class(BoundingBox)

    bpy.utils.register_class(FullCurve)
    bpy.utils.register_class(FullCircleCurve)

    bpy.utils.register_class(CustomAddMenu_OBM)

    # prepend = to MenuTop / append to MenuBottom
    bpy.types.INFO_MT_add.prepend(draw_item)
    bpy.types.INFO_MT_mesh_add.prepend(draw_item_Vert)

    # bpy.types.INFO_MT_add.prepend(draw_item_OBM)
    bpy.types.INFO_MT_mesh_add.append(draw_item_EDM)
    bpy.types.INFO_MT_curve_add.append(draw_item_Curve)

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_class(BoundingBoxSource)
    bpy.utils.unregister_class(BoundingBox)

    bpy.utils.unregister_class(FullCurve)
    bpy.utils.unregister_class(FullCircleCurve)

    bpy.utils.unregister_class(CustomAddMenu_OBM)
    bpy.utils.unregister_class(CustomAddMenu_EDM)

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
