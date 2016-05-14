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

# bl_info = {
#    "name": "Snippet Wazou_Menus",
#    "author": "Cédric Lepiller & DavideDozza & Lapineige & Leafar & 0rAngE",
#    "version": (0, 1, 6),
#    "blender": (2, 71, 4),
#    "description": "only Operator",
#    "category": "User Changed",}

import bpy
from bpy.types import Menu
from bpy.props import IntProperty, FloatProperty, BoolProperty
import bmesh
from mathutils import *
import math


######################
#   Cursor/Origin    #
######################

# Pivot to Bottom
class PivotBottom(bpy.types.Operator):
    bl_idname = "object.pivotobottom"
    bl_label = "Pivot To Bottom"

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        o = bpy.context.active_object
        init = 0
        for x in o.data.vertices:
            if init == 0:
                a = x.co.z
                init = 1
            elif x.co.z < a:
                a = x.co.z

        for x in o.data.vertices:
            x.co.z -= a

        o.location.z += a
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}


#####################
#   Simple Align    #
#####################
# Align X
class AlignX(bpy.types.Operator):
    bl_idname = "align.x"
    bl_label = "Align  X"

    def execute(self, context):

        for vert in bpy.context.object.data.vertices:
            bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}

# Align Y


class AlignY(bpy.types.Operator):
    bl_idname = "align.y"
    bl_label = "Align  Y"

    def execute(self, context):

        for vert in bpy.context.object.data.vertices:
            bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}

# Align Z


class AlignZ(bpy.types.Operator):
    bl_idname = "align.z"
    bl_label = "Align  Z"

    def execute(self, context):

        for vert in bpy.context.object.data.vertices:
            bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}

#####################
#    Align To 0     #
#####################

# Align to X - 0


class AlignToX0(bpy.types.Operator):
    bl_idname = "align.2x0"
    bl_label = "Align To X-0"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[0] = 0
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

# Align to Z - 0


class AlignToY0(bpy.types.Operator):
    bl_idname = "align.2y0"
    bl_label = "Align To Y-0"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[1] = 0
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

# Align to Z - 0


class AlignToZ0(bpy.types.Operator):
    bl_idname = "align.2z0"
    bl_label = "Align To Z-0"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[2] = 0
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

# Align X Left


class AlignXLeft(bpy.types.Operator):
    bl_idname = "alignx.left"
    bl_label = "Align X Left"

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 0
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] < max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

# Align X Right


class AlignXRight(bpy.types.Operator):
    bl_idname = "alignx.right"
    bl_label = "Align X Right"

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 0
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] > max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

# Align Y Back


class AlignYBack(bpy.types.Operator):
    bl_idname = "aligny.back"
    bl_label = "Align Y back"

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 1
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] > max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

# Align Y Front


class AlignYFront(bpy.types.Operator):
    bl_idname = "aligny.front"
    bl_label = "Align Y Front"

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 1
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] < max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}
# Align Z Top


class AlignZTop(bpy.types.Operator):
    bl_idname = "alignz.top"
    bl_label = "Align Z Top"

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 2
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] > max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

# Align Z Bottom


class AlignZBottom(bpy.types.Operator):
    bl_idname = "alignz.bottom"
    bl_label = "Align Z Bottom"

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 2
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] < max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

# Align X, Y, Z


class AlignXYZ(bpy.types.Menu):
    bl_idname = "align.xyz"
    bl_label = "Align Direction"

    def draw(self, context):
        layout = self.layout

        layout.operator("alignx.left", text="Align X Left", icon='TRIA_LEFT')
        layout.operator("alignx.right", text="Align X Right", icon='TRIA_RIGHT')
        layout.operator("aligny.front", text="Align Y Front", icon='PLUS')
        layout.operator("aligny.back", text="Align Y Back", icon='DISCLOSURE_TRI_DOWN')
        layout.operator("alignz.top", text="Align Z Top", icon='TRIA_UP')
        layout.operator("alignz.bottom", text="Align Z Bottom", icon='TRIA_DOWN')


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
