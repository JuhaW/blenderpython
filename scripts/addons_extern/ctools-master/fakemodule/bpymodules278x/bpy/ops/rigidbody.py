def bake_to_keyframes(*args, frame_start=1, frame_end=250, step=1):
    """Bake rigid body transformations of selected objects to keyframes
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param frame_start: Start Frame, Start frame for baking
        (type: int in [0, 300000], (optional))
    :type frame_start: int
    :param frame_end: End Frame, End frame for baking
        (type: int in [1, 300000], (optional))
    :type frame_end: int
    :param step: Frame Step, Frame Step
        (type: int in [1, 120], (optional))
    :type step: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def connect(*args, con_type='FIXED', pivot_type='CENTER', connection_pattern='SELECTED_TO_ACTIVE'):
    """Create rigid body constraints between selected rigid bodies
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param con_type: Type, Type of generated constraint
        * 'FIXED': Fixed, Glue rigid bodies together.
        * 'POINT': Point, Constrain rigid bodies to move around common pivot point.
        * 'HINGE': Hinge, Restrict rigid body rotation to one axis.
        * 'SLIDER': Slider, Restrict rigid body translation to one axis.
        * 'PISTON': Piston, Restrict rigid body translation and rotation to one axis.
        * 'GENERIC': Generic, Restrict translation and rotation to specified axes.
        * 'GENERIC_SPRING': Generic Spring, Restrict translation and rotation to specified axes with springs.
        * 'MOTOR': Motor, Drive rigid body around or along an axis.
        (type: enum in ['FIXED', 'POINT', 'HINGE', 'SLIDER', 'PISTON', 'GENERIC', 'GENERIC_SPRING', 'MOTOR'], (optional))
    :type con_type: str
    :param pivot_type: Location, Constraint pivot location
        * 'CENTER': Center, Pivot location is between the constrained rigid bodies.
        * 'ACTIVE': Active, Pivot location is at the active object position.
        * 'SELECTED': Selected, Pivot location is at the selected object position.
        (type: enum in ['CENTER', 'ACTIVE', 'SELECTED'], (optional))
    :type pivot_type: str
    :param connection_pattern: Connection Pattern, Pattern used to connect objects
        * 'SELECTED_TO_ACTIVE': Selected to Active, Connect selected objects to the active object.
        * 'CHAIN_DISTANCE': Chain by Distance, Connect objects as a chain based on distance, starting at the active object.
        (type: enum in ['SELECTED_TO_ACTIVE', 'CHAIN_DISTANCE'], (optional))
    :type connection_pattern: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def constraint_add(*args, type='FIXED'):
    """Add Rigid Body Constraint to active object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Rigid Body Constraint Type
        * 'FIXED': Fixed, Glue rigid bodies together.
        * 'POINT': Point, Constrain rigid bodies to move around common pivot point.
        * 'HINGE': Hinge, Restrict rigid body rotation to one axis.
        * 'SLIDER': Slider, Restrict rigid body translation to one axis.
        * 'PISTON': Piston, Restrict rigid body translation and rotation to one axis.
        * 'GENERIC': Generic, Restrict translation and rotation to specified axes.
        * 'GENERIC_SPRING': Generic Spring, Restrict translation and rotation to specified axes with springs.
        * 'MOTOR': Motor, Drive rigid body around or along an axis.
        (type: enum in ['FIXED', 'POINT', 'HINGE', 'SLIDER', 'PISTON', 'GENERIC', 'GENERIC_SPRING', 'MOTOR'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def constraint_remove(*args):
    """Remove Rigid Body Constraint from Object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def mass_calculate(*args, material='DEFAULT', density=1.0):
    """Automatically calculate mass values for Rigid Body Objects based on volume
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param material: Material Preset, Type of material that objects are made of (determines material density)
        (type: enum in ['DEFAULT'], (optional))
    :type material: str
    :param density: Density, Custom density value (kg/m^3) to use instead of material preset
        (type: float in [1.17549e-38, inf], (optional))
    :type density: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def object_add(*args, type='ACTIVE'):
    """Add active object as Rigid Body
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Rigid Body Type
        * 'ACTIVE': Active, Object is directly controlled by simulation results.
        * 'PASSIVE': Passive, Object is directly controlled by animation system.
        (type: enum in ['ACTIVE', 'PASSIVE'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def object_remove(*args):
    """Remove Rigid Body settings from Object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def object_settings_copy(*args):
    """Copy Rigid Body settings from active object to selected
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def objects_add(*args, type='ACTIVE'):
    """Add selected objects as Rigid Bodies
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Rigid Body Type
        * 'ACTIVE': Active, Object is directly controlled by simulation results.
        * 'PASSIVE': Passive, Object is directly controlled by animation system.
        (type: enum in ['ACTIVE', 'PASSIVE'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def objects_remove(*args):
    """Remove selected objects from Rigid Body simulation
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shape_change(*args, type='MESH'):
    """Change collision shapes for selected Rigid Body Objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Rigid Body Shape
        * 'BOX': Box, Box-like shapes (i.e. cubes), including planes (i.e. ground planes).
        * 'SPHERE': Sphere.
        * 'CAPSULE': Capsule.
        * 'CYLINDER': Cylinder.
        * 'CONE': Cone.
        * 'CONVEX_HULL': Convex Hull, A mesh-like surface encompassing (i.e. shrinkwrap over) all vertices (best results with fewer vertices).
        * 'MESH': Mesh, Mesh consisting of triangles only, allowing for more detailed interactions than convex hulls.
        (type: enum in ['BOX', 'SPHERE', 'CAPSULE', 'CYLINDER', 'CONE', 'CONVEX_HULL', 'MESH'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def world_add(*args):
    """Add Rigid Body simulation world to the current scene
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def world_remove(*args):
    """Remove Rigid Body simulation world from the current scene
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
