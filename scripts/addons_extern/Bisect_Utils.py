bl_info = {
    "name" : "Bisect utils",
    "description": "A menu for quickly applying bisect along anchor of the object within 6 different directions",
    "author" : "Smoke Fumus <smokethehedgehog@gmail.com>",
    "version": (0,1),
    "blender": (2,74,0),
    "location": "Object > Bisect Utils",
    "warning": "",
    "wiki_url": "none yet",
    "category": "Object",
}



import bpy

from mathutils import Vector, Matrix, Quaternion, Euler, Color

class BisectUtilMenu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_object_Menu"
    bl_label = "Bisect Utils"

    def draw(self, ctx):

        layout = self.layout


        props = layout.operator(BisectUtils.bl_idname, text="Y-")
        props.planevector=Vector((0.0,1.0,0.0))
        props.clearinner=True
        props.clearoutter=False #operator should compute fresh value

        props = layout.operator(BisectUtils.bl_idname, text="Y+")
        props.planevector=Vector((0.0,1.0,0.0))
        props.clearinner=False
        props.clearoutter=True

        props = layout.operator(BisectUtils.bl_idname, text="X-")
        props.planevector=Vector((1.0,0.0,0.0))
        props.clearinner=True
        props.clearoutter=False


        props = layout.operator(BisectUtils.bl_idname, text="X+")
        props.planevector=Vector((1.0,0.0,0.0))
        props.clearinner=False
        props.clearoutter=True


        props = layout.operator(BisectUtils.bl_idname, text="Z-")
        props.planevector=Vector((0.0,0.0,1.0))
        props.clearinner=True
        props.clearoutter=False


        props = layout.operator(BisectUtils.bl_idname, text="Z+")
        props.planevector=Vector((0.0,0.0,1.0))
        props.clearinner=False
        props.clearoutter=True


  
class BisectUtils(bpy.types.Operator):  
    bl_idname = "object.bisect_utils"  
    bl_label = "Bisect Util"  
    bl_options = {'REGISTER', 'UNDO'}
    clearinner=bpy.props.BoolProperty(name="Clear Inner", description="Clear Inner", default=False)
    clearoutter=bpy.props.BoolProperty(name="Clear Outer", description="Clear Outer", default=False)
    planevector=bpy.props.FloatVectorProperty(name="Plane Normal", description="Plane Normal", default=Vector((0.0,0.0,0.0)))
    
    def execute(self, context):
        if bpy.context.mode == 'OBJECT' and len(bpy.context.selected_objects)>0 :  
            bpy.ops.object.editmode_toggle()
            mesh=context.active_object.data
            for v in mesh.vertices:
                v.select = True
            
            bpy.ops.mesh.bisect(clear_outer=self.clearoutter, xstart=0, clear_inner=self.clearinner, cursor=1002, yend=1, use_fill=False, ystart=114, plane_no=self.planevector, plane_co=context.active_object.location, threshold=9.999999747378752e-05, xend=264)
            bpy.ops.object.editmode_toggle()
            return {'FINISHED'}
        else:
            return {'CANCELLED'}  
  
def menu_func(self, ctx):
    self.layout.menu(BisectUtilMenu.bl_idname)  
  
def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_object.append(menu_func)  
  
def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    bpy.utils.unregister_module(__name__) 
  
if __name__ == "__main__":
    try:
        unregister()
    except:
        pass
    register()