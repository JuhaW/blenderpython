from . import geometry
from . import ops
from . import types
from . import utils


def from_edit_mesh(mesh):
    """Return a BMesh from this mesh, currently the mesh must already be in editmode.
    
    :param mesh: The editmode mesh.
    :type mesh: bpy.types.Mesh
    :return: the BMesh associated with this mesh.
    :param : (type: bmesh.types.BMesh)
    :rtype: types.BMesh
    """


def new(use_operators=True):
    """
    :param use_operators: Support calling operators in bmesh.ops (uses some extra memory per vert/edge/face).
    :type use_operators: bool
    :return: Return a new, empty BMesh.
    :param : (type: bmesh.types.BMesh)
    :rtype: types.BMesh
    """


def update_edit_mesh(mesh, tessface=True, destructive=True):
    """Update the mesh after changes to the BMesh in editmode,
                            optionally recalculating n-gon tessellation.
    
    :param mesh: The editmode mesh.
    :type mesh: bpy.types.Mesh
    :param tessface: Option to recalculate n-gon tessellation.
    :type tessface: bool
    :param destructive: Use when geometry has been added or removed.
    :type destructive: bool
    """
