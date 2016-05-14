import bpy
import bmesh
from bpy.props import *

bl_info = {
    "name": "MakeRope",
    "description": "Make a rope object between two points",
    "author": "Couzar Michel",
    "version": (0, 0, 2),
    "blender": (2, 76, 0),
    "location": "View3D",
    "wiki_url": "",
    "category": "Object"}


def getWorld(vco, ob):
    mat = ob.matrix_world
    loc = mat * vco
    return loc


def getEnds(ob):
    verts = ob.data.vertices
    for v in verts:
        if v.select:
            return v.co


def makeline(ends, line):
    bm = bmesh.new()
    for v in ends:
        bm.verts.new(v)
    bm.verts.ensure_lookup_table()
    bverts = (bm.verts[0], bm.verts[1])
    bm.edges.new(bverts)
    bm.to_mesh(line)


class AddRopeHooks(bpy.types.Operator):
    bl_idname = 'object.add_rope_hooks'
    bl_label = 'Add Hooks'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return not context.screen.is_animation_playing

    def execute(self, context):
        obj = context.active_object
        line = obj.data
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')
        for e in range(2):
            vert = line.vertices[e]
            vert.select = True
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.object.hook_add_newob()
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.modifier_move_down(modifier="Rope")
        context.scene.objects.active = obj
        obj.select = True
        return{'FINISHED'}


class ApplyRope(bpy.types.Operator):
    bl_idname = 'object.apply_rope'
    bl_label = 'Apply Rope'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return not context.screen.is_animation_playing

    def execute(self, context):
        obj = context.active_object
        for ob in bpy.data.objects:
            if ob != obj:
                ob.select = False
        cmod = obj.modifiers['Rope']
        bpy.ops.object.convert(target='CURVE')
        obj.is_rope = False
        spline = obj.data.splines[0]
        spline.type = 'BEZIER'
        for p in spline.bezier_points:
            p.handle_left_type = 'AUTO'
            p.handle_right_type = 'AUTO'
        bpy.context.scene.frame_end = 250
        return{'FINISHED'}


class RopeSim(bpy.types.Operator):
    bl_idname = 'object.rope_sim'
    bl_label = 'Simulate Rope'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = bpy.context.scene
        screen = bpy.context.screen
        scene.frame_end = 5000
        if not screen.is_animation_playing:
            scene.frame_set(1)
            bpy.ops.screen.animation_play()
        else:
            bpy.ops.screen.animation_play()
        return {'FINISHED'}


class MakeRope(bpy.types.Operator):
    """Create a rope between to selected vertices"""
    bl_idname = "object.make_rope"
    bl_label = "Make Rope"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and len(context.selected_objects) == 2

    def execute(self, context):
        ends = []
        cnt = 0
        for ob in bpy.context.selected_objects:
            co = getEnds(ob)
            if not co:
                self.report({'ERROR'}, 'Please select vertex in ' + ob.name)
                return{'CANCELLED'}
            vco = getWorld(co, ob)
            ends.append(vco)
        line = bpy.data.meshes.new('rope')
        obj = bpy.data.objects.new('Rope', line)
        context.scene.objects.link(obj)
        bpy.context.scene.objects.active = obj
        obj.select = True
        makeline(ends, line)

        for v in line.vertices:
            v.select = True
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.subdivide(number_cuts=8)
        bpy.ops.object.mode_set(mode='OBJECT')

        vg = obj.vertex_groups.new('rope ends')
        vg.add(range(0, 2), 1.0, 'REPLACE')

        cmod = obj.modifiers.new('Rope', 'CLOTH')
        cmod.point_cache.frame_end = 5000
        cmod.settings.use_pin_cloth = True
        cmod.settings.vertex_group_mass = vg.name
        obj.is_rope = True
        return{'FINISHED'}


class MakeRopePanel(bpy.types.Panel):
    bl_label = "Make Rope"
    bl_category = "Make Rope"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "objectmode"

    @classmethod
    def poll(cls, context):
        if context.active_object != None:
            return context.active_object.is_rope or len(context.selected_objects) == 2
        else:
            return False

    def draw(self, context):
        obj = context.active_object
        layout = self.layout
        row = layout.row()
        if not context.active_object.is_rope:
            row.operator('object.make_rope', text='Make Rope', icon='IPO_BACK')
        else:
            if not bpy.context.screen.is_animation_playing:
                row.operator('object.rope_sim', text='Simulate')
            else:
                row.operator('screen.animation_play', text='Stop')
            row = layout.row()
            row.prop(obj.modifiers['Rope'].settings, 'structural_stiffness', text='Tension')
            row = layout.row()
            row.operator('object.add_rope_hooks')
            row = layout.row()
            box = row.box()
            box.operator('object.apply_rope', text='Apply')


def register():
    bpy.utils.register_module(__name__)
    bpy.types.Object.is_rope = bpy.props.BoolProperty(name='Rope Object')


def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
