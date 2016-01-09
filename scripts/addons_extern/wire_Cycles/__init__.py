bl_info = {
    "name": "Wire for Cycles",
    "author": "edddy (edddy74@live.fr)",
    "version": (0, 3, 111221),
    "blender": (2, 6, 1),
    "api": 42615,
    "location": "View3D > Tools > Wire shader Cycles",
    "description": "Wire shader for Cycles",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "http://blenderclan.tuxfamily.org/html/modules/newbb/viewtopic.php?topic_id=33099",
    "category": "Material"}


import bpy

# fonction pricipale
def wire(context):
    wc = bpy.context.window_manager.wireconfig
    bpy.ops.mesh.uv_texture_add() #ajouter un UVlayer 
    context.active_object.data.uv_textures.active.name="layerWire" #renommer cet UVlayer
    # creer une liste de chemins possibles vers le rep du addon
    filepath = bpy.utils.script_paths("addons/wire_Cycles/")

    #import des mat (a condition qu'elles ne le soit pas deja)
    if "quads" in bpy.data.materials :
        bpy.data.materials["quads"].name="quads.001"
        bpy.data.materials["Tris"].name="Tris.001"
    try:
        with bpy.data.libraries.load(filepath[0]+"lib.blend") as (data_from, data_to):
            data_to.materials = ["quads","Tris"]
    except:
        with bpy.data.libraries.load(filepath[1]+"lib.blend") as (data_from, data_to):
            data_to.materials = ["quads","Tris"]

    mat_slots = context.active_object.data.materials #recupere la liste des mat de l'objet

    bpy.ops.object.mode_set(mode = 'OBJECT')

    #affecter un fake user aux mat et les delinker de l'objet
    for mat_slot in mat_slots :
        if mat_slot:
            mat_slot.use_fake_user = True 
        bpy.ops.object.material_slot_remove()

    qtree = bpy.data.materials['quads'].node_tree 
    qnodes = qtree.nodes
     
    ttree = bpy.data.materials['Tris'].node_tree
    tnodes = ttree.nodes
 

    qnodes.remove(qnodes["Diffuse BSDF"])

    qnodes.remove(qnodes["Diffuse BSDF.001"])

    tnodes.remove(tnodes["Diffuse BSDF"])

    tnodes.remove(tnodes["Diffuse BSDF.001"])

    

    newnode = qnodes.new(wc.type_shad_face)
    qtree.links.new(newnode.outputs[0], qnodes["Mix Shader"].inputs[1])
    newnode.inputs["Color"].default_value = wc.col_face

    newnode = qnodes.new(wc.type_shad_wire)
    qtree.links.new(newnode.outputs[0], qnodes["Mix Shader"].inputs[2])
    newnode.inputs["Color"].default_value = wc.col_wire
    newnode.location = 0,-160


    newnode = tnodes.new(wc.type_shad_face)
    ttree.links.new(newnode.outputs[0], tnodes["Mix Shader"].inputs[1])
    newnode.inputs["Color"].default_value = wc.col_face

    newnode = tnodes.new(wc.type_shad_wire)
    ttree.links.new(newnode.outputs[0], tnodes["Mix Shader"].inputs[2])
    newnode.inputs["Color"].default_value = wc.col_wire
    newnode.location = 0,-160

    #linker les mat importees a l'objet
    mat_slots.append(bpy.data.materials["quads"])
    mat_slots.append(bpy.data.materials["Tris"])
    #passe en edit mode  
    bpy.ops.object.mode_set(mode = 'EDIT')
    #reset de l'UVlayer
    bpy.ops.uv.reset()
    #recuperation de la liste des vertex select.
    old_select_mode = list(context.tool_settings.mesh_select_mode)
    #mode select face
    context.tool_settings.mesh_select_mode = [False, False, True]
    #selection des tris
    bpy.ops.mesh.select_by_number_vertices(type='TRIANGLES')
    #selection de la mat tris
    context.active_object.active_material_index=1
    #assigner la mat
    bpy.ops.object.material_slot_assign()
    #selectionner l'acienne selection
    context.tool_settings.mesh_select_mode = old_select_mode
    #selection de la mat quad (pour l'estetique XD)
    context.active_object.active_material_index=0
    #passer en mode objet (a remplacer par retour au mode de depart XD)
    bpy.ops.object.mode_set(mode = 'OBJECT')
    
    
#class de la fonction
class wire_cycles(bpy.types.Operator):
    bl_idname = "object.wire_cycles"
    bl_label = "WireForCycles"
    bl_description = "Wire shader for Cycles"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    #autorise la fonction si l'objet est un mesh et que Cycles est le renderer
    def poll(cls, context):
        ob = context.active_object
        return(ob and ob.type == 'MESH' and context.scene.render.engine == 'CYCLES')

    def draw(self, context):
        wc = bpy.context.window_manager.wireconfig 
        layout = self.layout
        layout.prop(wc, "col_face", text="Face color ")
        layout.prop(wc, "type_shad_face")
        layout.prop(wc, "col_wire", text="Wire color ")
        layout.prop(wc, "type_shad_wire")

    #execute la fonction principal
    def execute(self, context):
        wire(context)
        return{'FINISHED'}
    
#class du bouton d'appel de la fonction
class VIEW3D_PT_tools_wirecycles(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = "Wire shader Cycles"

    @classmethod
    #autorise l'affichage si l'objet est un mesh et que Cycles est le renderer
    def poll(cls, context):
        ob = context.active_object
        return(ob and ob.type == 'MESH' and context.scene.render.engine == 'CYCLES')

    #affichage du bouton
    def draw(self, context):
        wc = bpy.context.window_manager.wireconfig 
        layout = self.layout
        
        layout.operator("object.wire_cycles", text="Set wire shader")
        layout.prop(wc, "col_face", text="Face color ")
        layout.prop(wc, "type_shad_face")
        layout.prop(wc, "col_wire", text="Wire color ")
        layout.prop(wc, "type_shad_wire")

class wireconfigProps(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.wireconfig
    """
    col_face = bpy.props.FloatVectorProperty(default=(1.0, 0.9, 0.8,1.0),\
        min=0.0, max=1.0, step=1, subtype='COLOR', size=4)
 
    col_wire = bpy.props.FloatVectorProperty(default=(1.0, 0.0, 0.0,1.0),\
        min=0.0, max=1.0, step=1, subtype='COLOR', size=4)

    shaders= [("BSDF_DIFFUSE", "Diffuse", "01"),\
        ("BSDF_TRANSPARENT", "Transparent", "02"),\
        ("BSDF_GLOSSY", "Glossy", "03"),\
        ("BSDF_GLASS", "Glass", "04"),\
        ("EMISSION", "Emission", "05")]
    type_shad_face = bpy.props.EnumProperty(items=shaders,name="Face shader")
    type_shad_wire = bpy.props.EnumProperty(items=shaders,name="Wire shader")


def register():
    bpy.utils.register_class(wire_cycles)
    bpy.utils.register_class(VIEW3D_PT_tools_wirecycles)
    bpy.utils.register_class(wireconfigProps)
    bpy.types.WindowManager.wireconfig = bpy.props.PointerProperty(\
        type = wireconfigProps)

def unregister():
    bpy.utils.unregister_class(wire_cycles)
    bpy.utils.unregister_class(VIEW3D_PT_tools_wirecycles)
    bpy.utils.unregister_class(wireconfigProps)
    try:
        del bpy.types.WindowManager.wireconfig
    except:
        pass
    

if __name__ == "__main__":
    register()
