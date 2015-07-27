from bpy.props import *
from bl_ui.properties_paint_common import (
        UnifiedPaintPanel)
        
from core import *
from brushes import *
from brush_options import *
from dyntopo_menu import *
from stroke_options import *
from symmetry_options import *
from texture_options import *


class PaintControlMenu(bpy.types.Menu):
    bl_label = "Paint Control"
    bl_idname = "view3d.paint_control_menu"

    @classmethod
    def poll(self, context):
        if get_mode() in [sculpt, vertex_paint, weight_paint, texture_paint, particle_edit]:
            return True
        else:
            return False
        

    def draw(self, context):
        menu = Menu(self)

        # create menu
        if get_mode() == sculpt:
            self.sculpt_control(menu, context)

        elif get_mode() == vertex_paint:
            self.vp_control(menu, context)
            
        elif get_mode() == weight_paint:
            self.wp_control(menu, context)

        elif get_mode() == texture_paint:
            self.texpaint_control(menu, context)

        else:
            self.particle_control(menu, context)
            

    def sculpt_control(self, menu, context):
        # brushes
        menu.add_item().menu(BrushOptionsMenu.bl_idname, icon='BRUSH_DATA')
        menu.add_item().menu(DynTopoMenu.bl_idname, icon="MESH_ICOSPHERE")
        menu.add_item().menu(TextureMenu.bl_idname, icon='TEXTURE')
        menu.add_item().menu(StrokeOptionsMenu.bl_idname, icon="ANIM")
        menu.add_item().menu("view3d.brush_curve_menu", icon="RNDCURVE")

        # symmetry
        menu.add_item().menu(MasterSymmetryMenu.bl_idname, icon="OUTLINER_DATA_ARMATURE")

    def vp_control(self, menu, context):
        # brushes
        menu.add_item().operator(ColorPickerPopup.bl_idname, icon="COLOR")
        
        menu.add_item().menu(BrushOptionsMenu.bl_idname, icon='BRUSH_DATA')
        menu.add_item().menu(TextureMenu.bl_idname, icon='TEXTURE')
        menu.add_item().menu(StrokeOptionsMenu.bl_idname, icon="ANIM")
        menu.add_item().menu("view3d.brush_curve_menu", icon="RNDCURVE")
        
    def wp_control(self, menu, context):
        # brushes
        menu.add_item().menu(BrushOptionsMenu.bl_idname, icon='BRUSH_DATA')
        menu.add_item().menu(StrokeOptionsMenu.bl_idname, icon="ANIM")
        menu.add_item().menu("view3d.brush_curve_menu", icon="RNDCURVE")

    def texpaint_control(self, menu, context):
        # brushes
        menu.add_item().operator(ColorPickerPopup.bl_idname, icon="COLOR")
        
        menu.add_item().menu(BrushOptionsMenu.bl_idname, icon='BRUSH_DATA')
        menu.add_item().menu(TextureMenu.bl_idname, icon='TEXTURE')
        menu.add_item().menu(StrokeOptionsMenu.bl_idname, icon="ANIM")
        menu.add_item().menu("view3d.brush_curve_menu", icon="RNDCURVE")

    def particle_control(self, menu, context):
        # brushes
        if context.tool_settings.particle_edit.tool == 'NONE':
            menu.add_item().label("No Brush Selected")
            menu.add_item().menu(BrushesMenu.bl_idname, text="Select Brush")

        else:
            menu.add_item().menu("view3d.brushes_menu")
            menu.add_item().menu(BrushRadiusMenu.bl_idname)
         
            if context.tool_settings.particle_edit.tool != 'ADD':
                menu.add_item().menu(BrushStrengthMenu.bl_idname)

            if context.tool_settings.particle_edit.tool == 'ADD':
                menu.add_item().prop(context.tool_settings.particle_edit.brush,
                                                       "count", slider=True)
                
                menu.add_item().separator()
                
                menu.add_item().prop(context.tool_settings.particle_edit,
                                                       "use_default_interpolate", toggle=True)

                if context.tool_settings.particle_edit.use_default_interpolate:
                    menu.add_item().prop(context.tool_settings.particle_edit.brush,
                                                           "steps", slider=True)
                    
                    menu.add_item().prop(context.tool_settings.particle_edit,
                                                           "default_key_count", slider=True)

            if context.tool_settings.particle_edit.tool == 'LENGTH':
                menu.add_item().separator()
                
                menu.add_item().menu("view3d.particle_length_menu")

            if context.tool_settings.particle_edit.tool == 'PUFF':
                menu.add_item().separator()
                
                menu.add_item().menu("view3d.particle_puff_menu")
                menu.add_item().prop(context.tool_settings.particle_edit.brush,
                                                       "use_puff_volume", toggle=True)
            
class ColorPickerPopup(bpy.types.Operator):
    bl_label = "Color Picker"
    bl_idname = "view3d.color_picker_popup"
    bl_options = {'REGISTER'}
    
    def draw(self, context):
        menu = Menu(self)
        
        if get_mode() == texture_paint:
            brush = context.tool_settings.image_paint.brush
            
        else:
            brush = context.tool_settings.vertex_paint.brush
        
        menu.add_item().template_color_picker(brush, "color", value_slider=True)
        menu.add_item().prop(brush, "color", text="")
        
    def execute(self, context):
        return context.window_manager.invoke_popup(self, width=180)

### ------------ New hotkeys and registration ------------ ###

addon_keymaps = []

def register():
    # register the new menus
    bpy.utils.register_module(__name__)

    # create the global hotkey
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('wm.call_menu', 'V', 'PRESS')
    kmi.properties.name = 'view3d.paint_control_menu'
    addon_keymaps.append((km, kmi))

def unregister():
    # remove keymaps when add-on is deactivated
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    # unregister the new menus
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()

