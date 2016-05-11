import bpy
bl_info = {
    "name": "sumie",
    "author": "SolPie",
    "version": (1, 0),
    "blender": (2, 69, 0),
    "location": "View3D > Specials > sumie",
    "description": "add sumie object",
    "warning": "",
    "category": "Object"}



offset = 0.06
diffuse = (0.02,0.002,0.002)
def sumie():
    ob = bpy.context.active_object
    #new object
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'})
    #new modiyies
    bpy.ops.object.modifier_add(type='SHRINKWRAP')
    bpy.context.object.modifiers["Shrinkwrap"].offset = offset
    bpy.context.object.modifiers["Shrinkwrap"].use_keep_above_surface = True
    bpy.context.object.modifiers["Shrinkwrap"].target = ob
    
    new_name = ob.name + '.sumie'
    ob = bpy.context.active_object
    ob.name = new_name
    ob.data.name = ob.name
    
    normal_inside(True)

    
    mat = sumie_mat()
    mesh = ob.data
    while len(mesh.materials):
        mesh.materials.pop()
    mesh.materials.append(mat)
    #show effect
    bpy.context.space_data.show_backface_culling = True

def sumie_mat():
    if bpy.data.materials.get('sumie'):
        mat = bpy.data.materials.get('sumie')

    else:
        #new mat
        mat = bpy.data.materials.new("sumie")

        mat.use_nodes = True
        mat.use_transparency = True
        mat.use_shadeless = True
        mat.use_cast_buffer_shadows = False
        mat.use_cast_approximate = False
        mat.use_raytrace = False
        mat.use_shadows = False
        mat.use_ray_shadow_bias = False
        mat.use_mist = False
        #diffuse on back side
        mat.translucency = 1
        mat.diffuse_color = diffuse
        #add node to tree
        tree = mat.node_tree
        links = tree.links
        # clear default nodes
        for n in tree.nodes:
            tree.nodes.remove(n)
        geom_node = tree.nodes.new('ShaderNodeGeometry')
        
        mat_node = tree.nodes.new('ShaderNodeMaterial')
        mat_node.location = 0,400
        mat_node.material = mat
        mat_node.use_specular = False
        
        output_node = tree.nodes.new('ShaderNodeOutput')
        output_node.location = 300,0
        
        links.new(geom_node.outputs[8], output_node.inputs[1])
        links.new(mat_node.outputs[0],output_node.inputs[0])
    return mat

def normal_inside(inside=False):
    #recalculate normals
    bpy.ops.object.editmode_toggle()
    #for some hide mesh
    bpy.ops.mesh.reveal()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent(inside=inside)
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.editmode_toggle()
    pass


class VIEW3D_PT_tools_sumie(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = "Sumie Generator"
    bl_context = "objectmode"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        active_obj = context.active_object
        layout = self.layout
        col = layout.column(align=True)

        col.operator("sumie.new", text="sumie object")
        col.operator("mesh.normals_outside", text="normal inside")


class Sumie(bpy.types.Operator):
    bl_idname = 'sumie.new'
    bl_label = 'Sumie object'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj and obj.type == 'MESH')
        
    def execute(self, context):
        sumie()
        return {'FINISHED'}

class NormalInsdie(bpy.types.Operator):
    bl_idname = 'mesh.normals_outside'
    bl_label = 'Sumie object'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj and obj.type == 'MESH')
        
    def execute(self, context):
        normal_inside(False)
        return {'FINISHED'}
        


def menu_func(self, context):
    self.layout.operator(Sumie.bl_idname, text=Sumie.bl_label)


def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_object_specials.append(menu_func)



def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.VIEW3D_MT_object_specials.remove(menu_func)
