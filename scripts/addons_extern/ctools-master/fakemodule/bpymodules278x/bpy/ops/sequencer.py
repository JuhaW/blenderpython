def change_effect_input(*args, swap='A_B'):
    """Undocumented
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param swap: Swap, The effect inputs to swap
        (type: enum in ['A_B', 'B_C', 'A_C'], (optional))
    :type swap: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def change_effect_type(*args, type='CROSS'):
    """Undocumented
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type, Sequencer effect type
        * 'CROSS': Crossfade, Crossfade effect strip type.
        * 'ADD': Add, Add effect strip type.
        * 'SUBTRACT': Subtract, Subtract effect strip type.
        * 'ALPHA_OVER': Alpha Over, Alpha Over effect strip type.
        * 'ALPHA_UNDER': Alpha Under, Alpha Under effect strip type.
        * 'GAMMA_CROSS': Gamma Cross, Gamma Cross effect strip type.
        * 'MULTIPLY': Multiply, Multiply effect strip type.
        * 'OVER_DROP': Alpha Over Drop, Alpha Over Drop effect strip type.
        * 'WIPE': Wipe, Wipe effect strip type.
        * 'GLOW': Glow, Glow effect strip type.
        * 'TRANSFORM': Transform, Transform effect strip type.
        * 'COLOR': Color, Color effect strip type.
        * 'SPEED': Speed, Color effect strip type.
        * 'MULTICAM': Multicam Selector.
        * 'ADJUSTMENT': Adjustment Layer.
        * 'GAUSSIAN_BLUR': Gaussian Blur.
        * 'TEXT': Text.
        (type: enum in ['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'OVER_DROP', 'WIPE', 'GLOW', 'TRANSFORM', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def change_path(*args, filepath="", directory="", files=None, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', use_placeholders=False):
    """Undocumented
    
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
    :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
        (type: boolean, (optional))
    :type use_placeholders: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def copy(*args):
    """Undocumented
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def crossfade_sounds(*args):
    """Do cross-fading volume animation of two selected sound strips
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def cut(*args, frame=0, type='SOFT', side='BOTH'):
    """Cut the selected strips
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param frame: Frame, Frame where selected strips will be cut
        (type: int in [-inf, inf], (optional))
    :type frame: int
    :param type: Type, The type of cut operation to perform on strips
        (type: enum in ['SOFT', 'HARD'], (optional))
    :type type: str
    :param side: Side, The side that remains selected after cutting
        (type: enum in ['LEFT', 'RIGHT', 'BOTH'], (optional))
    :type side: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def cut_multicam(*args, camera=1):
    """Cut multi-cam strip and select camera
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param camera: Camera
        (type: int in [1, 32], (optional))
    :type camera: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def deinterlace_selected_movies(*args):
    """Deinterlace all selected movie sources
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def delete(*args):
    """Erase selected strips from the sequencer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def duplicate(*args, mode='TRANSLATION'):
    """Duplicate the selected strips
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mode: Mode
        (type: enum in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional))
    :type mode: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def duplicate_move(*args, SEQUENCER_OT_duplicate=None, TRANSFORM_OT_seq_slide=None):
    """Duplicate selected strips and move them
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips
        (type: SEQUENCER_OT_duplicate, (optional))
    :type SEQUENCER_OT_duplicate: SEQUENCER_OT_duplicate
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
        (type: TRANSFORM_OT_seq_slide, (optional))
    :type TRANSFORM_OT_seq_slide: TRANSFORM_OT_seq_slide
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def effect_strip_add(*args, frame_start=0, frame_end=0, channel=1, replace_sel=True, overlap=False, type='CROSS', color=(0.0, 0.0, 0.0)):
    """Add an effect to the sequencer, most are applied on top of existing strips
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param frame_start: Start Frame, Start frame of the sequence strip
        (type: int in [-inf, inf], (optional))
    :type frame_start: int
    :param frame_end: End Frame, End frame for the color strip
        (type: int in [-inf, inf], (optional))
    :type frame_end: int
    :param channel: Channel, Channel to place this strip into
        (type: int in [1, 32], (optional))
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
        (type: boolean, (optional))
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
        (type: boolean, (optional))
    :type overlap: bool
    :param type: Type, Sequencer effect type
        * 'CROSS': Crossfade, Crossfade effect strip type.
        * 'ADD': Add, Add effect strip type.
        * 'SUBTRACT': Subtract, Subtract effect strip type.
        * 'ALPHA_OVER': Alpha Over, Alpha Over effect strip type.
        * 'ALPHA_UNDER': Alpha Under, Alpha Under effect strip type.
        * 'GAMMA_CROSS': Gamma Cross, Gamma Cross effect strip type.
        * 'MULTIPLY': Multiply, Multiply effect strip type.
        * 'OVER_DROP': Alpha Over Drop, Alpha Over Drop effect strip type.
        * 'WIPE': Wipe, Wipe effect strip type.
        * 'GLOW': Glow, Glow effect strip type.
        * 'TRANSFORM': Transform, Transform effect strip type.
        * 'COLOR': Color, Color effect strip type.
        * 'SPEED': Speed, Color effect strip type.
        * 'MULTICAM': Multicam Selector.
        * 'ADJUSTMENT': Adjustment Layer.
        * 'GAUSSIAN_BLUR': Gaussian Blur.
        * 'TEXT': Text.
        (type: enum in ['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'OVER_DROP', 'WIPE', 'GLOW', 'TRANSFORM', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT'], (optional))
    :type type: str
    :param color: Color, Initialize the strip with this color (only used when type='COLOR')
        (type: float array of 3 items in [0, 1], (optional))
    :type color: mathutils.Vector
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def enable_proxies(*args, proxy_25=False, proxy_50=False, proxy_75=False, proxy_100=False, override=False):
    """Enable selected proxies on all selected Movie strips
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param proxy_25: 25%
        (type: boolean, (optional))
    :type proxy_25: bool
    :param proxy_50: 50%
        (type: boolean, (optional))
    :type proxy_50: bool
    :param proxy_75: 75%
        (type: boolean, (optional))
    :type proxy_75: bool
    :param proxy_100: 100%
        (type: boolean, (optional))
    :type proxy_100: bool
    :param override: Override
        (type: boolean, (optional))
    :type override: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def export_subtitles(*args, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA'):
    """Export .srt file containing text strips
    
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


def gap_insert(*args, frames=10):
    """Insert gap at current frame to first strips at the right, independent of selection or locked state of strips
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param frames: Frames, Frames to insert after current strip
        (type: int in [0, inf], (optional))
    :type frames: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def gap_remove(*args, all=False):
    """Remove gap at current frame to first strip at the right, independent of selection or locked state of strips
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param all: All Gaps, Do all gaps to right of current frame
        (type: boolean, (optional))
    :type all: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def image_strip_add(*args, directory="", files=None, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', frame_start=0, frame_end=0, channel=1, replace_sel=True, overlap=False, use_placeholders=False):
    """Add an image or image sequence to the sequencer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
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
    :param frame_start: Start Frame, Start frame of the sequence strip
        (type: int in [-inf, inf], (optional))
    :type frame_start: int
    :param frame_end: End Frame, End frame for the color strip
        (type: int in [-inf, inf], (optional))
    :type frame_end: int
    :param channel: Channel, Channel to place this strip into
        (type: int in [1, 32], (optional))
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
        (type: boolean, (optional))
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
        (type: boolean, (optional))
    :type overlap: bool
    :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
        (type: boolean, (optional))
    :type use_placeholders: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def images_separate(*args, length=1):
    """On image sequence strips, it returns a strip for each image
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param length: Length, Length of each frame
        (type: int in [1, inf], (optional))
    :type length: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def lock(*args):
    """Lock the active strip so that it can't be transformed
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def mask_strip_add(*args, frame_start=0, channel=1, replace_sel=True, overlap=False, mask=''):
    """Add a mask strip to the sequencer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param frame_start: Start Frame, Start frame of the sequence strip
        (type: int in [-inf, inf], (optional))
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
        (type: int in [1, 32], (optional))
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
        (type: boolean, (optional))
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
        (type: boolean, (optional))
    :type overlap: bool
    :param mask: Mask
        (type: enum in [], (optional))
    :type mask: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def meta_make(*args):
    """Group selected strips into a metastrip
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def meta_separate(*args):
    """Put the contents of a metastrip back in the sequencer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def meta_toggle(*args):
    """Toggle a metastrip (to edit enclosed strips)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def movie_strip_add(*args, filepath="", files=None, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', frame_start=0, channel=1, replace_sel=True, overlap=False, sound=True, use_framerate=True):
    """Add a movie strip to the sequencer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param filepath: File Path, Path to file
        (type: str, (optional, never None))
    :type filepath: str
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
    :param frame_start: Start Frame, Start frame of the sequence strip
        (type: int in [-inf, inf], (optional))
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
        (type: int in [1, 32], (optional))
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
        (type: boolean, (optional))
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
        (type: boolean, (optional))
    :type overlap: bool
    :param sound: Sound, Load sound with the movie
        (type: boolean, (optional))
    :type sound: bool
    :param use_framerate: Use Movie Framerate, Use framerate from the movie to keep sound and video in sync
        (type: boolean, (optional))
    :type use_framerate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def movieclip_strip_add(*args, frame_start=0, channel=1, replace_sel=True, overlap=False, clip=''):
    """Add a movieclip strip to the sequencer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param frame_start: Start Frame, Start frame of the sequence strip
        (type: int in [-inf, inf], (optional))
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
        (type: int in [1, 32], (optional))
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
        (type: boolean, (optional))
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
        (type: boolean, (optional))
    :type overlap: bool
    :param clip: Clip
        (type: enum in [], (optional))
    :type clip: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def mute(*args, unselected=False):
    """Mute (un)selected strips
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param unselected: Unselected, Mute unselected rather than selected strips
        (type: boolean, (optional))
    :type unselected: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def offset_clear(*args):
    """Clear strip offsets from the start and end frames
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def paste(*args):
    """Undocumented
    
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


def reassign_inputs(*args):
    """Reassign the inputs for the effect strip
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def rebuild_proxy(*args):
    """Rebuild all selected proxies and timecode indices using the job system
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def refresh_all(*args):
    """Refresh the sequencer editor
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def reload(*args, adjust_length=False):
    """Reload strips in the sequencer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param adjust_length: Adjust Length, Adjust length of strips to their data length
        (type: boolean, (optional))
    :type adjust_length: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def rendersize(*args):
    """Set render size and aspect from active sequence
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def sample(*args):
    """Use mouse to sample color in current frame
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def scene_strip_add(*args, frame_start=0, channel=1, replace_sel=True, overlap=False, scene=''):
    """Add a strip to the sequencer using a blender scene as a source
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param frame_start: Start Frame, Start frame of the sequence strip
        (type: int in [-inf, inf], (optional))
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
        (type: int in [1, 32], (optional))
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
        (type: boolean, (optional))
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
        (type: boolean, (optional))
    :type overlap: bool
    :param scene: Scene
        (type: enum in [], (optional))
    :type scene: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select(*args, extend=False, linked_handle=False, left_right='NONE', linked_time=False):
    """Select a strip (last selected becomes the "active strip")
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend the selection
        (type: boolean, (optional))
    :type extend: bool
    :param linked_handle: Linked Handle, Select handles next to the active strip
        (type: boolean, (optional))
    :type linked_handle: bool
    :param left_right: Left/Right, Select based on the current frame side the cursor is on
        * 'NONE': None, Don't do left-right selection.
        * 'MOUSE': Mouse, Use mouse position for selection.
        * 'LEFT': Left, Select left.
        * 'RIGHT': Right, Select right.
        (type: enum in ['NONE', 'MOUSE', 'LEFT', 'RIGHT'], (optional))
    :type left_right: str
    :param linked_time: Linked Time, Select other strips at the same time
        (type: boolean, (optional))
    :type linked_time: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_active_side(*args, side='BOTH'):
    """Select strips on the nominated side of the active strip
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param side: Side, The side of the handle that is selected
        (type: enum in ['LEFT', 'RIGHT', 'BOTH'], (optional))
    :type side: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_all(*args, action='TOGGLE'):
    """Select or deselect all strips
    
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


def select_border(*args, gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True):
    """Select strips using border selection
    
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
    :param extend: Extend, Extend selection instead of deselecting everything first
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_grouped(*args, type='TYPE', extend=False, use_active_channel=False):
    """Select all strips grouped by various properties
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        * 'TYPE': Type, Shared strip type.
        * 'TYPE_BASIC': Global Type, All strips of same basic type (Graphical or Sound).
        * 'TYPE_EFFECT': Effect Type, Shared strip effect type (if active strip is not an effect one, select all non-effect strips).
        * 'DATA': Data, Shared data (scene, image, sound, etc.).
        * 'EFFECT': Effect, Shared effects.
        * 'EFFECT_LINK': Effect/Linked, Other strips affected by the active one (sharing some time, and below or effect-assigned).
        * 'OVERLAP': Overlap, Overlapping time.
        (type: enum in ['TYPE', 'TYPE_BASIC', 'TYPE_EFFECT', 'DATA', 'EFFECT', 'EFFECT_LINK', 'OVERLAP'], (optional))
    :type type: str
    :param extend: Extend, Extend selection instead of deselecting everything first
        (type: boolean, (optional))
    :type extend: bool
    :param use_active_channel: Same Channel, Only consider strips on the same channel as the active one
        (type: boolean, (optional))
    :type use_active_channel: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_handles(*args, side='BOTH'):
    """Select manipulator handles on the sides of the selected strip
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param side: Side, The side of the handle that is selected
        (type: enum in ['LEFT', 'RIGHT', 'BOTH'], (optional))
    :type side: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_less(*args):
    """Shrink the current selection of adjacent selected strips
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_linked(*args):
    """Select all strips adjacent to the current selection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_linked_pick(*args, extend=False):
    """Select a chain of linked strips nearest to the mouse pointer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend the selection
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_more(*args):
    """Select more strips adjacent to the current selection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def slip(*args, offset=0):
    """Trim the contents of the active strip
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param offset: Offset, Offset to the data of the strip
        (type: int in [-inf, inf], (optional))
    :type offset: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def snap(*args, frame=0):
    """Frame where selected strips will be snapped
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param frame: Frame, Frame where selected strips will be snapped
        (type: int in [-inf, inf], (optional))
    :type frame: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def sound_strip_add(*args, filepath="", files=None, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', frame_start=0, channel=1, replace_sel=True, overlap=False, cache=False, mono=False):
    """Add a sound strip to the sequencer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param filepath: File Path, Path to file
        (type: str, (optional, never None))
    :type filepath: str
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
    :param frame_start: Start Frame, Start frame of the sequence strip
        (type: int in [-inf, inf], (optional))
    :type frame_start: int
    :param channel: Channel, Channel to place this strip into
        (type: int in [1, 32], (optional))
    :type channel: int
    :param replace_sel: Replace Selection, Replace the current selection
        (type: boolean, (optional))
    :type replace_sel: bool
    :param overlap: Allow Overlap, Don't correct overlap on new sequence strips
        (type: boolean, (optional))
    :type overlap: bool
    :param cache: Cache, Cache the sound in memory
        (type: boolean, (optional))
    :type cache: bool
    :param mono: Mono, Merge all the sound's channels into one
        (type: boolean, (optional))
    :type mono: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def strip_jump(*args, next=True, center=True):
    """Move frame to previous edit point
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param next: Next Strip
        (type: boolean, (optional))
    :type next: bool
    :param center: Use strip center
        (type: boolean, (optional))
    :type center: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def strip_modifier_add(*args, type='COLOR_BALANCE'):
    """Add a modifier to the strip
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        (type: enum in ['COLOR_BALANCE', 'CURVES', 'HUE_CORRECT', 'BRIGHT_CONTRAST', 'MASK', 'WHITE_BALANCE', 'TONEMAP'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def strip_modifier_copy(*args, type='REPLACE'):
    """Copy modifiers of the active strip to all selected strips
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        * 'REPLACE': Replace, Replace modifiers in destination.
        * 'APPEND': Append, Append active modifiers to selected strips.
        (type: enum in ['REPLACE', 'APPEND'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def strip_modifier_move(*args, name="Name", direction='UP'):
    """Move modifier up and down in the stack
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param name: Name, Name of modifier to remove
        (type: str, (optional, never None))
    :type name: str
    :param direction: Type
        * 'UP': Up, Move modifier up in the stack.
        * 'DOWN': Down, Move modifier down in the stack.
        (type: enum in ['UP', 'DOWN'], (optional))
    :type direction: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def strip_modifier_remove(*args, name="Name"):
    """Remove a modifier from the strip
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param name: Name, Name of modifier to remove
        (type: str, (optional, never None))
    :type name: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def swap(*args, side='RIGHT'):
    """Swap active strip with strip to the right or left
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param side: Side, Side of the strip to swap
        (type: enum in ['LEFT', 'RIGHT'], (optional))
    :type side: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def swap_data(*args):
    """Swap 2 sequencer strips
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def swap_inputs(*args):
    """Swap the first two inputs for the effect strip
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def unlock(*args):
    """Unlock the active strip so that it can't be transformed
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def unmute(*args, unselected=False):
    """Unmute (un)selected strips
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param unselected: Unselected, Unmute unselected rather than selected strips
        (type: boolean, (optional))
    :type unselected: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_all(*args):
    """View all the strips in the sequencer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_all_preview(*args):
    """Zoom preview to fit in the area
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_frame(*args):
    """Reset viewable area to show range around current frame
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_ghost_border(*args, gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0):
    """Set the boundaries of the border used for offset-view
    
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


def view_selected(*args):
    """Zoom the sequencer on the selected strips
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_toggle(*args):
    """Toggle between sequencer views (sequence, preview, both)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def view_zoom_ratio(*args, ratio=1.0):
    """Change zoom ratio of sequencer preview
    
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
