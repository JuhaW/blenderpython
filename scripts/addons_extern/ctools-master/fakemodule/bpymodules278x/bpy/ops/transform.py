def bend(*args, value=(0.0), mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, release_confirm=False, use_accurate=False):
    """Bend selected items between the 3D cursor and the mouse
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Angle
        (type: float array of 1 items in [-inf, inf], (optional))
    :type value: collections.Sequence[float]
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        (type: boolean, (optional))
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def create_orientation(*args, name="", use_view=False, use=False, overwrite=False):
    """Create transformation orientation from selection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param name: Name, Name of the new custom orientation
        (type: str, (optional, never None))
    :type name: str
    :param use_view: Use View, Use the current view instead of the active object to create the new orientation
        (type: boolean, (optional))
    :type use_view: bool
    :param use: Use after creation, Select orientation after its creation
        (type: boolean, (optional))
    :type use: bool
    :param overwrite: Overwrite previous, Overwrite previously created orientation with same name
        (type: boolean, (optional))
    :type overwrite: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def delete_orientation(*args):
    """Delete transformation orientation
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def edge_bevelweight(*args, value=0.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False):
    """Change the bevel weight of edges
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Factor
        (type: float in [-1, 1], (optional))
    :type value: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def edge_crease(*args, value=0.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False):
    """Change the crease of edges
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Factor
        (type: float in [-1, 1], (optional))
    :type value: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def edge_slide(*args, value=0.0, single_side=False, use_even=False, flipped=False, use_clamp=True, mirror=False, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), correct_uv=False, release_confirm=False, use_accurate=False):
    """Slide an edge loop along a mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Factor
        (type: float in [-10, 10], (optional))
    :type value: float
    :param single_side: Single Side
        (type: boolean, (optional))
    :type single_side: bool
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
        (type: boolean, (optional))
    :type use_even: bool
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
        (type: boolean, (optional))
    :type flipped: bool
    :param use_clamp: Clamp, Clamp within the edge extents
        (type: boolean, (optional))
    :type use_clamp: bool
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming
        (type: boolean, (optional))
    :type correct_uv: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def mirror(*args, constraint_axis=(False, False, False), constraint_orientation='GLOBAL', proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, gpencil_strokes=False, release_confirm=False, use_accurate=False):
    """Mirror selected items around one or more axes
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param constraint_axis: Constraint Axis
        (type: boolean array of 3 items, (optional))
    :type constraint_axis: collections.Sequence[bool]
    :param constraint_orientation: Orientation, Transformation orientation
        (type: enum in [], (optional))
    :type constraint_orientation: str
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        (type: boolean, (optional))
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def push_pull(*args, value=0.0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False):
    """Push/Pull selected items
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Distance
        (type: float in [-inf, inf], (optional))
    :type value: float
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def resize(*args, value=(1.0, 1.0, 1.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False, use_accurate=False):
    """Scale (resize) selected items
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Vector
        (type: float array of 3 items in [-inf, inf], (optional))
    :type value: mathutils.Vector
    :param constraint_axis: Constraint Axis
        (type: boolean array of 3 items, (optional))
    :type constraint_axis: collections.Sequence[bool]
    :param constraint_orientation: Orientation, Transformation orientation
        (type: enum in [], (optional))
    :type constraint_orientation: str
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        (type: boolean, (optional))
    :type gpencil_strokes: bool
    :param texture_space: Edit Texture Space, Edit Object data texture space
        (type: boolean, (optional))
    :type texture_space: bool
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
        (type: boolean, (optional))
    :type remove_on_cancel: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def rotate(*args, value=0.0, axis=(0.0, 0.0, 0.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, release_confirm=False, use_accurate=False):
    """Rotate selected items
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Angle
        (type: float in [-inf, inf], (optional))
    :type value: float
    :param axis: Axis, The axis around which the transformation occurs
        (type: float array of 3 items in [-inf, inf], (optional))
    :type axis: mathutils.Vector
    :param constraint_axis: Constraint Axis
        (type: boolean array of 3 items, (optional))
    :type constraint_axis: collections.Sequence[bool]
    :param constraint_orientation: Orientation, Transformation orientation
        (type: enum in [], (optional))
    :type constraint_orientation: str
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        (type: boolean, (optional))
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_orientation(*args, orientation='GLOBAL'):
    """Select transformation orientation
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param orientation: Orientation, Transformation orientation
        (type: enum in [], (optional))
    :type orientation: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def seq_slide(*args, value=(0.0, 0.0), snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False):
    """Slide a sequence strip in time
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Vector
        (type: float array of 2 items in [-inf, inf], (optional))
    :type value: collections.Sequence[float]
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shear(*args, value=0.0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, release_confirm=False, use_accurate=False):
    """Shear selected items along the horizontal screen axis
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Offset
        (type: float in [-inf, inf], (optional))
    :type value: float
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        (type: boolean, (optional))
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shrink_fatten(*args, value=0.0, use_even_offset=True, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False):
    """Shrink/fatten selected vertices along normals
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Offset
        (type: float in [-inf, inf], (optional))
    :type value: float
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
        (type: boolean, (optional))
    :type use_even_offset: bool
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def skin_resize(*args, value=(1.0, 1.0, 1.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False):
    """Scale selected vertices' skin radii
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Vector
        (type: float array of 3 items in [-inf, inf], (optional))
    :type value: mathutils.Vector
    :param constraint_axis: Constraint Axis
        (type: boolean array of 3 items, (optional))
    :type constraint_axis: collections.Sequence[bool]
    :param constraint_orientation: Orientation, Transformation orientation
        (type: enum in [], (optional))
    :type constraint_orientation: str
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def tilt(*args, value=0.0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), release_confirm=False, use_accurate=False):
    """Tilt selected control vertices of 3D curve
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Angle
        (type: float in [-inf, inf], (optional))
    :type value: float
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def tosphere(*args, value=0.0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, release_confirm=False, use_accurate=False):
    """Move selected vertices outward in a spherical shape around mesh center
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Factor
        (type: float in [0, 1], (optional))
    :type value: float
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        (type: boolean, (optional))
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def trackball(*args, value=(0.0, 0.0), mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, release_confirm=False, use_accurate=False):
    """Trackball style rotation of selected items
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Angle
        (type: float array of 2 items in [-inf, inf], (optional))
    :type value: collections.Sequence[float]
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        (type: boolean, (optional))
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def transform(*args, mode='TRANSLATION', value=(0.0, 0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, release_confirm=False, use_accurate=False):
    """Transform selected items by mode type
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mode: Mode
        (type: enum in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional))
    :type mode: str
    :param value: Values
        (type: float array of 4 items in [-inf, inf], (optional))
    :type value: mathutils.Vector
    :param axis: Axis, The axis around which the transformation occurs
        (type: float array of 3 items in [-inf, inf], (optional))
    :type axis: mathutils.Vector
    :param constraint_axis: Constraint Axis
        (type: boolean array of 3 items, (optional))
    :type constraint_axis: collections.Sequence[bool]
    :param constraint_orientation: Orientation, Transformation orientation
        (type: enum in [], (optional))
    :type constraint_orientation: str
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        (type: boolean, (optional))
    :type gpencil_strokes: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def translate(*args, value=(0.0, 0.0, 0.0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1.0, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False, use_accurate=False):
    """Translate (move) selected items
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Vector
        (type: float array of 3 items in [-inf, inf], (optional))
    :type value: collections.Sequence[float]
    :param constraint_axis: Constraint Axis
        (type: boolean array of 3 items, (optional))
    :type constraint_axis: collections.Sequence[bool]
    :param constraint_orientation: Orientation, Transformation orientation
        (type: enum in [], (optional))
    :type constraint_orientation: str
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param proportional: Proportional Editing
        * 'DISABLED': Disable, Proportional Editing disabled.
        * 'ENABLED': Enable, Proportional Editing enabled.
        * 'PROJECTED': Projected (2D), Proportional Editing using screen space locations.
        * 'CONNECTED': Connected, Proportional Editing using connected geometry only.
        (type: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional))
    :type proportional: str
    :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode
        * 'SMOOTH': Smooth, Smooth falloff.
        * 'SPHERE': Sphere, Spherical falloff.
        * 'ROOT': Root, Root falloff.
        * 'INVERSE_SQUARE': Inverse Square, Inverse Square falloff.
        * 'SHARP': Sharp, Sharp falloff.
        * 'LINEAR': Linear, Linear falloff.
        * 'CONSTANT': Constant, Constant falloff.
        * 'RANDOM': Random, Random falloff.
        (type: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional))
    :type proportional_edit_falloff: str
    :param proportional_size: Proportional Size
        (type: float in [1e-06, inf], (optional))
    :type proportional_size: float
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        (type: boolean, (optional))
    :type gpencil_strokes: bool
    :param texture_space: Edit Texture Space, Edit Object data texture space
        (type: boolean, (optional))
    :type texture_space: bool
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
        (type: boolean, (optional))
    :type remove_on_cancel: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vert_slide(*args, value=0.0, use_even=False, flipped=False, use_clamp=True, mirror=False, snap=False, snap_target='CLOSEST', snap_point=(0.0, 0.0, 0.0), snap_align=False, snap_normal=(0.0, 0.0, 0.0), correct_uv=False, release_confirm=False, use_accurate=False):
    """Slide a vertex along a mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param value: Factor
        (type: float in [-10, 10], (optional))
    :type value: float
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
        (type: boolean, (optional))
    :type use_even: bool
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
        (type: boolean, (optional))
    :type flipped: bool
    :param use_clamp: Clamp, Clamp within the edge extents
        (type: boolean, (optional))
    :type use_clamp: bool
    :param mirror: Mirror Editing
        (type: boolean, (optional))
    :type mirror: bool
    :param snap: Use Snapping Options
        (type: boolean, (optional))
    :type snap: bool
    :param snap_target: Target
        * 'CLOSEST': Closest, Snap closest point onto target.
        * 'CENTER': Center, Snap center onto target.
        * 'MEDIAN': Median, Snap median onto target.
        * 'ACTIVE': Active, Snap active onto target.
        (type: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional))
    :type snap_target: str
    :param snap_point: Point
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_point: mathutils.Vector
    :param snap_align: Align with Point Normal
        (type: boolean, (optional))
    :type snap_align: bool
    :param snap_normal: Normal
        (type: float array of 3 items in [-inf, inf], (optional))
    :type snap_normal: mathutils.Vector
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming
        (type: boolean, (optional))
    :type correct_uv: bool
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        (type: boolean, (optional))
    :type release_confirm: bool
    :param use_accurate: Accurate, Use accurate transformation
        (type: boolean, (optional))
    :type use_accurate: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_random(*args, offset=0.1, uniform=0.0, normal=0.0, seed=0):
    """Randomize vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param offset: Amount, Distance to offset
        (type: float in [-inf, inf], (optional))
    :type offset: float
    :param uniform: Uniform, Increase for uniform offset distance
        (type: float in [0, 1], (optional))
    :type uniform: float
    :param normal: normal, Align offset direction to normals
        (type: float in [0, 1], (optional))
    :type normal: float
    :param seed: Random Seed, Seed for the random number generator
        (type: int in [0, 10000], (optional))
    :type seed: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_warp(*args, warp_angle=6.28319, offset_angle=0.0, min=-1, max=1.0, viewmat=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), center=(0.0, 0.0, 0.0)):
    """Warp vertices around the cursor
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param warp_angle: Warp Angle, Amount to warp about the cursor
        (type: float in [-inf, inf], (optional))
    :type warp_angle: float
    :param offset_angle: Offset Angle, Angle to use as the basis for warping
        (type: float in [-inf, inf], (optional))
    :type offset_angle: float
    :param min: Min
        (type: float in [-inf, inf], (optional))
    :type min: float
    :param max: Max
        (type: float in [-inf, inf], (optional))
    :type max: float
    :param viewmat: Matrix
        (type: float array of 16 items in [-inf, inf], (optional))
    :type viewmat: mathutils.Matrix
    :param center: Center
        (type: float array of 3 items in [-inf, inf], (optional))
    :type center: collections.Sequence[float]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
