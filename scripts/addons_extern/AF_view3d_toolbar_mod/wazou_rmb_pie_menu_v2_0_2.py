# -*- coding: utf-8 -*-

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "Wazou_RMB_Pie_Menu",
    "author": "Cedric Lepiller",
    "version": (2, 0, 2),
    "blender": (2, 78, 0),
    "location": "View3D > RMB",
    "description": "Right Click Pie Menu",
    "category": "3D View"}

"""
Right Click Pie Menu
This adds a the Right Click Pie Menu in the View3D.
Left mouse is SELECTION.
Left Alt + Double click sets the 3D cursor.

"""

import bpy
import bmesh
from bpy.types import Menu, Operator
from bpy.props import PointerProperty, StringProperty, BoolProperty, \
    EnumProperty, IntProperty, FloatProperty, FloatVectorProperty, \
    CollectionProperty, BoolVectorProperty
import rna_keymap_ui
from bpy.types import Curve, SurfaceCurve, TextCurve

########################
#      Properties      #               
########################

class WazouRightMenuPiePrefs(bpy.types.AddonPreferences):
    bl_idname = __name__

    prefs_tabs = EnumProperty(
        items=(('info', "Info", "Info"),
               ('keymap', "Keymap", "Keymap"),
               ('links', "Links", "Links")),
               default='info'
               )
    
    use_normal_primitives = BoolProperty(
            name="Use Normal Primitives",
            default=False,
            description="Use Normal Primitives"
            ) 
            
    def draw(self, context):
        layout = self.layout
        wm = bpy.context.window_manager
        
        
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
        if self.prefs_tabs == 'info':
            box=layout.box() 
            box.label("This addon works with the Right Mouse Button !")    
            box.label("To move the Cursor, press Alt + Double click", icon='CURSOR')
            box.label("You can change the keymap of course !")
            box=layout.box() 
            box.label("To have all the tools, you need to Activate or install :")  
            box.label("- Looptools") 
            box.label("- Offset Edges") 
            row=box.row(align=True)
            row.label("- Auto Mirror") 
            row.operator("wm.url_open", text="Link").url = "https://github.com/lapineige/Blender_add-ons/blob/master/AutoMirror/AutoMirror_V2-4.py"
            row=box.row(align=True)
            row.label("- Mesh Vertex tools") 
            row.operator("wm.url_open", text="Link").url = "http://samoloty.wjaworski.pl/scripts-254_p.xml"
            box=layout.box() 
            box.label("Place your mouse over Buttons to see possibilities")  
            box.label("You can use Ctrl, Shift, Alt do do multiple operationS with one button") 
            box.label("You can combine keys Ctrl+shift, Shift+Alt etc") 
            box.separator()
            box.label("PRIMITIVES:")
            box.label("Click > Add on the cursor")
            box.label("Shift > Add on a selection, if no selection, on the cursor")
            box.label("Ctrl  > Add on the mouse, to place is where you want")
            box.label("Alt   > Add in Edit mode, you can combine with Shift and Ctrl")
            box.label("Blender don't allow editable mesh after moving them, so I added normal primitives")
            box.separator()
            box.label("CAMERA:")
            box.label("Click > Add on the cursor")
            box.label("Shift > Add a Camera and see through with the object selected to turn around selection")
            box.label("Ctrl  > Add on the mouse, to place is where you want")
            box.label("Alt   > Add a Camera and an empty as Dof object, keep the previous selection active")
            box.separator()
            box.label("TRANSFORMS:")
            box.label("Click > Apply transforms")
            box.label("Shit  > Apply Transforms and keep Origin")
            box.separator()
            box.label("PARENT/UNPARENT:")
            box.label("Click > Parent to active Object")
            box.label("Ctrl  > Unparent")
            box.label("Ctrl + Shift > Unparent and clear transforms")
            box.label("Works on parent and Children")
            box.separator()
            box.label("SUBSURF:")
            box.label("Click > Add/remove subsurf level 2")
            box.label("Shift in Object Mode > Apply subsurf")
            box.label("Shift in Edit Mode   > Add and Apply subsurf level 1")
            box.label("Ctrl in Edit Mode    > Add and Apply subsurf level 2")
            box.separator()
            box.label("SEPARATE:")
            box.label("Click > Join or Separate objects by loose parts")
            box.label("Shift > Join Object and Remove Double")
            box.label("Click in Edit Mode > Duplicate Selection to a new object")
            box.label("Ctrl  > Go in Edit mode")
            box.label("Shift + Click in Edit Mode > Separate selection to a new object")
            box.label("Ctrl  > Go in Edit mode")
            box.label("Click > Join or Separate objects by loose parts")
            box.separator()
            box.label("MODIFIERS:")
            box.label("Click > Apply Modifiers on selection")
            box.label("Ctrl  > Remove Modifiers on selection")
            box.separator()
            box.label("KNIFE:")
            box.label("Click > Enter in Knife too mode")
            box.label("Shift > Enter in Knife too mode and cut through")
            box.separator()
            box.label("INSERT/POKE:")
            box.label("Click > Enter in insert tool")
            box.label("Shift > Poke face")
            box.label("Ctrl  > Poke and Enter in insert tool")
            box.separator()
            box.label("SEAM:")
            box.label("Click > Add Seam")
            box.label("Ctrl > Remove Seam")
            box.separator()
            box.label("UNWRAP:")
            box.label("Click > Add Seam and Unwrap")
            box.label("Shift > Smart Uv Project")
            box.label("Ctrl  > Follow Active Quad")
            box.label("Alt   > Reset Uv's")
            box.separator()
            box.label("CIRCLE:")
            box.label("Click > Add circle")
            box.label("Shift > Add circle with a loop")
            box.label("Ctrl  > Individual")
            box.label("Alt   > Sudivide")
            box.label("You can combine Individual, subdivide and loop on faces")
            box.label("You cannot subdivide on several vertices")
            box.separator() 
            box.operator("wm.url_open", text="Settings for the pie menu").url = "http://pitiwazou.com/screenshots/blender_2017-05-22_16-30-57.jpg"
        
        
        if self.prefs_tabs == 'keymap':   
            box=layout.box()
            split = box.split()
            col = split.column()       
            col.label('Setup Pie menu Hotkey')
            col.separator()
            wm = bpy.context.window_manager
            kc = wm.keyconfigs.user
            km = kc.keymaps['3D View Generic']
            kmi = get_hotkey_entry_item(km, 'wm.call_menu_pie', 'pie.rightclicmenu')
            if kmi:
                col.context_pointer_set("keymap", km)
                rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
            else:
                col.label("No hotkey entry found")
                col.operator(Template_Add_Hotkey.bl_idname, text = "Add hotkey entry", icon = 'ZOOMIN')
            
            box=layout.box()
            split = box.split()
            col = split.column()       
            col.label('Setup Cursor Hotkey')
            col.separator()
            wm = bpy.context.window_manager
            kc = wm.keyconfigs.user
            km = kc.keymaps['3D View Generic']
            kmi = get_hotkey_entry_item(km, 'view3d.cursor3d', None)
            if kmi:
                col.context_pointer_set("keymap", km)
                rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
            else:
                col.label("No hotkey entry found")
                col.operator(Template_Add_Hotkey.bl_idname, text = "Add hotkey entry", icon = 'ZOOMIN')

         
        if self.prefs_tabs == 'links': 
            layout.operator("wm.url_open", text="Asset Management").url = "https://gumroad.com/l/kANV"
            layout.operator("wm.url_open", text="Speedflow").url = "https://gumroad.com/l/speedflow"
            layout.operator("wm.url_open", text="SpeedSculpt").url = "https://gumroad.com/l/SpeedSculpt"
            layout.operator("wm.url_open", text="SpeedRetopo").url = "https://gumroad.com/l/speedretopo"
            layout.separator() 
            layout.operator("wm.url_open", text="Pitiwazou.com").url = "http://www.pitiwazou.com/"
            layout.operator("wm.url_open", text="Wazou's Ghitub").url = "https://github.com/pitiwazou/Scripts-Blender"
            layout.operator("wm.url_open", text="BlenderLounge Forum").url = "http://blenderlounge.fr/forum/"              

#######################
#       Classes       #               
#######################


#Looptools    
class VIEW3D_MT_edit_mesh_looptools(bpy.types.Menu):
    bl_idname = "loop.tools" 
    bl_label = "LoopTools"

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.looptools_bridge", text="Bridge").loft = False
        layout.operator("mesh.looptools_circle")
        layout.operator("mesh.looptools_curve")
        layout.operator("mesh.looptools_flatten")
        layout.operator("mesh.looptools_gstretch")
        layout.operator("mesh.looptools_bridge", text="Loft").loft = True
        layout.operator("mesh.looptools_relax")
        layout.operator("mesh.looptools_space") 

#Create Hole
class CreateHole(bpy.types.Operator):                                 
    bl_idname = "object.createhole"                     
    bl_label = "Create Hole on a Selection" 
    bl_description = "Create holes, Shift> Add Loop, Ctrl> Individual, Alt> Subdivide"  
    bl_options = {'REGISTER', 'UNDO'}     

    @classmethod                                     
    def poll(cls, context):                         
        return context.active_object is not None 

    def invoke(self, context, event):
        WM = context.window_manager  
        bm = bmesh.from_edit_mesh(bpy.context.object.data)
        sel_vert=[e for e in bm.verts if e.select]  
        
        #If faces
        if tuple (bpy.context.tool_settings.mesh_select_mode) == (False, False, True) :               
            
            #Individual
            if event.ctrl :
                bpy.ops.mesh.inset(thickness=0.02, use_individual=True)
            else:
                bpy.ops.mesh.inset(thickness=0.02)
            
            #Subdivide
            if event.alt :
                bpy.ops.mesh.subdivide(smoothness=0)
                bpy.ops.mesh.dissolve_mode()

                bpy.ops.mesh.poke()
            bpy.ops.mesh.looptools_circle()
            
            #Add Loop
            if event.shift :
                bpy.ops.mesh.inset(thickness=0.02)
                bpy.ops.mesh.select_more()
            
            bpy.context.space_data.pivot_point = 'INDIVIDUAL_ORIGINS'
            bpy.ops.transform.resize('INVOKE_DEFAULT')                     
        
        
        elif tuple (bpy.context.tool_settings.mesh_select_mode) == (True, False, False) :
            
            bpy.ops.mesh.bevel(offset=0.1, vertex_only=True)
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            
            if event.alt :
                if len(sel_vert)>1:
                    pass
                else :
                    bpy.ops.mesh.subdivide(smoothness=0)
                    bpy.ops.mesh.dissolve_mode()
                    bpy.ops.mesh.looptools_circle()
                    bpy.ops.mesh.poke()

            if event.shift :
                bpy.ops.mesh.inset(thickness=0.02)
                bpy.ops.mesh.poke()
                bpy.ops.mesh.select_more()
                
            bpy.ops.mesh.looptools_circle()
            
            bpy.context.space_data.pivot_point = 'INDIVIDUAL_ORIGINS'
            bpy.ops.transform.resize('INVOKE_DEFAULT') 
        
        else:
            pass           
        return {'FINISHED'} 
    
#Space
class RetopoSpace(bpy.types.Operator):  
    bl_idname = "retopo.space"  
    bl_label = "Retopo Space" 
    bl_description = "Add even space between vertices" 
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        bpy.ops.mesh.looptools_space(influence=100, input='selected', interpolation='cubic', lock_x=False, lock_y=False, lock_z=False)
        return {'FINISHED'}  
    
#Apply_Transforms
class RMB_Apply_Transforms(bpy.types.Operator):
    bl_idname = "object.rmb_apply_transforms"
    bl_label = "Rmb Apply Transforms"
    bl_description = "Apply transforms, Shift to keep Origin"
    bl_options = {"REGISTER","UNDO"}

    def invoke(self, context, event):
        saved_location_0 = bpy.context.scene.cursor_location.copy() 
        
        if event.shift:
            bpy.ops.view3d.snap_cursor_to_active()
            saved_location = bpy.context.scene.cursor_location.copy()
#            bpy.ops.apply.transformall()
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True) 
            bpy.context.scene.cursor_location = saved_location
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        else:
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)    
        
        bpy.context.scene.cursor_location = saved_location_0
        return {"FINISHED"}    
    
#Make Object An Empty
class MakeObjectAnEmpty(bpy.types.Operator):
    bl_idname = "object.makeempty"
    bl_label = "Make Object An Empty"
    bl_description = "Create object as empty for inserts"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        if bpy.context.object.hide_render == False:
            bpy.context.object.hide_render = True
            bpy.context.object.draw_type = 'WIRE'
            bpy.context.object.cycles_visibility.camera = False
            bpy.context.object.cycles_visibility.diffuse = False
            bpy.context.object.cycles_visibility.glossy = False
            bpy.context.object.cycles_visibility.scatter = False
            bpy.context.object.cycles_visibility.transmission = False
            bpy.context.object.cycles_visibility.shadow = False
        elif bpy.context.object.hide_render == True: 
            bpy.context.object.hide_render = False
            bpy.context.object.draw_type = 'SOLID'
            bpy.context.object.cycles_visibility.camera = True
            bpy.context.object.cycles_visibility.diffuse = True
            bpy.context.object.cycles_visibility.glossy = True
            bpy.context.object.cycles_visibility.scatter = True
            bpy.context.object.cycles_visibility.transmission = True
            bpy.context.object.cycles_visibility.shadow = True   
        return {'FINISHED'} 

#Mark Seam
class Mark_Clear_Seam(bpy.types.Operator):  
    bl_idname = "object.mark_clear_seam"  
    bl_label = "Mark/clear Seam, Ctrl to Clear Seam" 
    bl_description = "Add/Remove Seam, Ctrl to Remove"
    bl_options = {'REGISTER','UNDO'} 
  
    def invoke(self, context, event):
        
        if event.ctrl:
            bpy.ops.mesh.mark_seam(clear=True)
        else:    
            bpy.ops.mesh.mark_seam()
        return {'FINISHED'}
        
#Unwrap
class Unwrap(bpy.types.Operator):
    bl_idname = "object.unwrap"
    bl_label = "Unwrap"
    bl_description = "Unwrap, shift to smart Project, Ctrl to Follow Active quad"
    bl_options = {"REGISTER", "UNDO"}


    def invoke(self, context, event):
        obj = bpy.context.edit_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)

        if event.shift :
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.uv.smart_project()
        
        if event.ctrl:
            bpy.ops.uv.follow_active_quads()
        
        if event.alt:
            bpy.ops.uv.reset()

        else:    
            if tuple (bpy.context.tool_settings.mesh_select_mode) == (False, True, False) :      
                for e in bm.edges:
                    if e.select :  
                        bpy.ops.mesh.mark_seam(clear=False)
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
                bpy.ops.mesh.select_all(action='SELECT')
                   
            bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
        
        return {"FINISHED"}    
    
#Simplify Circle       
class Simplify_Circle(bpy.types.Operator):
    bl_idname = "simplify.circle"
    bl_label = "Simplify Circle"
    bl_description = ""
    bl_options = {"REGISTER", 'UNDO'} 
    
    
    def execute(self, context):
        bpy.ops.mesh.select_nth()
        bpy.ops.mesh.edge_collapse()
        return {"FINISHED"}
   
#Extract_Duplicate
class Extract_Duplicate(bpy.types.Operator):
    bl_idname = "object.extract_duplicate"
    bl_label = "Extract Duplicate"
    bl_description = "Extract Duplicate, Object: Ctrl>separate, 2obj Ctrl>join remove double, Edit: Ctrl>duplicate and stay in Edit Mode, SHIFT>extract, Ctrl+Shif>extract and stay in Edit Mode on Join to remove doubles"
    bl_options = {"REGISTER","UNDO"}

    def invoke(self, context, event):
        obj = context.active_object
        
        if bpy.context.object.mode == 'OBJECT':
            if len(bpy.context.selected_objects) == 1:
                bpy.ops.mesh.separate(type='LOOSE')
                bpy.context.active_object.select = True  
            else:
                bpy.ops.Object.join()  
                if event.shift:
                    bpy.ops.object.mode_set(mode = 'EDIT')
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.remove_doubles()
                    bpy.ops.object.mode_set(mode = 'OBJECT')
            
        elif bpy.context.object.mode == 'EDIT':   
            if event.shift:  
                bpy.ops.mesh.separate(type='SELECTED')
                bpy.ops.object.mode_set(mode = 'OBJECT')
                obj.select=False
                bpy.context.scene.objects.active = bpy.context.selected_objects[0]     
            
            else:  
                bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.object.duplicate_move()
                bpy.ops.object.mode_set(mode = 'EDIT')
                
                if tuple (bpy.context.tool_settings.mesh_select_mode) == (False, False, True) :    
                    bpy.ops.mesh.select_all(action='INVERT')
                    bpy.ops.mesh.delete(type='FACE')
                else:
                    bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT') 
                    bpy.ops.mesh.select_all(action='INVERT')
                    bpy.ops.mesh.delete(type='VERT')
                
                bpy.ops.object.mode_set(mode = 'OBJECT')
            
            if event.ctrl:
                bpy.ops.object.mode_set(mode = 'EDIT')
         
        return {"FINISHED"}

#Poke_face    
class Inset_Poke_Faces(bpy.types.Operator):
    bl_idname = "object.inset_poke_faces"
    bl_label = "Inset/Poke Faces"
    bl_description = "Inset/Poke Faces, Shift to close and Poke, Ctrl to Poke and inset"
    bl_options = {"REGISTER","UNDO"}

    def invoke(self, context, event):
        bm = bmesh.from_edit_mesh(bpy.context.object.data)
        sel_faces=[e for e in bm.faces if e.select]
        
        if event.shift:
            if len(sel_faces)>0:
                bpy.ops.mesh.poke() 
            else:    
                bpy.ops.mesh.edge_face_add()
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE') 
                bpy.ops.mesh.poke() 
              
        elif event.ctrl:
            if len(sel_faces)>0:
                bpy.ops.mesh.poke() 
                bpy.ops.mesh.inset('INVOKE_DEFAULT')
            else:    
                bpy.ops.mesh.edge_face_add()
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE') 
                bpy.ops.mesh.poke()
                bpy.ops.mesh.inset('INVOKE_DEFAULT')
        
        else:
            if len(sel_faces)==0:
                bpy.ops.mesh.edge_face_add()
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE') 
            bpy.ops.mesh.inset('INVOKE_DEFAULT')
            
            
        return {"FINISHED"}  

#Subsurf
class Subsurf_Operator(bpy.types.Operator):
    bl_idname = "object.subsurf_operator"
    bl_label = "Subsurf Operator"
    bl_description = "Add or Remove subsurf, Shift add and Apply, Alt add and apply ite 1"
    bl_options = {"REGISTER",'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        if context.object is not None :
            return True

    def invoke(self, context, event):
        obj = context.active_object
        
        if "Subsurf" in obj.modifiers:  
            for obj in bpy.context.selected_objects:
                obj.select = True
                bpy.context.scene.objects.active=obj   
                if event.shift:
                    if bpy.context.object.mode == "EDIT":
                        bpy.ops.object.mode_set(mode = 'OBJECT')
                        bpy.ops.object.modifier_apply(modifier="Subsurf")
                        bpy.ops.object.mode_set(mode = 'EDIT')
                    else:
                        bpy.ops.object.modifier_apply(modifier="Subsurf")  
                        
                bpy.ops.object.modifier_remove(modifier="Subsurf")
        
        else: 
            for obj in bpy.context.selected_objects:
                obj.select = True
                bpy.context.scene.objects.active=obj       
                bpy.ops.object.subdivision_set(level=2)
                bpy.context.object.modifiers["Subsurf"].show_only_control_edges = True
                
                if bpy.context.object.mode == "EDIT":
                    bpy.ops.object.subdivision_set(level=2)
                    bpy.context.object.modifiers["Subsurf"].show_on_cage = True
                    bpy.ops.object.mode_set(mode = 'EDIT')
                
                #add and apply ite 1
                if event.shift:
                    if bpy.context.object.mode == "EDIT":
                        bpy.ops.object.mode_set(mode = 'OBJECT')
                        bpy.context.object.modifiers["Subsurf"].levels = 1
                        bpy.ops.object.modifier_apply(modifier="Subsurf")
                        bpy.ops.object.mode_set(mode = 'EDIT')
                    else:
                        bpy.context.object.modifiers["Subsurf"].levels = 1
                        bpy.ops.object.modifier_apply(modifier="Subsurf")  
                
                #Add and apply ite 2
                if event.ctrl:
                    if bpy.context.object.mode == "EDIT":
                        bpy.ops.object.mode_set(mode = 'OBJECT')
                        bpy.ops.object.modifier_apply(modifier="Subsurf")
                        bpy.ops.object.mode_set(mode = 'EDIT')
                    else:
                        bpy.ops.object.modifier_apply(modifier="Subsurf")  
        return {"FINISHED"}  

      
#Apply_Remove_Modifiers    
class Apply_Remove_Modifiers(bpy.types.Operator):
    bl_idname = "object.apply_remove_modifiers"
    bl_label = "Apply Remove Modifiers"
    bl_description = "Apply or Remove modifier, Ctrl to Remove"
    bl_options = {"REGISTER",'UNDO'}

    def invoke(self, context, event):
        obj = context.active_object
        selection = bpy.context.selected_objects
        
        #Apply
        if event.ctrl:
            for obj in selection:
                obj.select = True
                if obj.modifiers:
                    bpy.context.scene.objects.active=obj
                    for mod in obj.modifiers :
                        bpy.ops.object.modifier_remove(modifier=mod.name)             
        else:
            for obj in selection:
                obj.select = True
                if obj.modifiers:
                    bpy.context.scene.objects.active=obj
                    for mod in obj.modifiers :
                        if mod.show_viewport == False :
                            bpy.ops.object.modifier_remove(modifier=mod.name)
                        else:
                            bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)  
        return {"FINISHED"}             


#Parent Unparent
class Parent_Objects(bpy.types.Operator):
    bl_idname = "object.parent_objects"
    bl_label = "Parent Objects"
    bl_description = "Parent/Unparent, Ctrl to Unparent, Ctrl+shift to clear Parent"
    bl_options = {"REGISTER","UNDO"}
    
    def invoke(self, context, event):
        obj = context.active_object
        
        #Parent
        bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
        
        #Unparent
        if event.ctrl:
            #If parent selected
            if not obj.parent:
                C = bpy.context
                for obj in C.object.children: 
                    obj.select = True
                    
                    if event.shift:
                        bpy.ops.object.parent_clear(type='CLEAR')
                    else:    
                        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
                    bpy.ops.object.select_all(action='TOGGLE')
            
            #If child selected
            else:  
                for obj in bpy.context.selected_objects:
                    obj.select = True
                    bpy.context.scene.objects.active=obj 
                    
                    if event.shift:
                        bpy.ops.object.parent_clear(type='CLEAR')
                    else:    
                        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM') 

        return {"FINISHED"}    

#Primitives    
class RMB_Primitives(bpy.types.Operator):
    bl_idname = "object.rmb_primitives"
    bl_label = "Custom Add Primitives"
    bl_description = "Create primitives, Shift on selection, Ctrl on mouse, Alt in Edit Mode"
    bl_options = {"REGISTER", "UNDO"}
    
    primitive = bpy.props.EnumProperty(
        items = (('cube', "Cube", ""),
                 ('sphere', "Sphere", ""),
                 ('plan', "Plan", ""),
                 ('grid', "Grid", ""),
                 ('cylinder', "Cylinder", ""),
                 ('cone', "Cone", ""),
                 ('torus', "Torus", ""),
                 ('empty_axe', "Empty_Axe", ""),
                 ('bezier', "Bezier", ""),
                 ('vertex', "Vertex", ""),
                 ('text', "Text", ""),
                 ('area', "Area", ""),
                 ('sun', "Sun", ""),
                 ('hemi', "hemi", ""),
                 ('point', "Point", ""),
                 ('spot', "Spot", ""),
                 ('camera', "Camera", ""),
                 ('curve_line', "Curve Line", "")),
                 default = 'cube'
                 )
    
    def invoke(self, context, event):
        obj = False      
        obj = context.active_object
        
        saved_location = bpy.context.scene.cursor_location.copy()
        
        if event.shift:
            bpy.ops.view3d.snap_cursor_to_selected()

        if event.ctrl:
            bpy.ops.view3d.cursor3d('INVOKE_DEFAULT')
        
        #Cube
        if self.primitive == 'cube':
            if event.alt:
                if context.object is not None and bpy.context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT') 
                bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=True)                
            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False)      
         
        #Plan    
        elif self.primitive == 'plan':
            if event.alt:
                if context.object is not None and bpy.context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.mesh.primitive_plane_add(enter_editmode=True)
            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.mesh.primitive_plane_add()
        #Grid
        elif self.primitive == 'grid':
            if event.alt:
                if context.object is not None and bpy.context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                    
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=10, y_subdivisions=10, radius=1,enter_editmode=True)  
            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.mesh.primitive_grid_add(x_subdivisions=10, y_subdivisions=10, radius=1)   
        
        #Sphere                                
        elif self.primitive == 'sphere':
            if event.alt:
                if context.object is not None and bpy.context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12,enter_editmode=True)  
            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12)
        
        #Cylinder    
        elif self.primitive == 'cylinder':
            if event.alt:
                if context.object is not None and bpy.context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.mesh.primitive_cylinder_add(vertices=16, view_align=False,enter_editmode=True)  
            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.mesh.primitive_cylinder_add(vertices=16, view_align=False)
        
        #cone    
        elif self.primitive == 'cone':
            if event.alt:
                if context.object is not None and bpy.context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT') 
                bpy.ops.mesh.primitive_cone_add(vertices=16, radius1=1, radius2=0, depth=2,enter_editmode=True)  
            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.mesh.primitive_cone_add(vertices=16, radius1=1, radius2=0, depth=2)
        
        #Empty Axe
        elif self.primitive == 'empty_axe':
            if context.object is not None :
                bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.empty_add(type='PLAIN_AXES', radius=1)
        
        #Bezier
        elif self.primitive == 'bezier':
            if event.alt:
                if context.object is not None and bpy.context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.curve.primitive_bezier_curve_add(radius=1,enter_editmode=True)      
            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')        
                bpy.ops.curve.primitive_bezier_curve_add(radius=1)
        
        #Text
        elif self.primitive == 'text': 
            if event.alt:
                if context.object is not None and bpy.context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT') 
                bpy.ops.object.text_add(radius=1,enter_editmode=True)     
            
            else:       
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT') 
                bpy.ops.object.text_add(radius=1)
        
        #Torus         
        elif self.primitive == 'torus': 
            if event.alt:
                if context.object is not None and bpy.context.object.mode == "OBJECT":
                    bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.mesh.primitive_torus_add(major_segments=32, minor_segments=12, major_radius=1, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75)  
                bpy.ops.object.mode_set(mode = 'EDIT')
            else:
                if context.object is not None :
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                bpy.ops.mesh.primitive_torus_add(major_segments=32, minor_segments=12, major_radius=1, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75)
                
        #Vertex
        elif self.primitive == 'vertex': 
            if context.object is not None :
                bpy.ops.object.mode_set(mode = 'OBJECT') 
            bpy.ops.view3d.cursor3d('INVOKE_DEFAULT')
            bpy.ops.mesh.primitive_plane_add()
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            bpy.ops.mesh.merge(type='CENTER')
            if bpy.context.space_data.use_occlude_geometry == True :
                bpy.context.space_data.use_occlude_geometry = False
            else :
                pass
            bpy.ops.transform.translate('INVOKE_DEFAULT')
        
        #Curve Line
        elif self.primitive == 'curve_line': 
            if context.object is not None and obj.type == 'MESH':
                bpy.ops.object.mode_set(mode = 'OBJECT') 
            bpy.ops.curve.primitive_bezier_curve_add(view_align=True) 
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.curve.delete(type='VERT')
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.context.object.data.show_normal_face = False
            bpy.ops.curve.draw('INVOKE_DEFAULT')
        
        #Area
        elif self.primitive == 'area': 
            if context.object is not None :
                bpy.ops.object.mode_set(mode = 'OBJECT') 
            bpy.ops.object.lamp_add(type='AREA', radius=1)
        
        #Sun
        elif self.primitive == 'sun': 
            if context.object is not None :
                bpy.ops.object.mode_set(mode = 'OBJECT') 
            bpy.ops.object.lamp_add(type='SUN')
        
        #Spot
        elif self.primitive == 'spot': 
            if context.object is not None :
                bpy.ops.object.mode_set(mode = 'OBJECT') 
            bpy.ops.object.lamp_add(type='SPOT')
            
        #Hemi    
        elif self.primitive == 'hemi': 
            if context.object is not None :
                bpy.ops.object.mode_set(mode = 'OBJECT') 
            bpy.ops.object.lamp_add(type='HEMI')  
        
        #Point    
        elif self.primitive == 'point': 
            if context.object is not None :
                bpy.ops.object.mode_set(mode = 'OBJECT') 
            bpy.ops.object.lamp_add(type='POINT')      
        
#        #Camera
#        elif self.primitive == 'camera': 
#            act_obj = bpy.context.active_object
#            
#            if event.alt :
#                if context.object is not None :
#                    bpy.ops.view3d.snap_cursor_to_selected()
#                    bpy.ops.object.mode_set(mode = 'OBJECT')
#                    
#                bpy.ops.object.empty_add(type='PLAIN_AXES', radius=3)
#                empty = bpy.context.active_object
#                
#            
#            if event.shift:
#                if context.object is not None :
#                    bpy.ops.object.mode_set(mode = 'OBJECT')
#                    bpy.ops.object.select_all(action='DESELECT')
#                else :
#                        
#                bpy.ops.object.camera_add()
#                cam = bpy.context.active_object.name
#                bpy.context.scene.camera = bpy.data.objects[cam]
#                bpy.ops.view3d.camera_to_view()
#                bpy.context.space_data.lock_camera = True
#                bpy.context.scene.render.use_border = True

#                if event.alt :
##                    empty.name = "Empty_Dof_%s" %cam                    
#                    empty.name = "Dof_" + cam
#                    bpy.context.object.data.dof_object = empty
#                    bpy.context.object.data.cycles.aperture_size = 0.5

#                #Select previous object to turn around
#                bpy.ops.object.select_all(action='DESELECT')
#                bpy.context.scene.objects.active=act_obj
#                act_obj.select=True
#    
#            else:
#                bpy.ops.object.camera_add(view_align=False) 

        # Clic> ajoute, ctrl>sur la souris, shift>dans la cam sur la selection, alt>dans la cam + empty dof
             
        #Camera
        elif self.primitive == 'camera': 
            obj = bpy.context.active_object

            if event.shift:
                if len([obj for obj in context.selected_objects if context.object is not None]) >= 1: 
#                if getattr(bpy.context, 'selected_objects')    
                    act_obj = True
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                    bpy.ops.object.select_all(action='DESELECT')
                    
                else:
                    act_obj = False 
                
                #Add cam and go inside        
                bpy.ops.object.camera_add()
                cam = bpy.context.active_object.name
                bpy.context.scene.camera = bpy.data.objects[cam]
                bpy.ops.view3d.camera_to_view()
                bpy.context.space_data.lock_camera = True
                bpy.context.scene.render.use_border = True
                
                if act_obj == True : 
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.context.scene.objects.active = obj 
                    obj.select=True
                    
                else:
                    bpy.ops.object.select_all(action='DESELECT')     
            
             
            elif event.alt :
                if len([obj for obj in context.selected_objects if context.object is not None]) >= 1: 
#                if getattr(bpy.context, 'selected_objects')    
                    act_obj = True
                    bpy.ops.object.mode_set(mode = 'OBJECT')
                    bpy.ops.object.select_all(action='DESELECT')
                    
                else:
                    act_obj = False 
                
                #Create Empty Dof
                bpy.ops.object.empty_add(type='PLAIN_AXES', radius=3)
                empty = bpy.context.active_object    
                            
                #Add cam and go inside        
                bpy.ops.object.camera_add()
                cam = bpy.context.active_object.name
                bpy.context.scene.camera = bpy.data.objects[cam]
                bpy.ops.view3d.camera_to_view()
                bpy.context.space_data.lock_camera = True
                bpy.context.scene.render.use_border = True
                
                #Name empty Dof and use it for camera
                empty.name = "Dof_" + cam
                bpy.context.object.data.dof_object = empty
                bpy.context.object.data.cycles.aperture_size = 0.5
                
                if act_obj == True : 
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.context.scene.objects.active = obj 
                    obj.select=True
                    
                else:
                    bpy.ops.object.select_all(action='DESELECT')     
            
            else:
                bpy.ops.object.camera_add(view_align=False) 
               
#                if context.object is not None :
#                    bpy.ops.view3d.snap_cursor_to_selected()
#                    bpy.ops.object.mode_set(mode = 'OBJECT')
#                    
#                bpy.ops.object.empty_add(type='PLAIN_AXES', radius=3)
#                empty = bpy.context.active_object
        
        if event.ctrl:
            bpy.ops.transform.translate('INVOKE_DEFAULT')
            
        bpy.context.scene.cursor_location = saved_location     
        return {"FINISHED"}   

#Knife tool
class Rmb_knife_Tools(bpy.types.Operator):
    bl_idname = "object.rmb_knife_tools"
    bl_label = "knife Tools"
    bl_description = "knife Tools, shift to cut throught the mesh"
    bl_options = {"REGISTER","UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.context.object.mode == 'EDIT':
            return True

    def invoke(self, context, event):
        obj = context.active_object
          
        if event.shift:
            bpy.ops.mesh.knife_tool('INVOKE_DEFAULT',use_occlude_geometry=False, only_selected=False)
            if event.ctrl:
                bpy.ops.mesh.knife_tool('INVOKE_DEFAULT',use_occlude_geometry=True, only_selected=True)
        else:
            bpy.ops.mesh.knife_tool('INVOKE_DEFAULT',use_occlude_geometry=True, only_selected=False)
        return {"FINISHED"}              
########################################################################
# Pie Menus 
########################################################################

#RMB          
class View3dRightClicMenu(Menu):
    bl_idname = "pie.rightclicmenu"
    bl_label = "RMB Pie Menu"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        wm = bpy.context.window_manager
        obj = context.active_object
        
        ################################################
        # No Objects                                   #
        ################################################
        if bpy.context.area.type == 'VIEW_3D' and not bpy.context.object:
            
            #4 - LEFT
            pie.operator("wm.read_homefile", text="New", icon='NEW')
            #6 - RIGHT
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.scale_y=1.5
            row.operator("wm.recover_last_session", text="Recover Last Session", icon='RECOVER_LAST')
            row = col.row(align=True)
            row.scale_y=1.5
            row.operator("wm.recover_auto_save", text="Recover auto Save", icon='RECOVER_AUTO')
            #2 - BOTTOM
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.separator()
            row = col.row(align=True)
            row.label("Primitives :")
            row = col.row(align=True)
            row.scale_y=1.25
            row.scale_x=1.4
#            if self.use_normal_primitives :
#                row.operator("mesh.primitive_cube_add", text="", icon='MESH_CUBE')
#                row.operator("mesh.primitive_plane_add", text="", icon='MESH_PLANE')
#                row.operator("mesh.primitive_grid_add", text=" ", icon='MESH_GRID')
#                row.operator("mesh.primitive_uv_sphere_add", text="", icon='MESH_UVSPHERE')
#                row.operator("mesh.primitive_cylinder_add", text="", icon='MESH_CYLINDER')
#                row.operator("mesh.primitive_cone_add", text=" ", icon='MESH_CONE')
#                row.operator("mesh.primitive_torus_add", text=" ", icon='MESH_TORUS')
#            else:    
            row.operator("object.rmb_primitives",text="", icon ='MESH_CUBE').primitive = "cube"
            row.operator("object.rmb_primitives",text="", icon ='MESH_PLANE').primitive = "plan"
            row.operator("object.rmb_primitives",text="", icon ='MESH_GRID').primitive = "grid"
            row.operator("object.rmb_primitives", text = "", icon = 'MATSPHERE').primitive = "sphere"
            row.operator("object.rmb_primitives",text="", icon ='MESH_CYLINDER').primitive = "cylinder"
            row.operator("object.rmb_primitives",text="", icon ='MESH_CONE').primitive = "cone"
            row.operator("object.rmb_primitives",text="", icon ='MESH_TORUS').primitive = "torus"
            row.operator("object.rmb_primitives",text="", icon ='OUTLINER_OB_EMPTY').primitive = "empty_axe"
            row.operator("object.rmb_primitives",text="", icon ='CURVE_BEZCURVE').primitive = "bezier"
            row = col.row(align=True)
            row.scale_y=1.25
            row.scale_x=1.4
            row.operator("object.rmb_primitives",text="", icon ='VERTEXSEL').primitive = "vertex"
            row.operator("object.rmb_primitives",text="", icon ='BRUSH_DATA').primitive = "curve_line"
            row.operator("object.rmb_primitives",text="", icon ='OUTLINER_OB_FONT').primitive = "text"
            row.operator("object.rmb_primitives",text="", icon ='OUTLINER_OB_CAMERA').primitive = "camera"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_AREA').primitive = "area"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_SUN').primitive = "sun"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_HEMI').primitive = "hemi"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_SPOT').primitive = "spot"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_POINT').primitive = "point"  
            row = col.row()
            row.label("Editable Primitives :")
            row = col.row(align=True)
            row.scale_y=1.25
            row.scale_x=1.4
            row.operator("mesh.primitive_cube_add", text="", icon='MESH_CUBE')
            row.operator("mesh.primitive_plane_add", text="", icon='MESH_PLANE')
            row.operator("mesh.primitive_grid_add", text="", icon='MESH_GRID')
            row.operator("mesh.primitive_uv_sphere_add", text="", icon='MESH_UVSPHERE')
            row.operator("mesh.primitive_cylinder_add", text="", icon='MESH_CYLINDER')
            row.operator("mesh.primitive_cone_add", text="", icon='MESH_CONE')
            row.operator("mesh.primitive_torus_add", text="", icon='MESH_TORUS')
            #8 - TOP
            pie.operator("wm.save_mainfile", text="Save", icon='FILE_TICK')
            
            #7 - TOP - LEFT 
            pie.operator("wm.open_mainfile", text="Open file", icon='FILE_FOLDER')
            
            #9 - TOP - RIGHT
            pie.operator("wm.save_as_mainfile", text="Save As...", icon='SAVE_AS')
           
            #1 - BOTTOM - LEFT
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.scale_y=1.5
            if hasattr(bpy.types, "IMPORT_SCENE_OT_obj"): 
                row.operator("import_scene.obj", text="Import OBJ", icon='IMPORT')
            else :
                row.label("OBJ", icon='ERROR') 
            
            if hasattr(bpy.types, "IMPORT_SCENE_OT_fbx"):     
                row = col.row(align=True)
                row.scale_y=1.5
                row.operator("import_scene.fbx", text="FBX", icon='IMPORT')
            else :
                row.label("FBX", icon='ERROR')    
            row.operator("wm.alembic_import", text="Alembic", icon='IMPORT')
            
            #3 - BOTTOM - RIGHT
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.scale_y=1.5
            row.scale_x=1.5
            row.operator("wm.link", text="Link", icon='LINK_BLEND')
            row = col.row(align=True)
            row.scale_y=1.5
            row.scale_x=1.5
            row.operator("wm.append", text="Append", icon='APPEND_BLEND')
        
        ################################################
        # Object Mode                                  #
        ################################################    
        elif bpy.context.area.type == 'VIEW_3D' and bpy.context.object.mode == 'OBJECT':
            
            #4 - LEFT
            selection = bpy.context.selected_objects
            if len(bpy.context.selected_objects) == 1:
                pie.operator("object.extract_duplicate", text="Separate", icon='FULLSCREEN_ENTER')
            else:
                pie.operator("object.extract_duplicate", text="Join", icon='FULLSCREEN_EXIT')
                
            #6 - RIGHT
            pie.operator("object.subsurf_operator", text="Subsurf", icon='MOD_SUBSURF')
                
            #2 - BOTTOM
            split = pie.split()
            col = split.column(align=True)
            
            row = col.row(align=True)
            row.label("Primitives :")
            row = col.row(align=True)
            
            row.scale_y=1.25
            row.scale_x=1.4
#            if self.use_normal_primitives :
#                row.operator("mesh.primitive_cube_add", text="", icon='MESH_CUBE')
#                row.operator("mesh.primitive_plane_add", text="", icon='MESH_PLANE')
#                row.operator("mesh.primitive_grid_add", text=" ", icon='MESH_GRID')
#                row.operator("mesh.primitive_uv_sphere_add", text="", icon='MESH_UVSPHERE')
#                row.operator("mesh.primitive_cylinder_add", text="", icon='MESH_CYLINDER')
#                row.operator("mesh.primitive_cone_add", text=" ", icon='MESH_CONE')
#                row.operator("mesh.primitive_torus_add", text=" ", icon='MESH_TORUS')
#            else:    
            row.operator("object.rmb_primitives",text="", icon ='MESH_CUBE').primitive = "cube"
            row.operator("object.rmb_primitives",text="", icon ='MESH_PLANE').primitive = "plan"
            row.operator("object.rmb_primitives",text="", icon ='MESH_GRID').primitive = "grid"
            row.operator("object.rmb_primitives", text = "", icon = 'MATSPHERE').primitive = "sphere"
            row.operator("object.rmb_primitives",text="", icon ='MESH_CYLINDER').primitive = "cylinder"
            row.operator("object.rmb_primitives",text="", icon ='MESH_CONE').primitive = "cone"
            row.operator("object.rmb_primitives",text="", icon ='MESH_TORUS').primitive = "torus"
            row.operator("object.rmb_primitives",text="", icon ='OUTLINER_OB_EMPTY').primitive = "empty_axe"
            row.operator("object.rmb_primitives",text="", icon ='CURVE_BEZCURVE').primitive = "bezier"
            row = col.row(align=True)
            row.scale_y=1.25
            row.scale_x=1.4
            row.operator("object.rmb_primitives",text="", icon ='VERTEXSEL').primitive = "vertex"
            row.operator("object.rmb_primitives",text="", icon ='BRUSH_DATA').primitive = "curve_line"
            row.operator("object.rmb_primitives",text="", icon ='OUTLINER_OB_FONT').primitive = "text"
            row.operator("object.rmb_primitives",text="", icon ='OUTLINER_OB_CAMERA').primitive = "camera"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_AREA').primitive = "area"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_SUN').primitive = "sun"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_HEMI').primitive = "hemi"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_SPOT').primitive = "spot"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_POINT').primitive = "point"  
            row = col.row()
            row.label("Editable Primitives :")
            row = col.row(align=True)
            row.scale_y=1.25
            row.scale_x=1.4
            row.operator("mesh.primitive_cube_add", text="", icon='MESH_CUBE')
            row.operator("mesh.primitive_plane_add", text="", icon='MESH_PLANE')
            row.operator("mesh.primitive_grid_add", text="", icon='MESH_GRID')
            row.operator("mesh.primitive_uv_sphere_add", text="", icon='MESH_UVSPHERE')
            row.operator("mesh.primitive_cylinder_add", text="", icon='MESH_CYLINDER')
            row.operator("mesh.primitive_cone_add", text="", icon='MESH_CONE')
            row.operator("mesh.primitive_torus_add", text="", icon='MESH_TORUS')   
              
            #8 - TOP
            pie.operator("screen.redo_last", text="F6", icon='SCRIPTWIN')
           
            #7 - TOP - LEFT 
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)   
            if hasattr(bpy.types, "OBJECT_OT_automirror"): 
                row.scale_y=1.5
                row.operator("object.automirror", icon = 'MOD_MIRROR')
                row = col.row(align=True)
            else:
                row.label("Automirror", icon='ERROR')   
                row = col.row(align=True)  
            row.operator_menu_enum("object.modifier_add", "type")
            row.operator("object.apply_remove_modifiers", text="", icon='FILE_TICK')
            
            #9 - TOP - RIGHT
            pie.operator("object.parent_objects", text="Parent/Unparent", icon='MOD_SUBSURF')
            
            #1 - BOTTOM - LEFT
            row=pie.row()
            row.scale_y=1.5
            row.operator("object.rmb_apply_transforms", text="Apply Transforms", icon='MANIPUL') 
            
            #3 - BOTTOM - RIGHT
            row=pie.row()
            row.scale_y=1.5
            if bpy.context.object.hide_render == False:
                
                row.operator("object.makeempty", text="Make Empty", icon='OUTLINER_OB_EMPTY')
            else :
                row.operator("object.makeempty", text="Make Normal", icon='MESH_CUBE')
        
        ################################################
        # Edit Mode                                    #
        ################################################    
        elif bpy.context.object.mode == 'EDIT':    

            #4 - LEFT
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.scale_y=1.5
            row.operator("object.rmb_knife_tools", text="Knife", icon='BRUSH_DATA')
            row.operator("object.inset_poke_faces", text="Inset/Poke") 
            
            selection = bpy.context.selected_objects
            row = col.row(align=True)
            row.scale_y=1.5
            if len(bpy.context.selected_objects) == 1:
                
                row.operator("object.extract_duplicate", text="Separate", icon='FULLSCREEN_ENTER')
            else:
                row.operator("object.extract_duplicate", text="Join", icon='FULLSCREEN_EXIT')
            
            #6 - RIGHT
            is_subsurf1 = False
            for mode in bpy.context.object.modifiers :
                if mode.type == 'SUBSURF' :
                    is_subsurf1 = True
            if is_subsurf1 == True :
                pie.operator("object.subsurf_operator", text="Subsurf", icon='MOD_SUBSURF')
            else :
                pie.operator("object.subsurf_operator", text="Subsurf", icon='MOD_SUBSURF')
            
            #2 - BOTTOM
            split = pie.split()
            col = split.column(align=True)
            
            if obj.type == 'MESH':
                row = col.row(align=True)
                row.separator()
                row = col.row(align=True)
                row.separator()
                row = col.row(align=True)
                row.label("Merge :")
                row = col.row(align=True)
                row.scale_y=1.25
                #Vertex
                if tuple (bpy.context.tool_settings.mesh_select_mode) == (True, False, False) :
                    row.operator("mesh.merge", text="First", icon='AUTOMERGE_ON').type='FIRST'
                    row.operator("mesh.merge", text="Center", icon='AUTOMERGE_ON').type='CENTER'
                    row.operator("mesh.merge", text="Last", icon='AUTOMERGE_ON').type='LAST'
                    row = col.row(align=True)
                    row.scale_y=1.25
                    row.operator("mesh.merge", text="Cursor", icon='CURSOR').type='CURSOR'
                    row.operator("mesh.merge", text="Collapse", icon='AUTOMERGE_ON').type='COLLAPSE'
                
                #Edges    
                if tuple (bpy.context.tool_settings.mesh_select_mode) == (False, True, False):
                    row.operator("mesh.merge", text="Cursor", icon='CURSOR').type='CURSOR'
                    row.operator("mesh.merge", text="Center", icon='AUTOMERGE_ON').type='CENTER'
                    row.operator("mesh.merge", text="Collapse", icon='AUTOMERGE_ON').type='COLLAPSE'
                
                #Faces
                if tuple (bpy.context.tool_settings.mesh_select_mode) == (False, False, True):
                    row.operator("mesh.merge", text="Cursor", icon='CURSOR').type='CURSOR'
                    row.operator("mesh.merge", text="Center", icon='AUTOMERGE_ON').type='CENTER'
                    row.operator("mesh.merge", text="Collapse", icon='AUTOMERGE_ON').type='COLLAPSE'     
               
                #Vertex/Edges
                if  tuple (bpy.context.tool_settings.mesh_select_mode) == (True, True, False):  
                    row.operator("mesh.merge", text="First", icon='AUTOMERGE_ON').type='FIRST'
                    row.operator("mesh.merge", text="Center", icon='AUTOMERGE_ON').type='CENTER'
                    row = col.row(align=True)
                    row.scale_y=1.25
                    row.operator("mesh.merge", text="Cursor", icon='CURSOR').type='CURSOR'
                    row.operator("mesh.merge", text="Collapse", icon='AUTOMERGE_ON').type='COLLAPSE'
                
                #Vertex/Edges/faces
                if  tuple (bpy.context.tool_settings.mesh_select_mode) == (True, True, True):  
                    row.operator("mesh.merge", text="Center", icon='AUTOMERGE_ON').type='CENTER'
                    row.operator("mesh.merge", text="Cursor", icon='CURSOR').type='CURSOR'
                    row.operator("mesh.merge", text="Collapse", icon='AUTOMERGE_ON').type='COLLAPSE'       
                
                #Edges/faces
                if  tuple (bpy.context.tool_settings.mesh_select_mode) == (False, True, True):  
                    row.operator("mesh.merge", text="Center", icon='AUTOMERGE_ON').type='CENTER'
                    row.operator("mesh.merge", text="Cursor", icon='CURSOR').type='CURSOR'
                    row.operator("mesh.merge", text="Collapse", icon='AUTOMERGE_ON').type='COLLAPSE'     
            
                #Vertex/faces
                if  tuple (bpy.context.tool_settings.mesh_select_mode) == (True, False, True):  
                    row.operator("mesh.merge", text="Center", icon='AUTOMERGE_ON').type='CENTER'
                    row.operator("mesh.merge", text="Cursor", icon='CURSOR').type='CURSOR'
                    row.operator("mesh.merge", text="Collapse", icon='AUTOMERGE_ON').type='COLLAPSE'   
            
            elif obj.type == 'CURVE':
                row = col.row(align=True)
                row.separator()
                row = col.row(align=True)
                row.separator()
                row = col.row(align=True)
                row.scale_y=1.25
                row.operator("curve.subdivide")
                row = col.row(align=True)
                row.scale_y=1.25
                row.operator("curve.smooth")
                row.operator("transform.vertex_random")
            
            elif obj.type == 'ARMATURE': 
                row = col.row(align=True)
                row.separator()
                row = col.row(align=True)
                row.separator()
                row = col.row(align=True)
                row.scale_y=1.25   
                row.operator("armature.subdivide", text="Subdivide")
                
            row = col.row(align=True)
            row.label("Primitives :")
            row = col.row(align=True)
            row.scale_y=1.25
            row.scale_x=1.4
#            if self.use_normal_primitives :
#                row.operator("mesh.primitive_cube_add", text="", icon='MESH_CUBE')
#                row.operator("mesh.primitive_plane_add", text="", icon='MESH_PLANE')
#                row.operator("mesh.primitive_grid_add", text=" ", icon='MESH_GRID')
#                row.operator("mesh.primitive_uv_sphere_add", text="", icon='MESH_UVSPHERE')
#                row.operator("mesh.primitive_cylinder_add", text="", icon='MESH_CYLINDER')
#                row.operator("mesh.primitive_cone_add", text=" ", icon='MESH_CONE')
#                row.operator("mesh.primitive_torus_add", text=" ", icon='MESH_TORUS')
#            else:    
            row.operator("object.rmb_primitives",text="", icon ='MESH_CUBE').primitive = "cube"
            row.operator("object.rmb_primitives",text="", icon ='MESH_PLANE').primitive = "plan"
            row.operator("object.rmb_primitives",text="", icon ='MESH_GRID').primitive = "grid"
            row.operator("object.rmb_primitives", text = "", icon = 'MATSPHERE').primitive = "sphere"
            row.operator("object.rmb_primitives",text="", icon ='MESH_CYLINDER').primitive = "cylinder"
            row.operator("object.rmb_primitives",text="", icon ='MESH_CONE').primitive = "cone"
            row.operator("object.rmb_primitives",text="", icon ='MESH_TORUS').primitive = "torus"
            row.operator("object.rmb_primitives",text="", icon ='OUTLINER_OB_EMPTY').primitive = "empty_axe"
            row.operator("object.rmb_primitives",text="", icon ='CURVE_BEZCURVE').primitive = "bezier"
            row = col.row(align=True)
            row.scale_y=1.25
            row.scale_x=1.4
            row.operator("object.rmb_primitives",text="", icon ='VERTEXSEL').primitive = "vertex"
            row.operator("object.rmb_primitives",text="", icon ='BRUSH_DATA').primitive = "curve_line"
            row.operator("object.rmb_primitives",text="", icon ='OUTLINER_OB_FONT').primitive = "text"
            row.operator("object.rmb_primitives",text="", icon ='OUTLINER_OB_CAMERA').primitive = "camera"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_AREA').primitive = "area"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_SUN').primitive = "sun"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_HEMI').primitive = "hemi"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_SPOT').primitive = "spot"
            row.operator("object.rmb_primitives",text="", icon ='LAMP_POINT').primitive = "point"  
            row = col.row()
            row.label("Editable Primitives :")
            row = col.row(align=True)
            row.scale_y=1.25
            row.scale_x=1.4
            row.operator("mesh.primitive_cube_add", text="", icon='MESH_CUBE')
            row.operator("mesh.primitive_plane_add", text="", icon='MESH_PLANE')
            row.operator("mesh.primitive_grid_add", text="", icon='MESH_GRID')
            row.operator("mesh.primitive_uv_sphere_add", text="", icon='MESH_UVSPHERE')
            row.operator("mesh.primitive_cylinder_add", text="", icon='MESH_CYLINDER')
            row.operator("mesh.primitive_cone_add", text="", icon='MESH_CONE')
            row.operator("mesh.primitive_torus_add", text="", icon='MESH_TORUS')  
            
            #8 - TOP
            pie.operator("screen.redo_last", text="F6", icon='SCRIPTWIN')
            #7 - TOP - LEFT 
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)   
            if hasattr(bpy.types, "OBJECT_OT_automirror"): 
                row.scale_y=1.5
                row.operator("object.automirror", icon = 'MOD_MIRROR')
                row = col.row(align=True)
            else:
                row.label("Automirror", icon='ERROR')   
                row = col.row(align=True) 
            row.scale_y=1.25 
            row.operator_menu_enum("object.modifier_add", "type")
            row.operator("object.apply_remove_modifiers", text="", icon='FILE_TICK')
            
            #9 - TOP - RIGHT
            box = pie.split().column()
            row = box.split(percentage=0.6)
            row.scale_y=1.25
            if hasattr(bpy.types, "MESH_OT_offset_edges"):
                row.operator("mesh.offset_edges", text="Offset Edges", icon='UV_EDGESEL')
            else:
                row.label("Offset Edges", icon='ERROR')      
            
            if hasattr(bpy.types, "MESH_OT_looptools_bridge"):
                row.menu("loop.tools")
            else:
                row.label("Looptools", icon='ERROR')    
            split = box.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.scale_y=1.25
            row.operator("mesh.fill_grid", text="Grid Fill")
            row = col.row(align=True)
            row.scale_y=1.25
            row.operator("object.mark_clear_seam", "Seam", icon='UV_EDGESEL')
            row.operator("object.unwrap", "Unwrap", icon='MOD_UVPROJECT')
            
            #1 - BOTTOM - LEFT
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.scale_y=1.5
            row.operator("mesh.loopcut", text="Loopcut").smoothness=1
            
            if hasattr(bpy.types, "MESH_OT_looptools_bridge"):
                row.operator("object.createhole",text="circle", icon='CLIPUV_DEHLT')
            else:
                row.label("Looptools", icon='ERROR')    
            
            row.operator("simplify.circle",text="Simplify", icon='MESH_CIRCLE')
            
            row = col.row(align=True)
            row.scale_y=1.5
            row.operator("retopo.space", icon='ALIGN', text="Distribute")
            if hasattr(bpy.types, "MESH_OT_vertex_align"): 
                row.operator("mesh.vertex_align", icon='ALIGN', text="Align")
                row.operator("mesh.vertex_inline", icon='ALIGN', text="Ali & Dis")
            
            else:
                row.label("Vertex Tools", icon='ERROR')  
            #3 - BOTTOM - RIGHT
            split = pie.split()
            col = split.column(align=True)
            row = col.row(align=True)
            row.scale_y=1.25
            row.operator("mesh.flip_normals",text="Flip Norm", icon = 'FILE_REFRESH')
            row.operator("mesh.normals_make_consistent",text="consistant", icon = 'MATCUBE')
            row = col.row(align=True)
            row.scale_y=1.25
            row.operator("wm.context_toggle", text="Show Norm", icon='FACESEL').data_path = "object.data.show_normal_face"
            row.operator("mesh.remove_doubles", text="rem Double",icon='X')
            row = col.row(align=True)
            row.scale_y=1.25
            row.operator("wm.context_toggle", text="Mirror X ", icon='MOD_MIRROR').data_path = "object.data.use_mirror_x"


# -----------------------------------------------------------------------------
#    Keymap      
# ----------------------------------------------------------------------------- 
addon_keymaps = [] 
         
def get_hotkey_entry_item(km, kmi_name, kmi_value):
    '''
    returns hotkey of specific type, with specific properties.name (keymap is not a dict, so referencing by keys is not enough
    if there are multiple hotkeys!)
    '''
    for i, km_item in enumerate(km.keymap_items):
        if km.keymap_items.keys()[i] == kmi_name:
            if kmi_value:
                if km.keymap_items[i].properties.name == kmi_value:
                    return km_item
            return km_item
    return None 


def add_hotkey():
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon 
    
    # Set 3d cursor with double click LMB
    km = kc.keymaps.new(name="3D View Generic", space_type='VIEW_3D', region_type = 'WINDOW')  
    kmi = km.keymap_items.new('view3d.cursor3d', 'LEFTMOUSE', 'DOUBLE_CLICK', alt=True)
    
    
    km = kc.keymaps.new(name="3D View Generic", space_type='VIEW_3D', region_type = 'WINDOW')  
    kmi = km.keymap_items.new("wm.call_menu_pie", 'ACTIONMOUSE', 'PRESS') 
    kmi.properties.name = "pie.rightclicmenu"                           
    kmi.active = True
    
    addon_keymaps.append((km, kmi))


class Template_Add_Hotkey(bpy.types.Operator):
    ''' Add hotkey entry '''
    bl_idname = "template.add_hotkey"
    bl_label = "Addon Preferences Example"
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        add_hotkey()

        self.report({'INFO'}, "Hotkey added in User Preferences -> Input -> Screen -> Screen (Global)")
        return {'FINISHED'}
    
    
def remove_hotkey():
    ''' clears all addon level keymap hotkeys stored in addon_keymaps '''
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    km = kc.keymaps['3D View Generic']
    
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()   

# -----------------------------------------------------------------------------
#    Register      
# -----------------------------------------------------------------------------  
 
def register():
    bpy.utils.register_module(__name__)

    # hotkey setup
    add_hotkey()
    
def unregister():
    bpy.utils.unregister_module(__name__)
    
    # hotkey cleanup
    remove_hotkey()
 
if __name__ == "__main__":
    register()     

if __name__ == "__main__":
    register()    