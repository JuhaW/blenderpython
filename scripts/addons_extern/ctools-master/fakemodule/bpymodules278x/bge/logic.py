globalDict = None
"""A dictionary that is saved between loading blend files so you can use it to store inventory and other variables you want to store between scenes and blend files.
                        It can also be written to a file and loaded later on with the game load/save actuators.
"""

keyboard = None
"""The current keyboard wrapped in an bge.types.SCA_PythonKeyboard object."""

mouse = None
"""The current mouse wrapped in an bge.types.SCA_PythonMouse object."""

joysticks = None
"""A list of attached bge.types.SCA_PythonJoystick.
                        The list size is the maximum number of supported joysticks.
                        If no joystick is available for a given slot, the slot is set to None.
"""


def getCurrentController():
    """Gets the Python controller associated with this Python script.
    
    :rtype: bge.types.SCA_PythonController
    """


def getCurrentScene():
    """Gets the current Scene.
    
    :rtype: bge.types.KX_Scene
    """


def getSceneList():
    """Gets a list of the current scenes loaded in the game engine.
    <Note> Scenes in your blend file that have not been converted wont be in this list. This list will only contain scenes such as overlays scenes.
    
    :param : (type: list of bge.types.KX_Scene)
    :rtype: list
    """


def loadGlobalDict():
    """Loads bge.logic.globalDict from a file."""


def saveGlobalDict():
    """Saves bge.logic.globalDict to a file."""


def startGame(blend):
    """Loads the blend file.
    
    :param blend: The name of the blend file
    :type blend: str
    """


def endGame():
    """Ends the current game."""


def restartGame():
    """Restarts the current game by reloading the .blend file (the last saved version, not what is currently running)."""


def LibLoad(blend, type, data, load_actions=False, verbose=False, load_scripts=True, async=False):
    """Converts the all of the datablocks of the given type from the given blend.
    <Note> Asynchronously loaded libraries will not be available immediately after LibLoad() returns. Use the returned KX_LibLoadStatus to figure out when the libraries are ready.
    
    :param blend: The path to the blend file (or the name to use for the library if data is supplied)
    :type blend: str
    :param type: The datablock type (currently only "Action", "Mesh" and "Scene" are supported)
    :type type: str
    :param data: Binary data from a blend file (optional)
    :type data: bytes
    :param load_actions: Search for and load all actions in a given Scene and not just the "active" actions (Scene type only)
    :type load_actions: bool
    :param verbose: Whether or not to print debugging information (e.g., "SceneName: Scene")
    :type verbose: bool
    :param load_scripts: Whether or not to load text datablocks as well (can be disabled for some extra security)
    :type load_scripts: bool
    :param async: Whether or not to do the loading asynchronously (in another thread). Only the "Scene" type is currently supported for this feature.
    :type async: bool
    :rtype: bge.types.KX_LibLoadStatus
    """


def LibNew(name, type, data):
    """Uses existing datablock data and loads in as a new library.
    
    :param name: A unique library name used for removal later
    :type name: str
    :param type: The datablock type (currently only "Mesh" is supported)
    :type type: str
    :param data: A list of names of the datablocks to load
        (type: list of strings)
    :type data: list
    """


def LibFree(name):
    """Frees a library, removing all objects and meshes from the currently active scenes.
    
    :param name: The name of the library to free (the name used in LibNew)
    :type name: str
    """


def LibList():
    """Returns a list of currently loaded libraries.
    
    :rtype: list [str]
    """


def addScene(name, overlay=1):
    """Loads a scene into the game engine.
    <Note> This function is not effective immediately, the scene is queued
                                    and added on the next logic cycle where it will be available
                                    from getSceneList
    
    :param name: The name of the scene
    :type name: str
    :param overlay: Overlay or underlay (optional)
    :type overlay: int
    """


def sendMessage(subject, body="", to="", message_from=""):
    """Sends a message to sensors in any active scene.
    
    :param subject: The subject of the message
    :type subject: str
    :param body: The body of the message (optional)
    :type body: str
    :param to: The name of the object to send the message to (optional)
    :type to: str
    :param message_from: The name of the object that the message is coming from (optional)
    :type message_from: str
    """


def setGravity(gravity):
    """Sets the world gravity.
    
    :param gravity: gravity vector
    :type gravity: mathutils.Vector((fx, fy, fz))
    """


def getSpectrum():
    """Returns a 512 point list from the sound card.
                            This only works if the fmod sound driver is being used.
    
    :rtype: list [float], len(getSpectrum()) == 512
    """


def getMaxLogicFrame():
    """Gets the maximum number of logic frames per render frame.
    
    :return: The maximum number of logic frames per render frame
    :rtype: int
    """


def setMaxLogicFrame(maxlogic):
    """Sets the maximum number of logic frames that are executed per render frame.
                            This does not affect the physic system that still runs at full frame rate.
    
    :param maxlogic: The new maximum number of logic frames per render frame. Valid values: 1..5
    :type maxlogic: int
    """


def getMaxPhysicsFrame():
    """Gets the maximum number of physics frames per render frame.
    
    :return: The maximum number of physics frames per render frame
    :rtype: int
    """


def setMaxPhysicsFrame(maxphysics):
    """Sets the maximum number of physics timestep that are executed per render frame.
                            Higher value allows physics to keep up with realtime even if graphics slows down the game.
                            Physics timestep is fixed and equal to 1/tickrate (see setLogicTicRate)
                            maxphysics/ticrate is the maximum delay of the renderer that physics can compensate.
    
    :param maxphysics: The new maximum number of physics timestep per render frame. Valid values: 1..5.
    :type maxphysics: int
    """


def getLogicTicRate():
    """Gets the logic update frequency.
    
    :return: The logic frequency in Hz
    :rtype: float
    """


def setLogicTicRate(ticrate):
    """Sets the logic update frequency.
    The logic update frequency is the number of times logic bricks are executed every second.
                            The default is 60 Hz.
    
    :param ticrate: The new logic update frequency (in Hz).
    :type ticrate: float
    """


def getPhysicsTicRate():
    """Gets the physics update frequency
    
    :return: The physics update frequency in Hz
    :rtype: float
    """


def setPhysicsTicRate(ticrate):
    """Sets the physics update frequency
    The physics update frequency is the number of times the physics system is executed every second.
                            The default is 60 Hz.
    
    :param ticrate: The new update frequency (in Hz).
    :type ticrate: float
    """


def getAnimRecordFrame():
    """Gets the current frame number used for recording animations. This
                            number is incremented automatically by Blender when the "Record
                            animation" feature is turned on.
    
    :rtype: int
    """


def setAnimRecordFrame(framenr):
    """Sets the current frame number used for recording animations. This
                            number is automatically incremented by Blender when the "Record
                            animation" feature is turned on.
    The frame number Must be non-negative, unless Blender has
                            bpy.types.UserPreferencesEdit.use_negative_frames enabled
                            in its user preferences. Only use non-negative numbers to be on
                            the safe side, unless you know what you are doing.
    
    :param framenr: The new frame number.
    :type framenr: int
    """


def getExitKey():
    """Gets the key used to exit the game engine
    
    :return: The key (defaults to bge.events.ESCKEY)
    :rtype: int
    """


def setExitKey(key):
    """Sets the key used to exit the game engine
    
    :param key: A key constant from bge.events
    :type key: int
    """


def NextFrame():
    """Render next frame (if Python has control)"""


def setRender(render):
    """Sets the global flag that controls the render of the scene.
                            If True, the render is done after the logic frame.
                            If False, the render is skipped and another logic frame starts immediately.
    <Note> GPU VSync no longer limits the number of frame per second when render is off,
                                    but the Use Frame Rate option still regulates the fps. To run as many frames
                                    as possible, untick this option (Render Properties, System panel).
    
    :param render: the render flag
    :type render: bool
    """


def getRender():
    """Get the current value of the global render flag
    
    :return: The flag value
    :rtype: bool
    """


def getClockTime():
    """Get the current BGE render time, in seconds. The BGE render time is the
                            simulation time corresponding to the next scene that will be rendered.
    
    :rtype: double
    """


def getFrameTime():
    """Get the current BGE frame time, in seconds. The BGE frame time is the
                            simulation time corresponding to the current call of the logic system.
                            Generally speaking, it is what the user is interested in.
    
    :rtype: double
    """


def getRealTime():
    """Get the number of real (system-clock) seconds elapsed since the beginning
                            of the simulation.
    
    :rtype: double
    """


def getTimeScale():
    """Get the time multiplier between real-time and simulation time. The default
                            value is 1.0. A value greater than 1.0 means that the simulation is going
                            faster than real-time, a value lower than 1.0 means that the simulation is
                            going slower than real-time.
    
    :rtype: double
    """


def setTimeScale(time_scale):
    """Set the time multiplier between real-time and simulation time. A value
                            greater than 1.0 means that the simulation is going faster than real-time,
                            a value lower than 1.0 means that the simulation is going slower than
                            real-time. Note that a too large value may lead to some physics
                            instabilities.
    
    :param time_scale: The new time multiplier.
    """


def getUseExternalClock():
    """Get if the BGE use the inner BGE clock, or rely or on an external
                            clock. The default is to use the inner BGE clock.
    
    :rtype: bool
    """


def setUseExternalClock(use_external_clock):
    """Set if the BGE use the inner BGE clock, or rely or on an external
                            clock. If the user selects the use of an external clock, he should call
                            regularly the setClockTime method.
    
    :param use_external_clock: the new setting
    """


def setClockTime(new_time):
    """Set the next value of the simulation clock. It is preferable to use this
                            method from a custom main function in python, as calling it in the logic
                            block can easily lead to a blocked system (if the time does not advance
                            enough to run at least the next logic step).
    
    :param new_time: the next value of the BGE clock (in second).
    """


def expandPath(path):
    """Converts a blender internal path into a proper file system path.
    Use / as directory separator in path
                            You can use '//' at the start of the string to define a relative path;
                            Blender replaces that string by the directory of the current .blend or runtime file
                            to make a full path name. The function also converts the directory separator to
                            the local file system format.
    
    :param path: The path string to be converted/expanded.
    :type path: str
    :return: The converted string
    :rtype: str
    """


def getAverageFrameRate():
    """Gets the estimated/average framerate for all the active scenes, not only the current scene.
    
    :return: The estimated average framerate in frames per second
    :rtype: float
    """


def getBlendFileList(path = "//"):
    """Returns a list of blend files in the same directory as the open blend file, or from using the option argument.
    
    :param path: Optional directory argument, will be expanded (like expandPath) into the full path.
    :type path: str
    :return: A list of filenames, with no directory prefix
    :rtype: list
    """


def getRandomFloat():
    """Returns a random floating point value in the range [0 - 1)"""


def PrintGLInfo():
    """Prints GL Extension Info into the console"""


def PrintMemInfo():
    """Prints engine statistics into the console"""


def getProfileInfo():
    """Returns a Python dictionary that contains the same information as the on screen profiler. The keys are the profiler categories and the values are tuples with the first element being time taken (in ms) and the second element being the percentage of total time."""


KX_TRUE = None
"""True value used by some modules."""

KX_FALSE = None
"""False value used by some modules."""

KX_SENSOR_INACTIVE = None

KX_SENSOR_JUST_ACTIVATED = None

KX_SENSOR_ACTIVE = None

KX_SENSOR_JUST_DEACTIVATED = None

KX_ARMSENSOR_STATE_CHANGED = 0
"""Detect that the constraint is changing state (active/inactive)

:type: int
"""

KX_ARMSENSOR_LIN_ERROR_BELOW = 1
"""Detect that the constraint linear error is above a threshold

:type: int
"""

KX_ARMSENSOR_LIN_ERROR_ABOVE = 2
"""Detect that the constraint linear error is below a threshold

:type: int
"""

KX_ARMSENSOR_ROT_ERROR_BELOW = 3
"""Detect that the constraint rotation error is above a threshold

:type: int
"""

KX_ARMSENSOR_ROT_ERROR_ABOVE = 4
"""Detect that the constraint rotation error is below a threshold

:type: int
"""

KX_PROPSENSOR_EQUAL = 1
"""Activate when the property is equal to the sensor value.

:type: int
"""

KX_PROPSENSOR_NOTEQUAL = 2
"""Activate when the property is not equal to the sensor value.

:type: int
"""

KX_PROPSENSOR_INTERVAL = 3
"""Activate when the property is between the specified limits.

:type: int
"""

KX_PROPSENSOR_CHANGED = 4
"""Activate when the property changes

:type: int
"""

KX_PROPSENSOR_EXPRESSION = 5
"""Activate when the expression matches

:type: int
"""

KX_PROPSENSOR_LESSTHAN = 6
"""Activate when the property is less than the sensor value

:type: int
"""

KX_PROPSENSOR_GREATERTHAN = 7
"""Activate when the property is greater than the sensor value

:type: int
"""

KX_RADAR_AXIS_POS_X = None

KX_RADAR_AXIS_POS_Y = None

KX_RADAR_AXIS_POS_Z = None

KX_RADAR_AXIS_NEG_X = None

KX_RADAR_AXIS_NEG_Y = None

KX_RADAR_AXIS_NEG_Z = None

KX_RAY_AXIS_POS_X = None

KX_RAY_AXIS_POS_Y = None

KX_RAY_AXIS_POS_Z = None

KX_RAY_AXIS_NEG_X = None

KX_RAY_AXIS_NEG_Y = None

KX_RAY_AXIS_NEG_Z = None

KX_ACTIONACT_PLAY = None

KX_ACTIONACT_PINGPONG = None

KX_ACTIONACT_FLIPPER = None

KX_ACTIONACT_LOOPSTOP = None

KX_ACTIONACT_LOOPEND = None

KX_ACTIONACT_PROPERTY = None

KX_ACT_ARMATURE_RUN = 0
"""Just make sure the armature will be updated on the next graphic frame.
                                This is the only persistent mode of the actuator:
                                it executes automatically once per frame until stopped by a controller

:type: int
"""

KX_ACT_ARMATURE_ENABLE = 1
"""Enable the constraint.

:type: int
"""

KX_ACT_ARMATURE_DISABLE = 2
"""Disable the constraint (runtime constraint values are not updated).

:type: int
"""

KX_ACT_ARMATURE_SETTARGET = 3
"""Change target and subtarget of constraint.

:type: int
"""

KX_ACT_ARMATURE_SETWEIGHT = 4
"""Change weight of constraint (IK only).

:type: int
"""

KX_ACT_ARMATURE_SETINFLUENCE = 5
"""Change influence of constraint.

:type: int
"""

KX_CONSTRAINTACT_NORMAL = None
"""Activate alignment to surface"""

KX_CONSTRAINTACT_DISTANCE = None
"""Activate distance control"""

KX_CONSTRAINTACT_LOCAL = None
"""Direction of the ray is along the local axis"""

KX_CONSTRAINTACT_DOROTFH = None
"""Force field act on rotation as well"""

KX_CONSTRAINTACT_MATERIAL = None
"""Detect material rather than property"""

KX_CONSTRAINTACT_PERMANENT = None
"""No deactivation if ray does not hit target"""

KX_CONSTRAINTACT_LOCX = None
"""Limit X coord."""

KX_CONSTRAINTACT_LOCY = None
"""Limit Y coord"""

KX_CONSTRAINTACT_LOCZ = None
"""Limit Z coord"""

KX_CONSTRAINTACT_ROTX = None
"""Limit X rotation"""

KX_CONSTRAINTACT_ROTY = None
"""Limit Y rotation"""

KX_CONSTRAINTACT_ROTZ = None
"""Limit Z rotation"""

KX_CONSTRAINTACT_DIRNX = None
"""Set distance along negative X axis"""

KX_CONSTRAINTACT_DIRNY = None
"""Set distance along negative Y axis"""

KX_CONSTRAINTACT_DIRNZ = None
"""Set distance along negative Z axis"""

KX_CONSTRAINTACT_DIRPX = None
"""Set distance along positive X axis"""

KX_CONSTRAINTACT_DIRPY = None
"""Set distance along positive Y axis"""

KX_CONSTRAINTACT_DIRPZ = None
"""Set distance along positive Z axis"""

KX_CONSTRAINTACT_ORIX = None
"""Set orientation of X axis"""

KX_CONSTRAINTACT_ORIY = None
"""Set orientation of Y axis"""

KX_CONSTRAINTACT_ORIZ = None
"""Set orientation of Z axis"""

KX_CONSTRAINTACT_FHNX = None
"""Set force field along negative X axis"""

KX_CONSTRAINTACT_FHNY = None
"""Set force field along negative Y axis"""

KX_CONSTRAINTACT_FHNZ = None
"""Set force field along negative Z axis"""

KX_CONSTRAINTACT_FHPX = None
"""Set force field along positive X axis"""

KX_CONSTRAINTACT_FHPY = None
"""Set force field along positive Y axis"""

KX_CONSTRAINTACT_FHPZ = None
"""Set force field along positive Z axis"""

KX_DYN_RESTORE_DYNAMICS = None

KX_DYN_DISABLE_DYNAMICS = None

KX_DYN_ENABLE_RIGID_BODY = None

KX_DYN_DISABLE_RIGID_BODY = None

KX_DYN_SET_MASS = None

KX_GAME_LOAD = None

KX_GAME_START = None

KX_GAME_RESTART = None

KX_GAME_QUIT = None

KX_GAME_SAVECFG = None

KX_GAME_LOADCFG = None

KX_ACT_MOUSE_OBJECT_AXIS_X = None

KX_ACT_MOUSE_OBJECT_AXIS_Y = None

KX_ACT_MOUSE_OBJECT_AXIS_Z = None

KX_PARENT_REMOVE = None

KX_PARENT_SET = None

KX_RANDOMACT_BOOL_CONST = None

KX_RANDOMACT_BOOL_UNIFORM = None

KX_RANDOMACT_BOOL_BERNOUILLI = None

KX_RANDOMACT_INT_CONST = None

KX_RANDOMACT_INT_UNIFORM = None

KX_RANDOMACT_INT_POISSON = None

KX_RANDOMACT_FLOAT_CONST = None

KX_RANDOMACT_FLOAT_UNIFORM = None

KX_RANDOMACT_FLOAT_NORMAL = None

KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL = None

KX_SCENE_RESTART = None

KX_SCENE_SET_SCENE = None

KX_SCENE_SET_CAMERA = None

KX_SCENE_ADD_FRONT_SCENE = None

KX_SCENE_ADD_BACK_SCENE = None

KX_SCENE_REMOVE_SCENE = None

KX_SCENE_SUSPEND = None

KX_SCENE_RESUME = None

KX_SOUNDACT_PLAYSTOP = 1
""":type: int"""

KX_SOUNDACT_PLAYEND = 2
""":type: int"""

KX_SOUNDACT_LOOPSTOP = 3
""":type: int"""

KX_SOUNDACT_LOOPEND = 4
""":type: int"""

KX_SOUNDACT_LOOPBIDIRECTIONAL = 5
""":type: int"""

KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP = 6
""":type: int"""

KX_STEERING_SEEK = 1
""":type: int"""

KX_STEERING_FLEE = 2
""":type: int"""

KX_STEERING_PATHFOLLOWING = 3
""":type: int"""

KX_TRACK_UPAXIS_POS_X = None

KX_TRACK_UPAXIS_POS_Y = None

KX_TRACK_UPAXIS_POS_Z = None

KX_TRACK_TRAXIS_POS_X = None

KX_TRACK_TRAXIS_POS_Y = None

KX_TRACK_TRAXIS_POS_Z = None

KX_TRACK_TRAXIS_NEG_X = None

KX_TRACK_TRAXIS_NEG_Y = None

KX_TRACK_TRAXIS_NEG_Z = None

RAS_2DFILTER_BLUR = 2
""":type: int"""

RAS_2DFILTER_CUSTOMFILTER = 12
"""Customer filter, the code code is set via shaderText property.

:type: int
"""

RAS_2DFILTER_DILATION = 4
""":type: int"""

RAS_2DFILTER_DISABLED = -1
"""Disable the filter that is currently active

:type: int
"""

RAS_2DFILTER_ENABLED = -2
"""Enable the filter that was previously disabled

:type: int
"""

RAS_2DFILTER_EROSION = 5
""":type: int"""

RAS_2DFILTER_GRAYSCALE = 9
""":type: int"""

RAS_2DFILTER_INVERT = 11
""":type: int"""

RAS_2DFILTER_LAPLACIAN = 6
""":type: int"""

RAS_2DFILTER_MOTIONBLUR = 1
"""Create and enable preset filters

:type: int
"""

RAS_2DFILTER_NOFILTER = 0
"""Disable and destroy the filter that is currently active

:type: int
"""

RAS_2DFILTER_PREWITT = 8
""":type: int"""

RAS_2DFILTER_SEPIA = 10
""":type: int"""

RAS_2DFILTER_SHARPEN = 3
""":type: int"""

RAS_2DFILTER_SOBEL = 7
""":type: int"""

ROT_MODE_QUAT = 0
"""Use quaternion in rotation attribute to update bone rotation.

:type: int
"""

ROT_MODE_XYZ = 1
"""Use euler_rotation and apply angles on bone's Z, Y, X axis successively.

:type: int
"""

ROT_MODE_XZY = 2
"""Use euler_rotation and apply angles on bone's Y, Z, X axis successively.

:type: int
"""

ROT_MODE_YXZ = 3
"""Use euler_rotation and apply angles on bone's Z, X, Y axis successively.

:type: int
"""

ROT_MODE_YZX = 4
"""Use euler_rotation and apply angles on bone's X, Z, Y axis successively.

:type: int
"""

ROT_MODE_ZXY = 5
"""Use euler_rotation and apply angles on bone's Y, X, Z axis successively.

:type: int
"""

ROT_MODE_ZYX = 6
"""Use euler_rotation and apply angles on bone's X, Y, Z axis successively.

:type: int
"""

CONSTRAINT_TYPE_TRACKTO = None

CONSTRAINT_TYPE_KINEMATIC = None

CONSTRAINT_TYPE_ROTLIKE = None

CONSTRAINT_TYPE_LOCLIKE = None

CONSTRAINT_TYPE_MINMAX = None

CONSTRAINT_TYPE_SIZELIKE = None

CONSTRAINT_TYPE_LOCKTRACK = None

CONSTRAINT_TYPE_STRETCHTO = None

CONSTRAINT_TYPE_CLAMPTO = None

CONSTRAINT_TYPE_TRANSFORM = None

CONSTRAINT_TYPE_DISTLIMIT = None

CONSTRAINT_IK_COPYPOSE = 0
"""constraint is trying to match the position and eventually the rotation of the target.

:type: int
"""

CONSTRAINT_IK_DISTANCE = 1
"""Constraint is maintaining a certain distance to target subject to ik_mode

:type: int
"""

CONSTRAINT_IK_FLAG_TIP = 1
"""Set when the constraint operates on the head of the bone and not the tail

:type: int
"""

CONSTRAINT_IK_FLAG_ROT = 2
"""Set when the constraint tries to match the orientation of the target

:type: int
"""

CONSTRAINT_IK_FLAG_STRETCH = 16
"""Set when the armature is allowed to stretch (only the bones with stretch factor > 0.0)

:type: int
"""

CONSTRAINT_IK_FLAG_POS = 32
"""Set when the constraint tries to match the position of the target.

:type: int
"""

CONSTRAINT_IK_MODE_INSIDE = 0
"""The constraint tries to keep the bone within ik_dist of target

:type: int
"""

CONSTRAINT_IK_MODE_OUTSIDE = 1
"""The constraint tries to keep the bone outside ik_dist of the target

:type: int
"""

CONSTRAINT_IK_MODE_ONSURFACE = 2
"""The constraint tries to keep the bone exactly at ik_dist of the target.

:type: int
"""

BL_DST_ALPHA = None

BL_DST_COLOR = None

BL_ONE = None

BL_ONE_MINUS_DST_ALPHA = None

BL_ONE_MINUS_DST_COLOR = None

BL_ONE_MINUS_SRC_ALPHA = None

BL_ONE_MINUS_SRC_COLOR = None

BL_SRC_ALPHA = None

BL_SRC_ALPHA_SATURATE = None

BL_SRC_COLOR = None

BL_ZERO = None

KX_INPUT_NONE = None

KX_INPUT_JUST_ACTIVATED = None

KX_INPUT_ACTIVE = None

KX_INPUT_JUST_RELEASED = None

KX_ACTION_MODE_PLAY = 0
"""Play the action once.

:type: int
"""

KX_ACTION_MODE_LOOP = 1
"""Loop the action (repeat it).

:type: int
"""

KX_ACTION_MODE_PING_PONG = 2
"""Play the action one direct then back the other way when it has completed.

:type: int
"""

KX_ACTION_BLEND_BLEND = 0
"""Blend layers using linear interpolation

:type: int
"""

KX_ACTION_BLEND_ADD = 1
"""Adds the layers together

:type: int
"""

KX_MOUSE_BUT_LEFT = None

KX_MOUSE_BUT_MIDDLE = None

KX_MOUSE_BUT_RIGHT = None

RM_WALLS = None
"""Draw only the walls."""

RM_POLYS = None
"""Draw only polygons."""

RM_TRIS = None
"""Draw triangle mesh."""

VIEWMATRIX = None

VIEWMATRIX_INVERSE = None

VIEWMATRIX_INVERSETRANSPOSE = None

VIEWMATRIX_TRANSPOSE = None

MODELMATRIX = None

MODELMATRIX_INVERSE = None

MODELMATRIX_INVERSETRANSPOSE = None

MODELMATRIX_TRANSPOSE = None

MODELVIEWMATRIX = None

MODELVIEWMATRIX_INVERSE = None

MODELVIEWMATRIX_INVERSETRANSPOSE = None

MODELVIEWMATRIX_TRANSPOSE = None

CAM_POS = None
"""Current camera position"""

CONSTANT_TIMER = None
"""User a timer for the uniform value."""

SHD_TANGENT = None

KX_STATE1 = None

KX_STATE2 = None

KX_STATE3 = None

KX_STATE4 = None

KX_STATE5 = None

KX_STATE6 = None

KX_STATE7 = None

KX_STATE8 = None

KX_STATE9 = None

KX_STATE10 = None

KX_STATE11 = None

KX_STATE12 = None

KX_STATE13 = None

KX_STATE14 = None

KX_STATE15 = None

KX_STATE16 = None

KX_STATE17 = None

KX_STATE18 = None

KX_STATE19 = None

KX_STATE20 = None

KX_STATE21 = None

KX_STATE22 = None

KX_STATE23 = None

KX_STATE24 = None

KX_STATE25 = None

KX_STATE26 = None

KX_STATE27 = None

KX_STATE28 = None

KX_STATE29 = None

KX_STATE30 = None

KX_STATE_OP_CLR = 0
"""Substract bits to state mask

:type: int
"""

KX_STATE_OP_CPY = 1
"""Copy state mask

:type: int
"""

KX_STATE_OP_NEG = 2
"""Invert bits to state mask

:type: int
"""

KX_STATE_OP_SET = 3
"""Add bits to state mask

:type: int
"""
