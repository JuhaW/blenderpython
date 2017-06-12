import sys


class BVHTree:
    """"""

    def FromBMesh(self, bmesh, epsilon=0.0):
        """BVH tree based on BMesh data.
        
        :param bmesh: BMesh data.
        :type bmesh: BMesh
        :param epsilon: Increase the threshold for detecting overlap and raycast hits.
        :type epsilon: float
        """

    def FromObject(self, object, scene, deform=True, render=False, cage=False, epsilon=0.0):
        """BVH tree based on Object data.
        
        :param object: Object data.
        :type object: Object
        :param scene: Scene data to use for evaluating the mesh.
        :type scene: Scene
        :param deform: Use mesh with deformations.
        :type deform: bool
        :param render: Use render settings.
        :type render: bool
        :param cage: Use render settings.
        :type cage: bool
        :param epsilon: Increase the threshold for detecting overlap and raycast hits.
        :type epsilon: float
        """

    def FromPolygons(self, vertices, polygons, all_triangles=False, epsilon=0.0):
        """BVH tree constructed geometry passed in as arguments.
        
        :param vertices: float triplets each representing (x, y, z)
        :type vertices: float triplet sequence
        :param polygons: Sequence of polyugons, each containing indices to the vertices argument.
            (type: Sequence of sequences containing ints)
        :type polygons: Sequence
        :param all_triangles: Use when all polygons are triangles for more efficient conversion.
        :type all_triangles: bool
        :param epsilon: Increase the threshold for detecting overlap and raycast hits.
        :type epsilon: float
        """

    def find_nearest(self, origin, distance=1.84467e+19):
        """Find the nearest element to a point.
        
        :param co: Find nearest element to this point.
        :type co: Vector
        :param distance: Maximum distance threshold.
        :type distance: float
        :return: Returns a tuple
                                                    (Vector location, Vector normal, int index, float distance),
                                                    Values will all be None if no hit is found.
        :rtype: tuple
        """

    def find_nearest_range(self, origin, distance=1.84467e+19):
        """Find the nearest elements to a point in the distance range.
        
        :param co: Find nearest elements to this point.
        :type co: Vector
        :param distance: Maximum distance threshold.
        :type distance: float
        :return: Returns a list of tuples
                                                    (Vector location, Vector normal, int index, float distance),
        :rtype: list
        """

    def overlap(self, other_tree):
        """Find overlapping indices between 2 trees.
        
        :param other_tree: Other tree to preform overlap test on.
            (type: mathutils.bvhtree.BVHTree)
        :type other_tree: BVHTree
        :return: Returns a list of unique index pairs,      the first index referencing this tree, the second referencing the other_tree.
        :rtype: list
        """

    def ray_cast(self, origin, direction, distance=sys.float_info.max):
        """Cast a ray onto the mesh.
        
        :param co: Start location of the ray in object space.
        :type co: Vector
        :param direction: Direction of the ray in object space.
        :type direction: Vector
        :param distance: Maximum distance threshold.
        :type distance: float
        :return: Returns a tuple
                                                    (Vector location, Vector normal, int index, float distance),
                                                    Values will all be None if no hit is found.
        :rtype: tuple
        """
