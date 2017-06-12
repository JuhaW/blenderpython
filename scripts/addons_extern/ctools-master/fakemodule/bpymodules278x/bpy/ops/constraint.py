def childof_clear_inverse(*args, constraint="", owner='OBJECT'):
    """Clear inverse correction for ChildOf constraint
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param constraint: Constraint, Name of the constraint to edit
        (type: str, (optional, never None))
    :type constraint: str
    :param owner: Owner, The owner of this constraint
        * 'OBJECT': Object, Edit a constraint on the active object.
        * 'BONE': Bone, Edit a constraint on the active bone.
        (type: enum in ['OBJECT', 'BONE'], (optional))
    :type owner: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def childof_set_inverse(*args, constraint="", owner='OBJECT'):
    """Set inverse correction for ChildOf constraint
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param constraint: Constraint, Name of the constraint to edit
        (type: str, (optional, never None))
    :type constraint: str
    :param owner: Owner, The owner of this constraint
        * 'OBJECT': Object, Edit a constraint on the active object.
        * 'BONE': Bone, Edit a constraint on the active bone.
        (type: enum in ['OBJECT', 'BONE'], (optional))
    :type owner: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def delete(*args):
    """Remove constraint from constraint stack
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def followpath_path_animate(*args, constraint="", owner='OBJECT', frame_start=1, length=100):
    """Add default animation for path used by constraint if it isn't animated already
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param constraint: Constraint, Name of the constraint to edit
        (type: str, (optional, never None))
    :type constraint: str
    :param owner: Owner, The owner of this constraint
        * 'OBJECT': Object, Edit a constraint on the active object.
        * 'BONE': Bone, Edit a constraint on the active bone.
        (type: enum in ['OBJECT', 'BONE'], (optional))
    :type owner: str
    :param frame_start: Start Frame, First frame of path animation
        (type: int in [-500000, 500000], (optional))
    :type frame_start: int
    :param length: Length, Number of frames that path animation should take
        (type: int in [0, 500000], (optional))
    :type length: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def limitdistance_reset(*args, constraint="", owner='OBJECT'):
    """Reset limiting distance for Limit Distance Constraint
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param constraint: Constraint, Name of the constraint to edit
        (type: str, (optional, never None))
    :type constraint: str
    :param owner: Owner, The owner of this constraint
        * 'OBJECT': Object, Edit a constraint on the active object.
        * 'BONE': Bone, Edit a constraint on the active bone.
        (type: enum in ['OBJECT', 'BONE'], (optional))
    :type owner: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def move_down(*args, constraint="", owner='OBJECT'):
    """Move constraint down in constraint stack
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param constraint: Constraint, Name of the constraint to edit
        (type: str, (optional, never None))
    :type constraint: str
    :param owner: Owner, The owner of this constraint
        * 'OBJECT': Object, Edit a constraint on the active object.
        * 'BONE': Bone, Edit a constraint on the active bone.
        (type: enum in ['OBJECT', 'BONE'], (optional))
    :type owner: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def move_up(*args, constraint="", owner='OBJECT'):
    """Move constraint up in constraint stack
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param constraint: Constraint, Name of the constraint to edit
        (type: str, (optional, never None))
    :type constraint: str
    :param owner: Owner, The owner of this constraint
        * 'OBJECT': Object, Edit a constraint on the active object.
        * 'BONE': Bone, Edit a constraint on the active bone.
        (type: enum in ['OBJECT', 'BONE'], (optional))
    :type owner: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def objectsolver_clear_inverse(*args, constraint="", owner='OBJECT'):
    """Clear inverse correction for ObjectSolver constraint
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param constraint: Constraint, Name of the constraint to edit
        (type: str, (optional, never None))
    :type constraint: str
    :param owner: Owner, The owner of this constraint
        * 'OBJECT': Object, Edit a constraint on the active object.
        * 'BONE': Bone, Edit a constraint on the active bone.
        (type: enum in ['OBJECT', 'BONE'], (optional))
    :type owner: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def objectsolver_set_inverse(*args, constraint="", owner='OBJECT'):
    """Set inverse correction for ObjectSolver constraint
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param constraint: Constraint, Name of the constraint to edit
        (type: str, (optional, never None))
    :type constraint: str
    :param owner: Owner, The owner of this constraint
        * 'OBJECT': Object, Edit a constraint on the active object.
        * 'BONE': Bone, Edit a constraint on the active bone.
        (type: enum in ['OBJECT', 'BONE'], (optional))
    :type owner: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def reload_scripts(*args):
    """Reload python constraints
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def stretchto_reset(*args, constraint="", owner='OBJECT'):
    """Reset original length of bone for Stretch To Constraint
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param constraint: Constraint, Name of the constraint to edit
        (type: str, (optional, never None))
    :type constraint: str
    :param owner: Owner, The owner of this constraint
        * 'OBJECT': Object, Edit a constraint on the active object.
        * 'BONE': Bone, Edit a constraint on the active bone.
        (type: enum in ['OBJECT', 'BONE'], (optional))
    :type owner: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
