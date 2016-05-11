#bl_info = {
#    "name": "Spacebar Menu_3D View",
#    "author": "marvin.k.breuer",
#    "version": (0, 1, 0),
#    "blender": (2, 7, 2),
#    "location": "View3D",
#    "description": "",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "User Menu"}


import bpy
from bpy import *

class VIEW3D_Space_3dview(bpy.types.Menu):
    bl_label = "3D View"
    bl_idname = "space_3dview"
 
    def draw(self, context):
        layout = self.layout
        view = context.space_data		
        obj = context.object
        obj_type = obj.type
        is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'})
        is_empty_image = (obj_type == 'EMPTY' and obj.empty_draw_type == 'IMAGE')		
        with_freestyle = bpy.app.build_options.freestyle
        layout.operator_context = 'INVOKE_REGION_WIN'
        mesh = context.active_object.data
        scene = context.scene

        gs = scene.game_settings
        mode_string = context.mode
        edit_object = context.edit_object
        obj = context.active_object
        
        toolsettings = context.tool_settings
       

        if view.viewport_shade == 'SOLID':
            layout.prop(view, "use_matcap")
            if view.use_matcap:
                layout.template_icon_view(view, "matcap_icon")
       
        layout.separator()
        
        layout.prop(view, "show_backface_culling")
        if obj and obj.mode == 'EDIT' and view.viewport_shade not in {'BOUNDBOX', 'WIREFRAME'}:
            layout.prop(view, "show_occlude_wire")
            
        layout.separator()            

        if view.viewport_shade == 'SOLID':               
            layout.prop(view, "show_textured_solid", text="Texture")
               
        elif view.viewport_shade == 'TEXTURED':
            if scene.render.use_shading_nodes or gs.material_mode != 'GLSL':
                layout.prop(view, "show_textured_shadeless")

        if not scene.render.use_shading_nodes:
            layout.prop(gs, "material_mode", text="")                

        layout.separator()   
                                        
        col = layout.column()
        col.prop(view, "show_only_render")

        col = layout.column()
        display_all = not view.show_only_render
        col.active = display_all
        col.prop(view, "show_outline_selected")
        col.prop(view, "show_all_objects_origin")
        col.prop(view, "show_relationship_lines")

        layout.separator()        

        col = layout.column()
        col.active = display_all
        layout.prop(view, "show_floor", text="Grid Floor")

        layout.prop(view, "show_axis_x", text="X", toggle=True)
        layout.prop(view, "show_axis_y", text="Y", toggle=True)
        layout.prop(view, "show_axis_z", text="Z", toggle=True)

        layout.separator()          

        sub = layout.column(align=True)
        sub.active = (display_all and view.show_floor)
        layout.prop(view, "grid_lines", text="Lines")
        layout.prop(view, "grid_scale", text="Scale")
        subsub = sub.column(align=True)
        subsub.active = scene.unit_settings.system == 'NONE'
        subsub.prop(view, "grid_subdivisions", text="Subdivisions")


######------------################################################################################################################
######  Registry  ################################################################################################################
######  Registry  ################################################################################################################
######------------################################################################################################################


def register():

    bpy.utils.register_class(VIEW3D_Space_3dview)    

def unregister():
  
    bpy.utils.unregister_class(VIEW3D_Space_3dview)    

if __name__ == "__main__":
    register() 	

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_Space_3dview.bl_idname)
         









