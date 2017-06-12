def change_frame(*args, frame=0):
    """Interactively change the current frame number
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param frame: Frame
        (type: int in [-500000, 500000], (optional))
    :type frame: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def clear_render_border(*args):
    """Clear the boundaries of the border render and disable border render
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def curves_point_set(*args, point='BLACK_POINT'):
    """Set black point or white point for curves
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param point: Point, Set black point or white point for curves
        (type: enum in ['BLACK_POINT', 'WHITE_POINT'], (optional))
    :type point: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def cycle_render_slot(*args, reverse=False):
    """Cycle through all non-void render slots
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param reverse: Cycle in Reverse
        (type: boolean, (optional))
    :type reverse: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def external_edit(*args, filepath=""):
    """Edit image in an external application
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param filepath: filepath
        (type: str, (optional, never None))
    :type filepath: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def invert(*args, invert_r=False, invert_g=False, invert_b=False, invert_a=False):
    """Invert image's channels
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param invert_r: Red, Invert Red Channel
        (type: boolean, (optional))
    :type invert_r: bool
    :param invert_g: Green, Invert Green Channel
        (type: boolean, (optional))
    :type invert_g: bool
    :param invert_b: Blue, Invert Blue Channel
        (type: boolean, (optional))
    :type invert_b: bool
    :param invert_a: Alpha, Invert Alpha Channel
        (type: boolean, (optional))
    :type invert_a: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def match_movie_length(*args):
    """Set image's user's length to the one of this video
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def new(*args, name="Untitled", width=1024, height=1024, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='BLANK', float=False, gen_context='NONE', use_stereo_3d=False):
    """Create a new image
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param name: Name, Image data-block name
        (type: str, (optional, never None))
    :type name: str
    :param width: Width, Image width
        (type: int in [1, inf], (optional))
    :type width: int
    :param height: Height, Image height
        (type: int in [1, inf], (optional))
    :type height: int
    :param color: Color, Default fill color
        (type: float array of 4 items in [0, inf], (optional))
    :type color: mathutils.Color
    :param alpha: Alpha, Create an image with an alpha channel
        (type: boolean, (optional))
    :type alpha: bool
    :param generated_type: Generated Type, Fill the image with a grid for UV map testing
        * 'BLANK': Blank, Generate a blank image.
        * 'UV_GRID': UV Grid, Generated grid to test UV mappings.
        * 'COLOR_GRID': Color Grid, Generated improved UV grid to test UV mappings.
        (type: enum in ['BLANK', 'UV_GRID', 'COLOR_GRID'], (optional))
    :type generated_type: str
    :param float: 32 bit Float, Create image with 32 bit floating point bit depth
        (type: boolean, (optional))
    :type float: bool
    :param gen_context: Gen Context, Generation context
        (type: enum in ['NONE', 'PAINT_CANVAS', 'PAINT_STENCIL'], (optional))
    :type gen_context: str
    :param use_stereo_3d: Stereo 3D, Create an image with left and right views
        (type: boolean, (optional))
    :type use_stereo_3d: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def open(*args, filepath="", directory="", files=None, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
    """Open image
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param filepath: File Path, Path to file
        (type: str, (optional, never None))
    :type filepath: str
    :param directory: Directory, Directory of the file
        (type: str, (optional, never None))
    :type directory: str
    :param files: Files
        (type: bpy_prop_collection of OperatorFileListElement, (optional))
    :type files: bpy_prop_collection
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
    :param relative_path: Relative Path, Select the file relative to the blend file
        (type: boolean, (optional))
    :type relative_path: bool
    :param show_multiview: Enable Multi-View
        (type: boolean, (optional))
    :type show_multiview: bool
    :param use_multiview: Use Multi-View
        (type: boolean, (optional))
    :type use_multiview: bool
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


def pack(*args, as_png=False):
    """Pack an image as embedded data into the .blend file
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param as_png: Pack As PNG, Pack image as lossless PNG
        (type: boolean, (optional))
    :type as_png: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def project_apply(*args):
    """Project edited image back onto the object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def project_edit(*args):
    """Edit a snapshot of the view-port in an external image editor
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def properties(*args):
    """Toggle the properties region visibility
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def read_renderlayers(*args):
    """Read all the current scene's render layers from cache, as needed
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def reload(*args):
    """Reload current image from disk
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def render_border(*args, xmin=0, xmax=0, ymin=0, ymax=0):
    """Set the boundaries of the border render and enable border render
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param xmin: X Min
        (type: int in [-inf, inf], (optional))
    :type xmin: int
    :param xmax: X Max
        (type: int in [-inf, inf], (optional))
    :type xmax: int
    :param ymin: Y Min
        (type: int in [-inf, inf], (optional))
    :type ymin: int
    :param ymax: Y Max
        (type: int in [-inf, inf], (optional))
    :type ymax: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def replace(*args, filepath="", filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
    """Replace current image by another one from disk
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param filepath: File Path, Path to file
        (type: str, (optional, never None))
    :type filepath: str
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
    :param relative_path: Relative Path, Select the file relative to the blend file
        (type: boolean, (optional))
    :type relative_path: bool
    :param show_multiview: Enable Multi-View
        (type: boolean, (optional))
    :type show_multiview: bool
    :param use_multiview: Use Multi-View
        (type: boolean, (optional))
    :type use_multiview: bool
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


def sample(*args):
    """Use mouse to sample a color in current image
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def sample_line(*args, xstart=0, xend=0, ystart=0, yend=0, cursor=1002):
    """Sample a line and show it in Scope panels
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param xstart: X Start
        (type: int in [-inf, inf], (optional))
    :type xstart: int
    :param xend: X End
        (type: int in [-inf, inf], (optional))
    :type xend: int
    :param ystart: Y Start
        (type: int in [-inf, inf], (optional))
    :type ystart: int
    :param yend: Y End
        (type: int in [-inf, inf], (optional))
    :type yend: int
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
        (type: int in [0, inf], (optional))
    :type cursor: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def save(*args):
    """Save the image with current name and settings
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def save_as(*args, save_as_render=False, copy=False, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
    """Save the image with another name and/or settings
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param save_as_render: Save As Render, Apply render part of display transform when saving byte image
        (type: boolean, (optional))
    :type save_as_render: bool
    :param copy: Copy, Create a new image file without modifying the current image in blender
        (type: boolean, (optional))
    :type copy: bool
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
    :param relative_path: Relative Path, Select the file relative to the blend file
        (type: boolean, (optional))
    :type relative_path: bool
    :param show_multiview: Enable Multi-View
        (type: boolean, (optional))
    :type show_multiview: bool
    :param use_multiview: Use Multi-View
        (type: boolean, (optional))
    :type use_multiview: bool
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


def save_dirty(*args):
    """Save all modified textures
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def save_sequence(*args):
    """Save a sequence of images
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def toolshelf(*args):
    """Toggles tool shelf display
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def unpack(*args, method='USE_LOCAL', id=""):
    """Save an image packed in the .blend file to disk
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param method: Method, How to unpack
        (type: enum in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL'], (optional))
    :type method: str
    :param id: Image Name, Image data-block name to unpack
        (type: str, (optional, never None))
    :type id: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_all(*args, fit_view=False):
    """View the entire image
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param fit_view: Fit View, Fit frame to the viewport
        (type: boolean, (optional))
    :type fit_view: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_ndof(*args):
    """Use a 3D mouse device to pan/zoom the view
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_pan(*args, offset=(0.0, 0.0)):
    """Pan the view
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param offset: Offset, Offset in floating point units, 1.0 is the width and height of the image
        (type: float array of 2 items in [-inf, inf], (optional))
    :type offset: mathutils.Vector
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_selected(*args):
    """View all selected UVs
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_zoom(*args, factor=0.0):
    """Zoom in/out the image
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param factor: Factor, Zoom factor, values higher than 1.0 zoom in, lower values zoom out
        (type: float in [-inf, inf], (optional))
    :type factor: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_zoom_border(*args, gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0):
    """Zoom in the view to the nearest item contained in the border
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param gesture_mode: Gesture Mode
        (type: int in [-inf, inf], (optional))
    :type gesture_mode: int
    :param xmin: X Min
        (type: int in [-inf, inf], (optional))
    :type xmin: int
    :param xmax: X Max
        (type: int in [-inf, inf], (optional))
    :type xmax: int
    :param ymin: Y Min
        (type: int in [-inf, inf], (optional))
    :type ymin: int
    :param ymax: Y Max
        (type: int in [-inf, inf], (optional))
    :type ymax: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_zoom_in(*args, location=(0.0, 0.0)):
    """Zoom in the image (centered around 2D cursor)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param location: Location, Cursor location in screen coordinates
        (type: float array of 2 items in [-inf, inf], (optional))
    :type location: mathutils.Vector
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_zoom_out(*args, location=(0.0, 0.0)):
    """Zoom out the image (centered around 2D cursor)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param location: Location, Cursor location in screen coordinates
        (type: float array of 2 items in [-inf, inf], (optional))
    :type location: mathutils.Vector
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_zoom_ratio(*args, ratio=0.0):
    """Set zoom ratio of the view
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
        (type: float in [-inf, inf], (optional))
    :type ratio: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
