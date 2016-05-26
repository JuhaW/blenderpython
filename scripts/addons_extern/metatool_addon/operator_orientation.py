import bpy
from bpy import*

######################################################################################################################################################
#######-------------#################
#######  Operators  #################
#######-------------#################
######################################################################################################################################################
# Menus Origin  #######-------------------------------------------------------
# Menus Origin  #######-------------------------------------------------------


class OriginSetup_mode(bpy.types.Menu):
    """Origin: Set to Selection & Set to BBox in Editmode / Objectmode"""
    bl_label = "Origin Setup Menu"
    bl_idname = "originsetup_mode"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.label("to Selected...", icon="RESTRICT_SELECT_OFF")

        layout.operator("object.originedm", "in Editmode")
        layout.operator("object.originobm", "in Objectmode")


bpy.utils.register_class(OriginSetup_mode)


class OriginSetupMenu_edm(bpy.types.Menu):
    """Origin: Set to Selection & Set to BBox in Editmode / Objectmode"""
    bl_label = "Origin Setup Menu"
    bl_idname = "originsetupmenu_edm"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.label("to Selected...", icon="RESTRICT_SELECT_OFF")

        layout.operator("object.originedm", "in Editmode")
        layout.operator("object.originobm", "in Objectmode")

        layout.separator()

        layout.label("to BBox Bottom", icon="BBOX")

        layout.operator("object.pivotobottom_edm", "in Editmode")
        layout.operator("object.pivotobottom_obm", "in Objectmode")

bpy.utils.register_class(OriginSetupMenu_edm)


class OriginSetupMenu_obm(bpy.types.Menu):
    """Origin: Set to BBox in Editmode / Objectmode & Default"""

    bl_label = "Origin Setup Menu"
    bl_idname = "originsetupmenu_obm"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.label("to BBox Bottom...", icon="BBOX")

        layout.operator("object.pivotobottom_edm", "in Editmode")
        layout.operator("object.pivotobottom_obm", "in Objectmode")

        layout.separator()

        layout.label("Origin to...", icon="SPACE3")

        layout.operator("object.origin_set", text="to Geometry").type = 'ORIGIN_GEOMETRY'
        layout.operator("object.origin_set", text="to 3D Cursor").type = 'ORIGIN_CURSOR'
        layout.operator("object.origin_set", text="to Center of Mass").type = 'ORIGIN_CENTER_OF_MASS'

        layout.separator()

        layout.operator("object.origin_set", text="Geometry to Origin").type = 'GEOMETRY_ORIGIN'


bpy.utils.register_class(OriginSetupMenu_obm)


class OriginSetupMenu_edm(bpy.types.Menu):
    """Origin: Set to Selection & Set to BBox in Editmode / Objectmode"""
    bl_label = "Origin Setup Menu"
    bl_idname = "originsetupmenu_edm"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.label("to Selected...", icon="RESTRICT_SELECT_OFF")

        layout.operator("object.originedm", "in Editmode")
        layout.operator("object.originobm", "in Objectmode")

        layout.separator()

        layout.label("to BBox Bottom", icon="BBOX")

        layout.operator("object.pivotobottom_edm", "in Editmode")
        layout.operator("object.pivotobottom_obm", "in Objectmode")

bpy.utils.register_class(OriginSetupMenu_edm)


class OriginSetupMenu_all_edm(bpy.types.Menu):
    """Origin: Set to Selection in Editmode / Objectmode / default"""
    bl_label = "Origin Setup Menu"
    bl_idname = "originsetupmenu_alledm"

    def draw(self, context):
        layout = self.layout

        layout.label("to Selected...", icon="LAYER_ACTIVE")

        layout.operator("object.originedm", "in Editmode")
        layout.operator("object.originobm", "in Objectmode")

bpy.utils.register_class(OriginSetupMenu_all_edm)


# Camera  #######-------------------------------------------------------
# Camera  #######-------------------------------------------------------

class VIEW3D_MTK_CameraView(bpy.types.Menu):
    """Align Camera & View"""
    bl_label = "Align Camera & View"
    bl_idname = "mtk_camview"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.camera_add")

        layout.operator("lookat.it", text="Look @ Obj")
        layout.operator("lookat.cursor", text="Look @ Cursor")

        layout.separator()

        layout.operator("object.build_dolly_rig")
        layout.operator("object.build_crane_rig")

        layout.separator()

        layout.operator("view3d.viewnumpad", text="Active Camera").type = 'CAMERA'
        layout.operator("view3d.object_as_camera")

        layout.operator("view3d.camera_to_view", text="Align Active Camera to View")
        layout.operator("view3d.camera_to_view_selected", text="Align Active Camera to Selected")

        layout.separator()

        layout.operator("view3d.view_selected")
        layout.operator("view3d.view_center_cursor")
        layout.operator("view3d.view_all", text="Center Cursor and View All").center = True

        layout.separator()
        layout.operator("view3d.view_lock_to_active")
        layout.operator("view3d.view_lock_clear")

        layout.separator()
        layout.menu("VIEW3D_MT_view_align_selected")

bpy.utils.register_class(VIEW3D_MTK_CameraView)


# Datablock  #######-------------------------------------------------------
# Datablock  #######-------------------------------------------------------


class VIEW3D_MTK_Datablock(bpy.types.Menu):
    """Clear Scnene & Data"""
    bl_label = "Datablock"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.delete", icon="PANEL_CLOSE")
        layout.operator("ba.delete_scene_obs")

        layout.separator()

        layout.operator("meshlint.select", "Meshlint > Mesh Data")

        layout.separator()

        scn = context.scene
        layout.operator("ba.delete_data_obs")
        layout.prop(scn, "mod_list", "")

        layout.separator()

        layout.operator("material.remove", text="Clear Materials")

        layout.separator()

        layout.menu("VIEW3D_MT_object_clear", text="Clear Location", icon='EMPTY_DATA')

        layout.separator()

        layout.menu("clearparent", text="Clear Parenting", icon='CONSTRAINT')
        layout.menu("cleartrack", text="Clear Tracking")
        layout.operator("object.constraints_clear", text="Clear Constraint")

        layout.separator()
        layout.operator("anim.keyframe_clear_v3d", text="Clear Keyframe", icon='KEY_DEHLT')
        layout.operator("object.game_property_clear")


bpy.utils.register_class(VIEW3D_MTK_Datablock)

# Hook  #######-------------------------------------------------------
# Hook  #######-------------------------------------------------------


class VIEW3D_MTK_Hook(bpy.types.Menu):
    """Hook Vertices Menu..."""
    bl_label = "---Hook---"
    bl_idname = "mtk_vertices_hook"

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        col.label(text="Hook use Modifier")

        layout.operator("object.hook_add_newob", text="New", icon="HOOK")
        layout.operator("object.hook_add_selob", text="to Select").use_bone = False
        layout.operator("object.hook_add_selob", text="to Bone").use_bone = True

        layout.operator("object.hook_select", text="Select")
        layout.operator("object.hook_reset", text="Reset")
        layout.perator("object.hook_recenter", text="Recenter")

bpy.utils.register_class(VIEW3D_MTK_Hook)


# Freeze  #######-------------------------------------------------------
# Freeze  #######-------------------------------------------------------

class VIEW3D_MTK_FreezeAll(bpy.types.Menu):
    """Freeze all by Type"""
    bl_label = "(Un)Freeze"
    bl_idname = "mtk_freezeall"

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        layout.operator("object.mesh_all", text="Mesh", icon="OBJECT_DATAMODE")
        layout.operator("object.lamp_all", text="Lampe", icon="LAMP")
        layout.operator("object.curve_all", text="Curve", icon="OUTLINER_OB_CURVE")
        layout.operator("object.bone_all", text="Bone", icon="BONE_DATA")
        layout.operator("object.particles_all", text="Particle", icon="MOD_PARTICLES")
        layout.operator("object.camera_all", text="Camera", icon="OUTLINER_DATA_CAMERA")

bpy.utils.register_class(VIEW3D_MTK_FreezeAll)


# Menus Snap to  #######-------------------------------------------------------
# Menus Snap to  #######-------------------------------------------------------

class SnaptoCursor(bpy.types.Menu):
    """Snap Cursor to..."""
    bl_label = "Snap to Menu"
    bl_idname = "mtk_snaptocursor"

    def draw(self, context):

        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("view3d.snap_cursor_to_grid", text="Grid")
        layout.operator("view3d.snap_cursor_to_active", text="Active")
        layout.operator("view3d.snap_cursor_to_center", text="Center")
        layout.operator("view3d.snap_cursor_to_selected", text="Selected")

        obj = context
        if obj and obj.mode == "EDIT_MESH":
            layout.operator("view3d.snap_cursor_to_edge_intersection", text="Edge Intersection")

bpy.utils.register_class(SnaptoCursor)


class SnaptoSelect(bpy.types.Menu):
    """Snap Selection to..."""
    bl_label = "Snap to Menu"
    bl_idname = "mtk_snaptoselect"

    def draw(self, context):

        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("view3d.snap_selected_to_grid", text="Grid")
        layout.operator("view3d.snap_selected_to_cursor", text="Cursor")
        layout.operator("view3d.snap_selected_to_cursor", "Cursor (offset)").use_offset = True
        layout.operator("mesh.snapcenteroffset", "Center (offset)")

bpy.utils.register_class(SnaptoSelect)


# Menus Snap  #######-------------------------------------------------------
# Menus Snap  #######-------------------------------------------------------

class SnapMenu(bpy.types.Menu):
    """Snap Menu..."""
    bl_label = "Snap Menu"
    bl_idname = "mtk_snapmenu"

    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        mesh = context.active_object.data

        settings = context.tool_settings
        view = context.space_data
        toolsettings = context.tool_settings

        snap_meta = toolsettings.use_snap

        if snap_meta == False:
            layout.operator("wm.context_toggle", text="Snap on/off", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
        else:
            layout.operator("wm.context_toggle", text="Snap on/off", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"

        if obj and obj.mode == 'EDIT':
            layout.prop(toolsettings, "use_mesh_automerge", text="Auto-Merge", icon='AUTOMERGE_ON')

        layout.separator()

        layout.label("Snap Type", icon="SNAP_INCREMENT")

        layout.operator("snape.increment", "Increment", icon="SNAP_INCREMENT")
        layout.operator("snape.vertex", "Vertex", icon="SNAP_VERTEX")
        layout.operator("snape.edge", "Edge", icon="SNAP_EDGE")
        layout.operator("snape.face", "Face", icon="SNAP_FACE")
        layout.operator("snape.volume", "Volume", icon="SNAP_VOLUME")

        layout.separator()

        layout.label("Snap Target", icon="EDIT")

        layout.operator("snap.closest", "Closest", icon="RIGHTARROW_THIN")
        layout.operator("snap.center", "Center", icon="RIGHTARROW_THIN")
        layout.operator("snap.median", "Median", icon="RIGHTARROW_THIN")
        layout.operator("snap.active", "Active", icon="RIGHTARROW_THIN")

        layout.separator()

        if obj and obj.mode == 'OBJECT':
            layout.prop(toolsettings, "use_snap_align_rotation", text="Snap Normal", icon="SNAP_NORMAL")

        if obj and obj.mode == 'EDIT':
            layout.prop(toolsettings, "use_snap_self", text="Snap Self", icon="ORTHO")
            layout.prop(toolsettings, "use_snap_project", text="Snap Projection", icon="RETOPO")

bpy.utils.register_class(SnapMenu)

#####  Pivot Point  ############################################################################################
#####  Pivot Point  ############################################################################################


class pivotBox(bpy.types.Operator):
    """Set pivot point to Bounding Box"""
    bl_label = "Set pivot point to Bounding Box"
    bl_idname = "view3d.pivot_bounding_box"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'
        return {"FINISHED"}


class pivotCursor(bpy.types.Operator):
    """Set pivot point to 3D Cursor"""
    bl_label = "Set pivot point to 3D Cursor"
    bl_idname = "view3d.pivot_3d_cursor"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.space_data.pivot_point = 'CURSOR'
        return {"FINISHED"}


class pivotMedian(bpy.types.Operator):
    """Set pivot point to Median Point"""
    bl_label = "Set pivot point to Median Point"
    bl_idname = "view3d.pivot_median"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'
        return {"FINISHED"}


class pivotActive(bpy.types.Operator):
    """Set pivot point to Active"""
    bl_label = "Set pivot point to Active"
    bl_idname = "view3d.pivot_active"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
        return {"FINISHED"}


class pivotIndividual(bpy.types.Operator):
    """Set pivot point to Individual"""
    bl_label = "Set pivot point to Individual Point"
    bl_idname = "view3d.pivot_individual"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.space_data.pivot_point = 'INDIVIDUAL_ORIGINS'
        return {"FINISHED"}


class pivotCursor3d(bpy.types.Operator):
    """place the origin between all selected with 3d cursor"""
    bl_label = "Set origin between selected with 3d cursor"
    bl_idname = "view3d.origin_3dcursor"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.space_data.pivot_point = 'CURSOR'

        return {"FINISHED"}


class pivotCursor3d2(bpy.types.Operator):
    """place the origin of the active to cursor with 3d cursor"""
    bl_label = "place the origin to cursor with 3d cursor"
    bl_idname = "view3d.origin_3dcursor2"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.space_data.pivot_point = 'CURSOR'

        return {"FINISHED"}


class pivotCursor3d3(bpy.types.Operator):
    """origin to geometry with median pivot"""
    bl_label = "origin to geometry"
    bl_idname = "view3d.origin_3dcursor3"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'

        return {"FINISHED"}


# Origin  #######-------------------------------------------------------
# Origin  #######-------------------------------------------------------

class loop7(bpy.types.Operator):
    """set origin to selected / objectmode"""
    bl_idname = "object.loops7"
    bl_label = "origin to selected / in objectmode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class loop8(bpy.types.Operator):
    """apply rotation & scale to use Mirror & Face to Face correctly"""
    bl_idname = "object.loops8"
    bl_label = "apply rotation & scale"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

        return {'FINISHED'}


class loop9(bpy.types.Operator):
    """set origin to selected / editmode / tip: change for local rotation"""
    bl_idname = "object.loops9"
    bl_label = "origin to selected in editmode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class OriginObm(bpy.types.Operator):
    """set origin to selected / stay in objectmode"""
    bl_idname = "object.originobm"
    bl_label = "origin to selected / in objectmode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class OriginEdm(bpy.types.Operator):
    """set origin to selected / stay in editmode"""
    bl_idname = "object.originedm"
    bl_label = "origin to selected in editmode"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class OriginBottom_Obm(bpy.types.Operator):
    """only for an object without instance"""
    bl_idname = "object.pivotobottom_obm"
    bl_label = "Origin To Bottom / Obm"

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        o = bpy.context.active_object
        init = 0
        for x in o.data.vertices:
            if init == 0:
                a = x.co.z
                init = 1
            elif x.co.z < a:
                a = x.co.z

        for x in o.data.vertices:
            x.co.z -= a

        o.location.z += a
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


class OriginBottom_Edm(bpy.types.Operator):
    """only for an object without instance"""
    bl_idname = "object.pivotobottom_edm"
    bl_label = "Origin To Bottom / Edm"

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        o = bpy.context.active_object
        init = 0
        for x in o.data.vertices:
            if init == 0:
                a = x.co.z
                init = 1
            elif x.co.z < a:
                a = x.co.z

        for x in o.data.vertices:
            x.co.z -= a

        o.location.z += a
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}


# -------------------------------------------------------
# -------------------------------------------------------

def abs(val):
    if val > 0:
        return val
    return -val


def edgeIntersect(context, operator):
    from mathutils.geometry import intersect_line_line

    obj = context.active_object

    if (obj.type != "MESH"):
        operator.report({'ERROR'}, "Object must be a mesh")
        return None

    edges = []
    mesh = obj.data
    verts = mesh.vertices

    is_editmode = (obj.mode == 'EDIT')
    if is_editmode:
        bpy.ops.object.mode_set(mode='OBJECT')

    for e in mesh.edges:
        if e.select:
            edges.append(e)

            if len(edges) > 2:
                break

    if is_editmode:
        bpy.ops.object.mode_set(mode='EDIT')

    if len(edges) != 2:
        operator.report({'ERROR'},
                        "Operator requires exactly 2 edges to be selected")
        return

    line = intersect_line_line(verts[edges[0].vertices[0]].co,
                               verts[edges[0].vertices[1]].co,
                               verts[edges[1].vertices[0]].co,
                               verts[edges[1].vertices[1]].co)

    if line is None:
        operator.report({'ERROR'}, "Selected edges do not intersect")
        return

    point = line[0].lerp(line[1], 0.5)
    context.scene.cursor_location = obj.matrix_world * point


class VIEW3D_OT_CursorToEdgeIntersection(bpy.types.Operator):
    "Finds the mid-point of the shortest distance between two edges"

    bl_idname = "view3d.snap_cursor_to_edge_intersection"
    bl_label = "Cursor to Edge Intersection"

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj != None and obj.type == 'MESH'

    def execute(self, context):
        edgeIntersect(context, self)
        return {'FINISHED'}


class VIEW3D_OT_CursorToEdgeIntersection(bpy.types.Operator):
    "Finds the mid-point of the shortest distance between two edges"

    bl_idname = "view3d.snap_cursor_to_edge_intersection"
    bl_label = "Cursor to Edge Intersection"

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj != None and obj.type == 'MESH'

    def execute(self, context):
        edgeIntersect(context, self)
        return {'FINISHED'}

# bpy.utils.register_class(VIEW3D_OT_CursorToEdgeIntersection)


#####  Mirror XYZ Global  ############################################################################################
#####  Mirror XYZ Global  ############################################################################################

class loop1(bpy.types.Operator):
    """mirror over X axis / global"""
    bl_idname = "object.loops1"
    bl_label = "mirror selected on X axis"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.mirror(constraint_axis=(True, False, False))

        return {'FINISHED'}


class loop2(bpy.types.Operator):
    """mirror over Y axis / global"""
    bl_idname = "object.loops2"
    bl_label = "mirror selected on Y axis"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.mirror(constraint_axis=(False, True, False))

        return {'FINISHED'}


class loop3(bpy.types.Operator):
    """mirror over Z axis / global"""
    bl_idname = "object.loops3"
    bl_label = "mirror selected on Z axis"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.transform.mirror(constraint_axis=(False, False, True))

        return {'FINISHED'}


#####  Mirror XYZ Local  #########################################################################################
#####  Mirror XYZ Local  #########################################################################################

class loop4(bpy.types.Operator):
    """mirror over X axis / local"""
    bl_idname = "object.loops4"
    bl_label = "mirror selected on X axis > local"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(True, False, False), constraint_orientation='LOCAL')

        return {'FINISHED'}


class loop5(bpy.types.Operator):
    """mirror over Y axis / local"""
    bl_idname = "object.loops5"
    bl_label = "mirror selected on Y axis > local"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(False, True, False), constraint_orientation='LOCAL')

        return {'FINISHED'}


class loop6(bpy.types.Operator):
    """mirror over Z axis / local"""
    bl_idname = "object.loops6"
    bl_label = "mirror selected on Z axis > local"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(False, False, True), constraint_orientation='LOCAL')

        return {'FINISHED'}


#####  Camera & View  #########################################################################################
#####  Camera & View  #########################################################################################

class VIEW3D_CameraView(bpy.types.Menu):
    """Align Camera & View"""
    bl_label = "Align Camera & View"

    def draw(self, context):
        view = context.space_data
        layout = self.layout

        layout.menu("VIEW3D_MT_view_align_selected", "Align View", icon="MANIPUL")

        layout.separator()

        layout.operator("lookat.it", text="Look Y @ Obj")
        layout.operator("lookat.cursor", text="LooK Y @ Cursor")

        layout.separator()

        layout.operator("view3d.viewnumpad", text="Active Camera", icon="CAMERA_DATA").type = 'CAMERA'
        layout.operator("view3d.object_as_camera", text="Active Object as Camera")

        layout.separator()

        layout.operator("view3d.camera_to_view", text="Active Camera to View")
        layout.operator("view3d.camera_to_view_selected", text="Active Camera to Selected")

        layout.separator()

        layout.operator("view3d.view_center_cursor", text="View to Cursor", icon="ZOOM_SELECTED")
        layout.operator("view3d.view_selected", text="View to Selected")
        layout.operator("view3d.view_all", text="View All / Center Cursor").center = True

        layout.separator()

        layout.operator("view3d.view_lock_to_active", icon="NDOF_DOM")
        layout.operator("view3d.view_lock_clear")

        layout.prop(view, "lock_camera")

        layout.separator()

        layout.label(text="View to Object:")
        layout.prop(view, "lock_object", text="")


#####  Camera & View  #########################################################################################
#####  Camera & View  #########################################################################################

class VIEW3D_ALIGNView(bpy.types.Menu):
    """Align View"""
    bl_label = "Align View"

    def draw(self, context):
        layout = self.layout

        layout.operator("view3d.view_center_cursor", text="View to Cursor", icon="ZOOM_SELECTED")
        layout.operator("view3d.view_selected", text="View to Selected")
        layout.operator("view3d.view_all", text="View All / Center Cursor").center = True

        layout.separator()

        layout.operator("view3d.view_lock_to_active", icon="NDOF_DOM")
        layout.operator("view3d.view_lock_clear")

        layout.separator()

        layout.label(text="View to Object:")
        layout.prop(view, "lock_object", text="")

#####  Datablock  #########################################################################################
#####  Datablock  #########################################################################################


class VIEW3D_Datablock(bpy.types.Menu):
    """Copy & Clear Data"""
    bl_label = "Datablock"

    def draw(self, context):
        layout = self.layout

        layout.menu("VIEW_MT_datablock_tools", text="Datablock Tools")
        layout.menu("VIEW3D_MT_copypopup", text="Copy Object Data")
        layout.menu("VIEW3D_MT_posecopypopup", text="Copy Pose Data")
        layout.menu("MESH_MT_CopyFaceSettings", text="Copy Face Settings")


# Menus Add  #######-------------------------------------------------------
# Menus Add  #######-------------------------------------------------------

class VIEW3D_MT_add_menus(bpy.types.Menu):
    bl_label = "Add Menu"

    def draw(self, context):
        self.draw_menus(self.layout, context)

    @staticmethod
    def draw_menus(layout, context):
        obj = context.active_object
        mode_string = context.mode
        edit_object = context.edit_object

        if mode_string == 'OBJECT':
            layout.menu("INFO_MT_add", text="Add")
        elif mode_string == 'EDIT_MESH':
            layout.menu("INFO_MT_mesh_add", text="Add")
        elif mode_string == 'EDIT_CURVE':
            layout.menu("INFO_MT_curve_add", text="Add")
        elif mode_string == 'EDIT_SURFACE':
            layout.menu("INFO_MT_surface_add", text="Add")
        elif mode_string == 'EDIT_METABALL':
            layout.menu("INFO_MT_metaball_add", text="Add")
        elif mode_string == 'EDIT_ARMATURE':
            layout.menu("INFO_MT_edit_armature_add", text="Add")

# bpy.utils.register_class(VIEW3D_MT_add_menus)


# Menus Multi Select  #######-------------------------------------------------------
# Menus Multi Select  #######-------------------------------------------------------

class VIEW3D_MT_edit_multi(bpy.types.Menu):
    bl_label = "Multi Select"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        prop = layout.operator("wm.context_set_value", text="Vertex Select", icon='VERTEXSEL')
        prop.value = "(True, False, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Edge Select", icon='EDGESEL')
        prop.value = "(False, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Face Select", icon='FACESEL')
        prop.value = "(False, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        layout.separator()

        prop = layout.operator("wm.context_set_value", text="Vertex & Edge Select", icon='EDITMODE_HLT')
        prop.value = "(True, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Vertex & Face Select", icon='ORTHO')
        prop.value = "(True, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Edge & Face Select", icon='SNAP_FACE')
        prop.value = "(False, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"
        layout.separator()

        prop = layout.operator("wm.context_set_value", text="Vertex & Edge & Face Select", icon='SNAP_VOLUME')
        prop.value = "(True, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

# bpy.utils.register_class(VIEW3D_MT_edit_multi)


######################################################################################################################################################
############------------############
############  REGISTER  ############
############------------############
######################################################################################################################################################

def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
