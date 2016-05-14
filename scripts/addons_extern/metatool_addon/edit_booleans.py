
bl_info = {
    "name": "Boolean Operators",
    "location": "View3D > Toolshelf > Addons",
    "description": "Add Boolean Tools for running boolean operations on two selected objects.",
    "author": "Jonathan Williamson",
    "version": (0, 4),
    "blender": (2, 71, 0),
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/booleanoperators",
    "tracker_url": "https://developer.blender.org/T34502",
    "category": "Object"}


import bpy

###------ Create Boolean Operators -------###


class boolean_A(bpy.types.Operator):
    """Boolean the currently selected objects"""
    bl_idname = "mesh.boolean"
    bl_label = "Boolean Operator"
    bl_options = {'REGISTER', 'UNDO'}

    modOp = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0

    def execute(self, context):

        scene = bpy.context.scene

        modName = "Bool"

        activeObj = context.active_object
        selected = context.selected_objects

        if selected:
            if len(selected) > 1:
                if len(selected) == 2:
                    for ob in selected:
                        if ob != activeObj:
                            nonActive = ob

                    bpy.ops.object.modifier_add(type="BOOLEAN")

                    for mod in activeObj.modifiers:
                        if mod.type == 'BOOLEAN':
                            mod.operation = self.modOp
                            mod.object = nonActive
                            mod.name = modName

                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modName)
                    scene.objects.active = nonActive
                    activeObj.select = False
                    bpy.ops.object.delete(use_global=False)
                    activeObj.select = True
                    scene.objects.active = activeObj
                else:
                    self.report({'INFO'}, "Select only 2 objects at a time")
            else:
                self.report({'INFO'}, "Only 1 object selected")
        else:
            self.report({'INFO'}, "No objects selected")

        return {"FINISHED"}


###------- Create the Boolean Menu --------###

class booleanMenu_B(bpy.types.Menu):
    bl_label = "Boolean Tools"
    bl_idname = "object.boolean_menu"

    def draw(self, context):
        layout = self.layout

        union = layout.operator("mesh.boolean", "Union")
        union.modOp = 'UNION'

        intersect = layout.operator("mesh.boolean", "Intersect")
        intersect.modOp = 'INTERSECT'

        difference = layout.operator("mesh.boolean", "Difference")
        difference.modOp = 'DIFFERENCE'


###------- Create the Boolean Toolbar --------###
"""
class booleanToolbar_C(bpy.types.Panel):
    bl_label = "Boolean Tools"
    bl_idname = "object.boolean_toolbar"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = 'objectmode'
    bl_category = 'Tools'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)

        col.label(text="Operation:", icon="MOD_BOOLEAN")

        row = col.row()
        union = row.operator("mesh.boolean", "Union")
        union.modOp = 'UNION'

        intersect = row.operator("mesh.boolean", "Intersect")
        intersect.modOp = 'INTERSECT'

        difference = row.operator("mesh.boolean", "Difference")
        difference.modOp = 'DIFFERENCE'
"""
###------- Define the Hotkeys and Register Operators ---------###


def register():
    bpy.utils.register_class(boolean_A)
    bpy.utils.register_class(booleanMenu_B)
    # bpy.utils.register_class(booleanToolbar_C)

    wm = bpy.context.window_manager


def unregister():
    bpy.utils.unregister_class(boolean_A)
    bpy.utils.unregister_class(booleanMenu_B)
    # bpy.utils.unregister_class(booleanToolbar_C)


if __name__ == "__main__":
    register()
