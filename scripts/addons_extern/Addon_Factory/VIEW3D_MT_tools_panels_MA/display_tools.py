# space_view_3d_display_tools.py Copyright (C) 2012, Jordi Vall-llovera
#
# Multiple display tools for fast navigate/interact with the vieport
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

bl_info = {
    "name": "Display Tools",
    "author": "Jordi Vall-llovera Medina",
    "version": (1, 0),
    "blender": (2, 6, 4),
    "location": "Toolshelf",
    "description": "Multiple display tools for fast navigate/interact with the vieport",
    "warning": "",
    "wiki_url": "http://jordiart3d.blogspot.com.es/",
    "tracker_url": "",
    "category": "3D View"}

"""
Additional links:
    Author Site: http://jordiart3d.blogspot.com.es/
"""

import bpy
from bpy.props import *

#Fast Navigate toggle function
def trigger_fast_navigate(trigger):
    scene = bpy.context.scene
    scene.FastNavigateStop = False
    if trigger == True:
        trigger = False
    else:
        trigger = True
        
#Fast Navigate operator
class FastNavigate(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "view3d.fast_navigate_operator"
    bl_label = "Fast Navigate"

    _timer = None
    context_change = bpy.props.BoolProperty(name="Toggle Context", default=True)
    trigger = BoolProperty(name="Toggle Fast Navigate",default=False)

    def modal(self, context, event):
        
        if self.context_change == True:
            bpy.context.area.type = "VIEW_3D"
            self.context_change = False
            
        view = context.space_data
             
        if event.type == 'ESC' or event.type == 'RET' or event.type == 'SPACE':
            return self.cancel(context)
        
        scene = bpy.context.scene    
        if scene.FastNavigateStop == True:
            return self.cancel(context)    
        
        if event.type == 'MIDDLEMOUSE':
            view.viewport_shade='BOUNDBOX'
            
        if event.type == 'G' or event.type == 'R' or event.type == 'S': 
            view.viewport_shade='BOUNDBOX'
            
        if event.type == 'WHEELUPMOUSE' or event.type == 'WHEELDOWNMOUSE':
            view.viewport_shade='BOUNDBOX'
            
        if event.type == 'MOUSEMOVE':
            view.viewport_shade='TEXTURED'
                
        return {'PASS_THROUGH'}
         
    def execute(self, context):
        context.window_manager.modal_handler_add(self)
        self._timer = context.window_manager.event_timer_add(0.1, context.window)
        trigger_fast_navigate(self.trigger)
        return {'RUNNING_MODAL'}
    
    def cancel(self, context):
        context.window_manager.event_timer_remove(self._timer)
        return {'CANCELLED'}
    
#Init values for fast navigate
bpy.types.Scene.FastNavigateStop = bpy.props.BoolProperty(name = "Fast Navigate Stop", 
		description = "Stop fast navigate mode",
		default = False)

#Fast Navigate Stop
def fast_navigate_stop(context):
    scene = bpy.context.scene
    scene.FastNavigateStop = True

#Fast Navigate Stop Operator
class FastNavigateStop(bpy.types.Operator):
    '''Stop Fast Navigate Operator'''
    bl_idname = "view3d.fast_navigate_stop"
    bl_label = "Stop"
    
    FastNavigateStop = IntProperty(name = "FastNavigateStop", 
		description = "Stop fast navigate mode",
		default=0)

    def execute(self,context):
        fast_navigate_stop(context)
        return {'FINISHED'}
    
#Drawtype textured
def draw_textured(context):   
    view = context.space_data
    view.viewport_shade='TEXTURED'
    bpy.context.scene.game_settings.material_mode='GLSL'
    selection = bpy.context.selected_objects  
    if not(selection):
        for obj in bpy.data.objects:
            obj.draw_type='TEXTURED'
    else:
        for obj in selection:
            obj.draw_type='TEXTURED' 
    
class DisplayTextured(bpy.types.Operator):
    '''Display objects in textured mode'''
    bl_idname = "view3d.display_textured"
    bl_label = "Textured"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        draw_textured(context)
        return {'FINISHED'}
    
#Drawtype solid
def draw_solid(context):
    view = context.space_data
    view.viewport_shade='SOLID'
    bpy.context.scene.game_settings.material_mode='GLSL'
    selection = bpy.context.selected_objects 
    if not(selection):
        for obj in bpy.data.objects:
            obj.draw_type='SOLID'
    else:
        for obj in selection:
            obj.draw_type='SOLID'

class DisplaySolid(bpy.types.Operator):
    '''Display objects in solid mode'''
    bl_idname = "view3d.display_solid"
    bl_label = "Solid"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        draw_solid(context)
        return {'FINISHED'}
    
#Drawtype wire
def draw_wire(context):
    view = context.space_data
    view.viewport_shade='WIREFRAME'
    bpy.context.scene.game_settings.material_mode='GLSL'
    selection = bpy.context.selected_objects 
    if not(selection):
        for obj in bpy.data.objects:
            obj.draw_type='WIRE'
    else:
        for obj in selection:
            obj.draw_type='WIRE'

class DisplayWire(bpy.types.Operator):
    '''Display objects in wireframe mode'''
    bl_idname = "view3d.display_wire"
    bl_label = "Wire"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        draw_wire(context)
        return {'FINISHED'}
    
#Drawtype bounds
def draw_bounds(context):
    view = context.space_data
    view.viewport_shade='BOUNDBOX'
    bpy.context.scene.game_settings.material_mode='GLSL'
    selection = bpy.context.selected_objects 
    if not(selection):
        for obj in bpy.data.objects:
            obj.draw_type='BOUNDS'
    else:
        for obj in selection:
            obj.draw_type='BOUNDS'

class DisplayBounds(bpy.types.Operator):
    '''Display objects in bounds mode'''
    bl_idname = "view3d.display_bounds"
    bl_label = "Bounds"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        draw_bounds(context)
        return {'FINISHED'}

#Shade smooth
def shade_smooth(context):
    selection = bpy.context.selected_objects   
    if not(selection): 
        for obj in bpy.data.objects:
            bpy.ops.object.select_all(action='TOGGLE')
            bpy.ops.object.shade_smooth()
            bpy.ops.object.select_all(action='TOGGLE')
    else:
        for obj in selection:
            bpy.ops.object.shade_smooth()  

class DisplayShadeSmooth(bpy.types.Operator):
    '''Display shade smooth meshes'''
    bl_idname = "view3d.display_shade_smooth"
    bl_label = "Smooth"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        shade_smooth(context)
        return {'FINISHED'}
    
#Shade flat
def shade_flat(context):
    selection = bpy.context.selected_objects   
    if not(selection): 
        for obj in bpy.data.objects:
            bpy.ops.object.select_all(action='TOGGLE')
            bpy.ops.object.shade_flat()
            bpy.ops.object.select_all(action='TOGGLE')
    else:
        for obj in selection:
            bpy.ops.object.shade_flat()    

class DisplayShadeFlat(bpy.types.Operator):
    '''Display shade flat meshes'''
    bl_idname = "view3d.display_shade_flat"
    bl_label = "Flat"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        shade_flat(context)
        return {'FINISHED'}
    
#Shadeless on
def shadeless_on(context):
    selection = bpy.context.selected_objects
    if not(selection): 
        for obj in bpy.data.materials:
            obj.use_shadeless=True
    else:
        for sel in selection:
            if sel.type == 'MESH':
                materials = sel.data.materials
                for mat in materials:
                    mat.use_shadeless=True  
            
class DisplayShadelessOn(bpy.types.Operator):
    '''Display shadeless material'''
    bl_idname = "view3d.display_shadeless_on"
    bl_label = "On"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        shadeless_on(context)
        return {'FINISHED'}
    
#Shadeless off
def shadeless_off(context):
    selection = bpy.context.selected_objects
    if not(selection): 
        for obj in bpy.data.materials:
            obj.use_shadeless=False
    else:
        for sel in selection:
            if sel.type == 'MESH':
                materials = sel.data.materials
                for mat in materials:
                    mat.use_shadeless=False   

class DisplayShadelessOff(bpy.types.Operator):
    '''Display shaded material'''
    bl_idname = "view3d.display_shadeless_off"
    bl_label = "Off"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        shadeless_off(context)
        return {'FINISHED'}

#Wireframe on
def wire_on(context):
    selection = bpy.context.selected_objects   
    if not(selection): 
        for obj in bpy.data.objects:
            obj.show_wire=True
            
        for mesh in bpy.data.meshes:
            mesh.show_edges=True
    else:
        for obj in selection:
            obj.show_wire=True
                
        for sel in selection:
            if sel.type == 'MESH':
                mesh = sel.data
                mesh.show_edges=True      

class DisplayWireframeOn(bpy.types.Operator):
    '''Display wireframe overlay on'''
    bl_idname = "view3d.display_wire_on"
    bl_label = "On"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        wire_on(context)
        return {'FINISHED'}
    
#Wireframe off
def wire_off(context):
    selection = bpy.context.selected_objects  
    if not(selection): 
        for obj in bpy.data.objects:
            obj.show_wire=False
            
        for mesh in bpy.data.meshes:
            mesh.show_edges=False
    else:
        for obj in selection:
            obj.show_wire=False
                
        for sel in selection:
            if sel.type == 'MESH':
                mesh = sel.data
                mesh.show_edges=False   

class DisplayWireframeOff(bpy.types.Operator):
    '''Display wireframe overlay off'''
    bl_idname = "view3d.display_wire_off"
    bl_label = "Off"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        wire_off(context)
        return {'FINISHED'}
    
#Double Sided on
def double_sided_on(context):
    selection = bpy.context.selected_objects
    if not(selection):
        for mesh in bpy.data.meshes:
            mesh.show_double_sided=True
    else:
        for sel in selection:
            if sel.type == 'MESH':
                mesh = sel.data
                mesh.show_double_sided=True        

class DisplayDoubleSidedOn(bpy.types.Operator):
    '''Turn on face double shaded mode'''
    bl_idname = "view3d.display_double_sided_on"
    bl_label = "On"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        double_sided_on(context)
        return {'FINISHED'}
    
#Double Sided off
def double_sided_off(context):
    selection = bpy.context.selected_objects
    if not(selection):
        for mesh in bpy.data.meshes:
            mesh.show_double_sided=False
    else:
        for sel in selection:
            if sel.type == 'MESH':
                mesh = sel.data
                mesh.show_double_sided=False 

class DisplayDoubleSidedOff(bpy.types.Operator):
    '''Turn off face double shaded mode'''
    bl_idname = "view3d.display_double_sided_off"
    bl_label = "Off"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        double_sided_off(context)
        return {'FINISHED'}
    
#XRay on
def x_ray_on(context):
    selection = bpy.context.selected_objects 
    if not(selection):  
        for obj in bpy.data.objects:
            obj.show_x_ray=True
    else:
        for obj in selection:
            obj.show_x_ray=True        

class DisplayXRayOn(bpy.types.Operator):
    '''X-Ray display on'''
    bl_idname = "view3d.display_x_ray_on"
    bl_label = "On"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        x_ray_on(context)
        return {'FINISHED'}
    
#XRay off
def x_ray_off(context):
    selection = bpy.context.selected_objects            
    if not(selection):  
        for obj in bpy.data.objects:
            obj.show_x_ray=False
    else:
        for obj in selection:
            obj.show_x_ray=False  

class DisplayXRayOff(bpy.types.Operator):
    '''X-Ray display off'''
    bl_idname = "view3d.display_x_ray_off"
    bl_label = "Off"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        x_ray_off(context)
        return {'FINISHED'}
    
#Init properties for scene
bpy.types.Scene.OutlineSelected = bpy.props.BoolProperty(name = "Outline Selected", 
		description = "Hide outline around selected objects",
		default=True)

bpy.types.Scene.OnlyRender = bpy.props.BoolProperty(name = "Only Render", 
		description = "Only show render objects",
		default=False)

bpy.types.Scene.TextureSolid = bpy.props.BoolProperty(name = "Textured Solid", 
		description = "Show uv textures on solid mode",
		default=False)

bpy.types.Scene.BackfaceCulling = bpy.props.BoolProperty(name = "Backface Culling", 
		description = "Use backface culling technique for display",
		default=False)
bpy.types.Scene.ShowManipulator = bpy.props.BoolProperty(name = "Show Manipulator", 
		description = "Hide manipulator gizmo",
		default=False)

bpy.types.Scene.Simplify = bpy.props.BoolProperty(
		name = "Simplify", 
		description = "Toggle scene simplification",
		default=False)
        
bpy.types.Scene.SimplifyLevel = bpy.props.IntProperty(
		name = "Subdivision", 
		description = "Simplify level of subdivision",
		default=0, 
        min=0, 
        max=6, 
        soft_min=0, 
        soft_max=6)
        
bpy.types.Scene.SimplifySamples = bpy.props.IntProperty(
		name = "Shadow Samples", 
		description = "Simplify shadow samples",
		default=1, 
        min=1, 
        max=16, 
        soft_min=1, 
        soft_max=16)
        
bpy.types.Scene.SimplifyChild= bpy.props.FloatProperty(
		name = "Child Particles", 
		description = "Simplify child particles",
        subtype = 'FACTOR',
		default=0, 
        min=0, 
        max=1, 
        soft_min=0, 
        soft_max=1)
        
bpy.types.Scene.SimplifyAOSSS= bpy.props.FloatProperty(
		name = "AO and SSS", 
		description = "Simplify AO and SSS settings",
        subtype = 'FACTOR',
		default=0, 
        min=0, 
        max=1, 
        soft_min=0, 
        soft_max=1)

#Set Render Settings
def set_render_settings(conext,Simplify,Level,Samples,Child,AOSSS):
    
    scene = bpy.context.scene
    render = bpy.context.scene.render
    view = bpy.context.space_data
    view.show_only_render=scene.OnlyRender
    view.show_outline_selected=scene.OutlineSelected
    view.show_textured_solid=scene.TextureSolid
    view.show_backface_culling=scene.BackfaceCulling
    view.show_manipulator=scene.ShowManipulator
    render.use_simplify=scene.Simplify
    render.simplify_subdivision=scene.SimplifyLevel
    render.simplify_shadow_samples=scene.SimplifySamples
    render.simplify_child_particles=scene.SimplifyChild
    render.simplify_ao_sss=scene.SimplifyAOSSS

class DisplaySimplify(bpy.types.Operator):
    '''Display scene simplified'''
    bl_idname = "view3d.display_simplify"
    bl_label = "Update Settings"
    
    OutlineSelected = BoolProperty(name = "OutlineSelected", 
        description = "Hide outline around selected objects",
		default=True)

    OnlyRender = BoolProperty(name = "OnlyRender", 
		description = "Only show render objects",
		default=False)
    
    TextureSolid = BoolProperty(name = "TextureSolid", 
		description = "Show uv textures on solid mode",
		default=False)
    
    BackfaceCulling = BoolProperty(name = "BackfaceCulling", 
		description = "Use backface culling technique for display",
		default=False)

    ShowManipulator = BoolProperty(name = "ShowManipulator", 
		description = "Hide manipulator gizmo",
		default=False)
    
    Simplify = BoolProperty(name = "Simplify", 
		description = "Toggle scene simplification",
		default=True)

    Level = IntProperty(name="Level",
        description="Level of subdivisions allowed",
        default=0, 
        min=0, 
        max=6, 
        soft_min=0, 
        soft_max=6)
        
    Samples = IntProperty(name="Samples",
        description="Level of shadow samples allowed",
        default=0, 
        min=0, 
        max=6, 
        soft_min=0, 
        soft_max=6)
        
    Child = FloatProperty(name="Child",
        description="Number of child particles allowed",
        subtype = 'FACTOR',
        default=0, 
        min=0, 
        max=1, 
        soft_min=0, 
        soft_max=1)
        
    AOSSS = FloatProperty(name = "AO and SSS", 
		description = "Simplify AO and SSS settings",
        subtype = 'FACTOR',
		default=0, 
        min=0, 
        max=1, 
        soft_min=0, 
        soft_max=1)
    
    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        set_render_settings(context,self.Simplify,self.Level,self.Samples,self.Child,self.AOSSS)
        return {'FINISHED'}

#Display Modifiers Render on
def modifiers_render_on(context):
    
    scene = bpy.context.scene
    bpy.types.Scene.Symplify = IntProperty(name = "Integer",description = "Enter an integer")
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
        bpy.ops.object.select_all(action='TOGGLE')
        bpy.ops.object.convert(target='MESH', keep_original=False)
        bpy.ops.object.select_all(action='TOGGLE')
    else:
        for mesh in selection:
            if mesh.type == "MESH":
                bpy.ops.object.convert(target='MESH', keep_original=False)
       
class DisplayModifiersApply(bpy.types.Operator):
    '''Apply modifiers'''
    bl_idname = "view3d.display_modifiers_apply"
    bl_label = "Apply Modifiers"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        modifiers_apply(context)
        return {'FINISHED'}

# main class of this toolbar
class VIEW3D_PT_DisplayTools(bpy.types.Panel):
    bl_label = "Display Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Tools'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout

# Buttons       
        layout.label("Fast Navigate", icon='AUTO') 
        row = layout.row(align=True)
        row.alignment = 'RIGHT'
        row.operator("view3d.fast_navigate_operator")
        row.operator("view3d.fast_navigate_stop")
        
        layout.label("Display Mode", icon='TEXTURE_SHADED') 
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("view3d.display_textured")
        row.operator("view3d.display_solid")
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("view3d.display_wire")
        row.operator("view3d.display_bounds")
   
        layout.label("Shading", icon='RETOPO')
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("view3d.display_shade_smooth")
        row.operator("view3d.display_shade_flat")
        
        layout.label("Shadeless", icon='SOLID')
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("view3d.display_shadeless_on")
        row.operator("view3d.display_shadeless_off")
        
        layout.label("Wire Overlay", icon='WIRE')
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("view3d.display_wire_on")
        row.operator("view3d.display_wire_off")
        
        layout.label("Double Sided", icon='MESH_DATA')
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("view3d.display_double_sided_on")
        row.operator("view3d.display_double_sided_off")
        
        layout.label("X-Ray", icon='GHOST_ENABLED')
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("view3d.display_x_ray_on")
        row.operator("view3d.display_x_ray_off")
         
        layout.label("Scene Visualisation", icon='WORLD')
        row = layout.row(align=True)
        row.operator("view3d.display_simplify")
        scene = context.scene
        layout.prop(scene, "OutlineSelected")
        layout.prop(scene, "OnlyRender")
        layout.prop(scene, "TextureSolid")
        layout.prop(scene, "BackfaceCulling")
        layout.prop(scene, "ShowManipulator")
        layout.prop(scene, "Simplify")
        if scene.Simplify == True:
            layout.prop(scene, "SimplifyLevel")
            layout.prop(scene, "SimplifySamples")
            layout.prop(scene, "SimplifyChild")
            layout.prop(scene, "SimplifyAOSSS")

        layout.label("Modifiers", icon='MODIFIER')
        row = layout.row(align=True)
        row.operator("view3d.display_modifiers_render_on",icon='RENDER_STILL')
        row.operator("view3d.display_modifiers_render_off")
        
        row = layout.row(align=True)
        row.operator("view3d.display_modifiers_viewport_on",icon='RESTRICT_VIEW_OFF')
        row.operator("view3d.display_modifiers_viewport_off")     
        
        row = layout.row(align=True)
        row.operator("view3d.display_modifiers_edit_on",icon='EDITMODE_HLT')
        row.operator("view3d.display_modifiers_edit_off")  
        
        row = layout.row(align=True)
        row.operator("view3d.display_modifiers_cage_on",icon='EDITMODE_HLT')
        row.operator("view3d.display_modifiers_cage_off")
        
        row = layout.row(align=True)
        row.operator("view3d.display_modifiers_expand",icon='TRIA_DOWN')
        row.operator("view3d.display_modifiers_collapse",icon='TRIA_RIGHT')
        
        row = layout.row(align=True)
        row.operator("view3d.display_modifiers_apply",icon='MODIFIER')
               
# register the classes
def register():
    bpy.utils.register_class(FastNavigate)
    bpy.utils.register_class(DisplayTextured)
    bpy.utils.register_class(DisplaySolid)
    bpy.utils.register_class(DisplayWire)
    bpy.utils.register_class(DisplayBounds)
    bpy.utils.register_class(DisplayWireframeOn)
    bpy.utils.register_class(DisplayShadeSmooth)
    bpy.utils.register_class(DisplayShadeFlat)
    bpy.utils.register_class(DisplayShadelessOn)
    bpy.utils.register_class(DisplayShadelessOff)
    bpy.utils.register_class(DisplayWireframeOff)
    bpy.utils.register_class(DisplayDoubleSidedOn)
    bpy.utils.register_class(DisplayDoubleSidedOff)
    bpy.utils.register_class(DisplayXRayOn)
    bpy.utils.register_class(DisplayXRayOff)
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
    bpy.utils.register_class(DisplaySimplify)
    bpy.utils.register_module(__name__)
 
    pass 

def unregister():
    bpy.utils.unregister_class(FastNavigate)
    bpy.utils.unregister_class(DisplayTextured)
    bpy.utils.unregister_class(DisplaySolid)
    bpy.utils.unregister_class(DisplayWire)
    bpy.utils.unregister_class(DisplayBounds)
    bpy.utils.unregister_class(DisplayShadeSmooth)
    bpy.utils.unregister_class(DisplayShadeFlat)
    bpy.utils.unregister_class(DisplayShadelessOn)
    bpy.utils.unregister_class(DisplayShadelessOff)
    bpy.utils.unregister_class(DisplayWireframeOn)
    bpy.utils.unregister_class(DisplayWireframeOff)
    bpy.utils.unregister_class(DisplayDoubleSidedOn)
    bpy.utils.unregister_class(DisplayDoubleSidedOff)
    bpy.utils.unregister_class(DisplayXRayOn)
    bpy.utils.unregister_class(DisplayXRayOff)
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
    bpy.utils.unregister_class(DisplaySimplify)
    bpy.utils.unregister_module(__name__)
 
    pass 

if __name__ == "__main__": 
    register()
    