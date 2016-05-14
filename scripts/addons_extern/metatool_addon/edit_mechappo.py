####################################
# Mechappo
#       v.1.0
#  (c)ishidourou 2013
####################################

#!BPY

import bpy
import random
from bpy.props import *
"""
#bl_info = {
#    "name": "Mechappo",
#    "author": "ishidourou",
#    "version": (1, 0),
#    "blender": (2, 65, 0),
#    "location": "View3D > Toolbar",
#    "description": "Mechappo",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": 'Mesh'}
  
#    Menu in tools region
class MechappoPanel(bpy.types.Panel):
    bl_label = "Mechappo"
    #bl_space_type = "VIEW_3D"
    #bl_region_type = "TOOLS"
 
    def draw(self, context):
        #layout = self.layout

        col = layout.column(align=True)
        row = col.row(align=True)
        row.operator("mechappo.select", text="Random Select")
        row = col.row(align=True)
        row.operator("mechappo.create", text="With Extrude")
"""
#---- main ------


def subdiv(obj, number, fromall):
    if number == 0:
        return
    mode = bpy.context.mode
    if mode != 'EDIT_MESH':
        bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_mode(type='FACE')
    if fromall == True:
        bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.subdivide(number_cuts=number)
    bpy.ops.mesh.select_mode(type='FACE')
    if mode != 'EDIT_MESH':
        bpy.ops.object.editmode_toggle()


def makemat(obj, matname, ct):
    mat = bpy.data.materials.new(matname)
    obj.data.materials.append(mat)
    #obj.data.materials[0] = mat
    bpy.context.object.active_material_index = ct
    bpy.ops.object.material_slot_assign()
    bpy.context.object.active_material.diffuse_color = (random.random(), random.random(), random.random())


def randselect(obj, ratio, fromall):
    bpy.ops.object.mode_set(mode='EDIT')
    if fromall == True:
        bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.object.mode_set(mode='OBJECT')
    ct = 0
    for i in obj.data.polygons:
        randval = random.random()
        if randval > ratio:
            i.select = False
        ct += 1
    bpy.ops.object.mode_set(mode='EDIT')


def hide():
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.hide(unselected=True)


def unhide():
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.reveal()
    bpy.ops.mesh.select_all(action='INVERT')


def extrude(size):
    bpy.ops.mesh.extrude_faces_move(MESH_OT_extrude_faces_indiv={"mirror": False}, TRANSFORM_OT_shrink_fatten={"value": size, "mirror": False, "proportional": 'DISABLED', "proportional_edit_falloff": 'SMOOTH', "proportional_size": 1, "snap": False, "snap_target": 'CLOSEST', "snap_point": (0, 0, 0), "snap_align": False, "snap_normal": (0, 0, 0), "release_confirm": False})


def selectcheck(obj):

    if obj == None:
        print('not selected object')
        return False
    if obj.type != 'MESH':
        print('not mesh type')
        return False


def get_polygon_number(obj):
    mesh = obj.data
    num = 0
    for face in mesh.polygons:
        num += 1
    return num


def valuecheck(obj, cuts, depth, ratio, sidepoly):
    if ratio == 0:
        ratio = 0.001
    polygons = get_polygon_number(obj)
    sidepoly += 1
    cuts += 1
    cuts **= 2
    value = polygons
    for i in range(depth):
        polygons = polygons * cuts
    #polygons *= sidepoly
    if polygons > 300000 / ratio:
        print('polygons=', polygons, value, 'limit=', 300000 / ratio)
        return False
    print('OK')
    print('polygons=', polygons, value, 300000 / ratio)
    return True


class ErrorDialog(bpy.types.Operator):
    bl_idname = "error.dialog"
    bl_label = "Warning:"
    bl_options = {'REGISTER'}

    my_message = StringProperty(name="message", default='Prease Input Smaller Values to Cuts or Depth.')

    def execute(self, context):
        message = self.my_message
        print(message)
        return{'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        global wmessage
        self.layout.label(wmessage)


cuts = 0
depth = 1
thickness = 0.01
ratio = 0.5
addmat = True
wmessage = 'Dummy'


class MechappoCreate(bpy.types.Operator):

    bl_idname = "mechappo.create"
    bl_label = "Mechappo Create"
    bl_options = {'REGISTER'}

    my_fromall = BoolProperty(name="from Selected All", default=False)
    my_cuts = bpy.props.IntProperty(name="Subdivide:", min=0, max=100, default=cuts)
    my_depth = bpy.props.IntProperty(name="Depth:", min=1, max=10, default=depth)
    my_thickness = bpy.props.FloatProperty(name="Thickness:", default=thickness)
    my_ratio = bpy.props.FloatProperty(name="Selected ratio:", min=0, max=1, default=ratio)
    my_addmat = BoolProperty(name="Add Material", default=addmat)

    def execute(self, context):

        fromall = self.my_fromall
        cuts = self.my_cuts
        depth = self.my_depth
        thickness = self.my_thickness
        ratio = self.my_ratio
        addmat = self.my_addmat
        global wmessage

        obj = bpy.context.active_object
        if selectcheck(obj) == False:
            wmessage = "Prease Select Mesh Object."
            bpy.ops.error.dialog('INVOKE_DEFAULT')
            return{'FINISHED'}
        if valuecheck(obj, cuts, depth, ratio, 4) == False:
            wmessage = "Prease Input Smaller Values to Cuts or Depth."
            bpy.ops.error.dialog('INVOKE_DEFAULT')
            return{'FINISHED'}

        ct = 0
        ii = 0
        for i in obj.data.materials:
            ii += 1
        print(ii)
        hide()
        for i in range(depth):
            subdiv(obj, cuts, fromall)
            randselect(obj, ratio, fromall)
            if ct == 0:
                thickness *= -1
            else:
                if random.random() < 0.5:
                    thickness *= -1
            extrude(thickness)
            if addmat == True:
                makemat(obj, 'mat', ct + ii)
            ct += 1
        unhide()

        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles(threshold=0.0001, use_unselected=False)

        return{'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class MechappoSelect(bpy.types.Operator):

    bl_idname = "mechappo.select"
    bl_label = "Mechappo Select"
    bl_options = {'REGISTER'}

    my_fromall = BoolProperty(name="from Selected All", default=False)
    my_cuts = bpy.props.IntProperty(name="Subdivide:", min=0, max=100, default=cuts)
    my_depth = bpy.props.IntProperty(name="Depth:", min=1, max=10, default=depth)
    my_ratio = bpy.props.FloatProperty(name="Selected ratio:", min=0, max=1, default=ratio)
    my_addmat = BoolProperty(name="Add Material", default=False)

    def execute(self, context):

        fromall = self.my_fromall
        cuts = self.my_cuts
        depth = self.my_depth
        ratio = self.my_ratio
        addmat = self.my_addmat
        global wmessage

        obj = bpy.context.active_object
        if selectcheck(obj) == False:
            wmessage = "Prease Select Mesh Object."
            bpy.ops.error.dialog('INVOKE_DEFAULT')
            return{'FINISHED'}
        if cuts != 0:
            if valuecheck(obj, cuts, depth, ratio, 0) == False:
                wmessage = "Prease Input Smaller Values to Cuts or Depth."
                bpy.ops.error.dialog('INVOKE_DEFAULT')
                return{'FINISHED'}

        ct = 0
        ii = 0
        for i in obj.data.materials:
            ii += 1
        for i in range(depth):
            subdiv(obj, cuts, fromall)
            randselect(obj, ratio, fromall)
            if addmat == True:
                makemat(obj, 'mat', ct + ii)
            ct += 1

        return{'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

#	Registration


def register():
    # bpy.utils.register_class(MechappoPanel)
    bpy.utils.register_class(MechappoCreate)
    bpy.utils.register_class(MechappoSelect)
    bpy.utils.register_class(ErrorDialog)


def unregister():
    # bpy.utils.unregister_class(MechappoPanel)
    bpy.utils.unregister_class(MechappoCreate)
    bpy.utils.unregister_class(MechappoSelect)
    bpy.utils.unregister_class(ErrorDialog)

if __name__ == "__main__":
    register()
