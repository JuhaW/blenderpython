def bvh(*args, filepath="", axis_forward='-Z', axis_up='Y', filter_glob="*.bvh", target='ARMATURE', global_scale=1.0, frame_start=1, use_fps_scale=False, update_scene_fps=False, update_scene_duration=False, use_cyclic=False, rotate_mode='NATIVE'):
    """Load a BVH motion capture file
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param filepath: File Path, Filepath used for importing the file
        (type: str, (optional, never None))
    :type filepath: str
    :param axis_forward: Forward
        (type: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional))
    :type axis_forward: str
    :param axis_up: Up
        (type: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional))
    :type axis_up: str
    :param filter_glob: filter_glob
        (type: str, (optional, never None))
    :type filter_glob: str
    :param target: Target, Import target type
        (type: enum in ['ARMATURE', 'OBJECT'], (optional))
    :type target: str
    :param global_scale: Scale, Scale the BVH by this value
        (type: float in [0.0001, 1e+06], (optional))
    :type global_scale: float
    :param frame_start: Start Frame, Starting frame for the animation
        (type: int in [-inf, inf], (optional))
    :type frame_start: int
    :param use_fps_scale: Scale FPS, Scale the framerate from the BVH to the current scenes, otherwise each BVH frame maps directly to a Blender frame
        (type: boolean, (optional))
    :type use_fps_scale: bool
    :param update_scene_fps: Update Scene FPS, Set the scene framerate to that of the BVH file (note that this nullifies the 'Scale FPS' option, as the scale will be 1:1)
        (type: boolean, (optional))
    :type update_scene_fps: bool
    :param update_scene_duration: Update Scene Duration, Extend the scene's duration to the BVH duration (never shortens the scene)
        (type: boolean, (optional))
    :type update_scene_duration: bool
    :param use_cyclic: Loop, Loop the animation playback
        (type: boolean, (optional))
    :type use_cyclic: bool
    :param rotate_mode: Rotation, Rotation conversion
        * 'QUATERNION': Quaternion, Convert rotations to quaternions.
        * 'NATIVE': Euler (Native), Use the rotation order defined in the BVH file.
        * 'XYZ': Euler (XYZ), Convert rotations to euler XYZ.
        * 'XZY': Euler (XZY), Convert rotations to euler XZY.
        * 'YXZ': Euler (YXZ), Convert rotations to euler YXZ.
        * 'YZX': Euler (YZX), Convert rotations to euler YZX.
        * 'ZXY': Euler (ZXY), Convert rotations to euler ZXY.
        * 'ZYX': Euler (ZYX), Convert rotations to euler ZYX.
        (type: enum in ['QUATERNION', 'NATIVE', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'], (optional))
    :type rotate_mode: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
