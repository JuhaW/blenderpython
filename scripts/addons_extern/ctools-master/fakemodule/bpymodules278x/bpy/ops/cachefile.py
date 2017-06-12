def open(*args, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=True, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
    """Load a cache file
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param filepath: File Path, Path to file
        (type: str, (optional, never None))
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
        (type: boolean, (optional))
    :type check_existing: bool
    :param filter_blender: Filter .blend files
        (type: boolean, (optional))
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
        (type: boolean, (optional))
    :type filter_backup: bool
    :param filter_image: Filter image files
        (type: boolean, (optional))
    :type filter_image: bool
    :param filter_movie: Filter movie files
        (type: boolean, (optional))
    :type filter_movie: bool
    :param filter_python: Filter python files
        (type: boolean, (optional))
    :type filter_python: bool
    :param filter_font: Filter font files
        (type: boolean, (optional))
    :type filter_font: bool
    :param filter_sound: Filter sound files
        (type: boolean, (optional))
    :type filter_sound: bool
    :param filter_text: Filter text files
        (type: boolean, (optional))
    :type filter_text: bool
    :param filter_btx: Filter btx files
        (type: boolean, (optional))
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
        (type: boolean, (optional))
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
        (type: boolean, (optional))
    :type filter_alembic: bool
    :param filter_folder: Filter folders
        (type: boolean, (optional))
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
        (type: boolean, (optional))
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        (type: int in [1, 9], (optional))
    :type filemode: int
    :param display_type: Display Type
        * 'DEFAULT': Default, Automatically determine display type for files.
        * 'LIST_SHORT': Short List, Display files as short list.
        * 'LIST_LONG': Long List, Display files as a detailed list.
        * 'THUMBNAIL': Thumbnails, Display files as thumbnails.
        (type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional))
    :type display_type: str
    :param sort_method: File sorting mode
        * 'FILE_SORT_ALPHA': Sort alphabetically, Sort the file list alphabetically.
        * 'FILE_SORT_EXTENSION': Sort by extension, Sort the file list by extension/type.
        * 'FILE_SORT_TIME': Sort by time, Sort files by modification time.
        * 'FILE_SORT_SIZE': Sort by size, Sort files by size.
        (type: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional))
    :type sort_method: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def reload(*args):
    """Update objects paths list with new data from the archive
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
