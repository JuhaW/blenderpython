def align(*args, axis='ALIGN_AUTO'):
    """Align selected UV vertices to an axis
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param axis: Axis, Axis to align UV locations on
        * 'ALIGN_S': Straighten, Align UVs along the line defined by the endpoints.
        * 'ALIGN_T': Straighten X, Align UVs along the line defined by the endpoints along the X axis.
        * 'ALIGN_U': Straighten Y, Align UVs along the line defined by the endpoints along the Y axis.
        * 'ALIGN_AUTO': Align Auto, Automatically choose the axis on which there is most alignment already.
        * 'ALIGN_X': Align X, Align UVs on X axis.
        * 'ALIGN_Y': Align Y, Align UVs on Y axis.
        (type: enum in ['ALIGN_S', 'ALIGN_T', 'ALIGN_U', 'ALIGN_AUTO', 'ALIGN_X', 'ALIGN_Y'], (optional))
    :type axis: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def average_islands_scale(*args):
    """Average the size of separate UV islands, based on their area in 3D space
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def circle_select(*args, x=0, y=0, radius=1, gesture_mode=0):
    """Select UV vertices using circle selection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param x: X
        (type: int in [-inf, inf], (optional))
    :type x: int
    :param y: Y
        (type: int in [-inf, inf], (optional))
    :type y: int
    :param radius: Radius
        (type: int in [1, inf], (optional))
    :type radius: int
    :param gesture_mode: Gesture Mode
        (type: int in [-inf, inf], (optional))
    :type gesture_mode: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def cube_project(*args, cube_size=1.0, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False):
    """Project the UV vertices of the mesh over the six faces of a cube
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param cube_size: Cube Size, Size of the cube to project on
        (type: float in [0, inf], (optional))
    :type cube_size: float
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        (type: boolean, (optional))
    :type correct_aspect: bool
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
        (type: boolean, (optional))
    :type clip_to_bounds: bool
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
        (type: boolean, (optional))
    :type scale_to_bounds: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def cursor_set(*args, location=(0.0, 0.0)):
    """Set 2D cursor location
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param location: Location, Cursor location in normalized (0.0-1.0) coordinates
        (type: float array of 2 items in [-inf, inf], (optional))
    :type location: mathutils.Vector
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def cylinder_project(*args, direction='VIEW_ON_EQUATOR', align='POLAR_ZX', radius=1.0, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False):
    """Project the UV vertices of the mesh over the curved wall of a cylinder
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param direction: Direction, Direction of the sphere or cylinder
        * 'VIEW_ON_EQUATOR': View on Equator, 3D view is on the equator.
        * 'VIEW_ON_POLES': View on Poles, 3D view is on the poles.
        * 'ALIGN_TO_OBJECT': Align to Object, Align according to object transform.
        (type: enum in ['VIEW_ON_EQUATOR', 'VIEW_ON_POLES', 'ALIGN_TO_OBJECT'], (optional))
    :type direction: str
    :param align: Align, How to determine rotation around the pole
        * 'POLAR_ZX': Polar ZX, Polar 0 is X.
        * 'POLAR_ZY': Polar ZY, Polar 0 is Y.
        (type: enum in ['POLAR_ZX', 'POLAR_ZY'], (optional))
    :type align: str
    :param radius: Radius, Radius of the sphere or cylinder
        (type: float in [0, inf], (optional))
    :type radius: float
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        (type: boolean, (optional))
    :type correct_aspect: bool
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
        (type: boolean, (optional))
    :type clip_to_bounds: bool
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
        (type: boolean, (optional))
    :type scale_to_bounds: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def export_layout(*args, filepath="", check_existing=True, export_all=False, modified=False, mode='PNG', size=(1024, 1024), opacity=0.25, tessellated=False):
    """Export UV layout to file
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param filepath: filepath
        (type: str, (optional, never None))
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
        (type: boolean, (optional))
    :type check_existing: bool
    :param export_all: All UVs, Export all UVs in this mesh (not just visible ones)
        (type: boolean, (optional))
    :type export_all: bool
    :param modified: Modified, Exports UVs from the modified mesh
        (type: boolean, (optional))
    :type modified: bool
    :param mode: Format, File format to export the UV layout to
        * 'SVG': Scalable Vector Graphic (.svg), Export the UV layout to a vector SVG file.
        * 'EPS': Encapsulate PostScript (.eps), Export the UV layout to a vector EPS file.
        * 'PNG': PNG Image (.png), Export the UV layout to a bitmap image.
        (type: enum in ['SVG', 'EPS', 'PNG'], (optional))
    :type mode: str
    :param size: size, Dimensions of the exported file
        (type: int array of 2 items in [8, 32768], (optional))
    :type size: collections.Sequence[int]
    :param opacity: Fill Opacity, Set amount of opacity for exported UV layout
        (type: float in [0, 1], (optional))
    :type opacity: float
    :param tessellated: Tessellated UVs, Export tessellated UVs instead of polygons ones
        (type: boolean, (optional))
    :type tessellated: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def follow_active_quads(*args, mode='LENGTH_AVERAGE'):
    """Follow UVs from active quads along continuous face loops
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mode: Edge Length Mode, Method to space UV edge loops
        * 'EVEN': Even, Space all UVs evenly.
        * 'LENGTH': Length, Average space UVs edge length of each loop.
        * 'LENGTH_AVERAGE': Length Average, Average space UVs edge length of each loop.
        (type: enum in ['EVEN', 'LENGTH', 'LENGTH_AVERAGE'], (optional))
    :type mode: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hide(*args, unselected=False):
    """Hide (un)selected UV vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param unselected: Unselected, Hide unselected rather than selected
        (type: boolean, (optional))
    :type unselected: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def lightmap_pack(*args, PREF_CONTEXT='SEL_FACES', PREF_PACK_IN_ONE=True, PREF_NEW_UVLAYER=False, PREF_APPLY_IMAGE=False, PREF_IMG_PX_SIZE=512, PREF_BOX_DIV=12, PREF_MARGIN_DIV=0.1):
    """Pack each faces UV's into the UV bounds
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param PREF_CONTEXT: Selection
        * 'SEL_FACES': Selected Faces, Space all UVs evenly.
        * 'ALL_FACES': All Faces, Average space UVs edge length of each loop.
        * 'ALL_OBJECTS': Selected Mesh Object, Average space UVs edge length of each loop.
        (type: enum in ['SEL_FACES', 'ALL_FACES', 'ALL_OBJECTS'], (optional))
    :type PREF_CONTEXT: str
    :param PREF_PACK_IN_ONE: Share Tex Space, Objects Share texture space, map all objects into 1 uvmap
        (type: boolean, (optional))
    :type PREF_PACK_IN_ONE: bool
    :param PREF_NEW_UVLAYER: New UV Map, Create a new UV map for every mesh packed
        (type: boolean, (optional))
    :type PREF_NEW_UVLAYER: bool
    :param PREF_APPLY_IMAGE: New Image, Assign new images for every mesh (only one if shared tex space enabled)
        (type: boolean, (optional))
    :type PREF_APPLY_IMAGE: bool
    :param PREF_IMG_PX_SIZE: Image Size, Width and Height for the new image
        (type: int in [64, 5000], (optional))
    :type PREF_IMG_PX_SIZE: int
    :param PREF_BOX_DIV: Pack Quality, Pre Packing before the complex boxpack
        (type: int in [1, 48], (optional))
    :type PREF_BOX_DIV: int
    :param PREF_MARGIN_DIV: Margin, Size of the margin as a division of the UV
        (type: float in [0.001, 1], (optional))
    :type PREF_MARGIN_DIV: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def mark_seam(*args, clear=False):
    """Mark selected UV edges as seams
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param clear: Clear Seams, Clear instead of marking seams
        (type: boolean, (optional))
    :type clear: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def minimize_stretch(*args, fill_holes=True, blend=0.0, iterations=0):
    """Reduce UV stretching by relaxing angles
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param fill_holes: Fill Holes, Virtual fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
        (type: boolean, (optional))
    :type fill_holes: bool
    :param blend: Blend, Blend factor between stretch minimized and original
        (type: float in [0, 1], (optional))
    :type blend: float
    :param iterations: Iterations, Number of iterations to run, 0 is unlimited when run interactively
        (type: int in [0, inf], (optional))
    :type iterations: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def pack_islands(*args, rotate=True, margin=0.001):
    """Transform all islands so that they fill up the UV space as much as possible
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param rotate: Rotate, Rotate islands for best fit
        (type: boolean, (optional))
    :type rotate: bool
    :param margin: Margin, Space between islands
        (type: float in [0, 1], (optional))
    :type margin: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def pin(*args, clear=False):
    """Set/clear selected UV vertices as anchored between multiple unwrap operations
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param clear: Clear, Clear pinning for the selection instead of setting it
        (type: boolean, (optional))
    :type clear: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def project_from_view(*args, orthographic=False, camera_bounds=True, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False):
    """Project the UV vertices of the mesh as seen in current 3D view
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param orthographic: Orthographic, Use orthographic projection
        (type: boolean, (optional))
    :type orthographic: bool
    :param camera_bounds: Camera Bounds, Map UVs to the camera region taking resolution and aspect into account
        (type: boolean, (optional))
    :type camera_bounds: bool
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        (type: boolean, (optional))
    :type correct_aspect: bool
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
        (type: boolean, (optional))
    :type clip_to_bounds: bool
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
        (type: boolean, (optional))
    :type scale_to_bounds: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def remove_doubles(*args, threshold=0.02, use_unselected=False):
    """Selected UV vertices that are within a radius of each other are welded together
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param threshold: Merge Distance, Maximum distance between welded vertices
        (type: float in [0, 10], (optional))
    :type threshold: float
    :param use_unselected: Unselected, Merge selected to other unselected vertices
        (type: boolean, (optional))
    :type use_unselected: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def reset(*args):
    """Reset UV projection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def reveal(*args):
    """Reveal all hidden UV vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def seams_from_islands(*args, mark_seams=True, mark_sharp=False):
    """Set mesh seams according to island setup in the UV editor
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mark_seams: Mark Seams, Mark boundary edges as seams
        (type: boolean, (optional))
    :type mark_seams: bool
    :param mark_sharp: Mark Sharp, Mark boundary edges as sharp
        (type: boolean, (optional))
    :type mark_sharp: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select(*args, extend=False, location=(0.0, 0.0)):
    """Select UV vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend selection rather than clearing the existing selection
        (type: boolean, (optional))
    :type extend: bool
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
        (type: float array of 2 items in [-inf, inf], (optional))
    :type location: mathutils.Vector
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_all(*args, action='TOGGLE'):
    """Change selection of all UV vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param action: Action, Selection action to execute
        * 'TOGGLE': Toggle, Toggle selection for all elements.
        * 'SELECT': Select, Select all elements.
        * 'DESELECT': Deselect, Deselect all elements.
        * 'INVERT': Invert, Invert selection of all elements.
        (type: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional))
    :type action: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_border(*args, pinned=False, gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
    """Select UV vertices using border selection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param pinned: Pinned, Border select pinned UVs only
        (type: boolean, (optional))
    :type pinned: bool
    :param gesture_mode: Gesture Mode
        (type: int in [-inf, inf], (optional))
    :type gesture_mode: int
    :param xmin: X Min
        (type: int in [-inf, inf], (optional))
    :type xmin: int
    :param xmax: X Max
        (type: int in [-inf, inf], (optional))
    :type xmax: int
    :param ymin: Y Min
        (type: int in [-inf, inf], (optional))
    :type ymin: int
    :param ymax: Y Max
        (type: int in [-inf, inf], (optional))
    :type ymax: int
    :param extend: Extend, Extend selection instead of deselecting everything first
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_lasso(*args, path=None, deselect=False, extend=True):
    """Select UVs using lasso selection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param path: Path
        (type: bpy_prop_collection of OperatorMousePath, (optional))
    :type path: bpy_prop_collection
    :param deselect: Deselect, Deselect rather than select items
        (type: boolean, (optional))
    :type deselect: bool
    :param extend: Extend, Extend selection instead of deselecting everything first
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_less(*args):
    """Deselect UV vertices at the boundary of each selection region
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_linked(*args, extend=False):
    """Select all UV vertices linked to the active UV map
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend selection rather than clearing the existing selection
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_linked_pick(*args, extend=False, location=(0.0, 0.0)):
    """Select all UV vertices linked under the mouse
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend selection rather than clearing the existing selection
        (type: boolean, (optional))
    :type extend: bool
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
        (type: float array of 2 items in [-inf, inf], (optional))
    :type location: mathutils.Vector
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_loop(*args, extend=False, location=(0.0, 0.0)):
    """Select a loop of connected UV vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend selection rather than clearing the existing selection
        (type: boolean, (optional))
    :type extend: bool
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
        (type: float array of 2 items in [-inf, inf], (optional))
    :type location: mathutils.Vector
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_more(*args):
    """Select more UV vertices connected to initial selection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_pinned(*args):
    """Select all pinned UV vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_split(*args):
    """Select only entirely selected faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def smart_project(*args, angle_limit=66.0, island_margin=0.0, user_area_weight=0.0, use_aspect=True, stretch_to_bounds=True):
    """This script projection unwraps the selected faces of a mesh (it operates on all selected mesh objects, and can be used to unwrap selected faces, or all faces)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param angle_limit: Angle Limit, Lower for more projection groups, higher for less distortion
        (type: float in [1, 89], (optional))
    :type angle_limit: float
    :param island_margin: Island Margin, Margin to reduce bleed from adjacent islands
        (type: float in [0, 1], (optional))
    :type island_margin: float
    :param user_area_weight: Area Weight, Weight projections vector by faces with larger areas
        (type: float in [0, 1], (optional))
    :type user_area_weight: float
    :param use_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        (type: boolean, (optional))
    :type use_aspect: bool
    :param stretch_to_bounds: Stretch to UV Bounds, Stretch the final output to texture bounds
        (type: boolean, (optional))
    :type stretch_to_bounds: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def snap_cursor(*args, target='PIXELS'):
    """Snap cursor to target type
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param target: Target, Target to snap the selected UVs to
        (type: enum in ['PIXELS', 'SELECTED'], (optional))
    :type target: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def snap_selected(*args, target='PIXELS'):
    """Snap selected UV vertices to target type
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param target: Target, Target to snap the selected UVs to
        (type: enum in ['PIXELS', 'CURSOR', 'CURSOR_OFFSET', 'ADJACENT_UNSELECTED'], (optional))
    :type target: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def sphere_project(*args, direction='VIEW_ON_EQUATOR', align='POLAR_ZX', correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False):
    """Project the UV vertices of the mesh over the curved surface of a sphere
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param direction: Direction, Direction of the sphere or cylinder
        * 'VIEW_ON_EQUATOR': View on Equator, 3D view is on the equator.
        * 'VIEW_ON_POLES': View on Poles, 3D view is on the poles.
        * 'ALIGN_TO_OBJECT': Align to Object, Align according to object transform.
        (type: enum in ['VIEW_ON_EQUATOR', 'VIEW_ON_POLES', 'ALIGN_TO_OBJECT'], (optional))
    :type direction: str
    :param align: Align, How to determine rotation around the pole
        * 'POLAR_ZX': Polar ZX, Polar 0 is X.
        * 'POLAR_ZY': Polar ZY, Polar 0 is Y.
        (type: enum in ['POLAR_ZX', 'POLAR_ZY'], (optional))
    :type align: str
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        (type: boolean, (optional))
    :type correct_aspect: bool
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
        (type: boolean, (optional))
    :type clip_to_bounds: bool
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
        (type: boolean, (optional))
    :type scale_to_bounds: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def stitch(*args, use_limit=False, snap_islands=True, limit=0.01, static_island=0, midpoint_snap=False, clear_seams=True, mode='VERTEX', stored_mode='VERTEX', selection=None):
    """Stitch selected UV vertices by proximity
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_limit: Use Limit, Stitch UVs within a specified limit distance
        (type: boolean, (optional))
    :type use_limit: bool
    :param snap_islands: Snap Islands, Snap islands together (on edge stitch mode, rotates the islands too)
        (type: boolean, (optional))
    :type snap_islands: bool
    :param limit: Limit, Limit distance in normalized coordinates
        (type: float in [0, inf], (optional))
    :type limit: float
    :param static_island: Static Island, Island that stays in place when stitching islands
        (type: int in [0, inf], (optional))
    :type static_island: int
    :param midpoint_snap: Snap At Midpoint, UVs are stitched at midpoint instead of at static island
        (type: boolean, (optional))
    :type midpoint_snap: bool
    :param clear_seams: Clear Seams, Clear seams of stitched edges
        (type: boolean, (optional))
    :type clear_seams: bool
    :param mode: Operation Mode, Use vertex or edge stitching
        (type: enum in ['VERTEX', 'EDGE'], (optional))
    :type mode: str
    :param stored_mode: Stored Operation Mode, Use vertex or edge stitching
        (type: enum in ['VERTEX', 'EDGE'], (optional))
    :type stored_mode: str
    :param selection: Selection
        (type: bpy_prop_collection of SelectedUvElement, (optional))
    :type selection: bpy_prop_collection
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def tile_set(*args, tile=(0, 0)):
    """Set UV image tile coordinates
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param tile: Tile, Tile coordinate
        (type: int array of 2 items in [0, inf], (optional))
    :type tile: collections.Sequence[int]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def unwrap(*args, method='ANGLE_BASED', fill_holes=True, correct_aspect=True, use_subsurf_data=False, margin=0.001):
    """Unwrap the mesh of the object being edited
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param method: Method, Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower)
        (type: enum in ['ANGLE_BASED', 'CONFORMAL'], (optional))
    :type method: str
    :param fill_holes: Fill Holes, Virtual fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
        (type: boolean, (optional))
    :type fill_holes: bool
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        (type: boolean, (optional))
    :type correct_aspect: bool
    :param use_subsurf_data: Use Subsurf Modifier, Map UVs taking vertex position after Subdivision Surface modifier has been applied
        (type: boolean, (optional))
    :type use_subsurf_data: bool
    :param margin: Margin, Space between islands
        (type: float in [0, 1], (optional))
    :type margin: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def weld(*args):
    """Weld selected UV vertices together
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
