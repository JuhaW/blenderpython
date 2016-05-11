# Repeats extrusion, rotation, scale, movement for one or more faces.
# borrowed from user liero (http://blenderartists.org/forum/showthread.php?219526-Multiple-extrusions-script)
# original source: http://dl.dropbox.com/u/16486113/Blender/mexii.py

bl_info = {
    "name": "Repeat Extrude",
    "version": (1, 0, 0),
    "blender": (2, 74, 0),
    "location": "View3D > Tool Shelf",
    "description": "Repeat extrusions from faces.",
    'warning': '',
    "category": "Mesh"}

import bpy
import bmesh
import random
import math
from math import radians
from random import gauss
from mathutils import Euler
from bpy.props import FloatProperty, BoolProperty, IntProperty

def vlocation(self, r):
    random.seed(self.seed + r)
    return random.gauss(0, self.var1 / 3)

def vrotation(self, r):
    random.seed(self.seed + r)
    return Euler((radians(self.rotx) + random.gauss(0, self.var2 / 3), \
        radians(self.roty) + random.gauss(0, self.var2 / 3), \
        radians(self.rotz) + random.gauss(0,self.var2 / 3)), 'XYZ')
        
class ScaleProperties(bpy.types.PropertyGroup):
    scale = FloatProperty(name='Scale', min=0.1, soft_min=0.5, \
        soft_max=1.2, max =2, default=.9, description='Scaling')
    factor_type = bpy.props.EnumProperty(
                                    items= (
                                            ('NONE', 'None', ''),
                                            ('LOG', 'Log', ''),
                                            ('LOGINVERSE', 'Log inverse', '')
                                        ),
                                    name = "Factor type") 
    factor = FloatProperty(name='Factor', min=0.00005, soft_min=0.00005, \
        soft_max=30, default=1, description='Factor')

    def register_layout(self, layout, text):
        column = layout.column(align=True)
        column.label(text=text + ' scale:')
        column.prop(self, 'scale', slider=True)
        row = column.row(align=False)
        row.prop(self, 'factor_type', expand=True)
        column.prop(self, 'factor', slider=True)
        
    def calculate_scale(self, repetitions, repetition, seed, scale_variance):
        random.seed(seed + repetition)
        result = self.scale * (1 + random.gauss(0, scale_variance / 3))
        
        try:
            if (self.factor_type == 'LOG'):
                log = math.log(repetition)
                
                if (log > 0):
                    result -= log * self.factor
                
            if (self.factor_type == 'LOGINVERSE'):
                log = math.log(repetitions - repetition)
                
                if (log > 0):
                    result -= log * self.factor
                
        except:
            result = self.scale
    
        return result

class OffsetProperties(bpy.types.PropertyGroup):
    offset = FloatProperty(name='Offset', min=-85, soft_min=-30, \
        soft_max=30, max=85, default=0, description='Offset')
    factor_type = bpy.props.EnumProperty(
                                    items= (
                                            ('NONE', 'None', ''),
                                            ('LOG', 'Log', ''),
                                            ('LOGINVERSE', 'Log inverse', '')
                                        ),
                                    name = "Factor type") 
    factor = FloatProperty(name='Factor', min=0.00005, soft_min=0.00005, \
        soft_max=30, default=1, description='Factor')
        
    def register_layout(self, layout, text):
        column = layout.column(align=True)
        column.label(text=text + ' offset:')
        column.prop(self, 'offset', slider=True)
        row = column.row(align=False)
        row.prop(self, 'factor_type', expand=True)
        column.prop(self, 'factor', slider=True)
        
    def calculate_offset(self, repetitions, repetition):
        result = self.offset
        
        try:
            if (self.factor_type == 'LOG'):
                log = math.log(repetition)
                
                if (log > 0):
                    result -= log * self.factor
                
            if (self.factor_type == 'LOGINVERSE'):
                log = math.log(repetitions - repetition)
                
                if (log > 0):
                    result -= log * self.factor
                
        except:
            result = self.offset
            
        return result

class RepeatExtrude(bpy.types.Operator):
    bl_idname = 'object.repeatextrude'
    bl_label = 'Repeat Extrude'
    bl_description = 'Repeat Extrude'
    bl_options = {'REGISTER', 'UNDO'}

    rotx = FloatProperty(name='Rot X', min=-85, soft_min=-30, \
        soft_max=30, max=85, default=0, description='X rotation')
    roty = FloatProperty(name='Rot Y', min=-85, soft_min=-30, \
        soft_max=30, max=85, default=0, description='Y rotation')
    rotz = FloatProperty(name='Rot Z', min=-85, soft_min=-30, \
        soft_max=30, max=85, default=-0, description='Z rotation')
        
    combined_scale_option = BoolProperty(name='Combined scale?')
    combined_scale = bpy.props.PointerProperty(type=ScaleProperties)

    x_offset = bpy.props.PointerProperty(type=OffsetProperties)
    y_offset = bpy.props.PointerProperty(type=OffsetProperties)
    z_offset = bpy.props.PointerProperty(type=OffsetProperties)
        
    x_scale = bpy.props.PointerProperty(type=ScaleProperties)
    y_scale = bpy.props.PointerProperty(type=ScaleProperties)
    z_scale = bpy.props.PointerProperty(type=ScaleProperties)
        
    var1 = FloatProperty(name='Offset Var', min=-5, soft_min=-1, \
        soft_max=1, max=5, default=0, description='Offset variation')
    var2 = FloatProperty(name='Rotation Var', min=-5, soft_min=-1, \
        soft_max=1, max=5, default=0, description='Rotation variation')
    scale_variance = FloatProperty(name='Scale Noise', min=-5, soft_min=-1, \
        soft_max=1, max=5, default=0, description='Scaling noise')
    repetitions = IntProperty(name='Repeat', min=1, max=50, soft_max=100, \
        default=5, description='Repetitions')
    seed = IntProperty(name='Seed', min=-9999, max=9999, default=0, \
        description='Seed to feed random values')

    @classmethod
    def poll(cls, context):
        obj = context.object
        return (obj and obj.type == 'MESH')

    def draw(self, context):
        layout = self.layout
        column = layout.column(align=True)
        column.label(text='Transformations:')
        column.prop(self, 'rotx', slider=True)
        column.prop(self, 'roty', slider=True)
        column.prop(self, 'rotz', slider=True)
        
        self.x_offset.register_layout(layout, 'X')
        self.y_offset.register_layout(layout, 'Y')
        self.z_offset.register_layout(layout, 'Z')
        
        layout.prop(self, 'combined_scale_option')
        
        if (self.combined_scale_option):
            self.combined_scale.register_layout(layout, 'Combined')
        else:
            self.x_scale.register_layout(layout, 'X')
            self.y_scale.register_layout(layout, 'Y')
            self.z_scale.register_layout(layout, 'Z')
        
        column = layout.column(align=True)
        column.label(text='Variation settings:')
        column.prop(self, 'var1', slider=True)
        column.prop(self, 'var2', slider=True)
        column.prop(self, 'scale_variance', slider=True)
        column.prop(self, 'seed')
        column = layout.column(align=False)
        column.prop(self, 'repetitions')

    def execute(self, context):
        obj = bpy.context.object
        mode = obj.mode
        mw = obj.matrix_world
        bpy.context.tool_settings.mesh_select_mode = [False, False, True]

        # bmesh operations
        bpy.ops.object.mode_set()
        bm = bmesh.new()
        bm.from_mesh(obj.data)
        selectedFaces = [f for f in bm.faces if f.select]

        # faces loop
        for i, selectedFace in enumerate(selectedFaces):
            rotation = vrotation(self, i)
            location = vlocation(self, i)
            selectedFace.normal_update()

            # extrusion loop
            for repetition in range(self.repetitions):
                newFace = selectedFace.copy()
                newFace.normal_update()
                newFaceNormal = newFace.normal.copy()
                newFaceCenterBounds = newFace.calc_center_bounds()
                
                if (self.combined_scale_option):
                    xscale = self.combined_scale.calculate_scale(self.repetitions, repetition, self.seed, self.scale_variance)
                    yscale = xscale
                    zscale = xscale
                else:
                    xscale = self.x_scale.calculate_scale(self.repetitions, repetition, self.seed, self.scale_variance)
                    yscale = self.y_scale.calculate_scale(self.repetitions, repetition, self.seed, self.scale_variance)
                    zscale = self.z_scale.calculate_scale(self.repetitions, repetition, self.seed, self.scale_variance)

                for v in newFace.verts:
                    v.co.rotate(rotation)
                    v.co += newFaceNormal * location
                    v.co = v.co.lerp(newFaceCenterBounds, 0)
                    
                    v.co.x += self.x_offset.calculate_offset(self.repetitions, repetition)
                    v.co.y += self.y_offset.calculate_offset(self.repetitions, repetition)
                    v.co.z += self.z_offset.calculate_offset(self.repetitions, repetition)

                bmesh.ops.scale(
                            bm,
                            vec=(xscale, yscale, zscale),
                            verts=newFace.verts
                            )

                # extrude code from TrumanBlending
                for a, b in zip(selectedFace.loops, newFace.loops):
                    sf = bm.faces.new((a.vert, a.link_loop_next.vert, \
                        b.link_loop_next.vert, b.vert))
                    sf.normal_update()

                bm.faces.remove(selectedFace)
                newFace.select_set(True)
                selectedFace = newFace

        for v in bm.verts: v.select = False
        for e in bm.edges: e.select = False
        bm.to_mesh(obj.data)
        obj.data.update()

        # restore user settings
        bpy.ops.object.mode_set(mode=mode)

        if not len(selectedFaces):
            self.report({'INFO'}, 'Please select one or more faces.')
        return{'FINISHED'}

class RepeatExtrudeToolButton(bpy.types.Panel):
    bl_label = 'Repeat Extrude'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout
        layout.operator('object.repeatextrude')

def register():
    bpy.utils.register_class(ScaleProperties)
    bpy.utils.register_class(OffsetProperties)
    bpy.utils.register_class(RepeatExtrude)
    bpy.utils.register_class(RepeatExtrudeToolButton)
    
def unregister():
    bpy.utils.unregister_class(RepeatExtrudeToolButton)
    bpy.utils.unregister_class(RepeatExtrude)
    bpy.utils.register_class(OffsetProperties)
    bpy.utils.register_class(ScaleProperties)

if __name__ == '__main__':
    register()
