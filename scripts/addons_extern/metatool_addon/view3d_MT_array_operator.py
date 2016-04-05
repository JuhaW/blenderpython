import bpy
from bpy import*


######################################################################################################################################################
#######-------------#################
#######  Operators  #################
#######-------------#################
######################################################################################################################################################

#####  Array  ############################################################################################
#####  Array  ############################################################################################

class loop10(bpy.types.Operator):
    """place a circle curve"""                 
    bl_idname = "object.loops10"          
    bl_label = "Circle Curve"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        #bpy.ops.view3d.snap_cursor_to_center()
        bpy.ops.curve.primitive_bezier_circle_add(radius=10, view_align=False, enter_editmode=False, location=(0, 0, 0))
        bpy.context.object.name = "Circle Curve Array"
        return {'FINISHED'}  
    

class loop11(bpy.types.Operator):
    """place a Array & Curve modifier to selected object"""                 
    bl_idname = "object.loops11"          
    bl_label = "Circle Curve & Array"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.ops.object.modifier_add(type='ARRAY')
        bpy.context.object.modifiers["Array"].fit_type = 'FIT_CURVE'
        bpy.context.object.modifiers["Array"].curve = bpy.data.objects["Circle Curve Array"]
     
        bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 5 
        bpy.ops.object.modifier_add(type='CURVE')
        bpy.context.object.modifiers["Curve"].object = bpy.data.objects["Circle Curve Array"]        
        return {'FINISHED'}   
       

class loop12(bpy.types.Operator):
    """place a path curve"""                 
    bl_idname = "object.loops12"          
    bl_label = "Path Curve & Array"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        #bpy.ops.view3d.snap_cursor_to_center()
        bpy.ops.curve.primitive_bezier_curve_add(radius=10)
        bpy.context.object.name = "Path Curve Array"        
        return {'FINISHED'}


class loop13(bpy.types.Operator):
    """place a Array & Curve modifier to selected object"""                 
    bl_idname = "object.loops13"          
    bl_label = "Path Curve Array"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.ops.object.modifier_add(type='ARRAY')
        bpy.context.object.modifiers["Array"].fit_type = 'FIT_CURVE'
        bpy.context.object.modifiers["Array"].curve = bpy.data.objects["Path Curve Array"]
     
        bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 1
        bpy.ops.object.modifier_add(type='CURVE')
        bpy.context.object.modifiers["Curve"].object = bpy.data.objects["Path Curve Array"]  
        return {'FINISHED'}         

      
class loops14(bpy.types.Operator):
    """place a curve for follow path"""                 
    bl_idname = "object.loops14"          
    bl_label = "Follow Path Curve"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.ops.curve.primitive_bezier_circle_add(radius=10, view_align=False, enter_editmode=False, location=(0, 0, 0))
        bpy.context.object.name = "Follow Path Curve"
        return {'FINISHED'}  
         

class loops15(bpy.types.Operator):
    """place a follow path constraint"""                 
    bl_idname = "object.loops15"          
    bl_label = "Follow Path Constraint"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
     
        bpy.ops.object.constraint_add(type='FOLLOW_PATH')
        bpy.context.object.constraints["Follow Path"].target = bpy.data.objects["Follow Path Curve"]
        bpy.context.object.constraints["Follow Path"].use_curve_follow = True
        bpy.context.object.constraints["Follow Path"].forward_axis = 'FORWARD_X'
        return {'FINISHED'}                      
    

class loops16(bpy.types.Operator):
    """linked object from constraint"""                 
    bl_idname = "object.loops16"          
    bl_label = "linked object from constraint"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        
        bpy.ops.object.select_linked(type='OBDATA')     
        bpy.ops.object.visual_transform_apply()
        bpy.ops.object.constraints_clear()
        #bpy.ops.object.make_single_user(type='ALL', object=True, obdata=True)
        return {'FINISHED'}  


class loops17(bpy.types.Operator):
    """single objects & data from constraint"""                 
    bl_idname = "object.loops17"          
    bl_label = "single objects & data from constraint"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        
        bpy.ops.object.select_linked(type='OBDATA')     
        bpy.ops.object.visual_transform_apply()
        bpy.ops.object.constraints_clear()
        bpy.ops.object.make_single_user(type='ALL', object=True, obdata=True)        
        return {'FINISHED'}  



#####  Grid Array  #############################################################################################
#####  Grid Array  #############################################################################################

class addArray2(bpy.types.Operator):
    """add 2 array modifier"""
    bl_label = "2 Array Modifier"
    bl_idname = "object.add_2array"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0
           
    def execute(self, context):
               
        for obj in bpy.context.selected_objects:
	        
            bpy.context.scene.objects.active = obj
            
            bpy.ops.object.modifier_add(type='ARRAY')
            bpy.context.object.modifiers["Array"].count = 3
            bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 1.5
            
            bpy.ops.object.modifier_add(type='ARRAY')
            bpy.context.object.modifiers["Array.001"].count = 3
            bpy.context.object.modifiers["Array.001"].relative_offset_displace[0] = 0
            bpy.context.object.modifiers["Array.001"].relative_offset_displace[1] = 1.5
        
        return {"FINISHED"}


class addArray3(bpy.types.Operator):
    """add 3 array modifier"""
    bl_label = "3 Array Modifier"
    bl_idname = "object.add_3array"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0
    
    def execute(self, context):
               
        for obj in bpy.context.selected_objects:
	        
            bpy.context.scene.objects.active = obj
            
            bpy.ops.object.modifier_add(type='ARRAY')
            bpy.context.object.modifiers["Array"].count = 3
            bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 1.5
            
            bpy.ops.object.modifier_add(type='ARRAY')
            bpy.context.object.modifiers["Array.001"].count = 3
            bpy.context.object.modifiers["Array.001"].relative_offset_displace[0] = 0
            bpy.context.object.modifiers["Array.001"].relative_offset_displace[1] = 1.5
            
            bpy.ops.object.modifier_add(type='ARRAY')
            bpy.context.object.modifiers["Array.002"].count = 3
            bpy.context.object.modifiers["Array.002"].relative_offset_displace[0] = 0
            bpy.context.object.modifiers["Array.002"].relative_offset_displace[2] = 1.5            
                
        return {"FINISHED"}
    
#######  Mirror Full activ  #######-------------------------------------------------------                  
#######  Mirror Full activ  #######-------------------------------------------------------                  

class FullMIRROR(bpy.types.Operator):
    """Add a x mirror modifier"""
    bl_idname = "view3d.fullmirror"
    bl_label = "Mirror X"

    def execute(self, context):
    
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.ops.view3d.display_modifiers_cage_on()
        bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}
    
bpy.utils.register_class(FullMIRROR) 

class FullMIRRORY(bpy.types.Operator):
    """Add a y mirror modifier"""
    bl_idname = "view3d.fullmirrory"
    bl_label = "Mirror Y"

    def execute(self, context):
    
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_x = False
        bpy.context.object.modifiers["Mirror"].use_y = True
        bpy.ops.view3d.display_modifiers_cage_on()
        bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}
    
bpy.utils.register_class(FullMIRRORY) 


class FullMIRRORZ(bpy.types.Operator):
    """Add a z mirror modifier"""
    bl_idname = "view3d.fullmirrorz"
    bl_label = "Mirror Z"

    def execute(self, context):
    
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_x = False
        bpy.context.object.modifiers["Mirror"].use_z = True        
        bpy.ops.view3d.display_modifiers_cage_on()
        bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}   

bpy.utils.register_class(FullMIRRORZ) 

######################################################################################################################################################
############------------############
############  REGISTER  ############
############------------############
######################################################################################################################################################

    
def register():
    bpy.utils.register_module(__name__)
 
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()


  



