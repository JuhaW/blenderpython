def createConstraint(physicsid_1, physicsid_2, constraint_type, pivot_x=0.0, pivot_y=0.0, pivot_z=0.0, axis_x=0.0, axis_y=0.0, axis_z=0.0, flag=0):
    """Creates a constraint.
    
    :param physicsid_1: The physics id of the first object in constraint.
    :type physicsid_1: int
    :param physicsid_2: The physics id of the second object in constraint.
    :type physicsid_2: int
    :param constraint_type: The type of the constraint, see Create Constraint Constants.
    :type constraint_type: int
    :param pivot_x: Pivot X position. (optional)
    :type pivot_x: float
    :param pivot_y: Pivot Y position. (optional)
    :type pivot_y: float
    :param pivot_z: Pivot Z position. (optional)
    :type pivot_z: float
    :param axis_x: X axis angle in degrees. (optional)
    :type axis_x: float
    :param axis_y: Y axis angle in degrees. (optional)
    :type axis_y: float
    :param axis_z: Z axis angle in degrees. (optional)
    :type axis_z: float
    :param flag: 128 to disable collision between linked bodies. (optional)
    :type flag: int
    :return: A constraint wrapper.
    :rtype: bge.types.KX_ConstraintWrapper
    """


def exportBulletFile(filename):
    """Exports a file representing the dynamics world (usually using .bullet extension).
    See Bullet binary serialization.
    
    :param filename: File path.
    :type filename: str
    """


def getAppliedImpulse(constraintId):
    """
    :param constraintId: The id of the constraint.
    :type constraintId: int
    :return: The most recent applied impulse.
    :rtype: float
    """


def getVehicleConstraint(constraintId):
    """
    :param constraintId: The id of the vehicle constraint.
    :type constraintId: int
    :return: A vehicle constraint object.
    :rtype: bge.types.KX_VehicleWrapper
    """


def getCharacter(gameobj):
    """
    :param gameobj: The game object with the character physics.
    :type gameobj: bge.types.KX_GameObject
    :return: Character wrapper.
    :rtype: bge.types.KX_CharacterWrapper
    """


def removeConstraint(constraintId):
    """Removes a constraint.
    
    :param constraintId: The id of the constraint to be removed.
    :type constraintId: int
    """


def setCcdMode(ccdMode):
    """<Note> Very experimental, not recommended
    Sets the CCD (Continous Colision Detection) mode in the Physics Environment.
    
    :param ccdMode: The new CCD mode.
    :type ccdMode: int
    """


def setContactBreakingTreshold(breakingTreshold):
    """<Note> Reasonable default is 0.02 (if units are meters)
    Sets tresholds to do with contact point management.
    
    :param breakingTreshold: The new contact breaking treshold.
    :type breakingTreshold: float
    """


def setDeactivationAngularTreshold(angularTreshold):
    """Sets the angular velocity treshold.
    
    :param angularTreshold: New deactivation angular treshold.
    :type angularTreshold: float
    """


def setDeactivationLinearTreshold(linearTreshold):
    """Sets the linear velocity treshold.
    
    :param linearTreshold: New deactivation linear treshold.
    :type linearTreshold: float
    """


def setDeactivationTime(time):
    """Sets the time after which a resting rigidbody gets deactived.
    
    :param time: The deactivation time.
    :type time: float
    """


def setDebugMode(mode):
    """Sets the debug mode.
    
    :param mode: The new debug mode, see Debug Mode Constants.
    :type mode: int
    """


def setGravity(x, y, z):
    """Sets the gravity force.
    
    :param x: Gravity X force.
    :type x: float
    :param y: Gravity Y force.
    :type y: float
    :param z: Gravity Z force.
    :type z: float
    """


def setLinearAirDamping(damping):
    """<Note> Not implemented
    Sets the linear air damping for rigidbodies.
    """


def setNumIterations(numiter):
    """Sets the number of iterations for an iterative constraint solver.
    
    :param numiter: New number of iterations.
    :type numiter: int
    """


def setNumTimeSubSteps(numsubstep):
    """Sets the number of substeps for each physics proceed. Tradeoff quality for performance.
    
    :param numsubstep: New number of substeps.
    :type numsubstep: int
    """


def setSolverDamping(damping):
    """<Note> Very experimental, not recommended
    Sets the damper constant of a penalty based solver.
    
    :param damping: New damping for the solver.
    :type damping: float
    """


def setSolverTau(tau):
    """<Note> Very experimental, not recommended
    Sets the spring constant of a penalty based solver.
    
    :param tau: New tau for the solver.
    :type tau: float
    """


def setSolverType(solverType):
    """<Note> Very experimental, not recommended
    Sets the solver type.
    
    :param solverType: The new type of the solver.
    :type solverType: int
    """


def setSorConstant(sor):
    """<Note> Very experimental, not recommended
    Sets the successive overrelaxation constant.
    
    :param sor: New sor value.
    :type sor: float
    """


def setUseEpa(epa):
    """<Note> Not implemented"""


error = ""
"""Symbolic constant string that indicates error.

:type: str
"""

DBG_NODEBUG = None
"""No debug."""

DBG_DRAWWIREFRAME = None
"""Draw wireframe in debug."""

DBG_DRAWAABB = None
"""Draw Axis Aligned Bounding Box in debug."""

DBG_DRAWFREATURESTEXT = None
"""Draw features text in debug."""

DBG_DRAWCONTACTPOINTS = None
"""Draw contact points in debug."""

DBG_NOHELPTEXT = None
"""Debug without help text."""

DBG_DRAWTEXT = None
"""Draw text in debug."""

DBG_PROFILETIMINGS = None
"""Draw profile timings in debug."""

DBG_ENABLESATCOMPARISION = None
"""Enable sat comparision in debug."""

DBG_DISABLEBULLETLCP = None
"""Disable Bullet LCP."""

DBG_ENABLECCD = None
"""Enable Continous Collision Detection in debug."""

DBG_DRAWCONSTRAINTS = None
"""Draw constraints in debug."""

DBG_DRAWCONSTRAINTLIMITS = None
"""Draw constraint limits in debug."""

DBG_FASTWIREFRAME = None
"""Draw a fast wireframe in debug."""

POINTTOPOINT_CONSTRAINT = None

LINEHINGE_CONSTRAINT = None

ANGULAR_CONSTRAINT = None

CONETWIST_CONSTRAINT = None

VEHICLE_CONSTRAINT = None

GENERIC_6DOF_CONSTRAINT = None
