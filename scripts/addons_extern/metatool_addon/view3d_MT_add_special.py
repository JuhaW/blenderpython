import bpy
from bpy import*


######################################################################################################################################################
#######-------------#################
#######  Operators  #################
#######-------------#################
######################################################################################################################################################

# -------------------------------------------------------
# -------------------------------------------------------

###Mr. Stan_Pancake
class ThroughSelected(bpy.types.Operator):
    """cycle through selected objects"""
    bl_idname = "object.throughselected"
    bl_label = "Cycle through Selected"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        selection = bpy.context.selected_objects

        if not bpy.context.active_object.select:
            if len(selection):
                bpy.context.scene.objects.active = selection[0]
        else:
            for i, o in enumerate(selection):
                if o == bpy.context.active_object:
                    bpy.context.scene.objects.active = selection[(i + 1) % len(selection)]
                    break

        return {'FINISHED'}


# -------------------------------------------------------
# -------------------------------------------------------

# wazou
class Wire_All(bpy.types.Operator):
    """wire all objects"""
    bl_idname = "object.wire_all"
    bl_label = "Wire on All Objects"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        for obj in bpy.data.objects:
            if obj.show_wire:
                obj.show_all_edges = False
                obj.show_wire = False
            else:
                obj.show_all_edges = True
                obj.show_wire = True

        return {'FINISHED'}


# -------------------------------------------------------
# -------------------------------------------------------

# vismaya
class Freeze_Selected(bpy.types.Operator):
    """freeze selection"""
    bl_idname = "view3d.freeze_selected"
    bl_label = "Freeze Selected"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj in bpy.context.selected_objects:

            bpy.context.scene.objects.active = obj

            bpy.context.object.hide_select = True

        return{'FINISHED'}


class UnFreeze_Selected(bpy.types.Operator):
    """unfreeze selection"""
    bl_idname = "view3d.unfreeze_selected"
    bl_label = "UnFreeze Selected"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj in bpy.context.selected_objects:

            bpy.context.object.hide_select = False
            bpy.context.scene.objects.active = obj

        return{'FINISHED'}


# -------------------------------------------------------
# -------------------------------------------------------

###http://oscurart.blogspot.com.ar/2013/12/blender-script-generador-id-color-mask.html###
class idgenerator(bpy.types.Operator):
    """add a id colorramp node to node editor"""
    bl_idname = "node.idgenerator"
    bl_label = "ID Color Node Generator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.assign_material()
        bpy.context.object.active_material.use_nodes = True

        ACTOBJ = bpy.context.active_object
        ACTMAT = ACTOBJ.material_slots[bpy.context.object.active_material_index].material
        NODE = ACTMAT.node_tree.nodes.new(type='ShaderNodeValToRGB')

        COLORS = 30
        CHUNK = 1 / COLORS
        I = 0

        for ELEMENT in range(COLORS):
            NODE.color_ramp.interpolation = "CONSTANT"
            ELEMENTO = NODE.color_ramp.elements.new(I)
            ELEMENTO.color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 1)
            I += CHUNK
        return {'FINISHED'}


import os
import shutil


class imagesave(bpy.types.Operator):
    """Create a folder in the .blend folder... and copy all pictures into. Is usefull for backups."""
    bl_idname = "image.imagesave"
    bl_label = "Collect Images"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        folder = os.path.dirname(bpy.data.filepath) + os.path.sep
        textfolder = folder + "TEXTURES" + os.path.basename(bpy.data.filepath).rpartition(".")[0]
        if not os.path.exists(textfolder):
            os.mkdir(textfolder)
            for image in bpy.data.images:
                if image.source == "FILE":
                    image.filepath.replace("//", folder), image.name
                    fl = shutil.copy(image.filepath.replace("//", folder), textfolder)
                    image.filepath = fl

        return {'FINISHED'}


# Offset Edge > Check your Unit Scale  #######-------------------------------------------------------
# Offset Edge > Check your Unit Scale  #######-------------------------------------------------------

class offsetone(bpy.types.Operator):
    """outside edges offset with extrude"""
    bl_idname = "edge.offsetone"
    bl_label = "Offset Edges Outside"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.offset_edges(width=1, geometry_mode='extrude', follow_face=False, mirror_modifier=False)

        return {'FINISHED'}


class offsettwo(bpy.types.Operator):
    """outside edges offset with extrude"""
    bl_idname = "edge.offsettwo"
    bl_label = "Offset Edges Outside"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.offset_edges(width=2, geometry_mode='extrude', follow_face=False, mirror_modifier=False)

        return {'FINISHED'}


class offsetthree(bpy.types.Operator):
    """outside edges offset with extrude"""
    bl_idname = "edge.offsetthree"
    bl_label = "Offset Edges Outside"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.offset_edges(width=4, geometry_mode='extrude', follow_face=False, mirror_modifier=False)

        return {'FINISHED'}


class offsetfour(bpy.types.Operator):
    """outside edges offset with extrude"""
    bl_idname = "edge.offsetfour"
    bl_label = "Offset Edges Outside"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.offset_edges(width=6, geometry_mode='extrude', follow_face=False, mirror_modifier=False)

        return {'FINISHED'}


class offsetfive(bpy.types.Operator):
    """outside edges offset with extrude"""
    bl_idname = "edge.offsetfive"
    bl_label = "Offset Edges Outside"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.offset_edges(width=8, geometry_mode='extrude', follow_face=False, mirror_modifier=False)

        return {'FINISHED'}


class offsetsix(bpy.types.Operator):
    """outside edges offset with extrude"""
    bl_idname = "edge.offsetsix"
    bl_label = "Offset Edges Outside"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.offset_edges(width=10, geometry_mode='extrude', follow_face=False, flip=False, mirror_modifier=False)

        return {'FINISHED'}


class offsetseven(bpy.types.Operator):
    """inside edges offset with extrude"""
    bl_idname = "edge.offsetseven"
    bl_label = "Offset Edges Inside"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.offset_edges(width=1, geometry_mode='extrude', follow_face=False, flip=True, mirror_modifier=False)

        return {'FINISHED'}


class offseteight(bpy.types.Operator):
    """inside edges offset with extrude"""
    bl_idname = "edge.offseteight"
    bl_label = "Offset Edges Inside"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.offset_edges(width=2, geometry_mode='extrude', follow_face=False, flip=True, mirror_modifier=False)

        return {'FINISHED'}


class offsetnine(bpy.types.Operator):
    """inside edges offset with extrude"""
    bl_idname = "edge.offsetnine"
    bl_label = "Offset Edges Inside"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.offset_edges(width=4, geometry_mode='extrude', follow_face=False, flip=True, mirror_modifier=False)

        return {'FINISHED'}


class offsetten(bpy.types.Operator):
    """inside edges offset with extrude"""
    bl_idname = "edge.offsetten"
    bl_label = "Offset Edges Inside"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.offset_edges(width=6, geometry_mode='extrude', follow_face=False, flip=True, mirror_modifier=False)

        return {'FINISHED'}


class offseteleven(bpy.types.Operator):
    """inside edges offset with extrude"""
    bl_idname = "edge.offseteleven"
    bl_label = "Offset Edges Inside"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.offset_edges(width=8, geometry_mode='extrude', follow_face=False, flip=True, mirror_modifier=False)

        return {'FINISHED'}


class offsettwelve(bpy.types.Operator):
    """inside edges offset with extrude"""
    bl_idname = "edge.offsettwelve"
    bl_label = "Offset Edges Inside"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def execute(self, context):

        bpy.ops.mesh.offset_edges(width=1, geometry_mode='extrude', follow_face=False, flip=True, mirror_modifier=False)

        return {'FINISHED'}


######################################################################################################################################################
############------------############
############  REGISTER  ############
############------------############
######################################################################################################################################################


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
