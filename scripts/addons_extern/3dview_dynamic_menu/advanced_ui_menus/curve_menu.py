from core import *

class BrushCurveMenu(bpy.types.Menu):
    bl_label = "Curve"
    bl_idname = "view3d.brush_curve_menu"

    def draw(self, context):
        menu = Menu(self)
        curves = [["Smooth", "SMOOTH", "SMOOTHCURVE"],
                         ["Sphere", "ROUND", "SPHERECURVE"],
                         ["Root","ROOT", "ROOTCURVE"],
                         ["Sharp", "SHARP", "SHARPCURVE"],
                         ["Linear", "LINE", "LINCURVE"],
                         ["Constant", "MAX", "NOCURVE"]]

        # add the top slider
        menu.add_item().operator(CurvePopup.bl_idname, icon="RNDCURVE")
        menu.add_item().separator()

        # add the rest of the menu items
        for curve in curves:
            item = menu.add_item().operator("brush.curve_preset", text=curve[0], icon=curve[2])
            item.shape = curve[1]

class CurvePopup(bpy.types.Operator):
    bl_label = "Adjust Curve"
    bl_idname = "view3d.curve_popup"
    bl_options = {'REGISTER'}
    
    def draw(self, context):
        menu = Menu(self)
        
        if get_mode() == sculpt:
            brush = context.tool_settings.sculpt.brush

        elif get_mode() == vertex_paint:
            brush = context.tool_settings.vertex_paint.brush

        elif get_mode() == weight_paint:
            brush = context.tool_settings.weight_paint.brush

        else:
            brush = context.tool_settings.image_paint.brush
        
        menu.add_item("column").template_curve_mapping(brush, "curve", brush=True)
        
    def execute(self, context):
        return context.window_manager.invoke_popup(self, width=180)

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
    
if __name__ == "__main__":
    register()
