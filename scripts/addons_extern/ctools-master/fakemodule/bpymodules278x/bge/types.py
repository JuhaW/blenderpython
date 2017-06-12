from . import logic


class PyObjectPlus:
    """PyObjectPlus base class of most other types in the Game Engine."""

    invalid = None
    """Test if the object has been freed by the game engine and is no longer valid.
    Normally this is not a problem but when storing game engine data in the GameLogic module,
                                KX_Scenes or other KX_GameObjects its possible to hold a reference to invalid data.
                                Calling an attribute or method on an invalid object will raise a SystemError.
    The invalid attribute allows testing for this case without exception handling.
    
    :type: bool
    """


class BL_ArmatureBone(PyObjectPlus):
    """Proxy to Blender bone structure. All fields are read-only and comply to RNA names.
                        All space attribute correspond to the rest pose.
    """

    name = ""
    """bone name.
    
    :type: str
    """

    connected = None
    """true when the bone head is struck to the parent's tail.
    
    :type: bool
    """

    hinge = None
    """true when bone doesn't inherit rotation or scale from parent bone.
    
    :type: bool
    """

    inherit_scale = None
    """true when bone inherits scaling from parent bone.
    
    :type: bool
    """

    bbone_segments = None
    """number of B-bone segments.
    
    :type: int
    """

    roll = None
    """bone rotation around head-tail axis.
    
    :type: float
    """

    head = None
    """location of head end of the bone in parent bone space.
    
    :type: vector [x, y, z]
    """

    tail = None
    """location of head end of the bone in parent bone space.
    
    :type: vector [x, y, z]
    """

    length = None
    """bone length.
    
    :type: float
    """

    arm_head = None
    """location of head end of the bone in armature space.
    
    :type: vector [x, y, z]
    """

    arm_tail = None
    """location of tail end of the bone in armature space.
    
    :type: vector [x, y, z]
    """

    arm_mat = None
    """matrix of the bone head in armature space.
    
    :type: matrix [4][4]
    """

    bone_mat = None
    """rotation matrix of the bone in parent bone space.
    
    :type: matrix [3][3]
    """

    parent = None
    """parent bone, or None for root bone.
    (type: bge.types.BL_ArmatureBone)
    
    :type: BL_ArmatureBone
    """

    children = None
    """list of bone's children.
    (type: list of bge.types.BL_ArmatureBone)
    
    :type: list
    """


class BL_ArmatureChannel(PyObjectPlus):
    """Proxy to armature pose channel. Allows to read and set armature pose.
                        The attributes are identical to RNA attributes, but mostly in read-only mode.
    """

    name = ""
    """channel name (=bone name), read-only.
    
    :type: str
    """

    bone = None
    """return the bone object corresponding to this pose channel, read-only.
    (type: bge.types.BL_ArmatureBone)
    
    :type: BL_ArmatureBone
    """

    parent = None
    """return the parent channel object, None if root channel, read-only.
    (type: bge.types.BL_ArmatureChannel)
    
    :type: BL_ArmatureChannel
    """

    has_ik = None
    """true if the bone is part of an active IK chain, read-only.
                                This flag is not set when an IK constraint is defined but not enabled (miss target information for example).
    
    :type: bool
    """

    ik_dof_x = None
    """true if the bone is free to rotation in the X axis, read-only.
    
    :type: bool
    """

    ik_dof_y = None
    """true if the bone is free to rotation in the Y axis, read-only.
    
    :type: bool
    """

    ik_dof_z = None
    """true if the bone is free to rotation in the Z axis, read-only.
    
    :type: bool
    """

    ik_limit_x = None
    """true if a limit is imposed on X rotation, read-only.
    
    :type: bool
    """

    ik_limit_y = None
    """true if a limit is imposed on Y rotation, read-only.
    
    :type: bool
    """

    ik_limit_z = None
    """true if a limit is imposed on Z rotation, read-only.
    
    :type: bool
    """

    ik_rot_control = None
    """true if channel rotation should applied as IK constraint, read-only.
    
    :type: bool
    """

    ik_lin_control = None
    """true if channel size should applied as IK constraint, read-only.
    
    :type: bool
    """

    location = None
    """displacement of the bone head in armature local space, read-write.
    
    :type: vector [X, Y, Z].
    """

    scale = None
    """scale of the bone relative to its parent, read-write.
    
    :type: vector [sizeX, sizeY, sizeZ].
    """

    rotation_quaternion = None
    """rotation of the bone relative to its parent expressed as a quaternion, read-write.
    
    :type: vector [qr, qi, qj, qk].
    """

    rotation_euler = None
    """rotation of the bone relative to its parent expressed as a set of euler angles, read-write.
    
    :type: vector [X, Y, Z].
    """

    rotation_mode = None
    """Method of updating the bone rotation, read-write.
    
    :type: integer (one of bge.logic#armaturechannel-constants-rotation-modethese constants)
    """

    channel_matrix = None
    """pose matrix in bone space (deformation of the bone due to action, constraint, etc), Read-only.
                                This field is updated after the graphic render, it represents the current pose.
    
    :type: matrix [4][4]
    """

    pose_matrix = None
    """pose matrix in armature space, read-only,
                                This field is updated after the graphic render, it represents the current pose.
    
    :type: matrix [4][4]
    """

    pose_head = None
    """position of bone head in armature space, read-only.
    
    :type: vector [x, y, z]
    """

    pose_tail = None
    """position of bone tail in armature space, read-only.
    
    :type: vector [x, y, z]
    """

    ik_min_x = None
    """minimum value of X rotation in degree (<= 0) when X rotation is limited (see ik_limit_x), read-only.
    
    :type: float
    """

    ik_max_x = None
    """maximum value of X rotation in degree (>= 0) when X rotation is limited (see ik_limit_x), read-only.
    
    :type: float
    """

    ik_min_y = None
    """minimum value of Y rotation in degree (<= 0) when Y rotation is limited (see ik_limit_y), read-only.
    
    :type: float
    """

    ik_max_y = None
    """maximum value of Y rotation in degree (>= 0) when Y rotation is limited (see ik_limit_y), read-only.
    
    :type: float
    """

    ik_min_z = None
    """minimum value of Z rotation in degree (<= 0) when Z rotation is limited (see ik_limit_z), read-only.
    
    :type: float
    """

    ik_max_z = None
    """maximum value of Z rotation in degree (>= 0) when Z rotation is limited (see ik_limit_z), read-only.
    
    :type: float
    """

    ik_stiffness_x = None
    """bone rotation stiffness in X axis, read-only.
    
    :type: float between 0 and 1
    """

    ik_stiffness_y = None
    """bone rotation stiffness in Y axis, read-only.
    
    :type: float between 0 and 1
    """

    ik_stiffness_z = None
    """bone rotation stiffness in Z axis, read-only.
    
    :type: float between 0 and 1
    """

    ik_stretch = None
    """ratio of scale change that is allowed, 0=bone can't change size, read-only.
    
    :type: float
    """

    ik_rot_weight = None
    """weight of rotation constraint when ik_rot_control is set, read-write.
    
    :type: float between 0 and 1
    """

    ik_lin_weight = None
    """weight of size constraint when ik_lin_control is set, read-write.
    
    :type: float between 0 and 1
    """

    joint_rotation = None
    """Control bone rotation in term of joint angle (for robotic applications), read-write.
    When writing to this attribute, you pass a [x, y, z] vector and an appropriate set of euler angles or quaternion is calculated according to the rotation_mode.
    When you read this attribute, the current pose matrix is converted into a [x, y, z] vector representing the joint angles.
    The value and the meaning of the x, y, z depends on the ik_dof_x/ik_dof_y/ik_dof_z attributes:
    * 1DoF joint X, Y or Z: the corresponding x, y, or z value is used an a joint angle in radiant
    * 2DoF joint X+Y or Z+Y: treated as 2 successive 1DoF joints: first X or Z, then Y. The x or z value is used as a joint angle in radiant along the X or Z axis, followed by a rotation along the new Y axis of y radiants.
    * 2DoF joint X+Z: treated as a 2DoF joint with rotation axis on the X/Z plane. The x and z values are used as the coordinates of the rotation vector in the X/Z plane.
    * 3DoF joint X+Y+Z: treated as a revolute joint. The [x, y, z] vector represents the equivalent rotation vector to bring the joint from the rest pose to the new pose.
    
    :type: vector [x, y, z]
    """


class BL_ArmatureConstraint(PyObjectPlus):
    """Proxy to Armature Constraint. Allows to change constraint on the fly.
                        Obtained through bge.types.BL_ArmatureObject.constraints.
    <Note> Not all armature constraints are supported in the GE.
    """

    type = None
    """Type of constraint, (read-only).
    Use one of bge.logic#armatureconstraint-constants-typethese constants.
    
    :type: integer, one of CONSTRAINT_TYPE_* constants
    """

    name = ""
    """Name of constraint constructed as <bone_name>:<constraint_name>. constraints list.
    This name is also the key subscript on bge.types.BL_ArmatureObject.
    
    :type: str
    """

    enforce = None
    """fraction of constraint effect that is enforced. Between 0 and 1.
    
    :type: float
    """

    headtail = None
    """Position of target between head and tail of the target bone: 0=head, 1=tail.
    
    :type: float.
    """

    lin_error = None
    """runtime linear error (in Blender units) on constraint at the current frame.
    This is a runtime value updated on each frame by the IK solver. Only available on IK constraint and iTaSC solver.
    
    :type: float
    """

    rot_error = None
    """Runtime rotation error (in radiant) on constraint at the current frame.
    This is a runtime value updated on each frame by the IK solver. Only available on IK constraint and iTaSC solver.
    It is only set if the constraint has a rotation part, for example, a CopyPose+Rotation IK constraint.
    
    :type: float.
    """

    target = None
    """Primary target object for the constraint. The position of this object in the GE will be used as target for the constraint.
    (type: bge.types.KX_GameObject.)
    
    :type: KX_GameObject.
    """

    subtarget = None
    """Secondary target object for the constraint. The position of this object in the GE will be used as secondary target for the constraint.
    Currently this is only used for pole target on IK constraint.
    (type: bge.types.KX_GameObject.)
    
    :type: KX_GameObject.
    """

    active = None
    """True if the constraint is active.
    
    :type: bool
    """

    ik_weight = None
    """Weight of the IK constraint between 0 and 1.
    Only defined for IK constraint.
    
    :type: float
    """

    ik_type = None
    """Type of IK constraint, (read-only).
    Use one of bge.logic#armatureconstraint-constants-ik-typethese constants.
    
    :type: integer.
    """

    ik_flag = None
    """Combination of IK constraint option flags, read-only.
    Use one of bge.logic#armatureconstraint-constants-ik-flagthese constants.
    
    :type: int
    """

    ik_dist = None
    """Distance the constraint is trying to maintain with target, only used when ik_type=CONSTRAINT_IK_DISTANCE.
    
    :type: float
    """

    ik_mode = None
    """Use one of bge.logic#armatureconstraint-constants-ik-modethese constants.
    Additional mode for IK constraint. Currently only used for Distance constraint:
    
    :type: int
    """


class BL_Shader(PyObjectPlus):
    """BL_Shader GLSL shaders.
    TODO - Description
    """

    def setUniformfv(self, name, fList):
        """Set a uniform with a list of float values
        
        :param name: the uniform name
        :type name: str
        :param fList: a list (2, 3 or 4 elements) of float values
        :type fList: bpy.types.ThemeSpaceListGeneric.list[float]
        """

    def delSource(self):
        """Clear the shader. Use this method before the source is changed with bge.types.BL_Shader.setSource."""

    def getFragmentProg(self):
        """Returns the fragment program.
        
        :return: The fragment program.
        :rtype: str
        """

    def getVertexProg(self):
        """Get the vertex program.
        
        :return: The vertex program.
        :rtype: str
        """

    def isValid(self):
        """Check if the shader is valid.
        
        :return: True if the shader is valid
        :rtype: bool
        """

    def setAttrib(self, enum):
        """Set attribute location. (The parameter is ignored a.t.m. and the value of "tangent" is always used.)
        
        :param enum: attribute location value
        :type enum: int
        """

    def setNumberOfPasses(self, max_pass):
        """Set the maximum number of passes. Not used a.t.m.
        
        :param max_pass: the maximum number of passes
        :type max_pass: int
        """

    def setSampler(self, name, index):
        """Set uniform texture sample index.
        
        :param name: Uniform name
        :type name: str
        :param index: Texture sample index.
        :type index: int
        """

    def setSource(self, vertexProgram, fragmentProgram):
        """Set the vertex and fragment programs
        
        :param vertexProgram: Vertex program
        :type vertexProgram: str
        :param fragmentProgram: Fragment program
        :type fragmentProgram: str
        """

    def setUniform1f(self, name, fx):
        """Set a uniform with 1 float value.
        
        :param name: the uniform name
        :type name: str
        :param fx: Uniform value
        :type fx: float
        """

    def setUniform1i(self, name, ix):
        """Set a uniform with an integer value.
        
        :param name: the uniform name
        :type name: str
        :param ix: the uniform value
        :type ix: int
        """

    def setUniform2f(self, name, fx, fy):
        """Set a uniform with 2 float values
        
        :param name: the uniform name
        :type name: str
        :param fx: first float value
        :type fx: float
        :param fy: second float value
        :type fy: float
        """

    def setUniform2i(self, name, ix, iy):
        """Set a uniform with 2 integer values
        
        :param name: the uniform name
        :type name: str
        :param ix: first integer value
        :type ix: int
        :param iy: second integer value
        :type iy: int
        """

    def setUniform3f(self, name, fx, fy, fz):
        """Set a uniform with 3 float values.
        
        :param name: the uniform name
        :type name: str
        :param fx: first float value
        :type fx: float
        :param fy: second float value
        :type fy: float
        :param fz: third float value
        :type fz: float
        """

    def setUniform3i(self, name, ix, iy, iz):
        """Set a uniform with 3 integer values
        
        :param name: the uniform name
        :type name: str
        :param ix: first integer value
        :type ix: int
        :param iy: second integer value
        :type iy: int
        :param iz: third integer value
        :type iz: int
        """

    def setUniform4f(self, name, fx, fy, fz, fw):
        """Set a uniform with 4 float values.
        
        :param name: the uniform name
        :type name: str
        :param fx: first float value
        :type fx: float
        :param fy: second float value
        :type fy: float
        :param fz: third float value
        :type fz: float
        :param fw: fourth float value
        :type fw: float
        """

    def setUniform4i(self, name, ix, iy, iz, iw):
        """Set a uniform with 4 integer values
        
        :param name: the uniform name
        :type name: str
        :param ix: first integer value
        :type ix: int
        :param iy: second integer value
        :type iy: int
        :param iz: third integer value
        :type iz: int
        :param iw: fourth integer value
        :type iw: int
        """

    def setUniformDef(self, name, type):
        """Define a new uniform
        
        :param name: the uniform name
        :type name: str
        :param type: uniform type
        :type type: UNI_NONE, UNI_INT, UNI_FLOAT, UNI_INT2, UNI_FLOAT2, UNI_INT3, UNI_FLOAT3, UNI_INT4, UNI_FLOAT4, UNI_MAT3, UNI_MAT4, UNI_MAX
        """

    def setUniformMatrix3(self, name, mat, transpose):
        """Set a uniform with a 3x3 matrix value
        
        :param name: the uniform name
        :type name: str
        :param mat: A 3x3 matrix [[f, f, f], [f, f, f], [f, f, f]]
        :type mat: 3x3 matrix
        :param transpose: set to True to transpose the matrix
        :type transpose: bool
        """

    def setUniformMatrix4(self, name, mat, transpose):
        """Set a uniform with a 4x4 matrix value
        
        :param name: the uniform name
        :type name: str
        :param mat: A 4x4 matrix [[f, f, f, f], [f, f, f, f], [f, f, f, f], [f, f, f, f]]
        :type mat: 4x4 matrix
        :param transpose: set to True to transpose the matrix
        :type transpose: bool
        """

    def setUniformiv(self, name, iList):
        """Set a uniform with a list of integer values
        
        :param name: the uniform name
        :type name: str
        :param iList: a list (2, 3 or 4 elements) of integer values
        :type iList: bpy.types.ThemeSpaceListGeneric.list[integer]
        """

    def setUniformEyef(self, name):
        """Set a uniform with a float value that reflects the eye being render in stereo mode:
                                    0.0 for the left eye, 0.5 for the right eye. In non stereo mode, the value of the uniform
                                    is fixed to 0.0. The typical use of this uniform is in stereo mode to sample stereo textures
                                    containing the left and right eye images in a top-bottom order.
        
        :param name: the uniform name
        :type name: str
        """

    def validate(self):
        """Validate the shader object."""


class CValue(PyObjectPlus):
    """This class is a basis for other classes."""

    name = ""
    """The name of this CValue derived object (read-only).
    
    :type: str
    """


class KX_BlenderMaterial(PyObjectPlus):
    """This is the interface to materials in the game engine.
    Materials define the render state to be applied to mesh objects.
    The example below shows a simple GLSL shader setup allowing to dynamically mix two texture channels
                        in a material. All materials of the object executing this script should have two textures using
                        separate UV maps in the two first texture channels.
    The code works for both Multitexture and GLSL rendering modes.
    """

    shader = None
    """The material's shader.
    (type: bge.types.BL_Shader)
    
    :type: BL_Shader
    """

    blending = None
    """Ints used for pixel blending, (src, dst), matching the setBlending method.
    
    :type: (integer, integer)
    """

    material_index = None
    """The material's index.
    
    :type: int
    """

    def getShader(self):
        """Returns the material's shader.
        
        :return: the material's shader
        :param : (type: bge.types.BL_Shader)
        :rtype: BL_Shader
        """

    def getTextureBindcode(self, textureslot):
        """Returns the material's texture OpenGL bind code/id/number/name.
        
        :param textureslot: Specifies the texture slot number
        :type textureslot: int
        :return: the material's texture OpenGL bind code/id/number/name
        :rtype: int
        """

    alpha = None
    """The material's alpha transparency.
    
    :type: float between 0.0 and 1.0 inclusive
    """

    hardness = None
    """How hard (sharp) the material's specular reflection is.
    
    :type: integer between 1 and 511 inclusive
    """

    emit = None
    """Amount of light to emit.
    
    :type: float between 0.0 and 2.0 inclusive
    """

    specularIntensity = None
    """How intense (bright) the material's specular reflection is.
    
    :type: float between 0.0 and 1.0 inclusive
    """

    diffuseIntensity = None
    """The material's amount of diffuse reflection.
    
    :type: float between 0.0 and 1.0 inclusive
    """

    specularColor = None
    """The material's specular color.
    
    :type: mathutils.Color
    """

    diffuseColor = None
    """The material's diffuse color.
    
    :type: mathutils.Color
    """

    def setBlending(self, src, dest):
        """Set the pixel color arithmetic functions.
        
        :param src: Specifies how the red, green, blue, and alpha source blending factors are computed, one of...
            * 'GL_ZERO':
            * 'GL_ONE':
            * 'GL_SRC_COLOR':
            * 'GL_ONE_MINUS_SRC_COLOR':
            * 'GL_DST_COLOR':
            * 'GL_ONE_MINUS_DST_COLOR':
            * 'GL_SRC_ALPHA':
            * 'GL_ONE_MINUS_SRC_ALPHA':
            * 'GL_DST_ALPHA':
            * 'GL_ONE_MINUS_DST_ALPHA':
            * 'GL_SRC_ALPHA_SATURATE':
        :type src: int
        :param dest: Specifies how the red, green, blue, and alpha destination blending factors are computed, one of...
            * 'GL_ZERO':
            * 'GL_ONE':
            * 'GL_SRC_COLOR':
            * 'GL_ONE_MINUS_SRC_COLOR':
            * 'GL_DST_COLOR':
            * 'GL_ONE_MINUS_DST_COLOR':
            * 'GL_SRC_ALPHA':
            * 'GL_ONE_MINUS_SRC_ALPHA':
            * 'GL_DST_ALPHA':
            * 'GL_ONE_MINUS_DST_ALPHA':
            * 'GL_SRC_ALPHA_SATURATE':
        :type dest: int
        """

    def getMaterialIndex(self):
        """Returns the material's index.
        
        :return: the material's index
        :rtype: int
        """


class KX_CharacterWrapper(PyObjectPlus):
    """A wrapper to expose character physics options."""

    onGround = None
    """Whether or not the character is on the ground. (read-only)
    
    :type: bool
    """

    gravity = None
    """The gravity value used for the character.
    
    :type: float
    """

    maxJumps = 1
    """The maximum number of jumps a character can perform before having to touch the ground. By default this is set to 1. 2 allows for a double jump, etc.
    (type: int in [0, 255], default 1)
    
    :type: int
    """

    jumpCount = None
    """The current jump count. This can be used to have different logic for a single jump versus a double jump. For example, a different animation for the second jump.
    
    :type: int
    """

    walkDirection = None
    """The speed and direction the character is traveling in using world coordinates. This should be used instead of applyMovement() to properly move the character.
    
    :type: Vector((x, y, z))
    """

    def jump(self):
        """The character jumps based on it's jump speed."""


class KX_ConstraintWrapper(PyObjectPlus):
    """KX_ConstraintWrapper"""

    def getConstraintId(self, val):
        """Returns the contraint ID
        
        :return: the constraint ID
        :rtype: int
        """

    def setParam(self, axis, value0, value1):
        """Set the contraint limits
        <Note> * Lowerlimit == Upperlimit -> axis is locked
            * Lowerlimit > Upperlimit -> axis is free
            * Lowerlimit < Upperlimit -> axis it limited in that range
        For PHY_LINEHINGE_CONSTRAINT = 2 or PHY_ANGULAR_CONSTRAINT = 3:
        For PHY_CONE_TWIST_CONSTRAINT = 4:
        For PHY_GENERIC_6DOF_CONSTRAINT = 12:
        
        :type axis: int
        :param (min) (value0): Set the minimum limit of the axis
        :param (max) (value1): Set the maximum limit of the axis
        :param (min) (value0): Set the minimum limit of the axis
        :param (max) (value1): Set the maximum limit of the axis
        :param (min) (value0): Set the minimum limit of the axis
        :param (max) (value1): Set the maximum limit of the axis
        :param (speed) (value0): Set the linear velocity of the axis
        :param (force) (value1): Set the maximum force limit of the axis
        :param (stiffness) (value0): Set the stiffness of the spring
        :param (damping) (value1): Tendency of the spring to return to it's original position
        """

    def getParam(self, axis):
        """Get the contraint position or euler angle of a generic 6DOF constraint
        
        :type axis: int
        :return: position
        :rtype: float
        :return: angle
        :rtype: float
        """

    constraint_id = None
    """Returns the contraint ID  (read only)
    
    :type: int
    """

    constraint_type = None
    """Returns the contraint type (read only)
    
    :type: integer
        - bge.constraints.POINTTOPOINT_CONSTRAINT
        - bge.constraints.LINEHINGE_CONSTRAINT
        - bge.constraints.ANGULAR_CONSTRAINT
        - bge.constraints.CONETWIST_CONSTRAINT
        - bge.constraints.VEHICLE_CONSTRAINT
        - bge.constraints.GENERIC_6DOF_CONSTRAINT
    """


class KX_LibLoadStatus(PyObjectPlus):
    """An object providing information about a LibLoad() operation."""

    onFinish = None
    """A callback that gets called when the lib load is done.
    
    :type: callable
    """

    finished = None
    """The current status of the lib load.
    
    :type: bool
    """

    progress = None
    """The current progress of the lib load as a normalized value from 0.0 to 1.0.
    
    :type: float
    """

    libraryName = ""
    """The name of the library being loaded (the first argument to LibLoad).
    
    :type: str
    """

    timeTaken = None
    """The amount of time, in seconds, the lib load took (0 until the operation is complete).
    
    :type: float
    """


class KX_Scene(PyObjectPlus):
    """An active scene that gives access to objects, cameras, lights and scene attributes.
    The activity culling stuff is supposed to disable logic bricks when their owner gets too far
                        from the active camera.  It was taken from some code lurking at the back of KX_Scene - who knows
                        what it does!
    @bug: All attributes are read only at the moment.
    """

    name = ""
    """The scene's name, (read-only).
    
    :type: str
    """

    objects = None
    """A list of objects in the scene, (read-only).
    (type: bge.types.CListValue of bge.types.KX_GameObject)
    
    :type: CListValue
    """

    objectsInactive = None
    """A list of objects on background layers (used for the addObject actuator), (read-only).
    (type: bge.types.CListValue of bge.types.KX_GameObject)
    
    :type: CListValue
    """

    lights = None
    """A list of lights in the scene, (read-only).
    (type: bge.types.CListValue of bge.types.KX_LightObject)
    
    :type: CListValue
    """

    cameras = None
    """A list of cameras in the scene, (read-only).
    (type: bge.types.CListValue of bge.types.KX_Camera)
    
    :type: CListValue
    """

    active_camera = None
    """The current active camera.
    (type: bge.types.KX_Camera)
    
    :type: KX_Camera
    """

    world = None
    """The current active world, (read-only).
    (type: bge.types.KX_WorldInfo)
    
    :type: KX_WorldInfo
    """

    suspended = None
    """True if the scene is suspended, (read-only).
    
    :type: bool
    """

    activity_culling = None
    """True if the scene is activity culling.
    
    :type: bool
    """

    activity_culling_radius = None
    """The distance outside which to do activity culling. Measured in manhattan distance.
    
    :type: float
    """

    dbvt_culling = None
    """True when Dynamic Bounding box Volume Tree is set (read-only).
    
    :type: bool
    """

    pre_draw = None
    """A list of callables to be run before the render step.
    
    :type: list
    """

    post_draw = None
    """A list of callables to be run after the render step.
    
    :type: list
    """

    pre_draw_setup = None
    """A list of callables to be run before the drawing setup (i.e., before the model view and projection matrices are computed).
    
    :type: list
    """

    gravity = None
    """The scene gravity using the world x, y and z axis.
    
    :type: Vector((gx, gy, gz))
    """

    def addObject(self, object, reference, time=0):
        """Adds an object to the scene like the Add Object Actuator would.
        
        :param object: The (name of the) object to add.
            (type: bge.types.KX_GameObject or string)
        :type object: KX_GameObject or string
        :param reference: The (name of the) object which position, orientation, and scale to copy (optional), if the object to add is a light and there is not reference the light's layer will be the same that the active layer in the blender scene.
            (type: bge.types.KX_GameObject or string)
        :type reference: KX_GameObject or string
        :param time: The lifetime of the added object, in frames. A time of 0 means the object will last forever (optional).
        :type time: int
        :return: The newly added object.
        :param : (type: bge.types.KX_GameObject)
        :rtype: KX_GameObject
        """

    def end(self):
        """Removes the scene from the game."""

    def restart(self):
        """Restarts the scene."""

    def replace(self, scene):
        """Replaces this scene with another one.
        
        :param scene: The name of the scene to replace this scene with.
        :type scene: str
        :return: True if the scene exists and was scheduled for addition, False otherwise.
        :rtype: bool
        """

    def suspend(self):
        """Suspends this scene."""

    def resume(self):
        """Resume this scene."""

    def get(self, key, default=None):
        """Return the value matching key, or the default value if its not found.
                                    :return: The key value or a default.
        """

    def drawObstacleSimulation(self):
        """Draw debug visualization of obstacle simulation."""


class KX_VehicleWrapper(PyObjectPlus):
    """KX_VehicleWrapper
    TODO - description
    """

    def addWheel(self, wheel, attachPos, downDir, axleDir, suspensionRestLength, wheelRadius, hasSteering):
        """Add a wheel to the vehicle
        
        :param wheel: The object to use as a wheel.
            (type: bge.types.KX_GameObject or a bge.types.KX_GameObject name)
        :type wheel: KX_GameObject or a KX_GameObject name
        :param attachPos: The position to attach the wheel, relative to the chassis object center.
            (type: vector of 3 floats)
        :type attachPos: vector
        :param downDir: The direction vector pointing down to where the vehicle should collide with the floor.
            (type: vector of 3 floats)
        :type downDir: vector
        :param axleDir: The axis the wheel rotates around, relative to the chassis.
            (type: vector of 3 floats)
        :type axleDir: vector
        :param suspensionRestLength: The length of the suspension when no forces are being applied.
        :type suspensionRestLength: float
        :param wheelRadius: The radius of the wheel (half the diameter).
        :type wheelRadius: float
        :param hasSteering: True if the wheel should turn with steering, typically used in front wheels.
        :type hasSteering: bool
        """

    def applyBraking(self, force, wheelIndex):
        """Apply a braking force to the specified wheel
        
        :param force: the brake force
        :type force: float
        :param wheelIndex: index of the wheel where the force needs to be applied
        :type wheelIndex: int
        """

    def applyEngineForce(self, force, wheelIndex):
        """Apply an engine force to the specified wheel
        
        :param force: the engine force
        :type force: float
        :param wheelIndex: index of the wheel where the force needs to be applied
        :type wheelIndex: int
        """

    def getConstraintId(self):
        """Get the constraint ID
        
        :return: the constraint id
        :rtype: int
        """

    def getConstraintType(self):
        """Returns the constraint type.
        
        :return: constraint type
        :rtype: int
        """

    def getNumWheels(self):
        """Returns the number of wheels.
        
        :return: the number of wheels for this vehicle
        :rtype: int
        """

    def getWheelOrientationQuaternion(self, wheelIndex):
        """Returns the wheel orientation as a quaternion.
        
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        :return: TODO Description
        :rtype: TODO - type should be quat as per method name but from the code it looks like a matrix
        """

    def getWheelPosition(self, wheelIndex):
        """Returns the position of the specified wheel
        
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        :return: position vector
        :rtype: list[x, y, z]
        """

    def getWheelRotation(self, wheelIndex):
        """Returns the rotation of the specified wheel
        
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        :return: the wheel rotation
        :rtype: float
        """

    def setRollInfluence(self, rollInfluece, wheelIndex):
        """Set the specified wheel's roll influence.
                                    The higher the roll influence the more the vehicle will tend to roll over in corners.
        
        :param rollInfluece: the wheel roll influence
        :type rollInfluece: float
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        """

    def setSteeringValue(self, steering, wheelIndex):
        """Set the specified wheel's steering
        
        :param steering: the wheel steering
        :type steering: float
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        """

    def setSuspensionCompression(self, compression, wheelIndex):
        """Set the specified wheel's compression
        
        :param compression: the wheel compression
        :type compression: float
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        """

    def setSuspensionDamping(self, damping, wheelIndex):
        """Set the specified wheel's damping
        
        :param damping: the wheel damping
        :type damping: float
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        """

    def setSuspensionStiffness(self, stiffness, wheelIndex):
        """Set the specified wheel's stiffness
        
        :param stiffness: the wheel stiffness
        :type stiffness: float
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        """

    def setTyreFriction(self, friction, wheelIndex):
        """Set the specified wheel's tyre friction
        
        :param friction: the tyre friction
        :type friction: float
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        """


class KX_WorldInfo(PyObjectPlus):
    """A world object."""

    KX_MIST_QUADRATIC = None
    """Type of quadratic attenuation used to fade mist."""

    KX_MIST_LINEAR = None
    """Type of linear attenuation used to fade mist."""

    KX_MIST_INV_QUADRATIC = None
    """Type of inverse quadratic attenuation used to fade mist."""

    mistEnable = None
    """Return the state of the mist.
    
    :type: bool
    """

    mistStart = None
    """The mist start point.
    
    :type: float
    """

    mistDistance = None
    """The mist distance fom the start point to reach 100% mist.
    
    :type: float
    """

    mistIntensity = None
    """The mist intensity.
    
    :type: float
    """

    mistType = None
    """The type of mist - must be KX_MIST_QUADRATIC, KX_MIST_LINEAR or KX_MIST_INV_QUADRATIC"""

    mistColor = None
    """The color of the mist. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].
                                Mist and background color sould always set to the same color.
    
    :type: mathutils.Color
    """

    backgroundColor = None
    """The color of the background. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].
                                Mist and background color sould always set to the same color.
    
    :type: mathutils.Color
    """

    ambientColor = None
    """The color of the ambient light. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].
    
    :type: mathutils.Color
    """


class SCA_PythonJoystick(PyObjectPlus):
    """A Python interface to a joystick."""

    name = ""
    """The name assigned to the joystick by the operating system. (read-only)
    
    :type: str
    """

    activeButtons = None
    """A list of active button values. (read-only)
    
    :type: list
    """

    axisValues = None
    """The state of the joysticks axis as a list of values bge.types.SCA_PythonJoystick.numAxis long. (read-only).
    Each specifying the value of an axis between -1.0 and 1.0
                                depending on how far the axis is pushed, 0 for nothing.
                                The first 2 values are used by most joysticks and gamepads for directional control.
                                3rd and 4th values are only on some joysticks and can be used for arbitary controls.
    * left:[-1.0, 0.0, ...]
    * right:[1.0, 0.0, ...]
    * up:[0.0, -1.0, ...]
    * down:[0.0, 1.0, ...]
    (type: list of ints.)
    
    :type: list
    """

    hatValues = None
    """The state of the joysticks hats as a list of values bge.types.SCA_PythonJoystick.numHats long. (read-only).
    Each specifying the direction of the hat from 1 to 12, 0 when inactive.
    Hat directions are as follows...
    * 0:None
    * 1:Up
    * 2:Right
    * 4:Down
    * 8:Left
    * 3:Up - Right
    * 6:Down - Right
    * 12:Down - Left
    * 9:Up - Left
    (type: list of ints)
    
    :type: list
    """

    numAxis = None
    """The number of axes for the joystick at this index. (read-only).
    
    :type: int
    """

    numButtons = None
    """The number of buttons for the joystick at this index. (read-only).
    
    :type: int
    """

    numHats = None
    """The number of hats for the joystick at this index. (read-only).
    
    :type: int
    """


class SCA_PythonKeyboard(PyObjectPlus):
    """The current keyboard."""

    events = None
    """A dictionary containing the status of each keyboard event or key. (read-only).
    
    :type: dictionary {bge.events#keyboard-keyskeycode:bge.logic#input-statusstatus, ...}
    """

    active_events = None
    """A dictionary containing the status of only the active keyboard events or keys. (read-only).
    
    :type: dictionary {bge.events#keyboard-keyskeycode:bge.logic#input-statusstatus, ...}
    """

    def getClipboard(self):
        """Gets the clipboard text.
        
        :rtype: str
        """

    def setClipboard(self, text):
        """Sets the clipboard text.
        
        :param text: New clipboard text
        :type text: str
        """


class SCA_PythonMouse(PyObjectPlus):
    """The current mouse."""

    events = None
    """a dictionary containing the status of each mouse event. (read-only).
    
    :type: dictionary {bge.events#mouse-keyskeycode:bge.logic#input-statusstatus, ...}
    """

    active_events = None
    """a dictionary containing the status of only the active mouse events. (read-only).
    
    :type: dictionary {bge.events#mouse-keyskeycode:bge.logic#input-statusstatus, ...}
    """

    position = None
    """The normalized x and y position of the mouse cursor.
    
    :type: tuple (x, y)
    """

    visible = None
    """The visibility of the mouse cursor.
    
    :type: bool
    """


class CPropValue(CValue):
    """This class has no python functions"""


class SCA_ILogicBrick(CValue):
    """Base class for all logic bricks."""

    executePriority = None
    """This determines the order controllers are evaluated, and actuators are activated (lower priority is executed first).
    
    :type: executePriority: int
    """

    owner = None
    """The game object this logic brick is attached to (read-only).
    (type: bge.types.KX_GameObject or None in exceptional cases.)
    
    :type: KX_GameObject or None in exceptional cases.
    """

    name = ""
    """The name of this logic brick (read-only).
    
    :type: str
    """


class SCA_IObject(CValue):
    """This class has no python functions"""


class CListValue(CPropValue):
    """This is a list like object used in the game engine internally that behaves similar to a python list in most ways.
    As well as the normal index lookup (val= clist[i]), CListValue supports string lookups (val= scene.objects["Cube"])
    Other operations such as len(clist), list(clist), clist[0:10] are also supported.
    """

    def append(self, val):
        """Add an item to the list (like pythons append)"""

    def count(self, val):
        """Count the number of instances of a value in the list.
        
        :return: number of instances
        :rtype: int
        """

    def index(self, val):
        """Return the index of a value in the list.
        
        :return: The index of the value in the list.
        :rtype: int
        """

    def reverse(self):
        """Reverse the order of the list."""

    def get(self, key, default=None):
        """Return the value matching key, or the default value if its not found.
        
        :return: The key value or a default.
        """

    def from_id(self, id):
        """This is a funtion especially for the game engine to return a value with a spesific id.
        Since object names are not always unique, the id of an object can be used to get an object from the CValueList.
        Example:
        Where myObID is an int or long from the id function.
        This has the advantage that you can store the id in places you could not store a gameObject.
        """


class KX_GameObject(SCA_IObject):
    """All game objects are derived from this class.
    Properties assigned to game objects are accessible as attributes of this class.
    <Note> Calling ANY method or attribute on an object that has been removed from a scene will raise a SystemError,
                                if an object may have been removed since last accessing it use the invalid attribute to check.
    KX_GameObject can be subclassed to extend functionality. For example:
    When subclassing objects other than empties and meshes, the specific type
                        should be used - e.g. inherit from bge.types.BL_ArmatureObject when the object
                        to mutate is an armature.
    """

    name = ""
    """The object's name. (read-only).
    
    :type: str
    """

    mass = None
    """The object's mass
    
    :type: float
    """

    isSuspendDynamics = None
    """The object's dynamic state (read-only).
    
    :type: bool
    """

    linearDamping = None
    """The object's linear damping, also known as translational damping. Can be set simultaneously with angular damping using the bge.types.KX_GameObject.setDamping method.
    
    :type: float between 0 and 1 inclusive.
    """

    angularDamping = None
    """The object's angular damping, also known as rotationation damping. Can be set simultaneously with linear damping using the bge.types.KX_GameObject.setDamping method.
    
    :type: float between 0 and 1 inclusive.
    """

    linVelocityMin = None
    """Enforces the object keeps moving at a minimum velocity.
    
    :type: float
    """

    linVelocityMax = None
    """Clamp the maximum linear velocity to prevent objects moving beyond a set speed.
    
    :type: float
    """

    angularVelocityMin = None
    """Enforces the object keeps rotating at a minimum velocity. A value of 0.0 disables this.
    
    :type: non-negative float
    """

    angularVelocityMax = None
    """Clamp the maximum angular velocity to prevent objects rotating beyond a set speed.
                                A value of 0.0 disables clamping; it does not stop rotation.
    
    :type: non-negative float
    """

    localInertia = None
    """the object's inertia vector in local coordinates. Read only.
    
    :type: Vector((ix, iy, iz))
    """

    parent = None
    """The object's parent object. (read-only).
    (type: bge.types.KX_GameObject or None)
    
    :type: KX_GameObject or None
    """

    groupMembers = None
    """Returns the list of group members if the object is a group object (dupli group instance), otherwise None is returned.
    (type: bge.types.CListValue of bge.types.KX_GameObject or None)
    
    :type: CListValue
    """

    groupObject = None
    """Returns the group object (dupli group instance) that the object belongs to or None if the object is not part of a group.
    (type: bge.types.KX_GameObject or None)
    
    :type: KX_GameObject or None
    """

    collisionGroup = None
    """The object's collision group.
    
    :type: bitfield
    """

    collisionMask = None
    """The object's collision mask.
    
    :type: bitfield
    """

    collisionCallbacks = None
    """A list of functions to be called when a collision occurs.
    Callbacks should either accept one argument (object), or three
                                arguments (object, point, normal). For simplicity, per
                                colliding object only the first collision point is reported.
    (type: list of functions and/or methods)
    
    :type: list
    """

    scene = None
    """The object's scene. (read-only).
    (type: bge.types.KX_Scene or None)
    
    :type: KX_Scene or None
    """

    visible = None
    """visibility flag.
    
    :type: bool
    """

    record_animation = None
    """Record animation for this object.
    
    :type: bool
    """

    color = None
    """The object color of the object. [r, g, b, a]
    
    :type: mathutils.Vector
    """

    occlusion = None
    """occlusion capability flag.
    
    :type: bool
    """

    position = None
    """The object's position. [x, y, z] On write: local position, on read: world position
    
    :type: mathutils.Vector
    """

    orientation = None
    """The object's orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector. On write: local orientation, on read: world orientation
    
    :type: mathutils.Matrix
    """

    scaling = None
    """The object's scaling factor. [sx, sy, sz] On write: local scaling, on read: world scaling
    
    :type: mathutils.Vector
    """

    localOrientation = None
    """The object's local orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector.
    
    :type: mathutils.Matrix
    """

    worldOrientation = None
    """The object's world orientation. 3x3 Matrix.
    
    :type: mathutils.Matrix
    """

    localScale = None
    """The object's local scaling factor. [sx, sy, sz]
    
    :type: mathutils.Vector
    """

    worldScale = None
    """The object's world scaling factor. [sx, sy, sz]
    
    :type: mathutils.Vector
    """

    localPosition = None
    """The object's local position. [x, y, z]
    
    :type: mathutils.Vector
    """

    worldPosition = None
    """The object's world position. [x, y, z]
    
    :type: mathutils.Vector
    """

    localTransform = None
    """The object's local space transform matrix. 4x4 Matrix.
    
    :type: mathutils.Matrix
    """

    worldTransform = None
    """The object's world space transform matrix. 4x4 Matrix.
    
    :type: mathutils.Matrix
    """

    localLinearVelocity = None
    """The object's local linear velocity. [x, y, z]
    
    :type: mathutils.Vector
    """

    worldLinearVelocity = None
    """The object's world linear velocity. [x, y, z]
    
    :type: mathutils.Vector
    """

    localAngularVelocity = None
    """The object's local angular velocity. [x, y, z]
    
    :type: mathutils.Vector
    """

    worldAngularVelocity = None
    """The object's world angular velocity. [x, y, z]
    
    :type: mathutils.Vector
    """

    timeOffset = None
    """adjust the slowparent delay at runtime.
    
    :type: float
    """

    state = None
    """the game object's state bitmask, using the first 30 bits, one bit must always be set.
    
    :type: int
    """

    meshes = None
    """a list meshes for this object.
    (type: list of bge.types.KX_MeshProxy)
    
    :type: list
    """

    sensors = None
    """a sequence of bge.types.SCA_ISensor objects with string/index lookups and iterator support.
    
    :type: list
    """

    controllers = None
    """a sequence of bge.types.SCA_IController objects with string/index lookups and iterator support.
    (type: list of bge.types.SCA_ISensor)
    
    :type: list
    """

    actuators = None
    """a list of bge.types.SCA_IActuator with string/index lookups and iterator support.
    
    :type: list
    """

    attrDict = None
    """get the objects internal python attribute dictionary for direct (faster) access.
    
    :type: dict
    """

    children = None
    """direct children of this object, (read-only).
    (type: bge.types.CListValue of bge.types.KX_GameObject's)
    
    :type: CListValue
    """

    childrenRecursive = None
    """all children of this object including children's children, (read-only).
    (type: bge.types.CListValue of bge.types.KX_GameObject's)
    
    :type: CListValue
    """

    life = None
    """The number of seconds until the object ends, assumes 50fps.
                                (when added with an add object actuator), (read-only).
    
    :type: float
    """

    debug = None
    """If true, the object's debug properties will be displayed on screen.
    
    :type: bool
    """

    debugRecursive = None
    """If true, the object's and children's debug properties will be displayed on screen.
    
    :type: bool
    """

    currentLodLevel = None
    """The index of the level of detail (LOD) currently used by this object (read-only).
    
    :type: int
    """

    def endObject(self):
        """Delete this object, can be used in place of the EndObject Actuator.
        The actual removal of the object from the scene is delayed.
        """

    def replaceMesh(self, mesh, useDisplayMesh=True, usePhysicsMesh=False):
        """Replace the mesh of this object with a new mesh. This works the same was as the actuator.
        
        :param mesh: mesh to replace or the meshes name.
        :type mesh: MeshProxy or string
        :param useDisplayMesh: when enabled the display mesh will be replaced (optional argument).
        :type useDisplayMesh: bool
        :param usePhysicsMesh: when enabled the physics mesh will be replaced (optional argument).
        :type usePhysicsMesh: bool
        """

    def setVisible(self, visible, recursive):
        """Sets the game object's visible flag.
        
        :param visible: the visible state to set.
        :type visible: bool
        :param recursive: optional argument to set all childrens visibility flag too.
        :type recursive: bool
        """

    def setOcclusion(self, occlusion, recursive):
        """Sets the game object's occlusion capability.
        
        :param occlusion: the state to set the occlusion to.
        :type occlusion: bool
        :param recursive: optional argument to set all childrens occlusion flag too.
        :type recursive: bool
        """

    def alignAxisToVect(self, vect, axis=2, factor=1.0):
        """Aligns any of the game object's axis along the given vector.
        
        :param vect: a vector to align the axis.
        :type vect: 3D vector
        :param axis: The axis you want to align
            * 0: X axis
            * 1: Y axis
            * 2: Z axis
        :type axis: int
        :param factor: Only rotate a feaction of the distance to the target vector (0.0 - 1.0)
        :type factor: float
        """

    def getAxisVect(self, vect):
        """Returns the axis vector rotates by the object's worldspace orientation.
                                    This is the equivalent of multiplying the vector by the orientation matrix.
        
        :param vect: a vector to align the axis.
        :type vect: 3D Vector
        :return: The vector in relation to the objects rotation.
        :rtype: 3d vector.
        """

    def applyMovement(self, movement, local=False):
        """Sets the game object's movement.
        
        :param movement: movement vector.
        :type movement: 3D Vector
        :param local:
            * False: you get the "global" movement ie: relative to world orientation.
            * True: you get the "local" movement ie: relative to object orientation.
        :param local: boolean
        """

    def applyRotation(self, rotation, local=False):
        """Sets the game object's rotation.
        
        :param rotation: rotation vector.
        :type rotation: 3D Vector
        :param local:
            * False: you get the "global" rotation ie: relative to world orientation.
            * True: you get the "local" rotation ie: relative to object orientation.
        :param local: boolean
        """

    def applyForce(self, force, local=False):
        """Sets the game object's force.
        This requires a dynamic object.
        
        :param force: force vector.
        :type force: 3D Vector
        :param local:
            * False: you get the "global" force ie: relative to world orientation.
            * True: you get the "local" force ie: relative to object orientation.
        :type local: bool
        """

    def applyTorque(self, torque, local=False):
        """Sets the game object's torque.
        This requires a dynamic object.
        
        :param torque: torque vector.
        :type torque: 3D Vector
        :param local:
            * False: you get the "global" torque ie: relative to world orientation.
            * True: you get the "local" torque ie: relative to object orientation.
        :type local: bool
        """

    def getLinearVelocity(self, local=False):
        """Gets the game object's linear velocity.
        This method returns the game object's velocity through it's center of mass, ie no angular velocity component.
        
        :param local:
            * False: you get the "global" velocity ie: relative to world orientation.
            * True: you get the "local" velocity ie: relative to object orientation.
        :type local: bool
        :return: the object's linear velocity.
        :rtype: Vector((vx, vy, vz))
        """

    def setLinearVelocity(self, velocity, local=False):
        """Sets the game object's linear velocity.
        This method sets game object's velocity through it's center of mass,
                                    ie no angular velocity component.
        This requires a dynamic object.
        
        :param velocity: linear velocity vector.
        :type velocity: 3D Vector
        :param local:
            * False: you get the "global" velocity ie: relative to world orientation.
            * True: you get the "local" velocity ie: relative to object orientation.
        :type local: bool
        """

    def getAngularVelocity(self, local=False):
        """Gets the game object's angular velocity.
        
        :param local:
            * False: you get the "global" velocity ie: relative to world orientation.
            * True: you get the "local" velocity ie: relative to object orientation.
        :type local: bool
        :return: the object's angular velocity.
        :rtype: Vector((vx, vy, vz))
        """

    def setAngularVelocity(self, velocity, local=False):
        """Sets the game object's angular velocity.
        This requires a dynamic object.
        
        :param velocity: angular velocity vector.
        :type velocity: bool
        :param local:
            * False: you get the "global" velocity ie: relative to world orientation.
            * True: you get the "local" velocity ie: relative to object orientation.
        """

    def getVelocity(self, point=(0, 0, 0)):
        """Gets the game object's velocity at the specified point.
        Gets the game object's velocity at the specified point, including angular
                                    components.
        
        :param point: optional point to return the velocity for, in local coordinates.
        :type point: 3D Vector
        :return: the velocity at the specified point.
        :rtype: Vector((vx, vy, vz))
        """

    def getReactionForce(self):
        """Gets the game object's reaction force.
        The reaction force is the force applied to this object over the last simulation timestep.
                                    This also includes impulses, eg from collisions.
        <Note> This is not implimented at the moment.
        
        :return: the reaction force of this object.
        :rtype: Vector((fx, fy, fz))
        """

    def applyImpulse(self, point, impulse, local=False):
        """Applies an impulse to the game object.
        This will apply the specified impulse to the game object at the specified point.
                                    If point != position, applyImpulse will also change the object's angular momentum.
                                    Otherwise, only linear momentum will change.
        
        :param point: the point to apply the impulse to (in world or local coordinates)
        :type point: freestyle.types.StrokeVertex.point [ix, iy, iz] the point to apply the impulse to (in world or local coordinates)
        :param impulse: impulse vector.
        :type impulse: 3D Vector
        :param local:
            * False: you get the "global" impulse ie: relative to world coordinates with world orientation.
            * True: you get the "local" impulse ie: relative to local coordinates with object orientation.
        :type local: bool
        """

    def setDamping(self, linear_damping, angular_damping):
        """Sets both the bge.types.KX_GameObject.linearDamping and bge.types.KX_GameObject.angularDamping simultaneously. This is more efficient than setting both properties individually.
        
        :param linear_damping: Linear ("translational") damping factor.
        :type linear_damping: float ∈ [0, 1]
        :param angular_damping: Angular ("rotational") damping factor.
        :type angular_damping: float ∈ [0, 1]
        """

    def suspendDynamics(self, ghost:"Optional"):
        """Suspends physics for this object.
        <See also> bge.types.KX_GameObject.isSuspendDynamics allows you to inspect whether the object is in a suspended state.
        
        :param ghost: When set to True, collisions with the object will be ignored, similar to the "ghost" checkbox in
                                                    Blender. When False (the default), the object becomes static but still collide with other objects.
        :type ghost: bool
        """

    def restoreDynamics(self):
        """Resumes physics for this object. Also reinstates collisions; the object will no longer be a ghost.
        <Note> The objects linear velocity will be applied from when the dynamics were suspended.
        """

    def enableRigidBody(self):
        """Enables rigid body physics for this object.
        Rigid body physics allows the object to roll on collisions.
        """

    def disableRigidBody(self):
        """Disables rigid body physics for this object."""

    def setParent(self, parent, compound=True, ghost=True):
        """Sets this object's parent.
                                    Control the shape status with the optional compound and ghost parameters:
        In that case you can control if it should be ghost or not:
        <Note> If the object type is sensor, it stays ghost regardless of ghost parameter
        
        :param parent: new parent object.
            (type: bge.types.KX_GameObject)
        :type parent: KX_GameObject
        :param compound: whether the shape should be added to the parent compound shape.
            * True: the object shape should be added to the parent compound shape.
            * False: the object should keep its individual shape.
        :type compound: bool
        :param ghost: whether the object should be ghost while parented.
            * True: if the object should be made ghost while parented.
            * False: if the object should be solid while parented.
        :type ghost: bool
        """

    def removeParent(self):
        """Removes this objects parent."""

    def getPhysicsId(self):
        """Returns the user data object associated with this game object's physics controller."""

    def getPropertyNames(self):
        """Gets a list of all property names.
        
        :return: All property names for this object.
        :rtype: list
        """

    def getDistanceTo(self, other):
        """
        :param other: a point or another bge.types.KX_GameObject to measure the distance to.
            (type: bge.types.KX_GameObject or list [x, y, z])
        :type other: KX_GameObject or list [x, y, z]
        :return: distance to another object or point.
        :rtype: float
        """

    def getVectTo(self, other):
        """Returns the vector and the distance to another object or point.
                                    The vector is normalized unless the distance is 0, in which a zero length vector is returned.
        
        :param other: a point or another bge.types.KX_GameObject to get the vector and distance to.
            (type: bge.types.KX_GameObject or list [x, y, z])
        :type other: KX_GameObject or list [x, y, z]
        :return: (distance, globalVector(3), localVector(3))
        :rtype: 3-tuple (float, 3-tuple (x, y, z), 3-tuple (x, y, z))
        """

    def rayCastTo(self, other, dist, prop):
        """Look towards another point/object and find first object hit within dist that matches prop.
        The ray is always casted from the center of the object, ignoring the object itself.
                                    The ray is casted towards the center of another object or an explicit [x, y, z] point.
                                    Use rayCast() if you need to retrieve the hit point
        
        :param other: [x, y, z] or object towards which the ray is casted
            (type: bge.types.KX_GameObject or 3-tuple)
        :type other: KX_GameObject or 3-tuple
        :param dist: max distance to look (can be negative => look behind); 0 or omitted => detect up to other
        :type dist: float
        :param prop: property name that object must have; can be omitted => detect any object
        :type prop: str
        :return: the first object hit or None if no object or object does not match prop
        :param : (type: bge.types.KX_GameObject)
        :rtype: KX_GameObject
        """

    def rayCast(self, objto, objfrom, dist, prop, face, xray, poly, mask):
        """Look from a point/object to another point/object and find first object hit within dist that matches prop.
                                    if poly is 0, returns a 3-tuple with object reference, hit point and hit normal or (None, None, None) if no hit.
                                    if poly is 1, returns a 4-tuple with in addition a bge.types.KX_PolyProxy as 4th element.
                                    if poly is 2, returns a 5-tuple with in addition a 2D vector with the UV mapping of the hit point as 5th element.
        The face parameter determines the orientation of the normal.
        * 0 => hit normal is always oriented towards the ray origin (as if you casted the ray from outside)
        * 1 => hit normal is the real face normal (only for mesh object, otherwise face has no effect)
        The ray has X-Ray capability if xray parameter is 1, otherwise the first object hit (other than self object) stops the ray.
                                    The prop and xray parameters interact as follow.
        * prop off, xray off: return closest hit or no hit if there is no object on the full extend of the ray.
        * prop off, xray on : idem.
        * prop on, xray off: return closest hit if it matches prop, no hit otherwise.
        * prop on, xray on : return closest hit matching prop or no hit if there is no object matching prop on the full extend of the ray.
        The bge.types.KX_PolyProxy 4th element of the return tuple when poly=1 allows to retrieve information on the polygon hit by the ray.
                                    If there is no hit or the hit object is not a static mesh, None is returned as 4th element.
        The ray ignores collision-free objects and faces that dont have the collision flag enabled, you can however use ghost objects.
        <Note> The ray ignores the object on which the method is called. It is casted from/to object center or explicit [x, y, z] points.
        
        :param objto: [x, y, z] or object to which the ray is casted
            (type: bge.types.KX_GameObject or 3-tuple)
        :type objto: KX_GameObject or 3-tuple
        :param objfrom: [x, y, z] or object from which the ray is casted; None or omitted => use self object center
            (type: bge.types.KX_GameObject or 3-tuple or None)
        :type objfrom: KX_GameObject or 3-tuple or None
        :param dist: max distance to look (can be negative => look behind); 0 or omitted => detect up to to
        :type dist: float
        :param prop: property name that object must have; can be omitted or "" => detect any object
        :type prop: str
        :param face: normal option: 1=>return face normal; 0 or omitted => normal is oriented towards origin
        :type face: int
        :param xray: X-ray option: 1=>skip objects that don't match prop; 0 or omitted => stop on first object
        :type xray: int
        :param poly: polygon option: 0, 1 or 2 to return a 3-, 4- or 5-tuple with information on the face hit.
            * 0 or omitted: return value is a 3-tuple (object, hitpoint, hitnormal) or (None, None, None) if no hit
            * 1: return value is a 4-tuple and the 4th element is a bge.types.KX_PolyProxy or None if no hit or the object doesn't use a mesh collision shape.
            * 2: return value is a 5-tuple and the 5th element is a 2-tuple (u, v) with the UV mapping of the hit point or None if no hit, or the object doesn't use a mesh collision shape, or doesn't have a UV mapping.
        :type poly: int
        :param mask: collision mask: The collision mask (16 layers mapped to a 16-bit integer) is combined with each object's collision group, to hit only a subset of the objects in the scene. Only those objects for which collisionGroup & mask is true can be hit.
        :type mask: bitfield
        :return: (object, hitpoint, hitnormal) or (object, hitpoint, hitnormal, polygon) or (object, hitpoint, hitnormal, polygon, hituv).
            * object, hitpoint and hitnormal are None if no hit.
            * polygon is valid only if the object is valid and is a static object, a dynamic object using mesh collision shape or a soft body object, otherwise it is None
            * hituv is valid only if polygon is valid and the object has a UV mapping, otherwise it is None
        :param : (type: * 3-tuple (bge.types.KX_GameObject, 3-tuple (x, y, z), 3-tuple (nx, ny, nz))
            * or 4-tuple (bge.types.KX_GameObject, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), bge.types.KX_PolyProxy)
            * or 5-tuple (bge.types.KX_GameObject, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), bge.types.KX_PolyProxy, 2-tuple (u, v)))
        :rtype: * 3-tuple (KX_GameObject, 3-tuple (x, y, z), 3-tuple (nx, ny, nz))
            * or 4-tuple (KX_GameObject, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), KX_PolyProxy)
            * or 5-tuple (KX_GameObject, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), KX_PolyProxy, 2-tuple (u, v))
        """

    def setCollisionMargin(self, margin):
        """Set the objects collision margin.
        <Note> If this object has no physics controller (a physics ID of zero), this function will raise RuntimeError.
        
        :param margin: the collision margin distance in blender units.
        :type margin: float
        """

    def sendMessage(self, subject, body="", to=""):
        """Sends a message.
        
        :param subject: The subject of the message
        :type subject: str
        :param body: The body of the message (optional)
        :type body: str
        :param to: The name of the object to send the message to (optional)
        :type to: str
        """

    def reinstancePhysicsMesh(self, gameObject, meshObject):
        """Updates the physics system with the changed mesh.
        If no arguments are given the physics mesh will be re-created from the first mesh assigned to the game object.
        <Note> If this object has instances the other instances will be updated too.
        <Note> The gameObject argument has an advantage that it can convert from a mesh with modifiers applied (such as the Subdivision Surface modifier).
        
        :param gameObject: optional argument, set the physics shape from this gameObjets mesh.
            (type: string, bge.types.KX_GameObject or None)
        :type gameObject: string, KX_GameObject or None
        :param meshObject: optional argument, set the physics shape from this mesh.
        :type meshObject: string, MeshProxy or None
        :return: True if reinstance succeeded, False if it failed.
        :rtype: bool
        """

    def get(self, key, default=None):
        """Return the value matching key, or the default value if its not found.
                                    :return: The key value or a default.
        """

    def playAction(self, name, start_frame, end_frame, layer=0, priority=0, blendin=0, play_mode=logic.KX_ACTION_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=1.0, blend_mode=logic.KX_ACTION_BLEND_BLEND):
        """Plays an action.
        
        :param name: the name of the action
        :type name: str
        :param start: the start frame of the action
        :type start: float
        :param end: the end frame of the action
        :type end: float
        :param layer: the layer the action will play in (actions in different layers are added/blended together)
        :type layer: int
        :param priority: only play this action if there isn't an action currently playing in this layer with a higher (lower number) priority
        :type priority: int
        :param blendin: the amount of blending between this animation and the previous one on this layer
        :type blendin: float
        :param play_mode: the play mode
            (type: one of bge.logic#gameobject-playaction-modethese constants)
        :type play_mode: one
        :param layer_weight: how much of the previous layer to use for blending
        :type layer_weight: float
        :param ipo_flags: flags for the old IPO behaviors (force, etc)
        :type ipo_flags: int bitfield
        :param speed: the playback speed of the action as a factor (1.0 = normal speed, 2.0 = 2x speed, etc)
        :type speed: float
        :param blend_mode: how to blend this layer with previous layers
            (type: one of bge.logic#gameobject-playaction-blendthese constants)
        :type blend_mode: one
        """

    def stopAction(self, layer=0):
        """Stop playing the action on the given layer.
        
        :param layer: The layer to stop playing.
        :type layer: int
        """

    def getActionFrame(self, layer=0):
        """Gets the current frame of the action playing in the supplied layer.
        
        :param layer: The layer that you want to get the frame from.
        :type layer: int
        :return: The current frame of the action
        :rtype: float
        """

    def getActionName(self, layer=0):
        """Gets the name of the current action playing in the supplied layer.
        
        :param layer: The layer that you want to get the action name from.
        :type layer: int
        :return: The name of the current action
        :rtype: str
        """

    def setActionFrame(self, frame, layer=0):
        """Set the current frame of the action playing in the supplied layer.
        
        :param layer: The layer where you want to set the frame
        :type layer: int
        :param frame: The frame to set the action to
        :type frame: float
        """

    def isPlayingAction(self, layer=0):
        """Checks to see if there is an action playing in the given layer.
        
        :param layer: The layer to check for a playing action.
        :type layer: int
        :return: Whether or not the action is playing
        :rtype: bool
        """

    def addDebugProperty(self, name, debug = True):
        """Adds a single debug property to the debug list.
        
        :param name: name of the property that added to the debug list.
        :type name: str
        :param debug: the debug state.
        :type debug: bool
        """


class KX_MeshProxy(SCA_IObject):
    """A mesh object.
    You can only change the vertex properties of a mesh object, not the mesh topology.
    To use mesh objects effectively, you should know a bit about how the game engine handles them.
    The correct method of iterating over every bge.types.KX_VertexProxy in a game object
    """

    materials = None
    """(type: list of bge.types.KX_BlenderMaterial type)
    
    :type: list
    """

    numPolygons = None
    """:type: int"""

    numMaterials = None
    """:type: int"""

    def getMaterialName(self, matid):
        """Gets the name of the specified material.
        
        :param matid: the specified material.
        :type matid: int
        :return: the attached material name.
        :rtype: str
        """

    def getTextureName(self, matid):
        """Gets the name of the specified material's texture.
        
        :param matid: the specified material
        :type matid: int
        :return: the attached material's texture name.
        :rtype: str
        """

    def getVertexArrayLength(self, matid):
        """Gets the length of the vertex array associated with the specified material.
        There is one vertex array for each material.
        
        :param matid: the specified material
        :type matid: int
        :return: the number of verticies in the vertex array.
        :rtype: int
        """

    def getVertex(self, matid, index):
        """Gets the specified vertex from the mesh object.
        
        :param matid: the specified material
        :type matid: int
        :param index: the index into the vertex array.
        :type index: int
        :return: a vertex object.
        :param : (type: bge.types.KX_VertexProxy)
        :rtype: KX_VertexProxy
        """

    def getPolygon(self, index):
        """Gets the specified polygon from the mesh.
        
        :param index: polygon number
        :type index: int
        :return: a polygon object.
        :param : (type: bge.types.KX_PolyProxy)
        :rtype: KX_PolyProxy
        """

    def transform(self, matid, matrix):
        """Transforms the vertices of a mesh.
        
        :param matid: material index, -1 transforms all.
        :type matid: int
        :param matrix: transformation matrix.
        :type matrix: 4x4 matrix [[float]]
        """

    def transformUV(self, matid, matrix, uv_index=-1, uv_index_from=-1):
        """Transforms the vertices UV's of a mesh.
        
        :param matid: material index, -1 transforms all.
        :type matid: int
        :param matrix: transformation matrix.
        :type matrix: 4x4 matrix [[float]]
        :param uv_index: optional uv index, -1 for all, otherwise 0 or 1.
        :type uv_index: int
        :param uv_index_from: optional uv index to copy from, -1 to transform the current uv.
        :type uv_index_from: int
        """


class KX_PolyProxy(SCA_IObject):
    """A polygon holds the index of the vertex forming the poylgon.
    Note:
                        The polygon attributes are read-only, you need to retrieve the vertex proxy if you want
                        to change the vertex settings.
    """

    material_name = ""
    """The name of polygon material, empty if no material.
    
    :type: str
    """

    material = None
    """The material of the polygon.
    (type: bge.types.KX_BlenderMaterial)
    
    :type: KX_BlenderMaterial
    """

    texture_name = ""
    """The texture name of the polygon.
    
    :type: str
    """

    material_id = None
    """The material index of the polygon, use this to retrieve vertex proxy from mesh proxy.
    
    :type: int
    """

    v1 = None
    """vertex index of the first vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.
    
    :type: int
    """

    v2 = None
    """vertex index of the second vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.
    
    :type: int
    """

    v3 = None
    """vertex index of the third vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.
    
    :type: int
    """

    v4 = None
    """Vertex index of the fourth vertex of the polygon, 0 if polygon has only 3 vertex
                                Use this to retrieve vertex proxy from mesh proxy.
    
    :type: int
    """

    visible = None
    """visible state of the polygon: 1=visible, 0=invisible.
    
    :type: int
    """

    collide = None
    """collide state of the polygon: 1=receives collision, 0=collision free.
    
    :type: int
    """

    def getMaterialName(self):
        """Returns the polygon material name with MA prefix
        
        :return: material name
        :rtype: str
        """

    def getMaterial(self):
        """
        :return: The polygon material
        :param : (type: bge.types.KX_BlenderMaterial)
        :rtype: KX_BlenderMaterial
        """

    def getTextureName(self):
        """
        :return: The texture name
        :rtype: str
        """

    def getMaterialIndex(self):
        """Returns the material bucket index of the polygon.
                                    This index and the ones returned by getVertexIndex() are needed to retrieve the vertex proxy from MeshProxy.
        
        :return: the material index in the mesh
        :rtype: int
        """

    def getNumVertex(self):
        """Returns the number of vertex of the polygon.
        
        :return: number of vertex, 3 or 4.
        :rtype: int
        """

    def isVisible(self):
        """Returns whether the polygon is visible or not
        
        :return: 0=invisible, 1=visible
        :rtype: bool
        """

    def isCollider(self):
        """Returns whether the polygon is receives collision or not
        
        :return: 0=collision free, 1=receives collision
        :rtype: int
        """

    def getVertexIndex(self, vertex):
        """Returns the mesh vertex index of a polygon vertex
                                    This index and the one returned by getMaterialIndex() are needed to retrieve the vertex proxy from MeshProxy.
        
        :param vertex: index of the vertex in the polygon: 0->3
        :param vertex: integer
        :return: mesh vertex index
        :rtype: int
        """

    def getMesh(self):
        """Returns a mesh proxy
        
        :return: mesh proxy
        :rtype: MeshProxy
        """


class KX_VertexProxy(SCA_IObject):
    """A vertex holds position, UV, color and normal information.
    Note:
                        The physics simulation is NOT currently updated - physics will not respond
                        to changes in the vertex position.
    """

    XYZ = None
    """The position of the vertex.
    
    :type: Vector((x, y, z))
    """

    UV = None
    """The texture coordinates of the vertex.
    
    :type: Vector((u, v))
    """

    normal = None
    """The normal of the vertex.
    
    :type: Vector((nx, ny, nz))
    """

    color = None
    """The color of the vertex.
    Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0]
    
    :type: Vector((r, g, b, a))
    """

    x = None
    """The x coordinate of the vertex.
    
    :type: float
    """

    y = None
    """The y coordinate of the vertex.
    
    :type: float
    """

    z = None
    """The z coordinate of the vertex.
    
    :type: float
    """

    u = None
    """The u texture coordinate of the vertex.
    
    :type: float
    """

    v = None
    """The v texture coordinate of the vertex.
    
    :type: float
    """

    u2 = None
    """The second u texture coordinate of the vertex.
    
    :type: float
    """

    v2 = None
    """The second v texture coordinate of the vertex.
    
    :type: float
    """

    r = None
    """The red component of the vertex color. 0.0 <= r <= 1.0.
    
    :type: float
    """

    g = None
    """The green component of the vertex color. 0.0 <= g <= 1.0.
    
    :type: float
    """

    b = None
    """The blue component of the vertex color. 0.0 <= b <= 1.0.
    
    :type: float
    """

    a = None
    """The alpha component of the vertex color. 0.0 <= a <= 1.0.
    
    :type: float
    """

    def getXYZ(self):
        """Gets the position of this vertex.
        
        :return: this vertexes position in local coordinates.
        :rtype: Vector((x, y, z))
        """

    def setXYZ(self, pos):
        """Sets the position of this vertex.
        
        :type: Vector((x, y, z))
        :param pos: the new position for this vertex in local coordinates.
        """

    def getUV(self):
        """Gets the UV (texture) coordinates of this vertex.
        
        :return: this vertexes UV (texture) coordinates.
        :rtype: Vector((u, v))
        """

    def setUV(self, uv):
        """Sets the UV (texture) coordinates of this vertex.
        
        :type: Vector((u, v))
        """

    def getUV2(self):
        """Gets the 2nd UV (texture) coordinates of this vertex.
        
        :return: this vertexes UV (texture) coordinates.
        :rtype: Vector((u, v))
        """

    def setUV2(self, uv, unit):
        """Sets the 2nd UV (texture) coordinates of this vertex.
        
        :type: Vector((u, v))
        :param unit: optional argument, FLAT==1, SECOND_UV==2, defaults to SECOND_UV
        :param unit: integer
        """

    def getRGBA(self):
        """Gets the color of this vertex.
        The color is represented as four bytes packed into an integer value.  The color is
                                    packed as RGBA.
        Since Python offers no way to get each byte without shifting, you must use the struct module to
                                    access color in an machine independent way.
        Because of this, it is suggested you use the r, g, b and a attributes or the color attribute instead.
        
        :return: packed color. 4 byte integer with one byte per color channel in RGBA format.
        :rtype: int
        """

    def setRGBA(self, col):
        """Sets the color of this vertex.
        See getRGBA() for the format of col, and its relevant problems.  Use the r, g, b and a attributes
                                    or the color attribute instead.
        setRGBA() also accepts a four component list as argument col.  The list represents the color as [r, g, b, a]
                                    with black = [0.0, 0.0, 0.0, 1.0] and white = [1.0, 1.0, 1.0, 1.0]
        
        :param col: the new color of this vertex in packed RGBA format.
            (type: integer or bpy.types.ThemeSpaceListGeneric.list [bge.types.KX_VertexProxy.r, bge.types.KX_VertexProxy.g, bge.types.KX_VertexProxy.b, bge.types.KX_VertexProxy.a])
        :type col: integer or bpy.types.ThemeSpaceListGeneric.list [KX_VertexProxy.r, KX_VertexProxy.g, KX_VertexProxy.b, KX_VertexProxy.a]
        """

    def getNormal(self):
        """Gets the normal vector of this vertex.
        
        :return: normalized normal vector.
        :rtype: Vector((nx, ny, nz))
        """

    def setNormal(self, normal):
        """Sets the normal vector of this vertex.
        (type: sequence of floats [r, g, b])
        
        :type: collections.Sequence
        :param normal: the new normal of this vertex.
        """


class SCA_IActuator(SCA_ILogicBrick):
    """Base class for all actuator logic bricks."""


class SCA_IController(SCA_ILogicBrick):
    """Base class for all controller logic bricks."""

    state = None
    """The controllers state bitmask. This can be used with the GameObject's state to test if the controller is active.
    
    :type: int bitmask
    """

    sensors = None
    """A list of sensors linked to this controller.
    
    :type: sequence supporting index/string lookups and iteration.
    """

    actuators = None
    """A list of actuators linked to this controller.
    
    :type: sequence supporting index/string lookups and iteration.
    """

    useHighPriority = None
    """When set the controller executes always before all other controllers that dont have this set.
    
    :type: boolen
    """


class SCA_ISensor(SCA_ILogicBrick):
    """Base class for all sensor logic bricks."""

    usePosPulseMode = None
    """Flag to turn positive pulse mode on and off.
    
    :type: bool
    """

    useNegPulseMode = None
    """Flag to turn negative pulse mode on and off.
    
    :type: bool
    """

    frequency = None
    """The frequency for pulse mode sensors. (Deprecated: use SCA_ISensor.skippedTicks)
    
    :type: int
    """

    skippedTicks = None
    """Number of logic ticks skipped between 2 active pulses
    
    :type: int
    """

    level = None
    """level Option whether to detect level or edge transition when entering a state.
                                It makes a difference only in case of logic state transition (state actuator).
                                A level detector will immediately generate a pulse, negative or positive
                                depending on the sensor condition, as soon as the state is activated.
                                A edge detector will wait for a state change before generating a pulse.
                                note: mutually exclusive with bge.types.SCA_ISensor.tap, enabling will disable bge.types.SCA_ISensor.tap.
    
    :type: bool
    """

    tap = None
    """When enabled only sensors that are just activated will send a positive event,
                                after this they will be detected as negative by the controllers.
                                This will make a key thats held act as if its only tapped for an instant.
                                note: mutually exclusive with bge.types.SCA_ISensor.level, enabling will disable bge.types.SCA_ISensor.level.
    
    :type: bool
    """

    invert = None
    """Flag to set if this sensor activates on positive or negative events.
    
    :type: bool
    """

    triggered = None
    """True if this sensor brick is in a positive state. (read-only).
    
    :type: bool
    """

    positive = None
    """True if this sensor brick is in a positive state. (read-only).
    
    :type: bool
    """

    pos_ticks = None
    """The number of ticks since the last positive pulse (read-only).
    
    :type: int
    """

    neg_ticks = None
    """The number of ticks since the last negative pulse (read-only).
    
    :type: int
    """

    status = None
    """The status of the sensor (read-only): can be one of bge.logic#sensor-statusthese constants.
    
    :type: int
    """

    def reset(self):
        """Reset sensor internal state, effect depends on the type of sensor and settings.
        The sensor is put in its initial state as if it was just activated.
        """


class BL_ActionActuator(SCA_IActuator):
    """Action Actuators apply an action to an actor."""

    action = ""
    """The name of the action to set as the current action.
    
    :type: str
    """

    frameStart = None
    """Specifies the starting frame of the animation.
    
    :type: float
    """

    frameEnd = None
    """Specifies the ending frame of the animation.
    
    :type: float
    """

    blendIn = None
    """Specifies the number of frames of animation to generate when making transitions between actions.
    
    :type: float
    """

    priority = None
    """Sets the priority of this actuator. Actuators will lower priority numbers will override actuators with higher numbers.
    
    :type: int
    """

    frame = None
    """Sets the current frame for the animation.
    
    :type: float
    """

    propName = ""
    """Sets the property to be used in FromProp playback mode.
    
    :type: str
    """

    blendTime = None
    """Sets the internal frame timer. This property must be in the range from 0.0 to blendIn.
    
    :type: float
    """

    mode = None
    """The operation mode of the actuator. Can be one of bge.logic#action-actuatorthese constants.
    
    :type: int
    """

    useContinue = None
    """The actions continue option, True or False. When True, the action will always play from where last left off,
                                otherwise negative events to this actuator will reset it to its start frame.
    
    :type: bool
    """

    framePropName = ""
    """The name of the property that is set to the current frame number.
    
    :type: str
    """


class BL_ArmatureActuator(SCA_IActuator):
    """Armature Actuators change constraint condition on armatures."""

    type = None
    """The type of action that the actuator executes when it is active.
    Can be one of bge.logic#armatureactuator-constants-typethese constants
    
    :type: int
    """

    constraint = None
    """The constraint object this actuator is controlling.
    (type: bge.types.BL_ArmatureConstraint)
    
    :type: BL_ArmatureConstraint
    """

    target = None
    """The object that this actuator will set as primary target to the constraint it controls.
    (type: bge.types.KX_GameObject)
    
    :type: KX_GameObject
    """

    subtarget = None
    """The object that this actuator will set as secondary target to the constraint it controls.
    (type: bge.types.KX_GameObject.)
    
    :type: KX_GameObject.
    """

    weight = None
    """The weight this actuator will set on the constraint it controls.
    
    :type: float.
    """

    influence = None
    """The influence this actuator will set on the constraint it controls.
    
    :type: float.
    """


class BL_ArmatureObject(KX_GameObject):
    """An armature object."""

    constraints = None
    """The list of armature constraint defined on this armature.
                                Elements of the list can be accessed by index or string.
                                The key format for string access is '<bone_name>:<constraint_name>'.
    (type: list of bge.types.BL_ArmatureConstraint)
    
    :type: list
    """

    channels = None
    """The list of armature channels.
                                Elements of the list can be accessed by index or name the bone.
    (type: list of bge.types.BL_ArmatureChannel)
    
    :type: list
    """

    def update(self):
        """Ensures that the armature will be updated on next graphic frame.
        This action is unecessary if a KX_ArmatureActuator with mode run is active
                                    or if an action is playing. Use this function in other cases. It must be called
                                    on each frame to ensure that the armature is updated continously.
        """


class BL_ShapeActionActuator(SCA_IActuator):
    """ShapeAction Actuators apply an shape action to an mesh object."""

    action = ""
    """The name of the action to set as the current shape action.
    
    :type: str
    """

    frameStart = None
    """Specifies the starting frame of the shape animation.
    
    :type: float
    """

    frameEnd = None
    """Specifies the ending frame of the shape animation.
    
    :type: float
    """

    blendIn = None
    """Specifies the number of frames of animation to generate when making transitions between actions.
    
    :type: float
    """

    priority = None
    """Sets the priority of this actuator. Actuators will lower priority numbers will override actuators with higher numbers.
    
    :type: int
    """

    frame = None
    """Sets the current frame for the animation.
    
    :type: float
    """

    propName = ""
    """Sets the property to be used in FromProp playback mode.
    
    :type: str
    """

    blendTime = None
    """Sets the internal frame timer. This property must be in the range from 0.0 to blendin.
    
    :type: float
    """

    mode = None
    """The operation mode of the actuator. Can be one of these constants.
    
    :type: int
    """

    framePropName = ""
    """The name of the property that is set to the current frame number.
    
    :type: str
    """


class KX_ArmatureSensor(SCA_ISensor):
    """Armature sensor detect conditions on armatures."""

    type = None
    """The type of measurement that the sensor make when it is active.
    Can be one of bge.logic#armaturesensor-typethese constants
    
    :type: integer.
    """

    constraint = None
    """The constraint object this sensor is watching.
    (type: bge.types.BL_ArmatureConstraint)
    
    :type: BL_ArmatureConstraint
    """

    value = None
    """The threshold used in the comparison with the constraint error
                                The linear error is only updated on CopyPose/Distance IK constraint with iTaSC solver
                                The rotation error is only updated on CopyPose+rotation IK constraint with iTaSC solver
                                The linear error on CopyPose is always >= 0: it is the norm of the distance between the target and the bone
                                The rotation error on CopyPose is always >= 0: it is the norm of the equivalent rotation vector between the bone and the target orientations
                                The linear error on Distance can be positive if the distance between the bone and the target is greater than the desired distance, and negative if the distance is smaller.
    
    :type: float
    """


class KX_Camera(KX_GameObject):
    """A Camera object."""

    INSIDE = None
    """See bge.types.KX_Camera.sphereInsideFrustum and bge.types.KX_Camera.boxInsideFrustum"""

    INTERSECT = None
    """See bge.types.KX_Camera.sphereInsideFrustum and bge.types.KX_Camera.boxInsideFrustum"""

    OUTSIDE = None
    """See bge.types.KX_Camera.sphereInsideFrustum and bge.types.KX_Camera.boxInsideFrustum"""

    lens = None
    """The camera's lens value.
    
    :type: float
    """

    fov = None
    """The camera's field of view value.
    
    :type: float
    """

    ortho_scale = None
    """The camera's view scale when in orthographic mode.
    
    :type: float
    """

    near = None
    """The camera's near clip distance.
    
    :type: float
    """

    far = None
    """The camera's far clip distance.
    
    :type: float
    """

    shift_x = None
    """The camera's horizontal shift.
    
    :type: float
    """

    shift_y = None
    """The camera's vertical shift.
    
    :type: float
    """

    perspective = None
    """True if this camera has a perspective transform, False for an orthographic projection.
    
    :type: bool
    """

    frustum_culling = None
    """True if this camera is frustum culling.
    
    :type: bool
    """

    projection_matrix = None
    """This camera's 4x4 projection matrix.
    
    :type: 4x4 Matrix [[float]]
    """

    modelview_matrix = None
    """This camera's 4x4 model view matrix. (read-only).
    
    :type: 4x4 Matrix [[float]]
    """

    camera_to_world = None
    """This camera's camera to world transform. (read-only).
    
    :type: 4x4 Matrix [[float]]
    """

    world_to_camera = None
    """This camera's world to camera transform. (read-only).
    
    :type: 4x4 Matrix [[float]]
    """

    useViewport = None
    """True when the camera is used as a viewport, set True to enable a viewport for this camera.
    
    :type: bool
    """

    def sphereInsideFrustum(self, centre, radius):
        """Tests the given sphere against the view frustum.
        <Note> When the camera is first initialized the result will be invalid because the projection matrix has not been set.
        
        :param centre: The centre of the sphere (in world coordinates.)
            (type: bpy.types.ThemeSpaceListGeneric.list [bge.types.KX_VertexProxy.x, bge.types.KX_VertexProxy.y, bge.types.KX_VertexProxy.z])
        :type centre: bpy.types.ThemeSpaceListGeneric.list [KX_VertexProxy.x, KX_VertexProxy.y, KX_VertexProxy.z]
        :param radius: the radius of the sphere
        :type radius: float
        :return: bge.types.KX_Camera.INSIDE, bge.types.KX_Camera.OUTSIDE or bge.types.KX_Camera.INTERSECT
        :rtype: int
        """

    def boxInsideFrustum(self, box):
        """Tests the given box against the view frustum.
        <Note> When the camera is first initialized the result will be invalid because the projection matrix has not been set.
        
        :param box: Eight (8) corner points of the box (in world coordinates.)
            (type: list of lists)
        :type box: list
        :return: bge.types.KX_Camera.INSIDE, bge.types.KX_Camera.OUTSIDE or bge.types.KX_Camera.INTERSECT
        """

    def pointInsideFrustum(self, point):
        """Tests the given point against the view frustum.
        <Note> When the camera is first initialized the result will be invalid because the projection matrix has not been set.
        
        :param point: The point to test (in world coordinates.)
        :type point: 3D Vector
        :return: True if the given point is inside this camera's viewing frustum.
        :rtype: bool
        """

    def getCameraToWorld(self):
        """Returns the camera-to-world transform.
        
        :return: the camera-to-world transform matrix.
        :rtype: matrix (4x4 list)
        """

    def getWorldToCamera(self):
        """Returns the world-to-camera transform.
        This returns the inverse matrix of getCameraToWorld().
        
        :return: the world-to-camera transform matrix.
        :rtype: matrix (4x4 list)
        """

    def setOnTop(self):
        """Set this cameras viewport ontop of all other viewport."""

    def setViewport(self, left, bottom, right, top):
        """Sets the region of this viewport on the screen in pixels.
        Use bge.render.getWindowHeight and bge.render.getWindowWidth to calculate values relative to the entire display.
        
        :param left: left pixel coordinate of this viewport
        :type left: int
        :param bottom: bottom pixel coordinate of this viewport
        :type bottom: int
        :param right: right pixel coordinate of this viewport
        :type right: int
        :param top: top pixel coordinate of this viewport
        :type top: int
        """

    def getScreenPosition(self, object):
        """Gets the position of an object projected on screen space.
        
        :param object: object name or list [x, y, z]
            (type: bge.types.KX_GameObject or 3D Vector)
        :type object: KX_GameObject or 3D Vector
        :return: the object's position in screen coordinates.
        :rtype: list [x, y]
        """

    def getScreenVect(self, x, y):
        """Gets the vector from the camera position in the screen coordinate direction.
        
        :param x: X Axis
        :type x: float
        :param y: Y Axis
        :type y: float
        :rtype: 3D Vector
        :return: The vector from screen coordinate.
        """

    def getScreenRay(self, x, y, dist=float("inf"), property=None):
        """Look towards a screen coordinate (x, y) and find first object hit within dist that matches prop.
                                    The ray is similar to KX_GameObject->rayCastTo.
        
        :param x: X Axis
        :type x: float
        :param y: Y Axis
        :type y: float
        :param dist: max distance to look (can be negative => look behind); 0 or omitted => detect up to other
        :type dist: float
        :param property: property name that object must have; can be omitted => detect any object
        :type property: str
        :param : (type: bge.types.KX_GameObject)
        :rtype: KX_GameObject
        :return: the first object hit or None if no object or object does not match prop
        """


class KX_CameraActuator(SCA_IActuator):
    """Applies changes to a camera."""

    damping = None
    """strength of of the camera following movement.
    
    :type: float
    """

    axis = None
    """The camera axis (0, 1, 2) for positive XYZ, (3, 4, 5) for negative XYZ.
    
    :type: int
    """

    min = None
    """minimum distance to the target object maintained by the actuator.
    
    :type: float
    """

    max = None
    """maximum distance to stay from the target object.
    
    :type: float
    """

    height = None
    """height to stay above the target object.
    
    :type: float
    """

    object = None
    """the object this actuator tracks.
    (type: bge.types.KX_GameObject or None)
    
    :type: KX_GameObject or None
    """


class KX_ConstraintActuator(SCA_IActuator):
    """A constraint actuator limits the position, rotation, distance or orientation of an object."""

    damp = None
    """Time constant of the constraint expressed in frame (not use by Force field constraint).
    
    :type: int
    """

    rotDamp = None
    """Time constant for the rotation expressed in frame (only for the distance constraint), 0 = use damp for rotation as well.
    
    :type: int
    """

    direction = None
    """The reference direction in world coordinate for the orientation constraint.
    
    :type: 3-tuple of float: (x, y, z)
    """

    option = None
    """Binary combination of bge.logic#constraint-actuator-optionthese constants
    
    :type: int
    """

    time = None
    """activation time of the actuator. The actuator disables itself after this many frame. If set to 0, the actuator is not limited in time.
    
    :type: int
    """

    propName = ""
    """the name of the property or material for the ray detection of the distance constraint.
    
    :type: str
    """

    min = None
    """The lower bound of the constraint. For the rotation and orientation constraint, it represents radiant.
    
    :type: float
    """

    distance = None
    """the target distance of the distance constraint.
    
    :type: float
    """

    max = None
    """the upper bound of the constraint. For rotation and orientation constraints, it represents radiant.
    
    :type: float
    """

    rayLength = None
    """the length of the ray of the distance constraint.
    
    :type: float
    """

    limit = None
    """type of constraint. Use one of the bge.logic#constraint-actuator-limitthese constants
    
    :type: integer.
    """


class KX_FontObject(KX_GameObject):
    """A Font object."""

    text = ""
    """The text displayed by this Font object.
    
    :type: str
    """


class KX_GameActuator(SCA_IActuator):
    """The game actuator loads a new .blend file, restarts the current .blend file or quits the game."""

    fileName = ""
    """the new .blend file to load.
    
    :type: str
    """

    mode = None
    """The mode of this actuator. Can be on of bge.logic#game-actuatorthese constants
    
    :type: Int
    """


class KX_LightObject(KX_GameObject):
    """A Light object."""

    SPOT = None
    """A spot light source. See attribute bge.types.KX_LightObject.type"""

    SUN = None
    """A point light source with no attenuation. See attribute bge.types.KX_LightObject.type"""

    NORMAL = None
    """A point light source. See attribute bge.types.KX_LightObject.type"""

    type = None
    """The type of light - must be SPOT, SUN or NORMAL"""

    layer = None
    """The layer mask that this light affects object on.
    
    :type: bitfield
    """

    energy = None
    """The brightness of this light.
    
    :type: float
    """

    shadowClipStart = None
    """The shadowmap clip start, below which objects will not generate shadows.
    
    :type: float (read only)
    """

    shadowClipEnd = None
    """The shadowmap clip end, beyond which objects will not generate shadows.
    
    :type: float (read only)
    """

    shadowFrustumSize = None
    """Size of the frustum used for creating the shadowmap.
    
    :type: float (read only)
    """

    shadowBindId = None
    """The OpenGL shadow texture bind number/id.
    
    :type: int (read only)
    """

    shadowMapType = None
    """The shadow shadow map type (0 -> Simple; 1 -> Variance)
    
    :type: int (read only)
    """

    shadowBias = None
    """The shadow buffer sampling bias.
    
    :type: float (read only)
    """

    shadowBleedBias = None
    """The bias for reducing light-bleed on variance shadow maps.
    
    :type: float (read only)
    """

    useShadow = None
    """Returns True if the light has Shadow option activated, else returns False.
    
    :type: boolean (read only)
    """

    shadowColor = None
    """The color of this light shadows. Black = (0.0, 0.0, 0.0), White = (1.0, 1.0, 1.0).
    
    :type: mathutils.Color (read only)
    """

    shadowMatrix = None
    """Matrix that converts a vector in camera space to shadow buffer depth space.
    mat4_perspective_to_depth is a fixed matrix defined as follow:
    
    :type: Matrix4x4 (read only)
    """

    distance = None
    """The maximum distance this light can illuminate. (SPOT and NORMAL lights only).
    
    :type: float
    """

    color = None
    """The color of this light. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].
    
    :type: list [r, g, b]
    """

    lin_attenuation = None
    """The linear component of this light's attenuation. (SPOT and NORMAL lights only).
    
    :type: float
    """

    quad_attenuation = None
    """The quadratic component of this light's attenuation (SPOT and NORMAL lights only).
    
    :type: float
    """

    spotsize = None
    """The cone angle of the spot light, in degrees (SPOT lights only).
    (type: float in [0 - 180].)
    
    :type: float
    """

    spotblend = None
    """Specifies the intensity distribution of the spot light (SPOT lights only).
    (type: float in [0 - 1])
    
    :type: float
    """


class KX_MouseActuator(SCA_IActuator):
    """The mouse actuator gives control over the visibility of the mouse cursor and rotates the parent object according to mouse movement."""

    def reset(self):
        """Undoes the rotation caused by the mouse actuator."""

    visible = None
    """The visibility of the mouse cursor.
    
    :type: bool
    """

    use_axis_x = None
    """Mouse movement along the x axis effects object rotation.
    
    :type: bool
    """

    use_axis_y = None
    """Mouse movement along the y axis effects object rotation.
    
    :type: bool
    """

    threshold = None
    """Amount of movement from the mouse required before rotation is triggered.
    The values in the list should be between 0.0 and 0.5.
    
    :type: list (vector of 2 floats)
    """

    reset_x = None
    """Mouse is locked to the center of the screen on the x axis.
    
    :type: bool
    """

    reset_y = None
    """Mouse is locked to the center of the screen on the y axis.
    
    :type: bool
    """

    object_axis = None
    """The object's 3D axis to rotate with the mouse movement. ([x, y])
    * KX_ACT_MOUSE_OBJECT_AXIS_X
    * KX_ACT_MOUSE_OBJECT_AXIS_Y
    * KX_ACT_MOUSE_OBJECT_AXIS_Z
    
    :type: list (vector of 2 integers from 0 to 2)
    """

    local_x = None
    """Rotation caused by mouse movement along the x axis is local.
    
    :type: bool
    """

    local_y = None
    """Rotation caused by mouse movement along the y axis is local.
    
    :type: bool
    """

    sensitivity = None
    """The amount of rotation caused by mouse movement along the x and y axis.
    Negative values invert the rotation.
    
    :type: list (vector of 2 floats)
    """

    limit_x = None
    """The minimum and maximum angle of rotation caused by mouse movement along the x axis in degrees.
                                limit_x[0] is minimum, limit_x[1] is maximum.
    
    :type: list (vector of 2 floats)
    """

    limit_y = None
    """The minimum and maximum angle of rotation caused by mouse movement along the y axis in degrees.
                                limit_y[0] is minimum, limit_y[1] is maximum.
    
    :type: list (vector of 2 floats)
    """

    angle = None
    """The current rotational offset caused by the mouse actuator in degrees.
    
    :type: list (vector of 2 floats)
    """


class KX_NavMeshObject(KX_GameObject):
    """Python interface for using and controlling navigation meshes."""

    def findPath(self, start, goal):
        """Finds the path from start to goal points.
        
        :param start: the start point
        :param start: 3D Vector
        :param goal: the goal point
        :param start: 3D Vector
        :return: a path as a list of points
        :param : (type: list of points)
        :rtype: list
        """

    def raycast(self, start, goal):
        """Raycast from start to goal points.
        
        :param start: the start point
        :param start: 3D Vector
        :param goal: the goal point
        :param start: 3D Vector
        :return: the hit factor
        :rtype: float
        """

    def draw(self, mode):
        """Draws a debug mesh for the navigation mesh.
        
        :param mode: the drawing mode (one of bge.logic#navmesh-draw-modethese constants)
        :param mode: integer
        :return: None
        """

    def rebuild(self):
        """Rebuild the navigation mesh.
        
        :return: None
        """


class KX_NetworkMessageActuator(SCA_IActuator):
    """Message Actuator"""

    propName = ""
    """Messages will only be sent to objects with the given property name.
    
    :type: str
    """

    subject = ""
    """The subject field of the message.
    
    :type: str
    """

    body = ""
    """The body of the message.
    
    :type: str
    """

    usePropBody = None
    """Send a property instead of a regular body message.
    
    :type: bool
    """


class KX_NetworkMessageSensor(SCA_ISensor):
    """The Message Sensor logic brick.
    Currently only loopback (local) networks are supported.
    """

    subject = ""
    """The subject the sensor is looking for.
    
    :type: str
    """

    frameMessageCount = None
    """The number of messages received since the last frame. (read-only).
    
    :type: int
    """

    subjects = None
    """The list of message subjects received. (read-only).
    (type: list of strings)
    
    :type: list
    """

    bodies = None
    """The list of message bodies received. (read-only).
    (type: list of strings)
    
    :type: list
    """


class KX_ObjectActuator(SCA_IActuator):
    """The object actuator ("Motion Actuator") applies force, torque, displacement, angular displacement,
                        velocity, or angular velocity to an object.
                        Servo control allows to regulate force to achieve a certain speed target.
    """

    force = None
    """The force applied by the actuator.
    
    :type: Vector((x, y, z))
    """

    useLocalForce = None
    """A flag specifying if the force is local.
    
    :type: bool
    """

    torque = None
    """The torque applied by the actuator.
    
    :type: Vector((x, y, z))
    """

    useLocalTorque = None
    """A flag specifying if the torque is local.
    
    :type: bool
    """

    dLoc = None
    """The displacement vector applied by the actuator.
    
    :type: Vector((x, y, z))
    """

    useLocalDLoc = None
    """A flag specifying if the dLoc is local.
    
    :type: bool
    """

    dRot = None
    """The angular displacement vector applied by the actuator
    
    :type: Vector((x, y, z))
    """

    useLocalDRot = None
    """A flag specifying if the dRot is local.
    
    :type: bool
    """

    linV = None
    """The linear velocity applied by the actuator.
    
    :type: Vector((x, y, z))
    """

    useLocalLinV = None
    """A flag specifying if the linear velocity is local.
    
    :type: bool
    """

    angV = None
    """The angular velocity applied by the actuator.
    
    :type: Vector((x, y, z))
    """

    useLocalAngV = None
    """A flag specifying if the angular velocity is local.
    
    :type: bool
    """

    damping = None
    """The damping parameter of the servo controller.
    
    :type: short
    """

    forceLimitX = None
    """The min/max force limit along the X axis and activates or deactivates the limits in the servo controller.
    
    :type: list [min(float), max(float), bool]
    """

    forceLimitY = None
    """The min/max force limit along the Y axis and activates or deactivates the limits in the servo controller.
    
    :type: list [min(float), max(float), bool]
    """

    forceLimitZ = None
    """The min/max force limit along the Z axis and activates or deactivates the limits in the servo controller.
    
    :type: list [min(float), max(float), bool]
    """

    pid = None
    """The PID coefficients of the servo controller.
    (type: list of floats [proportional, integral, derivate])
    
    :type: list
    """

    reference = None
    """The object that is used as reference to compute the velocity for the servo controller.
    (type: bge.types.KX_GameObject or None)
    
    :type: KX_GameObject or None
    """


class KX_ParentActuator(SCA_IActuator):
    """The parent actuator can set or remove an objects parent object."""

    object = None
    """the object this actuator sets the parent too.
    (type: bge.types.KX_GameObject or None)
    
    :type: KX_GameObject or None
    """

    mode = None
    """The mode of this actuator.
    
    :type: integer from 0 to 1.
    """

    compound = None
    """Whether the object shape should be added to the parent compound shape when parenting.
    Effective only if the parent is already a compound shape.
    
    :type: bool
    """

    ghost = None
    """Whether the object should be made ghost when parenting
                                Effective only if the shape is not added to the parent compound shape.
    
    :type: bool
    """


class KX_RaySensor(SCA_ISensor):
    """A ray sensor detects the first object in a given direction."""

    propName = ""
    """The property the ray is looking for.
    
    :type: str
    """

    range = None
    """The distance of the ray.
    
    :type: float
    """

    useMaterial = None
    """Whether or not to look for a material (false = property).
    
    :type: bool
    """

    useXRay = None
    """Whether or not to use XRay.
    
    :type: bool
    """

    hitObject = None
    """The game object that was hit by the ray. (read-only).
    (type: bge.types.KX_GameObject)
    
    :type: KX_GameObject
    """

    hitPosition = None
    """The position (in worldcoordinates) where the object was hit by the ray. (read-only).
    
    :type: list [x, y, z]
    """

    hitNormal = None
    """The normal (in worldcoordinates) of the object at the location where the object was hit by the ray. (read-only).
    
    :type: list [x, y, z]
    """

    hitMaterial = ""
    """The material of the object in the face hit by the ray. (read-only).
    
    :type: str
    """

    rayDirection = None
    """The direction from the ray (in worldcoordinates). (read-only).
    
    :type: list [x, y, z]
    """

    axis = None
    """The axis the ray is pointing on.
    * KX_RAY_AXIS_POS_X
    * KX_RAY_AXIS_POS_Y
    * KX_RAY_AXIS_POS_Z
    * KX_RAY_AXIS_NEG_X
    * KX_RAY_AXIS_NEG_Y
    * KX_RAY_AXIS_NEG_Z
    
    :type: integer from 0 to 5
    """


class KX_SCA_AddObjectActuator(SCA_IActuator):
    """Edit Object Actuator (in Add Object Mode)"""

    object = None
    """the object this actuator adds.
    (type: bge.types.KX_GameObject or None)
    
    :type: KX_GameObject or None
    """

    objectLastCreated = None
    """the last added object from this actuator (read-only).
    (type: bge.types.KX_GameObject or None)
    
    :type: KX_GameObject or None
    """

    time = None
    """the lifetime of added objects, in frames. Set to 0 to disable automatic deletion.
    
    :type: int
    """

    linearVelocity = None
    """the initial linear velocity of added objects.
    
    :type: list [vx, vy, vz]
    """

    angularVelocity = None
    """the initial angular velocity of added objects.
    
    :type: list [vx, vy, vz]
    """

    def instantAddObject(self):
        """adds the object without needing to calling SCA_PythonController.activate()
        <Note> Use objectLastCreated to get the newly created object.
        """


class KX_SCA_DynamicActuator(SCA_IActuator):
    """Dynamic Actuator."""

    mode = None
    """the type of operation of the actuator, 0-4
    * KX_DYN_RESTORE_DYNAMICS(0)
    * KX_DYN_DISABLE_DYNAMICS(1)
    * KX_DYN_ENABLE_RIGID_BODY(2)
    * KX_DYN_DISABLE_RIGID_BODY(3)
    * KX_DYN_SET_MASS(4)
    
    :type: int
    """

    mass = None
    """the mass value for the KX_DYN_SET_MASS operation.
    
    :type: float
    """


class KX_SCA_EndObjectActuator(SCA_IActuator):
    """Edit Object Actuator (in End Object mode)
    This actuator has no python methods.
    """


class KX_SCA_ReplaceMeshActuator(SCA_IActuator):
    """Edit Object actuator, in Replace Mesh mode."""

    mesh = None
    """MeshProxy or the name of the mesh that will replace the current one.
    Set to None to disable actuator.
    
    :type: MeshProxy or None if no mesh is set
    """

    useDisplayMesh = None
    """when true the displayed mesh is replaced.
    
    :type: bool
    """

    usePhysicsMesh = None
    """when true the physics mesh is replaced.
    
    :type: bool
    """

    def instantReplaceMesh(self):
        """Immediately replace mesh without delay."""


class KX_SceneActuator(SCA_IActuator):
    """Scene Actuator logic brick."""

    scene = ""
    """the name of the scene to change to/overlay/underlay/remove/suspend/resume.
    
    :type: str
    """

    camera = None
    """the camera to change to.
    (type: bge.types.KX_Camera on read, string or bge.types.KX_Camera on write)
    
    :type: KX_Camera on read, string or KX_Camera on write
    """

    useRestart = None
    """Set flag to True to restart the sene.
    
    :type: bool
    """

    mode = None
    """The mode of the actuator.
    
    :type: integer from 0 to 5.
    """


class KX_SoundActuator(SCA_IActuator):
    """Sound Actuator.
    The bge.types.KX_SoundActuator.startSound, bge.types.KX_SoundActuator.pauseSound and bge.types.KX_SoundActuator.stopSound do not require the actuator to be activated - they act instantly provided that the actuator has been activated once at least.
    """

    volume = None
    """The volume (gain) of the sound.
    
    :type: float
    """

    time = None
    """The current position in the audio stream (in seconds).
    
    :type: float
    """

    pitch = None
    """The pitch of the sound.
    
    :type: float
    """

    mode = None
    """The operation mode of the actuator. Can be one of bge.logic#logic-sound-actuatorthese constants
    
    :type: int
    """

    sound = None
    """The sound the actuator should play.
    
    :type: Audaspace factory
    """

    is3D = None
    """Whether or not the actuator should be using 3D sound. (read-only)
    
    :type: bool
    """

    volume_maximum = None
    """The maximum gain of the sound, no matter how near it is.
    
    :type: float
    """

    volume_minimum = None
    """The minimum gain of the sound, no matter how far it is away.
    
    :type: float
    """

    distance_reference = None
    """The distance where the sound has a gain of 1.0.
    
    :type: float
    """

    distance_maximum = None
    """The maximum distance at which you can hear the sound.
    
    :type: float
    """

    attenuation = None
    """The influence factor on volume depending on distance.
    
    :type: float
    """

    cone_angle_inner = None
    """The angle of the inner cone.
    
    :type: float
    """

    cone_angle_outer = None
    """The angle of the outer cone.
    
    :type: float
    """

    cone_volume_outer = None
    """The gain outside the outer cone (the gain in the outer cone will be interpolated between this value and the normal gain in the inner cone).
    
    :type: float
    """

    def startSound(self):
        """Starts the sound.
        
        :return: None
        """

    def pauseSound(self):
        """Pauses the sound.
        
        :return: None
        """

    def stopSound(self):
        """Stops the sound.
        
        :return: None
        """


class KX_StateActuator(SCA_IActuator):
    """State actuator changes the state mask of parent object."""

    operation = None
    """Type of bit operation to be applied on object state mask.
    You can use one of bge.logic#state-actuator-operationthese constants
    
    :type: int
    """

    mask = None
    """Value that defines the bits that will be modified by the operation.
    The bits that are 1 in the mask will be updated in the object state.
    The bits that are 0 are will be left unmodified expect for the Copy operation which copies the mask to the object state.
    
    :type: int
    """


class KX_SteeringActuator(SCA_IActuator):
    """Steering Actuator for navigation."""

    behavior = None
    """The steering behavior to use.
    (type: one of bge.logic#logic-steering-actuatorthese constants)
    
    :type: one
    """

    velocity = None
    """Velocity magnitude
    
    :type: float
    """

    acceleration = None
    """Max acceleration
    
    :type: float
    """

    turnspeed = None
    """Max turn speed
    
    :type: float
    """

    distance = None
    """Relax distance
    
    :type: float
    """

    target = None
    """Target object
    (type: bge.types.KX_GameObject)
    
    :type: KX_GameObject
    """

    navmesh = None
    """Navigation mesh
    (type: bge.types.KX_GameObject)
    
    :type: KX_GameObject
    """

    selfterminated = None
    """Terminate when target is reached
    
    :type: bool
    """

    enableVisualization = None
    """Enable debug visualization
    
    :type: bool
    """

    pathUpdatePeriod = None
    """Path update period
    
    :type: int
    """


class KX_TouchSensor(SCA_ISensor):
    """Touch sensor detects collisions between objects."""

    propName = ""
    """The property or material to collide with.
    
    :type: str
    """

    useMaterial = None
    """Determines if the sensor is looking for a property or material. KX_True = Find material; KX_False = Find property.
    
    :type: bool
    """

    usePulseCollision = None
    """When enabled, changes to the set of colliding objects generate a pulse.
    
    :type: bool
    """

    hitObject = None
    """The last collided object. (read-only).
    (type: bge.types.KX_GameObject or None)
    
    :type: KX_GameObject or None
    """

    hitObjectList = None
    """A list of colliding objects. (read-only).
    (type: bge.types.CListValue of bge.types.KX_GameObject)
    
    :type: CListValue
    """

    hitMaterial = ""
    """The material of the object in the face hit by the ray. (read-only).
    
    :type: str
    """


class KX_TrackToActuator(SCA_IActuator):
    """Edit Object actuator in Track To mode."""

    object = None
    """the object this actuator tracks.
    (type: bge.types.KX_GameObject or None)
    
    :type: KX_GameObject or None
    """

    time = None
    """the time in frames with which to delay the tracking motion.
    
    :type: int
    """

    use3D = None
    """the tracking motion to use 3D.
    
    :type: bool
    """

    upAxis = None
    """The axis that points upward.
    * KX_TRACK_UPAXIS_POS_X
    * KX_TRACK_UPAXIS_POS_Y
    * KX_TRACK_UPAXIS_POS_Z
    
    :type: integer from 0 to 2
    """

    trackAxis = None
    """The axis that points to the target object.
    * KX_TRACK_TRAXIS_POS_X
    * KX_TRACK_TRAXIS_POS_Y
    * KX_TRACK_TRAXIS_POS_Z
    * KX_TRACK_TRAXIS_NEG_X
    * KX_TRACK_TRAXIS_NEG_Y
    * KX_TRACK_TRAXIS_NEG_Z
    
    :type: integer from 0 to 5
    """


class KX_VisibilityActuator(SCA_IActuator):
    """Visibility Actuator."""

    visibility = None
    """whether the actuator makes its parent object visible or invisible.
    
    :type: bool
    """

    useOcclusion = None
    """whether the actuator makes its parent object an occluder or not.
    
    :type: bool
    """

    useRecursion = None
    """whether the visibility/occlusion should be propagated to all children of the object.
    
    :type: bool
    """


class SCA_2DFilterActuator(SCA_IActuator):
    """Create, enable and disable 2D filters.
    The following properties don't have an immediate effect.
                        You must active the actuator to get the result.
                        The actuator is not persistent: it automatically stops itself after setting up the filter
                        but the filter remains active. To stop a filter you must activate the actuator with 'type'
                        set to bge.logic.RAS_2DFILTER_DISABLED or bge.logic.RAS_2DFILTER_NOFILTER.
    """

    shaderText = ""
    """shader source code for custom shader.
    
    :type: str
    """

    disableMotionBlur = None
    """action on motion blur: 0=enable, 1=disable.
    
    :type: int
    """

    mode = None
    """Type of 2D filter, use one of bge.logic#two-d-filteractuator-modethese constants.
    
    :type: int
    """

    passNumber = None
    """order number of filter in the stack of 2D filters. Filters are executed in increasing order of passNb.
    Only be one filter can be defined per passNb.
    
    :type: integer (0-100)
    """

    value = None
    """argument for motion blur filter.
    
    :type: float (0.0-100.0)
    """


class SCA_ANDController(SCA_IController):
    """An AND controller activates only when all linked sensors are activated.
    There are no special python methods for this controller.
    """


class SCA_ActuatorSensor(SCA_ISensor):
    """Actuator sensor detect change in actuator state of the parent object.
                        It generates a positive pulse if the corresponding actuator is activated
                        and a negative pulse if the actuator is deactivated.
    """

    actuator = ""
    """the name of the actuator that the sensor is monitoring.
    
    :type: str
    """


class SCA_AlwaysSensor(SCA_ISensor):
    """This sensor is always activated."""


class SCA_DelaySensor(SCA_ISensor):
    """The Delay sensor generates positive and negative triggers at precise time,
                        expressed in number of frames. The delay parameter defines the length of the initial OFF period. A positive trigger is generated at the end of this period.
    The duration parameter defines the length of the ON period following the OFF period.
                        There is a negative trigger at the end of the ON period. If duration is 0, the sensor stays ON and there is no negative trigger.
    The sensor runs the OFF-ON cycle once unless the repeat option is set: the OFF-ON cycle repeats indefinately (or the OFF cycle if duration is 0).
    Use bge.types.SCA_ISensor.reset at any time to restart sensor.
    """

    delay = None
    """length of the initial OFF period as number of frame, 0 for immediate trigger.
    
    :type: integer.
    """

    duration = None
    """length of the ON period in number of frame after the initial OFF period.
    If duration is greater than 0, a negative trigger is sent at the end of the ON pulse.
    
    :type: int
    """

    repeat = None
    """1 if the OFF-ON cycle should be repeated indefinately, 0 if it should run once.
    
    :type: int
    """


class SCA_JoystickSensor(SCA_ISensor):
    """This sensor detects player joystick events."""

    axisValues = None
    """The state of the joysticks axis as a list of values bge.types.SCA_JoystickSensor.numAxis long. (read-only).
    Each specifying the value of an axis between -32767 and 32767 depending on how far the axis is pushed, 0 for nothing.
                                The first 2 values are used by most joysticks and gamepads for directional control. 3rd and 4th values are only on some joysticks and can be used for arbitary controls.
    * left:[-32767, 0, ...]
    * right:[32767, 0, ...]
    * up:[0, -32767, ...]
    * down:[0, 32767, ...]
    (type: list of ints.)
    
    :type: list
    """

    axisSingle = None
    """like bge.types.SCA_JoystickSensor.axisValues but returns a single axis value that is set by the sensor. (read-only).
    
    :type: int
    """

    hatValues = None
    """The state of the joysticks hats as a list of values bge.types.SCA_JoystickSensor.numHats long. (read-only).
    Each specifying the direction of the hat from 1 to 12, 0 when inactive.
    Hat directions are as follows...
    * 0:None
    * 1:Up
    * 2:Right
    * 4:Down
    * 8:Left
    * 3:Up - Right
    * 6:Down - Right
    * 12:Down - Left
    * 9:Up - Left
    (type: list of ints)
    
    :type: list
    """

    hatSingle = None
    """Like bge.types.SCA_JoystickSensor.hatValues but returns a single hat direction value that is set by the sensor. (read-only).
    
    :type: int
    """

    numAxis = None
    """The number of axes for the joystick at this index. (read-only).
    
    :type: int
    """

    numButtons = None
    """The number of buttons for the joystick at this index. (read-only).
    
    :type: int
    """

    numHats = None
    """The number of hats for the joystick at this index. (read-only).
    
    :type: int
    """

    connected = None
    """True if a joystick is connected at this joysticks index. (read-only).
    
    :type: bool
    """

    index = None
    """The joystick index to use (from 0 to 7). The first joystick is always 0.
    
    :type: int
    """

    threshold = None
    """Axis threshold. Joystick axis motion below this threshold wont trigger an event. Use values between (0 and 32767), lower values are more sensitive.
    
    :type: int
    """

    button = None
    """The button index the sensor reacts to (first button = 0). When the "All Events" toggle is set, this option has no effect.
    
    :type: int
    """

    axis = None
    """The axis this sensor reacts to, as a list of two values [axisIndex, axisDirection]
    * axisIndex: the axis index to use when detecting axis movement, 1=primary directional control, 2=secondary directional control.
    * axisDirection: 0=right, 1=up, 2=left, 3=down.
    
    :type: [integer, integer]
    """

    hat = None
    """The hat the sensor reacts to, as a list of two values: [hatIndex, hatDirection]
    * hatIndex: the hat index to use when detecting hat movement, 1=primary hat, 2=secondary hat (4 max).
    * hatDirection: 1-12.
    
    :type: [integer, integer]
    """

    def getButtonActiveList(self):
        """
        :return: A list containing the indicies of the currently pressed buttons.
        :rtype: list
        """

    def getButtonStatus(self, buttonIndex):
        """
        :param buttonIndex: the button index, 0=first button
        :type buttonIndex: int
        :return: The current pressed state of the specified button.
        :rtype: bool
        """


class SCA_KeyboardSensor(SCA_ISensor):
    """A keyboard sensor detects player key presses.
    See module bge.events for keycode values.
    """

    key = None
    """The key code this sensor is looking for.
    
    :type: keycode from bge.events module
    """

    hold1 = None
    """The key code for the first modifier this sensor is looking for.
    
    :type: keycode from bge.events module
    """

    hold2 = None
    """The key code for the second modifier this sensor is looking for.
    
    :type: keycode from bge.events module
    """

    toggleProperty = ""
    """The name of the property that indicates whether or not to log keystrokes as a string.
    
    :type: str
    """

    targetProperty = ""
    """The name of the property that receives keystrokes in case in case a string is logged.
    
    :type: str
    """

    useAllKeys = None
    """Flag to determine whether or not to accept all keys.
    
    :type: bool
    """

    events = None
    """a list of pressed keys that have either been pressed, or just released, or are active this frame. (read-only).
    
    :type: list [[bge.events#keyboard-keyskeycode, bge.logic#input-statusstatus], ...]
    """

    def getKeyStatus(self, keycode):
        """Get the status of a key.
        
        :param keycode: The code that represents the key you want to get the state of, use one of bge.events#keyboard-keysthese constants
        :type keycode: int
        :return: The state of the given key, can be one of bge.logic#input-statusthese constants
        :rtype: int
        """


class SCA_MouseSensor(SCA_ISensor):
    """Mouse Sensor logic brick."""

    position = None
    """current [x, y] coordinates of the mouse, in frame coordinates (pixels).
    
    :type: [integer, interger]
    """

    mode = None
    """sensor mode.
    
    :type: integer
        * KX_MOUSESENSORMODE_LEFTBUTTON(1)
        * KX_MOUSESENSORMODE_MIDDLEBUTTON(2)
        * KX_MOUSESENSORMODE_RIGHTBUTTON(3)
        * KX_MOUSESENSORMODE_WHEELUP(4)
        * KX_MOUSESENSORMODE_WHEELDOWN(5)
        * KX_MOUSESENSORMODE_MOVEMENT(6)
    """

    def getButtonStatus(self, button):
        """Get the mouse button status.
        
        :param button: The code that represents the key you want to get the state of, use one of bge.events#mouse-keysthese constants
        :type button: int
        :return: The state of the given key, can be one of bge.logic#input-statusthese constants
        :rtype: int
        """


class SCA_NANDController(SCA_IController):
    """An NAND controller activates when all linked sensors are not active.
    There are no special python methods for this controller.
    """


class SCA_NORController(SCA_IController):
    """An NOR controller activates only when all linked sensors are de-activated.
    There are no special python methods for this controller.
    """


class SCA_ORController(SCA_IController):
    """An OR controller activates when any connected sensor activates.
    There are no special python methods for this controller.
    """


class SCA_PropertyActuator(SCA_IActuator):
    """Property Actuator"""

    propName = ""
    """the property on which to operate.
    
    :type: str
    """

    value = ""
    """the value with which the actuator operates.
    
    :type: str
    """

    mode = None
    """TODO - add constants to game logic dict!.
    
    :type: int
    """


class SCA_PropertySensor(SCA_ISensor):
    """Activates when the game object property matches."""

    mode = None
    """Type of check on the property. Can be one of bge.logic#logic-property-sensorthese constants
    
    :type: integer.
    """

    propName = ""
    """the property the sensor operates.
    
    :type: str
    """

    value = ""
    """the value with which the sensor compares to the value of the property.
    
    :type: str
    """

    min = ""
    """the minimum value of the range used to evaluate the property when in interval mode.
    
    :type: str
    """

    max = ""
    """the maximum value of the range used to evaluate the property when in interval mode.
    
    :type: str
    """


class SCA_PythonController(SCA_IController):
    """A Python controller uses a Python script to activate it's actuators,
                        based on it's sensors.
    """

    owner = None
    """The object the controller is attached to.
    (type: bge.types.KX_GameObject)
    
    :type: KX_GameObject
    """

    script = ""
    """The value of this variable depends on the execution methid.
    * When 'Script' execution mode is set this value contains the entire python script as a single string (not the script name as you might expect) which can be modified to run different scripts.
    * When 'Module' execution mode is set this value will contain a single line string - module name and function "module.func" or "package.modile.func" where the module names are python textblocks or external scripts.
    
    :type: str
    """

    mode = None
    """the execution mode for this controller (read-only).
    * Script: 0, Execite the bge.types.SCA_PythonController.script as a python code.
    * Module: 1, Execite the bge.types.SCA_PythonController.script as a module and function.
    
    :type: int
    """

    def activate(self, actuator):
        """Activates an actuator attached to this controller.
        
        :param actuator: The actuator to operate on.
            (type: bge.types.SCA_ActuatorSensor.actuator or the actuator name as a string)
        :type actuator: SCA_ActuatorSensor.actuator or the actuator name as a string
        """

    def deactivate(self, actuator):
        """Deactivates an actuator attached to this controller.
        
        :param actuator: The actuator to operate on.
            (type: bge.types.SCA_ActuatorSensor.actuator or the actuator name as a string)
        :type actuator: SCA_ActuatorSensor.actuator or the actuator name as a string
        """


class SCA_RandomActuator(SCA_IActuator):
    """Random Actuator"""

    seed = None
    """Seed of the random number generator.
    Equal seeds produce equal series. If the seed is 0, the generator will produce the same value on every call.
    
    :type: integer.
    """

    para1 = None
    """the first parameter of the active distribution.
    Refer to the documentation of the generator types for the meaning of this value.
    
    :type: float, read-only.
    """

    para2 = None
    """the second parameter of the active distribution.
    Refer to the documentation of the generator types for the meaning of this value.
    
    :type: float, read-only
    """

    distribution = None
    """Distribution type. (read-only). Can be one of bge.logic#logic-random-distributionsthese constants
    
    :type: int
    """

    propName = ""
    """the name of the property to set with the random value.
    If the generator and property types do not match, the assignment is ignored.
    
    :type: str
    """

    def setBoolConst(self, value):
        """Sets this generator to produce a constant boolean value.
        
        :param value: The value to return.
        :type value: bool
        """

    def setBoolUniform(self):
        """Sets this generator to produce a uniform boolean distribution.
        The generator will generate True or False with 50% chance.
        """

    def setBoolBernouilli(self, value):
        """Sets this generator to produce a Bernouilli distribution.
        
        :param value: Specifies the proportion of False values to produce.
            * 0.0: Always generate True
            * 1.0: Always generate False
        :type value: float
        """

    def setIntConst(self, value):
        """Sets this generator to always produce the given value.
        
        :param value: the value this generator produces.
        :type value: int
        """

    def setIntUniform(self, lower_bound, upper_bound):
        """Sets this generator to produce a random value between the given lower and
                                    upper bounds (inclusive).
        """

    def setIntPoisson(self, value):
        """Generate a Poisson-distributed number.
        This performs a series of Bernouilli tests with parameter value.
                                    It returns the number of tries needed to achieve succes.
        """

    def setFloatConst(self, value):
        """Always generate the given value."""

    def setFloatUniform(self, lower_bound, upper_bound):
        """Generates a random float between lower_bound and upper_bound with a
                                    uniform distribution.
        """

    def setFloatNormal(self, mean, standard_deviation):
        """Generates a random float from the given normal distribution.
        
        :param mean: The mean (average) value of the generated numbers
        :type mean: float
        :param standard_deviation: The standard deviation of the generated numbers.
        :type standard_deviation: float
        """

    def setFloatNegativeExponential(self, half_life):
        """Generate negative-exponentially distributed numbers.
        The half-life 'time' is characterized by half_life.
        """


class SCA_RandomSensor(SCA_ISensor):
    """This sensor activates randomly."""

    lastDraw = None
    """The seed of the random number generator.
    
    :type: int
    """

    seed = None
    """The seed of the random number generator.
    
    :type: int
    """


class SCA_XNORController(SCA_IController):
    """An XNOR controller activates when all linked sensors are the same (activated or inative).
    There are no special python methods for this controller.
    """


class SCA_XORController(SCA_IController):
    """An XOR controller activates when there is the input is mixed, but not when all are on or off.
    There are no special python methods for this controller.
    """


class KX_MouseFocusSensor(SCA_MouseSensor):
    """The mouse focus sensor detects when the mouse is over the current game object.
    The mouse focus sensor works by transforming the mouse coordinates from 2d device
                        space to 3d space then raycasting away from the camera.
    """

    raySource = None
    """The worldspace source of the ray (the view position).
    
    :type: list (vector of 3 floats)
    """

    rayTarget = None
    """The worldspace target of the ray.
    
    :type: list (vector of 3 floats)
    """

    rayDirection = None
    """The bge.types.KX_MouseFocusSensor.rayTarget - bge.types.KX_MouseFocusSensor.raySource normalized.
    
    :type: list (normalized vector of 3 floats)
    """

    hitObject = None
    """the last object the mouse was over.
    (type: bge.types.KX_GameObject or None)
    
    :type: KX_GameObject or None
    """

    hitPosition = None
    """The worldspace position of the ray intersecton.
    
    :type: list (vector of 3 floats)
    """

    hitNormal = None
    """the worldspace normal from the face at point of intersection.
    
    :type: list (normalized vector of 3 floats)
    """

    hitUV = None
    """the UV coordinates at the point of intersection.
    If the object has no UV mapping, it returns [0, 0].
    The UV coordinates are not normalized, they can be < 0 or > 1 depending on the UV mapping.
    
    :type: list (vector of 2 floats)
    """

    usePulseFocus = None
    """When enabled, moving the mouse over a different object generates a pulse. (only used when the 'Mouse Over Any' sensor option is set).
    
    :type: bool
    """

    useXRay = None
    """:type: bool"""

    propName = ""
    """:type: str"""

    useMaterial = None
    """:type: bool"""


class KX_NearSensor(KX_TouchSensor):
    """A near sensor is a specialised form of touch sensor."""

    distance = None
    """The near sensor activates when an object is within this distance.
    
    :type: float
    """

    resetDistance = None
    """The near sensor deactivates when the object exceeds this distance.
    
    :type: float
    """


class KX_RadarSensor(KX_NearSensor):
    """Radar sensor is a near sensor with a conical sensor object."""

    coneOrigin = None
    """The origin of the cone with which to test. The origin is in the middle of the cone. (read-only).
    (type: list of floats [x, y, z])
    
    :type: list
    """

    coneTarget = None
    """The center of the bottom face of the cone with which to test. (read-only).
    (type: list of floats [x, y, z])
    
    :type: list
    """

    distance = None
    """The height of the cone with which to test.
    
    :type: float
    """

    angle = None
    """The angle of the cone (in degrees) with which to test.
    
    :type: float
    """

    axis = None
    """The axis on which the radar cone is cast.
    KX_RADAR_AXIS_POS_X, KX_RADAR_AXIS_POS_Y, KX_RADAR_AXIS_POS_Z,
                                KX_RADAR_AXIS_NEG_X, KX_RADAR_AXIS_NEG_Y, KX_RADAR_AXIS_NEG_Z
    
    :type: integer from 0 to 5
    """
