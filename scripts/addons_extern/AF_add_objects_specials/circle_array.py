# -*- coding: utf-8 -*-

bl_info = {  
     "name": "Circle Array",  
     "author": "Antonis Karvelas",  
     "version": (1, 0),  
     "blender": (2, 6, 7),  
     "location": "View3D > Object > Circle_Array",  
     "description": "Uses an existing array and creates an empty,rotates it properly and makes a Circle Array ",  
     "warning": "You must have an object and an array, or two objects, with only the first having an array",  
     "wiki_url": "",  
     "tracker_url": "",  
     "category": "Mesh"}  


import bpy
from math import radians

class Circle_Array(bpy.types.Operator):
    bl_label = "Circle Array"
    bl_idname = "objects.circle_array_operator"
    bl_description = 'Add Array Mod First'             
    def execute(self, context):
        bpy.ops.object.modifier_add(type='ARRAY')
                
        if len(bpy.context.selected_objects) == 2:
            list = bpy.context.selected_objects
            active = list[0]
            active.modifiers[0].use_object_offset = True 
            active.modifiers[0].use_relative_offset = False
            active.select = False
            bpy.context.scene.objects.active = list[0]
            bpy.ops.view3d.snap_cursor_to_selected()
            if active.modifiers[0].offset_object == None:
                bpy.ops.object.add(type='EMPTY')
                empty_name = bpy.context.active_object
                empty_name.name = "EMPTY"
                active.modifiers[0].offset_object = empty_name
            else:
                empty_name = active.modifiers[0].offset_object                
            bpy.context.scene.objects.active = active            
            num = active.modifiers["Array"].count
            print(num)
            rotate_num = 360 / num
            print(rotate_num)
            active.select = True
            bpy.ops.object.transform_apply(location = False, rotation = True, scale = True) 
            empty_name.rotation_euler = (0, 0, radians(rotate_num))
            empty_name.select = False
            active.select = True
            bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
            return {'FINISHED'}     
        
        
        else:
            active = context.active_object
            active.modifiers[0].use_object_offset = True 
            active.modifiers[0].use_relative_offset = False
            bpy.ops.view3d.snap_cursor_to_selected()
            if active.modifiers[0].offset_object == None:
                bpy.ops.object.add(type='EMPTY')
                empty_name = bpy.context.active_object
                empty_name.name = "EMPTY"
                active.modifiers[0].offset_object = empty_name
            else:
                empty_name = active.modifiers[0].offset_object
            bpy.context.scene.objects.active = active
            num = active.modifiers["Array"].count
            print(num)
            rotate_num = 360 / num
            print(rotate_num)
            active.select = True
            bpy.ops.object.transform_apply(location = False, rotation = True, scale = True) 
            empty_name.rotation_euler = (0, 0, radians(rotate_num))
            empty_name.select = False
            active.select = True
            return {'FINISHED'} 
        
            
def circle_array_menu(self, context):
    self.layout.operator(Circle_Array.bl_idname, text="Circle_Array")
        
def register():
    bpy.utils.register_class(Circle_Array)
    bpy.types.VIEW3D_MT_object.append(circle_array_menu)
def unregister():
    bpy.utils.unregister_class(Circle_Array)
    bpy.types.VIEW3D_MT_object.remove(circle_array_menu)  
    
if __name__ == "__main__":
    register() 
