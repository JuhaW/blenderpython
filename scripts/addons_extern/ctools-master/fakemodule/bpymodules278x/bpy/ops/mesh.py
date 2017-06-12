def beautify_fill(*args, angle_limit=3.14159):
    """Rearrange some faces to try to get less degenerated geometry
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param angle_limit: Max Angle, Angle limit
        (type: float in [0, 3.14159], (optional))
    :type angle_limit: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def bevel(*args, offset_type='OFFSET', offset=0.0, segments=1, profile=0.5, vertex_only=False, clamp_overlap=False, loop_slide=True, material=-1):
    """Edge Bevel
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param offset_type: Amount Type, What distance Amount measures
        * 'OFFSET': Offset, Amount is offset of new edges from original.
        * 'WIDTH': Width, Amount is width of new face.
        * 'DEPTH': Depth, Amount is perpendicular distance from original edge to bevel face.
        * 'PERCENT': Percent, Amount is percent of adjacent edge length.
        (type: enum in ['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT'], (optional))
    :type offset_type: str
    :param offset: Amount
        (type: float in [-1e+06, 1e+06], (optional))
    :type offset: float
    :param segments: Segments, Segments for curved edge
        (type: int in [1, 1000], (optional))
    :type segments: int
    :param profile: Profile, Controls profile shape (0.5 = round)
        (type: float in [0.15, 1], (optional))
    :type profile: float
    :param vertex_only: Vertex Only, Bevel only vertices
        (type: boolean, (optional))
    :type vertex_only: bool
    :param clamp_overlap: Clamp Overlap, Do not allow beveled edges/vertices to overlap each other
        (type: boolean, (optional))
    :type clamp_overlap: bool
    :param loop_slide: Loop Slide, Prefer slide along edge to even widths
        (type: boolean, (optional))
    :type loop_slide: bool
    :param material: Material, Material for bevel faces (-1 means use adjacent faces)
        (type: int in [-1, inf], (optional))
    :type material: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def bisect(*args, plane_co=(0.0, 0.0, 0.0), plane_no=(0.0, 0.0, 0.0), use_fill=False, clear_inner=False, clear_outer=False, threshold=0.0001, xstart=0, xend=0, ystart=0, yend=0, cursor=1002):
    """Cut geometry along a plane (click-drag to define plane)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param plane_co: Plane Point, A point on the plane
        (type: float array of 3 items in [-inf, inf], (optional))
    :type plane_co: mathutils.Vector
    :param plane_no: Plane Normal, The direction the plane points
        (type: float array of 3 items in [-1, 1], (optional))
    :type plane_no: mathutils.Vector
    :param use_fill: Fill, Fill in the cut
        (type: boolean, (optional))
    :type use_fill: bool
    :param clear_inner: Clear Inner, Remove geometry behind the plane
        (type: boolean, (optional))
    :type clear_inner: bool
    :param clear_outer: Clear Outer, Remove geometry in front of the plane
        (type: boolean, (optional))
    :type clear_outer: bool
    :param threshold: Axis Threshold
        (type: float in [0, 10], (optional))
    :type threshold: float
    :param xstart: X Start
        (type: int in [-inf, inf], (optional))
    :type xstart: int
    :param xend: X End
        (type: int in [-inf, inf], (optional))
    :type xend: int
    :param ystart: Y Start
        (type: int in [-inf, inf], (optional))
    :type ystart: int
    :param yend: Y End
        (type: int in [-inf, inf], (optional))
    :type yend: int
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
        (type: int in [0, inf], (optional))
    :type cursor: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def blend_from_shape(*args, shape='', blend=1.0, add=True):
    """Blend in shape from a shape key
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param shape: Shape, Shape key to use for blending
        (type: enum in [], (optional))
    :type shape: str
    :param blend: Blend, Blending factor
        (type: float in [-1000, 1000], (optional))
    :type blend: float
    :param add: Add, Add rather than blend between shapes
        (type: boolean, (optional))
    :type add: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def bridge_edge_loops(*args, type='SINGLE', use_merge=False, merge_factor=0.5, twist_offset=0, number_cuts=0, interpolation='PATH', smoothness=1.0, profile_shape_factor=0.0, profile_shape='SMOOTH'):
    """Make faces between two or more edge loops
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Connect Loops, Method of bridging multiple loops
        (type: enum in ['SINGLE', 'CLOSED', 'PAIRS'], (optional))
    :type type: str
    :param use_merge: Merge, Merge rather than creating faces
        (type: boolean, (optional))
    :type use_merge: bool
    :param merge_factor: Merge Factor
        (type: float in [0, 1], (optional))
    :type merge_factor: float
    :param twist_offset: Twist, Twist offset for closed loops
        (type: int in [-1000, 1000], (optional))
    :type twist_offset: int
    :param number_cuts: Number of Cuts
        (type: int in [0, 1000], (optional))
    :type number_cuts: int
    :param interpolation: Interpolation, Interpolation method
        (type: enum in ['LINEAR', 'PATH', 'SURFACE'], (optional))
    :type interpolation: str
    :param smoothness: Smoothness, Smoothness factor
        (type: float in [0, 1000], (optional))
    :type smoothness: float
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
        (type: float in [-1000, 1000], (optional))
    :type profile_shape_factor: float
    :param profile_shape: Profile Shape, Shape of the profile
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR'], (optional))
    :type profile_shape: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def colors_reverse(*args):
    """Flip direction of vertex colors inside faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def colors_rotate(*args, use_ccw=False):
    """Rotate vertex colors inside faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_ccw: Counter Clockwise
        (type: boolean, (optional))
    :type use_ccw: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def convex_hull(*args, delete_unused=True, use_existing_faces=True, make_holes=False, join_triangles=True, face_threshold=0.698132, shape_threshold=0.698132, uvs=False, vcols=False, seam=False, sharp=False, materials=False):
    """Enclose selected vertices in a convex polyhedron
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param delete_unused: Delete Unused, Delete selected elements that are not used by the hull
        (type: boolean, (optional))
    :type delete_unused: bool
    :param use_existing_faces: Use Existing Faces, Skip hull triangles that are covered by a pre-existing face
        (type: boolean, (optional))
    :type use_existing_faces: bool
    :param make_holes: Make Holes, Delete selected faces that are used by the hull
        (type: boolean, (optional))
    :type make_holes: bool
    :param join_triangles: Join Triangles, Merge adjacent triangles into quads
        (type: boolean, (optional))
    :type join_triangles: bool
    :param face_threshold: Max Face Angle, Face angle limit
        (type: float in [0, 3.14159], (optional))
    :type face_threshold: float
    :param shape_threshold: Max Shape Angle, Shape angle limit
        (type: float in [0, 3.14159], (optional))
    :type shape_threshold: float
    :param uvs: Compare UVs
        (type: boolean, (optional))
    :type uvs: bool
    :param vcols: Compare VCols
        (type: boolean, (optional))
    :type vcols: bool
    :param seam: Compare Seam
        (type: boolean, (optional))
    :type seam: bool
    :param sharp: Compare Sharp
        (type: boolean, (optional))
    :type sharp: bool
    :param materials: Compare Materials
        (type: boolean, (optional))
    :type materials: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def customdata_custom_splitnormals_add(*args):
    """Add a custom split normals layer, if none exists yet
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def customdata_custom_splitnormals_clear(*args):
    """Remove the custom split normals layer, if it exists
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def customdata_mask_clear(*args):
    """Clear vertex sculpt masking data from the mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def customdata_skin_add(*args):
    """Add a vertex skin layer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def customdata_skin_clear(*args):
    """Clear vertex skin layer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def decimate(*args, ratio=1.0, use_vertex_group=False, vertex_group_factor=1.0, invert_vertex_group=False, use_symmetry=False, symmetry_axis='Y'):
    """Simplify geometry by collapsing edges
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param ratio: Ratio
        (type: float in [0, 1], (optional))
    :type ratio: float
    :param use_vertex_group: Vertex Group, Use active vertex group as an influence
        (type: boolean, (optional))
    :type use_vertex_group: bool
    :param vertex_group_factor: Weight, Vertex group strength
        (type: float in [0, 1000], (optional))
    :type vertex_group_factor: float
    :param invert_vertex_group: Invert, Invert vertex group influence
        (type: boolean, (optional))
    :type invert_vertex_group: bool
    :param use_symmetry: Symmetry, Maintain symmetry on an axis
        (type: boolean, (optional))
    :type use_symmetry: bool
    :param symmetry_axis: Axis, Axis of symmetry
        (type: enum in ['X', 'Y', 'Z'], (optional))
    :type symmetry_axis: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def delete(*args, type='VERT'):
    """Delete selected vertices, edges or faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type, Method used for deleting mesh data
        (type: enum in ['VERT', 'EDGE', 'FACE', 'EDGE_FACE', 'ONLY_FACE'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def delete_edgeloop(*args, use_face_split=True):
    """Delete an edge loop by merging the faces on each side
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
        (type: boolean, (optional))
    :type use_face_split: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def delete_loose(*args, use_verts=True, use_edges=True, use_faces=False):
    """Delete loose vertices, edges or faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_verts: Vertices, Remove loose vertices
        (type: boolean, (optional))
    :type use_verts: bool
    :param use_edges: Edges, Remove loose edges
        (type: boolean, (optional))
    :type use_edges: bool
    :param use_faces: Faces, Remove loose faces
        (type: boolean, (optional))
    :type use_faces: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def dissolve_degenerate(*args, threshold=0.0001):
    """Dissolve zero area faces and zero length edges
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param threshold: Merge Distance, Minimum distance between elements to merge
        (type: float in [1e-06, 50], (optional))
    :type threshold: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def dissolve_edges(*args, use_verts=True, use_face_split=False):
    """Dissolve edges, merging faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_verts: Dissolve Verts, Dissolve remaining vertices
        (type: boolean, (optional))
    :type use_verts: bool
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
        (type: boolean, (optional))
    :type use_face_split: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def dissolve_faces(*args, use_verts=False):
    """Dissolve faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_verts: Dissolve Verts, Dissolve remaining vertices
        (type: boolean, (optional))
    :type use_verts: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def dissolve_limited(*args, angle_limit=0.0872665, use_dissolve_boundaries=False, delimit={'NORMAL'}):
    """Dissolve selected edges and verts, limited by the angle of surrounding geometry
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param angle_limit: Max Angle, Angle limit
        (type: float in [0, 3.14159], (optional))
    :type angle_limit: float
    :param use_dissolve_boundaries: All Boundaries, Dissolve all vertices inbetween face boundaries
        (type: boolean, (optional))
    :type use_dissolve_boundaries: bool
    :param delimit: Delimit, Delimit dissolve operation
        * 'NORMAL': Normal, Delimit by face directions.
        * 'MATERIAL': Material, Delimit by face material.
        * 'SEAM': Seam, Delimit by edge seams.
        * 'SHARP': Sharp, Delimit by sharp edges.
        * 'UV': UVs, Delimit by UV coordinates.
        (type: enum set in {'NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV'}, (optional))
    :type delimit: enum set in {'NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV'}
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def dissolve_mode(*args, use_verts=False, use_face_split=False, use_boundary_tear=False):
    """Dissolve geometry based on the selection mode
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_verts: Dissolve Verts, Dissolve remaining vertices
        (type: boolean, (optional))
    :type use_verts: bool
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
        (type: boolean, (optional))
    :type use_face_split: bool
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
        (type: boolean, (optional))
    :type use_boundary_tear: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def dissolve_verts(*args, use_face_split=False, use_boundary_tear=False):
    """Dissolve verts, merge edges and faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
        (type: boolean, (optional))
    :type use_face_split: bool
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
        (type: boolean, (optional))
    :type use_boundary_tear: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def drop_named_image(*args, name="Image", filepath="Path", relative_path=True):
    """Assign Image to active UV Map, or create an UV Map
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param name: Name, Image name to assign
        (type: str, (optional, never None))
    :type name: str
    :param filepath: Filepath, Path to image file
        (type: str, (optional, never None))
    :type filepath: str
    :param relative_path: Relative Path, Select the file relative to the blend file
        (type: boolean, (optional))
    :type relative_path: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def dupli_extrude_cursor(*args, rotate_source=True):
    """Duplicate and extrude selected vertices, edges or faces towards the mouse cursor
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param rotate_source: Rotate Source, Rotate initial selection giving better shape
        (type: boolean, (optional))
    :type rotate_source: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def duplicate(*args, mode=1):
    """Duplicate selected vertices, edges or faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mode: Mode
        (type: int in [0, inf], (optional))
    :type mode: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def duplicate_move(*args, MESH_OT_duplicate=None, TRANSFORM_OT_translate=None):
    """Duplicate mesh and move
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param MESH_OT_duplicate: Duplicate, Duplicate selected vertices, edges or faces
        (type: MESH_OT_duplicate, (optional))
    :type MESH_OT_duplicate: MESH_OT_duplicate
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
        (type: TRANSFORM_OT_translate, (optional))
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def edge_collapse(*args):
    """Collapse selected edges
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def edge_face_add(*args):
    """Add an edge or face to selected
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def edge_rotate(*args, use_ccw=False):
    """Rotate selected edge or adjoining faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_ccw: Counter Clockwise
        (type: boolean, (optional))
    :type use_ccw: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def edge_split(*args):
    """Split selected edges so that each neighbor face gets its own copy
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def edgering_select(*args, extend=False, deselect=False, toggle=False, ring=True):
    """Select an edge ring
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend the selection
        (type: boolean, (optional))
    :type extend: bool
    :param deselect: Deselect, Remove from the selection
        (type: boolean, (optional))
    :type deselect: bool
    :param toggle: Toggle Select, Toggle the selection
        (type: boolean, (optional))
    :type toggle: bool
    :param ring: Select Ring, Select ring
        (type: boolean, (optional))
    :type ring: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def edges_select_sharp(*args, sharpness=0.523599):
    """Select all sharp-enough edges
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param sharpness: Sharpness
        (type: float in [0.000174533, 3.14159], (optional))
    :type sharpness: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def extrude_edges_indiv(*args, mirror=False):
    """Extrude individual edges only
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def extrude_edges_move(*args, MESH_OT_extrude_edges_indiv=None, TRANSFORM_OT_translate=None):
    """Extrude edges and move result
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
        (type: MESH_OT_extrude_edges_indiv, (optional))
    :type MESH_OT_extrude_edges_indiv: MESH_OT_extrude_edges_indiv
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
        (type: TRANSFORM_OT_translate, (optional))
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def extrude_faces_indiv(*args, mirror=False):
    """Extrude individual faces only
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def extrude_faces_move(*args, MESH_OT_extrude_faces_indiv=None, TRANSFORM_OT_shrink_fatten=None):
    """Extrude faces and move result
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param MESH_OT_extrude_faces_indiv: Extrude Individual Faces, Extrude individual faces only
        (type: MESH_OT_extrude_faces_indiv, (optional))
    :type MESH_OT_extrude_faces_indiv: MESH_OT_extrude_faces_indiv
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
        (type: TRANSFORM_OT_shrink_fatten, (optional))
    :type TRANSFORM_OT_shrink_fatten: TRANSFORM_OT_shrink_fatten
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def extrude_region(*args, mirror=False):
    """Extrude region of faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def extrude_region_move(*args, MESH_OT_extrude_region=None, TRANSFORM_OT_translate=None):
    """Extrude region and move result
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
        (type: MESH_OT_extrude_region, (optional))
    :type MESH_OT_extrude_region: MESH_OT_extrude_region
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
        (type: TRANSFORM_OT_translate, (optional))
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def extrude_region_shrink_fatten(*args, MESH_OT_extrude_region=None, TRANSFORM_OT_shrink_fatten=None):
    """Extrude region and move result
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
        (type: MESH_OT_extrude_region, (optional))
    :type MESH_OT_extrude_region: MESH_OT_extrude_region
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
        (type: TRANSFORM_OT_shrink_fatten, (optional))
    :type TRANSFORM_OT_shrink_fatten: TRANSFORM_OT_shrink_fatten
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def extrude_repeat(*args, offset=2.0, steps=10):
    """Extrude selected vertices, edges or faces repeatedly
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param offset: Offset
        (type: float in [0, inf], (optional))
    :type offset: float
    :param steps: Steps
        (type: int in [0, 1000000], (optional))
    :type steps: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def extrude_vertices_move(*args, MESH_OT_extrude_verts_indiv=None, TRANSFORM_OT_translate=None):
    """Extrude vertices and move result
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param MESH_OT_extrude_verts_indiv: Extrude Only Vertices, Extrude individual vertices only
        (type: MESH_OT_extrude_verts_indiv, (optional))
    :type MESH_OT_extrude_verts_indiv: MESH_OT_extrude_verts_indiv
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
        (type: TRANSFORM_OT_translate, (optional))
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def extrude_verts_indiv(*args, mirror=False):
    """Extrude individual vertices only
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def face_make_planar(*args, factor=1.0, repeat=1):
    """Flatten selected faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param factor: Factor
        (type: float in [-10, 10], (optional))
    :type factor: float
    :param repeat: Iterations
        (type: int in [1, 10000], (optional))
    :type repeat: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def face_split_by_edges(*args):
    """Weld loose edges into faces (splitting them into new faces)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def faces_mirror_uv(*args, direction='POSITIVE', precision=3):
    """Copy mirror UV coordinates on the X axis based on a mirrored mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param direction: Axis Direction
        (type: enum in ['POSITIVE', 'NEGATIVE'], (optional))
    :type direction: str
    :param precision: Precision, Tolerance for finding vertex duplicates
        (type: int in [1, 16], (optional))
    :type precision: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def faces_select_linked_flat(*args, sharpness=0.0174533):
    """Select linked faces by angle
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param sharpness: Sharpness
        (type: float in [0.000174533, 3.14159], (optional))
    :type sharpness: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def faces_shade_flat(*args):
    """Display faces flat
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def faces_shade_smooth(*args):
    """Display faces smooth (using vertex normals)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def fill(*args, use_beauty=True):
    """Fill a selected edge loop with faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_beauty: Beauty, Use best triangulation division
        (type: boolean, (optional))
    :type use_beauty: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def fill_grid(*args, span=1, offset=0, use_interp_simple=False):
    """Fill grid from two loops
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param span: Span, Number of sides (zero disables)
        (type: int in [1, 1000], (optional))
    :type span: int
    :param offset: Offset, Number of sides (zero disables)
        (type: int in [-1000, 1000], (optional))
    :type offset: int
    :param use_interp_simple: Simple Blending
        (type: boolean, (optional))
    :type use_interp_simple: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def fill_holes(*args, sides=4):
    """Fill in holes (boundary edge loops)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param sides: Sides, Number of sides in hole required to fill (zero fills all holes)
        (type: int in [0, 1000], (optional))
    :type sides: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def flip_normals(*args):
    """Flip the direction of selected faces' normals (and of their vertices)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hide(*args, unselected=False):
    """Hide (un)selected vertices, edges or faces
    
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


def inset(*args, use_boundary=True, use_even_offset=True, use_relative_offset=False, use_edge_rail=False, thickness=0.01, depth=0.0, use_outset=False, use_select_inset=False, use_individual=False, use_interpolate=True):
    """Inset new faces into selected faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_boundary: Boundary, Inset face boundaries
        (type: boolean, (optional))
    :type use_boundary: bool
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
        (type: boolean, (optional))
    :type use_even_offset: bool
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
        (type: boolean, (optional))
    :type use_relative_offset: bool
    :param use_edge_rail: Edge Rail, Inset the region along existing edges
        (type: boolean, (optional))
    :type use_edge_rail: bool
    :param thickness: Thickness
        (type: float in [0, inf], (optional))
    :type thickness: float
    :param depth: Depth
        (type: float in [-inf, inf], (optional))
    :type depth: float
    :param use_outset: Outset, Outset rather than inset
        (type: boolean, (optional))
    :type use_outset: bool
    :param use_select_inset: Select Outer, Select the new inset faces
        (type: boolean, (optional))
    :type use_select_inset: bool
    :param use_individual: Individual, Individual Face Inset
        (type: boolean, (optional))
    :type use_individual: bool
    :param use_interpolate: Interpolate, Blend face data across the inset
        (type: boolean, (optional))
    :type use_interpolate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def intersect(*args, mode='SELECT_UNSELECT', separate_mode='CUT', threshold=1e-06):
    """Cut an intersection into faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mode: Source
        * 'SELECT': Self Intersect, Self intersect selected faces.
        * 'SELECT_UNSELECT': Selected/Unselected, Intersect selected with unselected faces.
        (type: enum in ['SELECT', 'SELECT_UNSELECT'], (optional))
    :type mode: str
    :param separate_mode: Separate Mode
        * 'ALL': All, Separate all geometry from intersections.
        * 'CUT': Cut, Cut into geometry keeping each side separate (Selected/Unselected only).
        * 'NONE': Merge, Merge all geometry from the intersection.
        (type: enum in ['ALL', 'CUT', 'NONE'], (optional))
    :type separate_mode: str
    :param threshold: Merge threshold
        (type: float in [0, 0.01], (optional))
    :type threshold: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def intersect_boolean(*args, operation='DIFFERENCE', use_swap=False, threshold=1e-06):
    """Cut solid geometry from selected to unselected
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param operation: Boolean
        (type: enum in ['INTERSECT', 'UNION', 'DIFFERENCE'], (optional))
    :type operation: str
    :param use_swap: Swap, Use with difference intersection to swap which side is kept
        (type: boolean, (optional))
    :type use_swap: bool
    :param threshold: Merge threshold
        (type: float in [0, 0.01], (optional))
    :type threshold: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def knife_project(*args, cut_through=False):
    """Use other objects outlines & boundaries to project knife cuts
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param cut_through: Cut through, Cut through all faces, not just visible ones
        (type: boolean, (optional))
    :type cut_through: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def knife_tool(*args, use_occlude_geometry=True, only_selected=False):
    """Cut new topology
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_occlude_geometry: Occlude Geometry, Only cut the front most geometry
        (type: boolean, (optional))
    :type use_occlude_geometry: bool
    :param only_selected: Only Selected, Only cut selected geometry
        (type: boolean, (optional))
    :type only_selected: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def loop_multi_select(*args, ring=False):
    """Select a loop of connected edges by connection type
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param ring: Ring
        (type: boolean, (optional))
    :type ring: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def loop_select(*args, extend=False, deselect=False, toggle=False, ring=False):
    """Select a loop of connected edges
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend Select, Extend the selection
        (type: boolean, (optional))
    :type extend: bool
    :param deselect: Deselect, Remove from the selection
        (type: boolean, (optional))
    :type deselect: bool
    :param toggle: Toggle Select, Toggle the selection
        (type: boolean, (optional))
    :type toggle: bool
    :param ring: Select Ring, Select ring
        (type: boolean, (optional))
    :type ring: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def loop_to_region(*args, select_bigger=False):
    """Select region of faces inside of a selected loop of edges
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param select_bigger: Select Bigger, Select bigger regions instead of smaller ones
        (type: boolean, (optional))
    :type select_bigger: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def loopcut(*args, number_cuts=1, smoothness=0.0, falloff='INVERSE_SQUARE', edge_index=-1, mesh_select_mode_init=(False, False, False)):
    """Add a new loop between existing loops
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param number_cuts: Number of Cuts
        (type: int in [1, 1000000], (optional))
    :type number_cuts: int
    :param smoothness: Smoothness, Smoothness factor
        (type: float in [-1000, 1000], (optional))
    :type smoothness: float
    :param falloff: Falloff, Falloff type the feather
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR'], (optional))
    :type falloff: str
    :param edge_index: Edge Index
        (type: int in [-1, inf], (optional))
    :type edge_index: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def loopcut_slide(*args, MESH_OT_loopcut=None, TRANSFORM_OT_edge_slide=None):
    """Cut mesh loop and slide it
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param MESH_OT_loopcut: Loop Cut, Add a new loop between existing loops
        (type: MESH_OT_loopcut, (optional))
    :type MESH_OT_loopcut: MESH_OT_loopcut
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
        (type: TRANSFORM_OT_edge_slide, (optional))
    :type TRANSFORM_OT_edge_slide: TRANSFORM_OT_edge_slide
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def mark_freestyle_edge(*args, clear=False):
    """(Un)mark selected edges as Freestyle feature edges
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param clear: Clear
        (type: boolean, (optional))
    :type clear: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def mark_freestyle_face(*args, clear=False):
    """(Un)mark selected faces for exclusion from Freestyle feature edge detection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param clear: Clear
        (type: boolean, (optional))
    :type clear: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def mark_seam(*args, clear=False):
    """(Un)mark selected edges as a seam
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param clear: Clear
        (type: boolean, (optional))
    :type clear: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def mark_sharp(*args, clear=False, use_verts=False):
    """(Un)mark selected edges as sharp
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param clear: Clear
        (type: boolean, (optional))
    :type clear: bool
    :param use_verts: Vertices, Consider vertices instead of edges to select which edges to (un)tag as sharp
        (type: boolean, (optional))
    :type use_verts: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def merge(*args, type='CENTER', uvs=False):
    """Merge selected vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type, Merge method to use
        (type: enum in ['FIRST', 'LAST', 'CENTER', 'CURSOR', 'COLLAPSE'], (optional))
    :type type: str
    :param uvs: UVs, Move UVs according to merge
        (type: boolean, (optional))
    :type uvs: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def navmesh_clear(*args):
    """Remove navmesh data from this mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def navmesh_face_add(*args):
    """Add a new index and assign it to selected faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def navmesh_face_copy(*args):
    """Copy the index from the active face
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def navmesh_make(*args):
    """Create navigation mesh for selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def navmesh_reset(*args):
    """Assign a new index to every face
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def noise(*args, factor=0.1):
    """Use vertex coordinate as texture coordinate
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param factor: Factor
        (type: float in [-10000, 10000], (optional))
    :type factor: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def normals_make_consistent(*args, inside=False):
    """Make face and vertex normals point either outside or inside the mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param inside: Inside
        (type: boolean, (optional))
    :type inside: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def offset_edge_loops(*args, use_cap_endpoint=False):
    """Create offset edge loop from the current selection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_cap_endpoint: Cap Endpoint, Extend loop around end-points
        (type: boolean, (optional))
    :type use_cap_endpoint: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def offset_edge_loops_slide(*args, MESH_OT_offset_edge_loops=None, TRANSFORM_OT_edge_slide=None):
    """Offset edge loop slide
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param MESH_OT_offset_edge_loops: Offset Edge Loop, Create offset edge loop from the current selection
        (type: MESH_OT_offset_edge_loops, (optional))
    :type MESH_OT_offset_edge_loops: MESH_OT_offset_edge_loops
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
        (type: TRANSFORM_OT_edge_slide, (optional))
    :type TRANSFORM_OT_edge_slide: TRANSFORM_OT_edge_slide
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def poke(*args, offset=0.0, use_relative_offset=False, center_mode='MEAN_WEIGHTED'):
    """Split a face into a fan
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param offset: Poke Offset, Poke Offset
        (type: float in [-1000, 1000], (optional))
    :type offset: float
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
        (type: boolean, (optional))
    :type use_relative_offset: bool
    :param center_mode: Poke Center, Poke Face Center Calculation
        * 'MEAN_WEIGHTED': Weighted Mean, Weighted Mean Face Center.
        * 'MEAN': Mean, Mean Face Center.
        * 'BOUNDS': Bounds, Face Bounds Center.
        (type: enum in ['MEAN_WEIGHTED', 'MEAN', 'BOUNDS'], (optional))
    :type center_mode: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def primitive_circle_add(*args, vertices=32, radius=1.0, fill_type='NOTHING', calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Construct a circle mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param vertices: Vertices
        (type: int in [3, 10000000], (optional))
    :type vertices: int
    :param radius: Radius
        (type: float in [0, inf], (optional))
    :type radius: float
    :param fill_type: Fill Type
        * 'NOTHING': Nothing, Don't fill at all.
        * 'NGON': Ngon, Use ngons.
        * 'TRIFAN': Triangle Fan, Use triangle fans.
        (type: enum in ['NOTHING', 'NGON', 'TRIFAN'], (optional))
    :type fill_type: str
    :param calc_uvs: Generate UVs, Generate a default UV map
        (type: boolean, (optional))
    :type calc_uvs: bool
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def primitive_cone_add(*args, vertices=32, radius1=1.0, radius2=0.0, depth=2.0, end_fill_type='NGON', calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Construct a conic mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param vertices: Vertices
        (type: int in [3, 10000000], (optional))
    :type vertices: int
    :param radius1: Radius 1
        (type: float in [0, inf], (optional))
    :type radius1: float
    :param radius2: Radius 2
        (type: float in [0, inf], (optional))
    :type radius2: float
    :param depth: Depth
        (type: float in [0, inf], (optional))
    :type depth: float
    :param end_fill_type: Base Fill Type
        * 'NOTHING': Nothing, Don't fill at all.
        * 'NGON': Ngon, Use ngons.
        * 'TRIFAN': Triangle Fan, Use triangle fans.
        (type: enum in ['NOTHING', 'NGON', 'TRIFAN'], (optional))
    :type end_fill_type: str
    :param calc_uvs: Generate UVs, Generate a default UV map
        (type: boolean, (optional))
    :type calc_uvs: bool
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def primitive_cube_add(*args, radius=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Construct a cube mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param radius: Radius
        (type: float in [0, inf], (optional))
    :type radius: float
    :param calc_uvs: Generate UVs, Generate a default UV map
        (type: boolean, (optional))
    :type calc_uvs: bool
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def primitive_cylinder_add(*args, vertices=32, radius=1.0, depth=2.0, end_fill_type='NGON', calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Construct a cylinder mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param vertices: Vertices
        (type: int in [3, 10000000], (optional))
    :type vertices: int
    :param radius: Radius
        (type: float in [0, inf], (optional))
    :type radius: float
    :param depth: Depth
        (type: float in [0, inf], (optional))
    :type depth: float
    :param end_fill_type: Cap Fill Type
        * 'NOTHING': Nothing, Don't fill at all.
        * 'NGON': Ngon, Use ngons.
        * 'TRIFAN': Triangle Fan, Use triangle fans.
        (type: enum in ['NOTHING', 'NGON', 'TRIFAN'], (optional))
    :type end_fill_type: str
    :param calc_uvs: Generate UVs, Generate a default UV map
        (type: boolean, (optional))
    :type calc_uvs: bool
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def primitive_grid_add(*args, x_subdivisions=10, y_subdivisions=10, radius=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Construct a grid mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param x_subdivisions: X Subdivisions
        (type: int in [2, 10000000], (optional))
    :type x_subdivisions: int
    :param y_subdivisions: Y Subdivisions
        (type: int in [2, 10000000], (optional))
    :type y_subdivisions: int
    :param radius: Radius
        (type: float in [0, inf], (optional))
    :type radius: float
    :param calc_uvs: Generate UVs, Generate a default UV map
        (type: boolean, (optional))
    :type calc_uvs: bool
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def primitive_ico_sphere_add(*args, subdivisions=2, size=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Construct an Icosphere mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param subdivisions: Subdivisions
        (type: int in [1, 10], (optional))
    :type subdivisions: int
    :param size: Size
        (type: float in [0, inf], (optional))
    :type size: float
    :param calc_uvs: Generate UVs, Generate a default UV map
        (type: boolean, (optional))
    :type calc_uvs: bool
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def primitive_monkey_add(*args, radius=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Construct a Suzanne mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param radius: Radius
        (type: float in [0, inf], (optional))
    :type radius: float
    :param calc_uvs: Generate UVs, Generate a default UV map
        (type: boolean, (optional))
    :type calc_uvs: bool
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def primitive_plane_add(*args, radius=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Construct a filled planar mesh with 4 vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param radius: Radius
        (type: float in [0, inf], (optional))
    :type radius: float
    :param calc_uvs: Generate UVs, Generate a default UV map
        (type: boolean, (optional))
    :type calc_uvs: bool
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def primitive_torus_add(*args, view_align=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False), major_segments=48, minor_segments=12, mode='MAJOR_MINOR', major_radius=1.0, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75, generate_uvs=False):
    """Add a torus mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param view_align: Align to View
        (type: boolean, (optional))
    :type view_align: bool
    :param location: Location
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: mathutils.Vector
    :param rotation: Rotation
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layers
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :param major_segments: Major Segments, Number of segments for the main ring of the torus
        (type: int in [3, 256], (optional))
    :type major_segments: int
    :param minor_segments: Minor Segments, Number of segments for the minor ring of the torus
        (type: int in [3, 256], (optional))
    :type minor_segments: int
    :param mode: Torus Dimensions
        * 'MAJOR_MINOR': Major/Minor, Use the major/minor radii for torus dimensions.
        * 'EXT_INT': Exterior/Interior, Use the exterior/interior radii for torus dimensions.
        (type: enum in ['MAJOR_MINOR', 'EXT_INT'], (optional))
    :type mode: str
    :param major_radius: Major Radius, Radius from the origin to the center of the cross sections
        (type: float in [0.01, 100], (optional))
    :type major_radius: float
    :param minor_radius: Minor Radius, Radius of the torus' cross section
        (type: float in [0.01, 100], (optional))
    :type minor_radius: float
    :param abso_major_rad: Exterior Radius, Total Exterior Radius of the torus
        (type: float in [0.01, 100], (optional))
    :type abso_major_rad: float
    :param abso_minor_rad: Interior Radius, Total Interior Radius of the torus
        (type: float in [0.01, 100], (optional))
    :type abso_minor_rad: float
    :param generate_uvs: Generate UVs, Generate a default UV map
        (type: boolean, (optional))
    :type generate_uvs: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def primitive_uv_sphere_add(*args, segments=32, ring_count=16, size=1.0, calc_uvs=False, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Construct a UV sphere mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param segments: Segments
        (type: int in [3, 100000], (optional))
    :type segments: int
    :param ring_count: Rings
        (type: int in [3, 100000], (optional))
    :type ring_count: int
    :param size: Size
        (type: float in [0, inf], (optional))
    :type size: float
    :param calc_uvs: Generate UVs, Generate a default UV map
        (type: boolean, (optional))
    :type calc_uvs: bool
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def quads_convert_to_tris(*args, quad_method='BEAUTY', ngon_method='BEAUTY'):
    """Triangulate selected faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param quad_method: Quad Method, Method for splitting the quads into triangles
        * 'BEAUTY': Beauty , Split the quads in nice triangles, slower method.
        * 'FIXED': Fixed, Split the quads on the first and third vertices.
        * 'FIXED_ALTERNATE': Fixed Alternate, Split the quads on the 2nd and 4th vertices.
        * 'SHORTEST_DIAGONAL': Shortest Diagonal, Split the quads based on the distance between the vertices.
        (type: enum in ['BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL'], (optional))
    :type quad_method: str
    :param ngon_method: Polygon Method, Method for splitting the polygons into triangles
        * 'BEAUTY': Beauty, Arrange the new triangles evenly (slow).
        * 'CLIP': Clip, Split the polygons with an ear clipping algorithm.
        (type: enum in ['BEAUTY', 'CLIP'], (optional))
    :type ngon_method: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def region_to_loop(*args):
    """Select boundary edges around the selected faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def remove_doubles(*args, threshold=0.0001, use_unselected=False):
    """Remove duplicate vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param threshold: Merge Distance, Minimum distance between elements to merge
        (type: float in [1e-06, 50], (optional))
    :type threshold: float
    :param use_unselected: Unselected, Merge selected to other unselected vertices
        (type: boolean, (optional))
    :type use_unselected: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def reveal(*args):
    """Reveal all hidden vertices, edges and faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def rip(*args, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, release_confirm=False, use_accurate=False, use_fill=False):
    """Disconnect vertex or edges from connected geometry
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :param use_fill: Fill, Fill the ripped region
        (type: boolean, (optional))
    :type use_fill: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def rip_edge(*args, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, release_confirm=False, use_accurate=False):
    """Extend vertices along the edge closest to the cursor
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def rip_edge_move(*args, MESH_OT_rip_edge=None, TRANSFORM_OT_translate=None):
    """Extend vertices and move the result
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param MESH_OT_rip_edge: Extend Vertices, Extend vertices along the edge closest to the cursor
        (type: MESH_OT_rip_edge, (optional))
    :type MESH_OT_rip_edge: MESH_OT_rip_edge
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
        (type: TRANSFORM_OT_translate, (optional))
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def rip_move(*args, MESH_OT_rip=None, TRANSFORM_OT_translate=None):
    """Rip polygons and move the result
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param MESH_OT_rip: Rip, Disconnect vertex or edges from connected geometry
        (type: MESH_OT_rip, (optional))
    :type MESH_OT_rip: MESH_OT_rip
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
        (type: TRANSFORM_OT_translate, (optional))
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def rip_move_fill(*args, MESH_OT_rip=None, TRANSFORM_OT_translate=None):
    """Rip-fill polygons and move the result
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param MESH_OT_rip: Rip, Disconnect vertex or edges from connected geometry
        (type: MESH_OT_rip, (optional))
    :type MESH_OT_rip: MESH_OT_rip
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
        (type: TRANSFORM_OT_translate, (optional))
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def screw(*args, steps=9, turns=1, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0)):
    """Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param steps: Steps, Steps
        (type: int in [1, 100000], (optional))
    :type steps: int
    :param turns: Turns, Turns
        (type: int in [1, 100000], (optional))
    :type turns: int
    :param center: Center, Center in global view space
        (type: float array of 3 items in [-inf, inf], (optional))
    :type center: mathutils.Vector
    :param axis: Axis, Axis in global view space
        (type: float array of 3 items in [-1, 1], (optional))
    :type axis: mathutils.Vector
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_all(*args, action='TOGGLE'):
    """(De)select all vertices, edges or faces
    
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


def select_axis(*args, mode='POSITIVE', axis='X_AXIS', threshold=0.0001):
    """Select all data in the mesh on a single axis
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mode: Axis Mode, Axis side to use when selecting
        (type: enum in ['POSITIVE', 'NEGATIVE', 'ALIGNED'], (optional))
    :type mode: str
    :param axis: Axis, Select the axis to compare each vertex on
        (type: enum in ['X_AXIS', 'Y_AXIS', 'Z_AXIS'], (optional))
    :type axis: str
    :param threshold: Threshold
        (type: float in [1e-06, 50], (optional))
    :type threshold: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_face_by_sides(*args, number=4, type='EQUAL', extend=True):
    """Select vertices or faces by the number of polygon sides
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param number: Number of Vertices
        (type: int in [3, inf], (optional))
    :type number: int
    :param type: Type, Type of comparison to make
        (type: enum in ['LESS', 'EQUAL', 'GREATER', 'NOTEQUAL'], (optional))
    :type type: str
    :param extend: Extend, Extend the selection
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_interior_faces(*args):
    """Select faces where all edges have more than 2 face users
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_less(*args, use_face_step=True):
    """Deselect vertices, edges or faces at the boundary of each selection region
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_face_step: Face Step, Connected faces (instead of edges)
        (type: boolean, (optional))
    :type use_face_step: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_linked(*args, delimit={'SEAM'}):
    """Select all vertices linked to the active mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param delimit: Delimit, Delimit selected region
        * 'NORMAL': Normal, Delimit by face directions.
        * 'MATERIAL': Material, Delimit by face material.
        * 'SEAM': Seam, Delimit by edge seams.
        * 'SHARP': Sharp, Delimit by sharp edges.
        * 'UV': UVs, Delimit by UV coordinates.
        (type: enum set in {'NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV'}, (optional))
    :type delimit: enum set in {'NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV'}
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_linked_pick(*args, deselect=False, delimit={'SEAM'}, index=-1):
    """(De)select all vertices linked to the edge under the mouse cursor
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param deselect: Deselect
        (type: boolean, (optional))
    :type deselect: bool
    :param delimit: Delimit, Delimit selected region
        * 'NORMAL': Normal, Delimit by face directions.
        * 'MATERIAL': Material, Delimit by face material.
        * 'SEAM': Seam, Delimit by edge seams.
        * 'SHARP': Sharp, Delimit by sharp edges.
        * 'UV': UVs, Delimit by UV coordinates.
        (type: enum set in {'NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV'}, (optional))
    :type delimit: enum set in {'NORMAL', 'MATERIAL', 'SEAM', 'SHARP', 'UV'}
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_loose(*args, extend=False):
    """Select loose geometry based on the selection mode
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend the selection
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_mirror(*args, axis={'X'}, extend=False):
    """Select mesh items at mirrored locations
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param axis: Axis
        (type: enum set in {'X', 'Y', 'Z'}, (optional))
    :type axis: enum set in {'X', 'Y', 'Z'}
    :param extend: Extend, Extend the existing selection
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_mode(*args, use_extend=False, use_expand=False, type='VERT', action='TOGGLE'):
    """Change selection mode
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_extend: Extend
        (type: boolean, (optional))
    :type use_extend: bool
    :param use_expand: Expand
        (type: boolean, (optional))
    :type use_expand: bool
    :param type: Type
        (type: enum in ['VERT', 'EDGE', 'FACE'], (optional))
    :type type: str
    :param action: Action, Selection action to execute
        * 'DISABLE': Disable, Disable selected markers.
        * 'ENABLE': Enable, Enable selected markers.
        * 'TOGGLE': Toggle, Toggle disabled flag for selected markers.
        (type: enum in ['DISABLE', 'ENABLE', 'TOGGLE'], (optional))
    :type action: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_more(*args, use_face_step=True):
    """Select more vertices, edges or faces connected to initial selection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_face_step: Face Step, Connected faces (instead of edges)
        (type: boolean, (optional))
    :type use_face_step: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_next_item(*args):
    """Select the next element (using selection order)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_non_manifold(*args, extend=True, use_wire=True, use_boundary=True, use_multi_face=True, use_non_contiguous=True, use_verts=True):
    """Select all non-manifold vertices or edges
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend the selection
        (type: boolean, (optional))
    :type extend: bool
    :param use_wire: Wire, Wire edges
        (type: boolean, (optional))
    :type use_wire: bool
    :param use_boundary: Boundaries, Boundary edges
        (type: boolean, (optional))
    :type use_boundary: bool
    :param use_multi_face: Multiple Faces, Edges shared by 3+ faces
        (type: boolean, (optional))
    :type use_multi_face: bool
    :param use_non_contiguous: Non Contiguous, Edges between faces pointing in alternate directions
        (type: boolean, (optional))
    :type use_non_contiguous: bool
    :param use_verts: Vertices, Vertices connecting multiple face regions
        (type: boolean, (optional))
    :type use_verts: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_nth(*args, nth=2, skip=1, offset=0):
    """Deselect every Nth element starting from the active vertex, edge or face
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param nth: Nth Selection
        (type: int in [2, inf], (optional))
    :type nth: int
    :param skip: Skip
        (type: int in [1, inf], (optional))
    :type skip: int
    :param offset: Offset
        (type: int in [-inf, inf], (optional))
    :type offset: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_prev_item(*args):
    """Select the next element (using selection order)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_random(*args, percent=50.0, seed=0, action='SELECT'):
    """Randomly select vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param percent: Percent, Percentage of objects to select randomly
        (type: float in [0, 100], (optional))
    :type percent: float
    :param seed: Random Seed, Seed for the random number generator
        (type: int in [0, inf], (optional))
    :type seed: int
    :param action: Action, Selection action to execute
        * 'SELECT': Select, Select all elements.
        * 'DESELECT': Deselect, Deselect all elements.
        (type: enum in ['SELECT', 'DESELECT'], (optional))
    :type action: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_similar(*args, type='NORMAL', compare='EQUAL', threshold=0.0):
    """Select similar vertices, edges or faces by property types
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        (type: enum in ['NORMAL', 'FACE', 'VGROUP', 'EDGE', 'LENGTH', 'DIR', 'FACE', 'FACE_ANGLE', 'CREASE', 'BEVEL', 'SEAM', 'SHARP', 'FREESTYLE_EDGE', 'MATERIAL', 'IMAGE', 'AREA', 'SIDES', 'PERIMETER', 'NORMAL', 'COPLANAR', 'SMOOTH', 'FREESTYLE_FACE'], (optional))
    :type type: str
    :param compare: Compare
        (type: enum in ['EQUAL', 'GREATER', 'LESS'], (optional))
    :type compare: str
    :param threshold: Threshold
        (type: float in [0, 1], (optional))
    :type threshold: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_similar_region(*args):
    """Select similar face regions to the current selection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_ungrouped(*args, extend=False):
    """Select vertices without a group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend the selection
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def separate(*args, type='SELECTED'):
    """Separate selected geometry into a new mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        (type: enum in ['SELECTED', 'MATERIAL', 'LOOSE'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def set_normals_from_faces(*args):
    """Set the custom vertex normals from the selected faces ones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shape_propagate_to_all(*args):
    """Apply selected vertex locations to all other shape keys
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shortest_path_pick(*args, use_face_step=False, use_topology_distance=False, use_fill=False, nth=1, skip=1, offset=0, index=-1):
    """Select shortest path between two selections
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
        (type: boolean, (optional))
    :type use_face_step: bool
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
        (type: boolean, (optional))
    :type use_topology_distance: bool
    :param use_fill: Fill Region, Select all paths between the source/destination elements
        (type: boolean, (optional))
    :type use_fill: bool
    :param nth: Nth Selection
        (type: int in [1, inf], (optional))
    :type nth: int
    :param skip: Skip
        (type: int in [1, inf], (optional))
    :type skip: int
    :param offset: Offset
        (type: int in [-inf, inf], (optional))
    :type offset: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shortest_path_select(*args, use_face_step=False, use_topology_distance=False, use_fill=False, nth=1, skip=1, offset=0):
    """Selected vertex path between two vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
        (type: boolean, (optional))
    :type use_face_step: bool
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
        (type: boolean, (optional))
    :type use_topology_distance: bool
    :param use_fill: Fill Region, Select all paths between the source/destination elements
        (type: boolean, (optional))
    :type use_fill: bool
    :param nth: Nth Selection
        (type: int in [1, inf], (optional))
    :type nth: int
    :param skip: Skip
        (type: int in [1, inf], (optional))
    :type skip: int
    :param offset: Offset
        (type: int in [-inf, inf], (optional))
    :type offset: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def solidify(*args, thickness=0.01):
    """Create a solid skin by extruding, compensating for sharp angles
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param thickness: Thickness
        (type: float in [-10000, 10000], (optional))
    :type thickness: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def sort_elements(*args, type='VIEW_ZAXIS', elements={'VERT'}, reverse=False, seed=0):
    """The order of selected vertices/edges/faces is modified, based on a given method
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type, Type of re-ordering operation to apply
        * 'VIEW_ZAXIS': View Z Axis, Sort selected elements from farthest to nearest one in current view.
        * 'VIEW_XAXIS': View X Axis, Sort selected elements from left to right one in current view.
        * 'CURSOR_DISTANCE': Cursor Distance, Sort selected elements from nearest to farthest from 3D cursor.
        * 'MATERIAL': Material, Sort selected elements from smallest to greatest material index (faces only!).
        * 'SELECTED': Selected, Move all selected elements in first places, preserving their relative order (WARNING: this will affect unselected elements' indices as well!).
        * 'RANDOMIZE': Randomize, Randomize order of selected elements.
        * 'REVERSE': Reverse, Reverse current order of selected elements.
        (type: enum in ['VIEW_ZAXIS', 'VIEW_XAXIS', 'CURSOR_DISTANCE', 'MATERIAL', 'SELECTED', 'RANDOMIZE', 'REVERSE'], (optional))
    :type type: str
    :param elements: Elements, Which elements to affect (vertices, edges and/or faces)
        (type: enum set in {'VERT', 'EDGE', 'FACE'}, (optional))
    :type elements: enum set in {'VERT', 'EDGE', 'FACE'}
    :param reverse: Reverse, Reverse the sorting effect
        (type: boolean, (optional))
    :type reverse: bool
    :param seed: Seed, Seed for random-based operations
        (type: int in [0, inf], (optional))
    :type seed: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def spin(*args, steps=9, dupli=False, angle=1.5708, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0)):
    """Extrude selected vertices in a circle around the cursor in indicated viewport
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param steps: Steps, Steps
        (type: int in [0, 1000000], (optional))
    :type steps: int
    :param dupli: Dupli, Make Duplicates
        (type: boolean, (optional))
    :type dupli: bool
    :param angle: Angle, Rotation for each step
        (type: float in [-inf, inf], (optional))
    :type angle: float
    :param center: Center, Center in global view space
        (type: float array of 3 items in [-inf, inf], (optional))
    :type center: mathutils.Vector
    :param axis: Axis, Axis in global view space
        (type: float array of 3 items in [-1, 1], (optional))
    :type axis: mathutils.Vector
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def split(*args):
    """Split off selected geometry from connected unselected geometry
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def subdivide(*args, number_cuts=1, smoothness=0.0, quadtri=False, quadcorner='STRAIGHT_CUT', fractal=0.0, fractal_along_normal=0.0, seed=0):
    """Subdivide selected edges
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param number_cuts: Number of Cuts
        (type: int in [1, 100], (optional))
    :type number_cuts: int
    :param smoothness: Smoothness, Smoothness factor
        (type: float in [0, 1000], (optional))
    :type smoothness: float
    :param quadtri: Quad/Tri Mode, Tries to prevent ngons
        (type: boolean, (optional))
    :type quadtri: bool
    :param quadcorner: Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent ngons)
        (type: enum in ['INNERVERT', 'PATH', 'STRAIGHT_CUT', 'FAN'], (optional))
    :type quadcorner: str
    :param fractal: Fractal, Fractal randomness factor
        (type: float in [0, 1e+06], (optional))
    :type fractal: float
    :param fractal_along_normal: Along Normal, Apply fractal displacement along normal only
        (type: float in [0, 1], (optional))
    :type fractal_along_normal: float
    :param seed: Random Seed, Seed for the random number generator
        (type: int in [0, inf], (optional))
    :type seed: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def subdivide_edgering(*args, number_cuts=10, interpolation='PATH', smoothness=1.0, profile_shape_factor=0.0, profile_shape='SMOOTH'):
    """Undocumented
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param number_cuts: Number of Cuts
        (type: int in [0, 1000], (optional))
    :type number_cuts: int
    :param interpolation: Interpolation, Interpolation method
        (type: enum in ['LINEAR', 'PATH', 'SURFACE'], (optional))
    :type interpolation: str
    :param smoothness: Smoothness, Smoothness factor
        (type: float in [0, 1000], (optional))
    :type smoothness: float
    :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
        (type: float in [-1000, 1000], (optional))
    :type profile_shape_factor: float
    :param profile_shape: Profile Shape, Shape of the profile
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR'], (optional))
    :type profile_shape: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def symmetrize(*args, direction='NEGATIVE_X', threshold=0.0001):
    """Enforce symmetry (both form and topological) across an axis
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param direction: Direction, Which sides to copy from and to
        (type: enum in ['NEGATIVE_X', 'POSITIVE_X', 'NEGATIVE_Y', 'POSITIVE_Y', 'NEGATIVE_Z', 'POSITIVE_Z'], (optional))
    :type direction: str
    :param threshold: Threshold
        (type: float in [0, 10], (optional))
    :type threshold: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def symmetry_snap(*args, direction='NEGATIVE_X', threshold=0.05, factor=0.5, use_center=True):
    """Snap vertex pairs to their mirrored locations
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param direction: Direction, Which sides to copy from and to
        (type: enum in ['NEGATIVE_X', 'POSITIVE_X', 'NEGATIVE_Y', 'POSITIVE_Y', 'NEGATIVE_Z', 'POSITIVE_Z'], (optional))
    :type direction: str
    :param threshold: Threshold
        (type: float in [0, 10], (optional))
    :type threshold: float
    :param factor: Factor
        (type: float in [0, 1], (optional))
    :type factor: float
    :param use_center: Center, Snap mid verts to the axis center
        (type: boolean, (optional))
    :type use_center: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def tris_convert_to_quads(*args, face_threshold=0.698132, shape_threshold=0.698132, uvs=False, vcols=False, seam=False, sharp=False, materials=False):
    """Join triangles into quads
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param face_threshold: Max Face Angle, Face angle limit
        (type: float in [0, 3.14159], (optional))
    :type face_threshold: float
    :param shape_threshold: Max Shape Angle, Shape angle limit
        (type: float in [0, 3.14159], (optional))
    :type shape_threshold: float
    :param uvs: Compare UVs
        (type: boolean, (optional))
    :type uvs: bool
    :param vcols: Compare VCols
        (type: boolean, (optional))
    :type vcols: bool
    :param seam: Compare Seam
        (type: boolean, (optional))
    :type seam: bool
    :param sharp: Compare Sharp
        (type: boolean, (optional))
    :type sharp: bool
    :param materials: Compare Materials
        (type: boolean, (optional))
    :type materials: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def unsubdivide(*args, iterations=2):
    """UnSubdivide selected edges & faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param iterations: Iterations, Number of times to unsubdivide
        (type: int in [1, 1000], (optional))
    :type iterations: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def uv_texture_add(*args):
    """Add UV Map
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def uv_texture_remove(*args):
    """Remove UV Map
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def uvs_reverse(*args):
    """Flip direction of UV coordinates inside faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def uvs_rotate(*args, use_ccw=False):
    """Rotate UV coordinates inside faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_ccw: Counter Clockwise
        (type: boolean, (optional))
    :type use_ccw: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vert_connect(*args):
    """Connect selected vertices of faces, splitting the face
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vert_connect_concave(*args):
    """Make all faces convex
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vert_connect_nonplanar(*args, angle_limit=0.0872665):
    """Split non-planar faces that exceed the angle threshold
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param angle_limit: Max Angle, Angle limit
        (type: float in [0, 3.14159], (optional))
    :type angle_limit: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vert_connect_path(*args):
    """Connect vertices by their selection order, creating edges, splitting faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_color_add(*args):
    """Add vertex color layer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_color_remove(*args):
    """Remove vertex color layer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertices_smooth(*args, factor=0.5, repeat=1, xaxis=True, yaxis=True, zaxis=True):
    """Flatten angles of selected vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param factor: Smoothing, Smoothing factor
        (type: float in [-10, 10], (optional))
    :type factor: float
    :param repeat: Repeat, Number of times to smooth the mesh
        (type: int in [1, 1000], (optional))
    :type repeat: int
    :param xaxis: X-Axis, Smooth along the X axis
        (type: boolean, (optional))
    :type xaxis: bool
    :param yaxis: Y-Axis, Smooth along the Y axis
        (type: boolean, (optional))
    :type yaxis: bool
    :param zaxis: Z-Axis, Smooth along the Z axis
        (type: boolean, (optional))
    :type zaxis: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertices_smooth_laplacian(*args, repeat=1, lambda_factor=5e-05, lambda_border=5e-05, use_x=True, use_y=True, use_z=True, preserve_volume=True):
    """Laplacian smooth of selected vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param repeat: Number of iterations to smooth the mesh
        (type: int in [1, 1000], (optional))
    :type repeat: int
    :param lambda_factor: Lambda factor
        (type: float in [1e-07, 1000], (optional))
    :type lambda_factor: float
    :param lambda_border: Lambda factor in border
        (type: float in [1e-07, 1000], (optional))
    :type lambda_border: float
    :param use_x: Smooth X Axis, Smooth object along X axis
        (type: boolean, (optional))
    :type use_x: bool
    :param use_y: Smooth Y Axis, Smooth object along Y axis
        (type: boolean, (optional))
    :type use_y: bool
    :param use_z: Smooth Z Axis, Smooth object along Z axis
        (type: boolean, (optional))
    :type use_z: bool
    :param preserve_volume: Preserve Volume, Apply volume preservation after smooth
        (type: boolean, (optional))
    :type preserve_volume: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def wireframe(*args, use_boundary=True, use_even_offset=True, use_relative_offset=False, use_replace=True, thickness=0.01, offset=0.01, use_crease=False, crease_weight=0.01):
    """Create a solid wire-frame from faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_boundary: Boundary, Inset face boundaries
        (type: boolean, (optional))
    :type use_boundary: bool
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
        (type: boolean, (optional))
    :type use_even_offset: bool
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
        (type: boolean, (optional))
    :type use_relative_offset: bool
    :param use_replace: Replace, Remove original faces
        (type: boolean, (optional))
    :type use_replace: bool
    :param thickness: Thickness
        (type: float in [0, 10000], (optional))
    :type thickness: float
    :param offset: Offset
        (type: float in [0, 10000], (optional))
    :type offset: float
    :param use_crease: Crease, Crease hub edges for improved subsurf
        (type: boolean, (optional))
    :type use_crease: bool
    :param crease_weight: Crease weight
        (type: float in [0, 1000], (optional))
    :type crease_weight: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
