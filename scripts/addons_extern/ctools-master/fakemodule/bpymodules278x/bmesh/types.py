class BMesh:
    """The BMesh data structure"""

    def calc_tessellation(self):
        """Calc tessellation (use BMEdit_RecalcTessellation())."""

    def calc_tessface(self):
        """Calculate triangle tessellation from quads/ngons.
        
        :return: The triangulated faces.
        :param : (type: list of bmesh.types.BMLoop tuples)
        :rtype: list
        """

    def calc_volume(self, signed=False):
        """Calculate mesh volume based on face normals.
        
        :param signed: when signed is true, negative values may be returned.
        :type signed: bool
        :return: The volume of the mesh.
        :rtype: float
        """

    def clear(self):
        """Clear all mesh data."""

    def copy(self):
        """
        :return: A copy of this BMesh.
        :param : (type: bmesh.types.BMesh)
        :rtype: BMesh
        """

    def free(self):
        """Explicitly free the BMesh data from memory, causing exceptions on further access.
        <Note> The BMesh is freed automatically, typically when the script finishes executing.
                                                However in some cases its hard to predict when this will be and its useful to
                                                explicitly free the data.
        """

    def from_mesh(self, mesh, face_normals=True, use_shape_key=False, shape_key_index=0):
        """Initialize this bmesh from existing mesh datablock.
        
        :param mesh: The mesh data to load.
        :type mesh: Mesh
        :param use_shape_key: Use the locations from a shape key.
        :type use_shape_key: bool
        :param shape_key_index: The shape key index to use.
        :type shape_key_index: int
        """

    def from_object(self, object, scene, deform=True, render=False, cage=False, face_normals=True):
        """Initialize this bmesh from existing object datablock (currently only meshes are supported).
        
        :param object: The object data to load.
        :type object: Object
        :param deform: Apply deformation modifiers.
        :type deform: bool
        :param render: Use render settings.
        :type render: bool
        :param cage: Get the mesh as a deformed cage.
        :type cage: bool
        :param face_normals: Calculate face normals.
        :type face_normals: bool
        """

    def normal_update(self):
        """Update mesh normals."""

    def select_flush(self, select):
        """Flush selection, independent of the current selection mode.
        
        :param select: flush selection or de-selected elements.
        :type select: bool
        """

    def select_flush_mode(self):
        """flush selection based on the current mode current bmesh.types.BMesh.select_mode."""

    def to_mesh(self, mesh):
        """Writes this BMesh data into an existing Mesh datablock.
        
        :param mesh: The mesh data to write into.
        :type mesh: Mesh
        """

    def transform(self, matrix, filter=None):
        """Transform the mesh (optionally filtering flagged data only).
        
        :param matrix: transform matrix.
        :type matrix: 4x4 mathutils.Matrix
        :param filter: set of values in ('SELECT', 'HIDE', 'SEAM', 'SMOOTH', 'TAG').
        :type filter: set
        """

    edges = None
    """This meshes edge sequence (read-only).
    (type: bmesh.types.BMEdgeSeq)
    
    :type: BMEdgeSeq
    """

    faces = None
    """This meshes face sequence (read-only).
    (type: bmesh.types.BMFaceSeq)
    
    :type: BMFaceSeq
    """

    is_valid = None
    """True when this element is valid (hasn't been removed).
    
    :type: bool
    """

    is_wrapped = None
    """True when this mesh is owned by blender (typically the editmode BMesh).
    
    :type: bool
    """

    loops = None
    """This meshes loops (read-only).
    (type: bmesh.types.BMLoopSeq)
    
    :type: BMLoopSeq
    """

    select_history = None
    """Sequence of selected items (the last is displayed as active).
    (type: bmesh.types.BMEditSelSeq)
    
    :type: BMEditSelSeq
    """

    select_mode = None
    """The selection mode, values can be {'VERT', 'EDGE', 'FACE'}, can't be assigned an empty set.
    
    :type: set
    """

    verts = None
    """This meshes vert sequence (read-only).
    (type: bmesh.types.BMVertSeq)
    
    :type: BMVertSeq
    """


class BMVert:
    """The BMesh vertex type"""

    def calc_edge_angle(self, fallback=None):
        """Return the angle between this vert's two connected edges.
        
        :param fallback: return this when the vert doesn't have 2 edges
                                                        (instead of raising a ValueError).
        :type fallback: bpy.types.KeyMapItem.any
        :return: Angle between edges in radians.
        :rtype: float
        """

    def calc_shell_factor(self):
        """Return a multiplier calculated based on the sharpness of the vertex.
                                        Where a flat surface gives 1.0, and higher values sharper edges.
                                        This is used to maintain shell thickness when offsetting verts along their normals.
        
        :return: offset multiplier
        :rtype: float
        """

    def copy_from(self, other):
        """Copy values from another element of matching type."""

    def copy_from_face_interp(self, face):
        """Interpolate the customdata from a face onto this loop (the loops vert should overlap the face).
        
        :param face: The face to interpolate data from.
            (type: bmesh.types.BMFace)
        :type face: BMFace
        """

    def copy_from_vert_interp(self, vert_pair, fac):
        """Interpolate the customdata from a vert between 2 other verts.
        
        :param vert_pair: The vert to interpolate data from.
            (type: bmesh.types.BMVert)
        :type vert_pair: BMVert
        """

    def hide_set(self, hide):
        """Set the hide state.
                                        This is different from the hide attribute because it updates the selection and hide state of associated geometry.
        
        :param hide: Hidden or visible.
        :type hide: bool
        """

    def normal_update(self):
        """Update vertex normal."""

    def select_set(self, select):
        """Set the selection.
                                        This is different from the select attribute because it updates the selection state of associated geometry.
        <Note> Currently this only flushes down, so selecting a face will select all its vertices but de-selecting a vertex       won't de-select all the faces that use it, before finishing with a mesh typically flushing is still needed.
        
        :param select: Select or de-select.
        :type select: bool
        """

    co = None
    """The coordinates for this vertex as a 3D, wrapped vector.
    
    :type: mathutils.Vector
    """

    hide = None
    """Hidden state of this element.
    
    :type: bool
    """

    index = None
    """Index of this element.
    
    :type: int
    """

    is_boundary = None
    """True when this vertex is connected to boundary edges (read-only).
    
    :type: bool
    """

    is_manifold = None
    """True when this vertex is manifold (read-only).
    
    :type: bool
    """

    is_valid = None
    """True when this element is valid (hasn't been removed).
    
    :type: bool
    """

    is_wire = None
    """True when this vertex is not connected to any faces (read-only).
    
    :type: bool
    """

    link_edges = None
    """Edges connected to this vertex (read-only).
    (type: bmesh.types.BMElemSeq of bmesh.types.BMEdge)
    
    :type: BMElemSeq
    """

    link_faces = None
    """Faces connected to this vertex (read-only).
    (type: bmesh.types.BMElemSeq of bmesh.types.BMFace)
    
    :type: BMElemSeq
    """

    link_loops = None
    """Loops that use this vertex (read-only).
    (type: bmesh.types.BMElemSeq of bmesh.types.BMLoop)
    
    :type: BMElemSeq
    """

    normal = None
    """The normal for this vertex as a 3D, wrapped vector.
    
    :type: mathutils.Vector
    """

    select = None
    """Selected state of this element.
    
    :type: bool
    """

    tag = None
    """Generic attribute scripts can use for own logic
    
    :type: bool
    """


class BMEdge:
    """The BMesh edge connecting 2 verts"""

    def calc_face_angle(self, fallback=None):
        """
        :param fallback: return this when the edge doesn't have 2 faces
                                                        (instead of raising a ValueError).
        :type fallback: bpy.types.KeyMapItem.any
        :return: The angle between 2 connected faces in radians.
        :rtype: float
        """

    def calc_face_angle_signed(self, fallback=None):
        """
        :param fallback: return this when the edge doesn't have 2 faces
                                                        (instead of raising a ValueError).
        :type fallback: bpy.types.KeyMapItem.any
        :return: The angle between 2 connected faces in radians (negative for concave join).
        :rtype: float
        """

    def calc_length(self):
        """
        :return: The length between both verts.
        :rtype: float
        """

    def calc_tangent(self, loop):
        """Return the tangent at this edge relative to a face (pointing inward into the face).
                                        This uses the face normal for calculation.
        
        :param loop: The loop used for tangent calculation.
            (type: bmesh.types.BMLoop)
        :type loop: BMLoop
        :return: a normalized vector.
        :rtype: mathutils.Vector
        """

    def copy_from(self, other):
        """Copy values from another element of matching type."""

    def hide_set(self, hide):
        """Set the hide state.
                                        This is different from the hide attribute because it updates the selection and hide state of associated geometry.
        
        :param hide: Hidden or visible.
        :type hide: bool
        """

    def normal_update(self):
        """Update edges vertex normals."""

    def other_vert(self, vert):
        """Return the other vertex on this edge or None if the vertex is not used by this edge.
        
        :param vert: a vert in this edge.
            (type: bmesh.types.BMVert)
        :type vert: BMVert
        :return: The edges other vert.
        :param : (type: bmesh.types.BMVert or None)
        :rtype: BMVert or None
        """

    def select_set(self, select):
        """Set the selection.
                                        This is different from the select attribute because it updates the selection state of associated geometry.
        <Note> Currently this only flushes down, so selecting a face will select all its vertices but de-selecting a vertex       won't de-select all the faces that use it, before finishing with a mesh typically flushing is still needed.
        
        :param select: Select or de-select.
        :type select: bool
        """

    hide = None
    """Hidden state of this element.
    
    :type: bool
    """

    index = None
    """Index of this element.
    
    :type: int
    """

    is_boundary = None
    """True when this edge is at the boundary of a face (read-only).
    
    :type: bool
    """

    is_contiguous = None
    """True when this edge is manifold, between two faces with the same winding (read-only).
    
    :type: bool
    """

    is_convex = None
    """True when this edge joins two convex faces, depends on a valid face normal (read-only).
    
    :type: bool
    """

    is_manifold = None
    """True when this edge is manifold (read-only).
    
    :type: bool
    """

    is_valid = None
    """True when this element is valid (hasn't been removed).
    
    :type: bool
    """

    is_wire = None
    """True when this edge is not connected to any faces (read-only).
    
    :type: bool
    """

    link_faces = None
    """Faces connected to this edge, (read-only).
    (type: bmesh.types.BMElemSeq of bmesh.types.BMFace)
    
    :type: BMElemSeq
    """

    link_loops = None
    """Loops connected to this edge, (read-only).
    (type: bmesh.types.BMElemSeq of bmesh.types.BMLoop)
    
    :type: BMElemSeq
    """

    seam = None
    """Seam for UV unwrapping.
    
    :type: bool
    """

    select = None
    """Selected state of this element.
    
    :type: bool
    """

    smooth = None
    """Smooth state of this element.
    
    :type: bool
    """

    tag = None
    """Generic attribute scripts can use for own logic
    
    :type: bool
    """

    verts = None
    """Verts this edge uses (always 2), (read-only).
    (type: bmesh.types.BMElemSeq of bmesh.types.BMVert)
    
    :type: BMElemSeq
    """


class BMFace:
    """The BMesh face with 3 or more sides"""

    def calc_area(self):
        """Return the area of the face.
        
        :return: Return the area of the face.
        :rtype: float
        """

    def calc_center_bounds(self):
        """Return bounds center of the face.
        
        :return: a 3D vector.
        :rtype: mathutils.Vector
        """

    def calc_center_median(self):
        """Return median center of the face.
        
        :return: a 3D vector.
        :rtype: mathutils.Vector
        """

    def calc_center_median_weighted(self):
        """Return median center of the face weighted by edge lengths.
        
        :return: a 3D vector.
        :rtype: mathutils.Vector
        """

    def calc_perimeter(self):
        """Return the perimeter of the face.
        
        :return: Return the perimeter of the face.
        :rtype: float
        """

    def calc_tangent_edge(self):
        """Return face tangent based on longest edge.
        
        :return: a normalized vector.
        :rtype: mathutils.Vector
        """

    def calc_tangent_edge_diagonal(self):
        """Return face tangent based on the edge farthest from any vertex.
        
        :return: a normalized vector.
        :rtype: mathutils.Vector
        """

    def calc_tangent_edge_pair(self):
        """Return face tangent based on the two longest disconnected edges.
        - Tris: Use the edge pair with the most similar lengths.
        - Quads: Use the longest edge pair.
        - NGons: Use the two longest disconnected edges.
        
        :return: a normalized vector.
        :rtype: mathutils.Vector
        """

    def calc_tangent_vert_diagonal(self):
        """Return face tangent based on the two most distent vertices.
        
        :return: a normalized vector.
        :rtype: mathutils.Vector
        """

    def copy(self, verts=True, edges=True):
        """Make a copy of this face.
        
        :param verts: When set, the faces verts will be duplicated too.
        :type verts: bool
        :param edges: When set, the faces edges will be duplicated too.
        :type edges: bool
        :return: The newly created face.
        :param : (type: bmesh.types.BMFace)
        :rtype: BMFace
        """

    def copy_from(self, other):
        """Copy values from another element of matching type."""

    def copy_from_face_interp(self, face, vert=True):
        """Interpolate the customdata from another face onto this one (faces should overlap).
        
        :param face: The face to interpolate data from.
            (type: bmesh.types.BMFace)
        :type face: BMFace
        :param vert: When True, also copy vertex data.
        :type vert: bool
        """

    def hide_set(self, hide):
        """Set the hide state.
                                        This is different from the hide attribute because it updates the selection and hide state of associated geometry.
        
        :param hide: Hidden or visible.
        :type hide: bool
        """

    def normal_flip(self):
        """Reverses winding of a face, which flips its normal."""

    def normal_update(self):
        """Update face's normal."""

    def select_set(self, select):
        """Set the selection.
                                        This is different from the select attribute because it updates the selection state of associated geometry.
        <Note> Currently this only flushes down, so selecting a face will select all its vertices but de-selecting a vertex       won't de-select all the faces that use it, before finishing with a mesh typically flushing is still needed.
        
        :param select: Select or de-select.
        :type select: bool
        """

    edges = None
    """Edges of this face, (read-only).
    (type: bmesh.types.BMElemSeq of bmesh.types.BMEdge)
    
    :type: BMElemSeq
    """

    hide = None
    """Hidden state of this element.
    
    :type: bool
    """

    index = None
    """Index of this element.
    
    :type: int
    """

    is_valid = None
    """True when this element is valid (hasn't been removed).
    
    :type: bool
    """

    loops = None
    """Loops of this face, (read-only).
    (type: bmesh.types.BMElemSeq of bmesh.types.BMLoop)
    
    :type: BMElemSeq
    """

    material_index = None
    """The face's material index.
    
    :type: int
    """

    normal = None
    """The normal for this face as a 3D, wrapped vector.
    
    :type: mathutils.Vector
    """

    select = None
    """Selected state of this element.
    
    :type: bool
    """

    smooth = None
    """Smooth state of this element.
    
    :type: bool
    """

    tag = None
    """Generic attribute scripts can use for own logic
    
    :type: bool
    """

    verts = None
    """Verts of this face, (read-only).
    (type: bmesh.types.BMElemSeq of bmesh.types.BMVert)
    
    :type: BMElemSeq
    """


class BMLoop:
    """This is normally accessed from bmesh.types.BMFace.loops where each face loop represents a corner of the face."""

    def calc_angle(self):
        """Return the angle at this loops corner of the face.
                                        This is calculated so sharper corners give lower angles.
        
        :return: The angle in radians.
        :rtype: float
        """

    def calc_normal(self):
        """Return normal at this loops corner of the face.
                                        Falls back to the face normal for straight lines.
        
        :return: a normalized vector.
        :rtype: mathutils.Vector
        """

    def calc_tangent(self):
        """Return the tangent at this loops corner of the face (pointing inward into the face).
                                        Falls back to the face normal for straight lines.
        
        :return: a normalized vector.
        :rtype: mathutils.Vector
        """

    def copy_from(self, other):
        """Copy values from another element of matching type."""

    def copy_from_face_interp(self, face, vert=True, multires=True):
        """Interpolate the customdata from a face onto this loop (the loops vert should overlap the face).
        
        :param face: The face to interpolate data from.
            (type: bmesh.types.BMFace)
        :type face: BMFace
        :param vert: When enabled, interpolate the loops vertex data (optional).
        :type vert: bool
        :param multires: When enabled, interpolate the loops multires data (optional).
        :type multires: bool
        """

    edge = None
    """The loop's edge (between this loop and the next), (read-only).
    (type: bmesh.types.BMEdge)
    
    :type: BMEdge
    """

    face = None
    """The face this loop makes (read-only).
    (type: bmesh.types.BMFace)
    
    :type: BMFace
    """

    index = None
    """Index of this element.
    
    :type: int
    """

    is_convex = None
    """True when this loop is at the convex corner of a face, depends on a valid face normal (read-only).
    
    :type: bool
    """

    is_valid = None
    """True when this element is valid (hasn't been removed).
    
    :type: bool
    """

    link_loop_next = None
    """The next face corner (read-only).
    (type: bmesh.types.BMLoop)
    
    :type: BMLoop
    """

    link_loop_prev = None
    """The previous face corner (read-only).
    (type: bmesh.types.BMLoop)
    
    :type: BMLoop
    """

    link_loop_radial_next = None
    """The next loop around the edge (read-only).
    (type: bmesh.types.BMLoop)
    
    :type: BMLoop
    """

    link_loop_radial_prev = None
    """The previous loop around the edge (read-only).
    (type: bmesh.types.BMLoop)
    
    :type: BMLoop
    """

    link_loops = None
    """Loops connected to this loop, (read-only).
    (type: bmesh.types.BMElemSeq of bmesh.types.BMLoop)
    
    :type: BMElemSeq
    """

    tag = None
    """Generic attribute scripts can use for own logic
    
    :type: bool
    """

    vert = None
    """The loop's vertex (read-only).
    (type: bmesh.types.BMVert)
    
    :type: BMVert
    """


class BMElemSeq:
    """General sequence type used for accessing any sequence of
                            bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace, bmesh.types.BMLoop.
    When accessed via bmesh.types.BMesh.verts, bmesh.types.BMesh.edges, bmesh.types.BMesh.faces
                            there are also functions to create/remomove items.
    """

    def index_update(self):
        """Initialize the index values of this sequence.
        This is the equivalent of looping over all elements and assigning the index values.
        <Note> Running this on sequences besides bmesh.types.BMesh.verts, bmesh.types.BMesh.edges, bmesh.types.BMesh.faces
                                                works but wont result in each element having a valid index, insted its order in the sequence will be set.
        """


class BMVertSeq:
    """"""

    def ensure_lookup_table(self):
        """Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg bm.verts[index].
        This needs to be called again after adding/removing data in this sequence.
        """

    def index_update(self):
        """Initialize the index values of this sequence.
        This is the equivalent of looping over all elements and assigning the index values.
        <Note> Running this on sequences besides bmesh.types.BMesh.verts, bmesh.types.BMesh.edges, bmesh.types.BMesh.faces
                                                works but wont result in each element having a valid index, insted its order in the sequence will be set.
        """

    def new(self, co=(0.0, 0.0, 0.0), example=None):
        """Create a new vertex.
        
        :param co: The initial location of the vertex (optional argument).
        :type co: float triplet
        :param example: Existing vert to initialize settings.
            (type: bmesh.types.BMVert)
        :type example: BMVert
        :return: The newly created edge.
        :param : (type: bmesh.types.BMVert)
        :rtype: BMVert
        """

    def remove(self, vert):
        """Remove a vert."""

    def sort(self, key=None, reverse=False):
        """Sort the elements of this sequence, using an optional custom sort key.
                                        Indices of elements are not changed, BMElemeSeq.index_update() can be used for that.
        <Note> When the 'key' argument is not provided, the elements are reordered following their current index value.
                                                In particular this can be used by setting indices manually before calling this method.
        
        :param key: The key that sets the ordering of the elements.
        :param reverse: Reverse the order of the elements
        """

    layers = None
    """custom-data layers (read-only).
    (type: bmesh.types.BMLayerAccessVert)
    
    :type: BMLayerAccessVert
    """


class BMEdgeSeq:
    """"""

    def ensure_lookup_table(self):
        """Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg bm.verts[index].
        This needs to be called again after adding/removing data in this sequence.
        """

    def get(self, verts, fallback=None):
        """Return an edge which uses the verts passed.
        
        :param verts: Sequence of verts.
            (type: bmesh.types.BMVert)
        :type verts: BMVert
        :param fallback: Return this value if nothing is found.
        :return: The edge found or None
        :param : (type: bmesh.types.BMEdge)
        :rtype: BMEdge
        """

    def index_update(self):
        """Initialize the index values of this sequence.
        This is the equivalent of looping over all elements and assigning the index values.
        <Note> Running this on sequences besides bmesh.types.BMesh.verts, bmesh.types.BMesh.edges, bmesh.types.BMesh.faces
                                                works but wont result in each element having a valid index, insted its order in the sequence will be set.
        """

    def new(self, verts, example=None):
        """Create a new edge from a given pair of verts.
        
        :param verts: Vertex pair.
            (type: pair of bmesh.types.BMVert)
        :type verts: pair
        :param example: Existing edge to initialize settings (optional argument).
            (type: bmesh.types.BMEdge)
        :type example: BMEdge
        :return: The newly created edge.
        :param : (type: bmesh.types.BMEdge)
        :rtype: BMEdge
        """

    def remove(self, edge):
        """Remove an edge."""

    def sort(self, key=None, reverse=False):
        """Sort the elements of this sequence, using an optional custom sort key.
                                        Indices of elements are not changed, BMElemeSeq.index_update() can be used for that.
        <Note> When the 'key' argument is not provided, the elements are reordered following their current index value.
                                                In particular this can be used by setting indices manually before calling this method.
        
        :param key: The key that sets the ordering of the elements.
        :param reverse: Reverse the order of the elements
        """

    layers = None
    """custom-data layers (read-only).
    (type: bmesh.types.BMLayerAccessEdge)
    
    :type: BMLayerAccessEdge
    """


class BMFaceSeq:
    """"""

    def ensure_lookup_table(self):
        """Ensure internal data needed for int subscription is initialized with verts/edges/faces, eg bm.verts[index].
        This needs to be called again after adding/removing data in this sequence.
        """

    def get(self, verts, fallback=None):
        """Return a face which uses the verts passed.
        
        :param verts: Sequence of verts.
            (type: bmesh.types.BMVert)
        :type verts: BMVert
        :param fallback: Return this value if nothing is found.
        :return: The face found or None
        :param : (type: bmesh.types.BMFace)
        :rtype: BMFace
        """

    def index_update(self):
        """Initialize the index values of this sequence.
        This is the equivalent of looping over all elements and assigning the index values.
        <Note> Running this on sequences besides bmesh.types.BMesh.verts, bmesh.types.BMesh.edges, bmesh.types.BMesh.faces
                                                works but wont result in each element having a valid index, insted its order in the sequence will be set.
        """

    def new(self, verts, example=None):
        """Create a new face from a given set of verts.
        
        :param verts: Sequence of 3 or more verts.
            (type: bmesh.types.BMVert)
        :type verts: BMVert
        :param example: Existing face to initialize settings (optional argument).
            (type: bmesh.types.BMFace)
        :type example: BMFace
        :return: The newly created face.
        :param : (type: bmesh.types.BMFace)
        :rtype: BMFace
        """

    def remove(self, face):
        """Remove a face."""

    def sort(self, key=None, reverse=False):
        """Sort the elements of this sequence, using an optional custom sort key.
                                        Indices of elements are not changed, BMElemeSeq.index_update() can be used for that.
        <Note> When the 'key' argument is not provided, the elements are reordered following their current index value.
                                                In particular this can be used by setting indices manually before calling this method.
        
        :param key: The key that sets the ordering of the elements.
        :param reverse: Reverse the order of the elements
        """

    active = None
    """active face.
    (type: bmesh.types.BMFace or None)
    
    :type: BMFace or None
    """

    layers = None
    """custom-data layers (read-only).
    (type: bmesh.types.BMLayerAccessFace)
    
    :type: BMLayerAccessFace
    """


class BMLoopSeq:
    """"""

    layers = None
    """custom-data layers (read-only).
    (type: bmesh.types.BMLayerAccessLoop)
    
    :type: BMLayerAccessLoop
    """


class BMIter:
    """Internal BMesh type for looping over verts/faces/edges,
                            used for iterating over bmesh.types.BMElemSeq types.
    """


class BMEditSelSeq:
    """"""

    def add(self, element):
        """Add an element to the selection history (no action taken if its already added)."""

    def clear(self):
        """Empties the selection history."""

    def discard(self, element):
        """Discard an element from the selection history.
        Like remove but doesn't raise an error when the elements not in the selection list.
        """

    def remove(self, element):
        """Remove an element from the selection history."""

    def validate(self):
        """Ensures all elements in the selection history are selected."""

    active = None
    """The last selected element or None (read-only).
    (type: bmesh.types.BMVert, bmesh.types.BMEdge or bmesh.types.BMFace)
    
    :type: BMVert, BMEdge or BMFace
    """


class BMEditSelIter:
    """"""


class BMLayerAccessVert:
    """Exposes custom-data layer attributes."""

    bevel_weight = None
    """Bevel weight float in [0 - 1].
    (type: bmesh.types.BMLayerCollection)
    
    :type: BMLayerCollection
    """

    deform = None
    """Vertex deform weight bmesh.types.BMDeformVert (TODO).
    type: bmesh.types.BMLayerCollection
    """

    float = None
    """Generic float custom-data layer.
    type: bmesh.types.BMLayerCollection
    """

    int = None
    """Generic int custom-data layer.
    type: bmesh.types.BMLayerCollection
    """

    paint_mask = None
    """Accessor for paint mask layer.
    type: bmesh.types.BMLayerCollection
    """

    shape = None
    """Vertex shapekey absolute location (as a 3D Vector).
    (type: bmesh.types.BMLayerCollection)
    
    :type: BMLayerCollection
    """

    skin = None
    """Accessor for skin layer.
    type: bmesh.types.BMLayerCollection
    """

    string = None
    """Generic string custom-data layer (exposed as bytes, 255 max length).
    type: bmesh.types.BMLayerCollection
    """


class BMLayerAccessEdge:
    """Exposes custom-data layer attributes."""

    bevel_weight = None
    """Bevel weight float in [0 - 1].
    (type: bmesh.types.BMLayerCollection)
    
    :type: BMLayerCollection
    """

    crease = None
    """Edge crease for subsurf - float in [0 - 1].
    (type: bmesh.types.BMLayerCollection)
    
    :type: BMLayerCollection
    """

    float = None
    """Generic float custom-data layer.
    type: bmesh.types.BMLayerCollection
    """

    freestyle = None
    """Accessor for Freestyle edge layer.
    type: bmesh.types.BMLayerCollection
    """

    int = None
    """Generic int custom-data layer.
    type: bmesh.types.BMLayerCollection
    """

    string = None
    """Generic string custom-data layer (exposed as bytes, 255 max length).
    type: bmesh.types.BMLayerCollection
    """


class BMLayerAccessFace:
    """Exposes custom-data layer attributes."""

    float = None
    """Generic float custom-data layer.
    type: bmesh.types.BMLayerCollection
    """

    freestyle = None
    """Accessor for Freestyle face layer.
    type: bmesh.types.BMLayerCollection
    """

    int = None
    """Generic int custom-data layer.
    type: bmesh.types.BMLayerCollection
    """

    string = None
    """Generic string custom-data layer (exposed as bytes, 255 max length).
    type: bmesh.types.BMLayerCollection
    """

    tex = None
    """Accessor for BMTexPoly layer (TODO).
    type: bmesh.types.BMLayerCollection
    """


class BMLayerAccessLoop:
    """Exposes custom-data layer attributes."""

    color = None
    """Accessor for vertex color layer.
    type: bmesh.types.BMLayerCollection
    """

    float = None
    """Generic float custom-data layer.
    type: bmesh.types.BMLayerCollection
    """

    int = None
    """Generic int custom-data layer.
    type: bmesh.types.BMLayerCollection
    """

    string = None
    """Generic string custom-data layer (exposed as bytes, 255 max length).
    type: bmesh.types.BMLayerCollection
    """

    uv = None
    """Accessor for bmesh.types.BMLoopUV UV (as a 2D Vector).
    type: bmesh.types.BMLayerCollection
    """


class BMLayerCollection:
    """Gives access to a collection of custom-data layers of the same type and behaves like python dictionaries, except for the ability to do list like index access."""

    def get(self, key, default=None):
        """Returns the value of the layer matching the key or default
                                        when not found (matches pythons dictionary function of the same name).
        
        :param key: The key associated with the layer.
        :type key: str
        :param default: Optional argument for the value to return if
                                                                key is not found.
        :type default: Undefined
        """

    def items(self):
        """Return the identifiers of collection members
                                        (matching pythons dict.items() functionality).
        
        :return: (key, value) pairs for each member of this collection.
        :param : (type: list of tuples)
        :rtype: list
        """

    def keys(self):
        """Return the identifiers of collection members
                                        (matching pythons dict.keys() functionality).
        
        :return: the identifiers for each member of this collection.
        :param : (type: list of strings)
        :rtype: list
        """

    def new(self, name):
        """Create a new layer
        
        :param name: Optional name argument (will be made unique).
        :type name: str
        :return: The newly created layer.
        :param : (type: bmesh.types.BMLayerItem)
        :rtype: BMLayerItem
        """

    def remove(self, layer):
        """Remove a layer
        
        :param layer: The layer to remove.
            (type: bmesh.types.BMLayerItem)
        :type layer: BMLayerItem
        """

    def values(self):
        """Return the values of collection
                                        (matching pythons dict.values() functionality).
        
        :return: the members of this collection.
        :rtype: list
        """

    def verify(self):
        """Create a new layer or return an existing active layer
        
        :return: The newly verified layer.
        :param : (type: bmesh.types.BMLayerItem)
        :rtype: BMLayerItem
        """

    active = None
    """The active layer of this type (read-only).
    (type: bmesh.types.BMLayerItem)
    
    :type: BMLayerItem
    """

    is_singleton = None
    """True if there can exists only one layer of this type (read-only).
    
    :type: bool
    """


class BMLayerItem:
    """Exposes a single custom data layer, their main purpose is for use as item accessors to custom-data when used with vert/edge/face/loop data."""

    def copy_from(self, other):
        """Return a copy of the layer
        
        :param other: Another layer to copy from.
        :param other: bmesh.types.BMLayerItem
        """

    name = ""
    """The layers unique name (read-only).
    
    :type: str
    """


class BMLoopUV:
    """"""

    pin_uv = None
    """UV pin state.
    
    :type: bool
    """

    select = None
    """UV select state.
    
    :type: bool
    """

    select_edge = None
    """UV edge select state.
    
    :type: bool
    """

    uv = None
    """Loops UV (as a 2D Vector).
    
    :type: mathutils.Vector
    """


class BMDeformVert:
    """"""

    def clear(self):
        """Clears all weights."""

    def get(self, key, default=None):
        """Returns the deform weight matching the key or default
                                        when not found (matches pythons dictionary function of the same name).
        
        :param key: The key associated with deform weight.
        :type key: int
        :param default: Optional argument for the value to return if
                                                                key is not found.
        :type default: Undefined
        """

    def items(self):
        """Return (group, weight) pairs for this vertex
                                        (matching pythons dict.items() functionality).
        
        :return: (key, value) pairs for each deform weight of this vertex.
        :param : (type: list of tuples)
        :rtype: list
        """

    def keys(self):
        """Return the group indices used by this vertex
                                        (matching pythons dict.keys() functionality).
        
        :return: the deform group this vertex uses
        :param : (type: list of ints)
        :rtype: list
        """

    def values(self):
        """Return the weights of the deform vertex
                                        (matching pythons dict.values() functionality).
        
        :return: The weights that influence this vertex
        :param : (type: list of floats)
        :rtype: list
        """
