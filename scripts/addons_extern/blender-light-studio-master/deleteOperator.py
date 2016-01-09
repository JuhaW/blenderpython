import bpy
from bpy.props import BoolProperty

class DeleteOperator(bpy.types.Operator):
    """ Custom delete """
    bl_idname = "object.delete_custom" 
    bl_label = "Delete"
    bl_options = {'REGISTER', 'UNDO'}

    use_global = BoolProperty(default = False)

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D' and context.mode == 'OBJECT'
    
    def execute(self, context):
        for obj in context.selected_objects:
            if obj.protected :
                obj.select = False
                self.report({'WARNING'}, obj.name +' is protected')

        bpy.ops.object.delete(use_global=self.use_global)
        #change the property

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=100)
            
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.label(text="OK?")

def replace_shortkey( old_op_name, new_op_name) :
        wm = bpy.context.window_manager
        keyconfig = wm.keyconfigs.active
        keymap = keyconfig.keymaps['Object Mode']
        items = keymap.keymap_items

        item = items.get(old_op_name, None)
        while item :

                props = item.properties

                use_global = props.use_global.real

                item.idname = new_op_name

                props.use_global = use_global

                item = items.get( old_op_name, None)


