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
from bpy.props import FloatProperty, EnumProperty, IntProperty, BoolProperty, FloatVectorProperty

from .events import reviewBounceFibers

############################################################################
# Parameter Definitiions That Can Be Animated And Appear In Panels
############################################################################


def property_update(self, context):
    # Any parameter change gets routed to the update of the managed curve set.
    reviewBounceFibers(self, context)


class cls_BounceFibers(bpy.types.PropertyGroup):
    bounce_count = IntProperty(
        name="Number Bounces",
        description="How many curve points each fiber will have.",
        min=3, max=4800, default=960, update=property_update)

    sub_steps = IntProperty(
        name="Sub Steps",
        description="Number of sub rays to generate if a collision is not found. Set greater than 0 to activate.",
        min=0, max=256, default=0, update=property_update)

    rnd_noise = FloatProperty(
        name="Random Noise",
        description="The amount of random noise to add to a vector upon each bounce collision.",
        min=0.0, max=10.0,
        default=0.25, update=property_update)

    smoothness = IntProperty(
        name="Smoothness",
        description="Number divisions to use when displaying or rendering the curve.",
        min=1, max=128, default=12, update=property_update)

    thickness = FloatProperty(
        name="Thickness",
        description="How thick to make the fiber when no bevel shape is present.",
        min=0.0, max=1.0,
        default=0.01, update=property_update)

    rnd_thickness = FloatProperty(
        name="Random Thickness",
        description="When greater than zero a random radius value, based upon this value, will be generated for each vertex along the curve.",
        min=0.0, max=42.0,
        default=0.0, update=property_update)

    height_offset = FloatProperty(
        name="Height Offset",
        description="How much to offset each normal for point generation. 0.0 = Inside Mesh, 1.0 = Outside Mesh.",
        min=0.0, max=1.0,
        default=0.0, update=property_update)

    rnd_seed = IntProperty(
        name="Random Seed",
        description="A seed value for the random number generator. Change for variations.",
        min=0, max=16384, default=801, update=property_update)

    use_selection = BoolProperty(name="Use Selection",
                                 description="When enabled multiple curves will be generated, one for each face selected in the mesh in edit mode. A single random face is chosen when disabled.",
                                 default=False, update=property_update)

# collection of property group classes that need to be registered on module startup
classes = [cls_BounceFibers]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # Add these properties to every object in the entire Blender system (muha-haa!!)
    bpy.types.Object.BounceFibers_List_Index = bpy.props.IntProperty(min=0, default=0, description="Internal value. Do not animate.")
    bpy.types.Object.BounceFibers_List = bpy.props.CollectionProperty(type=cls_BounceFibers, description="Internal list class.")


def unregister():
    bpy.utils.unregister_module(__name__)
