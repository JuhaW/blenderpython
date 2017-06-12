def ply(*args, filepath="", check_existing=True, axis_forward='Y', axis_up='Z', filter_glob="*.ply", use_mesh_modifiers=True, use_normals=True, use_uv_coords=True, use_colors=True, global_scale=1.0):
    """Export a single object as a Stanford PLY with normals, colors and texture coordinates
    
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
    :param axis_forward: Forward
        (type: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional))
    :type axis_forward: str
    :param axis_up: Up
        (type: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional))
    :type axis_up: str
    :param filter_glob: filter_glob
        (type: str, (optional, never None))
    :type filter_glob: str
    :param use_mesh_modifiers: Apply Modifiers, Apply Modifiers to the exported mesh
        (type: boolean, (optional))
    :type use_mesh_modifiers: bool
    :param use_normals: Normals, Export Normals for smooth and hard shaded faces (hard shaded faces will be exported as individual faces)
        (type: boolean, (optional))
    :type use_normals: bool
    :param use_uv_coords: UVs, Export the active UV layer
        (type: boolean, (optional))
    :type use_uv_coords: bool
    :param use_colors: Vertex Colors, Export the active vertex color layer
        (type: boolean, (optional))
    :type use_colors: bool
    :param global_scale: Scale
        (type: float in [0.01, 1000], (optional))
    :type global_scale: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def stl(*args, filepath="", check_existing=True, axis_forward='Y', axis_up='Z', filter_glob="*.stl", use_selection=False, global_scale=1.0, use_scene_unit=False, ascii=False, use_mesh_modifiers=True, batch_mode='OFF'):
    """Save STL triangle mesh data from the active object
    
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
    :param axis_forward: Forward
        (type: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional))
    :type axis_forward: str
    :param axis_up: Up
        (type: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional))
    :type axis_up: str
    :param filter_glob: filter_glob
        (type: str, (optional, never None))
    :type filter_glob: str
    :param use_selection: Selection Only, Export selected objects only
        (type: boolean, (optional))
    :type use_selection: bool
    :param global_scale: Scale
        (type: float in [0.01, 1000], (optional))
    :type global_scale: float
    :param use_scene_unit: Scene Unit, Apply current scene's unit (as defined by unit scale) to exported data
        (type: boolean, (optional))
    :type use_scene_unit: bool
    :param ascii: Ascii, Save the file in ASCII file format
        (type: boolean, (optional))
    :type ascii: bool
    :param use_mesh_modifiers: Apply Modifiers, Apply the modifiers before saving
        (type: boolean, (optional))
    :type use_mesh_modifiers: bool
    :param batch_mode: Batch Mode
        * 'OFF': Off, All data in one file.
        * 'OBJECT': Object, Each object as a file.
        (type: enum in ['OFF', 'OBJECT'], (optional))
    :type batch_mode: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
