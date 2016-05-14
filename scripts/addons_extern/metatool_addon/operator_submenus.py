import bpy
from bpy import*

######################################################################################################################################################
######------------###################
######  Sub Menu  ###################
######------------###################
######################################################################################################################################################


class AHM(bpy.types.Menu):
    bl_idname = "armature.hide_menu"
    bl_label = "Hide"

    def draw(self, context):
        layout = self.layout

        layout.operator("armature.hide").unselected = False
        layout.operator("armature.hide").unselected = True
        layout.operator("armature.reveal")

bpy.utils.register_class(AHM)


class ViewModeset(bpy.types.Menu):
    bl_idname = "pie_modeset"
    bl_label = "Mode Set"

    def draw(self, context):
        layout = self.layout

        layout.operator_enum("OBJECT_OT_mode_set", "mode")

bpy.utils.register_class(ViewModeset)


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


class CleanDelete(bpy.types.Menu):
    """Clean Up Mesh"""
    bl_label = "Clean Up & Delete Mesh"
    bl_idname = 'mesh.cleandelete'

    def draw(self, context):
        layout = self.layout

        layout.operator("mesh.delete", "Vertices", icon="SNAP_VERTEX").type = "VERT"
        layout.operator("mesh.dissolve_verts")
        layout.operator("mesh.remove_doubles")

        layout.separator()

        layout.operator("mesh.delete", "Edges", icon="SNAP_EDGE").type = "EDGE"
        layout.operator("mesh.dissolve_edges")
        layout.operator("mesh.delete_edgeloop", text="Remove Edge Loop")

        layout.separator()

        layout.operator("mesh.delete", "Faces", icon="SNAP_FACE").type = "FACE"
        layout.operator("mesh.dissolve_faces")
        layout.operator("mesh.delete", "Remove only Faces").type = "ONLY_FACE"

        layout.separator()

        layout.operator("mesh.dissolve_limited", icon="MATCUBE")
        layout.operator("mesh.dissolve_degenerate")
        layout.operator("mesh.delete", "Remove Edge & Faces").type = "EDGE_FACE"

        layout.separator()

        layout.operator("mesh.fill_holes", icon="RETOPO")
        layout.operator("mesh.delete_loose")
        layout.operator("mesh.edge_collapse")
        layout.operator("mesh.vert_connect_nonplanar")

        layout.separator()
        layout.operator("meshlint.select", "Meshlint > Mesh Data")


class ObjClearDelete(bpy.types.Menu):
    """Clear Menu"""
    bl_label = "Clear Menu"
    bl_idname = 'object.cleandelete'

    def draw(self, context):
        layout = self.layout

        layout.operator("object.hide_view_clear", text="Clear Hide")
        layout.operator("material.remove", text="Clear Materials")

        layout.separator()

        layout.menu("VIEW3D_MT_object_clear", text="Clear Location")
        layout.menu("clearparent", text="Clear Parenting")
        layout.menu("cleartrack", text="Clear Tracking")

        layout.separator()

        layout.operator("object.constraints_clear", text="Clear Constraint")
        layout.operator("anim.keyframe_clear_v3d", text="Clear Keyframe")
        layout.operator("object.game_property_clear")


# Menus Origin  #######-------------------------------------------------------
# Menus Origin  #######-------------------------------------------------------

class OriginSetupMenu_obm(bpy.types.Menu):
    bl_label = "Origin Setup Menu"
    bl_idname = "originsetupmenu_obm"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.label("Origin to...", icon="LAYER_ACTIVE")

        layout.operator("object.origin_set", text="to Geometry").type = 'ORIGIN_GEOMETRY'
        layout.operator("object.origin_set", text="to 3D Cursor").type = 'ORIGIN_CURSOR'
        layout.operator("object.origin_set", text="to Center of Mass").type = 'ORIGIN_CENTER_OF_MASS'

        layout.separator()

        layout.operator("object.origin_set", text="Geometry to Origin").type = 'GEOMETRY_ORIGIN'

        layout.separator()

        layout.label("Boundbox Bottom", icon="LAYER_ACTIVE")

        layout.operator("object.pivotobottom_edm", "to Editmode")
        layout.operator("object.pivotobottom_obm", "to Objectmode")


bpy.utils.register_class(OriginSetupMenu_obm)


class OriginSetupMenu_edm(bpy.types.Menu):
    bl_label = "Origin Setup Menu"
    bl_idname = "originsetupmenu_edm"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.label("Origin to Selected", icon="RESTRICT_SELECT_OFF")

        layout.operator("object.originedm", "to Editmode")
        layout.operator("object.originobm", "to Objectmode")

        layout.separator()

        layout.label("Boundbox Bottom", icon="LAYER_ACTIVE")

        layout.operator("object.pivotobottom_edm", "to Editmode")
        layout.operator("object.pivotobottom_obm", "to Objectmode")

bpy.utils.register_class(OriginSetupMenu_edm)


class OriginSetupMenu_all_edm(bpy.types.Menu):
    bl_label = "Origin Setup Menu"
    bl_idname = "originsetupmenu_alledm"

    def draw(self, context):
        layout = self.layout

        layout.label("Set Origin to Selected", icon="LAYER_ACTIVE")

        layout.operator("object.originedm", "to Editmode")
        layout.operator("object.originobm", "to Objectmode")

bpy.utils.register_class(OriginSetupMenu_all_edm)


class VIEW3D_select_obm(bpy.types.Menu):
    bl_label = "Select"
    bl_idname = "select.obm"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.select_all").action = 'TOGGLE'
        layout.operator("object.select_all", text="Inverse").action = 'INVERT'
        layout.operator("object.select_random", text="Random")
        layout.operator("object.select_mirror", text="Mirror")
        layout.operator("object.select_by_layer", text="Select All by Layer")
        layout.operator_menu_enum("object.select_by_type", "type", text="Select All by Type...")
        layout.operator("object.select_camera", text="Select Camera")

        layout.separator()

        layout.operator_menu_enum("object.select_grouped", "type", text="Grouped")
        layout.operator_menu_enum("object.select_linked", "type", text="Linked")
        layout.operator("object.select_pattern", text="Select Pattern...")

bpy.utils.register_class(VIEW3D_select_obm)


class VIEW3D_META_File(bpy.types.Menu):
    bl_label = "File Menu"
    bl_idname = "meta_file"

    def draw(self, context):
        layout = self.layout
        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator_context = 'INVOKE_AREA'

        layout.menu("INFO_MT_file_open_recent", icon='OPEN_RECENT')
        layout.operator("wm.revert_mainfile", icon='FILE_REFRESH')
        layout.operator("wm.recover_last_session", icon='RECOVER_LAST')
        layout.operator("wm.recover_auto_save", text="Recover Auto Save...", icon='RECOVER_AUTO')

        layout.separator()

        layout.operator_context = 'EXEC_AREA' if context.blend_data.is_saved else 'INVOKE_AREA'
        layout.operator("wm.save_mainfile", text="Save", icon='FILE_TICK')

        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.save_as_mainfile", text="Save As...", icon='SAVE_AS')
        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.save_as_mainfile", text="Save Copy...", icon='SAVE_COPY').copy = True

        layout.separator()

        layout.operator("screen.userpref_show", text="User Preferences...", icon='PREFERENCES')

        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.save_homefile", icon='SAVE_PREFS')
        layout.operator("wm.read_factory_settings", icon='LOAD_FACTORY')

        layout.separator()

        layout.menu("INFO_MT_file_previews")

        layout.separator()

        layout.menu("INFO_MT_game")
        layout.menu("INFO_MT_window")
        layout.menu("INFO_MT_help")

        layout.separator()

        layout.operator_context = 'EXEC_AREA'
        if bpy.data.is_dirty and context.user_preferences.view.use_quit_dialog:
            layout.operator_context = 'INVOKE_SCREEN'  # quit dialog
        layout.operator("wm.quit_blender", text="Quit", icon='QUIT')


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
