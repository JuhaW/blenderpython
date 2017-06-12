def autodesk_3ds(*args, filepath="", axis_forward='Y', axis_up='Z', filter_glob="*.3ds", constrain_size=10.0, use_image_search=True, use_apply_transform=True):
    """Import from 3DS file format (.3ds)
    
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
    :param constrain_size: Size Constraint, Scale the model by 10 until it reaches the size constraint (0 to disable)
        (type: float in [0, 1000], (optional))
    :type constrain_size: float
    :param use_image_search: Image Search, Search subdirectories for any associated images (Warning, may be slow)
        (type: boolean, (optional))
    :type use_image_search: bool
    :param use_apply_transform: Apply Transform, Workaround for object transformations importing incorrectly
        (type: boolean, (optional))
    :type use_apply_transform: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def fbx(*args, filepath="", axis_forward='-Z', axis_up='Y', directory="", filter_glob="*.fbx", ui_tab='MAIN', use_manual_orientation=False, global_scale=1.0, bake_space_transform=False, use_custom_normals=True, use_image_search=True, use_alpha_decals=False, decal_offset=0.0, use_anim=True, anim_offset=1.0, use_custom_props=True, use_custom_props_enum_as_string=True, ignore_leaf_bones=False, force_connect_children=False, automatic_bone_orientation=False, primary_bone_axis='Y', secondary_bone_axis='X', use_prepost_rot=True):
    """Load a FBX file
    
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
    :param directory: directory
        (type: str, (optional, never None))
    :type directory: str
    :param filter_glob: filter_glob
        (type: str, (optional, never None))
    :type filter_glob: str
    :param ui_tab: ui_tab, Import options categories
        * 'MAIN': Main, Main basic settings.
        * 'ARMATURE': Armatures, Armature-related settings.
        (type: enum in ['MAIN', 'ARMATURE'], (optional))
    :type ui_tab: str
    :param use_manual_orientation: Manual Orientation, Specify orientation and scale, instead of using embedded data in FBX file
        (type: boolean, (optional))
    :type use_manual_orientation: bool
    :param global_scale: Scale
        (type: float in [0.001, 1000], (optional))
    :type global_scale: float
    :param bake_space_transform: !EXPERIMENTAL! Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risks, known broken with armatures/animations)
        (type: boolean, (optional))
    :type bake_space_transform: bool
    :param use_custom_normals: Import Normals, Import custom normals, if available (otherwise Blender will recompute them)
        (type: boolean, (optional))
    :type use_custom_normals: bool
    :param use_image_search: Image Search, Search subdirs for any associated images (WARNING: may be slow)
        (type: boolean, (optional))
    :type use_image_search: bool
    :param use_alpha_decals: Alpha Decals, Treat materials with alpha as decals (no shadow casting)
        (type: boolean, (optional))
    :type use_alpha_decals: bool
    :param decal_offset: Decal Offset, Displace geometry of alpha meshes
        (type: float in [0, 1], (optional))
    :type decal_offset: float
    :param use_anim: Import Animation, Import FBX animation
        (type: boolean, (optional))
    :type use_anim: bool
    :param anim_offset: Animation Offset, Offset to apply to animation during import, in frames
        (type: float in [-inf, inf], (optional))
    :type anim_offset: float
    :param use_custom_props: Import User Properties, Import user properties as custom properties
        (type: boolean, (optional))
    :type use_custom_props: bool
    :param use_custom_props_enum_as_string: Import Enums As Strings, Store enumeration values as strings
        (type: boolean, (optional))
    :type use_custom_props_enum_as_string: bool
    :param ignore_leaf_bones: Ignore Leaf Bones, Ignore the last bone at the end of each chain (used to mark the length of the previous bone)
        (type: boolean, (optional))
    :type ignore_leaf_bones: bool
    :param force_connect_children: Force Connect Children, Force connection of children bones to their parent, even if their computed head/tail positions do not match (can be useful with pure-joints-type armatures)
        (type: boolean, (optional))
    :type force_connect_children: bool
    :param automatic_bone_orientation: Automatic Bone Orientation, Try to align the major bone axis with the bone children
        (type: boolean, (optional))
    :type automatic_bone_orientation: bool
    :param primary_bone_axis: Primary Bone Axis
        (type: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional))
    :type primary_bone_axis: str
    :param secondary_bone_axis: Secondary Bone Axis
        (type: enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional))
    :type secondary_bone_axis: str
    :param use_prepost_rot: Use Pre/Post Rotation, Use pre/post rotation from FBX transform (you may have to disable that in some cases)
        (type: boolean, (optional))
    :type use_prepost_rot: bool
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def obj(*args, filepath="", axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=True, use_groups_as_vgroups=False, use_image_search=True, split_mode='ON', global_clamp_size=0.0):
    """Load a Wavefront OBJ File
    
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
    :param use_edges: Lines, Import lines and faces with 2 verts as edge
        (type: boolean, (optional))
    :type use_edges: bool
    :param use_smooth_groups: Smooth Groups, Surround smooth groups by sharp edges
        (type: boolean, (optional))
    :type use_smooth_groups: bool
    :param use_split_objects: Object, Import OBJ Objects into Blender Objects
        (type: boolean, (optional))
    :type use_split_objects: bool
    :param use_split_groups: Group, Import OBJ Groups into Blender Objects
        (type: boolean, (optional))
    :type use_split_groups: bool
    :param use_groups_as_vgroups: Poly Groups, Import OBJ groups as vertex groups
        (type: boolean, (optional))
    :type use_groups_as_vgroups: bool
    :param use_image_search: Image Search, Search subdirs for any associated images (Warning, may be slow)
        (type: boolean, (optional))
    :type use_image_search: bool
    :param split_mode: Split
        * 'ON': Split, Split geometry, omits unused verts.
        * 'OFF': Keep Vert Order, Keep vertex order from file.
        (type: enum in ['ON', 'OFF'], (optional))
    :type split_mode: str
    :param global_clamp_size: Clamp Size, Clamp bounds under this value (zero to disable)
        (type: float in [0, 1000], (optional))
    :type global_clamp_size: float
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}


def x3d(*args, filepath="", axis_forward='Z', axis_up='Y', filter_glob="*.x3d;*.wrl"):
    """Import an X3D or VRML2 file
    
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
    :return: (type: enum set in {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'})
    :rtype: set[str]
    """
    return {'FINISHED'}
