# <pep8 compliant>

file_data = '''
import bpy

rig_id = "%s"

class FaceLayers(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Face Layers"
    bl_idname = rig_id + "_Face_rig_layers"

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False

    def draw(self, context):
        layout = self.layout
        col = layout.column()

        row = col.row()
        row.prop(context.active_object.data, 'layers', index=19, toggle=True, text='main')

        row = col.row()
        row.prop(context.active_object.data, 'layers', index=20, toggle=True, text='mimics')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=21, toggle=True, text='stretch squash')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=24, toggle=True, text='tmp')

def register():
    bpy.utils.register_class(FaceLayers)
    
def unregister():
    bpy.utils.unregister_class(FaceLayers)
    
register()

'''