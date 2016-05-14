# The entire code was written by CoDEmanX, but the idea was mine. Still full credit to CoDEmanX.
# bl_info = {
#    "name": "Clear All",
#    "description": "This script allows you to clear an objects Location, Rotation, and Scale at the same time",
#    "author": "CoDEmanX,Albertofx",
#    "version": (1,0),
#    "blender": (2, 71, 0),
#    "location": "Search Menu",
#    "category": "3D View"
#}

import bpy
from mathutils import Matrix


class OBJECT_OT_clear_all(bpy.types.Operator):
    """Clear Location, Rotation and Scale"""
    bl_idname = "object.clear_all"
    bl_label = "Clear All"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for ob in context.selected_editable_objects:
            ob.matrix_world = Matrix.Identity(4)
        return {'FINISHED'}


def draw_func(self, context):
    layout = self.layout
    layout.operator(OBJECT_OT_clear_all.bl_idname)


def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_object_clear.append(draw_func)


def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.VIEW3D_MT_object_clear.remove(draw_func)

if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.clear_all()
