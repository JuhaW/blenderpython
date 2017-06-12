def armature_apply(*args):
    """Apply the current pose as the new rest pose
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def autoside_names(*args, axis='XAXIS'):
    """Automatically renames the selected bones according to which side of the target axis they fall on
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param axis: Axis, Axis tag names with
        * 'XAXIS': X-Axis, Left/Right.
        * 'YAXIS': Y-Axis, Front/Back.
        * 'ZAXIS': Z-Axis, Top/Bottom.
        (type: enum in ['XAXIS', 'YAXIS', 'ZAXIS'], (optional))
    :type axis: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def bone_layers(*args, layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Change the layers that the selected bones belong to
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param layers: Layer, Armature layers that bone belongs to
        (type: boolean array of 32 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def breakdown(*args, percentage=0.5, prev_frame=0, next_frame=0, channels='ALL', axis_lock='FREE'):
    """Create a suitable breakdown pose on the current frame
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param percentage: Percentage, Weighting factor for which keyframe is favored more
        (type: float in [0, 1], (optional))
    :type percentage: float
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        (type: int in [-500000, 500000], (optional))
    :type prev_frame: int
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        (type: int in [-500000, 500000], (optional))
    :type next_frame: int
    :param channels: Channels, Set of properties that are affected
        * 'ALL': All Properties, All properties, including transforms, bendy bone shape, and custom properties.
        * 'LOC': Location, Location only.
        * 'ROT': Rotation, Rotation only.
        * 'SIZE': Scale, Scale only.
        * 'BBONE': Bendy Bone, Bendy Bone shape properties.
        * 'CUSTOM': Custom Properties, Custom properties.
        (type: enum in ['ALL', 'LOC', 'ROT', 'SIZE', 'BBONE', 'CUSTOM'], (optional))
    :type channels: str
    :param axis_lock: Axis Lock, Transform axis to restrict effects to
        * 'FREE': Free, All axes are affected.
        * 'X': X, Only X-axis transforms are affected.
        * 'Y': Y, Only Y-axis transforms are affected.
        * 'Z': Z, Only Z-axis transforms are affected.
        (type: enum in ['FREE', 'X', 'Y', 'Z'], (optional))
    :type axis_lock: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def constraint_add(*args, type=''):
    """Add a constraint to the active bone
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        * 'CAMERA_SOLVER': Camera Solver.
        * 'FOLLOW_TRACK': Follow Track.
        * 'OBJECT_SOLVER': Object Solver.
        * 'COPY_LOCATION': Copy Location, Copy the location of a target (with an optional offset), so that they move together.
        * 'COPY_ROTATION': Copy Rotation, Copy the rotation of a target (with an optional offset), so that they rotate together.
        * 'COPY_SCALE': Copy Scale, Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount.
        * 'COPY_TRANSFORMS': Copy Transforms, Copy all the transformations of a target, so that they move together.
        * 'LIMIT_DISTANCE': Limit Distance, Restrict movements to within a certain distance of a target (at the time of constraint evaluation only).
        * 'LIMIT_LOCATION': Limit Location, Restrict movement along each axis within given ranges.
        * 'LIMIT_ROTATION': Limit Rotation, Restrict rotation along each axis within given ranges.
        * 'LIMIT_SCALE': Limit Scale, Restrict scaling along each axis with given ranges.
        * 'MAINTAIN_VOLUME': Maintain Volume, Compensate for scaling one axis by applying suitable scaling to the other two axes.
        * 'TRANSFORM': Transformation, Use one transform property from target to control another (or same) property on owner.
        * 'TRANSFORM_CACHE': Transform Cache, Look up the transformation matrix from an external file.
        * 'CLAMP_TO': Clamp To, Restrict movements to lie along a curve by remapping location along curve's longest axis.
        * 'DAMPED_TRACK': Damped Track, Point towards a target by performing the smallest rotation necessary.
        * 'IK': Inverse Kinematics, Control a chain of bones by specifying the endpoint target (Bones only).
        * 'LOCKED_TRACK': Locked Track, Rotate around the specified ('locked') axis to point towards a target.
        * 'SPLINE_IK': Spline IK, Align chain of bones along a curve (Bones only).
        * 'STRETCH_TO': Stretch To, Stretch along Y-Axis to point towards a target.
        * 'TRACK_TO': Track To, Legacy tracking constraint prone to twisting artifacts.
        * 'ACTION': Action, Use transform property of target to look up pose for owner from an Action.
        * 'CHILD_OF': Child Of, Make target the 'detachable' parent of owner.
        * 'FLOOR': Floor, Use position (and optionally rotation) of target to define a 'wall' or 'floor' that the owner can not cross.
        * 'FOLLOW_PATH': Follow Path, Use to animate an object/bone following a path.
        * 'PIVOT': Pivot, Change pivot point for transforms (buggy).
        * 'RIGID_BODY_JOINT': Rigid Body Joint, Use to define a Rigid Body Constraint (for Game Engine use only).
        * 'SCRIPT': Script, Custom constraint(s) written in Python (Not yet implemented).
        * 'SHRINKWRAP': Shrinkwrap, Restrict movements to surface of target mesh.
        (type: enum in ['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'PIVOT', 'RIGID_BODY_JOINT', 'SCRIPT', 'SHRINKWRAP'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def constraint_add_with_targets(*args, type=''):
    """Add a constraint to the active bone, with target (where applicable) set to the selected Objects/Bones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        * 'CAMERA_SOLVER': Camera Solver.
        * 'FOLLOW_TRACK': Follow Track.
        * 'OBJECT_SOLVER': Object Solver.
        * 'COPY_LOCATION': Copy Location, Copy the location of a target (with an optional offset), so that they move together.
        * 'COPY_ROTATION': Copy Rotation, Copy the rotation of a target (with an optional offset), so that they rotate together.
        * 'COPY_SCALE': Copy Scale, Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount.
        * 'COPY_TRANSFORMS': Copy Transforms, Copy all the transformations of a target, so that they move together.
        * 'LIMIT_DISTANCE': Limit Distance, Restrict movements to within a certain distance of a target (at the time of constraint evaluation only).
        * 'LIMIT_LOCATION': Limit Location, Restrict movement along each axis within given ranges.
        * 'LIMIT_ROTATION': Limit Rotation, Restrict rotation along each axis within given ranges.
        * 'LIMIT_SCALE': Limit Scale, Restrict scaling along each axis with given ranges.
        * 'MAINTAIN_VOLUME': Maintain Volume, Compensate for scaling one axis by applying suitable scaling to the other two axes.
        * 'TRANSFORM': Transformation, Use one transform property from target to control another (or same) property on owner.
        * 'TRANSFORM_CACHE': Transform Cache, Look up the transformation matrix from an external file.
        * 'CLAMP_TO': Clamp To, Restrict movements to lie along a curve by remapping location along curve's longest axis.
        * 'DAMPED_TRACK': Damped Track, Point towards a target by performing the smallest rotation necessary.
        * 'IK': Inverse Kinematics, Control a chain of bones by specifying the endpoint target (Bones only).
        * 'LOCKED_TRACK': Locked Track, Rotate around the specified ('locked') axis to point towards a target.
        * 'SPLINE_IK': Spline IK, Align chain of bones along a curve (Bones only).
        * 'STRETCH_TO': Stretch To, Stretch along Y-Axis to point towards a target.
        * 'TRACK_TO': Track To, Legacy tracking constraint prone to twisting artifacts.
        * 'ACTION': Action, Use transform property of target to look up pose for owner from an Action.
        * 'CHILD_OF': Child Of, Make target the 'detachable' parent of owner.
        * 'FLOOR': Floor, Use position (and optionally rotation) of target to define a 'wall' or 'floor' that the owner can not cross.
        * 'FOLLOW_PATH': Follow Path, Use to animate an object/bone following a path.
        * 'PIVOT': Pivot, Change pivot point for transforms (buggy).
        * 'RIGID_BODY_JOINT': Rigid Body Joint, Use to define a Rigid Body Constraint (for Game Engine use only).
        * 'SCRIPT': Script, Custom constraint(s) written in Python (Not yet implemented).
        * 'SHRINKWRAP': Shrinkwrap, Restrict movements to surface of target mesh.
        (type: enum in ['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'PIVOT', 'RIGID_BODY_JOINT', 'SCRIPT', 'SHRINKWRAP'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def constraints_clear(*args):
    """Clear all the constraints for the selected bones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def constraints_copy(*args):
    """Copy constraints to other selected bones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def copy(*args):
    """Copies the current pose of the selected bones to copy/paste buffer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def flip_names(*args):
    """Flips (and corrects) the axis suffixes of the names of selected bones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def group_add(*args):
    """Add a new bone group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def group_assign(*args, type=0):
    """Add selected bones to the chosen bone group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Bone Group Index
        (type: int in [0, inf], (optional))
    :type type: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def group_deselect(*args):
    """Deselect bones of active Bone Group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def group_move(*args, direction='UP'):
    """Change position of active Bone Group in list of Bone Groups
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param direction: Direction, Direction to move the active Bone Group towards
        (type: enum in ['UP', 'DOWN'], (optional))
    :type direction: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def group_remove(*args):
    """Remove the active bone group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def group_select(*args):
    """Select bones in active Bone Group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def group_sort(*args):
    """Sort Bone Groups by their names in ascending order
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def group_unassign(*args):
    """Remove selected bones from all bone groups
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hide(*args, unselected=False):
    """Tag selected bones to not be visible in Pose Mode
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param unselected: Unselected
        (type: boolean, (optional))
    :type unselected: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def ik_add(*args, with_targets=True):
    """Add IK Constraint to the active Bone
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param with_targets: With Targets, Assign IK Constraint with targets derived from the select bones/objects
        (type: boolean, (optional))
    :type with_targets: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def ik_clear(*args):
    """Remove all IK Constraints from selected bones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def loc_clear(*args):
    """Reset locations of selected bones to their default values
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def paste(*args, flipped=False, selected_mask=False):
    """Paste the stored pose on to the current pose
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param flipped: Flipped on X-Axis, Paste the stored pose flipped on to current pose
        (type: boolean, (optional))
    :type flipped: bool
    :param selected_mask: On Selected Only, Only paste the stored pose on to selected bones in the current pose
        (type: boolean, (optional))
    :type selected_mask: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def paths_calculate(*args, start_frame=1, end_frame=250, bake_location='TAILS'):
    """Calculate paths for the selected bones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param start_frame: Start, First frame to calculate bone paths on
        (type: int in [-500000, 500000], (optional))
    :type start_frame: int
    :param end_frame: End, Last frame to calculate bone paths on
        (type: int in [-500000, 500000], (optional))
    :type end_frame: int
    :param bake_location: Bake Location, Which point on the bones is used when calculating paths
        * 'HEADS': Heads, Calculate bone paths from heads.
        * 'TAILS': Tails, Calculate bone paths from tails.
        (type: enum in ['HEADS', 'TAILS'], (optional))
    :type bake_location: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def paths_clear(*args, only_selected=False):
    """Clear path caches for all bones, hold Shift key for selected bones only
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param only_selected: Only Selected, Only clear paths from selected bones
        (type: boolean, (optional))
    :type only_selected: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def paths_update(*args):
    """Recalculate paths for bones that already have them
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def propagate(*args, mode='WHILE_HELD', end_frame=250.0):
    """Copy selected aspects of the current pose to subsequent poses already keyframed
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mode: Terminate Mode, Method used to determine when to stop propagating pose to keyframes
        * 'WHILE_HELD': While Held, Propagate pose to all keyframes after current frame that don't change (Default behavior).
        * 'NEXT_KEY': To Next Keyframe, Propagate pose to first keyframe following the current frame only.
        * 'LAST_KEY': To Last Keyframe, Propagate pose to the last keyframe only (i.e. making action cyclic).
        * 'BEFORE_FRAME': Before Frame, Propagate pose to all keyframes between current frame and 'Frame' property.
        * 'BEFORE_END': Before Last Keyframe, Propagate pose to all keyframes from current frame until no more are found.
        * 'SELECTED_KEYS': On Selected Keyframes, Propagate pose to all selected keyframes.
        * 'SELECTED_MARKERS': On Selected Markers, Propagate pose to all keyframes occurring on frames with Scene Markers after the current frame.
        (type: enum in ['WHILE_HELD', 'NEXT_KEY', 'LAST_KEY', 'BEFORE_FRAME', 'BEFORE_END', 'SELECTED_KEYS', 'SELECTED_MARKERS'], (optional))
    :type mode: str
    :param end_frame: End Frame, Frame to stop propagating frames to (for 'Before Frame' mode)
        (type: float in [1.17549e-38, inf], (optional))
    :type end_frame: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def push(*args, percentage=0.5, prev_frame=0, next_frame=0, channels='ALL', axis_lock='FREE'):
    """Exaggerate the current pose
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param percentage: Percentage, Weighting factor for which keyframe is favored more
        (type: float in [0, 1], (optional))
    :type percentage: float
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        (type: int in [-500000, 500000], (optional))
    :type prev_frame: int
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        (type: int in [-500000, 500000], (optional))
    :type next_frame: int
    :param channels: Channels, Set of properties that are affected
        * 'ALL': All Properties, All properties, including transforms, bendy bone shape, and custom properties.
        * 'LOC': Location, Location only.
        * 'ROT': Rotation, Rotation only.
        * 'SIZE': Scale, Scale only.
        * 'BBONE': Bendy Bone, Bendy Bone shape properties.
        * 'CUSTOM': Custom Properties, Custom properties.
        (type: enum in ['ALL', 'LOC', 'ROT', 'SIZE', 'BBONE', 'CUSTOM'], (optional))
    :type channels: str
    :param axis_lock: Axis Lock, Transform axis to restrict effects to
        * 'FREE': Free, All axes are affected.
        * 'X': X, Only X-axis transforms are affected.
        * 'Y': Y, Only Y-axis transforms are affected.
        * 'Z': Z, Only Z-axis transforms are affected.
        (type: enum in ['FREE', 'X', 'Y', 'Z'], (optional))
    :type axis_lock: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def quaternions_flip(*args):
    """Flip quaternion values to achieve desired rotations, while maintaining the same orientations
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def relax(*args, percentage=0.5, prev_frame=0, next_frame=0, channels='ALL', axis_lock='FREE'):
    """Make the current pose more similar to its surrounding ones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param percentage: Percentage, Weighting factor for which keyframe is favored more
        (type: float in [0, 1], (optional))
    :type percentage: float
    :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        (type: int in [-500000, 500000], (optional))
    :type prev_frame: int
    :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        (type: int in [-500000, 500000], (optional))
    :type next_frame: int
    :param channels: Channels, Set of properties that are affected
        * 'ALL': All Properties, All properties, including transforms, bendy bone shape, and custom properties.
        * 'LOC': Location, Location only.
        * 'ROT': Rotation, Rotation only.
        * 'SIZE': Scale, Scale only.
        * 'BBONE': Bendy Bone, Bendy Bone shape properties.
        * 'CUSTOM': Custom Properties, Custom properties.
        (type: enum in ['ALL', 'LOC', 'ROT', 'SIZE', 'BBONE', 'CUSTOM'], (optional))
    :type channels: str
    :param axis_lock: Axis Lock, Transform axis to restrict effects to
        * 'FREE': Free, All axes are affected.
        * 'X': X, Only X-axis transforms are affected.
        * 'Y': Y, Only Y-axis transforms are affected.
        * 'Z': Z, Only Z-axis transforms are affected.
        (type: enum in ['FREE', 'X', 'Y', 'Z'], (optional))
    :type axis_lock: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def reveal(*args):
    """Unhide all bones that have been tagged to be hidden in Pose Mode
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def rot_clear(*args):
    """Reset rotations of selected bones to their default values
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def rotation_mode_set(*args, type='QUATERNION'):
    """Set the rotation representation used by selected bones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Rotation Mode
        * 'QUATERNION': Quaternion (WXYZ), No Gimbal Lock (default).
        * 'XYZ': XYZ Euler, XYZ Rotation Order (prone to Gimbal Lock).
        * 'XZY': XZY Euler, XZY Rotation Order (prone to Gimbal Lock).
        * 'YXZ': YXZ Euler, YXZ Rotation Order (prone to Gimbal Lock).
        * 'YZX': YZX Euler, YZX Rotation Order (prone to Gimbal Lock).
        * 'ZXY': ZXY Euler, ZXY Rotation Order (prone to Gimbal Lock).
        * 'ZYX': ZYX Euler, ZYX Rotation Order (prone to Gimbal Lock).
        * 'AXIS_ANGLE': Axis Angle, Axis Angle (W+XYZ), defines a rotation around some axis defined by 3D-Vector.
        (type: enum in ['QUATERNION', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'AXIS_ANGLE'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def scale_clear(*args):
    """Reset scaling of selected bones to their default values
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_all(*args, action='TOGGLE'):
    """Toggle selection status of all bones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param action: Action, Selection action to execute
        * 'TOGGLE': Toggle, Toggle selection for all elements.
        * 'SELECT': Select, Select all elements.
        * 'DESELECT': Deselect, Deselect all elements.
        * 'INVERT': Invert, Invert selection of all elements.
        (type: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional))
    :type action: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_constraint_target(*args):
    """Select bones used as targets for the currently selected bones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_grouped(*args, extend=False, type='LAYER'):
    """Select all visible bones grouped by similar properties
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend selection instead of deselecting everything first
        (type: boolean, (optional))
    :type extend: bool
    :param type: Type
        * 'LAYER': Layer, Shared layers.
        * 'GROUP': Group, Shared group.
        * 'KEYINGSET': Keying Set, All bones affected by active Keying Set.
        (type: enum in ['LAYER', 'GROUP', 'KEYINGSET'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_hierarchy(*args, direction='PARENT', extend=False):
    """Select immediate parent/children of selected bones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param direction: Direction
        (type: enum in ['PARENT', 'CHILD'], (optional))
    :type direction: str
    :param extend: Extend, Extend the selection
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_linked(*args, extend=False):
    """Select bones related to selected ones by parent/child relationships
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend selection instead of deselecting everything first
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_mirror(*args, only_active=False, extend=False):
    """Mirror the bone selection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param only_active: Active Only, Only operate on the active bone
        (type: boolean, (optional))
    :type only_active: bool
    :param extend: Extend, Extend the selection
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_parent(*args):
    """Select bones that are parents of the currently selected bones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def transforms_clear(*args):
    """Reset location, rotation, and scaling of selected bones to their default values
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def user_transforms_clear(*args, only_selected=True):
    """Reset pose on selected bones to keyframed state
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param only_selected: Only Selected, Only visible/selected bones
        (type: boolean, (optional))
    :type only_selected: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def visual_transform_apply(*args):
    """Apply final constrained position of pose bones to their transform
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
