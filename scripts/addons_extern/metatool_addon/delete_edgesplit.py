# bl_info = {
#    "name": "Convert edge split",
#    "category": "Object",
#    'author': 'Hugh (The squidifier) Tomkins',
#}

import bpy


def menu_func(self, context):
    self.layout.operator(convertedge.bl_idname)


class convertedge(bpy.types.Operator):
    """Edge converter"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.convertedge"        # unique identifier for buttons and menu items to reference.
    bl_label = "Convert edge modifier"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.

        # The original script
        objects = bpy.context.selected_objects

        for object in objects:
            data = object.data
            modifiers = object.modifiers
            for modifier in object.modifiers:
                print(modifier.type)
                if (modifier.type == 'EDGE_SPLIT'):
                    object.modifiers.remove(modifier)
            data.use_auto_smooth = True
            data.auto_smooth_angle = 3.1

        return {'FINISHED'}            # this lets blender know the operator finished successfully.


def register():
    bpy.types.VIEW3D_MT_object.append(menu_func)
    bpy.utils.register_class(convertedge)


def unregister():
    bpy.utils.unregister_class(convertedge)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()
