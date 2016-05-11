bl_info = {
    "name": "Right step",
    "category": "Animation",
    "blender": (2, 76),
    "author": "Lenster (lenster-3d@ya.ru)",
    "description": "Add objects for create fixed step(fix bone with IK) in space. Ctrl-shift-R",
    "location": "View3D > Pose > Right step",
    "version": (1, 0, 2)
}

import bpy, re, mathutils, math, threading
from bpy import context
from math import radians
from bpy.props import (
        FloatVectorProperty,
        )

class AnimRightStep(bpy.types.Operator):
        
    """Right Step"""
    bl_idname = "anim.right_step"
    bl_label = "Right step"
    bl_options = {'REGISTER', 'UNDO'}
    bl_region_type = 'WINDOW'
    bl_context = "scene" 
  
    X = bpy.props.BoolProperty(name="X rotate", default=False) 
    X_inv = bpy.props.BoolProperty(name="Inverse", default=False)
    Y = bpy.props.BoolProperty(name="Y rotate", default=False) 
    Y_inv = bpy.props.BoolProperty(name="Inverse", default=False)
    Z = bpy.props.BoolProperty(name="Z rotate", default=False) 
    Z_inv = bpy.props.BoolProperty(name="Inverse", default=False)
    
    zHeight = bpy.props.IntProperty(name="Height", default=30, min=-300, max=300)
    xLength = bpy.props.IntProperty(name="Length", default=10, min=3, max=150)
    yWidth = bpy.props.IntProperty(name="Width", default=0, min=-3, max=100)
    xHeel = bpy.props.IntProperty(name="Heel", default=0, min=-5, max=30)
    R = bpy.props.IntProperty(name="R", default=0, min=-1, max=1)
    
    Mat_number = bpy.props.IntProperty(name="Material", default=1, min=1, max=100)
    
    Input = bpy.props.IntProperty(name="Input frame", default=3, min=1, max=100, description="Count of frame from 0 to 1 influence")
    Frame = bpy.props.IntProperty(name="Frame", default=10, min=1, max=100, description="Count of frame from 0 to 1 influence")
    Output = bpy.props.IntProperty(name="Output frame", default=1, min=1, max=100, description="Count of frame from 0 to 1 influence")
        
    CustomColor = bpy.props.FloatVectorProperty( 
    name="Color", 
    description="Color value", 
    default = (1.0, 0.0, 0.0),
    subtype='COLOR', min=0.0, max=1.0,
    )

    def draw(self, context):
        layout = self.layout
        
        scene = context.scene

        row = layout.row(align=True)
        row.prop(self, 'X')
        row.prop(self, 'X_inv')
        row = layout.row(align=True)
        row.prop(self, 'Y')
        row.prop(self, 'Y_inv')
        row = layout.row(align=True)
        row.prop(self, 'Z')
        row.prop(self, 'Z_inv')     
         
        
        col = layout.column(align=True)
        row = col.row()
        row.prop(self, 'CustomColor')  
        row = col.row()
        box = layout.box()
        
        box.prop(self, 'zHeight')
        box.prop(self, 'xLength')
        box.prop(self, 'yWidth')
        box.prop(self, 'xHeel')
        
        box.prop(self, 'Mat_number')
        
        
        row = layout.row(align=True)
        row.prop(self, 'Input')
        row.prop(self, 'Frame')
        row.prop(self, 'Output')
        
        
    
    def execute(self, context):
        if context.active_object.mode == 'POSE' and context.active_object.type == 'ARMATURE' and bpy.context.selected_pose_bones: 
            scene = context.scene
            frame = scene.frame_current
            bone = bpy.context.active_pose_bone # bpy.context.selected_pose_bones[0]
            armature = context.scene.objects.active 

# Create 4 objects
            x1 = (self.xHeel/100)
            z = -(self.zHeight/1000)
            x2 = (self.xLength/300)
            y = (self.yWidth/100)    

            verts=[(0, -y * 0.18 - 0.01, 0), (x2 - 0.004 + x1, -y * 0.18 - 0.01, 0),
                    (x2 - 0.004 + x1, y * 0.18 + 0.01, 0), (0, y * 0.18 + 0.01, 0)]
            faces=[(0,1,2,3)]
            me = bpy.data.meshes.new("HeelMesh.0")  
            ob = bpy.data.objects.new("Heel.0", me) 
            bpy.context.scene.objects.link(ob)        
            me.from_pydata(verts,[],faces)    
            me.update(calc_edges=True)     
                        
            me_empty = bpy.data.meshes.new("Empty_vertex_mesh")  
            ob_empty = bpy.data.objects.new("Empty_vertex", me_empty)           
            bpy.context.scene.objects.link(ob_empty)      

            me1 = bpy.data.meshes.new("PointMesh.0")  
            ob1 = bpy.data.objects.new("Point.0", me1)           
            bpy.context.scene.objects.link(ob1)    
            
            verts2=[(-x2 + 0.007, -y * 0.1 - 0.01, 0), (0, -y * 0.1 - 0.01, 0),
                    (0, y * 0.1 + 0.01, 0), (-x2 + 0.007, y * 0.1 + 0.01, 0),
                    (y * 0.2 + 0.027, 0, 0), (0, -y * 0.1 - 0.022, 0), (0, y * 0.1 + 0.022, 0)]
            faces2=[(0,1,2,3), (2,4,6), (1,4,5), (1,2,4)]
            me2 = bpy.data.meshes.new("ToeMesh.0")         
            ob2 = bpy.data.objects.new("Toe.0", me2)      
            bpy.context.scene.objects.link(ob2)               
            me2.from_pydata(verts2,[],faces2) 
            
# Recalculation normals (Toe - obj)                   
            bpy.ops.object.mode_set(mode="OBJECT")  
            armat = bpy.context.scene.objects.active
            bpy.context.scene.objects.active = ob2
            ob2.select = True
            armat.select = False    
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.normals_make_consistent(inside=False)
            me2.update(calc_edges=True)  
            ob2.select = False  
            bpy.ops.object.mode_set(mode="OBJECT")  

# Renaming   
            const_name = None
            i = 0    
            all = None
            list = 'a'
            list2 = 'a'
            number = 0
            exp = re.compile("Heel.\d")
            for all in bpy.data.objects:
                if exp.search(all.name):
                    list = list + all.name

            value = "".join(list)
            result = re.split("\D+", value)
            
            input = result
            output = [int(x) for x in input if x]
            for i in output:
                if i > number:
                    number = i
    
            ob.name = ("Heel."+str(number))
            me.name = ("Heel_mesh."+str(number))
            ob1.name = ("Point."+str(number))
            me1.name = ("Point_mesh."+str(number))
            ob2.name = ("Toe."+str(number))
            me2.name = ("Toe_mesh."+str(number))
            const_name = ("Step."+str(number))
            bpy.data.objects["Toe."+str(number)].hide_render = True
            bpy.data.objects["Point."+str(number)].hide_render = True
            bpy.data.objects["Heel."+str(number)].hide_render = True
#Create group   
            Group = None   
            ob.select = True
            ob1.select = True
            ob2.select = True
            group_exist = False
            x = 0      
            for x in bpy.data.groups:
                if x.name == "GroupOfSteps":
                    group_exist = True
                    break
            if group_exist:
                bpy.context.scene.objects.active = ob
                bpy.ops.object.group_link(group='GroupOfSteps')
                bpy.context.scene.objects.active = ob1
                bpy.ops.object.group_link(group='GroupOfSteps')
                bpy.context.scene.objects.active = ob2 
                bpy.ops.object.group_link(group='GroupOfSteps')         
                bpy.context.scene.objects.active = armat
            else:
                bpy.ops.group.create(name="GroupOfSteps")
                
            bpy.context.scene.objects.active = armat        
            armat.select = True
            ob_empty.select = False
            ob.select = False
            ob1.select = False
            ob2.select = False
            bpy.ops.object.mode_set(mode="POSE")
            
# Check material
            mat_exist = False      
            Col = bpy.context.scene.objects.active 
            for m in bpy.data.materials:
                if m.name == 'Step' + str(self.Mat_number):
                    mat_exist = True
                    break                 
            if mat_exist:
                ob.data.materials.append(m)
                ob1.data.materials.append(m)
                ob2.data.materials.append(m)
                ob.active_material.diffuse_color = (self.CustomColor.r, self.CustomColor.g, self.CustomColor.b) 
            else:
                mat = bpy.data.materials.new('Step' + str(self.Mat_number))
                ob.data.materials.append(mat)
                ob1.data.materials.append(mat)
                ob2.data.materials.append(mat)
                ob.active_material.diffuse_color = (self.CustomColor.r, self.CustomColor.g, self.CustomColor.b)    
 
#add parents and copying transformation from bone + creating opportunity to move origin.
            ob.matrix_world = mathutils.Matrix.Translation((-x1, 0, z))
            ob1.matrix_world = mathutils.Matrix.Translation((-x2 * 2, 0, -z))
            ob2.matrix_world = mathutils.Matrix.Translation((x2 * 2 + x1, 0, 0))
            ob.parent = ob_empty
            ob2.parent = ob 
            pose_bone = bone.id_data
            matrix_final = pose_bone.matrix_world * bone.matrix
            ob_empty.matrix_world = matrix_final
            ob1.matrix_world = matrix_final
                     
# rotate,rotate confuse want to create
            if self.X and not self.X_inv:
                xR = 90 
                bpy.context.object.parent = None

            elif self.X and self.X_inv: 
                xR = -90
            else:
                xR = 0            
                
            if self.Y and not self.Y_inv:
                yR = 90 
            elif self.Y and self.Y_inv: 
                yR = -90
            else:
                yR = 0              
                
            if self.Z and not self.Z_inv:
                zR = 90
            elif self.Z and self.Z_inv:
                zR = -90
            else:
                zR = 0             

            ob_empty.matrix_world = ob_empty.matrix_world * mathutils.Matrix.Rotation(math.radians(xR), 4, 'X')
            ob_empty.matrix_world = ob_empty.matrix_world * mathutils.Matrix.Rotation(math.radians(yR), 4, 'Y')
            ob_empty.matrix_world = ob_empty.matrix_world * mathutils.Matrix.Rotation(math.radians(zR), 4, 'Z')            
            
# Delete ob_empty     
            armat.select = False
            ob_empty.select = False
            ob.select = True
            ob1.select = False
            ob2.select = False
            bpy.context.scene.objects.active = ob
            bpy.ops.object.mode_set(mode='OBJECT') 
            bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM') 
            ob.select = False
            bpy.context.scene.objects.active = ob_empty
            ob_empty.select = True
            bpy.ops.object.delete(use_global=False)
                    
# Add constraint and anim.key
            bpy.context.scene.objects.active = armat
            armat.select = True
            bpy.ops.object.mode_set(mode='POSE') 
            const = bone.constraints.new('COPY_TRANSFORMS')
            const.name = const_name
            const.target = ob1
            const.show_expanded = False
            const.influence = 0 
            const.keyframe_insert(data_path="influence", frame=frame-self.Input)
            const.influence = 1
            const.keyframe_insert(data_path="influence", frame=frame)
            const.influence = 1
            const.keyframe_insert(data_path="influence", frame=frame+self.Frame)
            const.influence = 0
            const.keyframe_insert(data_path="influence", frame=frame+self.Frame+self.Output)
            
# Creatung last link - point with heel.   
            bpy.context.scene.objects.active = ob2
            armat.select = False
            ob1.select = True
            ob2.select = True
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
            bpy.context.scene.objects.active = armat
            ob1.select = False
            ob2.select = False
            armat.select = True
            
            scene.frame_current = frame
        else: 
            self.report({'ERROR'}, "Choose the bone")
        return {'FINISHED'}
    
class Create_button(bpy.types.Panel):
    bl_label = "Right step"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'}
  
    def draw(self, context):
        layout = self.layout
        row = layout.row(align = True)
        row.scale_x = 1.0
        row.operator("anim.right_step", text="Create")
    
def menu_func(self, context):
    self.layout.operator(AnimRightStep.bl_idname)

addon_keymaps = []

def register():
    bpy.utils.register_class(AnimRightStep)
    bpy.utils.register_class(Create_button)
    bpy.types.VIEW3D_MT_pose.append(menu_func)
    
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Pose', space_type='EMPTY')
    kmi = km.keymap_items.new(AnimRightStep.bl_idname, 'R', 'PRESS', ctrl=True, shift=True)
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(AnimRightStep)
    bpy.utils.unregister_class(Create_button)
    bpy.types.VIEW3D_MT_pose.remove(menu_func)

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()

 
 