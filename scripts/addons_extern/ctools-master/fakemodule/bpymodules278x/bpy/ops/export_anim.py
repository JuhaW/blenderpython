def bvh(*args, filepath="", check_existing=True, filter_glob="*.bvh", global_scale=1.0, frame_start=0, frame_end=0, rotate_mode='NATIVE', root_transform_only=False):
    """Save a BVH motion capture file from an armature
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param filepath: File Path, Filepath used for exporting the file
        (type: str, (optional, never None))
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
        (type: boolean, (optional))
    :type check_existing: bool
    :param filter_glob: filter_glob
        (type: str, (optional, never None))
    :type filter_glob: str
    :param global_scale: Scale, Scale the BVH by this value
        (type: float in [0.0001, 1e+06], (optional))
    :type global_scale: float
    :param frame_start: Start Frame, Starting frame to export
        (type: int in [-inf, inf], (optional))
    :type frame_start: int
    :param frame_end: End Frame, End frame to export
        (type: int in [-inf, inf], (optional))
    :type frame_end: int
    :param rotate_mode: Rotation, Rotation conversion
        * 'NATIVE': Euler (Native), Use the rotation order defined in the BVH file.
        * 'XYZ': Euler (XYZ), Convert rotations to euler XYZ.
        * 'XZY': Euler (XZY), Convert rotations to euler XZY.
        * 'YXZ': Euler (YXZ), Convert rotations to euler YXZ.
        * 'YZX': Euler (YZX), Convert rotations to euler YZX.
        * 'ZXY': Euler (ZXY), Convert rotations to euler ZXY.
        * 'ZYX': Euler (ZYX), Convert rotations to euler ZYX.
        (type: enum in ['NATIVE', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'], (optional))
    :type rotate_mode: str
    :param root_transform_only: Root Translation Only, Only write out translation channels for the root bone
        (type: boolean, (optional))
    :type root_transform_only: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
