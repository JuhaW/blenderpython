#bl_info = {
#    "name": "Spacebar Modifier",
#    "author": "Mutliple Authors, mkbreuer",
#    "version": (0, 1, 0),
#    "blender": (2, 7, 2),
#    "location": "View3D",
#    "description": "",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "User Menu"}





import bpy, re
from bpy import *

###########################################################################################################################################################
###########################################################################################################################################################
### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator  
### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator 
###########################################################################################################################################################
###########################################################################################################################################################

######  Mirror  #######------------------------------------------------------- 
######  Mirror  #######------------------------------------------------------- 

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


#####  Grid Array  #######------------------------------------------------------- 
#####  Grid Array  #######------------------------------------------------------- 

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

bpy.utils.register_class(addArray2) 


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

bpy.utils.register_class(addArray3) 



#####  Cursor Array  #######------------------------------------------------------- 
#####  Cursor Array  #######------------------------------------------------------- 

class ObjectCursorArray(bpy.types.Operator):
    """Array the active object to the cursor location"""
    bl_idname = "object.cursor_array"
    bl_label = "Cursor Array"
    bl_options = {'REGISTER', 'UNDO'}

    total = bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)

    def execute(self, context):
        scene = context.scene
        cursor = scene.cursor_location
        obj = scene.objects.active

        for i in range(self.total):
            obj_new = obj.copy()
            scene.objects.link(obj_new)

            factor = i / self.total
            obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))

        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event) 
    
def menu_func(self, context):
    self.layout.operator(ObjectCursorArray.bl_idname)

bpy.utils.register_class(ObjectCursorArray) 

######  Display Tools  #####################################################################################################################
######  Display Tools  #####################################################################################################################

#bl_info = {
    #"name": "Display Tools",
    #"author": "Jordi Vall-llovera Medina",
    #"version": (1, 5, 5),
    #"blender": (2, 6, 7),
    #"location": "Toolshelf",
    #"description": "Display tools for fast navigate/interact with the viewport",
    #"warning": "",
    #"wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/\
    #3D_interaction/Display_Tools",
    #"tracker_url": "",
    #"category": "3D View"}

"""
#Additional links:
   #Author Site: http://jordiart3d.blogspot.com.es/
"""

#import bpy

from bpy.props import IntProperty, BoolProperty, FloatProperty, EnumProperty


###########################################################################################################
###########################################################################################################


#Display Modifiers Render on
def modifiers_render_on(context):    
    scene = bpy.context.scene
    bpy.types.Scene.Symplify = IntProperty(
    name = "Integer",description = "Enter an integer")
    scene['Simplify'] = 1    
    selection = bpy.context.selected_objects  
    
    if not(selection):   
        for obj in bpy.data.objects:        
            for mod in obj.modifiers:
                mod.show_render = True
    else:
        for obj in selection:        
            for mod in obj.modifiers:
                mod.show_render = True
            
class DisplayModifiersRenderOn(bpy.types.Operator):
    '''Display modifiers in render'''
    bl_idname = "view3d.display_modifiers_render_on"
    bl_label = "On"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_render_on(context)
        return {'FINISHED'}
    
#Display Modifiers Render off
def modifiers_render_off(context):
    selection = bpy.context.selected_objects  
    
    if not(selection):   
        for obj in bpy.data.objects:        
            for mod in obj.modifiers:
                mod.show_render = False
    else:
        for obj in selection:        
            for mod in obj.modifiers:
                mod.show_render = False

class DisplayModifiersRenderOff(bpy.types.Operator):
    '''Hide modifiers in render'''
    bl_idname = "view3d.display_modifiers_render_off"
    bl_label = "Off"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_render_off(context)
        return {'FINISHED'}
    
#Display Modifiers Viewport on
def modifiers_viewport_on(context):
    selection = bpy.context.selected_objects 
    
    if not(selection):    
        for obj in bpy.data.objects:        
            for mod in obj.modifiers:
                mod.show_viewport = True
    else:
        for obj in selection:        
            for mod in obj.modifiers:
                mod.show_viewport = True
        
class DisplayModifiersViewportOn(bpy.types.Operator):
    '''Display modifiers in viewport'''
    bl_idname = "view3d.display_modifiers_viewport_on"
    bl_label = "On"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_viewport_on(context)
        return {'FINISHED'}
    
#Display Modifiers Viewport off
def modifiers_viewport_off(context):
    selection = bpy.context.selected_objects 
    
    if not(selection):    
        for obj in bpy.data.objects:        
            for mod in obj.modifiers:
                mod.show_viewport = False
    else:
        for obj in selection:        
            for mod in obj.modifiers:
                mod.show_viewport = False

class DisplayModifiersViewportOff(bpy.types.Operator):
    '''Hide modifiers in viewport'''
    bl_idname = "view3d.display_modifiers_viewport_off"
    bl_label = "Off"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_viewport_off(context)
        return {'FINISHED'}
    
#Display Modifiers Edit on
def modifiers_edit_on(context):
    selection = bpy.context.selected_objects 
      
    if not(selection):  
        for obj in bpy.data.objects:        
            for mod in obj.modifiers:
                mod.show_in_editmode = True
    else:
        for obj in selection:        
            for mod in obj.modifiers:
                mod.show_in_editmode = True

class DisplayModifiersEditOn(bpy.types.Operator):
    '''Display modifiers during edit mode'''
    bl_idname = "view3d.display_modifiers_edit_on"
    bl_label = "On"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_edit_on(context)
        return {'FINISHED'}
    
#Display Modifiers Edit off
def modifiers_edit_off(context):
    selection = bpy.context.selected_objects  
     
    if not(selection):  
        for obj in bpy.data.objects:        
            for mod in obj.modifiers:
                mod.show_in_editmode = False
    else:
        for obj in selection:        
            for mod in obj.modifiers:
                mod.show_in_editmode = False

class DisplayModifiersEditOff(bpy.types.Operator):
    '''Hide modifiers during edit mode'''
    bl_idname = "view3d.display_modifiers_edit_off"
    bl_label = "Off"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_edit_off(context)
        return {'FINISHED'}


#Display Modifiers Clipping On    
class DisplayModifiersclipOn(bpy.types.Operator):
    '''Display modifiers clipping'''
    bl_idname = "view3d.display_modifiers_clip_on"
    bl_label = "On"

    def execute(self, context):
        bpy.context.object.modifiers["Mirror"].use_clip = True
        return {'FINISHED'}
		

#Display Modifiers Clipping Off  
class DisplayModifiersclipOFF(bpy.types.Operator):
    '''Display modifiers clipping'''
    bl_idname = "view3d.display_modifiers_clip_on"
    bl_label = "On"

    def execute(self, context):
        bpy.context.object.modifiers["Mirror"].use_clip = False
        return {'FINISHED'}



#Display Modifiers Cage on
def modifiers_cage_on(context):
    selection = bpy.context.selected_objects  
      
    if not(selection): 
        for obj in bpy.data.objects:        
            for mod in obj.modifiers:
                mod.show_on_cage = True
    else:
        for obj in selection:        
            for mod in obj.modifiers:
                mod.show_on_cage = True

class DisplayModifiersCageOn(bpy.types.Operator):
    '''Display modifiers editing cage during edit mode'''
    bl_idname = "view3d.display_modifiers_cage_on"
    bl_label = "On"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_cage_on(context)
        return {'FINISHED'}
    
#Display Modifiers Cage off
def modifiers_cage_off(context):
    selection = bpy.context.selected_objects 
       
    if not(selection): 
        for obj in bpy.data.objects:        
            for mod in obj.modifiers:
                mod.show_on_cage = False
    else:
        for obj in selection:        
            for mod in obj.modifiers:
                mod.show_on_cage = False

class DisplayModifiersCageOff(bpy.types.Operator):
    '''Hide modifiers editing cage during edit mode'''
    bl_idname = "view3d.display_modifiers_cage_off"
    bl_label = "Off"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_cage_off(context)
        return {'FINISHED'}
    
#Display Modifiers Expand
def modifiers_expand(context):
    selection = bpy.context.selected_objects  
      
    if not(selection): 
        for obj in bpy.data.objects:        
            for mod in obj.modifiers:
                mod.show_expanded = True
    else:
        for obj in selection:        
            for mod in obj.modifiers:
                mod.show_expanded = True

class DisplayModifiersExpand(bpy.types.Operator):
    '''Expand all modifiers on modifier stack'''
    bl_idname = "view3d.display_modifiers_expand"
    bl_label = "Expand"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_expand(context)
        return {'FINISHED'}
    
#Display Modifiers Collapse
def modifiers_collapse(context):
    selection = bpy.context.selected_objects  
      
    if not(selection): 
        for obj in bpy.data.objects:        
            for mod in obj.modifiers:
                mod.show_expanded = False
    else:
        for obj in selection:        
            for mod in obj.modifiers:
                mod.show_expanded = False

class DisplayModifiersCollapse(bpy.types.Operator):
    '''Collapse all modifiers on modifier stack'''
    bl_idname = "view3d.display_modifiers_collapse"
    bl_label = "Collapse"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_collapse(context)
        return {'FINISHED'}
    
#Apply modifiers
def modifiers_apply(context):
    selection = bpy.context.selected_objects
    
    if not(selection):  
        bpy.ops.object.select_all(action = 'TOGGLE')
        bpy.ops.object.convert(target = 'MESH', keep_original = False)
        bpy.ops.object.select_all(action = 'TOGGLE')
    else:
        for mesh in selection:
            if mesh.type == "MESH":
                bpy.ops.object.convert(target='MESH', keep_original = False)
                
class DisplayModifiersApply(bpy.types.Operator):
    '''Apply modifiers'''
    bl_idname = "view3d.display_modifiers_apply"
    bl_label = "Apply All"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_apply(context)
        return {'FINISHED'}
    
#Delete modifiers
def modifiers_delete(context):
    selection = bpy.context.selected_objects
    
    if not(selection):  
        for obj in bpy.data.objects:
            for mod in obj.modifiers:
                bpy.context.scene.objects.active = obj
                bpy.ops.object.modifier_remove(modifier = mod.name)
    else:
        for obj in selection:
            for mod in obj.modifiers:
                bpy.context.scene.objects.active = obj
                bpy.ops.object.modifier_remove(modifier = mod.name)
                
class DisplayModifiersDelete(bpy.types.Operator):
    '''Delete modifiers'''
    bl_idname = "view3d.display_modifiers_delete"
    bl_label = "Delete All"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_delete(context)
        return {'FINISHED'}
    
#Put dummy modifier for boost subsurf
def modifiers_set_dummy(context):
    selection = bpy.context.selected_objects 
   
    if not(selection):             
        for obj in bpy.data.objects:  
            bpy.context.scene.objects.active = obj 
            bpy.ops.object.modifier_add(type='SIMPLE_DEFORM')
            value = 0
            for mod in obj.modifiers:
                if mod != 0:
                  if mod.type == 'SIMPLE_DEFORM':
                    value = value +1
                    mod.factor = 0
                  if value > 1:
                      bpy.ops.object.modifier_remove(modifier="SimpleDeform")
    else:
        for obj in selection:
            bpy.context.scene.objects.active = obj 
            bpy.ops.object.modifier_add(type='SIMPLE_DEFORM')
            value = 0
            for mod in obj.modifiers:
              if mod.type == 'SIMPLE_DEFORM':
                value = value +1
                mod.factor = 0
              if value > 1:
                  bpy.ops.object.modifier_remove(modifier="SimpleDeform")


###########################################################################################################
###########################################################################################################                  
  
                  
#Delete dummy modifier 
def modifiers_delete_dummy(context):
    selection = bpy.context.selected_objects 
   
    if not(selection):             
        for obj in bpy.data.objects:  
            bpy.context.scene.objects.active = obj 
            for mod in obj.modifiers:
                  if mod.type == 'SIMPLE_DEFORM':
                      bpy.ops.object.modifier_remove(modifier="SimpleDeform")
                      bpy.ops.object.modifier_remove(modifier="SimpleDeform.001")
    else:
        for obj in selection:
            bpy.context.scene.objects.active = obj 
            for mod in obj.modifiers:
                  if mod.type == 'SIMPLE_DEFORM':
                      bpy.ops.object.modifier_remove(modifier="SimpleDeform") 
                      bpy.ops.object.modifier_remove(modifier="SimpleDeform.001")     
                                               
                  
class DisplayAddDummy(bpy.types.Operator):
    '''Add a dummy simple deform modifier to boost\
     subsurf modifier viewport performance'''
    bl_idname = "view3d.display_modifiers_set_dummy"
    bl_label = "Put Dummy"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_set_dummy(context)
        return {'FINISHED'}
    
class DisplayDeleteDummy(bpy.types.Operator):
    '''Delete a dummy simple deform modifier to boost\
    subsurf modifier viewport performance'''
    bl_idname = "view3d.display_modifiers_delete_dummy"
    bl_label = "Delete Dummy"
    
    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        modifiers_delete_dummy(context)
        return {'FINISHED'}


###########################################################################################################
###########################################################################################################

      
#Display subsurf level 0
def modifiers_subsurf_level_0(context):
    selection = bpy.context.selected_objects 
    
    if not(selection):    
        for obj in bpy.data.objects:  
            bpy.context.scene.objects.active = obj 
            bpy.ops.object.modifier_add(type='SUBSURF')
            value = 0
            for mod in obj.modifiers:
              if mod.type == 'SUBSURF':
                value = value +1
                mod.levels = 0
              if value > 1:
                  bpy.ops.object.modifier_remove(modifier="Subsurf")
 
                
    else:
        for obj in selection:  
            bpy.ops.object.subdivision_set(level=0, relative=False)  
            for mod in obj.modifiers:
              if mod.type == 'SUBSURF':
                mod.levels = 0
              
                
#Display subsurf level 1
def modifiers_subsurf_level_1(context):
    selection = bpy.context.selected_objects 
    
    if not(selection):    
        for obj in bpy.data.objects:  
            bpy.context.scene.objects.active = obj 
            bpy.ops.object.modifier_add(type='SUBSURF')
            value = 0
            for mod in obj.modifiers:
              if mod.type == 'SUBSURF':
                value = value +1
                mod.levels = 1
              if value > 1:
                  bpy.ops.object.modifier_remove(modifier="Subsurf")
    else:
        for obj in selection:  
            bpy.ops.object.subdivision_set(level=1, relative=False)       
            for mod in obj.modifiers:
                if mod.type == 'SUBSURF':
                  mod.levels = 1
                
#Display subsurf level 2
def modifiers_subsurf_level_2(context):
    selection = bpy.context.selected_objects 
    
    if not(selection):    
        for obj in bpy.data.objects:  
            bpy.context.scene.objects.active = obj 
            bpy.ops.object.modifier_add(type='SUBSURF')
            value = 0
            for mod in obj.modifiers:
              if mod.type == 'SUBSURF':
                value = value +1
                mod.levels = 2
              if value > 1:
                  bpy.ops.object.modifier_remove(modifier="Subsurf")
    else:
        for obj in selection:        
            bpy.ops.object.subdivision_set(level=2, relative=False) 
            for mod in obj.modifiers:
              if mod.type == 'SUBSURF':
                mod.levels = 2
                
#Display subsurf level 3
def modifiers_subsurf_level_3(context):
    selection = bpy.context.selected_objects 
    
    if not(selection):   
        for obj in bpy.data.objects:   
            bpy.context.scene.objects.active = obj 
            bpy.ops.object.modifier_add(type='SUBSURF')
            value = 0
            for mod in obj.modifiers:
              if mod.type == 'SUBSURF':
                value = value +1
                mod.levels = 3
              if value > 1:
                  bpy.ops.object.modifier_remove(modifier="Subsurf")
    else:
        for obj in selection:          
            bpy.ops.object.subdivision_set(level=3, relative=False) 
            for mod in obj.modifiers:
              if mod.type == 'SUBSURF':
                mod.levels = 3

#Display subsurf level 4
def modifiers_subsurf_level_4(context):
    selection = bpy.context.selected_objects 
    
    if not(selection):    
        for obj in bpy.data.objects:  
            bpy.context.scene.objects.active = obj 
            bpy.ops.object.modifier_add(type='SUBSURF')
            value = 0
            for mod in obj.modifiers:
              if mod.type == 'SUBSURF':
                value = value +1
                mod.levels = 4
              if value > 1:
                  bpy.ops.object.modifier_remove(modifier="Subsurf")
    else:
        for obj in selection:        
            bpy.ops.object.subdivision_set(level=4, relative=False) 
            for mod in obj.modifiers:
              if mod.type == 'SUBSURF':
                mod.levels = 4
                
#Display subsurf level 5
def modifiers_subsurf_level_5(context):
    selection = bpy.context.selected_objects 
    
    if not(selection):    
        for obj in bpy.data.objects:  
            bpy.context.scene.objects.active = obj 
            bpy.ops.object.modifier_add(type='SUBSURF')
            value = 0
            for mod in obj.modifiers:
              if mod.type == 'SUBSURF':
                value = value +1
                mod.levels = 5
              if value > 1:
                  bpy.ops.object.modifier_remove(modifier="Subsurf")
    else:
        for obj in selection:        
            bpy.ops.object.subdivision_set(level=5, relative=False) 
            for mod in obj.modifiers:
              if mod.type == 'SUBSURF':
                mod.levels = 5

#Display subsurf level 6
def modifiers_subsurf_level_6(context):
    selection = bpy.context.selected_objects 
    
    if not(selection):  
        for obj in bpy.data.objects:    
            bpy.context.scene.objects.active = obj 
            bpy.ops.object.modifier_add(type='SUBSURF')
            value = 0
            for mod in obj.modifiers:
              if mod.type == 'SUBSURF':
                value = value +1
                mod.levels = 6
              if value > 1:
                  bpy.ops.object.modifier_remove(modifier="Subsurf")
    else:
        for obj in selection:        
            bpy.ops.object.subdivision_set(level=6, relative=False)    
            for mod in obj.modifiers:
              if mod.type == 'SUBSURF':
                mod.levels = 6

#main class of Display subsurf level 0           
class ModifiersSubsurfLevel_0(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "view3d.modifiers_subsurf_level_0"
    bl_label = "0"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_subsurf_level_0(context)
        return {'FINISHED'}
      
#main class of Display subsurf level 1        
class ModifiersSubsurfLevel_1(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "view3d.modifiers_subsurf_level_1"
    bl_label = "1"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_subsurf_level_1(context)
        return {'FINISHED'}
      
#main class of Display subsurf level 2           
class ModifiersSubsurfLevel_2(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "view3d.modifiers_subsurf_level_2"
    bl_label = "2"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_subsurf_level_2(context)
        return {'FINISHED'}
      
#main class of Display subsurf level 3         
class ModifiersSubsurfLevel_3(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "view3d.modifiers_subsurf_level_3"
    bl_label = "3"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_subsurf_level_3(context)
        return {'FINISHED'}
      
#main class of Display subsurf level 4          
class ModifiersSubsurfLevel_4(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "view3d.modifiers_subsurf_level_4"
    bl_label = "4"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_subsurf_level_4(context)
        return {'FINISHED'}
      
#main class of Display subsurf level 5         
class ModifiersSubsurfLevel_5(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "view3d.modifiers_subsurf_level_5"
    bl_label = "5"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_subsurf_level_5(context)
        return {'FINISHED'}
      
#main class of Display subsurf level 6          
class ModifiersSubsurfLevel_6(bpy.types.Operator):
    '''Change subsurf modifier level'''
    bl_idname = "view3d.modifiers_subsurf_level_6"
    bl_label = "6"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_subsurf_level_6(context)
        return {'FINISHED'}


###########################################################################################################
###########################################################################################################

             
# register the classes
def register():

    bpy.utils.register_class(DisplayModifiersRenderOn)
    bpy.utils.register_class(DisplayModifiersRenderOff)
    bpy.utils.register_class(DisplayModifiersViewportOn)
    bpy.utils.register_class(DisplayModifiersViewportOff)
    bpy.utils.register_class(DisplayModifiersEditOn)
    bpy.utils.register_class(DisplayModifiersEditOff)
    bpy.utils.register_class(DisplayModifiersCageOn)
    bpy.utils.register_class(DisplayModifiersCageOff)
    bpy.utils.register_class(DisplayModifiersExpand)
    bpy.utils.register_class(DisplayModifiersCollapse)
    bpy.utils.register_class(DisplayModifiersApply)
    bpy.utils.register_class(DisplayModifiersDelete)
    bpy.utils.register_class(ModifiersSubsurfLevel_0)
    bpy.utils.register_class(ModifiersSubsurfLevel_1)
    bpy.utils.register_class(ModifiersSubsurfLevel_2)
    bpy.utils.register_class(ModifiersSubsurfLevel_3)
    bpy.utils.register_class(ModifiersSubsurfLevel_4)
    bpy.utils.register_class(ModifiersSubsurfLevel_5)
    bpy.utils.register_class(ModifiersSubsurfLevel_6)



def unregister():

    bpy.utils.unregister_class(DisplayModifiersRenderOn)
    bpy.utils.unregister_class(DisplayModifiersRenderOff)
    bpy.utils.unregister_class(DisplayModifiersViewportOn)
    bpy.utils.unregister_class(DisplayModifiersViewportOff)
    bpy.utils.unregister_class(DisplayModifiersEditOn)
    bpy.utils.unregister_class(DisplayModifiersEditOff)
    bpy.utils.unregister_class(DisplayModifiersCageOn)
    bpy.utils.unregister_class(DisplayModifiersCageOff)
    bpy.utils.unregister_class(DisplayModifiersExpand)
    bpy.utils.unregister_class(DisplayModifiersCollapse)
    bpy.utils.unregister_class(DisplayModifiersApply)
    bpy.utils.unregister_class(DisplayModifiersDelete)
    bpy.utils.unregister_class(ModifiersSubsurfLevel_0)
    bpy.utils.unregister_class(ModifiersSubsurfLevel_1)
    bpy.utils.unregister_class(ModifiersSubsurfLevel_2)
    bpy.utils.unregister_class(ModifiersSubsurfLevel_3)
    bpy.utils.unregister_class(ModifiersSubsurfLevel_4)
    bpy.utils.unregister_class(ModifiersSubsurfLevel_5)
    bpy.utils.unregister_class(ModifiersSubsurfLevel_6)
    


#############################################################################################################################################################
#############################################################################################################################################################
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ###  
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ###  
#############################################################################################################################################################
#############################################################################################################################################################

#####  Array Menu  #######------------------------------------------------------- 
#####  Array Menu  #######------------------------------------------------------- 

class arraymodi(bpy.types.Menu):
    bl_label = "Array Menu"
    bl_idname = "space_arraymodifier"
    
    def draw(self, context):
        layout = self.layout

        layout.operator("object.cursor_array", text="2 Cursor", icon = 'RIGHTARROW_THIN')
        
        layout.separator()         
          
        layout.operator("object.add_2array", text="2d Grid", icon = 'RIGHTARROW_THIN')
        layout.operator("object.add_3array", text="3d Grid", icon = 'RIGHTARROW_THIN')

bpy.utils.register_class(arraymodi) 


 
#####  Visual Menu  #######------------------------------------------------------- 
#####  Visual Menu  #######------------------------------------------------------- 

class modivisual(bpy.types.Menu):
    bl_label = "Visual Menu"
    bl_idname = "space_modivisual"
    
    def draw(self, context):
        layout = self.layout

        layout.operator("view3d.display_modifiers_viewport_on", "View On", icon = 'RESTRICT_VIEW_OFF')
        layout.operator("view3d.display_modifiers_viewport_off", "View Off", icon = 'VISIBLE_IPO_OFF')         
        
        layout.separator() 
 
        layout.operator("view3d.display_modifiers_edit_on",  "Edit On", icon = 'EDITMODE_HLT')
        layout.operator("view3d.display_modifiers_edit_off", "Edit Off", icon = 'SNAP_VERTEX')       

        layout.separator()
                
        layout.operator("view3d.display_modifiers_cage_on", "Cage On", icon = 'OUTLINER_OB_MESH')
        layout.operator("view3d.display_modifiers_cage_off", "Cage Off", icon = 'OUTLINER_DATA_MESH')  
        
        layout.separator()

        layout.operator("view3d.display_modifiers_render_on", "Render On", icon = 'RENDER_STILL') 
        layout.operator("view3d.display_modifiers_render_off", "Render Off", icon = 'RENDER_STILL') 

bpy.utils.register_class(modivisual) 



#####  Array Menu  #######------------------------------------------------------- 
#####  Array Menu  #######------------------------------------------------------- 

class modifly(bpy.types.Menu):
    bl_label = "Flymode"
    bl_idname = "space_modifly"
    
    def draw(self, context):
        #active_obj = context.active_object
        active_obj = context.active_object
        layout = self.layout
        
        scene = context.scene
  
        layout.prop(scene,"OriginalMode", "")
     
        layout.prop(scene,"FastMode", "")
        
        layout.separator()
        
        layout.prop(scene,"EditActive", "Edit mode")
        
        layout.separator()
        
        layout.prop(scene,"Delay")
        layout.prop(scene,"DelayTimeGlobal")

        layout.separator()
        
        layout.prop(scene,"ShowParticles")
        layout.prop(scene,"ParticlesPercentageDisplay")
        
bpy.utils.register_class(modifly) 




#############################################################################################################################################################
#############################################################################################################################################################
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
#############################################################################################################################################################
#############################################################################################################################################################
 

######  Modifier Menu  #######------------------------------------------------------- 
######  Modifier Menu  #######------------------------------------------------------- 

class VIEW3D_Space_Modifier(bpy.types.Menu):
    bl_label = "Modifier"
    bl_idname = "space_modifier"  
    bl_space_type = 'VIEW_3D'

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'
        
        layout.operator_menu_enum("object.modifier_add", "type", text = "Add Menu", icon='MODIFIER')

        layout.menu("space_arraymodifier", icon='MOD_ARRAY')                  

        layout.menu("space_modivisual", icon='RESTRICT_VIEW_OFF')

        layout.separator()
        
        layout.label(text="Subsurf-Level",icon='MOD_SUBSURF')
        
        layout.operator("view3d.modifiers_subsurf_level_0",text="0-Level")
        layout.operator("view3d.modifiers_subsurf_level_1",text="1-Level")
        layout.operator("view3d.modifiers_subsurf_level_2",text="2-Level")
        layout.operator("view3d.modifiers_subsurf_level_3",text="3-Level")
        layout.operator("view3d.modifiers_subsurf_level_4",text="4-Level")
        layout.operator("view3d.modifiers_subsurf_level_5",text="5-Level")
        layout.operator("view3d.modifiers_subsurf_level_6",text="6-Level")

        layout.separator()                        

        layout.operator("view3d.fullmirror", icon='MOD_MIRROR', text="Clip-Mirror X")
        layout.operator("view3d.fullmirrory", icon='MOD_MIRROR', text="Clip-Mirror Y")
        layout.operator("view3d.fullmirrorz", icon='MOD_MIRROR', text="Clip-Mirror Z")
        
        layout.separator()         

        layout.operator("view3d.display_modifiers_apply", icon = 'FILE_TICK', text="Apply all Mod.")
        layout.operator("view3d.display_modifiers_delete", icon = 'X', text="Delete all Mod.")

        layout.separator()

        layout.operator("view3d.display_modifiers_expand", icon = 'TRIA_DOWN', text="Expand all Mod.")
        layout.operator("view3d.display_modifiers_collapse", icon = 'TRIA_RIGHT', text="Collapse all Mod.")           
            
 
###########################################################################################################################################################
###########################################################################################################################################################
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register 
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register 
###########################################################################################################################################################
###########################################################################################################################################################


def register():

    bpy.utils.register_class(VIEW3D_Space_Modifier)    
    
    bpy.utils.register_module(__name__)  

def unregister():
  
    bpy.utils.unregister_class(VIEW3D_Space_Modifier)    
    
    bpy.utils.unregister_module(__name__)  

if __name__ == "__main__":
    register() 	

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_Space_Modifier.bl_idname)


















