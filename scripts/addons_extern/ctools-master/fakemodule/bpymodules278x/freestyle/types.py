class AdjacencyIterator:
    """Class hierarchy: freestyle.types.Iterator > freestyle.types.AdjacencyIterator
    Class for representing adjacency iterators used in the chaining
                        process.  An AdjacencyIterator is created in the increment() and
                        decrement() methods of a freestyle.types.ChainingIterator and passed to the
                        traverse() method of the ChainingIterator.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: An AdjacencyIterator object.
            (type: freestyle.types.AdjacencyIterator)
        :type brother: AdjacencyIterator
        """

    def __init__(self, vertex, restrict_to_selection=True, restrict_to_unvisited=True):
        """Builds a AdjacencyIterator object.
        
        :param vertex: The vertex which is the next crossing.
            (type: freestyle.types.ViewVertex)
        :type vertex: ViewVertex
        :param restrict_to_selection: Indicates whether to force the chaining
                                                            to stay within the set of selected ViewEdges or not.
        :type restrict_to_selection: bool
        :param restrict_to_unvisited: Indicates whether a ViewEdge that has
                                                            already been chained must be ignored ot not.
        :type restrict_to_unvisited: bool
        """

    is_incoming = None
    """True if the current ViewEdge is coming towards the iteration vertex, and
                                False otherwise.
    
    :type: bool
    """

    object = None
    """The ViewEdge object currently pointed to by this iterator.
    (type: freestyle.types.ViewEdge)
    
    :type: ViewEdge
    """


class BBox:
    """Class for representing a bounding box."""

    def __init__(self):
        """Default constructor."""


class BinaryPredicate0D:
    """Base class for binary predicates working on freestyle.types.Interface0D
                        objects.  A BinaryPredicate0D is typically an ordering relation
                        between two Interface0D objects.  The predicate evaluates a relation
                        between the two Interface0D instances and returns a boolean value (true
                        or false).  It is used by invoking the __call__() method.
    """

    def __init__(self):
        """Default constructor."""

    def __call__(self, inter1, inter2):
        """Must be overload by inherited classes.  It evaluates a relation
                                    between two Interface0D objects.
        
        :param inter1: The first Interface0D object.
            (type: freestyle.types.Interface0D)
        :type inter1: Interface0D
        :param inter2: The second Interface0D object.
            (type: freestyle.types.Interface0D)
        :type inter2: Interface0D
        :return: True or false.
        :rtype: bool
        """

    name = ""
    """The name of the binary 0D predicate.
    
    :type: str
    """


class BinaryPredicate1D:
    """Base class for binary predicates working on freestyle.types.Interface1D
                        objects.  A BinaryPredicate1D is typically an ordering relation
                        between two Interface1D objects.  The predicate evaluates a relation
                        between the two Interface1D instances and returns a boolean value (true
                        or false).  It is used by invoking the __call__() method.
    """

    def __init__(self):
        """Default constructor."""

    def __call__(self, inter1, inter2):
        """Must be overload by inherited classes. It evaluates a relation
                                    between two Interface1D objects.
        
        :param inter1: The first Interface1D object.
            (type: freestyle.types.Interface1D)
        :type inter1: Interface1D
        :param inter2: The second Interface1D object.
            (type: freestyle.types.Interface1D)
        :type inter2: Interface1D
        :return: True or false.
        :rtype: bool
        """

    name = ""
    """The name of the binary 1D predicate.
    
    :type: str
    """


class Chain:
    """Class hierarchy: freestyle.types.Interface1D > freestyle.types.Curve > freestyle.types.Chain
    Class to represent a 1D elements issued from the chaining process.  A
                        Chain is the last step before the freestyle.types.Stroke and is used in the
                        Splitting and Creation processes.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: A Chain object.
            (type: freestyle.types.Chain)
        :type brother: Chain
        """

    def __init__(self, id):
        """Builds a chain from its Id.
        
        :param id: An Id object.
            (type: freestyle.types.Id)
        :type id: Id
        """

    def push_viewedge_back(self, viewedge, orientation):
        """Adds a ViewEdge at the end of the Chain.
        
        :param viewedge: The ViewEdge that must be added.
            (type: freestyle.types.ViewEdge)
        :type viewedge: ViewEdge
        :param orientation: The orientation with which the ViewEdge must be
                                                            processed.
        :type orientation: bool
        """

    def push_viewedge_front(self, viewedge, orientation):
        """Adds a ViewEdge at the beginning of the Chain.
        
        :param viewedge: The ViewEdge that must be added.
            (type: freestyle.types.ViewEdge)
        :type viewedge: ViewEdge
        :param orientation: The orientation with which the ViewEdge must be
                                                            processed.
        :type orientation: bool
        """


class ChainingIterator:
    """Class hierarchy: freestyle.types.Iterator > freestyle.types.ViewEdgeIterator > freestyle.types.ChainingIterator
    Base class for chaining iterators.  This class is designed to be
                        overloaded in order to describe chaining rules.  It makes the
                        description of chaining rules easier.  The two main methods that need
                        to overloaded are traverse() and init().  traverse() tells which
                        freestyle.types.ViewEdge to follow, among the adjacent ones.  If you specify
                        restriction rules (such as "Chain only ViewEdges of the selection"),
                        they will be included in the adjacency iterator (i.e, the adjacent
                        iterator will only stop on "valid" edges).
    """

    def __init__(self, restrict_to_selection=True, restrict_to_unvisited=True, begin=None, orientation=True):
        """Builds a Chaining Iterator from the first ViewEdge used for
                                    iteration and its orientation.
        
        :param restrict_to_selection: Indicates whether to force the chaining
                                                            to stay within the set of selected ViewEdges or not.
        :type restrict_to_selection: bool
        :param restrict_to_unvisited: Indicates whether a ViewEdge that has
                                                            already been chained must be ignored ot not.
        :type restrict_to_unvisited: bool
        :param begin: The ViewEdge from which to start the chain.
            (type: freestyle.types.ViewEdge or None)
        :type begin: ViewEdge or None
        :param orientation: The direction to follow to explore the graph.  If
                                                            true, the direction indicated by the first ViewEdge is used.
        :type orientation: bool
        """

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: (type: freestyle.types.ChainingIterator)
        :type brother: ChainingIterator
        """

    def init(self):
        """Initializes the iterator context.  This method is called each
                                    time a new chain is started.  It can be used to reset some
                                    history information that you might want to keep.
        """

    def traverse(self, it):
        """This method iterates over the potential next ViewEdges and returns
                                    the one that will be followed next.  Returns the next ViewEdge to
                                    follow or None when the end of the chain is reached.
        
        :param it: The iterator over the ViewEdges adjacent to the end vertex
                                                    of the current ViewEdge.  The adjacency iterator reflects the
                                                    restriction rules by only iterating over the valid ViewEdges.
            (type: freestyle.types.AdjacencyIterator)
        :type it: AdjacencyIterator
        :return: Returns the next ViewEdge to follow, or None if chaining ends.
        :param : (type: freestyle.types.ViewEdge or None)
        :rtype: ViewEdge or None
        """

    is_incrementing = None
    """True if the current iteration is an incrementation.
    
    :type: bool
    """

    next_vertex = None
    """The ViewVertex that is the next crossing.
    (type: freestyle.types.ViewVertex)
    
    :type: ViewVertex
    """

    object = None
    """The ViewEdge object currently pointed by this iterator.
    (type: freestyle.types.ViewEdge)
    
    :type: ViewEdge
    """


class Curve:
    """Class hierarchy: freestyle.types.Interface1D > freestyle.types.Curve
    Base class for curves made of CurvePoints.  freestyle.types.SVertex is the
                        type of the initial curve vertices.  A freestyle.types.Chain is a
                        specialization of a Curve.
    """

    def __init__(self):
        """Default Constructor."""

    def __init__(self, brother):
        """Copy Constructor.
        
        :param brother: A Curve object.
            (type: freestyle.types.Curve)
        :type brother: Curve
        """

    def __init__(self, id):
        """Builds a Curve from its Id.
        
        :param id: An Id object.
            (type: freestyle.types.Id)
        :type id: Id
        """

    def push_vertex_back(self, vertex):
        """Adds a single vertex at the end of the Curve.
        
        :param vertex: A vertex object.
            (type: freestyle.types.SVertex or freestyle.types.CurvePoint)
        :type vertex: SVertex or CurvePoint
        """

    def push_vertex_front(self, vertex):
        """Adds a single vertex at the front of the Curve.
        
        :param vertex: A vertex object.
            (type: freestyle.types.SVertex or freestyle.types.CurvePoint)
        :type vertex: SVertex or CurvePoint
        """

    is_empty = None
    """True if the Curve doesn't have any Vertex yet.
    
    :type: bool
    """

    segments_size = None
    """The number of segments in the polyline constituting the Curve.
    
    :type: int
    """


class CurvePoint:
    """Class hierarchy: freestyle.types.Interface0D > freestyle.types.CurvePoint
    Class to represent a point of a curve.  A CurvePoint can be any point
                        of a 1D curve (it doesn't have to be a vertex of the curve).  Any
                        freestyle.types.Interface1D is built upon ViewEdges, themselves built upon
                        FEdges.  Therefore, a curve is basically a polyline made of a list of
                        freestyle.types.SVertex objects.  Thus, a CurvePoint is built by linearly
                        interpolating two freestyle.types.SVertex instances.  CurvePoint can be used
                        as virtual points while querying 0D information along a curve at a
                        given resolution.
    """

    def __init__(self):
        """Defult constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: A CurvePoint object.
            (type: freestyle.types.CurvePoint)
        :type brother: CurvePoint
        """

    def __init__(self, first_vertex, second_vertex, t2d):
        """Builds a CurvePoint from two SVertex objects and an interpolation parameter.
        
        :param first_vertex: The first SVertex.
            (type: freestyle.types.SVertex)
        :type first_vertex: SVertex
        :param second_vertex: The second SVertex.
            (type: freestyle.types.SVertex)
        :type second_vertex: SVertex
        :param t2d: A 2D interpolation parameter used to linearly interpolate
                                                            first_vertex and second_vertex.
        :type t2d: float
        """

    def __init__(self, first_point, second_point, t2d):
        """Builds a CurvePoint from two CurvePoint objects and an interpolation
                                    parameter.
        
        :param first_point: The first CurvePoint.
            (type: freestyle.types.CurvePoint)
        :type first_point: CurvePoint
        :param second_point: The second CurvePoint.
            (type: freestyle.types.CurvePoint)
        :type second_point: CurvePoint
        :param t2d: The 2D interpolation parameter used to linearly interpolate
                                                            first_point and second_point.
        :type t2d: float
        """

    fedge = None
    """Gets the FEdge for the two SVertices that given CurvePoints consists out of.
                                A shortcut for CurvePoint.first_svertex.get_fedge(CurvePoint.second_svertex).
    (type: freestyle.types.FEdge)
    
    :type: FEdge
    """

    first_svertex = None
    """The first SVertex upon which the CurvePoint is built.
    (type: freestyle.types.SVertex)
    
    :type: SVertex
    """

    second_svertex = None
    """The second SVertex upon which the CurvePoint is built.
    (type: freestyle.types.SVertex)
    
    :type: SVertex
    """

    t2d = None
    """The 2D interpolation parameter.
    
    :type: float
    """


class CurvePointIterator:
    """Class hierarchy: freestyle.types.Iterator > freestyle.types.CurvePointIterator
    Class representing an iterator on a curve.  Allows an iterating
                        outside initial vertices.  A CurvePoint is instanciated and returned
                        through the .object attribute.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: A CurvePointIterator object.
            (type: freestyle.types.CurvePointIterator)
        :type brother: CurvePointIterator
        """

    def __init__(self, step=0.0):
        """Builds a CurvePointIterator object.
        
        :param step: A resampling resolution with which the curve is resampled.
                                                    If zero, no resampling is done (i.e., the iterator iterates over
                                                    initial vertices).
        :type step: float
        """

    object = None
    """The CurvePoint object currently pointed by this iterator.
    (type: freestyle.types.CurvePoint)
    
    :type: CurvePoint
    """

    t = None
    """The curvilinear abscissa of the current point.
    
    :type: float
    """

    u = None
    """The point parameter at the current point in the stroke (0 <= u <= 1).
    
    :type: float
    """


class FEdge:
    """Class hierarchy: freestyle.types.Interface1D > freestyle.types.FEdge
    Base Class for feature edges.  This FEdge can represent a silhouette,
                        a crease, a ridge/valley, a border or a suggestive contour.  For
                        silhouettes, the FEdge is oriented so that the visible face lies on
                        the left of the edge.  For borders, the FEdge is oriented so that the
                        face lies on the left of the edge.  An FEdge can represent an initial
                        edge of the mesh or runs across a face of the initial mesh depending
                        on the smoothness or sharpness of the mesh.  This class is specialized
                        into a smooth and a sharp version since their properties slightly vary
                        from one to the other.
    """

    def FEdge(self):
        """Default constructor."""

    def FEdge(self, brother):
        """Copy constructor.
        
        :param brother: An FEdge object.
            (type: freestyle.types.FEdge)
        :type brother: FEdge
        """

    def FEdge(self, first_vertex, second_vertex):
        """Builds an FEdge going from the first vertex to the second.
        
        :param first_vertex: The first SVertex.
            (type: freestyle.types.SVertex)
        :type first_vertex: SVertex
        :param second_vertex: The second SVertex.
            (type: freestyle.types.SVertex)
        :type second_vertex: SVertex
        """

    first_svertex = None
    """The first SVertex constituting this FEdge.
    (type: freestyle.types.SVertex)
    
    :type: SVertex
    """

    id = None
    """The Id of this FEdge.
    (type: freestyle.types.Id)
    
    :type: Id
    """

    is_smooth = None
    """True if this FEdge is a smooth FEdge.
    
    :type: bool
    """

    nature = None
    """The nature of this FEdge.
    (type: freestyle.types.Nature)
    
    :type: Nature
    """

    next_fedge = None
    """The FEdge following this one in the ViewEdge.  The value is None if
                                this FEdge is the last of the ViewEdge.
    (type: freestyle.types.FEdge)
    
    :type: FEdge
    """

    previous_fedge = None
    """The FEdge preceding this one in the ViewEdge.  The value is None if
                                this FEdge is the first one of the ViewEdge.
    (type: freestyle.types.FEdge)
    
    :type: FEdge
    """

    second_svertex = None
    """The second SVertex constituting this FEdge.
    (type: freestyle.types.SVertex)
    
    :type: SVertex
    """

    viewedge = None
    """The ViewEdge to which this FEdge belongs to.
    (type: freestyle.types.ViewEdge)
    
    :type: ViewEdge
    """


class FEdgeSharp:
    """Class hierarchy: freestyle.types.Interface1D > freestyle.types.FEdge > freestyle.types.FEdgeSharp
    Class defining a sharp FEdge.  A Sharp FEdge corresponds to an initial
                        edge of the input mesh.  It can be a silhouette, a crease or a border.
                        If it is a crease edge, then it is borded by two faces of the mesh.
                        Face a lies on its right whereas Face b lies on its left.  If it is a
                        border edge, then it doesn't have any face on its right, and thus Face
                        a is None.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: An FEdgeSharp object.
            (type: freestyle.types.FEdgeSharp)
        :type brother: FEdgeSharp
        """

    def __init__(self, first_vertex, second_vertex):
        """Builds an FEdgeSharp going from the first vertex to the second.
        
        :param first_vertex: The first SVertex object.
            (type: freestyle.types.SVertex)
        :type first_vertex: SVertex
        :param second_vertex: The second SVertex object.
            (type: freestyle.types.SVertex)
        :type second_vertex: SVertex
        """

    face_mark_left = None
    """The face mark of the face lying on the left of the FEdge.
    
    :type: bool
    """

    face_mark_right = None
    """The face mark of the face lying on the right of the FEdge.  If this FEdge
                                is a border, it has no face on the right and thus this property is set to
                                false.
    
    :type: bool
    """

    material_index_left = None
    """The index of the material of the face lying on the left of the FEdge.
    
    :type: int
    """

    material_index_right = None
    """The index of the material of the face lying on the right of the FEdge.
                                If this FEdge is a border, it has no Face on its right and therefore
                                no material.
    
    :type: int
    """

    material_left = None
    """The material of the face lying on the left of the FEdge.
    (type: freestyle.types.Material)
    
    :type: Material
    """

    material_right = None
    """The material of the face lying on the right of the FEdge.  If this FEdge
                                is a border, it has no Face on its right and therefore no material.
    (type: freestyle.types.Material)
    
    :type: Material
    """

    normal_left = None
    """The normal to the face lying on the left of the FEdge.
    
    :type: mathutils.Vector
    """

    normal_right = None
    """The normal to the face lying on the right of the FEdge.  If this FEdge
                                is a border, it has no Face on its right and therefore no normal.
    
    :type: mathutils.Vector
    """


class FEdgeSmooth:
    """Class hierarchy: freestyle.types.Interface1D > freestyle.types.FEdge > freestyle.types.FEdgeSmooth
    Class defining a smooth edge.  This kind of edge typically runs across
                        a face of the input mesh.  It can be a silhouette, a ridge or valley,
                        a suggestive contour.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: An FEdgeSmooth object.
            (type: freestyle.types.FEdgeSmooth)
        :type brother: FEdgeSmooth
        """

    def __init__(self, first_vertex, second_vertex):
        """Builds an FEdgeSmooth going from the first to the second.
        
        :param first_vertex: The first SVertex object.
            (type: freestyle.types.SVertex)
        :type first_vertex: SVertex
        :param second_vertex: The second SVertex object.
            (type: freestyle.types.SVertex)
        :type second_vertex: SVertex
        """

    face_mark = None
    """The face mark of the face that this FEdge is running across.
    
    :type: bool
    """

    material = None
    """The material of the face that this FEdge is running across.
    (type: freestyle.types.Material)
    
    :type: Material
    """

    material_index = None
    """The index of the material of the face that this FEdge is running across.
    
    :type: int
    """

    normal = None
    """The normal of the face that this FEdge is running across.
    
    :type: mathutils.Vector
    """


class Id:
    """Class for representing an object Id."""

    def __init__(self, first=0, second=0):
        """Build the Id from two numbers.
        
        :param first: The first number.
        :type first: int
        :param second: The second number.
        :type second: int
        """

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: An Id object.
            (type: freestyle.types.Id)
        :type brother: Id
        """

    first = None
    """The first number constituting the Id.
    
    :type: int
    """

    second = None
    """The second number constituting the Id.
    
    :type: int
    """


class IntegrationType:
    """Class hierarchy: int > freestyle.types.IntegrationType
    Different integration methods that can be invoked to integrate into a
                        single value the set of values obtained from each 0D element of an 1D
                        element:
    * IntegrationType.MEAN: The value computed for the 1D element is the
                                mean of the values obtained for the 0D elements.
    * IntegrationType.MIN: The value computed for the 1D element is the
                                minimum of the values obtained for the 0D elements.
    * IntegrationType.MAX: The value computed for the 1D element is the
                                maximum of the values obtained for the 0D elements.
    * IntegrationType.FIRST: The value computed for the 1D element is the
                                first of the values obtained for the 0D elements.
    * IntegrationType.LAST: The value computed for the 1D element is the
                                last of the values obtained for the 0D elements.
    """

    MEAN = 0
    """:type: int"""

    MIN = 1
    """:type: int"""

    MAX = 2
    """:type: int"""

    FIRST = 3
    """:type: int"""

    LAST = 4
    """:type: int"""


class Interface0D:
    """Base class for any 0D element."""

    def __init__(self):
        """Default constructor."""

    def get_fedge(self, inter):
        """Returns the FEdge that lies between this 0D element and the 0D
                                    element given as the argument.
        
        :param inter: A 0D element.
            (type: freestyle.types.Interface0D)
        :type inter: Interface0D
        :return: The FEdge lying between the two 0D elements.
        :param : (type: freestyle.types.FEdge)
        :rtype: FEdge
        """

    id = None
    """The Id of this 0D element.
    (type: freestyle.types.Id)
    
    :type: Id
    """

    name = ""
    """The string of the name of this 0D element.
    
    :type: str
    """

    nature = None
    """The nature of this 0D element.
    (type: freestyle.types.Nature)
    
    :type: Nature
    """

    point_2d = None
    """The 2D point of this 0D element.
    
    :type: mathutils.Vector
    """

    point_3d = None
    """The 3D point of this 0D element.
    
    :type: mathutils.Vector
    """

    projected_x = None
    """The X coordinate of the projected 3D point of this 0D element.
    
    :type: float
    """

    projected_y = None
    """The Y coordinate of the projected 3D point of this 0D element.
    
    :type: float
    """

    projected_z = None
    """The Z coordinate of the projected 3D point of this 0D element.
    
    :type: float
    """


class Interface0DIterator:
    """Class hierarchy: freestyle.types.Iterator > freestyle.types.Interface0DIterator
    Class defining an iterator over Interface0D elements.  An instance of
                        this iterator is always obtained from a 1D element.
    """

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: An Interface0DIterator object.
            (type: freestyle.types.Interface0DIterator)
        :type brother: Interface0DIterator
        """

    def __init__(self, it):
        """Construct a nested Interface0DIterator that can be the argument of
                                    a Function0D.
        
        :param it: An iterator object to be nested.
            (type: freestyle.types.SVertexIterator, freestyle.types.CurvePointIterator, or
                                                    freestyle.types.StrokeVertexIterator)
        :type it: SVertexIterator, CurvePointIterator, or
                                                    StrokeVertexIterator
        """

    at_last = None
    """True if the interator points to the last valid element.
                                For its counterpart (pointing to the first valid element), use it.is_begin.
    
    :type: bool
    """

    object = None
    """The 0D object currently pointed to by this iterator.  Note that the object
                                may be an instance of an Interface0D subclass. For example if the iterator
                                has been created from the vertices_begin() method of the freestyle.types.Stroke
                                class, the .object property refers to a freestyle.types.StrokeVertex object.
    (type: freestyle.types.Interface0D or one of its subclasses.)
    
    :type: Interface0D or one of its subclasses.
    """

    t = None
    """The curvilinear abscissa of the current point.
    
    :type: float
    """

    u = None
    """The point parameter at the current point in the 1D element (0 <= u <= 1).
    
    :type: float
    """


class Interface1D:
    """Base class for any 1D element."""

    def __init__(self):
        """Default constructor."""

    def points_begin(self, t=0.0):
        """Returns an iterator over the Interface1D points, pointing to the
                                    first point. The difference with vertices_begin() is that here we can
                                    iterate over points of the 1D element at a any given sampling.
                                    Indeed, for each iteration, a virtual point is created.
        
        :param t: A sampling with which we want to iterate over points of
                                                    this 1D element.
        :type t: float
        :return: An Interface0DIterator pointing to the first point.
        :param : (type: freestyle.types.Interface0DIterator)
        :rtype: Interface0DIterator
        """

    def points_end(self, t=0.0):
        """Returns an iterator over the Interface1D points, pointing after the
                                    last point. The difference with vertices_end() is that here we can
                                    iterate over points of the 1D element at a given sampling.  Indeed,
                                    for each iteration, a virtual point is created.
        
        :param t: A sampling with which we want to iterate over points of
                                                    this 1D element.
        :type t: float
        :return: An Interface0DIterator pointing after the last point.
        :param : (type: freestyle.types.Interface0DIterator)
        :rtype: Interface0DIterator
        """

    def vertices_begin(self):
        """Returns an iterator over the Interface1D vertices, pointing to the
                                    first vertex.
        
        :return: An Interface0DIterator pointing to the first vertex.
        :param : (type: freestyle.types.Interface0DIterator)
        :rtype: Interface0DIterator
        """

    def vertices_end(self):
        """Returns an iterator over the Interface1D vertices, pointing after
                                    the last vertex.
        
        :return: An Interface0DIterator pointing after the last vertex.
        :param : (type: freestyle.types.Interface0DIterator)
        :rtype: Interface0DIterator
        """

    id = None
    """The Id of this Interface1D.
    (type: freestyle.types.Id)
    
    :type: Id
    """

    length_2d = None
    """The 2D length of this Interface1D.
    
    :type: float
    """

    name = ""
    """The string of the name of the 1D element.
    
    :type: str
    """

    nature = None
    """The nature of this Interface1D.
    (type: freestyle.types.Nature)
    
    :type: Nature
    """

    time_stamp = None
    """The time stamp of the 1D element, mainly used for selection.
    
    :type: int
    """


class Iterator:
    """Base class to define iterators."""

    def __init__(self):
        """Default constructor."""

    def decrement(self):
        """Makes the iterator point the previous element."""

    def increment(self):
        """Makes the iterator point the next element."""

    is_begin = None
    """True if the interator points the first element.
    
    :type: bool
    """

    is_end = None
    """True if the interator points the last element.
    
    :type: bool
    """

    name = ""
    """The string of the name of this iterator.
    
    :type: str
    """


class Material:
    """Class defining a material."""

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: A Material object.
            (type: freestyle.types.Material)
        :type brother: Material
        """

    def __init__(self, line, diffuse, ambient, specular, emission, shininess, priority):
        """Builds a Material from its line, diffuse, ambient, specular, emissive
                                    colors, a shininess coefficient and line color priority.
        
        :param line: The line color.
        :type line: mathutils.Vector, list or tuple of 4 float values
        :param diffuse: The diffuse color.
        :type diffuse: mathutils.Vector, list or tuple of 4 float values
        :param ambient: The ambient color.
        :type ambient: mathutils.Vector, list or tuple of 4 float values
        :param specular: The specular color.
        :type specular: mathutils.Vector, list or tuple of 4 float values
        :param emission: The emissive color.
        :type emission: mathutils.Vector, list or tuple of 4 float values
        :param shininess: The shininess coefficient.
        :type shininess: float
        :param priority: The line color priority.
        :type priority: int
        """

    ambient = None
    """RGBA components of the ambient color of the material.
    
    :type: mathutils.Color
    """

    diffuse = None
    """RGBA components of the diffuse color of the material.
    
    :type: mathutils.Vector
    """

    emission = None
    """RGBA components of the emissive color of the material.
    
    :type: mathutils.Color
    """

    line = None
    """RGBA components of the line color of the material.
    
    :type: mathutils.Vector
    """

    priority = None
    """Line color priority of the material.
    
    :type: int
    """

    shininess = None
    """Shininess coefficient of the material.
    
    :type: float
    """

    specular = None
    """RGBA components of the specular color of the material.
    
    :type: mathutils.Vector
    """


class MediumType:
    """Class hierarchy: int > freestyle.types.MediumType
    The different blending modes available to similate the interaction
                        media-medium:
    * Stroke.DRY_MEDIUM: To simulate a dry medium such as Pencil or Charcoal.
    * Stroke.HUMID_MEDIUM: To simulate ink painting (color substraction blending).
    * Stroke.OPAQUE_MEDIUM: To simulate an opaque medium (oil, spray...).
    """


class Nature:
    """Class hierarchy: int > freestyle.types.Nature
    Different possible natures of 0D and 1D elements of the ViewMap.
    Vertex natures:
    * Nature.POINT: True for any 0D element.
    * Nature.S_VERTEX: True for SVertex.
    * Nature.VIEW_VERTEX: True for ViewVertex.
    * Nature.NON_T_VERTEX: True for NonTVertex.
    * Nature.T_VERTEX: True for TVertex.
    * Nature.CUSP: True for CUSP.
    Edge natures:
    * Nature.NO_FEATURE: True for non feature edges (always false for 1D
                                elements of the ViewMap).
    * Nature.SILHOUETTE: True for silhouettes.
    * Nature.BORDER: True for borders.
    * Nature.CREASE: True for creases.
    * Nature.RIDGE: True for ridges.
    * Nature.VALLEY: True for valleys.
    * Nature.SUGGESTIVE_CONTOUR: True for suggestive contours.
    * Nature.MATERIAL_BOUNDARY: True for edges at material boundaries.
    * Nature.EDGE_MARK: True for edges having user-defined edge marks.
    """


class Noise:
    """Class to provide Perlin noise functionalities.
    Undocumented
    Undocumented
    """

    def __init__(self, seed = -1):
        """Builds a Noise object.  Seed is an optional argument.  The seed value is used
                                    as a seed for random number generation if it is equal to or greater than zero;
                                    otherwise, time is used as a seed.
        
        :param seed: Seed for random number generation.
        :type seed: int
        """

    def smoothNoise1(self, v):
        """Returns a smooth noise value for a 1D element.
        
        :param v: One-dimensional sample point.
        :type v: float
        :return: A smooth noise value.
        :rtype: float
        """

    def smoothNoise2(self, v):
        """Returns a smooth noise value for a 2D element.
        
        :param v: Two-dimensional sample point.
        :type v: mathutils.Vector, list or tuple of 2 real numbers
        :return: A smooth noise value.
        :rtype: float
        """

    def smoothNoise3(self, v):
        """Returns a smooth noise value for a 3D element.
        
        :param v: Three-dimensional sample point.
        :type v: mathutils.Vector, list or tuple of 3 real numbers
        :return: A smooth noise value.
        :rtype: float
        """

    def turbulence1(self, v, freq, amp, oct=4):
        """Returns a noise value for a 1D element.
        
        :param v: One-dimensional sample point.
        :type v: float
        :param freq: Noise frequency.
        :type freq: float
        :param amp: Amplitude.
        :type amp: float
        :param oct: Number of octaves.
        :type oct: int
        :return: A noise value.
        :rtype: float
        """

    def turbulence2(self, v, freq, amp, oct=4):
        """Returns a noise value for a 2D element.
        
        :param v: Two-dimensional sample point.
        :type v: mathutils.Vector, list or tuple of 2 real numbers
        :param freq: Noise frequency.
        :type freq: float
        :param amp: Amplitude.
        :type amp: float
        :param oct: Number of octaves.
        :type oct: int
        :return: A noise value.
        :rtype: float
        """

    def turbulence3(self, v, freq, amp, oct=4):
        """Returns a noise value for a 3D element.
        
        :param v: Three-dimensional sample point.
        :type v: mathutils.Vector, list or tuple of 3 real numbers
        :param freq: Noise frequency.
        :type freq: float
        :param amp: Amplitude.
        :type amp: float
        :param oct: Number of octaves.
        :type oct: int
        :return: A noise value.
        :rtype: float
        """


class NonTVertex:
    """Class hierarchy: freestyle.types.Interface0D > freestyle.types.ViewVertex > freestyle.types.NonTVertex
    View vertex for corners, cusps, etc. associated to a single SVertex.
                        Can be associated to 2 or more view edges.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, svertex):
        """Build a NonTVertex from a SVertex.
        
        :param svertex: An SVertex object.
            (type: freestyle.types.SVertex)
        :type svertex: SVertex
        """

    svertex = None
    """The SVertex on top of which this NonTVertex is built.
    (type: freestyle.types.SVertex)
    
    :type: SVertex
    """


class Operators:
    """Class defining the operators used in a style module.  There are five
                        types of operators: Selection, chaining, splitting, sorting and
                        creation.  All these operators are user controlled through functors,
                        predicates and shaders that are taken as arguments.
    """

    def bidirectional_chain(self, it, pred):
        """Builds a set of chains from the current set of ViewEdges.  Each
                                    ViewEdge of the current list potentially starts a new chain.  The
                                    chaining operator then iterates over the ViewEdges of the ViewMap
                                    using the user specified iterator.  This operator iterates both using
                                    the increment and decrement operators and is therefore bidirectional.
                                    This operator works with a ChainingIterator which contains the
                                    chaining rules.  It is this last one which can be told to chain only
                                    edges that belong to the selection or not to process twice a ViewEdge
                                    during the chaining.  Each time a ViewEdge is added to a chain, its
                                    chaining time stamp is incremented.  This allows you to keep track of
                                    the number of chains to which a ViewEdge belongs to.
        
        :param it: The ChainingIterator on the ViewEdges of the ViewMap.  It
                                                            contains the chaining rule.
            (type: freestyle.types.ChainingIterator)
        :type it: ChainingIterator
        :param pred: The predicate on the ViewEdge that expresses the
                                                            stopping condition.
            (type: freestyle.types.UnaryPredicate1D)
        :type pred: UnaryPredicate1D
        """

    def bidirectional_chain(self, it):
        """The only difference with the above bidirectional chaining algorithm
                                    is that we don't need to pass a stopping criterion.  This might be
                                    desirable when the stopping criterion is already contained in the
                                    iterator definition.  Builds a set of chains from the current set of
                                    ViewEdges.  Each ViewEdge of the current list potentially starts a new
                                    chain.  The chaining operator then iterates over the ViewEdges of the
                                    ViewMap using the user specified iterator.  This operator iterates
                                    both using the increment and decrement operators and is therefore
                                    bidirectional.  This operator works with a ChainingIterator which
                                    contains the chaining rules.  It is this last one which can be told to
                                    chain only edges that belong to the selection or not to process twice
                                    a ViewEdge during the chaining.  Each time a ViewEdge is added to a
                                    chain, its chaining time stamp is incremented.  This allows you to
                                    keep track of the number of chains to which a ViewEdge belongs to.
        
        :param it: The ChainingIterator on the ViewEdges of the ViewMap.  It
                                                    contains the chaining rule.
            (type: freestyle.types.ChainingIterator)
        :type it: ChainingIterator
        """

    def chain(self, it, pred, modifier):
        """Builds a set of chains from the current set of ViewEdges.  Each
                                    ViewEdge of the current list starts a new chain.  The chaining
                                    operator then iterates over the ViewEdges of the ViewMap using the
                                    user specified iterator.  This operator only iterates using the
                                    increment operator and is therefore unidirectional.
        
        :param it: The iterator on the ViewEdges of the ViewMap. It contains
                                                            the chaining rule.
            (type: freestyle.types.ViewEdgeIterator)
        :type it: ViewEdgeIterator
        :param pred: The predicate on the ViewEdge that expresses the
                                                            stopping condition.
            (type: freestyle.types.UnaryPredicate1D)
        :type pred: UnaryPredicate1D
        :param modifier: A function that takes a ViewEdge as argument and
                                                            that is used to modify the processed ViewEdge state (the
                                                            timestamp incrementation is a typical illustration of such a
                                                            modifier).
            (type: freestyle.types.UnaryFunction1DVoid)
        :type modifier: UnaryFunction1DVoid
        """

    def chain(self, it, pred):
        """Builds a set of chains from the current set of ViewEdges.  Each
                                    ViewEdge of the current list starts a new chain.  The chaining
                                    operator then iterates over the ViewEdges of the ViewMap using the
                                    user specified iterator.  This operator only iterates using the
                                    increment operator and is therefore unidirectional.  This chaining
                                    operator is different from the previous one because it doesn't take
                                    any modifier as argument.  Indeed, the time stamp (insuring that a
                                    ViewEdge is processed one time) is automatically managed in this
                                    case.
        
        :param it: The iterator on the ViewEdges of the ViewMap. It contains
                                                            the chaining rule.
            (type: freestyle.types.ViewEdgeIterator)
        :type it: ViewEdgeIterator
        :param pred: The predicate on the ViewEdge that expresses the
                                                            stopping condition.
            (type: freestyle.types.UnaryPredicate1D)
        :type pred: UnaryPredicate1D
        """

    def create(self, pred, shaders):
        """Creates and shades the strokes from the current set of chains.  A
                                    predicate can be specified to make a selection pass on the chains.
        
        :param pred: The predicate that a chain must verify in order to be
                                                            transform as a stroke.
            (type: freestyle.types.UnaryPredicate1D)
        :type pred: UnaryPredicate1D
        :param shaders: The list of shaders used to shade the strokes.
            (type: list of freestyle.types.StrokeShader objects)
        :type shaders: list
        """

    def get_chain_from_index(self, i):
        """Returns the Chain at the index in the current set of Chains.
        
        :param i: index (0 <= i < Operators.get_chains_size()).
        :type i: int
        :return: The Chain object.
        :param : (type: freestyle.types.Chain)
        :rtype: Chain
        """

    def get_chains_size(self):
        """Returns the number of Chains.
        
        :return: The number of Chains.
        :rtype: int
        """

    def get_stroke_from_index(self, i):
        """Returns the Stroke at the index in the current set of Strokes.
        
        :param i: index (0 <= i < Operators.get_strokes_size()).
        :type i: int
        :return: The Stroke object.
        :param : (type: freestyle.types.Stroke)
        :rtype: Stroke
        """

    def get_strokes_size(self):
        """Returns the number of Strokes.
        
        :return: The number of Strokes.
        :rtype: int
        """

    def get_view_edges_size(self):
        """Returns the number of ViewEdges.
        
        :return: The number of ViewEdges.
        :rtype: int
        """

    def get_viewedge_from_index(self, i):
        """Returns the ViewEdge at the index in the current set of ViewEdges.
        
        :param i: index (0 <= i < Operators.get_view_edges_size()).
        :type i: int
        :return: The ViewEdge object.
        :param : (type: freestyle.types.ViewEdge)
        :rtype: ViewEdge
        """

    def recursive_split(self, func, pred_1d, sampling=0.0):
        """Splits the current set of chains in a recursive way.  We process the
                                    points of each chain (with a specified sampling) to find the point
                                    minimizing a specified function.  The chain is split in two at this
                                    point and the two new chains are processed in the same way.  The
                                    recursivity level is controlled through a predicate 1D that expresses
                                    a stopping condition on the chain that is about to be processed.
        
        :param func: The Unary Function evaluated at each point of the chain.
                                                            The splitting point is the point minimizing this function.
            (type: freestyle.types.UnaryFunction0DDouble)
        :type func: UnaryFunction0DDouble
        :param pred_1d: The Unary Predicate expressing the recursivity stopping
                                                            condition.  This predicate is evaluated for each curve before it
                                                            actually gets split.  If pred_1d(chain) is true, the curve won't be
                                                            split anymore.
            (type: freestyle.types.UnaryPredicate1D)
        :type pred_1d: UnaryPredicate1D
        :param sampling: The resolution used to sample the chain for the
                                                            predicates evaluation. (The chain is not actually resampled, a
                                                            virtual point only progresses along the curve using this
                                                            resolution.)
        :type sampling: float
        """

    def recursive_split(self, func, pred_0d, pred_1d, sampling=0.0):
        """Splits the current set of chains in a recursive way.  We process the
                                    points of each chain (with a specified sampling) to find the point
                                    minimizing a specified function.  The chain is split in two at this
                                    point and the two new chains are processed in the same way.  The user
                                    can specify a 0D predicate to make a first selection on the points
                                    that can potentially be split.  A point that doesn't verify the 0D
                                    predicate won't be candidate in realizing the min.  The recursivity
                                    level is controlled through a predicate 1D that expresses a stopping
                                    condition on the chain that is about to be processed.
        
        :param func: The Unary Function evaluated at each point of the chain.
                                                            The splitting point is the point minimizing this function.
            (type: freestyle.types.UnaryFunction0DDouble)
        :type func: UnaryFunction0DDouble
        :param pred_0d: The Unary Predicate 0D used to select the candidate
                                                            points where the split can occur.  For example, it is very likely
                                                            that would rather have your chain splitting around its middle
                                                            point than around one of its extremities.  A 0D predicate working
                                                            on the curvilinear abscissa allows to add this kind of constraints.
            (type: freestyle.types.UnaryPredicate0D)
        :type pred_0d: UnaryPredicate0D
        :param pred_1d: The Unary Predicate expressing the recursivity stopping
                                                            condition. This predicate is evaluated for each curve before it
                                                            actually gets split.  If pred_1d(chain) is true, the curve won't be
                                                            split anymore.
            (type: freestyle.types.UnaryPredicate1D)
        :type pred_1d: UnaryPredicate1D
        :param sampling: The resolution used to sample the chain for the
                                                            predicates evaluation. (The chain is not actually resampled; a
                                                            virtual point only progresses along the curve using this
                                                            resolution.)
        :type sampling: float
        """

    def reset(self, delete_strokes=True):
        """Resets the line stylization process to the initial state.  The results of
                                    stroke creation are accumulated if delete_strokes is set to False.
        
        :param delete_strokes: Delete the strokes that are currently stored.
        :type delete_strokes: bool
        """

    def select(self, pred):
        """Selects the ViewEdges of the ViewMap verifying a specified
                                    condition.
        
        :param pred: The predicate expressing this condition.
            (type: freestyle.types.UnaryPredicate1D)
        :type pred: UnaryPredicate1D
        """

    def sequential_split(self, starting_pred, stopping_pred, sampling=0.0):
        """Splits each chain of the current set of chains in a sequential way.
                                    The points of each chain are processed (with a specified sampling)
                                    sequentially. Each time a user specified starting condition is
                                    verified, a new chain begins and ends as soon as a user-defined
                                    stopping predicate is verified. This allows chains overlapping rather
                                    than chains partitioning. The first point of the initial chain is the
                                    first point of one of the resulting chains. The splitting ends when
                                    no more chain can start.
        
        :param starting_pred: The predicate on a point that expresses the
                                                            starting condition.
            (type: freestyle.types.UnaryPredicate0D)
        :type starting_pred: UnaryPredicate0D
        :param stopping_pred: The predicate on a point that expresses the
                                                            stopping condition.
            (type: freestyle.types.UnaryPredicate0D)
        :type stopping_pred: UnaryPredicate0D
        :param sampling: The resolution used to sample the chain for the
                                                            predicates evaluation. (The chain is not actually resampled;
                                                            a virtual point only progresses along the curve using this
                                                            resolution.)
        :type sampling: float
        """

    def sequential_split(self, pred, sampling=0.0):
        """Splits each chain of the current set of chains in a sequential way.
                                    The points of each chain are processed (with a specified sampling)
                                    sequentially and each time a user specified condition is verified,
                                    the chain is split into two chains.  The resulting set of chains is a
                                    partition of the initial chain
        
        :param pred: The predicate on a point that expresses the splitting
                                                            condition.
            (type: freestyle.types.UnaryPredicate0D)
        :type pred: UnaryPredicate0D
        :param sampling: The resolution used to sample the chain for the
                                                            predicate evaluation. (The chain is not actually resampled; a
                                                            virtual point only progresses along the curve using this
                                                            resolution.)
        :type sampling: float
        """

    def sort(self, pred):
        """Sorts the current set of chains (or viewedges) according to the
                                    comparison predicate given as argument.
        
        :param pred: The binary predicate used for the comparison.
            (type: freestyle.types.BinaryPredicate1D)
        :type pred: BinaryPredicate1D
        """


class SShape:
    """Class to define a feature shape.  It is the gathering of feature
                        elements from an identified input shape.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: An SShape object.
            (type: freestyle.types.SShape)
        :type brother: SShape
        """

    def add_edge(self, edge):
        """Adds an FEdge to the list of FEdges.
        
        :param edge: An FEdge object.
            (type: freestyle.types.FEdge)
        :type edge: FEdge
        """

    def add_vertex(self, vertex):
        """Adds an SVertex to the list of SVertex of this Shape.  The SShape
                                    attribute of the SVertex is also set to this SShape.
        
        :param vertex: An SVertex object.
            (type: freestyle.types.SVertex)
        :type vertex: SVertex
        """

    def compute_bbox(self):
        """Compute the bbox of the SShape."""

    bbox = None
    """The bounding box of the SShape.
    (type: freestyle.types.BBox)
    
    :type: BBox
    """

    edges = None
    """The list of edges constituting this SShape.
    (type: List of freestyle.types.FEdge objects)
    
    :type: List
    """

    id = None
    """The Id of this SShape.
    (type: freestyle.types.Id)
    
    :type: Id
    """

    name = ""
    """The name of the SShape.
    
    :type: str
    """

    vertices = None
    """The list of vertices constituting this SShape.
    (type: List of freestyle.types.SVertex objects)
    
    :type: List
    """


class SVertex:
    """Class hierarchy: freestyle.types.Interface0D > freestyle.types.SVertex
    Class to define a vertex of the embedding.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: A SVertex object.
            (type: freestyle.types.SVertex)
        :type brother: SVertex
        """

    def __init__(self, point_3d, id):
        """Builds a SVertex from 3D coordinates and an Id.
        
        :param point_3d: A three-dimensional vector.
        :type point_3d: mathutils.Vector
        :param id: An Id object.
            (type: freestyle.types.Id)
        :type id: Id
        """

    def add_fedge(self, fedge):
        """Add an FEdge to the list of edges emanating from this SVertex.
        
        :param fedge: An FEdge.
            (type: freestyle.types.FEdge)
        :type fedge: FEdge
        """

    def add_normal(self, normal):
        """Adds a normal to the SVertex's set of normals.  If the same normal
                                    is already in the set, nothing changes.
        
        :param normal: A three-dimensional vector.
        :type normal: mathutils.Vector, list or tuple of 3 real numbers
        """

    curvatures = None
    """Curvature information expressed in the form of a seven-element tuple
                                (K1, e1, K2, e2, Kr, er, dKr), where K1 and K2 are scalar values
                                representing the first (maximum) and second (minimum) principal
                                curvatures at this SVertex, respectively; e1 and e2 are
                                three-dimensional vectors representing the first and second principal
                                directions, i.e. the directions of the normal plane where the
                                curvature takes its maximum and minimum values, respectively; and Kr,
                                er and dKr are the radial curvature, radial direction, and the
                                derivative of the radial curvature at this SVertex, respectively.
    
    :type: tuple
    """

    id = None
    """The Id of this SVertex.
    (type: freestyle.types.Id)
    
    :type: Id
    """

    normals = None
    """The normals for this Vertex as a list.  In a sharp surface, an SVertex
                                has exactly one normal.  In a smooth surface, an SVertex can have any
                                number of normals.
    (type: list of mathutils.Vector objects)
    
    :type: list
    """

    normals_size = None
    """The number of different normals for this SVertex.
    
    :type: int
    """

    point_2d = None
    """The projected 3D coordinates of the SVertex.
    
    :type: mathutils.Vector
    """

    point_3d = None
    """The 3D coordinates of the SVertex.
    
    :type: mathutils.Vector
    """

    viewvertex = None
    """If this SVertex is also a ViewVertex, this property refers to the
                                ViewVertex, and None otherwise.
    (type: freestyle.types.ViewVertex)
    
    :type: ViewVertex
    """


class SVertexIterator:
    """Class hierarchy: freestyle.types.Iterator > freestyle.types.SVertexIterator
    Class representing an iterator over freestyle.types.SVertex of a
                        freestyle.types.ViewEdge.  An instance of an SVertexIterator can be obtained
                        from a ViewEdge by calling verticesBegin() or verticesEnd().
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: An SVertexIterator object.
            (type: freestyle.types.SVertexIterator)
        :type brother: SVertexIterator
        """

    def __init__(self, vertex, begin, previous_edge, next_edge, t):
        """Build an SVertexIterator that starts iteration from an SVertex
                                    object v.
        
        :param vertex: The SVertex from which the iterator starts iteration.
            (type: freestyle.types.SVertex)
        :type vertex: SVertex
        :param begin: The first SVertex of a ViewEdge.
            (type: freestyle.types.SVertex)
        :type begin: SVertex
        :param previous_edge: The previous FEdge coming to vertex.
            (type: freestyle.types.FEdge)
        :type previous_edge: FEdge
        :param next_edge: The next FEdge going out from vertex.
            (type: freestyle.types.FEdge)
        :type next_edge: FEdge
        :param t: The curvilinear abscissa at vertex.
        :type t: float
        """

    object = None
    """The SVertex object currently pointed by this iterator.
    (type: freestyle.types.SVertex)
    
    :type: SVertex
    """

    t = None
    """The curvilinear abscissa of the current point.
    
    :type: float
    """

    u = None
    """The point parameter at the current point in the 1D element (0 <= u <= 1).
    
    :type: float
    """


class Stroke:
    """Class hierarchy: freestyle.types.Interface1D > freestyle.types.Stroke
    Class to define a stroke.  A stroke is made of a set of 2D vertices
                        (freestyle.types.StrokeVertex), regularly spaced out.  This set of vertices
                        defines the stroke's backbone geometry.  Each of these stroke vertices
                        defines the stroke's shape and appearance at this vertex position.
    """

    def Stroke(self):
        """Default constructor"""

    def Stroke(self, brother):
        """Copy constructor"""

    def compute_sampling(self, n):
        """Compute the sampling needed to get N vertices.  If the
                                    specified number of vertices is less than the actual number of
                                    vertices, the actual sampling value is returned. (To remove Vertices,
                                    use the RemoveVertex() method of this class.)
        
        :param n: The number of stroke vertices we eventually want
                                                    in our Stroke.
        :type n: int
        :return: The sampling that must be used in the Resample(float)
                                                    method.
        :rtype: float
        """

    def insert_vertex(self, vertex, next):
        """Inserts the StrokeVertex given as argument into the Stroke before the
                                    point specified by next.  The length and curvilinear abscissa are
                                    updated consequently.
        
        :param vertex: The StrokeVertex to insert in the Stroke.
            (type: freestyle.types.StrokeVertex)
        :type vertex: StrokeVertex
        :param next: A StrokeVertexIterator pointing to the StrokeVertex
                                                            before which vertex must be inserted.
            (type: freestyle.types.StrokeVertexIterator)
        :type next: StrokeVertexIterator
        """

    def remove_all_vertices(self):
        """Removes all vertices from the Stroke."""

    def remove_vertex(self, vertex):
        """Removes the StrokeVertex given as argument from the Stroke. The length
                                    and curvilinear abscissa are updated consequently.
        
        :param vertex: the StrokeVertex to remove from the Stroke.
            (type: freestyle.types.StrokeVertex)
        :type vertex: StrokeVertex
        """

    def resample(self, n):
        """Resamples the stroke so that it eventually has N points.  That means
                                    it is going to add N-vertices_size, where vertices_size is the
                                    number of points we already have.  If vertices_size >= N, no
                                    resampling is done.
        
        :param n: The number of vertices we eventually want in our stroke.
        :type n: int
        """

    def resample(self, sampling):
        """Resamples the stroke with a given sampling.  If the sampling is
                                    smaller than the actual sampling value, no resampling is done.
        
        :param sampling: The new sampling value.
        :type sampling: float
        """

    def stroke_vertices_begin(self, t=0.0):
        """Returns a StrokeVertexIterator pointing on the first StrokeVertex of
                                    the Stroke. One can specify a sampling value to resample the Stroke
                                    on the fly if needed.
        
        :param t: The resampling value with which we want our Stroke to be
                                                    resampled.  If 0 is specified, no resampling is done.
        :type t: float
        :return: A StrokeVertexIterator pointing on the first StrokeVertex.
        :param : (type: freestyle.types.StrokeVertexIterator)
        :rtype: StrokeVertexIterator
        """

    def stroke_vertices_end(self):
        """Returns a StrokeVertexIterator pointing after the last StrokeVertex
                                    of the Stroke.
        
        :return: A StrokeVertexIterator pointing after the last StrokeVertex.
        :param : (type: freestyle.types.StrokeVertexIterator)
        :rtype: StrokeVertexIterator
        """

    def stroke_vertices_size(self):
        """Returns the number of StrokeVertex constituting the Stroke.
        
        :return: The number of stroke vertices.
        :rtype: int
        """

    def update_length(self):
        """Updates the 2D length of the Stroke."""

    id = None
    """The Id of this Stroke.
    (type: freestyle.types.Id)
    
    :type: Id
    """

    length_2d = None
    """The 2D length of the Stroke.
    
    :type: float
    """

    medium_type = None
    """The MediumType used for this Stroke.
    (type: freestyle.types.MediumType)
    
    :type: MediumType
    """

    texture_id = None
    """The ID of the texture used to simulate th marks system for this Stroke.
    
    :type: int
    """

    tips = None
    """True if this Stroke uses a texture with tips, and false otherwise.
    
    :type: bool
    """


class StrokeAttribute:
    """Class to define a set of attributes associated with a freestyle.types.StrokeVertex.
                        The attribute set stores the color, alpha and thickness values for a Stroke
                        Vertex.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: A StrokeAttribute object.
            (type: freestyle.types.StrokeAttribute)
        :type brother: StrokeAttribute
        """

    def __init__(self, red, green, blue, alpha, thickness_right, thickness_left):
        """Build a stroke vertex attribute from a set of parameters.
        
        :param red: Red component of a stroke color.
        :type red: float
        :param green: Green component of a stroke color.
        :type green: float
        :param blue: Blue component of a stroke color.
        :type blue: float
        :param alpha: Alpha component of a stroke color.
        :type alpha: float
        :param thickness_right: Stroke thickness on the right.
        :type thickness_right: float
        :param thickness_left: Stroke thickness on the left.
        :type thickness_left: float
        """

    def __init__(self, attribute1, attribute2, t):
        """Interpolation constructor. Build a StrokeAttribute from two
                                    StrokeAttribute objects and an interpolation parameter.
        
        :param attribute1: The first StrokeAttribute object.
            (type: freestyle.types.StrokeAttribute)
        :type attribute1: StrokeAttribute
        :param attribute2: The second StrokeAttribute object.
            (type: freestyle.types.StrokeAttribute)
        :type attribute2: StrokeAttribute
        :param t: The interpolation parameter (0 <= t <= 1).
        :type t: float
        """

    def get_attribute_real(self, name):
        """Returns an attribute of float type.
        
        :param name: The name of the attribute.
        :type name: str
        :return: The attribute value.
        :rtype: float
        """

    def get_attribute_vec2(self, name):
        """Returns an attribute of two-dimensional vector type.
        
        :param name: The name of the attribute.
        :type name: str
        :return: The attribute value.
        :rtype: mathutils.Vector
        """

    def get_attribute_vec3(self, name):
        """Returns an attribute of three-dimensional vector type.
        
        :param name: The name of the attribute.
        :type name: str
        :return: The attribute value.
        :rtype: mathutils.Vector
        """

    def has_attribute_real(self, name):
        """Checks whether the attribute name of float type is available.
        
        :param name: The name of the attribute.
        :type name: str
        :return: True if the attribute is availbale.
        :rtype: bool
        """

    def has_attribute_vec2(self, name):
        """Checks whether the attribute name of two-dimensional vector type
                                    is available.
        
        :param name: The name of the attribute.
        :type name: str
        :return: True if the attribute is availbale.
        :rtype: bool
        """

    def has_attribute_vec3(self, name):
        """Checks whether the attribute name of three-dimensional vector
                                    type is available.
        
        :param name: The name of the attribute.
        :type name: str
        :return: True if the attribute is availbale.
        :rtype: bool
        """

    def set_attribute_real(self, name, value):
        """Adds a user-defined attribute of float type.  If there is no
                                    attribute of the given name, it is added.  Otherwise, the new value
                                    replaces the old one.
        
        :param name: The name of the attribute.
        :type name: str
        :param value: The attribute value.
        :type value: float
        """

    def set_attribute_vec2(self, name, value):
        """Adds a user-defined attribute of two-dimensional vector type.  If
                                    there is no attribute of the given name, it is added.  Otherwise,
                                    the new value replaces the old one.
        
        :param name: The name of the attribute.
        :type name: str
        :param value: The attribute value.
        :type value: mathutils.Vector, list or tuple of 2 real numbers
        """

    def set_attribute_vec3(self, name, value):
        """Adds a user-defined attribute of three-dimensional vector type.
                                    If there is no attribute of the given name, it is added.
                                    Otherwise, the new value replaces the old one.
        
        :param name: The name of the attribute.
        :type name: str
        :param value: The attribute value.
        :type value: mathutils.Vector, list or tuple of 3 real numbers
        """

    alpha = None
    """Alpha component of the stroke color.
    
    :type: float
    """

    color = None
    """RGB components of the stroke color.
    
    :type: mathutils.Color
    """

    thickness = None
    """Right and left components of the stroke thickness.
                                The right (left) component is the thickness on the right (left) of the vertex
                                when following the stroke.
    
    :type: mathutils.Vector
    """

    visible = None
    """The visibility flag.  True if the StrokeVertex is visible.
    
    :type: bool
    """


class StrokeShader:
    """Base class for stroke shaders.  Any stroke shader must inherit from
                        this class and overload the shade() method.  A StrokeShader is
                        designed to modify stroke attributes such as thickness, color,
                        geometry, texture, blending mode, and so on.  The basic way for this
                        operation is to iterate over the stroke vertices of the freestyle.types.Stroke
                        and to modify the freestyle.types.StrokeAttribute of each vertex.  Here is a
                        code example of such an iteration:
    """

    def __init__(self):
        """Default constructor."""

    def shade(self, stroke):
        """The shading method.  Must be overloaded by inherited classes.
        
        :param stroke: A Stroke object.
            (type: freestyle.types.Stroke)
        :type stroke: Stroke
        """

    name = ""
    """The name of the stroke shader.
    
    :type: str
    """


class StrokeVertex:
    """Class hierarchy: freestyle.types.Interface0D > freestyle.types.CurvePoint > freestyle.types.StrokeVertex
    Class to define a stroke vertex.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: A StrokeVertex object.
            (type: freestyle.types.StrokeVertex)
        :type brother: StrokeVertex
        """

    def __init__(self, first_vertex, second_vertex, t3d):
        """Build a stroke vertex from 2 stroke vertices and an interpolation
                                    parameter.
        
        :param first_vertex: The first StrokeVertex.
            (type: freestyle.types.StrokeVertex)
        :type first_vertex: StrokeVertex
        :param second_vertex: The second StrokeVertex.
            (type: freestyle.types.StrokeVertex)
        :type second_vertex: StrokeVertex
        :param t3d: An interpolation parameter.
        :type t3d: float
        """

    def __init__(self, point):
        """Build a stroke vertex from a CurvePoint
        
        :param point: A CurvePoint object.
            (type: freestyle.types.CurvePoint)
        :type point: CurvePoint
        """

    def __init__(self, svertex):
        """Build a stroke vertex from a SVertex
        
        :param svertex: An SVertex object.
            (type: freestyle.types.SVertex)
        :type svertex: SVertex
        """

    def __init__(self, svertex, attribute):
        """Build a stroke vertex from an SVertex and a StrokeAttribute object.
        
        :param svertex: An SVertex object.
            (type: freestyle.types.SVertex)
        :type svertex: SVertex
        :param attribute: A StrokeAttribute object.
            (type: freestyle.types.StrokeAttribute)
        :type attribute: StrokeAttribute
        """

    attribute = None
    """StrokeAttribute for this StrokeVertex.
    (type: freestyle.types.StrokeAttribute)
    
    :type: StrokeAttribute
    """

    curvilinear_abscissa = None
    """Curvilinear abscissa of this StrokeVertex in the Stroke.
    
    :type: float
    """

    point = None
    """2D point coordinates.
    
    :type: mathutils.Vector
    """

    stroke_length = None
    """Stroke length (it is only a value retained by the StrokeVertex,
                                and it won't change the real stroke length).
    
    :type: float
    """

    u = None
    """Curvilinear abscissa of this StrokeVertex in the Stroke.
    
    :type: float
    """


class StrokeVertexIterator:
    """Class hierarchy: freestyle.types.Iterator > freestyle.types.StrokeVertexIterator
    Class defining an iterator designed to iterate over the
                        freestyle.types.StrokeVertex of a freestyle.types.Stroke.  An instance of a
                        StrokeVertexIterator can be obtained from a Stroke by calling
                        iter(), stroke_vertices_begin() or stroke_vertices_begin().  It is iterating
                        over the same vertices as an freestyle.types.Interface0DIterator.  The difference
                        resides in the object access: an Interface0DIterator only allows
                        access to an Interface0D while one might need to access the
                        specialized StrokeVertex type.  In this case, one should use a
                        StrokeVertexIterator.  To call functions of the UnaryFuntion0D type,
                        a StrokeVertexIterator can be converted to an Interface0DIterator by
                        by calling Interface0DIterator(it).
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: A StrokeVertexIterator object.
            (type: freestyle.types.StrokeVertexIterator)
        :type brother: StrokeVertexIterator
        """

    def decremented(self):
        """Returns a copy of a decremented StrokeVertexIterator.
        
        :return: A StrokeVertexIterator pointing the previous StrokeVertex.
        :param : (type: freestyle.types.StrokeVertexIterator)
        :rtype: StrokeVertexIterator
        """

    def incremented(self):
        """Returns a copy of an incremented StrokeVertexIterator.
        
        :return: A StrokeVertexIterator pointing the next StrokeVertex.
        :param : (type: freestyle.types.StrokeVertexIterator)
        :rtype: StrokeVertexIterator
        """

    def reversed(self):
        """Returns a StrokeVertexIterator that traverses stroke vertices in the
                                    reversed order.
        
        :return: A StrokeVertexIterator traversing stroke vertices backward.
        :param : (type: freestyle.types.StrokeVertexIterator)
        :rtype: StrokeVertexIterator
        """

    at_last = None
    """True if the interator points to the last valid element.
                                For its counterpart (pointing to the first valid element), use it.is_begin.
    
    :type: bool
    """

    object = None
    """The StrokeVertex object currently pointed to by this iterator.
    (type: freestyle.types.StrokeVertex)
    
    :type: StrokeVertex
    """

    t = None
    """The curvilinear abscissa of the current point.
    
    :type: float
    """

    u = None
    """The point parameter at the current point in the stroke (0 <= u <= 1).
    
    :type: float
    """


class TVertex:
    """Class hierarchy: freestyle.types.Interface0D > freestyle.types.ViewVertex > freestyle.types.TVertex
    Class to define a T vertex, i.e. an intersection between two edges.
                        It points towards two SVertex and four ViewEdges.  Among the
                        ViewEdges, two are front and the other two are back.  Basically a
                        front edge hides part of a back edge.  So, among the back edges, one
                        is of invisibility N and the other of invisibility N+1.
    """

    def __init__(self):
        """Default constructor."""

    def get_mate(self, viewedge):
        """Returns the mate edge of the ViewEdge given as argument.  If the
                                    ViewEdge is frontEdgeA, frontEdgeB is returned.  If the ViewEdge is
                                    frontEdgeB, frontEdgeA is returned.  Same for back edges.
        
        :param viewedge: A ViewEdge object.
            (type: freestyle.types.ViewEdge)
        :type viewedge: ViewEdge
        :return: The mate edge of the given ViewEdge.
        :param : (type: freestyle.types.ViewEdge)
        :rtype: ViewEdge
        """

    def get_svertex(self, fedge):
        """Returns the SVertex (among the 2) belonging to the given FEdge.
        
        :param fedge: An FEdge object.
            (type: freestyle.types.FEdge)
        :type fedge: FEdge
        :return: The SVertex belonging to the given FEdge.
        :param : (type: freestyle.types.SVertex)
        :rtype: SVertex
        """

    back_svertex = None
    """The SVertex that is further away from the viewpoint.
    (type: freestyle.types.SVertex)
    
    :type: SVertex
    """

    front_svertex = None
    """The SVertex that is closer to the viewpoint.
    (type: freestyle.types.SVertex)
    
    :type: SVertex
    """

    id = None
    """The Id of this TVertex.
    (type: freestyle.types.Id)
    
    :type: Id
    """


class UnaryFunction0D:
    """Base class for Unary Functions (functors) working on
                        freestyle.types.Interface0DIterator.  A unary function will be used by
                        invoking __call__() on an Interface0DIterator.  In Python, several
                        different subclasses of UnaryFunction0D are used depending on the
                        types of functors' return values.  For example, you would inherit from
                        a freestyle.types.UnaryFunction0DDouble if you wish to define a function that
                        returns a double value.  Available UnaryFunction0D subclasses are:
    * freestyle.types.UnaryFunction0DDouble
    * freestyle.types.UnaryFunction0DEdgeNature
    * freestyle.types.UnaryFunction0DFloat
    * freestyle.types.UnaryFunction0DId
    * freestyle.types.UnaryFunction0DMaterial
    * freestyle.types.UnaryFunction0DUnsigned
    * freestyle.types.UnaryFunction0DVec2f
    * freestyle.types.UnaryFunction0DVec3f
    * freestyle.types.UnaryFunction0DVectorViewShape
    * freestyle.types.UnaryFunction0DViewShape
    """

    name = ""
    """The name of the unary 0D function.
    
    :type: str
    """


class UnaryFunction0DDouble:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DDouble
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface0DIterator and return a float value.
    """

    def __init__(self):
        """Default constructor."""


class UnaryFunction0DEdgeNature:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DEdgeNature
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface0DIterator and return a freestyle.types.Nature object.
    """

    def __init__(self):
        """Default constructor."""


class UnaryFunction0DFloat:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DFloat
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface0DIterator and return a float value.
    """

    def __init__(self):
        """Default constructor."""


class UnaryFunction0DId:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DId
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface0DIterator and return an freestyle.types.Id object.
    """

    def __init__(self):
        """Default constructor."""


class UnaryFunction0DMaterial:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DMaterial
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface0DIterator and return a freestyle.types.Material object.
    """

    def __init__(self):
        """Default constructor."""


class UnaryFunction0DUnsigned:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DUnsigned
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface0DIterator and return an int value.
    """

    def __init__(self):
        """Default constructor."""


class UnaryFunction0DVec2f:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DVec2f
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface0DIterator and return a 2D vector.
    """

    def __init__(self):
        """Default constructor."""


class UnaryFunction0DVec3f:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DVec3f
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface0DIterator and return a 3D vector.
    """

    def __init__(self):
        """Default constructor."""


class UnaryFunction0DVectorViewShape:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DVectorViewShape
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface0DIterator and return a list of freestyle.types.ViewShape
                        objects.
    """

    def __init__(self):
        """Default constructor."""


class UnaryFunction0DViewShape:
    """Class hierarchy: freestyle.types.UnaryFunction0D > freestyle.types.UnaryFunction0DViewShape
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface0DIterator and return a freestyle.types.ViewShape object.
    """

    def __init__(self):
        """Default constructor."""


class UnaryFunction1D:
    """Base class for Unary Functions (functors) working on
                        freestyle.types.Interface1D.  A unary function will be used by invoking
                        __call__() on an Interface1D.  In Python, several different subclasses
                        of UnaryFunction1D are used depending on the types of functors' return
                        values.  For example, you would inherit from a
                        freestyle.types.UnaryFunction1DDouble if you wish to define a function that
                        returns a double value.  Available UnaryFunction1D subclasses are:
    * freestyle.types.UnaryFunction1DDouble
    * freestyle.types.UnaryFunction1DEdgeNature
    * freestyle.types.UnaryFunction1DFloat
    * freestyle.types.UnaryFunction1DUnsigned
    * freestyle.types.UnaryFunction1DVec2f
    * freestyle.types.UnaryFunction1DVec3f
    * freestyle.types.UnaryFunction1DVectorViewShape
    * freestyle.types.UnaryFunction1DVoid
    """

    name = ""
    """The name of the unary 1D function.
    
    :type: str
    """


class UnaryFunction1DDouble:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DDouble
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface1D and return a float value.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, integration_type):
        """Builds a unary 1D function using the integration method given as
                                    argument.
        
        :param integration_type: An integration method.
            (type: freestyle.types.IntegrationType)
        :type integration_type: IntegrationType
        """

    integration_type = None
    """The integration method.
    (type: freestyle.types.IntegrationType)
    
    :type: IntegrationType
    """


class UnaryFunction1DEdgeNature:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DEdgeNature
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface1D and return a freestyle.types.Nature object.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, integration_type):
        """Builds a unary 1D function using the integration method given as
                                    argument.
        
        :param integration_type: An integration method.
            (type: freestyle.types.IntegrationType)
        :type integration_type: IntegrationType
        """

    integration_type = None
    """The integration method.
    (type: freestyle.types.IntegrationType)
    
    :type: IntegrationType
    """


class UnaryFunction1DFloat:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DFloat
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface1D and return a float value.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, integration_type):
        """Builds a unary 1D function using the integration method given as
                                    argument.
        
        :param integration_type: An integration method.
            (type: freestyle.types.IntegrationType)
        :type integration_type: IntegrationType
        """

    integration_type = None
    """The integration method.
    (type: freestyle.types.IntegrationType)
    
    :type: IntegrationType
    """


class UnaryFunction1DUnsigned:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DUnsigned
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface1D and return an int value.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, integration_type):
        """Builds a unary 1D function using the integration method given as
                                    argument.
        
        :param integration_type: An integration method.
            (type: freestyle.types.IntegrationType)
        :type integration_type: IntegrationType
        """

    integration_type = None
    """The integration method.
    (type: freestyle.types.IntegrationType)
    
    :type: IntegrationType
    """


class UnaryFunction1DVec2f:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVec2f
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface1D and return a 2D vector.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, integration_type):
        """Builds a unary 1D function using the integration method given as
                                    argument.
        
        :param integration_type: An integration method.
            (type: freestyle.types.IntegrationType)
        :type integration_type: IntegrationType
        """

    integration_type = None
    """The integration method.
    (type: freestyle.types.IntegrationType)
    
    :type: IntegrationType
    """


class UnaryFunction1DVec3f:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVec3f
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface1D and return a 3D vector.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, integration_type):
        """Builds a unary 1D function using the integration method given as
                                    argument.
        
        :param integration_type: An integration method.
            (type: freestyle.types.IntegrationType)
        :type integration_type: IntegrationType
        """

    integration_type = None
    """The integration method.
    (type: freestyle.types.IntegrationType)
    
    :type: IntegrationType
    """


class UnaryFunction1DVectorViewShape:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVectorViewShape
    Base class for unary functions (functors) that work on
                        freestyle.types.Interface1D and return a list of freestyle.types.ViewShape
                        objects.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, integration_type):
        """Builds a unary 1D function using the integration method given as
                                    argument.
        
        :param integration_type: An integration method.
            (type: freestyle.types.IntegrationType)
        :type integration_type: IntegrationType
        """

    integration_type = None
    """The integration method.
    (type: freestyle.types.IntegrationType)
    
    :type: IntegrationType
    """


class UnaryFunction1DVoid:
    """Class hierarchy: freestyle.types.UnaryFunction1D > freestyle.types.UnaryFunction1DVoid
    Base class for unary functions (functors) working on
                        freestyle.types.Interface1D.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, integration_type):
        """Builds a unary 1D function using the integration method given as
                                    argument.
        
        :param integration_type: An integration method.
            (type: freestyle.types.IntegrationType)
        :type integration_type: IntegrationType
        """

    integration_type = None
    """The integration method.
    (type: freestyle.types.IntegrationType)
    
    :type: IntegrationType
    """


class UnaryPredicate0D:
    """Base class for unary predicates that work on
                        freestyle.types.Interface0DIterator.  A UnaryPredicate0D is a functor that
                        evaluates a condition on an Interface0DIterator and returns true or
                        false depending on whether this condition is satisfied or not.  The
                        UnaryPredicate0D is used by invoking its __call__() method.  Any
                        inherited class must overload the __call__() method.
    """

    def __init__(self):
        """Default constructor."""

    def __call__(self, it):
        """Must be overload by inherited classes.
        
        :param it: The Interface0DIterator pointing onto the Interface0D at
                                                    which we wish to evaluate the predicate.
            (type: freestyle.types.Interface0DIterator)
        :type it: Interface0DIterator
        :return: True if the condition is satisfied, false otherwise.
        :rtype: bool
        """

    name = ""
    """The name of the unary 0D predicate.
    
    :type: str
    """


class UnaryPredicate1D:
    """Base class for unary predicates that work on freestyle.types.Interface1D.  A
                        UnaryPredicate1D is a functor that evaluates a condition on a
                        Interface1D and returns true or false depending on whether this
                        condition is satisfied or not.  The UnaryPredicate1D is used by
                        invoking its __call__() method.  Any inherited class must overload the
                        __call__() method.
    """

    def __init__(self):
        """Default constructor."""

    def __call__(self, inter):
        """Must be overload by inherited classes.
        
        :param inter: The Interface1D on which we wish to evaluate the predicate.
            (type: freestyle.types.Interface1D)
        :type inter: Interface1D
        :return: True if the condition is satisfied, false otherwise.
        :rtype: bool
        """

    name = ""
    """The name of the unary 1D predicate.
    
    :type: str
    """


class ViewEdge:
    """Class hierarchy: freestyle.types.Interface1D > freestyle.types.ViewEdge
    Class defining a ViewEdge.  A ViewEdge in an edge of the image graph.
                        it connects two freestyle.types.ViewVertex objects.  It is made by connecting
                        a set of FEdges.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: A ViewEdge object.
            (type: freestyle.types.ViewEdge)
        :type brother: ViewEdge
        """

    def update_fedges(self):
        """Sets Viewedge to this for all embedded fedges."""

    chaining_time_stamp = None
    """The time stamp of this ViewEdge.
    
    :type: int
    """

    first_fedge = None
    """The first FEdge that constitutes this ViewEdge.
    (type: freestyle.types.FEdge)
    
    :type: FEdge
    """

    first_viewvertex = None
    """The first ViewVertex.
    (type: freestyle.types.ViewVertex)
    
    :type: ViewVertex
    """

    id = None
    """The Id of this ViewEdge.
    (type: freestyle.types.Id)
    
    :type: Id
    """

    is_closed = None
    """True if this ViewEdge forms a closed loop.
    
    :type: bool
    """

    last_fedge = None
    """The last FEdge that constitutes this ViewEdge.
    (type: freestyle.types.FEdge)
    
    :type: FEdge
    """

    last_viewvertex = None
    """The second ViewVertex.
    (type: freestyle.types.ViewVertex)
    
    :type: ViewVertex
    """

    nature = None
    """The nature of this ViewEdge.
    (type: freestyle.types.Nature)
    
    :type: Nature
    """

    occludee = None
    """The shape that is occluded by the ViewShape to which this ViewEdge
                                belongs to.  If no object is occluded, this property is set to None.
    (type: freestyle.types.ViewShape)
    
    :type: ViewShape
    """

    qi = None
    """The quantitative invisibility.
    
    :type: int
    """

    viewshape = None
    """The ViewShape to which this ViewEdge belongs to.
    (type: freestyle.types.ViewShape)
    
    :type: ViewShape
    """


class ViewEdgeIterator:
    """Class hierarchy: freestyle.types.Iterator > freestyle.types.ViewEdgeIterator
    Base class for iterators over ViewEdges of the freestyle.types.ViewMap Graph.
                        Basically the increment() operator of this class should be able to
                        take the decision of "where" (on which ViewEdge) to go when pointing
                        on a given ViewEdge.
    """

    def __init__(self, begin=None, orientation=True):
        """Builds a ViewEdgeIterator from a starting ViewEdge and its
                                    orientation.
        
        :param begin: The ViewEdge from where to start the iteration.
            (type: freestyle.types.ViewEdge or None)
        :type begin: ViewEdge or None
        :param orientation: If true, we'll look for the next ViewEdge among
                                                            the ViewEdges that surround the ending ViewVertex of begin.  If
                                                            false, we'll search over the ViewEdges surrounding the ending
                                                            ViewVertex of begin.
        :type orientation: bool
        """

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: A ViewEdgeIterator object.
            (type: freestyle.types.ViewEdgeIterator)
        :type brother: ViewEdgeIterator
        """

    def change_orientation(self):
        """Changes the current orientation."""

    begin = None
    """The first ViewEdge used for the iteration.
    (type: freestyle.types.ViewEdge)
    
    :type: ViewEdge
    """

    current_edge = None
    """The ViewEdge object currently pointed by this iterator.
    (type: freestyle.types.ViewEdge)
    
    :type: ViewEdge
    """

    object = None
    """The ViewEdge object currently pointed by this iterator.
    (type: freestyle.types.ViewEdge)
    
    :type: ViewEdge
    """

    orientation = None
    """The orientation of the pointed ViewEdge in the iteration.
                                If true, the iterator looks for the next ViewEdge among those ViewEdges
                                that surround the ending ViewVertex of the "begin" ViewEdge.  If false,
                                the iterator searches over the ViewEdges surrounding the ending ViewVertex
                                of the "begin" ViewEdge.
    
    :type: bool
    """


class ViewMap:
    """Class defining the ViewMap."""

    def __init__(self):
        """Default constructor."""

    def get_closest_fedge(self, x, y):
        """Gets the FEdge nearest to the 2D point specified as arguments.
        
        :param x: X coordinate of a 2D point.
        :type x: float
        :param y: Y coordinate of a 2D point.
        :type y: float
        :return: The FEdge nearest to the specified 2D point.
        :param : (type: freestyle.types.FEdge)
        :rtype: FEdge
        """

    def get_closest_viewedge(self, x, y):
        """Gets the ViewEdge nearest to the 2D point specified as arguments.
        
        :param x: X coordinate of a 2D point.
        :type x: float
        :param y: Y coordinate of a 2D point.
        :type y: float
        :return: The ViewEdge nearest to the specified 2D point.
        :param : (type: freestyle.types.ViewEdge)
        :rtype: ViewEdge
        """

    scene_bbox = None
    """The 3D bounding box of the scene.
    (type: freestyle.types.BBox)
    
    :type: BBox
    """


class ViewShape:
    """Class gathering the elements of the ViewMap (i.e., freestyle.types.ViewVertex
                        and freestyle.types.ViewEdge) that are issued from the same input shape.
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, brother):
        """Copy constructor.
        
        :param brother: A ViewShape object.
            (type: freestyle.types.ViewShape)
        :type brother: ViewShape
        """

    def __init__(self, sshape):
        """Builds a ViewShape from an SShape.
        
        :param sshape: An SShape object.
            (type: freestyle.types.SShape)
        :type sshape: SShape
        """

    def add_edge(self, edge):
        """Adds a ViewEdge to the list of ViewEdge objects.
        
        :param edge: A ViewEdge object.
            (type: freestyle.types.ViewEdge)
        :type edge: ViewEdge
        """

    def add_vertex(self, vertex):
        """Adds a ViewVertex to the list of the ViewVertex objects.
        
        :param vertex: A ViewVertex object.
            (type: freestyle.types.ViewVertex)
        :type vertex: ViewVertex
        """

    edges = None
    """The list of ViewEdge objects contained in this ViewShape.
    (type: List of freestyle.types.ViewEdge objects)
    
    :type: List
    """

    id = None
    """The Id of this ViewShape.
    (type: freestyle.types.Id)
    
    :type: Id
    """

    library_path = None
    """The library path of the ViewShape.
    
    :type: str, or None if the ViewShape is not part of a library
    """

    name = ""
    """The name of the ViewShape.
    
    :type: str
    """

    sshape = None
    """The SShape on top of which this ViewShape is built.
    (type: freestyle.types.SShape)
    
    :type: SShape
    """

    vertices = None
    """The list of ViewVertex objects contained in this ViewShape.
    (type: List of freestyle.types.ViewVertex objects)
    
    :type: List
    """


class ViewVertex:
    """Class hierarchy: freestyle.types.Interface0D > freestyle.types.ViewVertex
    Class to define a view vertex.  A view vertex is a feature vertex
                        corresponding to a point of the image graph, where the characteristics
                        of an edge (e.g., nature and visibility) might change.  A
                        freestyle.types.ViewVertex can be of two kinds: A freestyle.types.TVertex when it
                        corresponds to the intersection between two ViewEdges or a
                        freestyle.types.NonTVertex when it corresponds to a vertex of the initial
                        input mesh (it is the case for vertices such as corners for example).
                        Thus, this class can be specialized into two classes, the
                        freestyle.types.TVertex class and the freestyle.types.NonTVertex class.
    """

    def edges_begin(self):
        """Returns an iterator over the ViewEdges that goes to or comes from
                                    this ViewVertex pointing to the first ViewEdge of the list. The
                                    orientedViewEdgeIterator allows to iterate in CCW order over these
                                    ViewEdges and to get the orientation for each ViewEdge
                                    (incoming/outgoing).
        
        :return: An orientedViewEdgeIterator pointing to the first ViewEdge.
        :param : (type: freestyle.types.orientedViewEdgeIterator)
        :rtype: orientedViewEdgeIterator
        """

    def edges_end(self):
        """Returns an orientedViewEdgeIterator over the ViewEdges around this
                                    ViewVertex, pointing after the last ViewEdge.
        
        :return: An orientedViewEdgeIterator pointing after the last ViewEdge.
        :param : (type: freestyle.types.orientedViewEdgeIterator)
        :rtype: orientedViewEdgeIterator
        """

    def edges_iterator(self, edge):
        """Returns an orientedViewEdgeIterator pointing to the ViewEdge given
                                    as argument.
        
        :param edge: A ViewEdge object.
            (type: freestyle.types.ViewEdge)
        :type edge: ViewEdge
        :return: An orientedViewEdgeIterator pointing to the given ViewEdge.
        :param : (type: freestyle.types.orientedViewEdgeIterator)
        :rtype: orientedViewEdgeIterator
        """

    nature = None
    """The nature of this ViewVertex.
    (type: freestyle.types.Nature)
    
    :type: Nature
    """


class orientedViewEdgeIterator:
    """Class hierarchy: freestyle.types.Iterator > freestyle.types.orientedViewEdgeIterator
    Class representing an iterator over oriented ViewEdges around a
                        freestyle.types.ViewVertex.  This iterator allows a CCW iteration (in the image
                        plane).  An instance of an orientedViewEdgeIterator can only be
                        obtained from a ViewVertex by calling edges_begin() or edges_end().
    """

    def __init__(self):
        """Default constructor."""

    def __init__(self, iBrother):
        """Copy constructor.
        
        :param iBrother: An orientedViewEdgeIterator object.
            (type: freestyle.types.orientedViewEdgeIterator)
        :type iBrother: orientedViewEdgeIterator
        """

    object = None
    """The oriented ViewEdge (i.e., a tuple of the pointed ViewEdge and a boolean
                                value) currently pointed to by this iterator. If the boolean value is true,
                                the ViewEdge is incoming.
    (type: (freestyle.types.ViewEdge, bool))
    
    :type: (ViewEdge, bool)
    """
