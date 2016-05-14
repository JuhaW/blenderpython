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
import random as r
from mathutils import Vector

#####################################################################
# Globals.
#####################################################################
from .util import to_console
from .util import removeCurveFromMemory
from .util import returnNameForNumber

############################################################################
# Generation code.
############################################################################


def reviewBounceFibers(self, context):
    ob = context.object
    if ob != None:
        if ob.type == 'MESH':
            # Ok to proceed.
            generate_bounce_fibers(self, context)

######################################################
# Bounce code.
######################################################


def noise(var=1):
    rand = Vector((r.gauss(0, 1), r.gauss(0, 1), r.gauss(0, 1)))
    vec = rand.normalized() * var
    return vec


def traceFromPolygon(object_name, polygon_index, entry):
    # Fetch our user parameters from the passed collection entry.
    bounce_number = entry.bounce_count
    ang_noise = entry.rnd_noise
    extra = entry.sub_steps
    offset = entry.height_offset
    random_seed = entry.rnd_seed

    r.seed(random_seed)
    dist, points, = 1000, []

    # Trace path of points while bouncing around inside the object_name mesh.
    # The path starting points is the face referenced via polygon_index.
    ob = bpy.data.objects.get(object_name)
    if ob != None:
        if ob.type == 'MESH':
            polys = ob.data.polygons

            end = polys[polygon_index].normal.copy() * -1  # Invert the normal because we are bouncing around inside the mesh.
            start = polys[polygon_index].center
            points.append(start + offset * end)

            bounce_type = 0
            if extra > 0:
                bounce_type = 1
            if bounce_type == 0:
                # Original bounce type, no sub-sampling.
                for i in range(bounce_number):
                    end += noise(ang_noise)
                    hit, nor, index = ob.ray_cast(start, end * dist)[-3:]
                    if index == -1:
                        break
                    start = hit - nor / 10000
                    end = end.reflect(nor).normalized()
                    points.append(hit + offset * nor)
            else:
                # Detailed bounce type, sub-sampling.
                for i in range(bounce_number):
                    for ray in range(extra + 1):
                        rnd = noise(ang_noise)
                        end += rnd
                        try:
                            hit, nor, index = ob.ray_cast(start, end * dist)[-3:]
                        except:
                            index = -1
                        if index != -1:
                            start = hit - nor / 10000
                            end = end.reflect(nor).normalized()
                            points.append(hit + offset * nor)
                            break
                    if index == -1:
                        return points
    return points


def add_curve(entry, curve_name, points, matrix, apply=False):
    curve_data_name = ("cu_%s" % curve_name)
    tracer = bpy.data.curves.get(curve_data_name)
    if tracer == None:
        # Make a new one.
        tracer = bpy.data.curves.new(curve_data_name, type='CURVE')
    else:
        # Reuse this existing curve, but we must remove all of the current splines.
        for old_spline in tracer.splines:
            try:
                tracer.splines.remove(old_spline)
            except:
                to_console("add_curve: ERROR trying to remove old_spline")

    # Default parameters for the curve we are generating.
    tracer.dimensions = '3D'
    tracer.fill_mode = 'FULL'
    tracer.use_uv_as_generated = True                 # For Cycles color mapping. Seems to be broken or not supported for Blender Internal.
    tracer.bevel_depth = entry.thickness              # So it will render, set to 0.0 to not render.
    tracer.resolution_u = entry.smoothness            # Smoother viewport surface with higher numbers.

    spline = tracer.splines.new('BEZIER')
    spline.bezier_points.add(len(points) - 1)

    curvobj = bpy.data.objects.get(curve_name)
    if curvobj == None:
        curvobj = bpy.data.objects.new(curve_name, tracer)
    else:
        old_curve_name = curvobj.data.name
        if old_curve_name != curve_data_name:
            # The names are different, time to link to the new datablock.
            curvobj.data = tracer
            removeCurveFromMemory(old_curve_name)

    for i in range(len(points)):
        spline.bezier_points[i].co = points[i]
        spline.bezier_points[i].handle_right_type = 'AUTO'
        spline.bezier_points[i].handle_left_type = 'AUTO'
        if entry.rnd_thickness > 0.0:
            spline.bezier_points[i].radius = r.random() * entry.rnd_thickness
    try:
        bpy.data.scenes[0].objects.link(curvobj)
    except:
        # Alreadylinked.
        pass

    if apply:
        tracer.transform(matrix)
    else:
        curvobj.matrix_world = matrix

    curvobj.show_x_ray = True
    return curvobj


def generate_bounce_fibers(self, context):
    ob = context.object         # Fetch the object from the active object in the scene.
    ob_name = ob.name           # Get the name of the object so we are not passing object variables, just strings.
    poly_indicies = []          # The list of starting points, derived from selection set and or active face.
    if ob.mode != 'EDIT':
        try:
            # Simple trap against non-mesh objects.
            polys = ob.data.polygons
        except:
            polys = None
        if polys != None:
            entry = ob.BounceFibers_List[ob.BounceFibers_List_Index]
            if entry.use_selection:
                # Scan the polygons for any selected faces, active face first.
                ai = polys.active                   # Fetch the active index.
                if ai != -1:                        # New API change 2.7.x. -1 is returned when no face is active.
                    poly_indicies.append(ai)

                n = 0
                for poly in polys:
                    if poly.select == True:
                        # This face is selected.
                        if poly.index == ai:
                            # Skip the active face, we already added it.
                            pass
                        else:
                            poly_indicies.append(n)
                    n += 1
            else:
                # Not using selection so just pick a face at random.
                n = r.randint(0, len(polys) - 1)
                poly_indicies.append(n)

            if len(poly_indicies) > 0:
                # Create a curve for each selected face in the source mesh whose starting point is the location of the selected or random face index.
                c = 0
                for polygon_index in poly_indicies:
                    points = traceFromPolygon(ob_name, polygon_index, entry)
                    if len(points) > 0:
                        # The trace produced points that we can use for constructing a new curve object.
                        # The generated object name takes the form of 'fiber_' plus the source object name with a zero padded post fix it's position in the list it came from.
                        new_name = "%s_%s" % (ob_name, returnNameForNumber(c))
                        ob_new = add_curve(entry, new_name, points, ob.matrix_world, False)
                        ob_new.parent = ob
                    c += 1
            else:
                to_console("No polygons selected...?")
    else:
        # Source object is in edit mode, we can't ray cast in this state.
        to_console("Source object in edit mode, not supported at this time.")

    # -----------------------------

    # obj: the mesh object
    # number: number of points to add
    # ang_noise: add some noise to ray direction
    # extra: number of extra tries if it fails to hit mesh
    # offset: use normal direction to offset spline (in BU)
    # random_seed: a number != 0 to get the same curve

    # with no face selected a random one is choosen
    # with faces selected a curve is generated for each selected face with active face first
