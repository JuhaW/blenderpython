from core import *

# adds a pivot point menu
class ViewMenu(bpy.types.Menu):
    bl_label = "View"
    bl_idname = "view3d.view_menu"

    def draw(self, context):
        menu = Menu(self)
        view_modes = [["Front", 'FRONT'],
                                    ["Right", "RIGHT"],
                                    ["Top", "TOP"],
                                    ["Camera", "CAMERA"],
                                    ["Back", "BACK"],
                                    ["Left", "LEFT"],
                                    ["Bottom", "BOTTOM"]]

        column_flow = menu.add_item("column_flow", columns=2)
        
        # add the menu items
        for mode in view_modes:
            prop = menu.add_item(parent=column_flow).operator(
                "view3d.no_shortcut_view_op", mode[0])
            prop.mytype = mode[1]
            
            # disable the rows that need it
            #if mode[1] == get_view_mode():
                #menu.current_item.enabled = False

        menu.add_item(parent=column_flow).menu(OtherViewMenu.bl_idname)
        
        column_flow.alignment = 'LEFT'


class OtherViewMenu(bpy.types.Menu):
    bl_label = "Other"
    bl_idname = "view3d.other_view_menu"

    def draw(self, context):
        menu = Menu(self)

        menu.add_item().operator("view3d.view_selected")
        menu.add_item().operator("view3d.localview", "View Local/Global")
        menu.add_item().operator("view3d.view_persportho")
        menu.add_item().operator("screen.region_quadview")

        menu.add_item().separator()

        menu.add_item().prop(context.space_data, "lock_cursor", toggle=True)
        menu.add_item().prop(context.space_data, "lock_camera", toggle=True)

        menu.add_item().separator()

        menu.add_item().menu(LayersMenu.bl_idname)


class LayersMenu(bpy.types.Menu):
    bl_label = "Layers"
    bl_idname = "view3d.layers_menu"

    def draw(self, context):
        menu = Menu(self)
        
        column_flow = menu.add_item("column_flow", columns=2)
        
        # if the layer management addon is enabled name the layers with the layer names
        try:
            order = [context.scene.LayerName1, 
                            context.scene.LayerName2, 
                            context.scene.LayerName3, 
                            context.scene.LayerName4, 
                            context.scene.LayerName5, 
                            context.scene.LayerName6, 
                            context.scene.LayerName7, 
                            context.scene.LayerName8, 
                            context.scene.LayerName9, 
                            context.scene.LayerName10, 
                            context.scene.LayerName11, 
                            context.scene.LayerName12, 
                            context.scene.LayerName13, 
                            context.scene.LayerName14, 
                            context.scene.LayerName15, 
                            context.scene.LayerName16, 
                            context.scene.LayerName17, 
                            context.scene.LayerName18, 
                            context.scene.LayerName19, 
                            context.scene.LayerName20]
            # if the name has "layer" in front of a number remove "layer" and leave the number
            for name in enumerate(order, start=1):
                if name[1] == "layer{}".format(name[0]):
                    order[name[0] - 1 ] = name[0]
            
        # if not then name the layers with numbers
        except:
            order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        
        # add the menu items
        for num in range(20):
            if num == context.scene.active_layer:
                prop = menu.add_item(parent=column_flow).operator("view3d.layer_set", "{}".format(order[num]), icon='FILE_TICK')
                
            elif context.space_data.layers[num]:
                prop = menu.add_item(parent=column_flow).operator("view3d.layer_set", "{}".format(order[num]), icon='RESTRICT_VIEW_OFF')
                
            else:
                prop = menu.add_item(parent=column_flow).operator("view3d.layer_set", "{}".format(order[num]))
            
            menu.current_item.operator_context = 'EXEC_DEFAULT'
            prop.layer_num = num

        column_flow.scale_y = 0.7
        

### ------------ New hotkeys and registration ------------ ###

addon_keymaps = []

def register():
    # register all classes in the file
    bpy.utils.register_module(__name__)


    # create the global menu hotkey
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('wm.call_menu', 'Q', 'PRESS')
    kmi.properties.name = 'view3d.view_menu'
    addon_keymaps.append((km, kmi))


def unregister():
    # remove keymaps when add-on is deactivated
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    # unregister all classes in the file
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
