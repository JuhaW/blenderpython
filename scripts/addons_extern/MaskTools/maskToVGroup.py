import bpy

# CREATE NEW


class MaskToVertexGroup(bpy.types.Operator):
    '''Mask To Vertex Group'''
    bl_idname = "mesh.masktovgroup"
    bl_label = "Mask To Vertex Group"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.mode == 'SCULPT'

    def execute(self, context):

        dynatopoEnabled = False

        if context.active_object.mode == 'SCULPT':
            if context.sculpt_object.use_dynamic_topology_sculpting:
                dynatopoEnabled = True

            # Can only called by click event  context, fails poll
            bpy.ops.paint.hide_show(action='HIDE', area='MASKED')
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.mesh.reveal()
            bpy.ops.object.vertex_group_add()
            bpy.ops.object.vertex_group_assign()
            bpy.ops.sculpt.sculptmode_toggle()

            if dynatopoEnabled:
                bpy.ops.sculpt.dynamic_topology_toggle()

        return {'FINISHED'}


# APPEND
class MaskToVertexGroupAppend(bpy.types.Operator):
    '''Append Mask To Vertex Group'''
    bl_idname = "mesh.masktovgroup_append"
    bl_label = "Append Mask To Vertex Group"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.mode == 'SCULPT'

    def execute(self, context):

        dynatopoEnabled = False

        if context.active_object.mode == 'SCULPT':
            if context.sculpt_object.use_dynamic_topology_sculpting:
                dynatopoEnabled = True

        if context.active_object.mode == 'SCULPT'and context.active_object.vertex_groups.active is not None:
            vGroupLocked = context.active_object.vertex_groups.active.lock_weight

            if vGroupLocked == False:
                # Can only called by click event  context, fails poll
                bpy.ops.paint.hide_show(action='HIDE', area='MASKED')
                bpy.ops.object.editmode_toggle()
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                bpy.ops.mesh.select_all(action='DESELECT')
                bpy.ops.mesh.reveal()
                bpy.ops.object.vertex_group_assign()
                bpy.ops.sculpt.sculptmode_toggle()

                if dynatopoEnabled:
                    bpy.ops.sculpt.dynamic_topology_toggle()

        return {'FINISHED'}

# REMOVE


class MaskToVertexGroupRemove(bpy.types.Operator):
    '''Remove Mask From Vertex Group'''
    bl_idname = "mesh.masktovgroup_remove"
    bl_label = "Remove Mask From Vertex Group"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.mode == 'SCULPT'

    def execute(self, context):

        dynatopoEnabled = False

        if context.active_object.mode == 'SCULPT':
            if context.sculpt_object.use_dynamic_topology_sculpting:
                dynatopoEnabled = True

        if context.active_object.mode == 'SCULPT'and context.active_object.vertex_groups.active is not None:
            vGroupLocked = context.active_object.vertex_groups.active.lock_weight

            if vGroupLocked == False:
                # Can only called by click event  context, fails poll
                bpy.ops.paint.hide_show(action='HIDE', area='MASKED')
                bpy.ops.object.editmode_toggle()
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                bpy.ops.mesh.select_all(action='DESELECT')
                bpy.ops.mesh.reveal()
                bpy.ops.object.vertex_group_remove_from()
                bpy.ops.sculpt.sculptmode_toggle()

                if dynatopoEnabled:
                    bpy.ops.sculpt.dynamic_topology_toggle()

        return {'FINISHED'}


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
