from . import bvhtree
from . import geometry
from . import interpolate
from . import kdtree
from . import noise
import sys


class Color:
    def __new__(cls, rgb):
        """This object gives access to Colors in Blender.
        
        :param rgb: (r, g, b) color values
        :type rgb: 3d vector
        """
        return super().__new__(cls)

    def copy(self):
        """Returns a copy of this color.
        <Note> use this to get a copy of a wrapped color with
                                            no reference to the original data.
        
        :return: A copy of the color.
        :param : (type: mathutils.Color)
        :rtype: Color
        """

    def freeze(self):
        """Make this object immutable.
        After this the object can be hashed, used in dictionaries & sets.
        
        :return: An instance of this object.
        """

    b = None
    """Blue color channel.
    
    :type: float
    """

    g = None
    """Green color channel.
    
    :type: float
    """

    h = None
    """HSV Hue component in [0, 1].
    
    :type: float
    """

    hsv = None
    """HSV Values in [0, 1].
    
    :type: float triplet
    """

    is_frozen = None
    """True when this object has been frozen (read-only).
    
    :type: bool
    """

    is_wrapped = None
    """True when this object wraps external data (read-only).
    
    :type: bool
    """

    owner = None
    """The item this is wrapping or None  (read-only)."""

    r = None
    """Red color channel.
    
    :type: float
    """

    s = None
    """HSV Saturation component in [0, 1].
    
    :type: float
    """

    v = None
    """HSV Value component in [0, 1].
    
    :type: float
    """


class Euler:
    def __new__(cls, angles, order='XYZ'):
        """This object gives access to Eulers in Blender.
        
        :param angles: Three angles, in radians.
        :type angles: 3d vector
        :param order: Optional order of the angles, a permutation of XYZ.
        :type order: str
        """
        return super().__new__(cls)

    def copy(self):
        """Returns a copy of this euler.
        <Note> use this to get a copy of a wrapped euler with
                                            no reference to the original data.
        
        :return: A copy of the euler.
        :param : (type: mathutils.Euler)
        :rtype: Euler
        """

    def freeze(self):
        """Make this object immutable.
        After this the object can be hashed, used in dictionaries & sets.
        
        :return: An instance of this object.
        """

    def make_compatible(self, other):
        """Make this euler compatible with another,
                                    so interpolating between them works as intended.
        <Note> the rotation order is not taken into account for this function.
        """

    def rotate(self, other):
        """Rotates the euler by another mathutils value.
        
        :param other: rotation component of mathutils value
            (type: mathutils.Euler, mathutils.Quaternion or mathutils.Matrix)
        :type other: Euler, Quaternion or Matrix
        """

    def rotate_axis(self, axis, angle):
        """Rotates the euler a certain amount and returning a unique euler rotation
                                    (no 720 degree pitches).
        
        :param axis: single character in ['X, 'Y', 'Z'].
        :type axis: str
        :param angle: angle in radians.
        :type angle: float
        """

    def to_matrix(self):
        """Return a matrix representation of the euler.
        
        :return: A 3x3 roation matrix representation of the euler.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def to_quaternion(self):
        """Return a quaternion representation of the euler.
        
        :return: Quaternion representation of the euler.
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def zero(self):
        """Set all values to zero."""

    is_frozen = None
    """True when this object has been frozen (read-only).
    
    :type: bool
    """

    is_wrapped = None
    """True when this object wraps external data (read-only).
    
    :type: bool
    """

    order = ""
    """Euler rotation order.
    (type: string in ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'])
    
    :type: str
    """

    owner = None
    """The item this is wrapping or None  (read-only)."""

    x = None
    """Euler axis angle in radians.
    
    :type: float
    """

    y = None
    """Euler axis angle in radians.
    
    :type: float
    """

    z = None
    """Euler axis angle in radians.
    
    :type: float
    """


class Matrix:
    def __new__(cls, rows:"Optional"):
        """This object gives access to Matrices in Blender, supporting square and rectangular
                            matrices from 2x2 up to 4x4.
        
        :param rows: Sequence of rows.
                                            When ommitted, a 4x4 identity matrix is constructed.
        :type rows: 2d number sequence
        """
        return super().__new__(cls)

    def Identity(self, size):
        """Create an identity matrix.
        (type: Matrix Access)
        
        :param size: The size of the identity matrix to construct [2, 4].
        :type size: int
        :return: A new identity matrix.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def OrthoProjection(self, axis, size):
        """Create a matrix to represent an orthographic projection.
        (type: Matrix Access)
        
        :param axis: Can be any of the following: ['X', 'Y', 'XY', 'XZ', 'YZ'],
                                                            where a single axis is for a 2D matrix.
                                                            Or a vector for an arbitrary axis
            (type: string or mathutils.Vector)
        :type axis: string or Vector
        :param size: The size of the projection matrix to construct [2, 4].
        :type size: int
        :return: A new projection matrix.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def Rotation(self, angle, size, axis):
        """Create a matrix representing a rotation.
        (type: Matrix Access)
        
        :param angle: The angle of rotation desired, in radians.
        :type angle: float
        :param size: The size of the rotation matrix to construct [2, 4].
        :type size: int
        :param axis: a string in ['X', 'Y', 'Z'] or a 3D Vector Object
                                                            (optional when size is 2).
            (type: string or mathutils.Vector)
        :type axis: string or Vector
        :return: A new rotation matrix.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def Scale(self, factor, size, axis):
        """Create a matrix representing a scaling.
        (type: Matrix Access)
        
        :param factor: The factor of scaling to apply.
        :type factor: float
        :param size: The size of the scale matrix to construct [2, 4].
        :type size: int
        :param axis: Direction to influence scale. (optional).
            (type: mathutils.Vector)
        :type axis: Vector
        :return: A new scale matrix.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def Shear(self, plane, size, factor):
        """Create a matrix to represent an shear transformation.
        (type: Matrix Access)
        
        :param plane: Can be any of the following: ['X', 'Y', 'XY', 'XZ', 'YZ'],
                                                            where a single axis is for a 2D matrix only.
        :type plane: str
        :param size: The size of the shear matrix to construct [2, 4].
        :type size: int
        :param factor: The factor of shear to apply. For a 3 or 4 size matrix
                                                            pass a pair of floats corresponding with the plane axis.
        :type factor: float or float pair
        :return: A new shear matrix.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def Translation(self, vector):
        """Create a matrix representing a translation.
        (type: Matrix Access)
        
        :param vector: The translation vector.
            (type: mathutils.Vector)
        :type vector: Vector
        :return: An identity matrix with a translation.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def adjugate(self):
        """Set the matrix to its adjugate.
        <Note> When the matrix cannot be adjugated a ValueError exception is raised.
        <See also> Adjugate matrix <https://en.wikipedia.org/wiki/Adjugate_matrix> on Wikipedia.
        (type: Matrix Access)
        """

    def adjugated(self):
        """Return an adjugated copy of the matrix.
        <Note> When the matrix cant be adjugated a ValueError exception is raised.
        (type: Matrix Access)
        
        :return: the adjugated matrix.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def copy(self):
        """Returns a copy of this matrix.
        (type: Matrix Access)
        
        :return: an instance of itself
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def decompose(self):
        """Return the location, rotation and scale components of this matrix.
        (type: Matrix Access)
        
        :return: loc, rot, scale triple.
        :param : (type: (mathutils.Vector, mathutils.Quaternion, mathutils.Vector))
        :rtype: (Vector, Quaternion, Vector)
        """

    def determinant(self):
        """Return the determinant of a matrix.
        <See also> Determinant <https://en.wikipedia.org/wiki/Determinant> on Wikipedia.
        (type: Matrix Access)
        
        :return: Return the determinant of a matrix.
        :rtype: float
        """

    def freeze(self):
        """Make this object immutable.
        After this the object can be hashed, used in dictionaries & sets.
        (type: Matrix Access)
        
        :return: An instance of this object.
        """

    def identity(self):
        """Set the matrix to the identity matrix.
        <Note> An object with a location and rotation of zero, and a scale of one
                                            will have an identity matrix.
        <See also> Identity matrix <https://en.wikipedia.org/wiki/Identity_matrix> on Wikipedia.
        (type: Matrix Access)
        """

    def invert(self, fallback=None):
        """Set the matrix to its inverse.
        <See also> Inverse matrix <https://en.wikipedia.org/wiki/Inverse_matrix> on Wikipedia.
        (type: Matrix Access)
        
        :param fallback: Set the matrix to this value when the inverse cannot be calculated
                                                    (instead of raising a ValueError exception).
            (type: mathutils.Matrix)
        :type fallback: Matrix
        """

    def invert_safe(self):
        """Set the matrix to its inverse, will never error.
                                    If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
                                    If tweaked matrix is still degenerated, set to the identity matrix instead.
        <See also> Inverse Matrix <https://en.wikipedia.org/wiki/Inverse_matrix> on Wikipedia.
        (type: Matrix Access)
        """

    def inverted(self, fallback=None):
        """Return an inverted copy of the matrix.
        (type: Matrix Access)
        
        :param fallback: return this when the inverse can't be calculated
                                                    (instead of raising a ValueError).
        :type fallback: bpy.types.KeyMapItem.any
        :return: the inverted matrix or fallback when given.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def inverted_safe(self):
        """Return an inverted copy of the matrix, will never error.
                                    If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
                                    If tweaked matrix is still degenerated, return the identity matrix instead.
        (type: Matrix Access)
        
        :return: the inverted matrix.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def lerp(self, other, factor):
        """Returns the interpolation of two matrices.
        (type: Matrix Access)
        
        :param other: value to interpolate with.
            (type: mathutils.Matrix)
        :type other: Matrix
        :param factor: The interpolation value in [0.0, 1.0].
        :type factor: float
        :return: The interpolated matrix.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def normalize(self):
        """Normalize each of the matrix columns.
        (type: Matrix Access)
        """

    def normalized(self):
        """Return a column normalized matrix
        (type: Matrix Access)
        
        :return: a column normalized matrix
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def resize_4x4(self):
        """Resize the matrix to 4x4.
        (type: Matrix Access)
        """

    def rotate(self, other):
        """Rotates the matrix by another mathutils value.
        <Note> If any of the columns are not unit length this may not have desired results.
        (type: Matrix Access)
        
        :param other: rotation component of mathutils value
            (type: mathutils.Euler, mathutils.Quaternion or mathutils.Matrix)
        :type other: Euler, Quaternion or Matrix
        """

    def to_3x3(self):
        """Return a 3x3 copy of this matrix.
        (type: Matrix Access)
        
        :return: a new matrix.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def to_4x4(self):
        """Return a 4x4 copy of this matrix.
        (type: Matrix Access)
        
        :return: a new matrix.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def to_euler(self, order, euler_compat):
        """Return an Euler representation of the rotation matrix
                                    (3x3 or 4x4 matrix only).
        (type: Matrix Access)
        
        :param order: Optional rotation order argument in
                                                            ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
        :type order: str
        :param euler_compat: Optional euler argument the new euler will be made
                                                            compatible with (no axis flipping between them).
                                                            Useful for converting a series of matrices to animation curves.
            (type: mathutils.Euler)
        :type euler_compat: Euler
        :return: Euler representation of the matrix.
        :param : (type: mathutils.Euler)
        :rtype: Euler
        """

    def to_quaternion(self):
        """Return a quaternion representation of the rotation matrix.
        (type: Matrix Access)
        
        :return: Quaternion representation of the rotation matrix.
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def to_scale(self):
        """Return the scale part of a 3x3 or 4x4 matrix.
        <Note> This method does not return a negative scale on any axis because it is not possible to obtain this data from the matrix alone.
        (type: Matrix Access)
        
        :return: Return the scale of a matrix.
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def to_translation(self):
        """Return the translation part of a 4 row matrix.
        (type: Matrix Access)
        
        :return: Return the translation of a matrix.
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def transpose(self):
        """Set the matrix to its transpose.
        <See also> Transpose <https://en.wikipedia.org/wiki/Transpose> on Wikipedia.
        (type: Matrix Access)
        """

    def transposed(self):
        """Return a new, transposed matrix.
        (type: Matrix Access)
        
        :return: a transposed matrix
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    def zero(self):
        """Set all the matrix values to zero.
        (type: Matrix Access)
        
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    col = None
    """Access the matix by colums, 3x3 and 4x4 only, (read-only).
    (type: Matrix Access)
    
    :type: collections.Sequence[Vector]
    """

    is_frozen = None
    """True when this object has been frozen (read-only).
    (type: Matrix Access)
    
    :type: bool
    """

    is_negative = None
    """True if this matrix results in a negative scale, 3x3 and 4x4 only, (read-only).
    (type: Matrix Access)
    
    :type: bool
    """

    is_orthogonal = None
    """True if this matrix is orthogonal, 3x3 and 4x4 only, (read-only).
    (type: Matrix Access)
    
    :type: bool
    """

    is_orthogonal_axis_vectors = None
    """True if this matrix has got orthogonal axis vectors, 3x3 and 4x4 only, (read-only).
    (type: Matrix Access)
    
    :type: bool
    """

    is_wrapped = None
    """True when this object wraps external data (read-only).
    (type: Matrix Access)
    
    :type: bool
    """

    median_scale = None
    """The average scale applied to each axis (read-only).
    (type: Matrix Access)
    
    :type: float
    """

    owner = None
    """The item this is wrapping or None  (read-only).
    (type: Matrix Access)
    """

    row = None
    """Access the matix by rows (default), (read-only).
    (type: Matrix Access)
    
    :type: collections.Sequence[Vector]
    """

    translation = None
    """The translation component of the matrix.
    (type: Matrix Access)
    
    :type: Vector
    """


class Quaternion:
    def __new__(cls, seq:"Optional"):
        """This object gives access to Quaternions in Blender.
        The constructor takes arguments in various forms:
        
        :param seq: size 3 or 4
            (type: mathutils.Vector)
        :type seq: Vector
        :param angle: rotation angle, in radians
        :type angle: float
        """
        return super().__new__(cls)

    def conjugate(self):
        """Set the quaternion to its conjugate (negate x, y, z)."""

    def conjugated(self):
        """Return a new conjugated quaternion.
        
        :return: a new quaternion.
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def copy(self):
        """Returns a copy of this quaternion.
        <Note> use this to get a copy of a wrapped quaternion with
                                            no reference to the original data.
        
        :return: A copy of the quaternion.
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def cross(self, other):
        """Return the cross product of this quaternion and another.
        
        :param other: The other quaternion to perform the cross product with.
            (type: mathutils.Quaternion)
        :type other: Quaternion
        :return: The cross product.
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def dot(self, other):
        """Return the dot product of this quaternion and another.
        
        :param other: The other quaternion to perform the dot product with.
            (type: mathutils.Quaternion)
        :type other: Quaternion
        :return: The dot product.
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def freeze(self):
        """Make this object immutable.
        After this the object can be hashed, used in dictionaries & sets.
        
        :return: An instance of this object.
        """

    def identity(self):
        """Set the quaternion to an identity quaternion.
        
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def invert(self):
        """Set the quaternion to its inverse."""

    def inverted(self):
        """Return a new, inverted quaternion.
        
        :return: the inverted value.
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def negate(self):
        """Set the quaternion to its negative.
        
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def normalize(self):
        """Normalize the quaternion."""

    def normalized(self):
        """Return a new normalized quaternion.
        
        :return: a normalized copy.
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def rotate(self, other):
        """Rotates the quaternion by another mathutils value.
        
        :param other: rotation component of mathutils value
            (type: mathutils.Euler, mathutils.Quaternion or mathutils.Matrix)
        :type other: Euler, Quaternion or Matrix
        """

    def rotation_difference(self, other):
        """Returns a quaternion representing the rotational difference.
        
        :param other: second quaternion.
            (type: mathutils.Quaternion)
        :type other: Quaternion
        :return: the rotational difference between the two quat rotations.
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def slerp(self, other, factor):
        """Returns the interpolation of two quaternions.
        
        :param other: value to interpolate with.
            (type: mathutils.Quaternion)
        :type other: Quaternion
        :param factor: The interpolation value in [0.0, 1.0].
        :type factor: float
        :return: The interpolated rotation.
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def to_axis_angle(self):
        """Return the axis, angle representation of the quaternion.
        
        :return: axis, angle.
        :param : (type: (mathutils.Vector, float) pair)
        :rtype: (Vector, float) pair
        """

    def to_euler(self, order, euler_compat):
        """Return Euler representation of the quaternion.
        
        :param order: Optional rotation order argument in
                                                            ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
        :type order: str
        :param euler_compat: Optional euler argument the new euler will be made
                                                            compatible with (no axis flipping between them).
                                                            Useful for converting a series of matrices to animation curves.
            (type: mathutils.Euler)
        :type euler_compat: Euler
        :return: Euler representation of the quaternion.
        :param : (type: mathutils.Euler)
        :rtype: Euler
        """

    def to_exponential_map(self):
        """Return the exponential map representation of the quaternion.
        This representation consist of the rotation axis multiplied by the rotation angle.   Such a representation is useful for interpolation between multiple orientations.
        To convert back to a quaternion, pass it to the mathutils.Quaternion constructor.
        
        :return: exponential map.
        :param : (type: mathutils.Vector of size 3)
        :rtype: Vector
        """

    def to_matrix(self):
        """Return a matrix representation of the quaternion.
        
        :return: A 3x3 rotation matrix representation of the quaternion.
        :param : (type: mathutils.Matrix)
        :rtype: Matrix
        """

    angle = None
    """Angle of the quaternion.
    
    :type: float
    """

    axis = None
    """Quaternion axis as a vector.
    (type: mathutils.Vector)
    
    :type: Vector
    """

    is_frozen = None
    """True when this object has been frozen (read-only).
    
    :type: bool
    """

    is_wrapped = None
    """True when this object wraps external data (read-only).
    
    :type: bool
    """

    magnitude = None
    """Size of the quaternion (read-only).
    
    :type: float
    """

    owner = None
    """The item this is wrapping or None  (read-only)."""

    w = None
    """Quaternion axis value.
    
    :type: float
    """

    x = None
    """Quaternion axis value.
    
    :type: float
    """

    y = None
    """Quaternion axis value.
    
    :type: float
    """

    z = None
    """Quaternion axis value.
    
    :type: float
    """


class Vector:
    def __new__(cls, seq):
        """This object gives access to Vectors in Blender.
        
        :param seq: Components of the vector, must be a sequence of at least two
            (type: sequence of numbers)
        :type seq: collections.Sequence
        """
        return super().__new__(cls)

    def Fill(self, size, fill=0.0):
        """Create a vector of length size with all values set to fill.
        
        :param size: The length of the vector to be created.
        :type size: int
        :param fill: The value used to fill the vector.
        :type fill: float
        """

    def Linspace(self, start, stop, size):
        """Create a vector of the specified size which is filled with linearly spaced values between start and stop values.
        
        :param start: The start of the range used to fill the vector.
        :type start: int
        :param stop: The end of the range used to fill the vector.
        :type stop: int
        :param size: The size of the vector to be created.
        :type size: int
        """

    def Range(self, start=0, stop=0, step=1):
        """Create a filled with a range of values.
        
        :param start: The start of the range used to fill the vector.
        :type start: int
        :param stop: The end of the range used to fill the vector.
        :type stop: int
        :param step: The step between successive values in the vector.
        :type step: int
        """

    def Repeat(self, vector, size):
        """Create a vector by repeating the values in vector until the required size is reached.
        
        :param tuple: The vector to draw values from.
            (type: mathutils.Vector)
        :type tuple: Vector
        :param size: The size of the vector to be created.
        :type size: int
        """

    def angle(self, other, fallback=None):
        """Return the angle between two vectors.
        
        :param other: another vector to compare the angle with
            (type: mathutils.Vector)
        :type other: Vector
        :param fallback: return this when the angle can't be calculated (zero length vector),
                                                            (instead of raising a ValueError).
        :type fallback: bpy.types.KeyMapItem.any
        :return: angle in radians or fallback when given
        :rtype: float
        """

    def angle_signed(self, other, fallback):
        """Return the signed angle between two 2D vectors (clockwise is positive).
        
        :param other: another vector to compare the angle with
            (type: mathutils.Vector)
        :type other: Vector
        :param fallback: return this when the angle can't be calculated (zero length vector),
                                                            (instead of raising a ValueError).
        :type fallback: bpy.types.KeyMapItem.any
        :return: angle in radians or fallback when given
        :rtype: float
        """

    def copy(self):
        """Returns a copy of this vector.
        <Note> use this to get a copy of a wrapped vector with
                                            no reference to the original data.
        
        :return: A copy of the vector.
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def cross(self, other):
        """Return the cross product of this vector and another.
        <Note> both vectors must be 2D or 3D
        
        :param other: The other vector to perform the cross product with.
            (type: mathutils.Vector)
        :type other: Vector
        :return: The cross product.
        :param : (type: mathutils.Vector or float when 2D vectors are used)
        :rtype: Vector or float when 2D vectors are used
        """

    def dot(self, other):
        """Return the dot product of this vector and another.
        
        :param other: The other vector to perform the dot product with.
            (type: mathutils.Vector)
        :type other: Vector
        :return: The dot product.
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def freeze(self):
        """Make this object immutable.
        After this the object can be hashed, used in dictionaries & sets.
        
        :return: An instance of this object.
        """

    def lerp(self, other, factor):
        """Returns the interpolation of two vectors.
        
        :param other: value to interpolate with.
            (type: mathutils.Vector)
        :type other: Vector
        :param factor: The interpolation value in [0.0, 1.0].
        :type factor: float
        :return: The interpolated vector.
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def negate(self):
        """Set all values to their negative."""

    def normalize(self):
        """Normalize the vector, making the length of the vector always 1.0.
        <Note> Normalize works for vectors of all sizes,
                                            however 4D Vectors w axis is left untouched.
        """

    def normalized(self):
        """Return a new, normalized vector.
        
        :return: a normalized copy of the vector
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def orthogonal(self):
        """Return a perpendicular vector.
        <Note> the axis is undefined, only use when any orthogonal vector is acceptable.
        
        :return: a new vector 90 degrees from this vector.
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def project(self, other):
        """Return the projection of this vector onto the other.
        
        :param other: second vector.
            (type: mathutils.Vector)
        :type other: Vector
        :return: the parallel projection vector
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def reflect(self, mirror):
        """Return the reflection vector from the mirror argument.
        
        :param mirror: This vector could be a normal from the reflecting surface.
            (type: mathutils.Vector)
        :type mirror: Vector
        :return: The reflected vector matching the size of this vector.
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def resize(self, size=3):
        """Resize the vector to have size number of elements."""

    def resize_2d(self):
        """Resize the vector to 2D  (x, y)."""

    def resize_3d(self):
        """Resize the vector to 3D  (x, y, z)."""

    def resize_4d(self):
        """Resize the vector to 4D (x, y, z, w)."""

    def resized(self, size=3):
        """Return a resized copy of the vector with size number of elements.
        
        :return: a new vector
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def rotate(self, other):
        """Rotate the vector by a rotation value.
        
        :param other: rotation component of mathutils value
            (type: mathutils.Euler, mathutils.Quaternion or mathutils.Matrix)
        :type other: Euler, Quaternion or Matrix
        """

    def rotation_difference(self, other):
        """Returns a quaternion representing the rotational difference between this
                                    vector and another.
        <Note> 2D vectors raise an AttributeError.
        
        :param other: second vector.
            (type: mathutils.Vector)
        :type other: Vector
        :return: the rotational difference between the two vectors.
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def slerp(self, other, factor, fallback=None):
        """Returns the interpolation of two non-zero vectors (spherical coordinates).
        
        :param other: value to interpolate with.
            (type: mathutils.Vector)
        :type other: Vector
        :param factor: The interpolation value typically in [0.0, 1.0].
        :type factor: float
        :param fallback: return this when the vector can't be calculated (zero length vector or direct opposites),
                                                            (instead of raising a ValueError).
        :type fallback: bpy.types.KeyMapItem.any
        :return: The interpolated vector.
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def to_2d(self):
        """Return a 2d copy of the vector.
        
        :return: a new vector
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def to_3d(self):
        """Return a 3d copy of the vector.
        
        :return: a new vector
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def to_4d(self):
        """Return a 4d copy of the vector.
        
        :return: a new vector
        :param : (type: mathutils.Vector)
        :rtype: Vector
        """

    def to_track_quat(self, track, up):
        """Return a quaternion rotation from the vector and the track and up axis.
        
        :param track: Track axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z'].
        :type track: str
        :param up: Up axis in ['X', 'Y', 'Z'].
        :type up: str
        :return: rotation from the vector and the track and up axis.
        :param : (type: mathutils.Quaternion)
        :rtype: Quaternion
        """

    def to_tuple(self, precision=-1):
        """Return this vector as a tuple with.
        
        :param precision: The number to round the value to in [-1, 21].
        :type precision: int
        :return: the values of the vector rounded by precision
        :rtype: tuple
        """

    def zero(self):
        """Set all values to zero."""

    is_frozen = None
    """True when this object has been frozen (read-only).
    
    :type: bool
    """

    is_wrapped = None
    """True when this object wraps external data (read-only).
    
    :type: bool
    """

    length = None
    """Vector Length.
    
    :type: float
    """

    length_squared = None
    """Vector length squared (v.dot(v)).
    
    :type: float
    """

    magnitude = None
    """Vector Length.
    
    :type: float
    """

    owner = None
    """The item this is wrapping or None  (read-only)."""

    w = None
    """Vector W axis (4D Vectors only).
    
    :type: float
    """

    ww = None
    """Undocumented"""

    www = None
    """Undocumented"""

    wwww = None
    """Undocumented"""

    wwwx = None
    """Undocumented"""

    wwwy = None
    """Undocumented"""

    wwwz = None
    """Undocumented"""

    wwx = None
    """Undocumented"""

    wwxw = None
    """Undocumented"""

    wwxx = None
    """Undocumented"""

    wwxy = None
    """Undocumented"""

    wwxz = None
    """Undocumented"""

    wwy = None
    """Undocumented"""

    wwyw = None
    """Undocumented"""

    wwyx = None
    """Undocumented"""

    wwyy = None
    """Undocumented"""

    wwyz = None
    """Undocumented"""

    wwz = None
    """Undocumented"""

    wwzw = None
    """Undocumented"""

    wwzx = None
    """Undocumented"""

    wwzy = None
    """Undocumented"""

    wwzz = None
    """Undocumented"""

    wx = None
    """Undocumented"""

    wxw = None
    """Undocumented"""

    wxww = None
    """Undocumented"""

    wxwx = None
    """Undocumented"""

    wxwy = None
    """Undocumented"""

    wxwz = None
    """Undocumented"""

    wxx = None
    """Undocumented"""

    wxxw = None
    """Undocumented"""

    wxxx = None
    """Undocumented"""

    wxxy = None
    """Undocumented"""

    wxxz = None
    """Undocumented"""

    wxy = None
    """Undocumented"""

    wxyw = None
    """Undocumented"""

    wxyx = None
    """Undocumented"""

    wxyy = None
    """Undocumented"""

    wxyz = None
    """Undocumented"""

    wxz = None
    """Undocumented"""

    wxzw = None
    """Undocumented"""

    wxzx = None
    """Undocumented"""

    wxzy = None
    """Undocumented"""

    wxzz = None
    """Undocumented"""

    wy = None
    """Undocumented"""

    wyw = None
    """Undocumented"""

    wyww = None
    """Undocumented"""

    wywx = None
    """Undocumented"""

    wywy = None
    """Undocumented"""

    wywz = None
    """Undocumented"""

    wyx = None
    """Undocumented"""

    wyxw = None
    """Undocumented"""

    wyxx = None
    """Undocumented"""

    wyxy = None
    """Undocumented"""

    wyxz = None
    """Undocumented"""

    wyy = None
    """Undocumented"""

    wyyw = None
    """Undocumented"""

    wyyx = None
    """Undocumented"""

    wyyy = None
    """Undocumented"""

    wyyz = None
    """Undocumented"""

    wyz = None
    """Undocumented"""

    wyzw = None
    """Undocumented"""

    wyzx = None
    """Undocumented"""

    wyzy = None
    """Undocumented"""

    wyzz = None
    """Undocumented"""

    wz = None
    """Undocumented"""

    wzw = None
    """Undocumented"""

    wzww = None
    """Undocumented"""

    wzwx = None
    """Undocumented"""

    wzwy = None
    """Undocumented"""

    wzwz = None
    """Undocumented"""

    wzx = None
    """Undocumented"""

    wzxw = None
    """Undocumented"""

    wzxx = None
    """Undocumented"""

    wzxy = None
    """Undocumented"""

    wzxz = None
    """Undocumented"""

    wzy = None
    """Undocumented"""

    wzyw = None
    """Undocumented"""

    wzyx = None
    """Undocumented"""

    wzyy = None
    """Undocumented"""

    wzyz = None
    """Undocumented"""

    wzz = None
    """Undocumented"""

    wzzw = None
    """Undocumented"""

    wzzx = None
    """Undocumented"""

    wzzy = None
    """Undocumented"""

    wzzz = None
    """Undocumented"""

    x = None
    """Vector X axis.
    
    :type: float
    """

    xw = None
    """Undocumented"""

    xww = None
    """Undocumented"""

    xwww = None
    """Undocumented"""

    xwwx = None
    """Undocumented"""

    xwwy = None
    """Undocumented"""

    xwwz = None
    """Undocumented"""

    xwx = None
    """Undocumented"""

    xwxw = None
    """Undocumented"""

    xwxx = None
    """Undocumented"""

    xwxy = None
    """Undocumented"""

    xwxz = None
    """Undocumented"""

    xwy = None
    """Undocumented"""

    xwyw = None
    """Undocumented"""

    xwyx = None
    """Undocumented"""

    xwyy = None
    """Undocumented"""

    xwyz = None
    """Undocumented"""

    xwz = None
    """Undocumented"""

    xwzw = None
    """Undocumented"""

    xwzx = None
    """Undocumented"""

    xwzy = None
    """Undocumented"""

    xwzz = None
    """Undocumented"""

    xx = None
    """Undocumented"""

    xxw = None
    """Undocumented"""

    xxww = None
    """Undocumented"""

    xxwx = None
    """Undocumented"""

    xxwy = None
    """Undocumented"""

    xxwz = None
    """Undocumented"""

    xxx = None
    """Undocumented"""

    xxxw = None
    """Undocumented"""

    xxxx = None
    """Undocumented"""

    xxxy = None
    """Undocumented"""

    xxxz = None
    """Undocumented"""

    xxy = None
    """Undocumented"""

    xxyw = None
    """Undocumented"""

    xxyx = None
    """Undocumented"""

    xxyy = None
    """Undocumented"""

    xxyz = None
    """Undocumented"""

    xxz = None
    """Undocumented"""

    xxzw = None
    """Undocumented"""

    xxzx = None
    """Undocumented"""

    xxzy = None
    """Undocumented"""

    xxzz = None
    """Undocumented"""

    xy = None
    """Undocumented"""

    xyw = None
    """Undocumented"""

    xyww = None
    """Undocumented"""

    xywx = None
    """Undocumented"""

    xywy = None
    """Undocumented"""

    xywz = None
    """Undocumented"""

    xyx = None
    """Undocumented"""

    xyxw = None
    """Undocumented"""

    xyxx = None
    """Undocumented"""

    xyxy = None
    """Undocumented"""

    xyxz = None
    """Undocumented"""

    xyy = None
    """Undocumented"""

    xyyw = None
    """Undocumented"""

    xyyx = None
    """Undocumented"""

    xyyy = None
    """Undocumented"""

    xyyz = None
    """Undocumented"""

    xyz = None
    """Undocumented"""

    xyzw = None
    """Undocumented"""

    xyzx = None
    """Undocumented"""

    xyzy = None
    """Undocumented"""

    xyzz = None
    """Undocumented"""

    xz = None
    """Undocumented"""

    xzw = None
    """Undocumented"""

    xzww = None
    """Undocumented"""

    xzwx = None
    """Undocumented"""

    xzwy = None
    """Undocumented"""

    xzwz = None
    """Undocumented"""

    xzx = None
    """Undocumented"""

    xzxw = None
    """Undocumented"""

    xzxx = None
    """Undocumented"""

    xzxy = None
    """Undocumented"""

    xzxz = None
    """Undocumented"""

    xzy = None
    """Undocumented"""

    xzyw = None
    """Undocumented"""

    xzyx = None
    """Undocumented"""

    xzyy = None
    """Undocumented"""

    xzyz = None
    """Undocumented"""

    xzz = None
    """Undocumented"""

    xzzw = None
    """Undocumented"""

    xzzx = None
    """Undocumented"""

    xzzy = None
    """Undocumented"""

    xzzz = None
    """Undocumented"""

    y = None
    """Vector Y axis.
    
    :type: float
    """

    yw = None
    """Undocumented"""

    yww = None
    """Undocumented"""

    ywww = None
    """Undocumented"""

    ywwx = None
    """Undocumented"""

    ywwy = None
    """Undocumented"""

    ywwz = None
    """Undocumented"""

    ywx = None
    """Undocumented"""

    ywxw = None
    """Undocumented"""

    ywxx = None
    """Undocumented"""

    ywxy = None
    """Undocumented"""

    ywxz = None
    """Undocumented"""

    ywy = None
    """Undocumented"""

    ywyw = None
    """Undocumented"""

    ywyx = None
    """Undocumented"""

    ywyy = None
    """Undocumented"""

    ywyz = None
    """Undocumented"""

    ywz = None
    """Undocumented"""

    ywzw = None
    """Undocumented"""

    ywzx = None
    """Undocumented"""

    ywzy = None
    """Undocumented"""

    ywzz = None
    """Undocumented"""

    yx = None
    """Undocumented"""

    yxw = None
    """Undocumented"""

    yxww = None
    """Undocumented"""

    yxwx = None
    """Undocumented"""

    yxwy = None
    """Undocumented"""

    yxwz = None
    """Undocumented"""

    yxx = None
    """Undocumented"""

    yxxw = None
    """Undocumented"""

    yxxx = None
    """Undocumented"""

    yxxy = None
    """Undocumented"""

    yxxz = None
    """Undocumented"""

    yxy = None
    """Undocumented"""

    yxyw = None
    """Undocumented"""

    yxyx = None
    """Undocumented"""

    yxyy = None
    """Undocumented"""

    yxyz = None
    """Undocumented"""

    yxz = None
    """Undocumented"""

    yxzw = None
    """Undocumented"""

    yxzx = None
    """Undocumented"""

    yxzy = None
    """Undocumented"""

    yxzz = None
    """Undocumented"""

    yy = None
    """Undocumented"""

    yyw = None
    """Undocumented"""

    yyww = None
    """Undocumented"""

    yywx = None
    """Undocumented"""

    yywy = None
    """Undocumented"""

    yywz = None
    """Undocumented"""

    yyx = None
    """Undocumented"""

    yyxw = None
    """Undocumented"""

    yyxx = None
    """Undocumented"""

    yyxy = None
    """Undocumented"""

    yyxz = None
    """Undocumented"""

    yyy = None
    """Undocumented"""

    yyyw = None
    """Undocumented"""

    yyyx = None
    """Undocumented"""

    yyyy = None
    """Undocumented"""

    yyyz = None
    """Undocumented"""

    yyz = None
    """Undocumented"""

    yyzw = None
    """Undocumented"""

    yyzx = None
    """Undocumented"""

    yyzy = None
    """Undocumented"""

    yyzz = None
    """Undocumented"""

    yz = None
    """Undocumented"""

    yzw = None
    """Undocumented"""

    yzww = None
    """Undocumented"""

    yzwx = None
    """Undocumented"""

    yzwy = None
    """Undocumented"""

    yzwz = None
    """Undocumented"""

    yzx = None
    """Undocumented"""

    yzxw = None
    """Undocumented"""

    yzxx = None
    """Undocumented"""

    yzxy = None
    """Undocumented"""

    yzxz = None
    """Undocumented"""

    yzy = None
    """Undocumented"""

    yzyw = None
    """Undocumented"""

    yzyx = None
    """Undocumented"""

    yzyy = None
    """Undocumented"""

    yzyz = None
    """Undocumented"""

    yzz = None
    """Undocumented"""

    yzzw = None
    """Undocumented"""

    yzzx = None
    """Undocumented"""

    yzzy = None
    """Undocumented"""

    yzzz = None
    """Undocumented"""

    z = None
    """Vector Z axis (3D Vectors only).
    
    :type: float
    """

    zw = None
    """Undocumented"""

    zww = None
    """Undocumented"""

    zwww = None
    """Undocumented"""

    zwwx = None
    """Undocumented"""

    zwwy = None
    """Undocumented"""

    zwwz = None
    """Undocumented"""

    zwx = None
    """Undocumented"""

    zwxw = None
    """Undocumented"""

    zwxx = None
    """Undocumented"""

    zwxy = None
    """Undocumented"""

    zwxz = None
    """Undocumented"""

    zwy = None
    """Undocumented"""

    zwyw = None
    """Undocumented"""

    zwyx = None
    """Undocumented"""

    zwyy = None
    """Undocumented"""

    zwyz = None
    """Undocumented"""

    zwz = None
    """Undocumented"""

    zwzw = None
    """Undocumented"""

    zwzx = None
    """Undocumented"""

    zwzy = None
    """Undocumented"""

    zwzz = None
    """Undocumented"""

    zx = None
    """Undocumented"""

    zxw = None
    """Undocumented"""

    zxww = None
    """Undocumented"""

    zxwx = None
    """Undocumented"""

    zxwy = None
    """Undocumented"""

    zxwz = None
    """Undocumented"""

    zxx = None
    """Undocumented"""

    zxxw = None
    """Undocumented"""

    zxxx = None
    """Undocumented"""

    zxxy = None
    """Undocumented"""

    zxxz = None
    """Undocumented"""

    zxy = None
    """Undocumented"""

    zxyw = None
    """Undocumented"""

    zxyx = None
    """Undocumented"""

    zxyy = None
    """Undocumented"""

    zxyz = None
    """Undocumented"""

    zxz = None
    """Undocumented"""

    zxzw = None
    """Undocumented"""

    zxzx = None
    """Undocumented"""

    zxzy = None
    """Undocumented"""

    zxzz = None
    """Undocumented"""

    zy = None
    """Undocumented"""

    zyw = None
    """Undocumented"""

    zyww = None
    """Undocumented"""

    zywx = None
    """Undocumented"""

    zywy = None
    """Undocumented"""

    zywz = None
    """Undocumented"""

    zyx = None
    """Undocumented"""

    zyxw = None
    """Undocumented"""

    zyxx = None
    """Undocumented"""

    zyxy = None
    """Undocumented"""

    zyxz = None
    """Undocumented"""

    zyy = None
    """Undocumented"""

    zyyw = None
    """Undocumented"""

    zyyx = None
    """Undocumented"""

    zyyy = None
    """Undocumented"""

    zyyz = None
    """Undocumented"""

    zyz = None
    """Undocumented"""

    zyzw = None
    """Undocumented"""

    zyzx = None
    """Undocumented"""

    zyzy = None
    """Undocumented"""

    zyzz = None
    """Undocumented"""

    zz = None
    """Undocumented"""

    zzw = None
    """Undocumented"""

    zzww = None
    """Undocumented"""

    zzwx = None
    """Undocumented"""

    zzwy = None
    """Undocumented"""

    zzwz = None
    """Undocumented"""

    zzx = None
    """Undocumented"""

    zzxw = None
    """Undocumented"""

    zzxx = None
    """Undocumented"""

    zzxy = None
    """Undocumented"""

    zzxz = None
    """Undocumented"""

    zzy = None
    """Undocumented"""

    zzyw = None
    """Undocumented"""

    zzyx = None
    """Undocumented"""

    zzyy = None
    """Undocumented"""

    zzyz = None
    """Undocumented"""

    zzz = None
    """Undocumented"""

    zzzw = None
    """Undocumented"""

    zzzx = None
    """Undocumented"""

    zzzy = None
    """Undocumented"""

    zzzz = None
    """Undocumented"""
