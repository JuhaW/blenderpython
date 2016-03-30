# AddOn Bounce Fibers
# Bounce Fibers 1.0.
# Bounces a point around inside a mesh to create a curve or set of curves.
# Last Revision 04-07-2014
# Bounce code by Liero.
# AddOn functionality by Atom.

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

bl_info = {
    "name": "Bounce Fibers",
    "author": "Liero, Atom",
    "version": (1,1),
    "blender": (2, 7, 6),
    "location": "View3D > Add > Curve > Bounce Fibers",
    "description": "Creates a set of curves in the shape of mesh.",
    "warning": "This is a parametric object.",
    "wiki_url":"",
    "tracker_url": "",
    "category": "Add Curve"}

modules = ("util", "properties", "operators", "events", "ui")
if "bpy" in locals():
    import imp
    for mod in modules:
        exec("imp.reload(%s)" % mod)
else:
    for mod in modules:
        exec("from . import %s" % mod)

import bpy

def register():
	properties.register()
	operators.register()
	ui.register()

def unregister():
	properties.unregister()
	operators.unregister()
	ui.unregister()
