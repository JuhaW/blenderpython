def ply(*args, filepath="", files=None, directory="", filter_glob="*.ply"):
    """Load a PLY geometry file
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param filepath: File Path, Filepath used for importing the file
        (type: str, (optional, never None))
    :type filepath: str
    :param files: File Path, File path used for importing the PLY file
        (type: bpy_prop_collection of OperatorFileListElement, (optional))
    :type files: bpy_prop_collection
    :param directory: directory
        (type: str, (optional, never None))
    :type directory: str
    :param filter_glob: filter_glob
        (type: str, (optional, never None))
    :type filter_glob: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def stl(*args, filepath="", axis_forward='Y', axis_up='Z', filter_glob="*.stl", files=None, directory="", global_scale=1.0, use_scene_unit=False, use_facet_normal=False):
    """Load STL triangle mesh data
    
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
    :param files: File Path
        (type: bpy_prop_collection of OperatorFileListElement, (optional))
    :type files: bpy_prop_collection
    :param directory: directory
        (type: str, (optional, never None))
    :type directory: str
    :param global_scale: Scale
        (type: float in [1e-06, 1e+06], (optional))
    :type global_scale: float
    :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to imported data
        (type: boolean, (optional))
    :type use_scene_unit: bool
    :param use_facet_normal: Facet Normals, Use (import) facet normals (note that this will still give flat shading)
        (type: boolean, (optional))
    :type use_facet_normal: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
