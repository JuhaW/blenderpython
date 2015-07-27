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
#
# ***** END GPL LICENCE BLOCK *****


bl_info = {
    "name": "BBox Origin Setup",
    "author": "mkbreuer",
    "version": (0, 1, 0),
    "blender": (2, 7, 3),
    "location": "View3D",
    "description": "create bounding box or set origin to 27 places or more",
    "warning": "",
    "wiki_url": "",
    "category" : "Add Mesh"
}


import bpy, mathutils, math, re
from bpy import*
from math import radians
from mathutils import Vector
from mathutils.geometry import intersect_line_plane


############----------------------############
############  Props for DROPDOWN  ############
############----------------------############

class DropdownBBoxToolProps(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.bboxwindow
    """
    display_bboxfront = bpy.props.BoolProperty(name = "Front", description = "9 Places for Origin on BBox Frontside / +Y", default = False)
    display_bboxmiddle = bpy.props.BoolProperty(name = "Middle", description = "9 Places for  Origin on BBox Middle / XYZ", default = False)
    display_bboxback = bpy.props.BoolProperty(name = "Back", description = "9 Places for  Origin on BBox Backside / -Y", default = False)

bpy.utils.register_class(DropdownBBoxToolProps)
bpy.types.WindowManager.bboxwindow = bpy.props.PointerProperty(type = DropdownBBoxToolProps)


############  Objectmode Operator  ############
class BBOXSET(bpy.types.Panel):
    """BBox Origin Setup"""
    bl_idname = "VIEW3D_PT_bbox_setup"
    bl_label = "BBox Origin Setup"    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        lt = context.window_manager.bboxwindow
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'

        
        if context.mode == 'OBJECT':  
            row = layout.row(1)
            row.scale_y = 1.2
            row.operator("object.bounding_boxers",text="Bounding Box", icon="BBOX")  

       
        obj = context.active_object
        if obj:
            obj_type = obj.type

            if obj_type in {'MESH'}:    #{'MESH', 'CURVE', 'SURFACE', 'ARMATURE', 'FONT', 'LATTICE', 'META'}:


                if context.mode == 'EDIT_MESH' or 'OBJECT':  
                    box = layout.box()
                    row = box.column(1)
                    ###space1###

                    #col = layout.column(align=True)
                    if lt.display_bboxback:
                        row.scale_y = 1.2                  
                        row.prop(lt, "display_bboxback", text="Back", icon='TRIA_DOWN')

                    else:
                        row.scale_y = 1.2            
                        row.prop(lt, "display_bboxback", text="Back", icon='TRIA_RIGHT')

                    ###space1###
                    if lt.display_bboxback:
                         col = layout.column(align=True)  
                         box = col.column(align=True).box().column()
                         col_top = box.column(align=True)
                        
                         #Top
                         row = col_top.row(align=True)
                         row.alignment = 'CENTER'
                         row.scale_x = 1.55

                         row.operator("object.cubeback_cornertop_minus_xy", "", icon = "LAYER_ACTIVE")#"Back- Left -Top")
                         row.operator("object.cubeback_edgetop_minus_y", "", icon = "LAYER_ACTIVE")#"Back - Top")
                         row.operator("object.cubeback_cornertop_plus_xy","", icon = "LAYER_ACTIVE")# "Back- Right -Top ")
                         

                         #Middle
                         row = col_top.row(align=True)
                         row.alignment = 'CENTER'
                         row.scale_x = 1.55             
                         row.operator("object.cubefront_edgemiddle_minus_x","", icon = "LAYER_ACTIVE")#"Back- Left")
                         row.operator("object.cubefront_side_plus_y","", icon = "LAYER_ACTIVE")# "Back") 
                         row.operator("object.cubefront_edgemiddle_plus_x","", icon = "LAYER_ACTIVE")#"Back- Right")   
                         
                         #Bottom
                         row = col_top.row(align=True)
                         row.alignment = 'CENTER'
                         row.scale_x = 1.55
                         row.operator("object.cubeback_cornerbottom_minus_xy","", icon = "LAYER_ACTIVE")# "Back- Left -Bottom")
                         row.operator("object.cubefront_edgebottom_plus_y","", icon = "LAYER_ACTIVE")#"Back - Bottom") 
                         row.operator("object.cubeback_cornerbottom_plus_xy","", icon = "LAYER_ACTIVE")# "Back- Right -Bottom")  
                    
                         ##############################
                         col = layout.column(align=True)  
                         box = col.column(align=True).box().column()
                         col_top = box.column(align=True)
                         row = box.column(1)
               
                     
                    ###space1###

                    #col = layout.column(align=True)
                    if lt.display_bboxmiddle:
                        row.scale_y = 1.2                    
                        row.prop(lt, "display_bboxmiddle", text="Middle", icon='TRIA_DOWN')

                    else:
                        row.scale_y = 1.2
                        row.prop(lt, "display_bboxmiddle", text="Middle", icon='TRIA_RIGHT')


                    ###space1###
                    if lt.display_bboxmiddle:              
                         col = layout.column(align=True)  
                         box = col.column(align=True).box().column()
                         col_top = box.column(align=True)

                         #Top
                         row = col_top.row(align=True)
                         row.alignment = 'CENTER'
                         row.scale_x = 1.55

                         row.operator("object.cubefront_edgetop_minus_x","", icon = "LAYER_ACTIVE")#"Middle - Left Top")
                         row.operator("object.cubefront_side_plus_z", "", icon = "LAYER_ACTIVE")#"Top")
                         row.operator("object.cubefront_edgetop_plus_x","", icon = "LAYER_ACTIVE")#"Middle - Right Top")              

                         
                         #Middle
                         row = col_top.row(align=True)
                         row.alignment = 'CENTER'
                         row.scale_x = 1.55             
                          
                         row.operator("object.cubefront_side_minus_x","", icon = "LAYER_ACTIVE")# "Left")
                         obj = context.object
                         if obj and obj.mode == 'EDIT':          
                             row.operator("mesh.origincenter", text="", icon="LAYER_ACTIVE") 
                         else:
                             row.operator("object.origin_set", text="", icon="LAYER_ACTIVE").type='ORIGIN_GEOMETRY'            
                                         
                         row.operator("object.cubefront_side_plus_x","", icon = "LAYER_ACTIVE")# "Right")              
                    

                         #Bottom
                         row = col_top.row(align=True)
                         row.alignment = 'CENTER'
                         row.scale_x = 1.55            
                         
                         row.operator("object.cubefront_edgebottom_minus_x","", icon = "LAYER_ACTIVE")#"Middle - Left Bottom")
                         row.operator("object.cubefront_side_minus_z","", icon = "LAYER_ACTIVE")# "Bottom")             
                         row.operator("object.cubefront_edgebottom_plus_x","", icon = "LAYER_ACTIVE")#"Middle - Right Bottom")  

                         
                         ##############################
                         col = layout.column(align=True)  
                         box = col.column(align=True).box().column()
                         col_top = box.column(align=True)
                         row = col_top.row(align=True)
                       
                           

                    ###space1###

                    if lt.display_bboxfront:
                        row.scale_y = 1.2
                        row.prop(lt, "display_bboxfront", text="Front", icon='TRIA_DOWN')

                    else:
                        row.scale_y = 1.2           
                        row.prop(lt, "display_bboxfront", text="Front", icon='TRIA_RIGHT')

                    ###space1###
                    if lt.display_bboxfront:
                         col = layout.column(align=True)  
                         box = col.column(align=True).box().column()
                         col_top = box.column(align=True)
                        
                         #Top
                         row = col_top.row(align=True)
                         row.alignment = 'CENTER'
                         row.scale_x = 1.55
                                    
                         row.operator("object.cubefront_cornertop_minus_xy", "", icon = "LAYER_ACTIVE")# "Front- Left -Top"
                         row.operator("object.cubeback_edgetop_plus_y","", icon = "LAYER_ACTIVE")# "Front - Top"
                         row.operator("object.cubefront_cornertop_plus_xy","", icon = "LAYER_ACTIVE")#  "Front- Right -Top"
                        
                        
                         #Middle
                         row = col_top.row(align=True)
                         row.alignment = 'CENTER'
                         row.scale_x = 1.55
                                      
                         row.operator("object.cubefront_edgemiddle_minus_y","", icon = "LAYER_ACTIVE")# "Front- Left"       
                         row.operator("object.cubefront_side_minus_y","", icon = "LAYER_ACTIVE")#  "Front"           
                         row.operator("object.cubefront_edgemiddle_plus_y","", icon = "LAYER_ACTIVE")# "Front- Right"              


                         #Bottom
                         row = col_top.row(align=True)
                         row.alignment = 'CENTER'
                         row.scale_x = 1.55
                         
                         row.operator("object.cubefront_cornerbottom_minus_xy","", icon = "LAYER_ACTIVE")# "Front- Left -Bottom"                
                         row.operator("object.cubefront_edgebottom_minus_y","", icon = "LAYER_ACTIVE")# "Front - Bottom"
                         row.operator("object.cubefront_cornerbottom_plus_xy", "", icon = "LAYER_ACTIVE")# "Front- Right -Bottom") 
                         


        if obj:
            obj_type = obj.type

            if obj_type in {'MESH', 'CURVE', 'SURFACE', 'ARMATURE', 'FONT', 'LATTICE', 'META'}:

                if context.mode == 'OBJECT':                    
                    row = layout.box().column(1)
                    row.scale_y = 1.2
                    row.operator("object.origin_set", text="Origin to Geometry").type='ORIGIN_GEOMETRY'
                    row.operator("object.origin_set", text="Origin to Cursor").type='ORIGIN_CURSOR'
                    row.operator("object.origin_set", text="Origin to Mass").type='ORIGIN_CENTER_OF_MASS' 
                    row.operator("object.origin_set", text="Geometry to Origin").type='GEOMETRY_ORIGIN'            
                    if obj:
                        obj_type = obj.type
                        if obj_type in {'CURVE'}:
                            row = layout.box().column(1)
                            row.scale_y = 1.2
                            row.operator("curve.origin_start_point", text="Origin to First", icon ="PARTICLE_TIP")
                            row.operator("curve.switch_direction_obm","Direction" ,icon = "ARROW_LEFTRIGHT")                  
                else:
                #if context.mode == "EDIT_MESH" or "EDIT_CURVE" or "EDIT_SURFACE" or "EDIT_METABALL" or "EDIT_ARMATURE":
                    row = layout.box().column(1)
                    row.scale_y = 1.2                                
                    row.operator("origin.selected_edm","Origin to Selected", icon = "EDITMODE_HLT")   
                    row.operator("origin.selected_obm","Origin to Selected", icon = "OBJECT_DATAMODE")
    






####################
######  Menu  ######
####################



class BBoxOrigin_CornerMenu(bpy.types.Menu):
    bl_label = "BBox Origin Corner"
    bl_idname = "object.bbox_origin_corner_menu"

    def draw(self, context):
        layout = self.layout

        ###  Origin to Corners on Top 

        layout.operator("object.cubefront_cornertop_minus_xy", "Front- Left -Top")
        layout.operator("object.cubefront_cornerbottom_minus_xy", "Front- Left -Bottom")
        layout.operator("object.cubefront_cornertop_plus_xy", "Front- Right -Top")
        layout.operator("object.cubefront_cornerbottom_plus_xy", "Front- Right -Bottom")

        layout.separator()
        
        ###  Origin to Corners on Bottom
        layout.operator("object.cubeback_cornertop_minus_xy", "Back- Left -Top")
        layout.operator("object.cubeback_cornerbottom_minus_xy", "Back- Left -Bottom")
        layout.operator("object.cubeback_cornertop_plus_xy", "Back- Right -Top ")
        layout.operator("object.cubeback_cornerbottom_plus_xy", "Back- Right -Bottom")        


bpy.utils.register_class(BBoxOrigin_CornerMenu)



class BBoxOrigin_EdgeMenu(bpy.types.Menu):
    bl_label = "BBox Origin Edge"
    bl_idname = "object.bbox_origin_edge_menu"

    def draw(self, context):
        layout = self.layout

        ###  Origin to Back +Y 
        layout.operator("object.cubeback_edgetop_minus_y","Back - Top")
        layout.operator("object.cubefront_edgebottom_plus_y","Back - Bottom")                               
        layout.operator("object.cubefront_edgemiddle_minus_x","Back- Left")
        layout.operator("object.cubefront_edgemiddle_plus_x","Back- Right")          
                      
                
        layout.separator()        
        
        ###  Origin to the Middle
        layout.operator("object.cubefront_edgetop_minus_x","Middle - Left Top")
        layout.operator("object.cubefront_edgetop_plus_x","Middle - Right Top")              
        layout.operator("object.cubefront_edgebottom_minus_x","Middle - Left Bottom")
        layout.operator("object.cubefront_edgebottom_plus_x","Middle - Right Bottom")  

        layout.separator() 

        ###  Origin to Front -Y 
        layout.operator("object.cubeback_edgetop_plus_y","Front - Top")
        layout.operator("object.cubefront_edgebottom_minus_y","Front - Bottom") 
        layout.operator("object.cubefront_edgemiddle_minus_y","Front- Left")
        layout.operator("object.cubefront_edgemiddle_plus_y","Front- Right")     


bpy.utils.register_class(BBoxOrigin_EdgeMenu)



class BBoxOrigin_SideMenu(bpy.types.Menu):
    bl_label = "BBox Origin Side"
    bl_idname = "object.bbox_origin_side_menu"

    def draw(self, context):
        layout = self.layout

        ### Origin to the Middle of Side 
        layout.operator("object.cubefront_side_plus_z", "Top")
        layout.operator("object.cubefront_side_minus_z", "Bottom")
        layout.operator("object.cubefront_side_minus_y", "Front")
        layout.operator("object.cubefront_side_plus_y", "Back")                
        layout.operator("object.cubefront_side_minus_x", "Left")
        layout.operator("object.cubefront_side_plus_x", "Right") 

bpy.utils.register_class(BBoxOrigin_SideMenu)








### further function for BoundingBoxSource
class BoundingBox (bpy.types.Operator):
    """create a bound boxes for selected object"""      
    bl_idname = "object.bounding_boxers"
    bl_label = "BBox"
    bl_options = {'REGISTER', 'UNDO'}
                                 
    bbox_subdiv = bpy.props.IntProperty(name="Subdivide", description="How often?", default=0, min=0, soft_max=10, step=1)            

    bbox_wire = bpy.props.BoolProperty(name="Wire only", description="Delete Face", default= False) 

    bbox_origin = bpy.props.BoolProperty(name="Origin Center",  description="Origin to BBox-Center", default=False)  

    bbox_renderoff = bpy.props.BoolProperty(name="Render off",  description="Hide from Render", default=False)

    bbox_freeze = bpy.props.BoolProperty(name="Freeze Selection",  description="Hide from Selection", default=False)         

    def execute(self, context):

        if bpy.context.selected_objects: 
            if context.space_data.local_view is not None:
                bpy.ops.view3d.localview()
                bpy.ops.object.bounding_box_source()  
                bpy.ops.object.select_pattern(pattern="_bbox_edit", case_sensitive=False, extend=False)
                bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
            
            else:            
                bpy.ops.object.bounding_box_source()  
                bpy.ops.object.select_pattern(pattern="_bbox_edit", case_sensitive=False, extend=False)  
                bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

        else:
            bpy.ops.mesh.primitive_cube_add()            
            bpy.context.object.name = "_bbox"


        for obj in bpy.context.selected_objects:
             
            
            bpy.context.scene.objects.active = obj            
                                            
            bpy.ops.object.editmode_toggle()  
            bpy.ops.mesh.normals_make_consistent()                       
        

            for i in range(self.bbox_subdiv):
                bpy.ops.mesh.subdivide(number_cuts=1)

            for i in range(self.bbox_wire):
                bpy.ops.mesh.delete(type='ONLY_FACE')
           

            bpy.ops.object.editmode_toggle()

            for i in range(self.bbox_origin):
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')                              


            for i in range(self.bbox_freeze):
                bpy.context.object.hide_select = True
            
            for i in range(self.bbox_renderoff):
                bpy.context.object.hide_render = True
               
                            
            bpy.context.object.name = "_bbox" 

        return {'FINISHED'}                        

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)



### BoundingBoxSource from nikitron (Gorodetskiy Nikita / http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Object/Nikitron_tools)
class BoundingBoxSource (bpy.types.Operator):
    """Make bound boxes for selected objects"""      
    bl_idname = "object.bounding_box_source"
    bl_label = "Bounding boxes"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        objects = bpy.context.selected_objects
        i = 0
        for a in objects:
            self.make_it(i, a)
            i += 1
            
        return {'FINISHED'}


    def make_it(self, i, obj):
        box = bpy.context.selected_objects[i].bound_box
        mw = bpy.context.selected_objects[i].matrix_world
        name = ('_bbox_edit')                               #name = (bpy.context.selected_objects[i].name + '_bbox') 
        me = bpy.data.meshes.new(name)                      #bpy.data.meshes.new(name + 'Mesh')
        ob = bpy.data.objects.new(name, me)
        
        ob.location = mw.translation
        ob.scale = mw.to_scale()
        ob.rotation_euler = mw.to_euler()
        ob.show_name = False
        bpy.context.scene.objects.link(ob)
        loc = []
        for ver in box:
            loc.append(mathutils.Vector((ver[0],ver[1],ver[2])))
        me.from_pydata((loc), [], ((0,1,2,3),(0,1,5,4),(4,5,6,7), (6,7,3,2),(0,3,7,4),(1,2,6,5)))
        me.update(calc_edges=True) 
        return



class FullCurve(bpy.types.Operator):
    """Add A full Bevel Curve"""
    bl_idname = "view3d.fullcurve"
    bl_label = "A full Bevel Curve"
    bl_options = {'REGISTER', 'UNDO'}
 

    curve_subdiv = bpy.props.IntProperty(name="Subdivide", description="How often?", default=0, min=0, soft_max=10, step=1)     
    
    def execute(self, context):
    
        bpy.ops.curve.primitive_bezier_curve_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        bpy.ops.transform.resize(value=(5, 5, 5), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.context.object.data.fill_mode = 'FULL'
        bpy.context.object.data.bevel_resolution = 4
        bpy.context.object.data.resolution_u = 10
        bpy.context.object.data.bevel_depth = 0.2        

        bpy.ops.object.editmode_toggle()        
        
        bpy.context.object.data.show_normal_face = False
        

        for i in range(self.curve_subdiv):
            bpy.ops.curve.subdivide(number_cuts=1)        
        
        bpy.ops.object.editmode_toggle() 
        return {'FINISHED'}    



class FullCircleCurve(bpy.types.Operator):
    """Add A full Bevel Circle Curve"""
    bl_idname = "view3d.fullcirlcecurve"
    bl_label = "A full Bevel CircleCurve"
    bl_options = {'REGISTER', 'UNDO'}
   

    curve_subdiv = bpy.props.IntProperty(name="Subdivide", description="How often?", default=0, min=0, soft_max=10, step=1)

    curve_cycle = bpy.props.BoolProperty(name="Open?", description="Open", default = False)     
    
    def execute(self, context):
   
        bpy.ops.curve.primitive_bezier_circle_add(view_align=False, enter_editmode=False,location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
        bpy.ops.transform.resize(value=(5, 5, 5), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        bpy.context.object.data.fill_mode = 'FULL'
        bpy.context.object.data.bevel_resolution = 4
        bpy.context.object.data.resolution_u = 10
        bpy.context.object.data.bevel_depth = 0.2

        bpy.ops.object.editmode_toggle()
        
        bpy.context.object.data.show_normal_face = False

        for i in range(self.curve_subdiv):
            bpy.ops.curve.subdivide(number_cuts=1)  
 
        for i in range(self.curve_cycle):
            bpy.ops.curve.cyclic_toggle(direction='CYCLIC_U')             
        
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}



#Menu for Objectmode
class CustomAddMenu_OBM(bpy.types.Menu):
    bl_label = "Custom"
    bl_idname = "OBJECT_MT_custom_Add_menu"

    def draw(self, context):
        layout = self.layout
        
        layout.operator("object.bounding_boxers","BBox", icon = "BBOX")
        
        layout.separator()
        
        layout.operator("view3d.fullcurve","Bevel Curve", icon = "CURVE_BEZCURVE")
        layout.operator("view3d.fullcirlcecurve","Bevel Circle", icon = "CURVE_BEZCIRCLE")




############  Editmode Operator  ############

class MeshCenter(bpy.types.Operator):
    """Origin to Center of Mesh"""
    bl_idname = "mesh.origincenter"
    bl_label = "Center of Mesh"

    def execute(self, context):
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.object.loops9()
        bpy.ops.mesh.select_all(action='DESELECT')
        return {'FINISHED'}




class SINGLEVERTEX(bpy.types.Operator):
    """Add a single Vertex in Editmode"""
    bl_idname = "mesh.s_vertex"
    bl_label = "Single Vertex"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.mesh.merge(type='CENTER')
        return {'FINISHED'}


class SINGLELINE_X(bpy.types.Operator):
    """Add a single Line in Editmode"""
    bl_idname = "mesh.s_line_x"
    bl_label = "Single Line"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.mesh.merge(type='CENTER')
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(2, 0, 0), "constraint_axis":(True, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
        bpy.ops.mesh.select_linked(limit=False)        
        return {'FINISHED'} 


class SINGLELINE_Y(bpy.types.Operator):
    """Add a single Line in Editmode"""
    bl_idname = "mesh.s_line_y"
    bl_label = "Single Line"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.mesh.merge(type='CENTER')
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 2, 0), "constraint_axis":(False, True, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
        bpy.ops.mesh.select_linked(limit=False)        
        return {'FINISHED'} 


class SINGLELINE_Z(bpy.types.Operator):
    """Add a single Line in Editmode"""
    bl_idname = "mesh.s_line_z"
    bl_label = "Single Line"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.mesh.merge(type='CENTER')
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 2), "constraint_axis":(False, False, True), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
        bpy.ops.mesh.select_linked(limit=False)        
        return {'FINISHED'} 


class SINGLEPLANE_X(bpy.types.Operator):
    """Add a vertical Plane in Editmode"""
    bl_idname = "mesh.s_plane_x"
    bl_label = "Single Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}   


class SINGLEPLANE_Y(bpy.types.Operator):
    """Add a vertical Plane in Editmode"""
    bl_idname = "mesh.s_plane_y"
    bl_label = "Single Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}  
    

class SINGLEPLANE_Z(bpy.types.Operator):
    """Add a vertical Plane in Editmode"""
    bl_idname = "mesh.s_plane_z"
    bl_label = "Single Plane"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')    

    def execute(self, context):
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.transform.rotate(value=-1.5708, axis=(0, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}  
    

##################################----------------------------------------------------------------------------------------
###  Origin to Corners on Top  ###
##################################


class Origin_CubeBack_CornerTop_Minus_XY(bpy.types.Operator):  
    bl_idname = "object.cubeback_cornertop_minus_xy"  
    bl_label = "Origin to -XY Corner / Top of Cubeback"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z

            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z+=c
                 x.co.x-=a

            o.location.y-=b 
            o.location.z-=c
            o.location.x+=a          
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()
            
        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z

            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z+=c
                 x.co.x-=a

            o.location.y-=b 
            o.location.z-=c
            o.location.x+=a          
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeBack_CornerTop_Minus_XY) 


class Origin_CubeBack_CornerTop_Plus_XY(bpy.types.Operator):  
    bl_idname = "object.cubeback_cornertop_plus_xy"  
    bl_label = "Origin to +XY Corner / Top of Cubeback"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z+=c
                 x.co.x+=a

            o.location.y-=b
            o.location.z-=c
            o.location.x-=a          
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z+=c
                 x.co.x+=a

            o.location.y-=b
            o.location.z-=c
            o.location.x-=a          
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeBack_CornerTop_Plus_XY) 


class Origin_CubeFront_CornerTop_Minus_XY(bpy.types.Operator):  
    bl_idname = "object.cubefront_cornertop_minus_xy"  
    bl_label = "Origin to -XY Corner / Top of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':           
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z+=c
                 x.co.x-=a
                 
            o.location.y+=b 
            o.location.z-=c  
            o.location.x+=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z+=c
                 x.co.x-=a
                 
            o.location.y+=b 
            o.location.z-=c  
            o.location.x+=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_CornerTop_Minus_XY) 


class Origin_CubeFront_CornerTop_Plus_XY(bpy.types.Operator):  
    bl_idname = "object.cubefront_cornertop_plus_xy"  
    bl_label = "Origin to +XY Corner / Top of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z+=c
                 x.co.x+=a
                 
            o.location.y+=b
            o.location.z-=c  
            o.location.x-=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z+=c
                 x.co.x+=a
                 
            o.location.y+=b
            o.location.z-=c  
            o.location.x-=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_CornerTop_Plus_XY) 


#####################################----------------------------------------------------------------------------------------
###  Origin to Corners on Bottom  ###
#####################################

class Origin_CubeFront_CornerBottom_Minus_XY(bpy.types.Operator):  
    bl_idname = "object.cubefront_cornerbottom_minus_xy"  
    bl_label = "Origin to -XY Corner / Bottom of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':           
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z-=c
                 x.co.x-=a
                 
            o.location.y+=b
            o.location.z+=c 
            o.location.x+=a            
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()
            
        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z-=c
                 x.co.x-=a
                 
            o.location.y+=b
            o.location.z+=c 
            o.location.x+=a            
            bpy.ops.object.mode_set(mode = 'EDIT')
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_CornerBottom_Minus_XY) 


class Origin_CubeFront_CornerBottom_Plus_XY(bpy.types.Operator):  
    bl_idname = "object.cubefront_cornerbottom_plus_xy"  
    bl_label = "Origin to +XY Corner / Bottom of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z-=c
                 x.co.x+=a
                 
            o.location.y+=b 
            o.location.z+=c  
            o.location.x-=a              
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()
            
        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z-=c
                 x.co.x+=a
                 
            o.location.y+=b 
            o.location.z+=c  
            o.location.x-=a              
            bpy.ops.object.mode_set(mode = 'EDIT')
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_CornerBottom_Plus_XY) 


class Origin_CubeBack_CornerBottom_Minus_XY(bpy.types.Operator):  
    bl_idname = "object.cubeback_cornerbottom_minus_xy"  
    bl_label = "Origin to -XY Corner / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:            
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z-=c
                 x.co.x-=a
                 
            o.location.y-=b 
            o.location.z+=c  
            o.location.x+=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()
            
        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:            
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z-=c
                 x.co.x-=a
                 
            o.location.y-=b 
            o.location.z+=c  
            o.location.x+=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')            
     
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeBack_CornerBottom_Minus_XY) 


class Origin_CubeBack_CornerBottom_Plus_XY(bpy.types.Operator):  
    bl_idname = "object.cubeback_cornerbottom_plus_xy"  
    bl_label = "Origin to +XY Corner / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z-=c
                 x.co.x+=a
                 
            o.location.y-=b 
            o.location.z+=c  
            o.location.x-=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()
            
        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z-=c
                 x.co.x+=a
                 
            o.location.y-=b 
            o.location.z+=c  
            o.location.x-=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeBack_CornerBottom_Plus_XY) 



###############################################----------------------------------------------------------------------------------------
###  Origin to the Middle of the Top Edges  ###
###############################################


class Origin_CubeBack_EdgeTop_Minus_Y(bpy.types.Operator):  
    bl_idname = "object.cubeback_edgetop_minus_y"  
    bl_label = "Origin to -Y Edge / Top of Cubeback"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z+=c 
                             
            o.location.y-=b 
            o.location.z-=c                 
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()
            
        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z+=c 
                             
            o.location.y-=b 
            o.location.z-=c                 
            bpy.ops.object.mode_set(mode = 'EDIT')
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeBack_EdgeTop_Minus_Y) 


class Origin_CubeBack_EdgeTop_Plus_Y(bpy.types.Operator):  
    bl_idname = "object.cubeback_edgetop_plus_y"  
    bl_label = "Origin to +Y Edge / Top of Cubeback"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z+=c 
                             
            o.location.y+=b 
            o.location.z-=c                  
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()
            
        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z+=c 
                             
            o.location.y+=b 
            o.location.z-=c                  
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeBack_EdgeTop_Plus_Y) 


class Origin_CubeFront_EdgeTop_Minus_X(bpy.types.Operator):  
    bl_idname = "object.cubefront_edgetop_minus_x"  
    bl_label = "Origin to -X Edge / Top of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.x-=a
                 x.co.z+=c 
                             
            o.location.x+=a 
            o.location.z-=c                     
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()
            
        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.x-=a
                 x.co.z+=c 
                             
            o.location.x+=a 
            o.location.z-=c                     
            bpy.ops.object.mode_set(mode = 'EDIT')            

            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_EdgeTop_Minus_X) 


class Origin_CubeFront_EdgeTop_Plus_X(bpy.types.Operator):  
    bl_idname = "object.cubefront_edgetop_plus_x"  
    bl_label = "Origin to +X Edge / Top of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.x+=a
                 x.co.z+=c 
                             
            o.location.x-=a 
            o.location.z-=c                   
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()
            
        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.x+=a
                 x.co.z+=c 
                             
            o.location.x-=a 
            o.location.z-=c                   
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_EdgeTop_Plus_X) 


##################################################-----------------------------------------------------------------------------------
###  Origin to the Middle of the Bottom Edges  ###
##################################################


class Origin_CubeFront_EdgeBottom_Minus_Y(bpy.types.Operator):  
    bl_idname = "object.cubefront_edgebottom_minus_y"  
    bl_label = "Origin to -Y Edge / Bottom of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z-=c 
                             
            o.location.y+=b 
            o.location.z+=c              
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.z-=c 
                             
            o.location.y+=b 
            o.location.z+=c              
            bpy.ops.object.mode_set(mode = 'EDIT')

            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_EdgeBottom_Minus_Y) 


class Origin_CubeFront_EdgeBottom_Plus_Y(bpy.types.Operator):  
    bl_idname = "object.cubefront_edgebottom_plus_y"  
    bl_label = "Origin to +Y Edge / Bottom of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z-=c 
                             
            o.location.y-=b 
            o.location.z+=c           
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.z-=c 
                             
            o.location.y-=b 
            o.location.z+=c           
            bpy.ops.object.mode_set(mode = 'EDIT')            

            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_EdgeBottom_Plus_Y) 


class Origin_CubeFront_EdgeBottom_Minus_X(bpy.types.Operator):  
    bl_idname = "object.cubefront_edgebottom_minus_x"  
    bl_label = "Origin to -X Edge / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':           
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.x-=a
                 x.co.z-=c 
                             
            o.location.x+=a 
            o.location.z+=c                    
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.x-=a
                 x.co.z-=c 
                             
            o.location.x+=a 
            o.location.z+=c                    
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_EdgeBottom_Minus_X) 


class Origin_CubeFront_EdgeBottom_Plus_X(bpy.types.Operator):  
    bl_idname = "object.cubefront_edgebottom_plus_x"  
    bl_label = "Origin to +X Edge / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.x+=a
                 x.co.z-=c
                             
            o.location.x-=a 
            o.location.z+=c                    
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.x+=a
                 x.co.z-=c
                             
            o.location.x-=a 
            o.location.z+=c                    
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_EdgeBottom_Plus_X) 



################################################-----------------------------------------------------------------------------------
###  Origin to the Middle of the Side Edges  ###
################################################


class Origin_CubeFront_EdgeMiddle_Minus_Y(bpy.types.Operator):  
    bl_idname = "object.cubefront_edgemiddle_minus_y"  
    bl_label = "Origin to -Y Edge / Middle of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':           
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.x-=a 
                             
            o.location.y+=b 
            o.location.x+=a              
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.x-=a 
                             
            o.location.y+=b 
            o.location.x+=a              
            bpy.ops.object.mode_set(mode = 'EDIT')                        
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_EdgeMiddle_Minus_Y) 


class Origin_CubeFront_EdgeMiddle_Plus_Y(bpy.types.Operator):  
    bl_idname = "object.cubefront_edgemiddle_plus_y"  
    bl_label = "Origin to +Y Edge / Middle of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':            
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.x+=a 
                             
            o.location.y+=b 
            o.location.x-=a            
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y-=b
                 x.co.x+=a 
                             
            o.location.y+=b 
            o.location.x-=a            
            bpy.ops.object.mode_set(mode = 'EDIT')            

            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_EdgeMiddle_Plus_Y) 


class Origin_CubeFront_EdgeMiddle_Minus_X(bpy.types.Operator):  
    bl_idname = "object.cubefront_edgemiddle_minus_x"  
    bl_label = "Origin to -X Edge / Middle of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':           
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.x-=a 
                             
            o.location.y-=b 
            o.location.x+=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.x-=a 
                             
            o.location.y-=b 
            o.location.x+=a                    
            bpy.ops.object.mode_set(mode = 'EDIT')            

            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_EdgeMiddle_Minus_X) 


class Origin_CubeFront_EdgeMiddle_Plus_X(bpy.types.Operator):  
    bl_idname = "object.cubefront_edgemiddle_plus_x"  
    bl_label = "Origin to +X Edge / Middle of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.x+=a 
                             
            o.location.y-=b 
            o.location.x-=a                  
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     b=x.co.y
                     c=x.co.z

                     init=1
                 
                 elif x.co.x < a:
                     a=x.co.x
                     
                 elif x.co.y < b:
                     b=x.co.y
                 
                 elif x.co.z < c:
                     c=x.co.z
                     
            for x in o.data.vertices:
                 x.co.y+=b
                 x.co.x+=a 
                             
            o.location.y-=b 
            o.location.x-=a                  
            bpy.ops.object.mode_set(mode = 'EDIT')
    
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_EdgeMiddle_Plus_X) 



######################################----------------------------------------------------------------------------------
###  Origin to the Middle of Side  ### 
######################################


class Origin_CubeFront_Side_Minus_Y(bpy.types.Operator):  
    bl_idname = "object.cubefront_side_minus_y"  
    bl_label = "Origin to -Y Edge / Bottom of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.y
                     init=1
                 elif x.co.y<a:
                     a=x.co.y
                     
            for x in o.data.vertices:
                 x.co.y-=a
                             
            o.location.y+=a             
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()
        
        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.y
                     init=1
                 elif x.co.y<a:
                     a=x.co.y
                     
            for x in o.data.vertices:
                 x.co.y-=a
                             
            o.location.y+=a             
            bpy.ops.object.mode_set(mode = 'EDIT')            
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_Side_Minus_Y) 


class Origin_CubeFront_Side_Plus_Y(bpy.types.Operator):  
    bl_idname = "object.cubefront_side_plus_y"  
    bl_label = "Origin to +Y Edge / Bottom of CubeFront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':          
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.y
                     init=1
                 elif x.co.y<a:
                     a=x.co.y
                     
            for x in o.data.vertices:
                 x.co.y+=a
                             
            o.location.y-=a             
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.y
                     init=1
                 elif x.co.y<a:
                     a=x.co.y
                     
            for x in o.data.vertices:
                 x.co.y+=a
                             
            o.location.y-=a             
            bpy.ops.object.mode_set(mode = 'EDIT')                        
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_Side_Plus_Y) 


class Origin_CubeFront_Side_Minus_X(bpy.types.Operator):  
    bl_idname = "object.cubefront_side_minus_x"  
    bl_label = "Origin to -X Edge / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':           
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     init=1
                 elif x.co.x<a:
                     a=x.co.x
                     
            for x in o.data.vertices:
                 x.co.x-=a
                             
            o.location.x+=a                   
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     init=1
                 elif x.co.x<a:
                     a=x.co.x
                     
            for x in o.data.vertices:
                 x.co.x-=a
                             
            o.location.x+=a                   
            bpy.ops.object.mode_set(mode = 'EDIT')

        return {'FINISHED'}


bpy.utils.register_class(Origin_CubeFront_Side_Minus_X) 


class Origin_CubeFront_Side_Plus_X(bpy.types.Operator):  
    bl_idname = "object.cubefront_side_plus_x"  
    bl_label = "Origin to +X Edge / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':           
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     init=1
                 elif x.co.x<a:
                     a=x.co.x
                     
            for x in o.data.vertices:
                 x.co.x+=a
                             
            o.location.x-=a                   
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.x
                     init=1
                 elif x.co.x<a:
                     a=x.co.x
                     
            for x in o.data.vertices:
                 x.co.x+=a
                             
            o.location.x-=a                   
            bpy.ops.object.mode_set(mode = 'EDIT')
            
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_Side_Plus_X) 


class Origin_CubeFront_Side_Minus_Z(bpy.types.Operator):  
    bl_idname = "object.cubefront_side_minus_z"  
    bl_label = "Origin to -Z Edge / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':         
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.z
                     init=1
                 elif x.co.z<a:
                     a=x.co.z
                     
            for x in o.data.vertices:
                 x.co.z-=a
                             
            o.location.z+=a                   
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()

        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.z
                     init=1
                 elif x.co.z<a:
                     a=x.co.z
                     
            for x in o.data.vertices:
                 x.co.z-=a
                             
            o.location.z+=a                   
            bpy.ops.object.mode_set(mode = 'EDIT')
        
            
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_Side_Minus_Z) 


class Origin_CubeFront_Side_Plus_Z(bpy.types.Operator):  
    bl_idname = "object.cubefront_side_plus_z"  
    bl_label = "Origin to +Z Edge / Bottom of Cubefront"  
  
    def execute(self, context):
        if context.mode == 'OBJECT':        
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.z
                     init=1
                 elif x.co.z<a:
                     a=x.co.z
                     
            for x in o.data.vertices:
                 x.co.z+=a
                             
            o.location.z-=a                   
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.object.editmode_toggle()        
        
        else: 
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            o=bpy.context.active_object
            init=0
            for x in o.data.vertices:
                 if init==0:
                     a=x.co.z
                     init=1
                 elif x.co.z<a:
                     a=x.co.z
                     
            for x in o.data.vertices:
                 x.co.z+=a
                             
            o.location.z-=a                   
            bpy.ops.object.mode_set(mode = 'EDIT')


            
        
        return {'FINISHED'}

bpy.utils.register_class(Origin_CubeFront_Side_Plus_Z) 


###from curvetools2
class CurveOriginStart(bpy.types.Operator):
    bl_idname = "curve.origin_start_point"
    bl_label = "Origin to Start Point"
    bl_description = "Sets the origin of the active/selected curve to the starting point of the (first) spline. Nice for curve modifiers."

            
    def execute(self, context):
        blCurve = context.active_object
        blSpline = blCurve.data.splines[0]
        newOrigin = blCurve.matrix_world * blSpline.bezier_points[0].co
    
        origOrigin = bpy.context.scene.cursor_location.copy()
        print("--", "origOrigin: %.6f, %.6f, %.6f" % (origOrigin.x, origOrigin.y, origOrigin.z))
        print("--", "newOrigin: %.6f, %.6f, %.6f" % (newOrigin.x, newOrigin.y, newOrigin.z))
        
        bpy.context.scene.cursor_location = newOrigin
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.scene.cursor_location = origOrigin
        
        self.report({'INFO'}, "TODO: Origin to Start Point")
        
        return {'FINISHED'}


    
#######  Origin  #######-------------------------------------------------------                  
#######  Origin  #######------------------------------------------------------- 

class ORIGIN_SELECT_OBM(bpy.types.Operator):
    """set origin to selected / objectmode"""                 
    bl_idname = "origin.selected_obm"          
    bl_label = "origin to selected / toggle to objectmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}
     

class ORIGIN_SELECT_EDM(bpy.types.Operator):
    """set origin to selected / stay in editmode """                 
    bl_idname = "origin.selected_edm"          
    bl_label = "origin to selected / stay in editmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}    



class CurveDirection(bpy.types.Operator):
    """switch curve direction"""                 
    bl_idname = "curve.switch_direction_obm"        
    bl_label = "Curve Direction"                  
    #bl_options = {'REGISTER', 'UNDO'}  
        
    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.switch_direction()
        bpy.ops.object.editmode_toggle()        
        bpy.ops.curvetools2.operatororigintospline0start()        
        return {'FINISHED'}


############  Draw Menu  ############


#Menu for Editmode
class CustomAddMenu_EDM(bpy.types.Menu):
    bl_label = "Custom"
    bl_idname = "EDIT_MT_custom_Add_menu"

    def draw(self, context):
        layout = self.layout
                  
        layout.operator("mesh.s_plane_x", text="X-Plane")      
        layout.operator("mesh.s_plane_y", text="Y-Plane")       
        layout.operator("mesh.s_plane_z", text="Z-Plane")


#add a menu to objectmode
def draw_item_OBM(self, context):
    layout = self.layout
    layout.menu(CustomAddMenu_OBM.bl_idname, icon ="ROTATE") 


#add a menu to editmode
def draw_item_EDM(self, context):
    layout = self.layout
    if context.mode == 'EDIT_MESH':
        layout.menu(CustomAddMenu_EDM.bl_idname, icon ="ROTATE")  
        

#add single operator    
def draw_item_Vert(self, context):
    layout = self.layout
    if context.mode == 'EDIT_MESH':
        layout.operator("mesh.s_vertex", text="Vertex", icon = "LAYER_ACTIVE")


#add a menu to objectmode
def draw_item_Curve(self, context):
    layout = self.layout
    if context.mode == 'OBJECT':
        layout.separator()
        
        layout.operator("view3d.fullcurve","Bevel Curve", icon = "CURVE_BEZCURVE")
        layout.operator("view3d.fullcirlcecurve","Bevel Circle", icon = "CURVE_BEZCIRCLE")        
        

#add single operator    
def draw_item(self, context):
    layout = self.layout
    layout.operator("object.bounding_boxers","BBox", icon = "BBOX")
    
  
    
    
############  REGISTER  ############
  
def register():

    bpy.utils.register_class(BoundingBoxSource)
    bpy.utils.register_class(BoundingBox)

    bpy.utils.register_class(FullCurve)
    bpy.utils.register_class(FullCircleCurve)    
        
    bpy.utils.register_class(CustomAddMenu_OBM)
    bpy.utils.register_class(CustomAddMenu_EDM)
    
    bpy.utils.register_class(BBOXSET)

    #prepend = to MenuTop / append to MenuBottom 
    bpy.types.INFO_MT_add.prepend(draw_item) 
    bpy.types.INFO_MT_mesh_add.prepend(draw_item_Vert) 
        
    #bpy.types.INFO_MT_add.prepend(draw_item_OBM)
    bpy.types.INFO_MT_mesh_add.append(draw_item_EDM)
    bpy.types.INFO_MT_curve_add.append(draw_item_Curve)

   
    bpy.utils.register_module(__name__)
 
    
def unregister():

    
    bpy.utils.unregister_class(BoundingBoxSource)
    bpy.utils.unregister_class(BoundingBox)

    bpy.utils.unregister_class(FullCurve)
    bpy.utils.unregister_class(FullCircleCurve)     
    
    bpy.utils.unregister_class(CustomAddMenu_OBM)
    bpy.utils.unregister_class(CustomAddMenu_EDM)

    bpy.utils.unregister_class(BBOXSET)

    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()



















