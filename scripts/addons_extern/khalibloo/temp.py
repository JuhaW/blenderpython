import bpy
import custom_ops
class OperatorBlock0MoveDown(bpy.types.Operator):
    """Move operator block Down"""
    bl_idname = "object.khalibloo_opblock0_move_down"
    bl_label = "Move Operator Block Down"
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context):
        for opblock in context.scene.khalibloo_opblocks:
            if (opblock != None):
                if (opblock.index == 0):
                    block = opblock
                    break
        custom_ops.moveOpblock(opblock=block, direction='DOWN')
        return {'FINISHED'}
bpy.utils.register_class(OperatorBlock0MoveDown)