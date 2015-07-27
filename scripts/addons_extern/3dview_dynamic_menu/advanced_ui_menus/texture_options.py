from bpy.props import *
from core import *

class TextureMenu(bpy.types.Menu):
    bl_label = "Texture Options"
    bl_idname = "view3d.texture_menu"

    def draw(self, context):
        menu = Menu(self)

        if get_mode() == sculpt:
            self.sculpt(menu, context)
            
        elif get_mode() == vertex_paint:
            self.vertpaint(menu, context)
            
        else:
            self.texpaint(menu, context)

    def sculpt(self, menu, context):
        menu.add_item().menu(Textures.bl_idname)
        menu.add_item().menu(TextureMapMode.bl_idname)
        if context.tool_settings.sculpt.brush.texture_slot.map_mode != '3D':
            if context.tool_settings.sculpt.brush.texture_slot.map_mode in ['RANDOM', 'VIEW_PLANE', 'AREA_PLANE']:
                menu.add_item().menu(TextureAngleSource.bl_idname)

            menu.add_item().prop(context.tool_settings.sculpt.brush.texture_slot, "angle", slider=True)

    def vertpaint(self, menu, context):
        menu.add_item().menu(Textures.bl_idname)
        menu.add_item().menu(TextureMapMode.bl_idname)

        if context.tool_settings.vertex_paint.brush.texture_slot.tex_paint_map_mode != '3D':
            if context.tool_settings.vertex_paint.brush.texture_slot.tex_paint_map_mode in ['RANDOM', 'VIEW_PLANE']:
                menu.add_item().menu(TextureAngleSource.bl_idname)

            menu.add_item().prop(context.tool_settings.vertex_paint.brush.texture_slot, "angle", slider=True)

    def texpaint(self, menu, context):
        menu.add_item().label(text="Texture")
        
        menu.add_item().separator()
        
        menu.add_item().menu(Textures.bl_idname)
        menu.add_item().menu(TextureMapMode.bl_idname)

        if context.tool_settings.image_paint.brush.texture_slot.tex_paint_map_mode != '3D':
            if context.tool_settings.image_paint.brush.texture_slot.tex_paint_map_mode in ['RANDOM', 'VIEW_PLANE']:
                menu.add_item().menu(TextureAngleSource.bl_idname)

            menu.add_item().prop(context.tool_settings.image_paint.brush.texture_slot, "angle", slider=True)
        
        menu.add_item().separator()

        menu.add_item().label(text="Texture Mask")
        
        menu.add_item().separator()

        menu.add_item().menu(MaskTextures.bl_idname)
        menu.add_item().menu(MaskMapMode.bl_idname)
        menu.add_item().prop(context.tool_settings.image_paint.brush.mask_texture_slot, "angle", slider=True)

class Textures(bpy.types.Menu):
    bl_label = "Textures"
    bl_idname = "view3d.texture_list"

    def init(self):
        if get_mode() == sculpt:
            datapath = "tool_settings.sculpt.brush.texture"

        elif get_mode() == vertex_paint:
            datapath = "tool_settings.vertex_paint.brush.texture"

        elif get_mode() == texture_paint:
            datapath = "tool_settings.image_paint.brush.texture"

        else:
            datapath = ""

        return datapath

    def draw(self, context):
        datapath = self.init()
        menu = Menu(self)
        current_texture = eval("bpy.context.{}".format(datapath))
        
        # get the current texture's name
        if current_texture:
            current_texture = current_texture.name
        
        # add an item to set the texture to None
        menuprop(menu.add_item(), "None", "None",
                datapath, icon='RADIOBUT_OFF', disable=True, 
                disable_icon='RADIOBUT_ON',
                custom_disable_exp=[None, current_texture],
                path=True)
        
        # add the menu items
        for item in bpy.data.textures:
            menuprop(menu.add_item(), item.name, 'bpy.data.textures["%s"]' % item.name,
                datapath, icon='RADIOBUT_OFF', disable=True, 
                disable_icon='RADIOBUT_ON',
                custom_disable_exp=[item.name, current_texture],
                path=True)
            
class TextureMapMode(bpy.types.Menu):
    bl_label = "Brush Mapping"
    bl_idname = "view3d.texture_map_mode"
    
    def draw(self, context):
        menu = Menu(self)
        
        if get_mode() == sculpt:
            path = "tool_settings.sculpt.brush.texture_slot.map_mode"
            items = [["View Plane", 'VIEW_PLANE'],
                            ["Area Plane", 'AREA_PLANE'],
                            ["Tiled", 'TILED'],
                            ["3D", '3D'],
                            ["Random", 'RANDOM'],
                            ["Stencil", 'STENCIL']]
            
            # add the menu items
            for item in items:
                menuprop(menu.add_item(), item[0], 
                               item[1], path, icon='RADIOBUT_OFF', disable=True, 
                     disable_icon='RADIOBUT_ON')
                
        elif get_mode() == vertex_paint:
            path = "tool_settings.vertex_paint.brush.texture_slot.tex_paint_map_mode"
            items = [["View Plane", 'VIEW_PLANE'],
                           ["Tiled", 'TILED'],
                           ["3D", '3D'],
                           ["Random", 'RANDOM'],
                           ["Stencil", 'STENCIL']]
            
            # add the menu items
            for item in items:
                menuprop(menu.add_item(), item[0], 
                               item[1], path, icon='RADIOBUT_OFF', disable=True, 
                     disable_icon='RADIOBUT_ON')
                
        else:
            path = "tool_settings.image_paint.brush.texture_slot.tex_paint_map_mode"
            items = [["View Plane", 'VIEW_PLANE'],
                           ["Tiled", 'TILED'],
                           ["3D", '3D'],
                           ["Random", 'RANDOM'],
                           ["Stencil", 'STENCIL']]
            
            # add the menu items
            for item in items:
                menuprop(menu.add_item(), item[0], 
                               item[1], path, icon='RADIOBUT_OFF', disable=True, 
                     disable_icon='RADIOBUT_ON')
                
class TextureAngleSource(bpy.types.Menu):
    bl_label = "Texture Angle Source"
    bl_idname = "view3d.texture_angle_source"
    
    def draw(self, context):
        menu = Menu(self)
        items = [["User", 'USER'],
                        ["Rake", 'RAKE'],
                        ["Random", 'RANDOM']]

        if get_mode() == sculpt:
            path = "tool_settings.sculpt.brush.texture_angle_source_random"
            
        elif get_mode() == vertex_paint:
            path = "tool_settings.vertex_paint.brush.texture_angle_source_random"
            
        else:
            path = "tool_settings.image_paint.brush.texture_angle_source_random"
        
        # add the menu items
        for item in items:
            menuprop(menu.add_item(), item[0], 
                              item[1], path, icon='RADIOBUT_OFF', disable=True, 
                     disable_icon='RADIOBUT_ON')
            
class MaskTextures(bpy.types.Menu):
    bl_label = "Textures"
    bl_idname = "view3d.mask_texture_list"

    def draw(self, context):
        menu = Menu(self)
        datapath = "tool_settings.image_paint.brush.mask_texture"
        current_texture = eval("bpy.context.{}".format(datapath))
        
        # get the current texture's name
        if current_texture:
            current_texture = current_texture.name

        # add an item to set the texture to None
        menuprop(menu.add_item(), "None", "None",
                datapath, icon='RADIOBUT_OFF', disable=True, 
                disable_icon='RADIOBUT_ON',
                custom_disable_exp=[None, current_texture],
                path=True)
        
        # add the menu items
        for item in bpy.data.textures:
            menuprop(menu.add_item(), item.name, 'bpy.data.textures["%s"]' % item.name,
                datapath, icon='RADIOBUT_OFF', disable=True, 
                disable_icon='RADIOBUT_ON',
                custom_disable_exp=[item.name, current_texture],
                path=True)
            
class MaskMapMode(bpy.types.Menu):
    bl_label = "Mask Mapping"
    bl_idname = "view3d.mask_map_mode"
    
    def draw(self, context):
        menu = Menu(self)

        path = "tool_settings.vertex_paint.brush.texture_slot.mask_map_mode"
        items = [["View Plane", 'VIEW_PLANE'],
                        ["Tiled", 'TILED'],
                        ["3D", '3D'],
                        ["Random", 'RANDOM'],
                        ["Stencil", 'STENCIL']]
        
        # add the menu items
        for item in items:
            menuprop(menu.add_item(), item[0], 
                             item[1], path, icon='RADIOBUT_OFF', disable=True, 
                     disable_icon='RADIOBUT_ON')

def register():
    # register all classes in the file
    bpy.utils.register_module(__name__)

def unregister():
    # unregister all classes in the file
    bpy.utils.unregister_module(__name__)
    
if __name__ == "__main__":
    register()
