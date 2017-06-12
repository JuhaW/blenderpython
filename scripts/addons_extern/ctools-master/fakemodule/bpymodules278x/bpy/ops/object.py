def add(*args, radius=1.0, type='EMPTY', view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Add an object to the scene
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param radius: Radius
        (type: float in [0, inf], (optional))
    :type radius: float
    :param type: Type
        (type: enum in ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE', 'LATTICE', 'EMPTY', 'CAMERA', 'LAMP', 'SPEAKER'], (optional))
    :type type: str
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def add_named(*args, linked=False, name=""):
    """Add named object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param linked: Linked, Duplicate object but not object data, linking to the original data
        (type: boolean, (optional))
    :type linked: bool
    :param name: Name, Object name to add
        (type: str, (optional, never None))
    :type name: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def align(*args, bb_quality=True, align_mode='OPT_2', relative_to='OPT_4', align_axis={}):
    """Align Objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param bb_quality: High Quality, Enables high quality calculation of the bounding box for perfect results on complex shape meshes with rotation/scale (Slow)
        (type: boolean, (optional))
    :type bb_quality: bool
    :param align_mode: Align Mode:, Side of object to use for alignment
        (type: enum in ['OPT_1', 'OPT_2', 'OPT_3'], (optional))
    :type align_mode: str
    :param relative_to: Relative To:, Reference location to align to
        * 'OPT_1': Scene Origin, Use the Scene Origin as the position for the selected objects to align to.
        * 'OPT_2': 3D Cursor, Use the 3D cursor as the position for the selected objects to align to.
        * 'OPT_3': Selection, Use the selected objects as the position for the selected objects to align to.
        * 'OPT_4': Active, Use the active object as the position for the selected objects to align to.
        (type: enum in ['OPT_1', 'OPT_2', 'OPT_3', 'OPT_4'], (optional))
    :type relative_to: str
    :param align_axis: Align, Align to axis
        (type: enum set in {'X', 'Y', 'Z'}, (optional))
    :type align_axis: enum set in {'X', 'Y', 'Z'}
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def anim_transforms_to_deltas(*args):
    """Convert object animation for normal transforms to delta transforms
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def armature_add(*args, radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Add an armature object to the scene
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param radius: Radius
        (type: float in [0, inf], (optional))
    :type radius: float
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def bake(*args, type='COMBINED', pass_filter={}, filepath="", width=512, height=512, margin=16, use_selected_to_active=False, cage_extrusion=0.0, cage_object="", normal_space='TANGENT', normal_r='POS_X', normal_g='POS_Y', normal_b='POS_Z', save_mode='INTERNAL', use_clear=False, use_cage=False, use_split_materials=False, use_automatic_name=False, uv_layer=""):
    """Bake image textures of selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type, Type of pass to bake, some of them may not be supported by the current render engine
        (type: enum in ['COMBINED', 'AO', 'SHADOW', 'NORMAL', 'UV', 'EMIT', 'ENVIRONMENT', 'DIFFUSE', 'GLOSSY', 'TRANSMISSION', 'SUBSURFACE'], (optional))
    :type type: str
    :param pass_filter: Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes
        (type: enum set in {'NONE', 'AO', 'EMIT', 'DIRECT', 'INDIRECT', 'COLOR', 'DIFFUSE', 'GLOSSY', 'TRANSMISSION', 'SUBSURFACE'}, (optional))
    :type pass_filter: enum set in {'NONE', 'AO', 'EMIT', 'DIRECT', 'INDIRECT', 'COLOR', 'DIFFUSE', 'GLOSSY', 'TRANSMISSION', 'SUBSURFACE'}
    :param filepath: File Path, Image filepath to use when saving externally
        (type: str, (optional, never None))
    :type filepath: str
    :param width: Width, Horizontal dimension of the baking map (external only)
        (type: int in [1, inf], (optional))
    :type width: int
    :param height: Height, Vertical dimension of the baking map (external only)
        (type: int in [1, inf], (optional))
    :type height: int
    :param margin: Margin, Extends the baked result as a post process filter
        (type: int in [0, inf], (optional))
    :type margin: int
    :param use_selected_to_active: Selected to Active, Bake shading on the surface of selected objects to the active object
        (type: boolean, (optional))
    :type use_selected_to_active: bool
    :param cage_extrusion: Cage Extrusion, Distance to use for the inward ray cast when using selected to active
        (type: float in [0, inf], (optional))
    :type cage_extrusion: float
    :param cage_object: Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion
        (type: str, (optional, never None))
    :type cage_object: str
    :param normal_space: Normal Space, Choose normal space for baking
        * 'OBJECT': Object, Bake the normals in object space.
        * 'TANGENT': Tangent, Bake the normals in tangent space.
        (type: enum in ['OBJECT', 'TANGENT'], (optional))
    :type normal_space: str
    :param normal_r: R, Axis to bake in red channel
        (type: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], (optional))
    :type normal_r: str
    :param normal_g: G, Axis to bake in green channel
        (type: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], (optional))
    :type normal_g: str
    :param normal_b: B, Axis to bake in blue channel
        (type: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], (optional))
    :type normal_b: str
    :param save_mode: Save Mode, Choose how to save the baking map
        * 'INTERNAL': Internal, Save the baking map in an internal image data-block.
        * 'EXTERNAL': External, Save the baking map in an external file.
        (type: enum in ['INTERNAL', 'EXTERNAL'], (optional))
    :type save_mode: str
    :param use_clear: Clear, Clear Images before baking (only for internal saving)
        (type: boolean, (optional))
    :type use_clear: bool
    :param use_cage: Cage, Cast rays to active object from a cage
        (type: boolean, (optional))
    :type use_cage: bool
    :param use_split_materials: Split Materials, Split baked maps per material, using material name in output file (external only)
        (type: boolean, (optional))
    :type use_split_materials: bool
    :param use_automatic_name: Automatic Name, Automatically name the output file with the pass type
        (type: boolean, (optional))
    :type use_automatic_name: bool
    :param uv_layer: UV Layer, UV layer to override active
        (type: str, (optional, never None))
    :type uv_layer: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def bake_image(*args):
    """Bake image textures of selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def camera_add(*args, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Add a camera object to the scene
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def constraint_add(*args, type=''):
    """Add a constraint to the active object
    
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
    """Add a constraint to the active object, with target (where applicable) set to the selected Objects/Bones
    
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
    """Clear all the constraints for the active Object only
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def constraints_copy(*args):
    """Copy constraints to other selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def convert(*args, target='MESH', keep_original=False):
    """Convert selected objects to another type
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param target: Target, Type of object to convert to
        (type: enum in ['CURVE', 'MESH'], (optional))
    :type target: str
    :param keep_original: Keep Original, Keep original objects instead of replacing them
        (type: boolean, (optional))
    :type keep_original: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def correctivesmooth_bind(*args, modifier=""):
    """Bind base pose in Corrective Smooth modifier
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def data_transfer(*args, use_reverse_transfer=False, use_freeze=False, data_type='', use_create=True, vert_mapping='NEAREST', edge_mapping='NEAREST', loop_mapping='NEAREST_POLYNOR', poly_mapping='NEAREST', use_auto_transform=False, use_object_transform=True, use_max_distance=False, max_distance=1.0, ray_radius=0.0, islands_precision=0.1, layers_select_src='ACTIVE', layers_select_dst='ACTIVE', mix_mode='REPLACE', mix_factor=1.0):
    """Transfer data layer(s) (weights, edge sharp, ...) from active to selected meshes
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_reverse_transfer: Reverse Transfer, Transfer from selected objects to active one
        (type: boolean, (optional))
    :type use_reverse_transfer: bool
    :param use_freeze: Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry
        (type: boolean, (optional))
    :type use_freeze: bool
    :param data_type: Data Type, Which data to transfer
        * 'VGROUP_WEIGHTS': Vertex Group(s), Transfer active or all vertex groups.
        * 'BEVEL_WEIGHT_VERT': Bevel Weight, Transfer bevel weights.
        * 'SHARP_EDGE': Sharp, Transfer sharp mark.
        * 'SEAM': UV Seam, Transfer UV seam mark.
        * 'CREASE': Subsurf Crease, Transfer crease values.
        * 'BEVEL_WEIGHT_EDGE': Bevel Weight, Transfer bevel weights.
        * 'FREESTYLE_EDGE': Freestyle Mark, Transfer Freestyle edge mark.
        * 'CUSTOM_NORMAL': Custom Normals, Transfer custom normals.
        * 'VCOL': VCol, Vertex (face corners) colors.
        * 'UV': UVs, Transfer UV layers.
        * 'SMOOTH': Smooth, Transfer flat/smooth mark.
        * 'FREESTYLE_FACE': Freestyle Mark, Transfer Freestyle face mark.
        (type: enum in ['VGROUP_WEIGHTS', 'BEVEL_WEIGHT_VERT', 'SHARP_EDGE', 'SEAM', 'CREASE', 'BEVEL_WEIGHT_EDGE', 'FREESTYLE_EDGE', 'CUSTOM_NORMAL', 'VCOL', 'UV', 'SMOOTH', 'FREESTYLE_FACE'], (optional))
    :type data_type: str
    :param use_create: Create Data, Add data layers on destination meshes if needed
        (type: boolean, (optional))
    :type use_create: bool
    :param vert_mapping: Vertex Mapping, Method used to map source vertices to destination ones
        * 'TOPOLOGY': Topology, Copy from identical topology meshes.
        * 'NEAREST': Nearest vertex, Copy from closest vertex.
        * 'EDGE_NEAREST': Nearest Edge Vertex, Copy from closest vertex of closest edge.
        * 'EDGEINTERP_NEAREST': Nearest Edge Interpolated, Copy from interpolated values of vertices from closest point on closest edge.
        * 'POLY_NEAREST': Nearest Face Vertex, Copy from closest vertex of closest face.
        * 'POLYINTERP_NEAREST': Nearest Face Interpolated, Copy from interpolated values of vertices from closest point on closest face.
        * 'POLYINTERP_VNORPROJ': Projected Face Interpolated, Copy from interpolated values of vertices from point on closest face hit by normal-projection.
        (type: enum in ['TOPOLOGY', 'NEAREST', 'EDGE_NEAREST', 'EDGEINTERP_NEAREST', 'POLY_NEAREST', 'POLYINTERP_NEAREST', 'POLYINTERP_VNORPROJ'], (optional))
    :type vert_mapping: str
    :param edge_mapping: Edge Mapping, Method used to map source edges to destination ones
        * 'TOPOLOGY': Topology, Copy from identical topology meshes.
        * 'VERT_NEAREST': Nearest Vertices, Copy from most similar edge (edge which vertices are the closest of destination edge's ones).
        * 'NEAREST': Nearest Edge, Copy from closest edge (using midpoints).
        * 'POLY_NEAREST': Nearest Face Edge, Copy from closest edge of closest face (using midpoints).
        * 'EDGEINTERP_VNORPROJ': Projected Edge Interpolated, Interpolate all source edges hit by the projection of destination one along its own normal (from vertices).
        (type: enum in ['TOPOLOGY', 'VERT_NEAREST', 'NEAREST', 'POLY_NEAREST', 'EDGEINTERP_VNORPROJ'], (optional))
    :type edge_mapping: str
    :param loop_mapping: Face Corner Mapping, Method used to map source faces' corners to destination ones
        * 'TOPOLOGY': Topology, Copy from identical topology meshes.
        * 'NEAREST_NORMAL': Nearest Corner And Best Matching Normal, Copy from nearest corner which has the best matching normal.
        * 'NEAREST_POLYNOR': Nearest Corner And Best Matching Face Normal, Copy from nearest corner which has the face with the best matching normal to destination corner's face one.
        * 'NEAREST_POLY': Nearest Corner Of Nearest Face, Copy from nearest corner of nearest polygon.
        * 'POLYINTERP_NEAREST': Nearest Face Interpolated, Copy from interpolated corners of the nearest source polygon.
        * 'POLYINTERP_LNORPROJ': Projected Face Interpolated, Copy from interpolated corners of the source polygon hit by corner normal projection.
        (type: enum in ['TOPOLOGY', 'NEAREST_NORMAL', 'NEAREST_POLYNOR', 'NEAREST_POLY', 'POLYINTERP_NEAREST', 'POLYINTERP_LNORPROJ'], (optional))
    :type loop_mapping: str
    :param poly_mapping: Face Mapping, Method used to map source faces to destination ones
        * 'TOPOLOGY': Topology, Copy from identical topology meshes.
        * 'NEAREST': Nearest Face, Copy from nearest polygon (using center points).
        * 'NORMAL': Best Normal-Matching, Copy from source polygon which normal is the closest to destination one.
        * 'POLYINTERP_PNORPROJ': Projected Face Interpolated, Interpolate all source polygons intersected by the projection of destination one along its own normal.
        (type: enum in ['TOPOLOGY', 'NEAREST', 'NORMAL', 'POLYINTERP_PNORPROJ'], (optional))
    :type poly_mapping: str
    :param use_auto_transform: Auto Transform, Automatically compute transformation to get the best possible match between source and destination meshes (WARNING: results will never be as good as manual matching of objects)
        (type: boolean, (optional))
    :type use_auto_transform: bool
    :param use_object_transform: Object Transform, Evaluate source and destination meshes in global space
        (type: boolean, (optional))
    :type use_object_transform: bool
    :param use_max_distance: Only Neighbor Geometry, Source elements must be closer than given distance from destination one
        (type: boolean, (optional))
    :type use_max_distance: bool
    :param max_distance: Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings
        (type: float in [0, inf], (optional))
    :type max_distance: float
    :param ray_radius: Ray Radius, 'Width' of rays (especially useful when raycasting against vertices or edges)
        (type: float in [0, inf], (optional))
    :type ray_radius: float
    :param islands_precision: Islands Precision, Factor controlling precision of islands handling (the higher, the better the results)
        (type: float in [0, 10], (optional))
    :type islands_precision: float
    :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types
        * 'ACTIVE': Active Layer, Only transfer active data layer.
        * 'ALL': All Layers, Transfer all data layers.
        * 'BONE_SELECT': Selected Pose Bones, Transfer all vertex groups used by selected pose bones.
        * 'BONE_DEFORM': Deform Pose Bones, Transfer all vertex groups used by deform bones.
        (type: enum in ['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM'], (optional))
    :type layers_select_src: str
    :param layers_select_dst: Destination Layers Matching, How to match source and destination layers
        * 'ACTIVE': Active Layer, Affect active data layer of all targets.
        * 'NAME': By Name, Match target data layers to affect by name.
        * 'INDEX': By Order, Match target data layers to affect by order (indices).
        (type: enum in ['ACTIVE', 'NAME', 'INDEX'], (optional))
    :type layers_select_dst: str
    :param mix_mode: Mix Mode, How to affect destination elements with source values
        * 'REPLACE': Replace, Overwrite all elements' data.
        * 'ABOVE_THRESHOLD': Above Threshold, Only replace destination elements where data is above given threshold (exact behavior depends on data type).
        * 'BELOW_THRESHOLD': Below Threshold, Only replace destination elements where data is below given threshold (exact behavior depends on data type).
        * 'MIX': Mix, Mix source value into destination one, using given threshold as factor.
        * 'ADD': Add, Add source value to destination one, using given threshold as factor.
        * 'SUB': Subtract, Subtract source value to destination one, using given threshold as factor.
        * 'MUL': Multiply, Multiply source value to destination one, using given threshold as factor.
        (type: enum in ['REPLACE', 'ABOVE_THRESHOLD', 'BELOW_THRESHOLD', 'MIX', 'ADD', 'SUB', 'MUL'], (optional))
    :type mix_mode: str
    :param mix_factor: Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode)
        (type: float in [0, 1], (optional))
    :type mix_factor: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def datalayout_transfer(*args, modifier="", data_type='', use_delete=False, layers_select_src='ACTIVE', layers_select_dst='ACTIVE'):
    """Transfer layout of data layer(s) from active to selected meshes
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :param data_type: Data Type, Which data to transfer
        * 'VGROUP_WEIGHTS': Vertex Group(s), Transfer active or all vertex groups.
        * 'BEVEL_WEIGHT_VERT': Bevel Weight, Transfer bevel weights.
        * 'SHARP_EDGE': Sharp, Transfer sharp mark.
        * 'SEAM': UV Seam, Transfer UV seam mark.
        * 'CREASE': Subsurf Crease, Transfer crease values.
        * 'BEVEL_WEIGHT_EDGE': Bevel Weight, Transfer bevel weights.
        * 'FREESTYLE_EDGE': Freestyle Mark, Transfer Freestyle edge mark.
        * 'CUSTOM_NORMAL': Custom Normals, Transfer custom normals.
        * 'VCOL': VCol, Vertex (face corners) colors.
        * 'UV': UVs, Transfer UV layers.
        * 'SMOOTH': Smooth, Transfer flat/smooth mark.
        * 'FREESTYLE_FACE': Freestyle Mark, Transfer Freestyle face mark.
        (type: enum in ['VGROUP_WEIGHTS', 'BEVEL_WEIGHT_VERT', 'SHARP_EDGE', 'SEAM', 'CREASE', 'BEVEL_WEIGHT_EDGE', 'FREESTYLE_EDGE', 'CUSTOM_NORMAL', 'VCOL', 'UV', 'SMOOTH', 'FREESTYLE_FACE'], (optional))
    :type data_type: str
    :param use_delete: Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source
        (type: boolean, (optional))
    :type use_delete: bool
    :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types
        * 'ACTIVE': Active Layer, Only transfer active data layer.
        * 'ALL': All Layers, Transfer all data layers.
        * 'BONE_SELECT': Selected Pose Bones, Transfer all vertex groups used by selected pose bones.
        * 'BONE_DEFORM': Deform Pose Bones, Transfer all vertex groups used by deform bones.
        (type: enum in ['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM'], (optional))
    :type layers_select_src: str
    :param layers_select_dst: Destination Layers Matching, How to match source and destination layers
        * 'ACTIVE': Active Layer, Affect active data layer of all targets.
        * 'NAME': By Name, Match target data layers to affect by name.
        * 'INDEX': By Order, Match target data layers to affect by order (indices).
        (type: enum in ['ACTIVE', 'NAME', 'INDEX'], (optional))
    :type layers_select_dst: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def delete(*args, use_global=False):
    """Delete selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_global: Delete Globally, Remove object from all scenes
        (type: boolean, (optional))
    :type use_global: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def drop_named_image(*args, filepath="", relative_path=True, name="", view_align=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Add an empty image type to scene with data
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param filepath: Filepath, Path to image file
        (type: str, (optional, never None))
    :type filepath: str
    :param relative_path: Relative Path, Select the file relative to the blend file
        (type: boolean, (optional))
    :type relative_path: bool
    :param name: Name, Image name to assign
        (type: str, (optional, never None))
    :type name: str
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def drop_named_material(*args, name="Material"):
    """Undocumented
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param name: Name, Material name to assign
        (type: str, (optional, never None))
    :type name: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def dupli_offset_from_cursor(*args):
    """Set offset used for DupliGroup based on cursor position
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def duplicate(*args, linked=False, mode='TRANSLATION'):
    """Duplicate selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param linked: Linked, Duplicate object but not object data, linking to the original data
        (type: boolean, (optional))
    :type linked: bool
    :param mode: Mode
        (type: enum in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional))
    :type mode: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def duplicate_move(*args, OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None):
    """Duplicate selected objects and move them
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
        (type: OBJECT_OT_duplicate, (optional))
    :type OBJECT_OT_duplicate: OBJECT_OT_duplicate
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
        (type: TRANSFORM_OT_translate, (optional))
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def duplicate_move_linked(*args, OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None):
    """Duplicate selected objects and move them
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
        (type: OBJECT_OT_duplicate, (optional))
    :type OBJECT_OT_duplicate: OBJECT_OT_duplicate
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
        (type: TRANSFORM_OT_translate, (optional))
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def duplicates_make_real(*args, use_base_parent=False, use_hierarchy=False):
    """Make dupli objects attached to this object real
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_base_parent: Parent, Parent newly created objects to the original duplicator
        (type: boolean, (optional))
    :type use_base_parent: bool
    :param use_hierarchy: Keep Hierarchy, Maintain parent child relationships
        (type: boolean, (optional))
    :type use_hierarchy: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def editmode_toggle(*args):
    """Toggle object's editmode
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def effector_add(*args, type='FORCE', radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Add an empty object with a physics effector to the scene
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        (type: enum in ['FORCE', 'WIND', 'VORTEX', 'MAGNET', 'HARMONIC', 'CHARGE', 'LENNARDJ', 'TEXTURE', 'GUIDE', 'BOID', 'TURBULENCE', 'DRAG', 'SMOKE'], (optional))
    :type type: str
    :param radius: Radius
        (type: float in [0, inf], (optional))
    :type radius: float
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def empty_add(*args, type='PLAIN_AXES', radius=1.0, view_align=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Add an empty object to the scene
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        (type: enum in ['PLAIN_AXES', 'ARROWS', 'SINGLE_ARROW', 'CIRCLE', 'CUBE', 'SPHERE', 'CONE', 'IMAGE'], (optional))
    :type type: str
    :param radius: Radius
        (type: float in [0, inf], (optional))
    :type radius: float
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def explode_refresh(*args, modifier=""):
    """Refresh data in the Explode modifier
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def forcefield_toggle(*args):
    """Toggle object's force field
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def game_physics_copy(*args):
    """Copy game physics properties to other selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def game_property_clear(*args):
    """Remove all game properties from all selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def game_property_copy(*args, operation='COPY', property=''):
    """Copy/merge/replace a game property from active object to all selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param operation: Operation
        (type: enum in ['REPLACE', 'MERGE', 'COPY'], (optional))
    :type operation: str
    :param property: Property, Properties to copy
        (type: enum in [], (optional))
    :type property: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def game_property_move(*args, index=0, direction='UP'):
    """Move game property
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param index: Index, Property index to move
        (type: int in [0, inf], (optional))
    :type index: int
    :param direction: Direction, Direction for moving the property
        (type: enum in ['UP', 'DOWN'], (optional))
    :type direction: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def game_property_new(*args, type='FLOAT', name=""):
    """Create a new property available to the game engine
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type, Type of game property to add
        * 'BOOL': Boolean, Boolean Property.
        * 'INT': Integer, Integer Property.
        * 'FLOAT': Float, Floating-Point Property.
        * 'STRING': String, String Property.
        * 'TIMER': Timer, Timer Property.
        (type: enum in ['BOOL', 'INT', 'FLOAT', 'STRING', 'TIMER'], (optional))
    :type type: str
    :param name: Name, Name of the game property to add
        (type: str, (optional, never None))
    :type name: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def game_property_remove(*args, index=0):
    """Remove game property
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param index: Index, Property index to remove
        (type: int in [0, inf], (optional))
    :type index: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def group_add(*args):
    """Add an object to a new group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def group_instance_add(*args, name="Group", group='', view_align=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Add a dupligroup instance
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param name: Name, Group name to add
        (type: str, (optional, never None))
    :type name: str
    :param group: Group
        (type: enum in [], (optional))
    :type group: str
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def group_link(*args, group=''):
    """Add an object to an existing group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param group: Group
        (type: enum in [], (optional))
    :type group: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def group_remove(*args):
    """Remove the active object from this group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def group_unlink(*args):
    """Unlink the group from all objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def grouped_select(*args):
    """Select all objects in group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hide_render_clear(*args):
    """Reveal the render object by setting the hide render flag
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hide_render_clear_all(*args):
    """Reveal all render objects by setting the hide render flag
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hide_render_set(*args, unselected=False):
    """Hide the render object by setting the hide render flag
    
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


def hide_view_clear(*args):
    """Reveal the object by setting the hide flag
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hide_view_set(*args, unselected=False):
    """Hide the object by setting the hide flag
    
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


def hook_add_newob(*args):
    """Hook selected vertices to a newly created object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hook_add_selob(*args, use_bone=False):
    """Hook selected vertices to the first selected object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_bone: Active Bone, Assign the hook to the hook objects active bone
        (type: boolean, (optional))
    :type use_bone: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hook_assign(*args, modifier=''):
    """Assign the selected vertices to a hook
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Modifier number to assign to
        (type: enum in [], (optional))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hook_recenter(*args, modifier=''):
    """Set hook center to cursor position
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Modifier number to assign to
        (type: enum in [], (optional))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hook_remove(*args, modifier=''):
    """Remove a hook from the active object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Modifier number to remove
        (type: enum in [], (optional))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hook_reset(*args, modifier=''):
    """Recalculate and clear offset transformation
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Modifier number to assign to
        (type: enum in [], (optional))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def hook_select(*args, modifier=''):
    """Select affected vertices on mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Modifier number to remove
        (type: enum in [], (optional))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def isolate_type_render(*args):
    """Hide unselected render objects of same type as active by setting the hide render flag
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def join(*args):
    """Join selected objects into active object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def join_shapes(*args):
    """Merge selected objects to shapes of active object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def join_uvs(*args):
    """Transfer UV Maps from active to selected objects (needs matching geometry)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def lamp_add(*args, type='POINT', radius=1.0, view_align=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Add a lamp object to the scene
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        * 'POINT': Point, Omnidirectional point light source.
        * 'SUN': Sun, Constant direction parallel ray light source.
        * 'SPOT': Spot, Directional cone light source.
        * 'HEMI': Hemi, 180 degree constant light source.
        * 'AREA': Area, Directional area light source.
        (type: enum in ['POINT', 'SUN', 'SPOT', 'HEMI', 'AREA'], (optional))
    :type type: str
    :param radius: Radius
        (type: float in [0, inf], (optional))
    :type radius: float
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def laplaciandeform_bind(*args, modifier=""):
    """Bind mesh to system in laplacian deform modifier
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def location_clear(*args, clear_delta=False):
    """Clear the object's location
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param clear_delta: Clear Delta, Clear delta location in addition to clearing the normal location transform
        (type: boolean, (optional))
    :type clear_delta: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def lod_add(*args):
    """Add a level of detail to this object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def lod_by_name(*args):
    """Add levels of detail to this object based on object names
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def lod_clear_all(*args):
    """Remove all levels of detail from this object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def lod_generate(*args, count=3, target=0.1, package=False):
    """Generate levels of detail using the decimate modifier
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param count: Count
        (type: int in [-inf, inf], (optional))
    :type count: int
    :param target: Target Size
        (type: float in [0, 1], (optional))
    :type target: float
    :param package: Package into Group
        (type: boolean, (optional))
    :type package: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def lod_remove(*args, index=1):
    """Remove a level of detail from this object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param index: Index
        (type: int in [1, inf], (optional))
    :type index: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def logic_bricks_copy(*args):
    """Copy logic bricks to other selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def make_dupli_face(*args):
    """Convert objects into dupli-face instanced
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def make_links_data(*args, type='OBDATA'):
    """Apply active object links to other selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        (type: enum in ['OBDATA', 'MATERIAL', 'ANIMATION', 'GROUPS', 'DUPLIGROUP', 'MODIFIERS', 'FONTS'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def make_links_scene(*args, scene=''):
    """Link selection to another scene
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param scene: Scene
        (type: enum in [], (optional))
    :type scene: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def make_local(*args, type='SELECT_OBJECT'):
    """Make library linked data-blocks local to this file
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        (type: enum in ['SELECT_OBJECT', 'SELECT_OBDATA', 'SELECT_OBDATA_MATERIAL', 'ALL'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def make_single_user(*args, type='SELECTED_OBJECTS', object=False, obdata=False, material=False, texture=False, animation=False):
    """Make linked data local to each object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        (type: enum in ['SELECTED_OBJECTS', 'ALL'], (optional))
    :type type: str
    :param object: Object, Make single user objects
        (type: boolean, (optional))
    :type object: bool
    :param obdata: Object Data, Make single user object data
        (type: boolean, (optional))
    :type obdata: bool
    :param material: Materials, Make materials local to each data-block
        (type: boolean, (optional))
    :type material: bool
    :param texture: Textures, Make textures local to each material (needs 'Materials' to be set too)
        (type: boolean, (optional))
    :type texture: bool
    :param animation: Object Animation, Make animation data local to each object
        (type: boolean, (optional))
    :type animation: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def material_slot_add(*args):
    """Add a new material slot
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def material_slot_assign(*args):
    """Assign active material slot to selection
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def material_slot_copy(*args):
    """Copies materials to other selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def material_slot_deselect(*args):
    """Deselect by active material slot
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def material_slot_move(*args, direction='UP'):
    """Move the active material up/down in the list
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param direction: Direction, Direction to move the active material towards
        (type: enum in ['UP', 'DOWN'], (optional))
    :type direction: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def material_slot_remove(*args):
    """Remove the selected material slot
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def material_slot_select(*args):
    """Select by active material slot
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def meshdeform_bind(*args, modifier=""):
    """Bind mesh to cage in mesh deform modifier
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def metaball_add(*args, type='BALL', radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Add an metaball object to the scene
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Primitive
        (type: enum in ['BALL', 'CAPSULE', 'PLANE', 'ELLIPSOID', 'CUBE'], (optional))
    :type type: str
    :param radius: Radius
        (type: float in [0, inf], (optional))
    :type radius: float
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def mode_set(*args, mode='OBJECT', toggle=False):
    """Sets the object interaction mode
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mode: Mode
        * 'OBJECT': Object Mode.
        * 'EDIT': Edit Mode.
        * 'POSE': Pose Mode.
        * 'SCULPT': Sculpt Mode.
        * 'VERTEX_PAINT': Vertex Paint.
        * 'WEIGHT_PAINT': Weight Paint.
        * 'TEXTURE_PAINT': Texture Paint.
        * 'PARTICLE_EDIT': Particle Edit.
        * 'GPENCIL_EDIT': Edit Strokes, Edit Grease Pencil Strokes.
        (type: enum in ['OBJECT', 'EDIT', 'POSE', 'SCULPT', 'VERTEX_PAINT', 'WEIGHT_PAINT', 'TEXTURE_PAINT', 'PARTICLE_EDIT', 'GPENCIL_EDIT'], (optional))
    :type mode: str
    :param toggle: Toggle
        (type: boolean, (optional))
    :type toggle: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def modifier_add(*args, type='SUBSURF'):
    """Add a modifier to the active object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        * 'DATA_TRANSFER': Data Transfer.
        * 'MESH_CACHE': Mesh Cache.
        * 'MESH_SEQUENCE_CACHE': Mesh Sequence Cache.
        * 'NORMAL_EDIT': Normal Edit.
        * 'UV_PROJECT': UV Project.
        * 'UV_WARP': UV Warp.
        * 'VERTEX_WEIGHT_EDIT': Vertex Weight Edit.
        * 'VERTEX_WEIGHT_MIX': Vertex Weight Mix.
        * 'VERTEX_WEIGHT_PROXIMITY': Vertex Weight Proximity.
        * 'ARRAY': Array.
        * 'BEVEL': Bevel.
        * 'BOOLEAN': Boolean.
        * 'BUILD': Build.
        * 'DECIMATE': Decimate.
        * 'EDGE_SPLIT': Edge Split.
        * 'MASK': Mask.
        * 'MIRROR': Mirror.
        * 'MULTIRES': Multiresolution.
        * 'REMESH': Remesh.
        * 'SCREW': Screw.
        * 'SKIN': Skin.
        * 'SOLIDIFY': Solidify.
        * 'SUBSURF': Subdivision Surface.
        * 'TRIANGULATE': Triangulate.
        * 'WIREFRAME': Wireframe, Generate a wireframe on the edges of a mesh.
        * 'ARMATURE': Armature.
        * 'CAST': Cast.
        * 'CORRECTIVE_SMOOTH': Corrective Smooth.
        * 'CURVE': Curve.
        * 'DISPLACE': Displace.
        * 'HOOK': Hook.
        * 'LAPLACIANSMOOTH': Laplacian Smooth.
        * 'LAPLACIANDEFORM': Laplacian Deform.
        * 'LATTICE': Lattice.
        * 'MESH_DEFORM': Mesh Deform.
        * 'SHRINKWRAP': Shrinkwrap.
        * 'SIMPLE_DEFORM': Simple Deform.
        * 'SMOOTH': Smooth.
        * 'SURFACE_DEFORM': Surface Deform.
        * 'WARP': Warp.
        * 'WAVE': Wave.
        * 'CLOTH': Cloth.
        * 'COLLISION': Collision.
        * 'DYNAMIC_PAINT': Dynamic Paint.
        * 'EXPLODE': Explode.
        * 'FLUID_SIMULATION': Fluid Simulation.
        * 'OCEAN': Ocean.
        * 'PARTICLE_INSTANCE': Particle Instance.
        * 'PARTICLE_SYSTEM': Particle System.
        * 'SMOKE': Smoke.
        * 'SOFT_BODY': Soft Body.
        * 'SURFACE': Surface.
        (type: enum in ['DATA_TRANSFER', 'MESH_CACHE', 'MESH_SEQUENCE_CACHE', 'NORMAL_EDIT', 'UV_PROJECT', 'UV_WARP', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_PROXIMITY', 'ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 'EDGE_SPLIT', 'MASK', 'MIRROR', 'MULTIRES', 'REMESH', 'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'WIREFRAME', 'ARMATURE', 'CAST', 'CORRECTIVE_SMOOTH', 'CURVE', 'DISPLACE', 'HOOK', 'LAPLACIANSMOOTH', 'LAPLACIANDEFORM', 'LATTICE', 'MESH_DEFORM', 'SHRINKWRAP', 'SIMPLE_DEFORM', 'SMOOTH', 'SURFACE_DEFORM', 'WARP', 'WAVE', 'CLOTH', 'COLLISION', 'DYNAMIC_PAINT', 'EXPLODE', 'FLUID_SIMULATION', 'OCEAN', 'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM', 'SMOKE', 'SOFT_BODY', 'SURFACE'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def modifier_apply(*args, apply_as='DATA', modifier=""):
    """Apply modifier and remove from the stack
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param apply_as: Apply as, How to apply the modifier to the geometry
        * 'DATA': Object Data, Apply modifier to the object's data.
        * 'SHAPE': New Shape, Apply deform-only modifier to a new shape on this object.
        (type: enum in ['DATA', 'SHAPE'], (optional))
    :type apply_as: str
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def modifier_convert(*args, modifier=""):
    """Convert particles to a mesh object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def modifier_copy(*args, modifier=""):
    """Duplicate modifier at the same position in the stack
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def modifier_move_down(*args, modifier=""):
    """Move modifier down in the stack
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def modifier_move_up(*args, modifier=""):
    """Move modifier up in the stack
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def modifier_remove(*args, modifier=""):
    """Remove a modifier from the active object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def move_to_layer(*args, layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Move the object to different layers
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def multires_base_apply(*args, modifier=""):
    """Modify the base mesh to conform to the displaced mesh
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def multires_external_pack(*args):
    """Pack displacements from an external file
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def multires_external_save(*args, filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_btx=True, filter_collada=False, filter_alembic=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='FILE_SORT_ALPHA', modifier=""):
    """Save displacements to an external file
    
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
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def multires_higher_levels_delete(*args, modifier=""):
    """Deletes the higher resolution mesh, potential loss of detail
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def multires_reshape(*args, modifier=""):
    """Copy vertex coordinates from other object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def multires_subdivide(*args, modifier=""):
    """Add a new level of subdivision
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def ocean_bake(*args, modifier="", free=False):
    """Bake an image sequence of ocean data
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :param free: Free, Free the bake, rather than generating it
        (type: boolean, (optional))
    :type free: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def origin_clear(*args):
    """Clear the object's origin
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def origin_set(*args, type='GEOMETRY_ORIGIN', center='MEDIAN'):
    """Set the object's origin, by either moving the data, or set to center of data, or use 3D cursor
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        * 'GEOMETRY_ORIGIN': Geometry to Origin, Move object geometry to object origin.
        * 'ORIGIN_GEOMETRY': Origin to Geometry, Move object origin to center of object geometry.
        * 'ORIGIN_CURSOR': Origin to 3D Cursor, Move object origin to position of the 3D cursor.
        * 'ORIGIN_CENTER_OF_MASS': Origin to Center of Mass, Move object origin to the object center of mass (assuming uniform density).
        (type: enum in ['GEOMETRY_ORIGIN', 'ORIGIN_GEOMETRY', 'ORIGIN_CURSOR', 'ORIGIN_CENTER_OF_MASS'], (optional))
    :type type: str
    :param center: Center
        (type: enum in ['MEDIAN', 'BOUNDS'], (optional))
    :type center: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def parent_clear(*args, type='CLEAR'):
    """Clear the object's parenting
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        * 'CLEAR': Clear Parent, Completely clear the parenting relationship, including involved modifiers if any.
        * 'CLEAR_KEEP_TRANSFORM': Clear and Keep Transformation, As 'Clear Parent', but keep the current visual transformations of the object.
        * 'CLEAR_INVERSE': Clear Parent Inverse, Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.
        (type: enum in ['CLEAR', 'CLEAR_KEEP_TRANSFORM', 'CLEAR_INVERSE'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def parent_no_inverse_set(*args):
    """Set the object's parenting without setting the inverse parent correction
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def parent_set(*args, type='OBJECT', xmirror=False, keep_transform=False):
    """Set the object's parenting
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        (type: enum in ['OBJECT', 'ARMATURE', 'ARMATURE_NAME', 'ARMATURE_AUTO', 'ARMATURE_ENVELOPE', 'BONE', 'BONE_RELATIVE', 'CURVE', 'FOLLOW', 'PATH_CONST', 'LATTICE', 'VERTEX', 'VERTEX_TRI'], (optional))
    :type type: str
    :param xmirror: X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation
        (type: boolean, (optional))
    :type xmirror: bool
    :param keep_transform: Keep Transform, Apply transformation before parenting
        (type: boolean, (optional))
    :type keep_transform: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def particle_system_add(*args):
    """Add a particle system
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def particle_system_remove(*args):
    """Remove the selected particle system
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def paths_calculate(*args, start_frame=1, end_frame=250):
    """Calculate motion paths for the selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param start_frame: Start, First frame to calculate object paths on
        (type: int in [-500000, 500000], (optional))
    :type start_frame: int
    :param end_frame: End, Last frame to calculate object paths on
        (type: int in [-500000, 500000], (optional))
    :type end_frame: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def paths_clear(*args, only_selected=False):
    """Clear path caches for all objects, hold Shift key for selected objects only
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param only_selected: Only Selected, Only clear paths from selected objects
        (type: boolean, (optional))
    :type only_selected: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def paths_update(*args):
    """Recalculate paths for selected objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def posemode_toggle(*args):
    """Enable or disable posing/selecting bones
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def proxy_make(*args, object='DEFAULT'):
    """Add empty object to become local replacement data of a library-linked object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param object: Proxy Object, Name of lib-linked/grouped object to make a proxy for
        (type: enum in ['DEFAULT'], (optional))
    :type object: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def quick_explode(*args, style='EXPLODE', amount=100, frame_duration=50, frame_start=1, frame_end=10, velocity=1.0, fade=True):
    """Undocumented
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param style: Explode Style
        (type: enum in ['EXPLODE', 'BLEND'], (optional))
    :type style: str
    :param amount: Amount of pieces
        (type: int in [2, 10000], (optional))
    :type amount: int
    :param frame_duration: Duration
        (type: int in [1, 300000], (optional))
    :type frame_duration: int
    :param frame_start: Start Frame
        (type: int in [1, 300000], (optional))
    :type frame_start: int
    :param frame_end: End Frame
        (type: int in [1, 300000], (optional))
    :type frame_end: int
    :param velocity: Outwards Velocity
        (type: float in [0, 300000], (optional))
    :type velocity: float
    :param fade: Fade, Fade the pieces over time
        (type: boolean, (optional))
    :type fade: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def quick_fluid(*args, style='BASIC', initial_velocity=(0.0, 0.0, 0.0), show_flows=False, start_baking=False):
    """Undocumented
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param style: Fluid Style
        (type: enum in ['INFLOW', 'BASIC'], (optional))
    :type style: str
    :param initial_velocity: Initial Velocity, Initial velocity of the fluid
        (type: float array of 3 items in [-100, 100], (optional))
    :type initial_velocity: collections.Sequence[float]
    :param show_flows: Render Fluid Objects, Keep the fluid objects visible during rendering
        (type: boolean, (optional))
    :type show_flows: bool
    :param start_baking: Start Fluid Bake, Start baking the fluid immediately after creating the domain object
        (type: boolean, (optional))
    :type start_baking: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def quick_fur(*args, density='MEDIUM', view_percentage=10, length=0.1):
    """Undocumented
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param density: Fur Density
        (type: enum in ['LIGHT', 'MEDIUM', 'HEAVY'], (optional))
    :type density: str
    :param view_percentage: View %
        (type: int in [1, 100], (optional))
    :type view_percentage: int
    :param length: Length
        (type: float in [0.001, 100], (optional))
    :type length: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def quick_smoke(*args, style='SMOKE', show_flows=False):
    """Undocumented
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param style: Smoke Style
        (type: enum in ['SMOKE', 'FIRE', 'BOTH'], (optional))
    :type style: str
    :param show_flows: Render Smoke Objects, Keep the smoke objects visible during rendering
        (type: boolean, (optional))
    :type show_flows: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def randomize_transform(*args, random_seed=0, use_delta=False, use_loc=True, loc=(0.0, 0.0, 0.0), use_rot=True, rot=(0.0, 0.0, 0.0), use_scale=True, scale_even=False, scale=(1.0, 1.0, 1.0)):
    """Randomize objects loc/rot/scale
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param random_seed: Random Seed, Seed value for the random generator
        (type: int in [0, 10000], (optional))
    :type random_seed: int
    :param use_delta: Transform Delta, Randomize delta transform values instead of regular transform
        (type: boolean, (optional))
    :type use_delta: bool
    :param use_loc: Randomize Location, Randomize the location values
        (type: boolean, (optional))
    :type use_loc: bool
    :param loc: Location, Maximum distance the objects can spread over each axis
        (type: float array of 3 items in [-100, 100], (optional))
    :type loc: mathutils.Vector
    :param use_rot: Randomize Rotation, Randomize the rotation values
        (type: boolean, (optional))
    :type use_rot: bool
    :param rot: Rotation, Maximum rotation over each axis
        (type: float array of 3 items in [-3.14159, 3.14159], (optional))
    :type rot: mathutils.Euler
    :param use_scale: Randomize Scale, Randomize the scale values
        (type: boolean, (optional))
    :type use_scale: bool
    :param scale_even: Scale Even, Use the same scale value for all axis
        (type: boolean, (optional))
    :type scale_even: bool
    :param scale: Scale, Maximum scale randomization over each axis
        (type: float array of 3 items in [-100, 100], (optional))
    :type scale: mathutils.Vector
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def rotation_clear(*args, clear_delta=False):
    """Clear the object's rotation
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param clear_delta: Clear Delta, Clear delta rotation in addition to clearing the normal rotation transform
        (type: boolean, (optional))
    :type clear_delta: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def scale_clear(*args, clear_delta=False):
    """Clear the object's scale
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param clear_delta: Clear Delta, Clear delta scale in addition to clearing the normal scale transform
        (type: boolean, (optional))
    :type clear_delta: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_all(*args, action='TOGGLE'):
    """Change selection of all visible objects in scene
    
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


def select_by_layer(*args, match='EXACT', extend=False, layers=1):
    """Select all visible objects on a layer
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param match: Match
        (type: enum in ['EXACT', 'SHARED'], (optional))
    :type match: str
    :param extend: Extend, Extend selection instead of deselecting everything first
        (type: boolean, (optional))
    :type extend: bool
    :param layers: Layer
        (type: int in [1, 20], (optional))
    :type layers: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_by_type(*args, extend=False, type='MESH'):
    """Select all visible objects that are of a type
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend selection instead of deselecting everything first
        (type: boolean, (optional))
    :type extend: bool
    :param type: Type
        (type: enum in ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE', 'LATTICE', 'EMPTY', 'CAMERA', 'LAMP', 'SPEAKER'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_camera(*args, extend=False):
    """Select the active camera
    
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


def select_grouped(*args, extend=False, type='CHILDREN_RECURSIVE'):
    """Select all visible objects grouped by various properties
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend selection instead of deselecting everything first
        (type: boolean, (optional))
    :type extend: bool
    :param type: Type
        * 'CHILDREN_RECURSIVE': Children.
        * 'CHILDREN': Immediate Children.
        * 'PARENT': Parent.
        * 'SIBLINGS': Siblings, Shared Parent.
        * 'TYPE': Type, Shared object type.
        * 'LAYER': Layer, Shared layers.
        * 'GROUP': Group, Shared group.
        * 'HOOK': Hook.
        * 'PASS': Pass, Render pass Index.
        * 'COLOR': Color, Object Color.
        * 'PROPERTIES': Properties, Game Properties.
        * 'KEYINGSET': Keying Set, Objects included in active Keying Set.
        * 'LAMP_TYPE': Lamp Type, Matching lamp types.
        (type: enum in ['CHILDREN_RECURSIVE', 'CHILDREN', 'PARENT', 'SIBLINGS', 'TYPE', 'LAYER', 'GROUP', 'HOOK', 'PASS', 'COLOR', 'PROPERTIES', 'KEYINGSET', 'LAMP_TYPE'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_hierarchy(*args, direction='PARENT', extend=False):
    """Select object relative to the active object's position in the hierarchy
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param direction: Direction, Direction to select in the hierarchy
        (type: enum in ['PARENT', 'CHILD'], (optional))
    :type direction: str
    :param extend: Extend, Extend the existing selection
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_less(*args):
    """Deselect objects at the boundaries of parent/child relationships
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_linked(*args, extend=False, type='OBDATA'):
    """Select all visible objects that are linked
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param extend: Extend, Extend selection instead of deselecting everything first
        (type: boolean, (optional))
    :type extend: bool
    :param type: Type
        (type: enum in ['OBDATA', 'MATERIAL', 'TEXTURE', 'DUPGROUP', 'PARTICLE', 'LIBRARY', 'LIBRARY_OBDATA'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_mirror(*args, extend=False):
    """Select the Mirror objects of the selected object eg. L.sword -> R.sword
    
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


def select_more(*args):
    """Select connected parent/child objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_pattern(*args, pattern="*", case_sensitive=False, extend=True):
    """Select objects matching a naming pattern
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param pattern: Pattern, Name filter using '*', '?' and '[abc]' unix style wildcards
        (type: str, (optional, never None))
    :type pattern: str
    :param case_sensitive: Case Sensitive, Do a case sensitive compare
        (type: boolean, (optional))
    :type case_sensitive: bool
    :param extend: Extend, Extend the existing selection
        (type: boolean, (optional))
    :type extend: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_random(*args, percent=50.0, seed=0, action='SELECT'):
    """Set select on random visible objects
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param percent: Percent, Percentage of objects to select randomly
        (type: float in [0, 100], (optional))
    :type percent: float
    :param seed: Random Seed, Seed for the random number generator
        (type: int in [0, inf], (optional))
    :type seed: int
    :param action: Action, Selection action to execute
        * 'SELECT': Select, Select all elements.
        * 'DESELECT': Deselect, Deselect all elements.
        (type: enum in ['SELECT', 'DESELECT'], (optional))
    :type action: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def select_same_group(*args, group=""):
    """Select object in the same group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param group: Group, Name of the group to select
        (type: str, (optional, never None))
    :type group: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shade_flat(*args):
    """Render and display faces uniform, using Face Normals
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shade_smooth(*args):
    """Render and display faces smooth, using interpolated Vertex Normals
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shape_key_add(*args, from_mix=True):
    """Add shape key to the object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param from_mix: From Mix, Create the new shape key from the existing mix of keys
        (type: boolean, (optional))
    :type from_mix: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shape_key_clear(*args):
    """Clear weights for all shape keys
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shape_key_mirror(*args, use_topology=False):
    """Mirror the current shape key along the local X axis
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
        (type: boolean, (optional))
    :type use_topology: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shape_key_move(*args, type='TOP'):
    """Move the active shape key up/down in the list
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        * 'TOP': Top, Top of the list.
        * 'UP': Up.
        * 'DOWN': Down.
        * 'BOTTOM': Bottom, Bottom of the list.
        (type: enum in ['TOP', 'UP', 'DOWN', 'BOTTOM'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shape_key_remove(*args, all=False):
    """Remove shape key from the object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param all: All, Remove all shape keys
        (type: boolean, (optional))
    :type all: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shape_key_retime(*args):
    """Resets the timing for absolute shape keys
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def shape_key_transfer(*args, mode='OFFSET', use_clamp=False):
    """Copy another selected objects active shape to this one by applying the relative offsets
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mode: Transformation Mode, Relative shape positions to the new shape method
        * 'OFFSET': Offset, Apply the relative positional offset.
        * 'RELATIVE_FACE': Relative Face, Calculate relative position (using faces).
        * 'RELATIVE_EDGE': Relative Edge, Calculate relative position (using edges).
        (type: enum in ['OFFSET', 'RELATIVE_FACE', 'RELATIVE_EDGE'], (optional))
    :type mode: str
    :param use_clamp: Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape
        (type: boolean, (optional))
    :type use_clamp: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def skin_armature_create(*args, modifier=""):
    """Create an armature that parallels the skin layout
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def skin_loose_mark_clear(*args, action='MARK'):
    """Mark/clear selected vertices as loose
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param action: Action
        * 'MARK': Mark, Mark selected vertices as loose.
        * 'CLEAR': Clear, Set selected vertices as not loose.
        (type: enum in ['MARK', 'CLEAR'], (optional))
    :type action: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def skin_radii_equalize(*args):
    """Make skin radii of selected vertices equal on each axis
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def skin_root_mark(*args):
    """Mark selected vertices as roots
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def slow_parent_clear(*args):
    """Clear the object's slow parent
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def slow_parent_set(*args):
    """Set the object's slow parent
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def speaker_add(*args, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Add a speaker object to the scene
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def subdivision_set(*args, level=1, relative=False):
    """Sets a Subdivision Surface Level (1-5)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param level: Level
        (type: int in [-100, 100], (optional))
    :type level: int
    :param relative: Relative, Apply the subsurf level as an offset relative to the current level
        (type: boolean, (optional))
    :type relative: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def surfacedeform_bind(*args, modifier=""):
    """Bind mesh to target in surface deform modifier
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param modifier: Modifier, Name of the modifier to edit
        (type: str, (optional, never None))
    :type modifier: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def text_add(*args, radius=1.0, view_align=False, enter_editmode=False, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)):
    """Add a text object to the scene
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param radius: Radius
        (type: float in [0, inf], (optional))
    :type radius: float
    :param view_align: Align to View, Align the new object to the view
        (type: boolean, (optional))
    :type view_align: bool
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        (type: boolean, (optional))
    :type enter_editmode: bool
    :param location: Location, Location for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type location: collections.Sequence[float]
    :param rotation: Rotation, Rotation for the newly added object
        (type: float array of 3 items in [-inf, inf], (optional))
    :type rotation: mathutils.Euler
    :param layers: Layer
        (type: boolean array of 20 items, (optional))
    :type layers: collections.Sequence[bool]
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def track_clear(*args, type='CLEAR'):
    """Clear tracking constraint or flag from object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        (type: enum in ['CLEAR', 'CLEAR_KEEP_TRANSFORM'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def track_set(*args, type='DAMPTRACK'):
    """Make the object track another object, using various methods/constraints
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param type: Type
        (type: enum in ['DAMPTRACK', 'TRACKTO', 'LOCKTRACK'], (optional))
    :type type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def transform_apply(*args, location=False, rotation=False, scale=False):
    """Apply the object's transformation to its data
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param location: Location
        (type: boolean, (optional))
    :type location: bool
    :param rotation: Rotation
        (type: boolean, (optional))
    :type rotation: bool
    :param scale: Scale
        (type: boolean, (optional))
    :type scale: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def transforms_to_deltas(*args, mode='ALL', reset_values=True):
    """Convert normal object transforms to delta transforms, any existing delta transforms will be included as well
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mode: Mode, Which transforms to transfer
        * 'ALL': All Transforms, Transfer location, rotation, and scale transforms.
        * 'LOC': Location, Transfer location transforms only.
        * 'ROT': Rotation, Transfer rotation transforms only.
        * 'SCALE': Scale, Transfer scale transforms only.
        (type: enum in ['ALL', 'LOC', 'ROT', 'SCALE'], (optional))
    :type mode: str
    :param reset_values: Reset Values, Clear transform values after transferring to deltas
        (type: boolean, (optional))
    :type reset_values: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def unlink_data(*args):
    """Undocumented
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_add(*args):
    """Add a new vertex group to the active object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_assign(*args):
    """Assign the selected vertices to the active vertex group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_assign_new(*args):
    """Assign the selected vertices to a new vertex group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_clean(*args, group_select_mode='', limit=0.0, keep_single=False):
    """Remove vertex group assignments which are not required
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param group_select_mode: Subset, Define which subset of Groups shall be used
        (type: enum in [], (optional))
    :type group_select_mode: str
    :param limit: Limit, Remove vertices which weight is below or equal to this limit
        (type: float in [0, 1], (optional))
    :type limit: float
    :param keep_single: Keep Single, Keep verts assigned to at least one group when cleaning
        (type: boolean, (optional))
    :type keep_single: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_copy(*args):
    """Make a copy of the active vertex group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_copy_to_linked(*args):
    """Replace vertex groups of all users of the same geometry data by vertex groups of active object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_copy_to_selected(*args):
    """Replace vertex groups of selected objects by vertex groups of active object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_deselect(*args):
    """Deselect all selected vertices assigned to the active vertex group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_fix(*args, dist=0.0, strength=1.0, accuracy=1.0):
    """Modify the position of selected vertices by changing only their respective groups' weights (this tool may be slow for many vertices)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param dist: Distance, The distance to move to
        (type: float in [-inf, inf], (optional))
    :type dist: float
    :param strength: Strength, The distance moved can be changed by this multiplier
        (type: float in [-2, inf], (optional))
    :type strength: float
    :param accuracy: Change Sensitivity, Change the amount weights are altered with each iteration: lower values are slower
        (type: float in [0.05, inf], (optional))
    :type accuracy: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_invert(*args, group_select_mode='', auto_assign=True, auto_remove=True):
    """Invert active vertex group's weights
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param group_select_mode: Subset, Define which subset of Groups shall be used
        (type: enum in [], (optional))
    :type group_select_mode: str
    :param auto_assign: Add Weights, Add verts from groups that have zero weight before inverting
        (type: boolean, (optional))
    :type auto_assign: bool
    :param auto_remove: Remove Weights, Remove verts from groups that have zero weight after inverting
        (type: boolean, (optional))
    :type auto_remove: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_levels(*args, group_select_mode='', offset=0.0, gain=1.0):
    """Add some offset and multiply with some gain the weights of the active vertex group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param group_select_mode: Subset, Define which subset of Groups shall be used
        (type: enum in [], (optional))
    :type group_select_mode: str
    :param offset: Offset, Value to add to weights
        (type: float in [-1, 1], (optional))
    :type offset: float
    :param gain: Gain, Value to multiply weights by
        (type: float in [0, inf], (optional))
    :type gain: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_limit_total(*args, group_select_mode='', limit=4):
    """Limit deform weights associated with a vertex to a specified number by removing lowest weights
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param group_select_mode: Subset, Define which subset of Groups shall be used
        (type: enum in [], (optional))
    :type group_select_mode: str
    :param limit: Limit, Maximum number of deform weights
        (type: int in [1, 32], (optional))
    :type limit: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_lock(*args, action='TOGGLE'):
    """Change the lock state of all vertex groups of active object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param action: Action, Lock action to execute on vertex groups
        * 'TOGGLE': Toggle, Unlock all vertex groups if there is at least one locked group, lock all in other case.
        * 'LOCK': Lock, Lock all vertex groups.
        * 'UNLOCK': Unlock, Unlock all vertex groups.
        * 'INVERT': Invert, Invert the lock state of all vertex groups.
        (type: enum in ['TOGGLE', 'LOCK', 'UNLOCK', 'INVERT'], (optional))
    :type action: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_mirror(*args, mirror_weights=True, flip_group_names=True, all_groups=False, use_topology=False):
    """Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param mirror_weights: Mirror Weights, Mirror weights
        (type: boolean, (optional))
    :type mirror_weights: bool
    :param flip_group_names: Flip Group Names, Flip vertex group names
        (type: boolean, (optional))
    :type flip_group_names: bool
    :param all_groups: All Groups, Mirror all vertex groups weights
        (type: boolean, (optional))
    :type all_groups: bool
    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
        (type: boolean, (optional))
    :type use_topology: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_move(*args, direction='UP'):
    """Move the active vertex group up/down in the list
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param direction: Direction, Direction to move the active vertex group towards
        (type: enum in ['UP', 'DOWN'], (optional))
    :type direction: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_normalize(*args):
    """Normalize weights of the active vertex group, so that the highest ones are now 1.0
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_normalize_all(*args, group_select_mode='', lock_active=True):
    """Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param group_select_mode: Subset, Define which subset of Groups shall be used
        (type: enum in [], (optional))
    :type group_select_mode: str
    :param lock_active: Lock Active, Keep the values of the active group while normalizing others
        (type: boolean, (optional))
    :type lock_active: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_quantize(*args, group_select_mode='', steps=4):
    """Set weights to a fixed number of steps
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param group_select_mode: Subset, Define which subset of Groups shall be used
        (type: enum in [], (optional))
    :type group_select_mode: str
    :param steps: Steps, Number of steps between 0 and 1
        (type: int in [1, 1000], (optional))
    :type steps: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_remove(*args, all=False, all_unlocked=False):
    """Delete the active or all vertex groups from the active object
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param all: All, Remove all vertex groups
        (type: boolean, (optional))
    :type all: bool
    :param all_unlocked: All Unlocked, Remove all unlocked vertex groups
        (type: boolean, (optional))
    :type all_unlocked: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_remove_from(*args, use_all_groups=False, use_all_verts=False):
    """Remove the selected vertices from active or all vertex group(s)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param use_all_groups: All Groups, Remove from all groups
        (type: boolean, (optional))
    :type use_all_groups: bool
    :param use_all_verts: All Verts, Clear the active group
        (type: boolean, (optional))
    :type use_all_verts: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_select(*args):
    """Select all the vertices assigned to the active vertex group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_set_active(*args, group=''):
    """Set the active vertex group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param group: Group, Vertex group to set as active
        (type: enum in [], (optional))
    :type group: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_smooth(*args, group_select_mode='', factor=0.5, repeat=1, expand=0.0, source='ALL'):
    """Smooth weights for selected vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param group_select_mode: Subset, Define which subset of Groups shall be used
        (type: enum in [], (optional))
    :type group_select_mode: str
    :param factor: Factor
        (type: float in [0, 1], (optional))
    :type factor: float
    :param repeat: Iterations
        (type: int in [1, 10000], (optional))
    :type repeat: int
    :param expand: Expand/Contract, Expand/contract weights
        (type: float in [-1, 1], (optional))
    :type expand: float
    :param source: Source, Vertices to mix with
        (type: enum in ['ALL', 'SELECT', 'DESELECT'], (optional))
    :type source: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_group_sort(*args, sort_type='NAME'):
    """Sort vertex groups
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param sort_type: Sort type, Sort type
        (type: enum in ['NAME', 'BONE_HIERARCHY'], (optional))
    :type sort_type: str
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_parent_set(*args):
    """Parent selected objects to the selected vertices
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_weight_copy(*args):
    """Copy weights from active to selected
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_weight_delete(*args, weight_group=-1):
    """Delete this weight from the vertex (disabled if vertex group is locked)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param weight_group: Weight Index, Index of source weight in active vertex group
        (type: int in [-1, inf], (optional))
    :type weight_group: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_weight_normalize_active_vertex(*args):
    """Normalize active vertex's weights
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_weight_paste(*args, weight_group=-1):
    """Copy this group's weight to other selected verts (disabled if vertex group is locked)
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param weight_group: Weight Index, Index of source weight in active vertex group
        (type: int in [-1, inf], (optional))
    :type weight_group: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def vertex_weight_set_active(*args, weight_group=-1):
    """Set as active vertex group
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :param weight_group: Weight Index, Index of source weight in active vertex group
        (type: int in [-1, inf], (optional))
    :type weight_group: int
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def visual_transform_apply(*args):
    """Apply the object's visual transformation to its data
    
    :param args: (override_context, execution_context, undo)
        override_context (dict)
        execution_context (str) -- enum in ['INVOKE_DEFAULT', 'INVOKE_REGION_WIN', 'INVOKE_REGION_CHANNELS', 'INVOKE_REGION_PREVIEW', 'INVOKE_AREA', 'INVOKE_SCREEN', 'EXEC_DEFAULT', 'EXEC_REGION_WIN', 'EXEC_REGION_CHANNELS', 'EXEC_REGION_PREVIEW', 'EXEC_AREA', 'EXEC_SCREEN']
        undo (bool)
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
