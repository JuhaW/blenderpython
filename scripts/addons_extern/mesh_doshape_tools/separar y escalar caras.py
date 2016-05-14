
import bpy
import bmesh
import mathutils
import math


def separarcaras():

    obj = bpy.context.object
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    ### separar caras###
    listabordes = []

    for borde in bm.edges:
        listabordes.append(borde)

    bmesh.ops.split_edges(bm, edges=listabordes)

    bpy.ops.mesh.select_all(action='SELECT')

    bmesh.update_edit_mesh(me, True)


def escalarcaras():

    obj = bpy.context.object
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    bpy.ops.mesh.select_all(action='DESELECT')

    for cara in bm.faces:
        cara.select = True
        bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        cara.select = False

    bmesh.update_edit_mesh(me, True)


separarcaras()

escalarcaras()
