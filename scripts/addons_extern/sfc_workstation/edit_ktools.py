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



#Adds Autotubes to the Addon Kjartan Tysdal     
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
                

"""
class KPANEL(bpy.types.Panel):
    bl_label = "KTools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Tools+'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.column(1)
        row.operator("mesh.autotubes")
        row.operator("mesh.shrinkwrap_smooth")
        
        row.operator_context = 'INVOKE_DEFAULT'
        row.operator("mesh.build_corner")
        
        row.operator("mesh.grow_loop")
        row.operator("mesh.shrink_loop")
        row.operator("mesh.extend_loop")
        row.operator("object.custom_autosmooth")
"""


#Register and Unregister all the operators
def register():

        #bpy.utils.register_class(KPANEL)
        bpy.utils.register_class(autotubes)
        bpy.utils.register_class(customAutoSmooth)
        bpy.utils.register_class(shrinkwrapSmooth)
        bpy.utils.register_class(buildCorner)
        bpy.utils.register_class(growLoop)
        bpy.utils.register_class(extendLoop)
        bpy.utils.register_class(shrinkLoop)


def unregister():

        #bpy.utils.unregister_class(KPANEL)
        bpy.utils.unregister_class(autotubes)
        bpy.utils.unregister_class(customAutoSmooth)
        bpy.utils.unregister_class(shrinkwrapSmooth)
        bpy.utils.unregister_class(buildCorner)
        bpy.utils.unregister_class(growLoop)
        bpy.utils.unregister_class(extendLoop)
        bpy.utils.unregister_class(shrinkLoop)




# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
        register()
 
 
