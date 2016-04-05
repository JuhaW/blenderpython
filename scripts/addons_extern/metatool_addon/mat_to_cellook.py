#
#The MIT License (MIT)
#
#Copyright (c) 2014 ishidourou
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.


######################################
#    Mat to Cellook (English/Japanese)
#      v.0.5
# (c)ishidourou 2014
#####################################

import bpy
from bpy.props import *

#bl_info = {
#    "name": "Set Cellook Material",
#    "author": "ishidourou",
#    "version": (0, 50),
#    "blender": (2, 70, 0),
#    "location": "View3D > Toolbar and View3D",
#    "description": "Set Cellook Mat",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": 'Material'}

#    メッセージ（英語,日本語）
class mes():
    title = ('Set Cellook Material','セルルックにセット')
    btn01 = ('Set','セット')
    lampname = ('Cellook Lamp','セルルック専用ライト')
    matname = ('material','マテリアル')

def lang():
    system = bpy.context.user_preferences.system
    if system.use_international_fonts:
        if system.language == 'ja_JP':
            return 1
    return 0

def objselect(objct,selection):
    bpy.ops.object.mode_set(mode = 'OBJECT')
    if (selection == 'ONLY'):
        bpy.ops.object.select_all(action='DESELECT')
    bpy.context.scene.objects.active = objct
    objct.select = True

def existcheck(checkname,type):
    cobjs = bpy.context.scene.objects
    for i in cobjs:
        if i.name == checkname:
            if i.type == type:
                return True
    return False

def set_new_material():
    mat = bpy.data.materials.new(mes.matname[lang()])

    cmode = bpy.context.object.mode
    bpy.ops.object.mode_set(mode='OBJECT')
    obj = bpy.context.scene.objects.active
    for i in obj.material_slots:
        if i.name == '':
            bpy.ops.object.material_slot_remove()
    obj.data.materials.append(mat)
    bpy.ops.object.mode_set(mode=cmode)

def matcheck():
    nm = bpy.context.object.active_material
    if not(nm):
        set_new_material()
    return 1

def cellooklampset(name):
    if existcheck(name,'LAMP'):
        return bpy.data.objects[name]
    bpy.context.area.type = 'VIEW_3D'
    bpy.ops.object.lamp_add(type='POINT',location=(4, -8, 3))
    obj = bpy.context.active_object
    obj.name = name
    obj.data.name = name
    bpy.context.area.type = 'PROPERTIES'
    return obj
        
def mat_cellook(cobj,lampobj):
    objselect(cobj,'ONLY')        
    bpy.context.area.type = 'NODE_EDITOR'

    cmat = bpy.context.object.active_material
    #print(cmat.type)

    color = [[0.0,0.0,0.0,1],[0.0,0.0,0.0,1],[0.0,0.0,0.0,1]]
    for i in range(3):
        color[1][i] = cmat.diffuse_color[i]
    for i in range(3):
        ccolor = color[1][i] / 3
        if ccolor < 0.0:
            ccolor = 0.0
        color[0][i] = ccolor
    for i in range(3):
        ccolor = color[1][i] + 0.3
        if ccolor > 1.0:
            ccolor = 1.0
        color[2][i] = ccolor
 
    cmat.use_nodes = True
    bpy.context.space_data.tree_type = 'ShaderNodeTree'
    tree = cmat.node_tree
    nodes = tree.nodes
    links = tree.links

# clear default nodes
    for n in nodes:
        nodes.remove(n)

    geo = nodes.new('ShaderNodeGeometry')
    geo.name = 'Geometry_0'   
    geo.location = 0,0

    lmp = nodes.new('ShaderNodeLampData')
    lmp.name = 'Lampdata_0'   
    lmp.lamp_object = lampobj
    lmp.location = 0,200

    vecm = nodes.new('ShaderNodeVectorMath')
    vecm.name = 'VectorMath_0'
    vecm.operation = 'DOT_PRODUCT'   
    vecm.location = 200,100

    ccramp = nodes.new('ShaderNodeValToRGB')
    ccramp.name = 'Lampconv_0'   
    ccramp.location = 400,100
    cramp = ccramp.color_ramp
    cramp.elements[0].position = 0.232
    cramp.elements[1].position = 0.233
    cramp.elements.new(0.765)
    cramp.elements.new(0.766)
   
    cramp.elements[0].color = color[0]
    cramp.elements[1].color = color[1]
    cramp.elements[2].color = color[1]
    cramp.elements[3].color = color[2]
    
    nout = nodes.new('ShaderNodeOutput')
    nout.name = 'Output_0'   
    nout.location = 800,100

    links.new(lmp.outputs[1],vecm.inputs[0])
    links.new(geo.outputs[5],vecm.inputs[1])
    links.new(vecm.outputs[1],ccramp.inputs[0])
    links.new(ccramp.outputs[0],nout.inputs[0])

    bpy.context.area.type = 'PROPERTIES'


#class MatCellookPanel(bpy.types.Panel):
#    bl_label = mes.title[lang()]
#    bl_space_type = "PROPERTIES"
#    bl_region_type = "WINDOW"
#    bl_context = "material"
# 
#    def draw(self , context):
#        layout = self.layout
#        layout.operator("mat.cellook")
        
#    main
class MatCellook(bpy.types.Operator):
    bl_idname = "mat.cellook"
    bl_label = mes.btn01[lang()]
 
    def execute(self, context):
        cobj = bpy.context.object
        matcheck()

        lampo = cellooklampset(mes.lampname[lang()])
        mat_cellook(cobj,lampo)
        bpy.context.area.type = 'VIEW_3D'

        return{'FINISHED'}
            
#	Registration

def register():
    #bpy.utils.register_class(MatCellookPanel)
    bpy.utils.register_class(MatCellook)

def unregister():
    #bpy.utils.unregister_class(MatCellookPanel)
    bpy.utils.unregister_class(MatCellook)

if __name__ == "__main__":
    register()
