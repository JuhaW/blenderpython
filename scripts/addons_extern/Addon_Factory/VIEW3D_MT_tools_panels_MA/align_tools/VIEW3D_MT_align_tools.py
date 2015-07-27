# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Align Tools",
    "author": "Multiple Authors",
    "version": (0, 3, 0),
    "blender": (2, 74, 5),
    "location": "View3D > Toolshelf",
    "description": "Add Align Options",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
}

if "bpy" in locals():
    import importlib
    importlib.reload(simple_align)
    importlib.reload(object_align)
    importlib.reload(align_to_active_object)
    importlib.reload(advanced_align_tools)



else:
    from . import simple_align
    from . import object_align
    from . import align_to_active_object
    from . import advanced_align_tools


import bpy
from bpy.props import EnumProperty, PointerProperty, FloatProperty, BoolProperty
from mathutils import Vector
from math import *


class AlignUi(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = "Align Tools"
    bl_context = "objectmode"
    bl_category = 'Tools'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        obj = context.object

        if obj != None:
            row = layout.row()
            row.label(text="Active object is: ", icon='OBJECT_DATA')
            row = layout.row()
            row.label(obj.name, icon='EDITMODE_HLT')

        layout.separator()

        col = layout.column()
        col.label(text="Align Loc + Rot:", icon='MANIPUL')


        col = layout.column(align=False)
        col.operator("object.align",text="XYZ")

        col = layout.column()
        col.label(text="Align Location:", icon='MAN_TRANS')

        col = layout.column_flow(columns=5,align=True)
        col.operator("object.align_location_x",text="X")
        col.operator("object.align_location_y",text="Y")
        col.operator("object.align_location_z",text="Z")
        col.operator("object.align_location_all",text="All")

        col = layout.column()
        col.label(text="Align Rotation:", icon='MAN_ROT')

        col = layout.column_flow(columns=5,align=True)
        col.operator("object.align_rotation_x",text="X")
        col.operator("object.align_rotation_y",text="Y")
        col.operator("object.align_rotation_z",text="Z")
        col.operator("object.align_rotation_all",text="All")

        col = layout.column()
        col.label(text="Align Scale:", icon='MAN_SCALE')

        col = layout.column_flow(columns=5,align=True)
        col.operator("object.align_objects_scale_x",text="X")
        col.operator("object.align_objects_scale_y",text="Y")
        col.operator("object.align_objects_scale_z",text="Z")
        col.operator("object.align_objects_scale_all",text="All")
        col = layout.column()
        col.label(text="Advanced Align")
        layout = self.layout
        self.layout.operator("object.align_tools", text="Advanced")



# Register all operators and panels


def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.my_custom_props = PointerProperty(type = oa_p_group0)



def unregister():

    del bpy.context.scene['my_custom_props']
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()