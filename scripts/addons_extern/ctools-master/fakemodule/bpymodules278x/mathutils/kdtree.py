class KDTree:
    """KdTree(size) -> new kd-tree initialized to hold size items.
    <Note> mathutils.kdtree.KDTree.balance must have been called before using any of the find methods.
    <Note> This builds the entire tree, avoid calling after each insertion.
    """

    def balance(self):
        """Balance the tree."""

    def find(self, co, filter=None):
        """Find nearest point to co.
        
        :param co: 3d coordinates.
        :type co: float triplet
        :param filter: function which takes an index and returns True for indices to include in the search.
        :type filter: callable
        :return: Returns (Vector, index, distance).
        :rtype: tuple
        """

    def find_n(self, co, n):
        """Find nearest n points to co.
        
        :param co: 3d coordinates.
        :type co: float triplet
        :param n: Number of points to find.
        :type n: int
        :return: Returns a list of tuples (Vector, index, distance).
        :rtype: list
        """

    def find_range(self, co, radius):
        """Find all points within radius of co.
        
        :param co: 3d coordinates.
        :type co: float triplet
        :param radius: Distance to search for points.
        :type radius: float
        :return: Returns a list of tuples (Vector, index, distance).
        :rtype: list
        """

    def insert(self, co, index):
        """Insert a point into the KDTree.
        
        :param co: Point 3d position.
        :type co: float triplet
        :param index: The index of the point.
        :type index: int
        """
