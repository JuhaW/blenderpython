#
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

#bl_info = {
#    "name": "Spacebar Main Menus",
#    "author": "mkbreuer",
#    "version": (0, 1, 0),
#    "blender": (2, 7, 2),
#    "location": "View3D / Key:",
#    "description": "Spacebar Main Menus",
#    "warning": "",
#    "wiki_url": "",
#    "category": "User Menu",
#}

import bpy
from bpy import *


#############################################################################################################################################################
#############################################################################################################################################################
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ###  
### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ### Sub Menus ###  
#############################################################################################################################################################
#############################################################################################################################################################


#######  Menus Add  #######-------------------------------------------------------                  
#######  Menus Add  #######-------------------------------------------------------        

class VIEW3D_MT_add_menus(bpy.types.Menu):
    bl_label = "Add Menu"

    def draw(self, context):
        self.draw_menus(self.layout, context)

    @staticmethod
    def draw_menus(layout, context):
        obj = context.active_object
        mode_string = context.mode
        edit_object = context.edit_object

        if mode_string == 'OBJECT':
            layout.menu("INFO_MT_add", text="Add")
        elif mode_string == 'EDIT_MESH':
            layout.menu("INFO_MT_mesh_add", text="Add")
        elif mode_string == 'EDIT_CURVE':
            layout.menu("INFO_MT_curve_add", text="Add")
        elif mode_string == 'EDIT_SURFACE':
            layout.menu("INFO_MT_surface_add", text="Add")
        elif mode_string == 'EDIT_METABALL':
            layout.menu("INFO_MT_metaball_add", text="Add")
        elif mode_string == 'EDIT_ARMATURE':
            layout.menu("INFO_MT_edit_armature_add", text="Add")

#bpy.utils.register_class(VIEW3D_MT_add_menus)             



#######  Menus Relations  #######-------------------------------------------------------                  
#######  Menus Relations  #######-------------------------------------------------------        

class VIEW3D_MT_Relation_Menu(bpy.types.Menu):
    bl_label = "Relation Menu"

    def draw(self, context):
        layout = self.layout
        
        obj = context
        if obj and obj.mode == 'OBJECT':      
            
            layout.menu("VIEW3D_MT_Parent_Menu", icon="CONSTRAINT")
            layout.menu("VIEW3D_MT_Group_Menu")
            layout.menu("VIEW3D_MT_Constraint_Menu")

            layout.separator()
        
            layout.menu("VIEW3D_MT_make_links", text="M.Links", icon="LINKED")
            layout.menu("VIEW3D_MT_make_single_user", text="Single User")
        
            layout.separator()

            layout.operator("object.visual_transform_apply", icon="NDOF_DOM")
        
            layout.separator()
        
            layout.operator("object.duplicates_make_real")
        
            layout.separator()
        
            layout.operator("help.relation",text="make single from dupli", icon="INFO")            
       
        
        obj = context
        if obj and obj.mode == 'EDIT_ARMATURE':
            layout.menu("VIEW3D_MT_edit_armature_parent", icon='CONSTRAINT')              
        
        obj = context
        if obj and obj.mode == 'POSE':
            arm = context.active_object.data
       
            layout.menu("VIEW3D_MT_object_parent", icon='CONSTRAINT')
            layout.menu("VIEW3D_MT_pose_ik")
            layout.menu("VIEW3D_MT_pose_constraints")

#bpy.utils.register_class(VIEW3D_MT_Relation_Menu) 



class help4_text(bpy.types.Operator):
	bl_idname = "help.relation"
	bl_label = ''

	def draw(self, context):
		layout = self.layout
		layout.label('1. parent selected to activ')
		layout.label('2. apply Make Duplicates Real')
		layout.label('3. clear Parent / 4. to Join > selected Linked Object Data')
	
	def execute(self, context):
		return {'FINISHED'}

	def invoke(self, context, event):
		return context.window_manager.invoke_popup(self, width = 300)

#bpy.utils.register_class(help4_text)
 

            
######  Menus Constraint  ######-------------------------------------
######  Menus Constraint  ######-------------------------------------

class VIEW3D_MT_Constraint_Menu(bpy.types.Menu):
    bl_label = "Constraint Menu"

    def draw(self, context):
        layout = self.layout

        layout.operator_menu_enum("object.constraint_add", "type", text="  Constraint", icon="CONSTRAINT_DATA") 
        #layout.operator("object.track_set",text=">>>  Track  <<<")

        layout.separator()
        
        layout.label(text="to Selected:",icon="LAYER_ACTIVE")
        layout.operator("track.to", text="-> Track To")
        layout.operator("damped.track", text="-> Damped Track")
        layout.operator("lock.track", text="-> Lock Track")

        layout.separator()
        
        layout.label(text="to CursorPos+Empty:",icon="LAYER_ACTIVE")
        layout.operator("track.toempty", text="-> Track To")
        layout.operator("damped.trackempty", text="-> Damped Track")
        layout.operator("lock.trackempty", text="-> Lock Track")

#bpy.utils.register_class(VIEW3D_MT_Constraint_Menu)



######  Menus Parent  ######-------------------------------------
######  Menus Parent  ######-------------------------------------

class VIEW3D_MT_Parent_Menu(bpy.types.Menu):
    bl_label = "Parent Menu"

    def draw(self, context):
        layout = self.layout
        
        layout.operator("object.parent_set", text="Set")
        
        layout.separator()

        layout.operator("object.parent_clear").type="CLEAR"
        layout.operator("object.parent_clear", text="Clear Inverse").type="CLEAR_INVERSE" 
        layout.operator("object.parent_clear", text="Clear Keep Transform").type="CLEAR_KEEP_TRANSFORM"

#bpy.utils.register_class(VIEW3D_MT_Parent_Menu)



######  Menus Group  ######-------------------------------------             
######  Menus Group  ######-------------------------------------

class VIEW3D_MT_Group_Menu(bpy.types.Menu):
    bl_label = "Group Menu"

    def draw(self, context):
        layout = self.layout

        layout.operator("group.create", text="Group")
        layout.operator("group.objects_add_active", text="-> to Active")
        
        layout.separator()
        
        layout.operator("group.objects_remove", text="Remove")
        layout.operator("group.objects_remove_active", text="-> from Active")

#bpy.utils.register_class(VIEW3D_MT_Group_Menu)


#######  Menus Multi Select  #######-------------------------------------------------------                  
#######  Menus Multi Select  #######-------------------------------------------------------                  

class VIEW3D_MT_edit_multi(bpy.types.Menu):
    bl_label = "Multi Select"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        prop = layout.operator("wm.context_set_value", text="Vertex Select", icon='VERTEXSEL')
        prop.value = "(True, False, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Edge Select", icon='EDGESEL')
        prop.value = "(False, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Face Select", icon='FACESEL')
        prop.value = "(False, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"
        
        layout.separator()

        prop = layout.operator("wm.context_set_value", text="Vertex & Edge Select", icon='EDITMODE_HLT')
        prop.value = "(True, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Vertex & Face Select", icon='ORTHO')
        prop.value = "(True, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Edge & Face Select", icon='SNAP_FACE')
        prop.value = "(False, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"
        layout.separator()

        prop = layout.operator("wm.context_set_value", text="Vertex & Edge & Face Select", icon='SNAP_VOLUME')
        prop.value = "(True, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

#bpy.utils.register_class(VIEW3D_MT_edit_multi)

      

#######  Menus Snap to  #######-------------------------------------------------------                  
#######  Menus Snap to  #######-------------------------------------------------------                  

class VIEW3D_MT_SnaptoMenu(bpy.types.Menu):
    bl_label = "Snap to Menu"

    def draw(self, context):

        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.label("Cursor to",icon = "FORCE_FORCE")   
         
        layout.operator("view3d.snap_cursor_to_grid", text="Grid")
        layout.operator("view3d.snap_cursor_to_center", text="Center")
        layout.operator("view3d.snap_cursor_to_active", text="Active")    
        layout.operator("view3d.snap_cursor_to_selected", text="-Selected")
        
        layout.separator()

        layout.label("Selection to", icon = "RESTRICT_SELECT_OFF") 
         
        layout.operator("view3d.snap_selected_to_grid", text="Grid")       
        layout.operator("view3d.snap_selected_to_cursor", text="Cursor")

        if obj and obj.mode == 'EDIT':   
            layout.separator()
            
            layout.operator("transform.snap_type", text="Snap Tools", icon='SNAP_ON')    
            layout.operator("view3d.snap_cursor_to_edge_intersection", text="Cursor to Edge Intersection")
            
#bpy.utils.register_class(VIEW3D_MT_SnaptoMenu)
           
                   
                        
#######  Menus Particle  #######-------------------------------------------------------                  
#######  Menus Particle  #######------------------------------------------------------- 

class VIEW3D_Paint_Particle(bpy.types.Menu):
    bl_label = "Particles"

    def draw(self, context):
        layout = self.layout

        particle_edit = context.tool_settings.particle_edit

        layout.operator("particle.mirror")

        layout.separator()

        layout.operator("particle.subdivide")

        layout.separator()        

        layout.operator("particle.rekey")
        layout.operator("particle.weight_set")

#bpy.utils.register_class(VIEW3D_Paint_Particle)
  


#######  Menus Weights  #######-------------------------------------------------------                  
#######  Menus Weights  #######------------------------------------------------------- 

class VIEW3D_Paint_Weight(bpy.types.Menu):
    bl_label = "Weights"

    def draw(self, context):
        layout = self.layout

        layout.operator("paint.weight_from_bones", text="Assign Automatic From Bones").type = 'AUTOMATIC'
        layout.operator("paint.weight_from_bones", text="Assign From Bone Envelopes").type = 'ENVELOPES'

        layout.separator()

        layout.operator("object.vertex_group_normalize_all", text="Normalize All")
        layout.operator("object.vertex_group_normalize", text="Normalize")
        layout.operator("object.vertex_group_mirror", text="Mirror")
        layout.operator("object.vertex_group_invert", text="Invert")

        layout.separator()
        
        layout.operator("object.vertex_group_clean", text="Clean")
        layout.operator("object.vertex_group_quantize", text="Quantize")
        layout.operator("object.vertex_group_levels", text="Levels")
        layout.operator("object.vertex_group_blend", text="Blend")

        layout.separator()
        
        layout.operator("object.vertex_group_transfer_weight", text="Transfer Weights")
        layout.operator("object.vertex_group_limit_total", text="Limit Total")
        layout.operator("object.vertex_group_fix", text="Fix Deforms")

        layout.separator()

        layout.operator("paint.weight_set")

#bpy.utils.register_class(VIEW3D_Paint_Weight)


#######  Menus Sculpt  #######-------------------------------------------------------                  
#######  Menus Sculpt  #######------------------------------------------------------- 

class VIEW3D_MT_Sculptmode(bpy.types.Menu):
    bl_label = "Sculpt"

    def draw(self, context):
        layout = self.layout

        toolsettings = context.tool_settings
        sculpt = toolsettings.sculpt

        layout.prop(sculpt, "use_symmetry_x")
        layout.prop(sculpt, "use_symmetry_y")
        layout.prop(sculpt, "use_symmetry_z")
        layout.separator()
        layout.prop(sculpt, "lock_x")
        layout.prop(sculpt, "lock_y")
        layout.prop(sculpt, "lock_z")

        layout.separator()
        layout.prop(sculpt, "use_threaded", text="Threaded Sculpt")
        layout.prop(sculpt, "show_low_resolution")
        layout.prop(sculpt, "show_brush")
        layout.prop(sculpt, "use_deform_only")
        layout.prop(sculpt, "show_diffuse_color")
        
#bpy.utils.register_class(VIEW3D_MT_Sculptmode) 
        
                

#######  Menus Armature  #######-------------------------------------------------------                  
#######  Menus Armature  #######------------------------------------------------------- 

class VIEW3D_MT_EditArmatureTK(bpy.types.Menu):
    bl_label = "Armature Tools"

    def draw(self, context):
        layout = self.layout

        # Edit Armature

        layout.operator("transform.transform", text="Scale Envelope Distance").mode = 'BONE_SIZE'

        layout.operator("transform.transform", text="Scale B-Bone Width").mode = 'BONE_SIZE'
        
        layout.separator()

        layout.operator("armature.extrude_move")

        layout.operator("armature.extrude_forked")

        layout.operator("armature.duplicate_move")
        layout.operator("armature.merge")
        layout.operator("armature.fill")
        layout.operator("armature.delete")
        layout.operator("armature.separate")

        layout.separator()

        layout.operator("armature.subdivide", text="Subdivide")
        layout.operator("armature.switch_direction", text="Switch Direction")

#bpy.utils.register_class(VIEW3D_MT_EditArmatureTK) 
        

class VIEW3D_MT_ArmatureName(bpy.types.Menu):
    bl_label = "Armature Name"

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'EXEC_AREA'
        
        layout.operator("armature.autoside_names", text="AutoName Left/Right").type = 'XAXIS'
        layout.operator("armature.autoside_names", text="AutoName Front/Back").type = 'YAXIS'
        layout.operator("armature.autoside_names", text="AutoName Top/Bottom").type = 'ZAXIS'
        layout.operator("armature.flip_names")

#bpy.utils.register_class(VIEW3D_MT_ArmatureName) 
        

class VIEW3D_MT_ArmatureCut(bpy.types.Menu):
    bl_label = "Subdivide"

    def draw(self, context):
        layout = self.layout
  
        layout.operator("armature.subdivide",text="1-Cut").number_cuts=1
        layout.operator("armature.subdivide",text="2-Cuts").number_cuts=2
        layout.operator("armature.subdivide",text="3-Cuts").number_cuts=3
        layout.operator("armature.subdivide",text="4-Cuts").number_cuts=4
        layout.operator("armature.subdivide",text="5-Cuts").number_cuts=5
        layout.operator("armature.subdivide",text="6-Cuts").number_cuts=6     

#bpy.utils.register_class(VIEW3D_MT_ArmatureCut) 
        
 

#######  Menus Pose  #######-------------------------------------------------------                  
#######  Menus Pose  #######------------------------------------------------------- 

class VIEW3D_MT_PoseCopy(bpy.types.Menu):
    bl_label = "Pose Copy"

    def draw(self, context):
        layout = self.layout

        layout.operator("pose.copy")
        layout.operator("pose.paste")
        layout.operator("pose.paste", text="Paste X-Flipped Pose").flipped = True
        
        layout.separator()

bpy.utils.register_class(VIEW3D_MT_PoseCopy) 


class VIEW3D_MT_PoseNames(bpy.types.Menu):
    bl_label = "Pose Copy"

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'EXEC_AREA'
        layout.operator("pose.autoside_names", text="AutoName Left/Right").axis = 'XAXIS'
        layout.operator("pose.autoside_names", text="AutoName Front/Back").axis = 'YAXIS'
        layout.operator("pose.autoside_names", text="AutoName Top/Bottom").axis = 'ZAXIS'

        layout.operator("pose.flip_names")

#bpy.utils.register_class(VIEW3D_MT_PoseNames) 



#######  Menus Sculpt  #######-------------------------------------------------------                  
#######  Menus Sculpt  #######------------------------------------------------------- 

class VIEW3D_SculptBrush(bpy.types.Menu):
    bl_label = "Sculpt Brushes"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'        

        layout.operator("paint.brush_select", text='Blob', icon='BRUSH_BLOB').sculpt_tool= 'BLOB'
        
        #layout.separator()        
        
        layout.operator("paint.brush_select", text="Clay", icon='BRUSH_CLAY').sculpt_tool='CLAY'        
        layout.operator("paint.brush_select", text='Claystrips', icon='BRUSH_CREASE').sculpt_tool= 'CLAY_STRIPS'
        
        #layout.separator()
        
        layout.operator("paint.brush_select", text="Crease", icon='BRUSH_CREASE').sculpt_tool='CREASE'

        layout.operator("paint.brush_select", text='Brush', icon='BRUSH_SCULPT_DRAW').sculpt_tool='DRAW'
        layout.operator("paint.brush_select", text='Fill/Deepen', icon='BRUSH_FILL').sculpt_tool='FILL'

        layout.operator("paint.brush_select", text='Flatten', icon='BRUSH_FLATTEN').sculpt_tool='FLATTEN'
        layout.operator("paint.brush_select", text='Grab', icon='BRUSH_GRAB').sculpt_tool='GRAB'

        layout.operator("paint.brush_select", text='Inflate/Deflate', icon='BRUSH_INFLATE').sculpt_tool='INFLATE'
        layout.operator("paint.brush_select", text='Layer', icon='BRUSH_LAYER').sculpt_tool= 'LAYER'

        layout.operator("paint.brush_select", text='Mask', icon='BRUSH_MASK').sculpt_tool='MASK'
        layout.operator("paint.brush_select", text='Nudge', icon='BRUSH_NUDGE').sculpt_tool= 'NUDGE'

        layout.operator("paint.brush_select", text='Pinch/Magnify', icon='BRUSH_PINCH').sculpt_tool= 'PINCH'
        layout.operator("paint.brush_select", text='Twist', icon='BRUSH_ROTATE').sculpt_tool= 'ROTATE'

        layout.operator("paint.brush_select", text='Scrape/Peaks', icon='BRUSH_SCRAPE').sculpt_tool= 'SCRAPE'
        layout.operator("paint.brush_select", text='Polish', icon='BRUSH_FLATTEN')

        layout.operator("paint.brush_select", text='Smooth', icon='BRUSH_SMOOTH').sculpt_tool= 'SMOOTH'
        layout.operator("paint.brush_select", text='Snakehook', icon='BRUSH_SNAKE_HOOK').sculpt_tool= 'SNAKE_HOOK'

        layout.operator("paint.brush_select", text='Thumb', icon='BRUSH_THUMB').sculpt_tool= 'THUMB'
 
#bpy.utils.register_class(VIEW3D_SculptBrush) 

   

#######  Menus Texture  #######-------------------------------------------------------                  
#######  Menus Texture  #######------------------------------------------------------- 

class VIEW3D_TextureBrush(bpy.types.Menu):
    bl_label = "Texture Brushes"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN' 
        
        #layout.operator("paint.brush_select", text='Brush', icon='BRUSH_TEXDRAW').texture_paint_tool= 'BRUSH'               
        layout.operator("paint.brush_select", text='Clone', icon='BRUSH_CLONE').texture_paint_tool= 'CLONE'
        
        layout.operator("paint.brush_select", text='Draw', icon='BRUSH_TEXDRAW').texture_paint_tool= 'DRAW'
        layout.operator("paint.brush_select", text='Fill', icon='BRUSH_TEXFILL').texture_paint_tool= 'FILL'               
        
        layout.operator("paint.brush_select", text='Mask', icon='BRUSH_TEXMASK').texture_paint_tool= 'MASK'
        layout.operator("paint.brush_select", text='Smear', icon='BRUSH_SMEAR').texture_paint_tool= 'SMEAR'
          
        layout.operator("paint.brush_select", text='Soften', icon='BRUSH_SOFTEN').texture_paint_tool= 'SOFTEN'               
        layout.operator("paint.brush_select", text='TexDraw', icon='BRUSH_TEXDRAW').texture_paint_tool= 'TEXDRAW'
 
#bpy.utils.register_class(VIEW3D_TextureBrush) 



#######  Menus Vertex & Weight  #######-------------------------------------------------------                  
#######  Menus Vertex & Weight  #######------------------------------------------------------- 

class VIEW3D_VertexBrush(bpy.types.Menu):
    bl_label = "Vertex Brushes"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN' 
        
        layout.operator("paint.brush_select", text='Add', icon='BRUSH_ADD').vertex_paint_tool= 'ADD'               
        layout.operator("paint.brush_select", text='Blur', icon='BRUSH_MIX').vertex_paint_tool= 'BLUR'
        
        layout.operator("paint.brush_select", text='Darken', icon='BRUSH_DARKEN').vertex_paint_tool= 'DARKEN'               
        layout.operator("paint.brush_select", text='Lighten', icon='BRUSH_LIGHTEN').vertex_paint_tool= 'LIGHTEN'
          
        layout.operator("paint.brush_select", text='Mix', icon='BRUSH_MIX').vertex_paint_tool= 'MIX'               
        layout.operator("paint.brush_select", text='Multiply', icon='BRUSH_MULTIPLY').vertex_paint_tool= 'MUL'
     
        layout.operator("paint.brush_select", text='Substract', icon='BRUSH_SUBTRACT').vertex_paint_tool= 'SUB'                      

#bpy.utils.register_class(VIEW3D_VertexBrush) 


#######  AnimationPlayer  #######-------------------------------------------------------                  
#######  AnimationPlayer  #######------------------------------------------------------- 

class VIEW3D_AnimationPlayer(bpy.types.Menu):
    bl_label = "Animation Player"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        toolsettings = context.tool_settings
        screen = context.screen

        layout.operator("screen.frame_jump", text="Jump REW", icon='REW').end = False
        layout.operator("screen.keyframe_jump", text="Previous FR", icon='PREV_KEYFRAME').next = False
        layout.operator("screen.animation_play", text="Reverse", icon='PLAY_REVERSE').reverse = True
        
        layout.operator("screen.animation_play", text="PLAY", icon='PLAY')
        
        layout.operator("screen.animation_play", text="Stop", icon='PAUSE')
        
        layout.operator("screen.keyframe_jump", text="Next FR", icon='NEXT_KEYFRAME').next = True
        layout.operator("screen.frame_jump", text="Jump FF", icon='FF').end = True    

#bpy.utils.register_class(VIEW3D_AnimationPlayer) 



#######  BoolTool  #######-------------------------------------------------------                  
#######  BoolTool  #######------------------------------------------------------- 

class BoolToolMenu(bpy.types.Menu):
    bl_label = "BoolTool"
    bl_idname = "space_booltool"

    
    def draw(self, context):
        layout = self.layout

        layout.operator("btool.boolean_union", text = "Union Brush",icon = "ROTATECOLLECTION")
        layout.operator("btool.boolean_inters", text ="Intersection Brush",icon = "ROTATECENTER")
        layout.operator("btool.boolean_diff", text ="Difference Brush",icon = "ROTACTIVE")
        
        layout.separator()

        layout.operator("btool.boolean_union_direct", text = "Union Brush",icon = "ROTATECOLLECTION")
        layout.operator("btool.boolean_inters_direct", text ="Intersection Brush",icon = "ROTATECENTER")
        layout.operator("btool.boolean_diff_direct", text ="Difference Brush",icon = "ROTACTIVE")
        
        layout.separator()  
              
        layout.operator("btool.draw_polybrush",icon = "LINE_DATA")

#bpy.utils.register_class(BoolToolMenu) 



#########################################################################################################################################################
#########################################################################################################################################################
### Repeat Menus ### Repeat Menus ### Repeat Menus ### Repeat Menus ### Repeat Menus ### Repeat Menus ### Repeat Menus ### Repeat Menus ### Repeat Menus 
### Repeat Menus ### Repeat Menus ### Repeat Menus ### Repeat Menus ### Repeat Menus ### Repeat Menus ### Repeat Menus ### Repeat Menus ### Repeat Menus   
#########################################################################################################################################################
#########################################################################################################################################################


######  Spacebar Bottom1 History  ######-------------------------------------------------------                          
######  Spacebar Bottom1 History  ######-------------------------------------------------------                        
      
def draw_spacebar_bottom1_history_tools(context, layout):
    view = context.space_data
    obj = context.active_object
    toolsettings = context.tool_settings
    settings = context.tool_settings
    layout.operator_context = 'INVOKE_REGION_WIN'
    
    ###--- Bottom1 ---###
    
    layout.menu("space_viewextend", text="Mode", icon = "OBJECT_DATA")
    #layout.menu("space_viewcustom", text="Editor", icon = "GO_LEFT")             

    #layout.separator()      
    # Editor Menu
    layout.operator("object.editmode_toggle", text="Fast Toggle")

    layout.separator()
    
    layout.operator("view3d.properties", icon='MENU_PANEL')
    layout.operator("view3d.toolshelf", icon='MENU_PANEL')
    


######  Spacebar Bottom2 History  ######-------------------------------------------------------                         
######  Spacebar Bottom2 History  ######-------------------------------------------------------                         
      
def draw_spacebar_bottom2_history_tools(context, layout):
    view = context.space_data
    obj = context.active_object
    toolsettings = context.tool_settings
    settings = context.tool_settings
    layout.operator_context = 'INVOKE_REGION_WIN'

    ###--- Bottom1 ---###


    # Delete Menu
    layout.menu("space_delete", icon = "PANEL_CLOSE")

    obj = context
    if obj and obj.mode == 'EDIT_MESH':    
        layout.menu("cleanup", text="Clean Up")
 
    layout.separator()        

    layout.menu("space_viewextend", text="Mode", icon = "OBJECT_DATA")
    #layout.menu("space_viewcustom", text="Editor", icon = "GO_LEFT")    

    # Editor Menu
    layout.operator("object.editmode_toggle", text="Fast Toggle")    

    layout.separator()
    
    layout.operator("view3d.properties", icon='MENU_PANEL')
    layout.operator("view3d.toolshelf", icon='MENU_PANEL')





######  Transform  / Pivot  ######-------------------------------------------------------  
######  Transform  / Pivot  ######-------------------------------------------------------

class VIEW3D_Transform_Menu(bpy.types.Menu):
    bl_label = "Transform"
    bl_idname ="space_transform"    

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        wm = context.window_manager
        layout.operator_context = 'INVOKE_REGION_WIN'

        obj = context.active_object    

        layout.operator("transform.translate", text="Grab/Move", icon = "MAN_TRANS")
        layout.operator("transform.rotate", text="Rotate", icon = "MAN_ROT")
        layout.operator("transform.resize", text="Scale", icon = "MAN_SCALE")

        layout.separator()
        
        layout.label("Edit Transform", icon = "UV_SYNC_SELECT")

        layout.operator("transform.tosphere", text="Sphere")
        layout.operator("transform.shear", text="Shear")
        layout.operator("transform.bend", text="Bend")
        layout.operator("transform.push_pull", text="Push/Pull")
        if context.edit_object and context.edit_object.type == 'ARMATURE':
            layout.operator("armature.align", icon = "OUTLINER_DATA_ARMATURE")
        else:
            layout.operator_context = 'EXEC_REGION_WIN'
            layout.separator()
            
            layout.operator("transform.transform",text="Align to Transform Orientation").mode = 'ALIGN'

        layout.separator()
                
        # Apply
        if obj and obj.mode == 'OBJECT':
                # Apply and Clear Menu
                layout.menu("space_apply_transform", text = "Apply", icon = "FILE_TICK")    
                layout.menu("space_clear_transform", text = "Clear", icon = "PANEL_CLOSE") 
        # Apply
        if obj and obj.mode == 'POSE':
                # Apply and Clear Menu
                layout.menu("space_applyclearpose", text = "Apply / Clear", icon = "PANEL_CLOSE") 

#bpy.utils.register_class(VIEW3D_TransformPivot_Menu) 


         
######  View Menu  ######------------------------------------------------------- 
######  View Menu  ######------------------------------------------------------- 

class VIEW3D_Object_View(bpy.types.Menu):
    bl_label = "Object View"
    bl_idname ="space_viewobjectmenu"

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        wm = context.window_manager
        layout.operator_context = 'INVOKE_REGION_WIN'
       

        #Shade Menu
        layout.menu("space_shade_menu", text = "Shade")
                                
        # Object & Mesh View Menu
        layout.menu("space_object", text="Object") 
    
        # 3D View Menu 
        layout.menu("space_3dview", text="3D Display")

        layout.separator()      

        # Flymode for HighPoly
     
        layout.operator("view3d.fast_navigate_operator", icon = "MOD_SOFT")
        layout.operator("view3d.fast_navigate_stop_new")
        
        layout.menu("space_modifly", text="Setting")         
     

        
        
#bpy.utils.register_class(VIEW3D_ViewMode_Menu) 



#############################################################################################################################################################
#############################################################################################################################################################
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
#############################################################################################################################################################
#############################################################################################################################################################

      
######  Spacebar Main Menu  ######-------------------------------------------------------
######  Spacebar Main Menu  ######-------------------------------------------------------

class VIEW3D_MT_Space_Display(bpy.types.Menu):
    bl_label = "Spacebar Menu"
    bl_idname ="space_spacebarmenu"    

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        wm = context.window_manager
        layout.operator_context = 'INVOKE_REGION_WIN'


##########--------------##########
##########  Objectmode  ##########
##########--------------##########  

        ob = context
        if ob.mode == 'OBJECT':
            
            # Search
            layout.operator("wm.search_menu", text="Search", icon="VIEWZOOM")            

            layout.separator()

            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")             
            layout.menu("space_special", text="Special", icon="PMARKER") 
            
            layout.separator()

            layout.menu("space_viewobjectmenu", icon="ZOOM_SELECTED") 
            layout.menu("space_transform", "Transform Menu")  

            layout.separator()

            layout.menu("space_selection", icon='RESTRICT_SELECT_OFF')

            # Snap To Menu
            layout.menu("space_snaptomenu", "Snap to Menu")

            layout.separator()

            # Origin Setup
            layout.menu("originsetupmenu_obm", "Set Origin", icon = "LAYER_ACTIVE")                                       
           
            # Align Menu
            layout.menu("space_alignmirror", text = "Align / Mirror")   

            # Pivot Menu
            #layout.menu("space_pivotmenu", "Pivot Menu", icon = "ROTATE")
                    
            # Snap Menu
            #layout.menu("space_snapmenu", "Snap Menu", icon = "SNAP_ON")
                    

            layout.separator()
            layout.menu("cameraviewmenu", text="Camera", icon="CAMERA_DATA")               
            layout.menu("bordermenu", text="Border Menu")                          
                   

            layout.separator()

            layout.menu("space_file", icon="FILESEL")
            layout.menu("space_imexport")

            layout.separator()
            
            # Delete Menu
            layout.operator("object.delete", "Delete", icon = "PANEL_CLOSE")             
            layout.menu("space_cleardelete", text = "Clear Menu")          

            layout.separator()   
            
            ####################################################                   
            draw_spacebar_bottom1_history_tools(context, layout)     
            ####################################################

            
 
            
##########------------##########
##########  Editmode  ##########
##########------------##########

        elif ob.mode == 'EDIT_MESH':
            # Edit mode
            
            # Setting Menu
            layout.operator("wm.search_menu", text="Search", icon="VIEWZOOM")
            
            layout.separator()
               
            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")            
            layout.menu("space_special", text="Special", icon="PMARKER") 
            
            layout.separator()
            
            layout.menu("space_viewobjectmenu", "Mesh View", icon="ZOOM_SELECTED") 
            layout.menu("space_transform", "Transform Menu")                

            layout.separator()   

            layout.menu("originsetupmenu_edm", "Set Origin", icon = "LAYER_ACTIVE") 
            
            layout.separator()            
            
            # Select Menu
            layout.menu("space_selection", icon='RESTRICT_SELECT_OFF')
            
            # Multi Select Menu
            layout.menu("VIEW3D_MT_edit_multi", text = "Selection Modes")             
            
            layout.separator()
            
			# Vertices Menu
            layout.menu("space_vertice_edm", icon='VERTEXSEL')
            
            # Align Menu
            layout.menu("align.xyz_new", text = "Align / Mirror")
            
            layout.separator()            
                        
		     # Edge Menu
            layout.menu("space_edge_one_edm", icon='EDGESEL')  
            layout.menu("space_edge_two_edm")           
            
            layout.separator()
            			
            # Face Menu
            layout.menu("space_face_one_edm", icon='FACESEL')             
            layout.menu("space_face_two_edm")

            layout.separator()
            
		    # Normal Menu
            layout.menu("space_normal_edm", icon='SNAP_NORMAL')

            layout.separator()             
            
            ######  Spacebar Bottom History  ###################                     
            draw_spacebar_bottom2_history_tools(context, layout)     
            ####################################################
        

            

##########---------##########
##########  Curve  ##########
##########---------##########            

        if ob.mode == 'EDIT_CURVE':
           
            # Search
            layout.operator("wm.search_menu", text="Search", icon="VIEWZOOM")            

            layout.separator()

            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")             
            layout.menu("space_special", text="Special", icon="PMARKER") 

            layout.separator()

            # Select Menu
            layout.menu("space_selection", icon='RESTRICT_SELECT_OFF')
            layout.menu("space_special", "Smooth Curve")

            layout.separator()

            layout.operator("curve.duplicate_move","Duplicate", icon = "DISCLOSURE_TRI_RIGHT")          
            layout.operator("curve.extrude_move","Extrude & Move")

            layout.separator()

            #layout.operator("curve.subdivide")
        
            layout.menu("space_curvesubdivide", icon = "IPO_QUINT")

            layout.separator()

            layout.operator("curve.split", icon = "RIGHTARROW_THIN")
        
            edit_object = context.edit_object
            if edit_object.type == 'CURVE':
            
                layout.operator("object._curve_outline",  text="Outline")
        
            layout.operator("curve.separate")             
            layout.operator("curve.make_segment")
        
            layout.separator()                
        
            edit_object = context.edit_object

            if edit_object.type == 'CURVE':
            
                layout.operator("transform.tilt", icon = "FILE_REFRESH")
                layout.operator("curve.tilt_clear")

            layout.separator()

            layout.operator_menu_enum("curve.handle_type_set", "type", icon = "IPO_BEZIER")
            layout.operator("curve.normals_make_consistent")
            
            layout.separator()

            layout.operator("curve.switch_direction", icon = "ARROW_LEFTRIGHT")

            layout.operator("curve.spline_weight_set")             
        
            edit_object = context.edit_object
            if edit_object.type == 'CURVE':
        
                layout.operator("curve.radius_set")

            layout.separator()

            layout.operator("curve.cyclic_toggle")               
        
            layout.separator()

            layout.menu("VIEW3D_MT_hook", icon = "HOOK")

            layout.separator()

            layout.menu("VIEW3D_MT_edit_curve_showhide", icon = "VISIBLE_IPO_ON")           


            layout.separator() 
            
            ######  Spacebar Bottom History  ###################                     
            draw_spacebar_bottom2_history_tools(context, layout)     
            ####################################################




##########-----------##########
##########  Surface  ##########
##########-----------########## 

        if ob.mode == 'EDIT_SURFACE':
            
            # Search
            layout.operator("wm.search_menu", text="Search", icon="VIEWZOOM")            

            layout.separator()

            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")             

            layout.separator()

            # Select Menu
            layout.menu("space_selection", icon='RESTRICT_SELECT_OFF')
            layout.menu("space_special", "Smooth Curve")

            layout.separator()

            layout.operator("curve.duplicate_move","Duplicate", icon = "DISCLOSURE_TRI_RIGHT")          
            layout.operator("curve.extrude_move","Extrude & Move")

            layout.separator()

            #layout.operator("curve.subdivide")
        
            layout.menu("space_curvesubdivide", icon = "IPO_QUINT")

            layout.separator()

            layout.operator("curve.split", icon = "RIGHTARROW_THIN")
            layout.operator("curve.separate")             
            layout.operator("curve.make_segment")
        
            layout.separator()                

            layout.operator_menu_enum("curve.handle_type_set", "type", icon = "IPO_BEZIER")
            
            layout.separator()

            layout.operator("curve.switch_direction", icon = "ARROW_LEFTRIGHT")

            layout.operator("curve.spline_weight_set")             
        
            edit_object = context.edit_object
            if edit_object.type == 'CURVE':
        
                layout.operator("curve.radius_set")

            layout.separator()

            layout.operator("curve.cyclic_toggle")               
        
            layout.separator()

            layout.menu("VIEW3D_MT_hook", icon = "HOOK")

            layout.separator()

            layout.menu("VIEW3D_MT_edit_curve_showhide", icon = "VISIBLE_IPO_ON")           


            layout.separator() 
            
            ######  Spacebar Bottom History  ###################                     
            draw_spacebar_bottom2_history_tools(context, layout)     
            ####################################################



##########------------##########
##########  Metaball  ##########
##########------------##########            

        if ob.mode == 'EDIT_METABALL':
            
            # Search
            layout.operator("wm.search_menu", text="Search", icon="VIEWZOOM")            

            layout.separator()

            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")             

            layout.separator()
            
            # Select Menu
            layout.menu("space_selection", icon='RESTRICT_SELECT_OFF')

            layout.operator("mball.duplicate_metaelems", icon='DISCLOSURE_TRI_RIGHT')   

            layout.separator() 
            
            ######  Spacebar Bottom History  ###################                     
            draw_spacebar_bottom1_history_tools(context, layout)     
            ####################################################


##########-----------##########
##########  Lattice  ##########
##########-----------##########

        elif ob.mode == 'EDIT_LATTICE':
            
            # Search
            layout.operator("wm.search_menu", text="Search", icon="VIEWZOOM")            

            layout.separator()

            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")             

            layout.separator()
            
            # Select Menu
            layout.menu("space_selection", icon='RESTRICT_SELECT_OFF')

            #layout.menu("space_special", icon='RIGHTARROW_THIN')            
            
            layout.separator() 
            
            ######  Spacebar Bottom History  ###################                     
            draw_spacebar_bottom2_history_tools(context, layout)     
            ####################################################



##########------------##########
##########  Particle  ##########
##########------------##########

        if  context.mode == 'PARTICLE':
            # Particle menu

            # Brush Menu
            layout.menu("VIEW3D_ParticleBrush", text = "Brushes", icon='BRUSH_DATA') 

            layout.separator()                        

            # Select Menu
            layout.menu("space_selection", icon='RESTRICT_SELECT_OFF')

            layout.separator() 

            # Particle Menu
            layout.menu("VIEW3D_Paint_Particle", icon='PARTICLEMODE', text = "Hair Particles")
            
            layout.separator() 

            # Special Menu
            layout.menu("space_special", icon='SOLO_OFF')                      

            
            ######  Spacebar Bottom History  ###################                     
            draw_spacebar_bottom2_history_tools(context, layout)     
            ####################################################



##########---------------##########
##########  Weightpaint  ##########
##########---------------##########

        ob = context
        if ob.mode == 'PAINT_WEIGHT':
            # Weight paint menu

            # Brush Menu
            layout.menu("VIEW3D_VertexBrush", text = "Brush", icon='BRUSH_DATA')

            # Brush Data Menu
            layout.menu("VIEW3D_MT_brush", text = "Brush Setting", icon='VPAINT_HLT')

            layout.separator()             
            
            # Weight Paint block
            layout.menu("VIEW3D_Paint_Weight", icon='WPAINT_HLT')

            layout.separator() 

            # Special Menu
            layout.menu("space_special", icon= 'PLUGIN')

            ######  Spacebar Bottom History  ###################                     
            draw_spacebar_bottom2_history_tools(context, layout)     
            ####################################################
    


##########---------------##########
##########  Vertexpaint  ##########
##########---------------##########            

        elif ob.mode == 'PAINT_VERTEX':
            # Vertex paint menu

            # Brush Menu
            layout.menu("VIEW3D_VertexBrush", text = "Brush", icon='BRUSH_DATA')

            # Brush Data Menu
            layout.menu("VIEW3D_MT_brush", text = "Brush Setting", icon='VPAINT_HLT')

            layout.separator()    
              
            layout.operator("Brush.stroke_method", text="stroke_method")
 
            # Special Menu
            layout.menu("space_special", icon='SOLO_OFF')  

            ######  Spacebar Bottom History  ###################                     
            draw_spacebar_bottom2_history_tools(context, layout)     
            ####################################################
    


##########----------------##########
##########  Texturepaint  ##########
##########----------------##########            

        elif ob.mode == 'PAINT_TEXTURE':
            # Texture paint menu


            # Brush Menu
            layout.menu("VIEW3D_TextureBrush", text = "Brush", icon='BRUSH_DATA')

            # Brush Data Menu
            layout.menu("VIEW3D_MT_brush", text = "Brush Setting", icon='VPAINT_HLT')

            ######  Spacebar Bottom History  ###################                     
            draw_spacebar_bottom2_history_tools(context, layout)     
            ####################################################
            
            


##########--------------##########
##########  Sculptmode  ##########
##########--------------##########            

        elif ob.mode == 'SCULPT':
            # Sculpt menu
            

            # Brush Menu
            layout.menu("VIEW3D_SculptBrush", text = "Brushes", icon='BRUSH_DATA')            
            
            # Sculptmode Menu
            layout.menu("VIEW3D_MT_sculptmode", text = "Sculptmode",  icon='SCULPTMODE_HLT')            
            
            # Sculpt Brush Menu
            layout.menu("VIEW3D_MT_brush", text = "Brush Settings", icon='LIGHTPAINT')

            ######  Spacebar Bottom History  ###################                     
            draw_spacebar_bottom2_history_tools(context, layout)     
            ####################################################
            

            
##########------------##########
##########  Armature  ##########
##########------------##########            
           
        elif ob.mode == 'EDIT_ARMATURE':

            # Search
            layout.operator("wm.search_menu", text="Search", icon="VIEWZOOM")            

            layout.separator()

            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")             

            layout.separator()

            # Select Menu
            layout.menu("space_selection", icon='RESTRICT_SELECT_OFF')
      
            # Subdivide Menu
            layout.menu("VIEW3D_MT_ArmatureCut")           

            layout.separator()
            
            # Edit Armature roll
            layout.menu("VIEW3D_MT_edit_armature_roll", icon='BONE_DATA')

            # Edit Armature Toolkit
            layout.menu("VIEW3D_MT_EditArmatureTK", icon='ARMATURE_DATA')

            layout.separator()             

            # Parent block
            layout.menu("VIEW3D_MT_edit_armature_parent", icon='CONSTRAINT')

            layout.separator()             

            # Edit Armature Name
            layout.menu("VIEW3D_MT_ArmatureName","Name", icon='OUTLINER_DATA_FONT')            

            # bone options block
            layout.menu("VIEW3D_MT_bone_options_toggle", text="Bone Settings", icon = "PREFERENCES")
            
            layout.separator() 
            
            ######  Spacebar Bottom History  ###################                     
            draw_spacebar_bottom1_history_tools(context, layout)     
            ####################################################



##########------------##########
##########  Posemode  ##########
##########------------##########

        if context.mode == 'POSE':
            arm = context.active_object.data
            # Search
            layout.operator("wm.search_menu", text="Search", icon="VIEWZOOM")       
             
            layout.separator() 
                                    
            # Setting Menu
            layout.operator("screen.redo_last", text="Settings", icon="SCRIPTWIN")
 
            layout.separator()            

            # Select Menu
            layout.menu("space_selection", icon='RESTRICT_SELECT_OFF')
                        
            # Special Menu
            layout.menu("space_special")             

            layout.separator()

            if arm.draw_type in {'BBONE', 'ENVELOPE'}:
                layout.operator("transform.transform", text="Scale Envelope Distance").mode = 'BONE_SIZE'            

            layout.menu("VIEW3D_MT_object_animation", icon = "CLIP")
            layout.menu("VIEW3D_MT_pose_propagate")
            layout.menu("VIEW3D_MT_pose_slide")
            layout.menu("VIEW3D_AnimationPlayer", text="Play Animation", icon = "TRIA_RIGHT") 
            
            layout.separator()

            layout.operator("pose.copy", icon = "COPYDOWN")
            layout.operator("pose.paste", icon = "PASTEDOWN")
            layout.operator("pose.paste", text="Paste X-Flipped Pose", icon = "PASTEFLIPDOWN").flipped = True

            layout.separator()

            layout.menu("VIEW3D_MT_pose_library", icon = "POSE_HLT")
            layout.menu("VIEW3D_MT_pose_motion")
            layout.menu("VIEW3D_MT_pose_group")

            layout.separator()

            layout.menu("VIEW3D_MT_object_parent", icon = "CONSTRAINT_BONE")
            layout.menu("VIEW3D_MT_pose_constraints")
            layout.menu("VIEW3D_MT_pose_ik")

            layout.separator()             
          
            layout.operator("pose.flip_names", icon = "ARROW_LEFTRIGHT")
            layout.operator("pose.quaternions_flip")

            layout.separator()             

            layout.operator_context = 'INVOKE_AREA'
            layout.operator("pose.bone_layers", text="Change Bone Layers...", icon = "NLA")
            layout.operator("armature.armature_layers",  text="Change Armature Layers...")

            layout.separator() 
                       
            layout.menu("VIEW3D_MT_bone_options_toggle",  text="Bone Settings", icon = "SCRIPTWIN")

            layout.separator() 
            
            layout.menu("VIEW3D_MT_pose_showhide")
                        
            ######  Spacebar Bottom History  ###################                     
            draw_spacebar_bottom2_history_tools(context, layout)     
            ####################################################
       

###########################################################################################################################################################
###########################################################################################################################################################
### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator  
### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator 
###########################################################################################################################################################
###########################################################################################################################################################

def abs(val):
    if val > 0:
        return val
    return -val

def edgeIntersect(context, operator):
    from mathutils.geometry import intersect_line_line

    obj = context.active_object

    if (obj.type != "MESH"):
        operator.report({'ERROR'}, "Object must be a mesh")
        return None

    edges = []
    mesh = obj.data
    verts = mesh.vertices

    is_editmode = (obj.mode == 'EDIT')
    if is_editmode:
        bpy.ops.object.mode_set(mode='OBJECT')

    for e in mesh.edges:
        if e.select:
            edges.append(e)

            if len(edges) > 2:
                break

    if is_editmode:
        bpy.ops.object.mode_set(mode='EDIT')

    if len(edges) != 2:
        operator.report({'ERROR'},
                        "Operator requires exactly 2 edges to be selected")
        return

    line = intersect_line_line(verts[edges[0].vertices[0]].co,
                               verts[edges[0].vertices[1]].co,
                               verts[edges[1].vertices[0]].co,
                               verts[edges[1].vertices[1]].co)

    if line is None:
        operator.report({'ERROR'}, "Selected edges do not intersect")
        return

    point = line[0].lerp(line[1], 0.5)
    context.scene.cursor_location = obj.matrix_world * point

#bpy.utils.register_class(edgeIntersect) 



class VIEW3D_OT_CursorToEdgeIntersection(bpy.types.Operator):
    "Finds the mid-point of the shortest distance between two edges"

    bl_idname = "view3d.snap_cursor_to_edge_intersection"
    bl_label = "Cursor to Edge Intersection"

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj != None and obj.type == 'MESH'

    def execute(self, context):
        edgeIntersect(context, self)
        return {'FINISHED'}

#bpy.utils.register_class(VIEW3D_OT_CursorToEdgeIntersection) 



class VIEW3D_OT_pivot_cursor(bpy.types.Operator):
    "Cursor as Pivot Point"
    bl_idname = "view3d.pivot_cursor"
    bl_label = "Cursor as Pivot Point"

    @classmethod
    def poll(cls, context):
        return bpy.context.space_data.pivot_point != 'CURSOR'

    def execute(self, context):
        bpy.context.space_data.pivot_point = 'CURSOR'
        return {'FINISHED'}

#bpy.utils.register_class(VIEW3D_OT_pivot_cursor) 



class VIEW3D_OT_revert_pivot(bpy.types.Operator):
    "Revert Pivot Point"
    bl_idname = "view3d.revert_pivot"
    bl_label = "Reverts Pivot Point to median"

    @classmethod
    def poll(cls, context):
        return bpy.context.space_data.pivot_point != 'MEDIAN_POINT'

    def execute(self, context):
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'
        # @todo Change this to 'BOUDNING_BOX_CENTER' if needed...
        return{'FINISHED'}

#bpy.utils.register_class(VIEW3D_OT_revert_pivot) 
    
    

###########################################################################################################################################################
###########################################################################################################################################################
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register 
### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register 
###########################################################################################################################################################
###########################################################################################################################################################


def register():
    
    bpy.utils.register_class(VIEW3D_MT_Space_Display)

    bpy.utils.register_module(__name__)    
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu', 'SPACE', 'PRESS')     #ctrl = True, alt = True, shift = True)
        kmi.properties.name = "space_spacebarmenu"
    

def unregister():
    
    bpy.utils.unregister_class(VIEW3D_MT_Space_Display)
    
    bpy.utils.unregister_module(__name__)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps['3D View']
        for kmi in km.keymap_items:
            if kmi.idname == 'wm.call_menu':
                if kmi.properties.name == "":
                    km.keymap_items.remove(kmi)
                    break

if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_MT_Space_Display.bl_idname)
































































