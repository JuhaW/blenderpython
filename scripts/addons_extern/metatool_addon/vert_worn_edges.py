#########################################################################################################################
#########################################################################################################################
#########  Worn Edges  ##################################################################################################
#########  Worn Edges  ##################################################################################################


#bl_info = {
#    "name": "Worn Edges",
#    "author": "Oscurart",
#    "version": (1, 2),
#    "blender": (2, 6, 8),
#    "location": "Vertex Paint > Paint > Worn Edges",
#    "description": "Create a Vertex Color map with Worn Edges",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "Paint"}


import bpy
from random import random
import bmesh

def CreateWornEdges(context, factor):
    actobj = bpy.context.object

    bpy.ops.object.mode_set(mode="EDIT")
    bm = bmesh.from_edit_mesh(actobj.data)

    sf = [(vert.calc_shell_factor() - 1.0) * factor for vert in bm.verts[:]]

    bpy.ops.object.mode_set(mode="VERTEX_PAINT")
    purge = {}

    for ind, loop in enumerate(bpy.context.object.data.loops[:]):
        if loop.vertex_index not in purge:
            purge[loop.vertex_index] = [ind]
        else:
            purge[loop.vertex_index].append(ind)

    for vert in actobj.data.vertices[:]:
        if vert.select:
            ran = (sf[vert.index], sf[vert.index], sf[vert.index])
            for i in purge[vert.index]:
                actobj.data.vertex_colors.active.data[i].color = ran
    actobj.data.update()


class OscurartWorn(bpy.types.Operator):
    """create a vertex color map with worn edges"""
    bl_idname = "paint.worn_edges"
    bl_label = "Worn Edges Map"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    factor = bpy.props.FloatProperty(name="Factor", min=.001, default=1)

    def execute(self, context):
        CreateWornEdges(context, self.factor)
        return {'FINISHED'}


def add_osc_futurism_button(self, context):
    self.layout.operator(
        OscurartWorn.bl_idname,
        text="Worn Edges",
        icon="PLUGIN")


#--Registry-----------------------------------------------------------------------------


def register():
    bpy.utils.register_class(OscurartWorn)
    bpy.types.VIEW3D_MT_paint_vertex.append(add_osc_futurism_button)


def unregister():
    bpy.utils.unregister_class(OscurartWorn)
    bpy.types.VIEW3D_MT_paint_vertex.remove(add_osc_futurism_button)


if __name__ == '__main__':
    register() 

