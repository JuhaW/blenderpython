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

import bpy

from .events import reviewBounceFibers

from .util import to_console

from .util import OBJECT_PREFIX
from .util import MAX_NAME_SIZE
    
############################################################################
# Operator code.
############################################################################
# Create operator to rename this object with the required preifix.   
class OBJECT_OT_rename_to_BounceFibers(bpy.types.Operator):
    bl_label = "Rename To Bounce Fibers"
    bl_idname = "op.rename_to_bounce_fibers"
    bl_description = "Click this button to rename this object with the required prefix. This will make it a Bounce Fibers object."
    
    def invoke(self, context, event):
        ob = context.object
        if ob != None:
            if ob.type == 'MESH':
                BounceFibers_name = OBJECT_PREFIX + ob.name
                if len(BounceFibers_name) > MAX_NAME_SIZE:
                    # Name too long.
                    BounceFibers_name = BounceFibers_name[:MAX_NAME_SIZE]
                ob_source = bpy.data.objects.get(BounceFibers_name)
                if ob_source != None:
                    # Hmm...already and object named like this.
                    to_console ("Already an object named like [" + BounceFibers_name + "] rename manualy.")
                else:
                    ob.name = BounceFibers_name
                ob.draw_type = 'WIRE'
                ob.hide_render = True
            else:
                to_console("Only MESH type objects can host bounce fibers.")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_rename_to_BounceFibers)
    
def unregister():
    bpy.utils.unregister_class(OBJECT_OT_rename_to_BounceFibers)


