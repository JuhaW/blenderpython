'''
BEGIN GPL LICENSE BLOCK

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

END GPL LICENCE BLOCK
'''

bl_info = {
    "name": "Boxpleating",
    "author": "Diego Quevedo ( http://doshape.com/ )",
    "version": (1, 0),
    "blender": (2, 7, 3),
    "location": "View3D > EditMode > ToolShelf",
    "description": "allow bisect in specific degree",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Mesh"}


import bpy
import bmesh
import mathutils
import math
import sys


class BoxpleatingOperator(bpy.types.Operator):
    "rota y junta las caras seleccionadas"
    bl_idname = 'mesh.boxpleating'
    bl_label = 'Boxpleating'
    bl_description = "rota y junta las caras seleccionadas"
    bl_options = {'REGISTER', 'UNDO'}

    angle = bpy.props.FloatProperty(
        name="angle",
        default=0.0,
        description="Angulo Rotacion",
        min=-sys.float_info.max,
        max=sys.float_info.max,
        precision=2,
        subtype="ANGLE",
        unit="ROTATION"
    )

    chboxaxisx = bpy.props.BoolProperty(
        name="Axis X",
        default=True
    )
    chboxaxisy = bpy.props.BoolProperty(
        name="Axis Y",
        default=False
    )

    chboxaxisz = bpy.props.BoolProperty(
        name="Axis z",
        default=False
    )

    def main(self, context, chboxaxisx, chboxaxisy, chboxaxisz, angle):

        angulo = angle

        RX_b = False
        RY_b = False
        RZ_b = False

        try:

            if chboxaxisx:
                RX = 1
                RX_b = True

            else:
                RX = 0

            if chboxaxisy:
                RY = 1
                RY_b = True

            else:
                RY = 0

            if chboxaxisz:
                RZ = 1
                RZ_b = True

            else:
                RZ = 0

            obj = bpy.context.object
            me = obj.data
            bm = bmesh.from_edit_mesh(me)

            faces = [c for c in bm.faces if (c.select and not c.hide)]

            caras = []

            for cara in faces:
                caras.append(cara)
                cara.select = False

            bpy.ops.mesh.select_all(action='DESELECT')

            for cara in caras:
                cara.select = True
                bm.faces.active = cara
                bpy.ops.transform.rotate(value=angulo, axis=(RX, RY, RZ), constraint_axis=(RX_b, RY_b, RZ_b), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
                cara.select = False

            for cara in caras:
                cara.select = True
                if len(cara.verts) == 3:
                    bm.faces.active = cara  # especifico a esta cara como la cara activa

            bmesh.update_edit_mesh(me, True)

        except:
            print("parametros no validos")

    @classmethod
    def poll(self, context):
        obj = context.active_object
        return all([obj is not None, obj.type == 'MESH', obj.mode == 'EDIT'])

    def execute(self, context):

        self.main(context, self.chboxaxisx, self.chboxaxisy, self.chboxaxisz, self.angle)
        return {'FINISHED'}


class BoxpleatingOperatorPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_label = "BoxPleating"

    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')

    def draw(self, context):

        layout = self.layout
        row = layout.row(align=True)
        row.operator(BoxpleatingOperator.bl_idname)


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
