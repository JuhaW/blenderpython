def cancel_stroke(*args):
    """Cancel the current sketch stroke
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def convert(*args):
    """Convert the selected sketch strokes to bone chains
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def delete(*args):
    """Delete a sketch stroke
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def draw_preview(*args, snap=False):
    """Draw preview of current sketch stroke (internal use)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param snap: Snap
        (type: boolean, (optional))
    :type snap: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def draw_stroke(*args, snap=False):
    """Start to draw a sketch stroke
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param snap: Snap
        (type: boolean, (optional))
    :type snap: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def finish_stroke(*args):
    """End and keep the current sketch stroke
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def gesture(*args, snap=False):
    """Start to draw a gesture stroke
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param snap: Snap
        (type: boolean, (optional))
    :type snap: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select(*args):
    """Select a sketch stroke
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
