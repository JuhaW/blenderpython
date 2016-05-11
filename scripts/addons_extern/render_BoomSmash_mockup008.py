bl_info = {
    "name": "Advanced Boomsmash",
    "author": "Luciano Muñoz & Cristián Hasbún",
    "version": (0, 1),
    "blender": (2, 7, 1),
    "location": "View3D > Tools > Animation > Boomsmash",
    "description": "Have quick access for opengl previews without the need to change your render settings",
    "warning": "It's very first beta! The addon is in progress!",
    "category": "Render"}

import bpy
from bpy.props import *
#import pudb
#_MODULE_SOURCE_CODE = "BoomSmash_mockup007_b.py"

class BoomProps(bpy.types.PropertyGroup):

    #twm.image_settings = bpy.types.ImageFormatSettings(
    #                        bpy.context.scene.render.image_settings)

    incremental = BoolProperty(
        name="Incremental",
        description="Save incremental boomsmashes.")

    #scene_cam = BoolProperty(
    #    name="Active Camera",
    #    description="Always renders from the active camera that's set in the Scene properties")

    use_stamp = BoolProperty(
        name="Stamp",
        description="Turn on stamp (uses settings from render properties).",
        default=0)    
        
    transparent = BoolProperty(
        name="Transparent",
        description="Make background transparent (only for formats that support alpha, i.e.: .png).",
        default=0)
        
    autoplay = BoolProperty(
        name="Autoplay",
        description="Automatically play boomsmash after making it.",
        default=0)              
        
    unsimplify = BoolProperty(
        name="Unsimplify",
        description="Boomsmash with the subdivision surface levels at it's render settings.",
        default=0)
        
    onlyrender = BoolProperty(
        name="Only Render",
        description="Only have renderable objects visible during boomsmash.",
        default=0)
        
    frame_skip = IntProperty(
        name="Skip Frames",
        description="Number of frames to skip",
        default = 0,
        min = 0)        

    resolution_percentage = IntProperty(
        name="Resolution Percentage",
        description="define a percentage of the Render Resolution to make your boomsmash",
        default = 50,
        min = 0,
        max = 100)        

    filepath = StringProperty(
        name="File Path",
        description="Folder where your boomsmash will be stored",
        default="insert name here", #"//BoomSmash/" + bpy.context.scene.name + "####",
        subtype='FILE_PATH')  

class DoBoom(bpy.types.Operator):
    bl_idname = "bs.doboom"
    bl_label = "Boomsmash"
    bl_options ={'REGISTER'}

    def execute (self, context): 
        cs = context.scene
        rd = context.scene.render
        sd = context.space_data
        bp = context.scene.boom_props
        
        #guardo settings
        old_use_stamp = rd.use_stamp
        old_onlyrender = sd.show_only_render
        old_simplify = rd.use_simplify 
        old_filepath = rd.filepath
        old_alpha_mode = rd.alpha_mode
        #old_image_settings = rd.image_settings
        old_resolution_percentage = rd.resolution_percentage
        old_frame_step = cs.frame_step

        #afecto settings originales
        rd.use_stamp = bp.use_stamp
        sd.show_only_render = bp.onlyrender
        if bp.unsimplify:
            rd.use_simplify = False
        rd.filepath = bp.filepath
        rd.alpha_mode = 'TRANSPARENT' if bp.transparent else 'SKY'

        #rd.image_settings = bp.image_settings
        rd.resolution_percentage = bp.resolution_percentage
        context.scene.frame_step = bp.frame_skip + 1
        #view_pers = context.area.spaces[0].region_3d.view_perspective
        #if bp.scene_cam and view_pers is not 'CAMERA':
        #    bpy.ops.view3d.viewnumpad(type='CAMERA')

        #ejecuto
        bpy.ops.render.opengl(animation=True)
        if bp.autoplay:
            bpy.ops.render.play_rendered_anim()
 
        #devuelvo settings
        rd.use_stamp = old_use_stamp
        sd.show_only_render = old_onlyrender
        rd.use_simplify = old_simplify
        rd.filepath = old_filepath
        rd.alpha_mode = old_alpha_mode
        #rd.image_settings = old_image_settings
        rd.resolution_percentage = old_resolution_percentage
        context.scene.frame_step = old_frame_step
        #if bp.scene_cam and view_pers is not 'CAMERA':
        #    bpy.ops.view3d.viewnumpad(type='CAMERA')    

        return {'FINISHED'}    

def draw_boomsmash_panel(context, layout):
    col = layout.column(align=True)
    rd = context.scene.render
    bp = context.scene.boom_props
    
    split = col.split()
    subcol = split.column()
    #subcol.prop(bp, "incremental")
    subcol.prop(bp, "use_stamp")
    subcol.prop(bp, "onlyrender")
    subcol.prop(bp, "scene_cam")

    subcol = split.column()
    subcol.prop(bp, "transparent")
    subcol.prop(bp, "autoplay")
    subcol.prop(bp, "unsimplify")
    
    col.separator()
    col.label(text="Use preview range:")
    sub = col.split()
    subrow = sub.row(align=True)
    subrow.prop(context.scene, "use_preview_range", text="")
    subrow.prop(context.scene, "frame_preview_start", text="Start")
    subrow.prop(bp, "frame_skip", text="Skip")
    subrow.prop(context.scene, "frame_preview_end", text="End")
    col.separator()
    
    final_res_x = (rd.resolution_x * bp.resolution_percentage) / 100
    final_res_y = (rd.resolution_y * bp.resolution_percentage) / 100
    col.label(text="Final Resolution: {} x {}".format(str(final_res_x)[:-2], str(final_res_y)[:-2]))
    col.prop(bp, "resolution_percentage", slider=True )
    
    col.separator()
    
    #col.label(text="Output Format:")
    #col.template_image_settings(wm.image_settings, color_management=False)
    
    col.separator()
    col.prop(bp, "filepath")

    
class VIEW3D_PT_tools_animation_boomsmash(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Animation"
    bl_context = "objectmode"
    bl_label = " "
    
    def draw_header(self, context):
        DoBTN = self.layout.operator("bs.doboom", text="BoomSmash", icon='RENDER_ANIMATION')
        #DoBTN.animation = True

    def draw(self, context):
        layout = self.layout
        draw_boomsmash_panel(context, layout)


class VIEW3D_PT_tools_pose_animation_boomsmash(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Tools"
    bl_context = "posemode"
    bl_label = " "
  
    def draw_header(self, context):
        DoBTN = self.layout.operator("bs.doboom", text="BoomSmash", icon='RENDER_ANIMATION')

    def draw(self, context):
        layout = self.layout
        draw_boomsmash_panel(context, layout)
        
        
def register():
    bpy.utils.register_module(__name__)

    bpy.types.Scene.boom_props = PointerProperty(
            type=BoomProps, name="BoomSmash Properties", description="")
    


def unregister():
    bpy.utils.unregister_module(__name__)
    
    del bpy.types.Scene.boom_props



if __name__ == "__main__":
    register()
    #unregister()
    print('hecho...')
        










