import bpy

# CREATE NEW
class VertexGroupToMask(bpy.types.Operator):
    '''Vertex Group To Mask'''
    bl_idname = "mesh.vgrouptomask"
    bl_label = "Vertex Group To Mask"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
     return context.active_object is not None and context.active_object.mode == 'SCULPT'

    def execute(self, context):

        dynatopoEnabled = False

        if context.active_object.mode == 'SCULPT' :
            if context.sculpt_object.use_dynamic_topology_sculpting :
                dynatopoEnabled = True

            if context.active_object.mode == 'SCULPT'and context.active_object.vertex_groups.active is not None :
                
                vGroupLocked = context.active_object.vertex_groups.active.lock_weight 
            
                if vGroupLocked == False :  
                    # Can only called by click event  > context fails poll
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action = 'DESELECT')
                    bpy.ops.mesh.select_mode(use_extend = False, use_expand = False, type = 'VERT')
                    bpy.ops.object.vertex_group_select()
                    
                    maskDataTrue = bpy.ops.mesh.customdata_clear_mask.poll() # Do we have mask data 
                    
                    if maskDataTrue :
                        bpy.ops.mesh.customdata_clear_mask() # Then clear it
                        
                    bpy.ops.mesh.hide(unselected = False)
                    bpy.ops.sculpt.sculptmode_toggle()
                    bpy.ops.paint.mask_flood_fill(mode = 'VALUE', value = 1)
                    bpy.ops.paint.hide_show(action = 'SHOW', area = 'ALL')
                    bpy.ops.paint.mask_flood_fill(mode = 'INVERT') 
               
                    if dynatopoEnabled :
                        bpy.ops.sculpt.dynamic_topology_toggle()
             
        return {'FINISHED'}

# APPEND
class VertexGroupToMaskAppend(bpy.types.Operator):
    '''Append Vertex Group To Mask'''
    bl_idname = "mesh.vgrouptomask_append"
    bl_label = "Append Vertex Group To Mask"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.mode == 'SCULPT'
    
    def execute(self, context):

        dynatopoEnabled = False

        if context.active_object.mode == 'SCULPT' :
            if context.sculpt_object.use_dynamic_topology_sculpting :
                dynatopoEnabled = True
                

            if context.active_object.mode == 'SCULPT'and context.active_object.vertex_groups.active is not None :
                
                vGroupLocked = context.active_object.vertex_groups.active.lock_weight 
            
                if vGroupLocked == False : 
                    # Can only called by click event  > context fails poll
                    bpy.ops.paint.hide_show(action = 'HIDE', area = 'MASKED') 
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_mode(use_extend = False, use_expand = False, type = 'VERT')
                    bpy.ops.mesh.select_all(action = 'DESELECT')
                    bpy.ops.mesh.reveal()
                    bpy.ops.object.vertex_group_select()
                    bpy.ops.mesh.customdata_clear_mask()
                    bpy.ops.mesh.hide(unselected = False)
                    bpy.ops.sculpt.sculptmode_toggle()
                    bpy.ops.paint.mask_flood_fill(mode = 'VALUE', value = 1)
                    bpy.ops.paint.hide_show(action = 'SHOW', area = 'ALL')
                    bpy.ops.paint.mask_flood_fill(mode = 'INVERT') 
               
                    if dynatopoEnabled :
                        bpy.ops.sculpt.dynamic_topology_toggle()
             
        return {'FINISHED'}
    
#REMOVE
class VertexGroupToMaskRemove(bpy.types.Operator):
    '''Remove Vertex Group From Mask'''
    bl_idname = "mesh.vgrouptomask_remove"
    bl_label = "Remove Vertex Group From Mask"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.mode == 'SCULPT'
    
    def execute(self, context):

        dynatopoEnabled = False

        if context.active_object.mode == 'SCULPT' :
            if context.sculpt_object.use_dynamic_topology_sculpting :
                dynatopoEnabled = True

            if context.active_object.mode == 'SCULPT'and context.active_object.vertex_groups.active is not None :
                
                vGroupLocked = context.active_object.vertex_groups.active.lock_weight 
                
                if vGroupLocked == False :
                    # Can only called by click event  > context fails poll
                    bpy.ops.paint.hide_show(action = 'HIDE', area = 'MASKED') 
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_mode(use_extend = False, use_expand = False, type = 'VERT')
                    bpy.ops.mesh.select_all(action = 'DESELECT')
                    bpy.ops.mesh.reveal()
                    bpy.ops.object.vertex_group_deselect()
                    bpy.ops.mesh.customdata_clear_mask()
                    bpy.ops.mesh.hide(unselected = False)
                    bpy.ops.sculpt.sculptmode_toggle()
                    bpy.ops.paint.mask_flood_fill(mode = 'VALUE', value = 1)
                    bpy.ops.paint.hide_show(action = 'SHOW', area = 'ALL')
                    bpy.ops.paint.mask_flood_fill(mode = 'INVERT') 
               
                    if dynatopoEnabled :
                        bpy.ops.sculpt.dynamic_topology_toggle()
             
        return {'FINISHED'}

def register():
	bpy.utils.register_module(__name__)



def unregister():
	bpy.utils.register_module(__name__)

   
if __name__ == "__main__":
    register()



