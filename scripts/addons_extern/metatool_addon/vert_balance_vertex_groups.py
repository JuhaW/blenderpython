# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# bl_info = {
#    "name": "Balance Vertex Groups",
#    "author": "Koilz",
#    "version": (1, 1),
#    "blender": (2, 70, 0),
#    "location": "Properties > Data > Vertex Groups > Edit Mode",
#    "description": "Balance the weight of two vertex groups",
#    "warning": "",
#    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Rigging/VG_Oppose",
#    "category": "Rigging"}

import bpy

bpy.types.Scene.vgai2 = bpy.props.StringProperty(name="Vertex Group Index 2", description="Second active index for vertex groups", default='')


def main(context):

    # save vertex_group
    vg_previous = context.active_object.vertex_groups.active_index

    # save weight
    vg_weight_previous = context.scene.tool_settings.vertex_group_weight

    # assign weight
    bpy.ops.object.vertex_group_assign()

    # oppose vertex group
    context.active_object.vertex_groups.active_index = context.active_object.vertex_groups[context.scene.vgai2].index

    # oppose weight
    context.scene.tool_settings.vertex_group_weight = 1 - vg_weight_previous

    # assign weight
    bpy.ops.object.vertex_group_assign()

    # restore vertex group
    context.active_object.vertex_groups.active_index = vg_previous

    # restore weight
    context.scene.tool_settings.vertex_group_weight = vg_weight_previous


class OT_BALANCE_VG(bpy.types.Operator):
    """Balance the weight of two vertex groups"""
    bl_idname = "object.vertex_group_balance"
    bl_label = "Balance"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def add_vertex_group_tools(self, context):

    layout = self.layout

    ob = context.object

    if ob.vertex_groups and ob.mode == 'EDIT':

        row = layout.row()
        row.operator("object.vertex_group_balance")
        row.prop_search(context.scene, "vgai2", context.active_object, "vertex_groups", text="")


def register():
    bpy.utils.register_class(OT_BALANCE_VG)
    bpy.types.DATA_PT_vertex_groups.append(add_vertex_group_tools)


def unregister():
    bpy.utils.unregister_class(OT_BALANCE_VG)
    bpy.types.DATA_PT_vertex_groups.remove(add_vertex_group_tools)

if __name__ == "__main__":
    register()
