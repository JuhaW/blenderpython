from core import *

class LayerSet(bpy.types.Operator):
    '''Visualize this Layer, Shift-Click to select multiple layers'''
    bl_idname = "view3d.layer_set"
    bl_label = "Set Layers"
    
    layer_num = None
    
    def modal(self, context, event):
        if event.shift:
            # toggle the layer on/off
            context.scene.layers[self.layer_num] = not context.scene.layers[self.layer_num]
            
        else:
            # create a boolian list of which layers on and off
            layers = [False]*20
            layers[self.layer_num] = True
            
            # apply the list to blender's layers
            context.scene.layers = layers
        
        # call the layer menu again so it stays up
        bpy.ops.wm.call_menu(name="view3d.layers_menu")
        
        return {'FINISHED'}
    
    def execute(self, context):
        context.window_manager.modal_handler_add(self)
        
        return {'RUNNING_MODAL'}
    
class NoShortcutViewOp(bpy.types.Operator):
    bl_label = ""
    bl_idname = "view3d.no_shortcut_view_op"

    mytype = None

    def execute(self, context):
        bpy.ops.view3d.viewnumpad(type=self.mytype)
        return {'FINISHED'}
    
def register():
    # create the layer_num property
    LayerSet.layer_num = set_prop("IntProperty", 
                    "bpy.types.Scene.layer_num", 
                    name="layer_num")
    
    # create the mytype property
    NoShortcutViewOp.mytype = set_prop("StringProperty", 
                    "bpy.types.Scene.mytype", 
                    name="mytype")
    
    # register all classes in the file
    bpy.utils.register_module(__name__)

def unregister():
    # set the class attribute layer_num back to None
    LayerSet.layer_num = None
    # unregister all classes in the file
    bpy.utils.unregister_module(__name__)
    
if __name__ == "__main__":
    register()
    
