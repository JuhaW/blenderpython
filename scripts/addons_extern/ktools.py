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
        'name': "Kjartans Scripts",
        'author': "Kjartan Tysdal",
        'location': '"Shift+Q" and also in EditMode "W-Specials/ KTools"',
        'description': "Adds my personal collection of small handy scripts (mostly modeling tools)",
        'category': "Mesh",
        'blender': (2, 7, 6),
        'version': (0, 2, 4),
        'wiki_url': 'http://www.kjartantysdal.com/scripts',
}


import bpy, bmesh 
from bpy.props import StringProperty, IntProperty, FloatProperty, EnumProperty, BoolProperty



#Adds Calculate Normals and Smooth to the Addon 
class calc_normals(bpy.types.Operator):
        """Calculates and smooths normals.""" 
        bl_idname = "mesh.calc_normals"          
        bl_label = "Calculate Normals"               
        bl_options = {'REGISTER', 'UNDO'} 
        
        invert = BoolProperty(name = "Invert Normals", description = "Inverts the normals.", default = False)

        def execute(self, context):
                
                invert = self.invert
                mode = bpy.context.active_object.mode

                if mode == 'OBJECT':

                        sel = bpy.context.selected_objects
                        active = bpy.context.scene.objects.active.name

                        bpy.ops.object.shade_smooth()


                        for ob in sel:
                                ob = ob.name
                                bpy.context.scene.objects.active = bpy.data.objects[ob] 
                                bpy.ops.object.editmode_toggle()
                                bpy.ops.mesh.select_all(action='SELECT')
                                bpy.ops.mesh.normals_make_consistent(inside=invert)
                                bpy.ops.object.editmode_toggle()

                        bpy.context.scene.objects.active = bpy.data.objects[active] 
                        
                elif mode == 'EDIT':
                        bpy.ops.mesh.normals_make_consistent(inside=invert)

                             
                
                return {'FINISHED'} 



#Adds SnapToAxis to the Addon   
class snaptoaxis(bpy.types.Operator):
        """Snaps selected vertices to zero on the selected axis.""" 
        bl_idname = "mesh.snaptoaxis"              
        bl_label = "Snap to Axis"               
        bl_options = {'REGISTER', 'UNDO'} 
        
        #worldspace = bpy.props.EnumProperty(items= (('OBJECT', 'Object Space', 'Snap to the object axis'), 
        #                                                                                         ('WORLD', 'World Space', 'Snap to the global axis')),
        #                                                                                         name = "Object/World", default = 'OBJECT')
        
        snap_x = BoolProperty(name = "Snap to X", description = "Snaps to zero in X. Also sets the axis for the mirror modifier if that button is turned on", default = True)
        snap_y = BoolProperty(name = "Snap to Y", description = "Snaps to zero in Y. Also sets the axis for the mirror modifier if that button is turned on", default = False)
        snap_z = BoolProperty(name = "Snap to Z", description = "Snaps to zero in Z. Also sets the axis for the mirror modifier if that button is turned on", default = False)
        
        mirror_add = BoolProperty(name = "Mirror Modifier", description = "Adds a mirror modifer", default = False)
        
        mirror_x = BoolProperty(name = "Mirror on X", description = "Sets the modifier to mirror on X", default = True)
        mirror_y = BoolProperty(name = "Mirror on Y", description = "Sets the modifier to mirror on Y", default = False)
        mirror_z = BoolProperty(name = "Mirror on Z", description = "Sets the modifier to mirror on Z", default = False)
        clipping = BoolProperty(name = "Enable Clipping", description = "Prevents vertices from going through the mirror during transform", default = True)


        def draw(self, context):
            layout = self.layout
            col = layout.column()
            
            col_move = col.column(align=True)
            row = col_move.row(align=True)
            if self.snap_x:
                row.prop(self, "snap_x", text = "X", icon='CHECKBOX_HLT')
            else:
                row.prop(self, "snap_x", text = "X", icon='CHECKBOX_DEHLT')
            if self.snap_y:
                row.prop(self, "snap_y", text = "Y", icon='CHECKBOX_HLT')
            else:
                row.prop(self, "snap_y", text = "Y", icon='CHECKBOX_DEHLT')
            if self.snap_z:
                row.prop(self, "snap_z", text = "Z", icon='CHECKBOX_HLT')
            else:
                row.prop(self, "snap_z", text = "Z", icon='CHECKBOX_DEHLT')
                
            col.separator()
           
            col_move = col.column(align=True)
            col_move.prop(self, "mirror_add", icon = 'MODIFIER') 
            row = col_move.row(align=True)
            
            row = col_move.row(align=True)
            row.active = self.mirror_add
            if self.mirror_x:
                row.prop(self, "mirror_x", text = "X", icon='CHECKBOX_HLT')
            else:
                row.prop(self, "mirror_x", text = "X", icon='CHECKBOX_DEHLT')
            if self.mirror_y:
                row.prop(self, "mirror_y", text = "Y", icon='CHECKBOX_HLT')
            else:
                row.prop(self, "mirror_y", text = "Y", icon='CHECKBOX_DEHLT')
            if self.mirror_z:
                row.prop(self, "mirror_z", text = "Z", icon='CHECKBOX_HLT')
            else:
                row.prop(self, "mirror_z", text = "Z", icon='CHECKBOX_DEHLT')
            
            col = col.column()
            col.active = self.mirror_add
            col.prop(self, "clipping")   


        def execute(self, context):

                mode = bpy.context.active_object.mode
                mirror_find = bpy.context.object.modifiers.find('Mirror')
                run = True
                

                if mode == 'EDIT':
                    loc = bpy.context.object.location
                    
                    
                    me = bpy.context.object.data
                    bm = bmesh.from_edit_mesh(me)

                    for v in bm.verts:
                            if v.select:
                                if self.snap_x == True:
                                    v.co.x = 0
                                if self.snap_y == True:
                                    v.co.y = 0
                                if self.snap_z == True:
                                    v.co.z = 0
                                

                    bmesh.update_edit_mesh(me, True, False)
                    
                if self.mirror_add == True:
                    
                    if mirror_find <= -1:
                        bpy.ops.object.modifier_add(type='MIRROR')
                        bpy.context.object.modifiers["Mirror"].use_clip = self.clipping
                        bpy.context.object.modifiers['Mirror'].show_viewport = True
                        
                        run = False
                        
                    if self.mirror_x == True:
                        bpy.context.object.modifiers["Mirror"].use_x = True
                    if self.mirror_x == False:
                        bpy.context.object.modifiers["Mirror"].use_x = False
                    if self.mirror_y == True:
                        bpy.context.object.modifiers["Mirror"].use_y = True
                    if self.mirror_y == False:
                        bpy.context.object.modifiers["Mirror"].use_y = False
                    if self.mirror_z == True:
                        bpy.context.object.modifiers["Mirror"].use_z = True
                    if self.mirror_z == False:
                        bpy.context.object.modifiers["Mirror"].use_z = False
                        
                        

                elif mirror_find >= 0 and self.mirror_add == False:
                    bpy.ops.object.modifier_remove(modifier="Mirror")
                    
                
                    
                    

                        

                        
                return {'FINISHED'} 



#Adds QuickBool to the Addon     
class quickbool(bpy.types.Operator):
        """Quickly carves out the selected polygons. Works best with manifold meshes.""" 
        bl_idname = "mesh.quickbool"                
        bl_label = "Quick Bool"             
        bl_options = {'REGISTER', 'UNDO'} 
        
        del_bool = BoolProperty(name="Delete BoolMesh", description="Deletes the objects used for the boolean operation.", default= True)
        move_to = BoolProperty(name="Move to layer 10", description="Moves the objects used for the boolean operation to layer 10", default= False)

        def execute(self, context):
                
                del_bool = self.del_bool
                move_to = self.move_to
                mode = bpy.context.active_object.mode

                if mode == 'EDIT':

                    #Boolean From Edit mode
                    bpy.ops.mesh.separate(type='SELECTED')
                    bpy.ops.object.editmode_toggle()

                    #get name of Original+Bool object
                    original = bpy.context.selected_objects[1].name
                    bool = bpy.context.selected_objects[0].name

                    #perform boolean
                    bpy.ops.object.modifier_add(type='BOOLEAN')
                    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[bool]
                    bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

                    #delete Bool object
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.ops.object.select_pattern(pattern=bool)

                    bpy.context.scene.objects.active = bpy.data.objects[bool]

                    #Delete all geo inside Shrink_Object
                    bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.delete(type='VERT')
                    bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)

                    bpy.ops.object.delete()

                    #re-enter edit mode on Original object
                    bpy.context.scene.objects.active = bpy.data.objects[original]
                    bpy.ops.object.select_pattern(pattern=original)
                    bpy.ops.object.editmode_toggle()
                        

                else:

                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                        original = bpy.context.active_object.name
                        bool = bpy.context.selected_objects
                        
                        
                        list = []
                        
                        for x in bool:
                                x = x.name
                                if x != original:
                                        list.append(x)

                        for name in list:
                                #Perform Boolean
                                bpy.ops.object.modifier_add(type='BOOLEAN')
                                bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[name]
                                bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
                                bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
                                
                                
                                if del_bool == True:
                                        
                                        bpy.ops.object.select_all(action='DESELECT')
                                        bpy.ops.object.select_pattern(pattern=name)
                                        bpy.context.scene.objects.active = bpy.data.objects[name]

                            #Delete all geo inside Shrink_Object
                                        bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)
                                        bpy.ops.mesh.select_all(action='SELECT')
                                        bpy.ops.mesh.delete(type='VERT')
                                        bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)
 
                                        bpy.ops.object.delete(use_global=False)
                                        bpy.context.scene.objects.active = bpy.data.objects[original] 
                                else: 
                                        bpy.ops.object.select_all(action='DESELECT')
                                        bpy.ops.object.select_pattern(pattern=name)
                                        bpy.context.scene.objects.active = bpy.data.objects[name] 

                                        bpy.context.object.draw_type = 'WIRE'
                                        
                                        # Move to garbage layer
                                        if move_to == True:
                                                bpy.ops.object.move_to_layer(layers=(False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False))
                                                
                                        bpy.context.scene.objects.active = bpy.data.objects[original] 
                                     

                        bpy.ops.object.mode_set(mode=mode, toggle=False)


                return {'FINISHED'} 



#Adds Autotubes to the Addon     
class autotubes(bpy.types.Operator):
        """Creates a spline tube based on selected edges""" 
        bl_idname = "mesh.autotubes"                
        bl_label = "Auto Tubes"             
        bl_options = {'REGISTER', 'UNDO'} 

        bevel = FloatProperty(name="Tube Width", description="Change width of the tube.", default=0.1, min = 0)
        res = IntProperty(name="Tube Resolution", description="Change resolution of the tube.", default=2, min = 0, max = 20)
        

        def execute(self, context):
                
                mode = bpy.context.active_object.mode
                type = bpy.context.active_object.type
                bevel = self.bevel  
                res = self.res
                

                if mode == 'EDIT' and type == 'MESH':
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        bpy.ops.object.duplicate()
                        
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.mesh.select_all(action='INVERT')
                        bpy.ops.mesh.delete(type='EDGE')
                        
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        bpy.ops.object.subdivision_set(level=0)
                        bpy.ops.object.convert(target='CURVE')
                        bpy.context.object.data.fill_mode = 'FULL'
                        bpy.context.object.data.bevel_depth = 0.1
                        bpy.context.object.data.splines[0].use_smooth = True
                        bpy.context.object.data.bevel_resolution = 2
                        bpy.ops.object.shade_smooth()
                        
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.curve.spline_type_set(type='BEZIER')
                        
                        bpy.context.object.data.bevel_depth = bevel
                        bpy.context.object.data.bevel_resolution = res
                        
                        #bpy.ops.transform.transform(('INVOKE_DEFAULT'), mode='CURVE_SHRINKFATTEN')
                        
                        
                        
                elif type == 'CURVE':
                        
                        bpy.context.object.data.bevel_depth = bevel
                        bpy.context.object.data.bevel_resolution = res
                        
                elif mode != 'EDIT' and type == 'MESH':
                        self.report({'ERROR'}, "This one only works in Edit mode")
                        return {'CANCELLED'}


                return {'FINISHED'} 



#Adds basicRename to the Addon      

class basicRename(bpy.types.Operator):
        """Renames everything to Banana"""          
        bl_idname = "object.basic_rename"            
        bl_label = "Basic Renamer"               
        bl_options = {'REGISTER', 'UNDO'} 

        name = StringProperty(name="Rename", description="Rename selected objects", default="banana")
        padding = IntProperty(name = "Number Padding", description = "Adds how many padded numbers", default = 3, min = 1, max = 8)
        prefix =    StringProperty(name="Pre Fix", description="Adds a Prefix to the name", default="")
        post_ob = StringProperty(name="Post Fix Object", description="Adds ending to object name", default="_MDL")
        post_data = StringProperty(name="Post Fix Data", description="Adds ending to data name", default="_DATA")
        

        def execute(self, context):          

                
                # The original script
                obj = bpy.context.selected_objects
                name = self.name
                padding = self.padding
                prefix = self.prefix
                post_ob = self.post_ob
                post_data = self.post_data
                number = 0
                for item in obj:
                        number += 1
                        item.name = "%s%s_%s%s" %(str(prefix), str(name), str(number).zfill(padding), str(post_ob))
                        item.data.name = "%s%s_%s%s" %(str(prefix), str(name), str(number).zfill(padding), str(post_data)) 
                        

                return {'FINISHED'}



class cut_tool(bpy.types.Operator):
        """Context sensitive cut tool""" 
        bl_idname = "mesh.cut_tool"          
        bl_label = "Cut Tool"               
        bl_options = {'REGISTER', 'UNDO'} 

        cuts = IntProperty(name="Number of Cuts", description="Change the number of cuts.", default=1, min = 1, soft_max = 10)
        loopcut = BoolProperty(name="Insert LoopCut", description="Makes a loop cut based on the selected edges", default= False)
        smoothness = FloatProperty(name="Smoothness", description="Change the smoothness.", default=0, min = 0, soft_max = 1)
        quad_corners = bpy.props.EnumProperty(items= (('INNERVERT', 'Inner Vert', 'How to subdivide quad corners'),  
                                                                                                 ('PATH', 'Path', 'How to subdivide quad corners'),
                                                                                                 ('STRAIGHT_CUT', 'Straight Cut', 'How to subdivide quad corners'),          
                                                                                                 ('FAN', 'Fan', 'How to subdivide quad corners')),
                                                                                                 name = "Quad Corner Type", default = 'STRAIGHT_CUT')        

        def execute(self, context):
                
                quad_corners = self.quad_corners
                cuts = self.cuts
                loopcut = self.loopcut
                smoothness = self.smoothness
                mode = bpy.context.active_object.mode

                if mode == 'EDIT':
                        
                        sel_mode = bpy.context.tool_settings.mesh_select_mode[:]
                        
                                                        #Checks and stores if any Vert, Edge or Face is selected.
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                        me = bpy.context.object.data
                        bm = bmesh.new()     # create an empty BMesh
                        bm.from_mesh(me)     # fill it in from a Mesh
                        sel = []
                        edge_sel = []
                        vert_sel = []

                        for v in bm.faces:
                                if v.select:
                                        sel.append(v.index)
                        for v in bm.edges:
                                if v.select:
                                        edge_sel.append(v.index)
                        for v in bm.verts:
                                if v.select:
                                        vert_sel.append(v.index)
                        
                        
                        bm.to_mesh(me)
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                                
                        if len(sel) == 0 and len(edge_sel) == 0 and len(vert_sel) == 0 :
                                bpy.ops.mesh.knife_tool("INVOKE_DEFAULT")
                                
                        elif sel_mode[2] == True and len(sel) > 1:

                                vgrp = bpy.context.object.vertex_groups.active_index
                                

                                #Store the Hidden Polygons
                                bpy.ops.mesh.select_all(action='SELECT')
                                bpy.ops.object.vertex_group_assign_new()
                                tmp_hidden = bpy.context.object.vertex_groups.active_index
                                bpy.ops.mesh.select_all(action='DESELECT')
                                
                                #Select faces to be cut
                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                                mesh = bpy.context.active_object.data.polygons

                                for f in sel:
                                        mesh[f].select = True

                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                                bpy.ops.mesh.hide(unselected=True)
                                bpy.ops.mesh.select_all(action='SELECT')
                                bpy.ops.mesh.region_to_loop()

                                #Store Boundry Edges
                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                                me = bpy.context.object.data
                                bm = bmesh.new()     
                                bm.from_mesh(me)     
                                boundry_edge = []

                                for v in bm.edges:
                                        if v.select:
                                                boundry_edge.append(v.index)

                                bm.to_mesh(me)

                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                                #Store Cut Edges
                                bpy.ops.mesh.select_all(action='INVERT')
                                bpy.ops.mesh.loop_multi_select(ring=True)

                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                                me = bpy.context.object.data
                                bm = bmesh.new()     
                                bm.from_mesh(me)     
                                cut_edges = []

                                for v in bm.edges:
                                        if v.select:
                                                cut_edges.append(v.index)

                                bm.to_mesh(me)

                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                                #Store Intersection edges
                                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
                                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')

                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                                me = bpy.context.object.data
                                bm = bmesh.new()     
                                bm.from_mesh(me)     
                                int_edges = []

                                for v in bm.edges:
                                        if v.select:
                                                int_edges.append(v.index)

                                bm.to_mesh(me)

                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                                #Modify Lists
                                for x in int_edges:
                                        if x in boundry_edge:
                                                cut_edges.remove(x)
                                                
                                bpy.ops.mesh.select_all(action='DESELECT')

                                #Select the new edges to cut
                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                                mesh = bpy.context.active_object.data.edges

                                for f in cut_edges:
                                        mesh[f].select = True
                                        
                                #Perform cut and select the cut line.
                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                                bpy.ops.mesh.subdivide(number_cuts = cuts, smoothness = smoothness, quadcorner = quad_corners)
                                bpy.ops.mesh.select_all(action='SELECT')
                                bpy.ops.mesh.region_to_loop()
                                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                                bpy.ops.mesh.select_all(action='INVERT')
                                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
                                bpy.ops.mesh.loop_multi_select(ring=False)

                                #Store cut line.
                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                                me = bpy.context.object.data
                                bm = bmesh.new()     
                                bm.from_mesh(me)     
                                cut_line = []

                                for v in bm.edges:
                                        if v.select:
                                                cut_line.append(v.index)

                                bm.to_mesh(me)
                                
                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                                bpy.ops.mesh.reveal()
                                bpy.ops.mesh.select_all(action='DESELECT')

                                bpy.context.object.vertex_groups.active_index = tmp_hidden
                                bpy.ops.object.vertex_group_select()
                                bpy.ops.mesh.hide(unselected=True)


                                bpy.ops.mesh.select_all(action='DESELECT')


                                #Select Cutline
                                if cuts <= 1:
                                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                                        mesh = bpy.context.active_object.data.edges

                                        for f in cut_line:
                                                mesh[f].select = True
                                        
                                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                                        
                                bpy.ops.object.vertex_group_remove(all=False)
                                bpy.ops.mesh.select_mode(use_extend=True, use_expand=False, type='FACE')

                        elif sel_mode[0] == True:
                                bpy.ops.mesh.vert_connect_path()
                                
                        elif sel_mode[1] == True and loopcut == False:
                                bpy.ops.mesh.subdivide(number_cuts = cuts, smoothness = smoothness, quadcorner = quad_corners)
                                
                        elif sel_mode[1] == True and loopcut == True:
                                bpy.ops.mesh.loop_multi_select(ring=True)
                                bpy.ops.mesh.subdivide(number_cuts = cuts, smoothness = smoothness, quadcorner = quad_corners)
                
                else:
                        self.report({'ERROR'}, "This one only works in Edit mode")

                return {'FINISHED'} 



#Adds customAutoSmooth to the Addon  

class customAutoSmooth(bpy.types.Operator):
        """Set AutoSmooth angle"""          
        bl_idname = "object.custom_autosmooth"              
        bl_label = "Autosmooth"             
        bl_options = {'REGISTER', 'UNDO'} 

        angle = FloatProperty(name="AutoSmooth Angle", description="Set AutoSmooth angle", default= 30.0, min = 0.0, max = 180.0)
        

        def execute(self, context):          

                mode = bpy.context.active_object.mode
                
                if mode != 'OBJECT':
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
     
                ob = bpy.context.selected_objects
                angle = self.angle
                angle = angle * (3.14159265359/180)
                
                bpy.ops.object.shade_smooth()

                for x in ob:
                        x = x.name
                        bpy.data.objects[x].data.use_auto_smooth = True
                        bpy.data.objects[x].data.auto_smooth_angle = angle
                        
                bpy.ops.object.mode_set(mode=mode, toggle=False)        

                return {'FINISHED'}

#Adds shrinkwrapSmooth to the Addon  

class shrinkwrapSmooth(bpy.types.Operator):
        """Smooths the selected vertices while trying to keep the original shape with a shrinkwrap modifier. """            
        bl_idname = "mesh.shrinkwrap_smooth"                
        bl_label = "Shrinkwrap Smooth"               
        bl_options = {'REGISTER', 'UNDO'} 

        #iterate = IntProperty(name="Iterate Smooth", description="More or less smoothing.", default= 6, min = 0, soft_max = 20)
        pin = BoolProperty(name="Pin Selection Border", description="Pins the outer edge of the selection.", default = True)
        mode = bpy.props.EnumProperty(items= (('PROJECT', 'Project', 'Best results, but can cause wonky geometry in certain cases'),        
                                                                                                 ('NEAREST_SURFACEPOINT', 'Nearest Surface', 'Very stable, but can giv slightly worse results')),
                                                                                                 name = "Shrinkwrap Mode", default = 'NEAREST_SURFACEPOINT')            



        def execute(self, context):
                
                iterate = 6
                pin = self.pin
                mode = self.mode
                data = bpy.context.object.data.name


                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)
                org_ob = bpy.context.object.name

                # Create intermediate object
                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)
                bpy.ops.mesh.primitive_plane_add(radius=1, view_align=False, enter_editmode=False)
                bpy.context.object.data = bpy.data.meshes[data]
                tmp_ob = bpy.context.object.name


                bpy.ops.object.duplicate(linked=False)
                shrink_ob = bpy.context.object.name

                bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.object.select_pattern(pattern=tmp_ob)
                bpy.context.scene.objects.active = bpy.data.objects[tmp_ob] 

                bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')


                if pin == True:
                		bpy.ops.object.vertex_group_assign_new()
                		org_id = bpy.context.object.vertex_groups.active_index
                		
                		bpy.ops.object.vertex_group_assign_new()
                		sel = bpy.context.object.vertex_groups.active.name
                		sel_id = bpy.context.object.vertex_groups.active_index
                		
                		bpy.ops.mesh.region_to_loop()
                		bpy.ops.object.vertex_group_remove_from(use_all_groups=False, use_all_verts=False)
                		
                		bpy.ops.mesh.select_all(action='SELECT')
                		bpy.ops.mesh.region_to_loop()
                		bpy.ops.object.vertex_group_remove_from(use_all_groups=False, use_all_verts=False)
                		
                		bpy.ops.mesh.select_all(action='DESELECT')
                		bpy.ops.object.vertex_group_select(sel_id)
                		
                		
                else:
                		bpy.ops.object.vertex_group_assign_new()
                		sel = bpy.context.object.vertex_groups.active.name	  


                for x in range(iterate):
                		bpy.ops.object.modifier_add(type='SHRINKWRAP')
                		mod_id = (len(bpy.context.object.modifiers)-1)
                		shrink_name = bpy.context.object.modifiers[mod_id].name

                		bpy.context.object.modifiers[shrink_name].target = bpy.data.objects[shrink_ob]
                		bpy.context.object.modifiers[shrink_name].vertex_group = sel
                		
                		if mode == 'PROJECT':
                				bpy.context.object.modifiers[shrink_name].wrap_method = 'PROJECT'
                				bpy.context.object.modifiers[shrink_name].use_negative_direction = True
                				bpy.context.object.modifiers[shrink_name].cull_face = 'FRONT'
                		else:
                				bpy.context.object.modifiers[shrink_name].wrap_method = 'NEAREST_SURFACEPOINT'


                		bpy.ops.mesh.vertices_smooth(factor=1, repeat=1)


                		bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)
                		bpy.ops.object.convert(target='MESH')
                		bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)
                		

                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)

                bpy.ops.object.vertex_group_remove(all = False)
                bpy.ops.object.modifier_remove(modifier=shrink_name)

                bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.object.select_pattern(pattern=shrink_ob)
                bpy.context.scene.objects.active = bpy.data.objects[shrink_ob] 

                #Delete all geo inside Shrink_Object
                bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.delete(type='VERT')
                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)

                bpy.ops.object.delete(use_global=True)

                bpy.ops.object.select_pattern(pattern=tmp_ob)
                bpy.context.scene.objects.active = bpy.data.objects[tmp_ob] 


                bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)

                if pin == True:
                		bpy.ops.mesh.select_all(action='DESELECT')
                		bpy.ops.object.vertex_group_select(sel_id)

                bpy.ops.object.mode_set(mode = 'OBJECT', toggle = False)

                bpy.ops.object.delete(use_global=False)


                bpy.ops.object.select_pattern(pattern=org_ob)
                bpy.context.scene.objects.active = bpy.data.objects[org_ob] 

                bpy.ops.object.mode_set(mode = 'EDIT', toggle = False)


                return {'FINISHED'}

#Adds buildCorner to the Addon      

class buildCorner(bpy.types.Operator):
        """Builds corner topology. Good for converting ngons"""
        bl_idname = "mesh.build_corner"
        bl_label = "Build Corner"
        bl_options = {'REGISTER', 'UNDO'} 

        offset = IntProperty()
        
        def modal(self, context, event):
                
                if event.type == 'MOUSEMOVE':
                        
                        delta = self.offset - event.mouse_x
                        
                        if delta >= 0:
                                offset = 1
                        else:
                                offset = 0
                                
                        bpy.ops.mesh.edge_face_add()
                                
                        bpy.ops.mesh.poke()
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                        bpy.ops.object.vertex_group_assign_new()
                        sel_id = bpy.context.object.vertex_groups.active_index

                        bpy.ops.mesh.region_to_loop()
                        bpy.ops.object.vertex_group_remove_from()

                        bpy.ops.mesh.select_nth(nth=2, skip=1, offset=offset)

                        bpy.ops.object.vertex_group_select(sel_id)

                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
                        bpy.ops.mesh.dissolve_mode(use_verts=False)

                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                        bpy.ops.object.vertex_group_select()
                        bpy.ops.mesh.select_more()

                        bpy.ops.object.vertex_group_remove(all = False)
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
                                

                elif event.type == 'LEFTMOUSE':
                        return {'FINISHED'}

                elif event.type in {'RIGHTMOUSE', 'ESC'}:
                    bpy.ops.ed.undo()
                    return {'CANCELLED'}

                return {'RUNNING_MODAL'}

        def invoke(self, context, event):
                if context.object:
                        
                        # Check selection
                        
                        bpy.ops.mesh.edge_face_add()
                        bpy.ops.mesh.region_to_loop()
                         
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                        me = bpy.context.object.data
                        bm = bmesh.new()     # create an empty BMesh
                        bm.from_mesh(me)     # fill it in from a Mesh

                        face_sel = []
                        edge_sel = []
                        

                        for v in bm.faces:
                                if v.select:
                                        face_sel.append(v.index)
                        for v in bm.edges:
                                if v.select:
                                        edge_sel.append(v.index)

                        
                        
                        bm.to_mesh(me)
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.mesh.loop_to_region()

                        
                        ###################################
                        
                        edge_sel = len(edge_sel)
                        
                        if edge_sel == 4:
                                return {'FINISHED'}
                        
                        elif edge_sel%2 == 0:
                                self.offset = event.mouse_x
                                context.window_manager.modal_handler_add(self)
                                return {'RUNNING_MODAL'}
                        
                        #elif edge_sel == 5:
                        #    bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
                        #    bpy.ops.mesh.tris_convert_to_quads(face_threshold=3.14159, shape_threshold=3.14159)
                        #    return {'FINISHED'}
                                
                        else:
                                bpy.ops.mesh.poke()
                                bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
                                bpy.ops.mesh.tris_convert_to_quads(face_threshold=3.14159, shape_threshold=3.14159)
                                return {'FINISHED'}
                        

                else:
                        self.report({'WARNING'}, "No active object, could not finish")
                        return {'CANCELLED'}

        
#Adds growLoop to the Addon  

class growLoop(bpy.types.Operator):
        """Grows the selected edges in both directions """          
        bl_idname = "mesh.grow_loop"                
        bl_label = "Grow Loop"               
        bl_options = {'REGISTER', 'UNDO'} 

        grow = IntProperty(name="Grow Selection", description="How much to grow selection", default= 1, min=1, soft_max=10)
        
        def execute(self, context):
                
                grow = self.grow
                sel_mode = bpy.context.tool_settings.mesh_select_mode[:]
                
                for x in range(grow):
                        if sel_mode[2] == True:
                        
                                edge_sel = []
                                border = []
                                interior = []
                                face_org = []
                                face_loop = []
                                face_grow = []
                                face_sel = []
                                mesh_edges = bpy.context.active_object.data.edges
                                mesh_faces = bpy.context.active_object.data.polygons

                                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')   

                                me = bpy.context.object.data
                                bm = bmesh.from_edit_mesh(me)

                                for e in bm.edges:
                                        if e.select:
                                                edge_sel.append(e.index)

                                for f in bm.faces:
                                        if f.select:
                                                face_org.append(f.index)

                                bpy.ops.mesh.region_to_loop()

                                for e in bm.edges:
                                        if e.select:
                                                border.append(e.index)
                                                


                                for e in edge_sel:
                                        if e not in border:
                                                interior.append(e)

                                bmesh.update_edit_mesh(me, True, False)


                                bpy.ops.mesh.select_all(action='DESELECT')

                                #Select the interior edges
                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)


                                for e in interior:
                                        mesh_edges[e].select = True

                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                                bpy.ops.mesh.loop_multi_select(ring=True)
                                bpy.ops.mesh.select_mode(use_extend=False, use_expand=True, type='FACE')

                                me = bpy.context.object.data
                                bm = bmesh.from_edit_mesh(me)

                                for f in bm.faces:
                                        if f.select:
                                                face_loop.append(f.index)

                                bmesh.update_edit_mesh(me, True, False)

                                bpy.ops.mesh.select_all(action='DESELECT')


                                # Select original faces
                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                                for x in face_org:
                                        mesh_faces[x].select = True
                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)


                                bpy.ops.mesh.select_more(use_face_step=False)

                                me = bpy.context.object.data
                                bm = bmesh.from_edit_mesh(me)

                                for f in bm.faces:
                                        if f.select:
                                                face_grow.append(f.index)

                                for f in face_grow:
                                        if f in face_loop:
                                                face_sel.append(f)
                                                
                                for f in face_org:
                                        face_sel.append(f)
                                                
                                bmesh.update_edit_mesh(me, True, False)

                                bpy.ops.mesh.select_all(action='DESELECT')

                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                                for f in face_sel:
                                        mesh_faces[f].select = True

                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        
                        else:
                                mesh = bpy.context.active_object.data.edges

                                me = bpy.context.object.data
                                bm = bmesh.from_edit_mesh(me)
                                org_sel = []
                                grow_sel = []
                                loop_sel = []
                                sel = []

                                bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')

                                for e in bm.edges:
                                        if e.select:
                                                org_sel.append(e.index)
                                                
                                bpy.ops.mesh.select_more(use_face_step=False)

                                for e in bm.edges:
                                        if e.select:
                                                grow_sel.append(e.index)

                                bpy.ops.mesh.select_all(action='DESELECT')

                                bmesh.update_edit_mesh(me, True, False)
                                
                                # Select the original edges
                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                                for e in org_sel:
                                        mesh[e].select = True                               
                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                                
                                me = bpy.context.object.data
                                bm = bmesh.from_edit_mesh(me)
                                bpy.ops.mesh.loop_multi_select(ring=False)

                                for e in bm.edges:
                                        if e.select:
                                                loop_sel.append(e.index)

                                bmesh.update_edit_mesh(me, True, False)

                                bpy.ops.mesh.select_all(action='DESELECT')

                                for x in loop_sel:
                                        if x in grow_sel:
                                                sel.append(x)
                                                
                                bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                                for e in sel:
                                        mesh[e].select = True                               
                                bpy.ops.object.mode_set(mode='EDIT', toggle=False)  
                        
                        bpy.context.tool_settings.mesh_select_mode = sel_mode
                
                return {'FINISHED'}

#Adds extendLoop to the Addon    

class extendLoop(bpy.types.Operator):
        """Uses the active face or edge to extends the selection in one direction"""            
        bl_idname = "mesh.extend_loop"              
        bl_label = "Extend Loop"                 
        bl_options = {'REGISTER', 'UNDO'} 

        extend = IntProperty(name="Extend Selection", description="How much to extend selection", default= 1, min=1, soft_max=10)
        
        def execute(self, context):
                
                sel_mode = bpy.context.tool_settings.mesh_select_mode[:]
                extend = self.extend
                
                for x in range(extend):
                    if sel_mode[2] == True:
                        
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        active_face = bpy.context.object.data.polygons.active # find active face
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                        edge_sel = []
                        interior = []
                        face_org = []
                        face_loop = []
                        face_grow = []
                        face_sel = []
                        active_edges = []

                        # Get face selection
                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        for f in bm.faces:
                                if f.select:
                                        face_org.append(f.index)
                                        
                        face_org.remove(active_face)


                        bmesh.update_edit_mesh(me, True, False)

                        bpy.ops.mesh.select_all(action='DESELECT')
                        mesh = bpy.context.active_object.data.polygons

                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        for x in face_org:
                                mesh[x].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)



                        # Get edge selection
                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        for e in bm.edges:
                                if e.select:
                                        edge_sel.append(e.index)


                        bmesh.update_edit_mesh(me, True, False)


                        # Select Active Face
                        bpy.ops.mesh.select_all(action='DESELECT')
                        mesh = bpy.context.active_object.data.polygons

                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        mesh[active_face].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')

                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)


                        # Store the interior edge

                        for e in bm.edges:
                                if e.select:
                                        active_edges.append(e.index)
                                        

                        for e in active_edges:
                                if e in edge_sel:
                                        interior.append(e)

                        bmesh.update_edit_mesh(me, True, False)


                        bpy.ops.mesh.select_all(action='DESELECT')

                        #Select the interior edges
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                        mesh = bpy.context.active_object.data.edges

                        for e in interior:
                                mesh[e].select = True

                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)


                        bpy.ops.mesh.loop_multi_select(ring=True)
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=True, type='FACE')


                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        for f in bm.faces:
                                if f.select:
                                        face_loop.append(f.index)

                                        
                        bmesh.update_edit_mesh(me, True, False)

                        bpy.ops.mesh.select_all(action='DESELECT')

                        # Select active face
                        mesh = bpy.context.active_object.data.polygons

                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        mesh[active_face].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.mesh.select_more(use_face_step=False)


                        face_org.append(active_face)

                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        for f in bm.faces:
                                if f.select:
                                        face_grow.append(f.index)

                        for f in face_grow:
                                if f in face_loop:
                                        face_sel.append(f)
                                        
                        for f in face_sel:
                                if f not in face_org:
                                        active_face = f
                                        
                        for f in face_org:
                                face_sel.append(f)
                                        
                        bmesh.update_edit_mesh(me, True, False)

                        bpy.ops.mesh.select_all(action='DESELECT')

                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                        for f in face_sel:
                                mesh[f].select = True
                        bpy.context.object.data.polygons.active = active_face

                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        
                    elif sel_mode[1] == True:

                        mesh = bpy.context.active_object.data
                        org_sel = []
                        grow_sel = []
                        loop_sel = []
                        sel = []
                        org_verts = []
                        active_verts = []
                        
                        # Get active edge
                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        for x in reversed(bm.select_history):
                                if isinstance(x, bmesh.types.BMEdge):
                                        active_edge = x.index
                                        break

                        # Store the originally selected edges
                        for e in bm.edges:
                                if e.select:
                                        org_sel.append(e.index)
                                        

                        bmesh.update_edit_mesh(me, True, False)
                                        
                        # Select active edge
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        mesh.edges[active_edge].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                        # Get verts of active edge
                        bm = bmesh.from_edit_mesh(me)
                        
                        for v in bm.verts:
                                if v.select:
                                        active_verts.append(v.index)
                                        
                        bmesh.update_edit_mesh(me, True, False)
                        
                        # Select original selection minus active edge
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        for x in org_sel:
                            mesh.edges[x].select = True
                        mesh.edges[active_edge].select = False
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        
                        bm = bmesh.from_edit_mesh(me)
                        
                        # Store the original vertices minus active edge
                        for v in bm.verts:
                            if v.select:
                                org_verts.append(v.index)
                        
                        
                        # Compare verts
                        for x in active_verts:
                            if x in org_verts:
                                active_verts.remove(x)
                        
                        bmesh.update_edit_mesh(me, True, False)
                        
                        # Select end vertex
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        mesh.vertices[active_verts[0]].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        
                        
                        # Grow the end vertex and store the edges
                        bpy.ops.mesh.select_more(use_face_step=False)
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
                        bm = bmesh.from_edit_mesh(me)
                        
                        for e in bm.edges:
                                if e.select:
                                        grow_sel.append(e.index)

                        bmesh.update_edit_mesh(me, True, False)
                        bpy.ops.mesh.select_all(action='DESELECT')

                        # Run loop of the active edges and store it
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        mesh.edges[active_edge].select = True                   
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        bpy.ops.mesh.loop_multi_select(ring=False)

                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        for e in bm.edges:
                                if e.select:
                                        loop_sel.append(e.index)

                        bmesh.update_edit_mesh(me, True, False)
                        bpy.ops.mesh.select_all(action='DESELECT')

                        # Compare loop_sel vs grow_sel
                        for x in loop_sel:
                                if x in grow_sel:
                                        sel.append(x)


                        # Add original selection to new selection

                        for x in org_sel:
                            if x not in sel:
                                sel.append(x)
                                

                        # Compare org_sel with sel to get the active edge
                        for x in sel:
                            if x not in org_sel:
                                active_edge = x
                                
                        # Select the resulting edges
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        for e in sel:
                                mesh.edges[e].select = True                             
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                        # Set the new active edge
                        bm = bmesh.from_edit_mesh(me)

                        bm.edges.ensure_lookup_table()
                        bm.select_history.add(bm.edges[active_edge])
                        bmesh.update_edit_mesh(me, True, False)
                        
                
                return {'FINISHED'}


#Adds extendLoop to the Addon    

class shrinkLoop(bpy.types.Operator):
        """Shrink the selected loop"""          
        bl_idname = "mesh.shrink_loop"              
        bl_label = "Shrink Loop"                 
        bl_options = {'REGISTER', 'UNDO'} 

        shrink = IntProperty(name="Shrink Selection", description="How much to shrink selection", default= 1, min=1, soft_max=15)
        
        def execute(self, context):
                
                sel_mode = bpy.context.tool_settings.mesh_select_mode[:]
                shrink = self.shrink
                
                for x in range(shrink):
                    if sel_mode[2] == True:
                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)
                        mesh = bpy.context.active_object.data

                        sel = []
                        edge_dic = {}
                        vert_list = []
                        end_verts = []
                        org_faces = []
                        cur_faces = []
                        new_faces = []

                        # Store edges and verts
                        for e in bm.edges:
                            if e.select:
                                sel.append(e.index)
                                
                                # Populate vert_list
                                vert_list.append(e.verts[0].index)
                                vert_list.append(e.verts[1].index)
                                
                                # Store dictionary
                                edge_dic[e.index] = [e.verts[0].index, e.verts[1].index]

                        # Store original faces
                        for f in bm.faces:
                            if f.select:
                                org_faces.append(f.index)

                        # Store end verts
                        for v in vert_list:
                            if vert_list.count(v) == 2:
                                end_verts.append(v)
                                
                        # Check verts in dictionary
                        for key, value in edge_dic.items():
                            if value[0] in end_verts:
                                sel.remove(key)
                                continue
                            if value[1] in end_verts:
                                sel.remove(key)


                        bmesh.update_edit_mesh(me, True, False)

                        # Select the resulting edges
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                        for e in sel:
                            mesh.edges[e].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')

                        bm = bmesh.from_edit_mesh(me)

                        # Store current faces
                        for f in bm.faces:
                            if f.select:
                                cur_faces.append(f.index)

                        # Compare current and original faces
                        for x in org_faces:
                            if x in cur_faces:
                                new_faces.append(x)

                        bmesh.update_edit_mesh(me, True, False)

                        # Select the resulting faces
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

                        for e in new_faces:
                            mesh.polygons[e].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                    
                    else:
                        me = bpy.context.object.data
                        bm = bmesh.from_edit_mesh(me)

                        sel = []
                        edge_dic = {}
                        vert_list = []
                        end_verts = []

                        # Store edges and verts in dictionary
                        for e in bm.edges:
                            if e.select:
                                sel.append(e.index)
                                
                                # Populate vert_list
                                vert_list.append(e.verts[0].index)
                                vert_list.append(e.verts[1].index)
                                
                                # Store dictionary
                                edge_dic[e.index] = [e.verts[0].index, e.verts[1].index]

                        # Store end verts
                        for v in vert_list:
                            if vert_list.count(v) == 1:
                                end_verts.append(v)
                                
                        # Check verts in dictionary
                        for key, value in edge_dic.items():
                            if value[0] in end_verts:
                                sel.remove(key)
                                continue
                            if value[1] in end_verts:
                                sel.remove(key)


                        bmesh.update_edit_mesh(me, True, False)

                        # Select the resulting edges
                        bpy.ops.mesh.select_all(action='DESELECT')

                        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
                        mesh = bpy.context.active_object.data.edges
                        for e in sel:
                            mesh[e].select = True
                        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
                        
                
                return {'FINISHED'}



#Draws the Custom Menu in Object Mode
class ktools_menu(bpy.types.Menu):
        bl_label = "KTools - Object Mode"
        bl_idname = "OBJECT_MT_ktools_menu"

        def draw(self, context):

                layout = self.layout

                layout.operator("mesh.quickbool")
                layout.operator("mesh.calc_normals")
                layout.operator("object.custom_autosmooth")
                layout.operator("object.basic_rename")

                
#Draws the Custom Menu in Edit Mode
class VIEW3D_MT_edit_mesh_ktools_menuEdit(bpy.types.Menu):
        bl_label = "KTools - Edit Mode"
        bl_idname = "VIEW3D_MT_edit_mesh_ktools_menuEdit"

        def draw(self, context):
                
                

                layout = self.layout

                layout.operator("mesh.cut_tool")
                layout.operator("mesh.snaptoaxis")
                layout.operator("mesh.autotubes")
                layout.operator("mesh.shrinkwrap_smooth")
                
                layout.operator_context = 'INVOKE_DEFAULT'
                layout.operator("mesh.build_corner")
                
                layout.operator("mesh.grow_loop")
                layout.operator("mesh.shrink_loop")
                layout.operator("mesh.extend_loop")
                
                layout.separator()

                layout.operator("mesh.quickbool")            
                layout.operator("object.custom_autosmooth")
                layout.operator("mesh.calc_normals")
                layout.operator("object.basic_rename")



#Calls the KTools Menu
class ktools(bpy.types.Operator): #Namesuggestion: K-Tools or K-Mac
        """Calls the KTools Menu""" 
        bl_idname = "object.ktools"          
        bl_label = "KTools"             
        #bl_options = {'REGISTER', 'UNDO'}  

        def execute(self, context):
                
                mode = bpy.context.active_object.mode
                
                if mode == 'OBJECT':
                
                        bpy.ops.wm.call_menu(name=ktools_menu.bl_idname)
                        
                elif mode == 'EDIT':
                
                        bpy.ops.wm.call_menu(name=VIEW3D_MT_edit_mesh_ktools_menuEdit.bl_idname)

                return {'FINISHED'} 

# draw function for integration in menus
def menu_func(self, context):
    self.layout.separator()
    self.layout.menu("VIEW3D_MT_edit_mesh_ktools_menuEdit", text = "KTools")
    

#Register and Unregister all the operators
def register():
        bpy.utils.register_class(calc_normals)
        bpy.utils.register_class(snaptoaxis)
        bpy.utils.register_class(quickbool)
        bpy.utils.register_class(autotubes)
        bpy.utils.register_class(basicRename)
        bpy.utils.register_class(cut_tool)
        bpy.utils.register_class(customAutoSmooth)
        bpy.utils.register_class(shrinkwrapSmooth)
        bpy.utils.register_class(buildCorner)
        bpy.utils.register_class(growLoop)
        bpy.utils.register_class(extendLoop)
        bpy.utils.register_class(shrinkLoop)
        bpy.utils.register_class(ktools_menu)
        bpy.utils.register_class(VIEW3D_MT_edit_mesh_ktools_menuEdit)
        bpy.utils.register_class(ktools)
        bpy.types.VIEW3D_MT_edit_mesh_specials.append(menu_func)
        
        kc = bpy.context.window_manager.keyconfigs.addon
        if kc:
            km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
            kmi = km.keymap_items.new('object.ktools', 'Q', 'PRESS', shift=True)
            # Could pass settings to operator properties here
            #kmi.properties.mode = (False, True, False)


def unregister():
        bpy.utils.unregister_class(calc_normals)
        bpy.utils.unregister_class(snaptoaxis)
        bpy.utils.unregister_class(quickbool)
        bpy.utils.unregister_class(autotubes)
        bpy.utils.unregister_class(basicRename)
        bpy.utils.unregister_class(cut_tool)
        bpy.utils.unregister_class(customAutoSmooth)
        bpy.utils.unregister_class(shrinkwrapSmooth)
        bpy.utils.unregister_class(buildCorner)
        bpy.utils.unregister_class(growLoop)
        bpy.utils.unregister_class(extendLoop)
        bpy.utils.unregister_class(shrinkLoop)
        bpy.utils.unregister_class(ktools_menu)
        bpy.utils.unregister_class(VIEW3D_MT_edit_mesh_ktools_menuEdit)
        bpy.utils.unregister_class(ktools)
        bpy.types.VIEW3D_MT_edit_mesh_specials.remove(menu_func)

        kc = bpy.context.window_manager.keyconfigs.addon
        if kc:
            km = kc.keymaps["3D View"]
            for kmi in km.keymap_items:
                if kmi.idname == 'object.ktools':
                    km.keymap_items.remove(kmi)
                    break



# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
        register()
 
 
