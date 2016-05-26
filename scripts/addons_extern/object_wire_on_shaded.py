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

# <pep8-80 compliant>

# Copyright (C) 2013-2014: Tomas Dostal (stanley82), tomas.dostal.cz@gmail.com

bl_info = {
    "name": "Wireframe On Shaded Switch",
    "description": "Toggle wireframe on shaded display method for all object in scene",
    "author": "Tomas Dostal (stanley82)",
    "version": (0, 1),
    "blender": (2, 7, 0),
    "location": "View3D > Object",
    "warning": "WIP - not final version!",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Object"}

import bpy


def toggleWire():
    s = bpy.context.scene
    for object in s.objects:
        if object.type == 'MESH':
            if not object.show_wire or not object.show_all_edges:
                object.show_wire = True
                object.show_all_edges = True
                print(object.name)
            else:
                object.show_wire = False
                object.show_all_edges = False
                print(object.name)


class ToggleWire (bpy.types.Operator):
    """Toggle wire on all meshes"""
    bl_label = "Toggle wire"
    bl_idname = "object.toggle_wire"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print('Toggling Wire...')
        toggleWire()
        return {'FINISHED'}


def draw_ui(self, context):
    self.layout.operator(ToggleWire.bl_idname, text="Toggle wire")


def register():
    bpy.utils.register_class(ToggleWire)
    bpy.types.VIEW3D_MT_object.append(draw_ui)


def unregister():
    bpy.utils.unregister_class(ToggleWire)
    bpy.types.VIEW3D_MT_object.remove(draw_ui)

if __name__ == "__name__":
    register()
