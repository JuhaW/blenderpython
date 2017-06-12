def add_simple_uvs(*args):
    """Add cube map uvs on mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def add_texture_paint_slot(*args, type='DIFFUSE_COLOR', name="Untitled", width=1024, height=1024, color=(0.0, 0.0, 0.0, 1.0), alpha=True, generated_type='BLANK', float=False):
    """Add a texture paint slot
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type, Merge method to use
        (type: enum in ['DIFFUSE_COLOR', 'DIFFUSE_INTENSITY', 'ALPHA', 'TRANSLUCENCY', 'SPECULAR_COLOR', 'SPECULAR_INTENSITY', 'SPECULAR_HARDNESS', 'AMBIENT', 'EMIT', 'MIRROR_COLOR', 'RAYMIRROR', 'NORMAL', 'WARP', 'DISPLACE'], (optional))
    :type type: str
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
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def brush_colors_flip(*args):
    """Toggle foreground and background brush colors
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def brush_select(*args, paint_mode='ACTIVE', sculpt_tool='BLOB', vertex_paint_tool='MIX', weight_paint_tool='MIX', texture_paint_tool='DRAW', toggle=False, create_missing=False):
    """Select a paint mode's brush by tool type
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param paint_mode: Paint Mode
        * 'ACTIVE': Current, Set brush for active paint mode.
        * 'SCULPT': Sculpt.
        * 'VERTEX_PAINT': Vertex Paint.
        * 'WEIGHT_PAINT': Weight Paint.
        * 'TEXTURE_PAINT': Texture Paint.
        (type: enum in ['ACTIVE', 'SCULPT', 'VERTEX_PAINT', 'WEIGHT_PAINT', 'TEXTURE_PAINT'], (optional))
    :type paint_mode: str
    :param sculpt_tool: Sculpt Tool
        (type: enum in ['BLOB', 'CLAY', 'CLAY_STRIPS', 'CREASE', 'DRAW', 'FILL', 'FLATTEN', 'GRAB', 'INFLATE', 'LAYER', 'MASK', 'NUDGE', 'PINCH', 'ROTATE', 'SCRAPE', 'SIMPLIFY', 'SMOOTH', 'SNAKE_HOOK', 'THUMB'], (optional))
    :type sculpt_tool: str
    :param vertex_paint_tool: Vertex Paint Tool
        * 'MIX': Mix, Use mix blending mode while painting.
        * 'ADD': Add, Use add blending mode while painting.
        * 'SUB': Subtract, Use subtract blending mode while painting.
        * 'MUL': Multiply, Use multiply blending mode while painting.
        * 'BLUR': Blur, Blur the color with surrounding values.
        * 'LIGHTEN': Lighten, Use lighten blending mode while painting.
        * 'DARKEN': Darken, Use darken blending mode while painting.
        (type: enum in ['MIX', 'ADD', 'SUB', 'MUL', 'BLUR', 'LIGHTEN', 'DARKEN'], (optional))
    :type vertex_paint_tool: str
    :param weight_paint_tool: Weight Paint Tool
        * 'MIX': Mix, Use mix blending mode while painting.
        * 'ADD': Add, Use add blending mode while painting.
        * 'SUB': Subtract, Use subtract blending mode while painting.
        * 'MUL': Multiply, Use multiply blending mode while painting.
        * 'BLUR': Blur, Blur the color with surrounding values.
        * 'LIGHTEN': Lighten, Use lighten blending mode while painting.
        * 'DARKEN': Darken, Use darken blending mode while painting.
        (type: enum in ['MIX', 'ADD', 'SUB', 'MUL', 'BLUR', 'LIGHTEN', 'DARKEN'], (optional))
    :type weight_paint_tool: str
    :param texture_paint_tool: Texture Paint Tool
        (type: enum in ['DRAW', 'SOFTEN', 'SMEAR', 'CLONE', 'FILL', 'MASK'], (optional))
    :type texture_paint_tool: str
    :param toggle: Toggle, Toggle between two brushes rather than cycling
        (type: boolean, (optional))
    :type toggle: bool
    :param create_missing: Create Missing, If the requested brush type does not exist, create a new brush
        (type: boolean, (optional))
    :type create_missing: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def delete_texture_paint_slot(*args):
    """Delete selected texture paint slot
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def face_select_all(*args, action='TOGGLE'):
    """Change selection for all faces
    
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


def face_select_hide(*args, unselected=False):
    """Hide selected faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param unselected: Unselected, Hide unselected rather than selected objects
        (type: boolean, (optional))
    :type unselected: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def face_select_linked(*args):
    """Select linked faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def face_select_linked_pick(*args, deselect=False):
    """Select linked faces under the cursor
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param deselect: Deselect, Deselect rather than select items
        (type: boolean, (optional))
    :type deselect: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def face_select_reveal(*args, unselected=False):
    """Reveal hidden faces
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param unselected: Unselected, Hide unselected rather than selected objects
        (type: boolean, (optional))
    :type unselected: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def grab_clone(*args, delta=(0.0, 0.0)):
    """Move the clone source image
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param delta: Delta, Delta offset of clone image in 0.0..1.0 coordinates
        (type: float array of 2 items in [-inf, inf], (optional))
    :type delta: mathutils.Vector
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hide_show(*args, action='HIDE', area='INSIDE', xmin=0, xmax=0, ymin=0, ymax=0):
    """Hide/show some vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param action: Action, Whether to hide or show vertices
        * 'HIDE': Hide, Hide vertices.
        * 'SHOW': Show, Show vertices.
        (type: enum in ['HIDE', 'SHOW'], (optional))
    :type action: str
    :param area: Area, Which vertices to hide or show
        * 'OUTSIDE': Outside, Hide or show vertices outside the selection.
        * 'INSIDE': Inside, Hide or show vertices inside the selection.
        * 'ALL': All, Hide or show all vertices.
        * 'MASKED': Masked, Hide or show vertices that are masked (minimum mask value of 0.5).
        (type: enum in ['OUTSIDE', 'INSIDE', 'ALL', 'MASKED'], (optional))
    :type area: str
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


def image_from_view(*args, filepath=""):
    """Make an image from the current 3D view for re-projection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param filepath: File Path, Name of the file
        (type: str, (optional, never None))
    :type filepath: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def image_paint(*args, stroke=None, mode='NORMAL'):
    """Paint a stroke into the image
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param stroke: Stroke
        (type: bpy_prop_collection of OperatorStrokeElement, (optional))
    :type stroke: bpy_prop_collection
    :param mode: Stroke Mode, Action taken when a paint stroke is made
        * 'NORMAL': Normal, Apply brush normally.
        * 'INVERT': Invert, Invert action of brush for duration of stroke.
        * 'SMOOTH': Smooth, Switch brush to smooth mode for duration of stroke.
        (type: enum in ['NORMAL', 'INVERT', 'SMOOTH'], (optional))
    :type mode: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def mask_flood_fill(*args, mode='VALUE', value=0.0):
    """Fill the whole mask with a given value, or invert its values
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mode: Mode
        * 'VALUE': Value, Set mask to the level specified by the 'value' property.
        * 'VALUE_INVERSE': Value Inverted, Set mask to the level specified by the inverted 'value' property.
        * 'INVERT': Invert, Invert the mask.
        (type: enum in ['VALUE', 'VALUE_INVERSE', 'INVERT'], (optional))
    :type mode: str
    :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        (type: float in [0, 1], (optional))
    :type value: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def mask_lasso_gesture(*args, path=None, mode='VALUE', value=1.0):
    """Add mask within the lasso as you move the brush
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param path: path
        (type: bpy_prop_collection of OperatorMousePath, (optional))
    :type path: bpy_prop_collection
    :param mode: Mode
        * 'VALUE': Value, Set mask to the level specified by the 'value' property.
        * 'VALUE_INVERSE': Value Inverted, Set mask to the level specified by the inverted 'value' property.
        * 'INVERT': Invert, Invert the mask.
        (type: enum in ['VALUE', 'VALUE_INVERSE', 'INVERT'], (optional))
    :type mode: str
    :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        (type: float in [0, 1], (optional))
    :type value: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def project_image(*args, image=''):
    """Project an edited render from the active camera back onto the object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param image: Image
        (type: enum in [], (optional))
    :type image: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def sample_color(*args, location=(0, 0), merged=False, palette=False):
    """Use the mouse to sample a color in the image
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param location: Location
        (type: int array of 2 items in [0, inf], (optional))
    :type location: collections.Sequence[int]
    :param merged: Sample Merged, Sample the output display color
        (type: boolean, (optional))
    :type merged: bool
    :param palette: Add to Palette
        (type: boolean, (optional))
    :type palette: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def texture_paint_toggle(*args):
    """Toggle texture paint mode in 3D view
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vert_select_all(*args, action='TOGGLE'):
    """Change selection for all vertices
    
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


def vert_select_ungrouped(*args, extend=False):
    """Select vertices without a group
    
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


def vertex_color_brightness_contrast(*args, brightness=0.0, contrast=0.0):
    """Adjust vertex color brightness/contrast
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param brightness: Brightness
        (type: float in [-100, 100], (optional))
    :type brightness: float
    :param contrast: Contrast
        (type: float in [-100, 100], (optional))
    :type contrast: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_color_dirt(*args, blur_strength=1.0, blur_iterations=1, clean_angle=3.14159, dirt_angle=0.0, dirt_only=False):
    """Undocumented
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param blur_strength: Blur Strength, Blur strength per iteration
        (type: float in [0.01, 1], (optional))
    :type blur_strength: float
    :param blur_iterations: Blur Iterations, Number of times to blur the colors (higher blurs more)
        (type: int in [0, 40], (optional))
    :type blur_iterations: int
    :param clean_angle: Highlight Angle, Less than 90 limits the angle used in the tonal range
        (type: float in [0, 3.14159], (optional))
    :type clean_angle: float
    :param dirt_angle: Dirt Angle, Less than 90 limits the angle used in the tonal range
        (type: float in [0, 3.14159], (optional))
    :type dirt_angle: float
    :param dirt_only: Dirt Only, Don't calculate cleans for convex areas
        (type: boolean, (optional))
    :type dirt_only: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_color_hsv(*args, h=0.5, s=1.0, v=1.0):
    """Adjust vertex color HSV values
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param h: Hue
        (type: float in [0, 1], (optional))
    :type h: float
    :param s: Saturation
        (type: float in [0, 2], (optional))
    :type s: float
    :param v: Value
        (type: float in [0, 2], (optional))
    :type v: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_color_invert(*args):
    """Invert RGB values
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_color_levels(*args, offset=0.0, gain=1.0):
    """Adjust levels of vertex colors
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param offset: Offset, Value to add to colors
        (type: float in [-1, 1], (optional))
    :type offset: float
    :param gain: Gain, Value to multiply colors by
        (type: float in [0, inf], (optional))
    :type gain: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_color_set(*args):
    """Fill the active vertex color layer with the current paint color
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_color_smooth(*args):
    """Smooth colors across vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_paint(*args, stroke=None, mode='NORMAL'):
    """Paint a stroke in the active vertex color layer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param stroke: Stroke
        (type: bpy_prop_collection of OperatorStrokeElement, (optional))
    :type stroke: bpy_prop_collection
    :param mode: Stroke Mode, Action taken when a paint stroke is made
        * 'NORMAL': Normal, Apply brush normally.
        * 'INVERT': Invert, Invert action of brush for duration of stroke.
        * 'SMOOTH': Smooth, Switch brush to smooth mode for duration of stroke.
        (type: enum in ['NORMAL', 'INVERT', 'SMOOTH'], (optional))
    :type mode: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_paint_toggle(*args):
    """Toggle the vertex paint mode in 3D view
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def weight_from_bones(*args, type='AUTOMATIC'):
    """Set the weights of the groups matching the attached armature's selected bones, using the distance between the vertices and the bones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type, Method to use for assigning weights
        * 'AUTOMATIC': Automatic, Automatic weights from bones.
        * 'ENVELOPES': From Envelopes, Weights from envelopes with user defined radius.
        (type: enum in ['AUTOMATIC', 'ENVELOPES'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def weight_gradient(*args, type='LINEAR', xstart=0, xend=0, ystart=0, yend=0, cursor=1002):
    """Draw a line to apply a weight gradient to selected vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        (type: enum in ['LINEAR', 'RADIAL'], (optional))
    :type type: str
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


def weight_paint(*args, stroke=None, mode='NORMAL'):
    """Paint a stroke in the current vertex group's weights
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param stroke: Stroke
        (type: bpy_prop_collection of OperatorStrokeElement, (optional))
    :type stroke: bpy_prop_collection
    :param mode: Stroke Mode, Action taken when a paint stroke is made
        * 'NORMAL': Normal, Apply brush normally.
        * 'INVERT': Invert, Invert action of brush for duration of stroke.
        * 'SMOOTH': Smooth, Switch brush to smooth mode for duration of stroke.
        (type: enum in ['NORMAL', 'INVERT', 'SMOOTH'], (optional))
    :type mode: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def weight_paint_toggle(*args):
    """Toggle weight paint mode in 3D view
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def weight_sample(*args):
    """Use the mouse to sample a weight in the 3D view
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def weight_sample_group(*args, group='DEFAULT'):
    """Select one of the vertex groups available under current mouse position
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param group: Keying Set, The Keying Set to use
        (type: enum in ['DEFAULT'], (optional))
    :type group: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def weight_set(*args):
    """Fill the active vertex group with the current paint weight
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
