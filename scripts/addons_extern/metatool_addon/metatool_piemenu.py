
#
#### ALL included Scripts ###########################################################################################################
#### ALL included Scripts ###########################################################################################################
#
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****
#
#
#### ALL included Scripts ###########################################################################################################
#### ALL included Scripts ###########################################################################################################


bl_info = {
    "name": "MetaTool Main Pie Menu",
    "author": "mkbreuer",
    "version": (0, 1, 0),
    "blender": (2, 7, 2),
    "location": "View3D > PIE-MENU FOR METATOOL",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "User Interface"}


import bpy
from bpy import *
from bpy.types import Menu
from rna_prop_ui import PropertyPanel
# spawn an edit mode selection pie (run while object is in edit mode to get a valid output)


# create the Buttons in the Main Panel for the Sub Panels

bpy.types.Scene.osc_arrays = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_layer = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_layergroup = bpy.props.BoolProperty(default=False)

bpy.types.Scene.osc_quickpref = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_snapshot = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_relation = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_uvs = bpy.props.BoolProperty(default=False)

bpy.types.Scene.osc_material = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_pathtex = bpy.props.BoolProperty(default=False)

bpy.types.Scene.osc_vfx = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_arewo = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_sniper = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_setup = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_scene = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_grouper = bpy.props.BoolProperty(default=False)

###########################################################################################


class VIEW3D_EditPIE(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "META SPACE"
    bl_idname = "meta.edit_pie"

    def draw(self, context):

        layout = self.layout
        settings = context.tool_settings
        toolsettings = context.tool_settings

        self.scn = context.scene
        scene = context.scene
        view = context.space_data

        ob = context
        obj = context.object
        obj = context.active_object
        obj = bpy.context.scene.objects.active

        #layout.operator_context = 'INVOKE_REGION_WIN'

        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        #pie.operator_enum("mesh.select_mode", "type")


#######  OBJECTMODE  #######  OBJECTMODE  #######  OBJECTMODE  #######  OBJECTMODE  #######  OBJECTMODE  #######  OBJECTMODE  #######

        if ob.mode == 'OBJECT':
            # Object mode

            pie = layout.menu_pie()

# Objectmode
# -#-- PIE-BLOCK ---- 1_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.65

            row = box.row(align=True)
            row.scale_x = 0.9
            row.operator_menu_enum("object.modifier_add", "type", text="Modif", icon="MODIFIER")
            row.operator("object.automirror", text="AutoMirror", icon="MOD_WIREFRAME")

            row = box.row(align=True)
            row.scale_x = 0.8
            row.prop(context.scene, "AutoMirror_threshold", text="")
            row.prop(context.scene, "AutoMirror_axis", text="")
            row.prop(context.scene, "AutoMirror_orientation", text="")

            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_viewport_on", "", icon='RESTRICT_VIEW_OFF')
            row.operator("view3d.display_modifiers_viewport_off", "", icon='VISIBLE_IPO_OFF')
            row.operator("view3d.fullmirror", text="X-Clip")
            union = row.operator("mesh.boolean", "Union      ")
            union.modOp = 'UNION'

            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_delete", "", icon='X')
            row.operator("view3d.display_modifiers_apply", "", icon='FILE_TICK')
            row.operator("view3d.fullmirrory", text="Y-Clip")
            intersect = row.operator("mesh.boolean", "Intersect")
            intersect.modOp = 'INTERSECT'

            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_expand", "", icon='DISCLOSURE_TRI_DOWN_VEC')
            row.operator("view3d.display_modifiers_collapse", "", icon='DISCLOSURE_TRI_RIGHT_VEC')
            row.operator("view3d.fullmirrorz", text="Z-Clip")
            difference = row.operator("mesh.boolean", "Difference")
            difference.modOp = 'DIFFERENCE'

            row = box.row(align=True)
            row.scale_x = 1.5

            row.menu("htk_booltool", text="BoolTool", icon='GROUP')
            obj = context.active_object
            if obj:
                obj_type = obj.type

                if obj_type in {'MESH'}:
                    row.operator("retopo.latticeapply", text="E-Lattice", icon="OUTLINER_DATA_LATTICE")


# Objectmode
# -#-- PIE-BLOCK ---- 2_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.95

            row = box.row(align=True)
            row.scale_x = 1.7
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")

            row = box.row(align=True)
            row.scale_x = 1.7
            row.operator("snape.increment", "", icon="SNAP_INCREMENT")
            row.operator("snape.vertex", "", icon="SNAP_VERTEX")
            row.operator("snape.edge", "", icon="SNAP_EDGE")
            row.operator("snape.face", "", icon="SNAP_FACE")
            row.operator("snape.volume", "", icon="SNAP_VOLUME")

            row = box.row(align=True)
            row.scale_x = 1.3
            toolsettings = context.tool_settings

            row.operator("wm.context_toggle", text="", icon='MANIPUL').data_path = "space_data.show_manipulator"
            row.menu("htk_pivotorient", "Orientation", icon="EMPTY_DATA")

            row.prop(toolsettings, "use_snap_align_rotation", text="", icon="SNAP_NORMAL")

            row = box.row(align=True)
            row.scale_x = 1.3

            snap_meta = toolsettings.use_snap
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"
            row.menu("htk_snaptarget", "Snap Target", icon="SNAP_ON")
            row.prop(toolsettings, "use_snap_project", text="", icon="RETOPO")

            row = box.row(align=True)
            toolsettings = context.tool_settings
            row.prop(toolsettings, "use_proportional_edit_objects", "Prop.", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True)
            row.operator("view3d.ruler", text="Ruler")  # , icon="NOCURVE")

            row = box.row(align=True)
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho")


# Objectmode
# -#-- PIE-BLOCK ---- 3_Bottom ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.635

        ####--- LINE 01 ---####
            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.5
            row.operator("vfxtoolbox.freeze_selected_objects", text=" ", icon="RESTRICT_SELECT_ON")
            row.operator("vfxtoolbox.defreeze_all_objects", text=" ", icon="RESTRICT_SELECT_OFF")
            row.operator("object.move_to_layer", text="Move 2 Layer")

            row.label("")
            row.operator("object.join", text="Join        ", icon="FULLSCREEN_EXIT")
            row.operator("object.make_links_data", text="Set Instance").type = "OBDATA"

            row.label("")
            row.operator("wm.read_homefile", text="New      ", icon='NEW')
            row.operator("wm.open_mainfile", text="Open   ", icon='FILE_FOLDER')

        ####--- LINE 02 ---####
            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.5
            row.menu("VIEW3D_MT_object_parent", "Parent          ", icon="LINK_AREA")
            row.menu("VIEW3D_MT_object_group", "Group        ", icon="GROUP")

            row.label("")
            row.operator("object.duplicate_move", "Duplicate")
            row.operator("object.duplicate_move_linked", " Dupli.Linked")

            row.label("")
            row.operator("wm.link", text="Link      ", icon='LINK_BLEND')
            row.operator("wm.append", text="Append", icon='APPEND_BLEND')

        ####--- LINE 03 ---####
            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.5
            row.menu("VIEW3D_MT_object_constraints", icon="CONSTRAINT_DATA")
            row.menu("VIEW3D_MT_object_track", "Track        ", icon="CONSTRAINT")

            row.label("")
            row.operator("object.convert", text="to Mesh ", icon="OUTLINER_DATA_MESH").target = "MESH"
            row.operator("object.convert", text="to Curve   ", icon="OUTLINER_DATA_CURVE").target = "CURVE"

            row.label("")
            row.menu("VIEW3D_MT_make_links", text="M-Links", icon="LINKED")
            row.menu("VIEW3D_MT_make_single_user", "M-Single", icon="UNLINKED")

        ####--- LINE 04 ---####
            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55
            row.operator("ba.delete_data_obs", "Del Orphan ", icon="PANEL_CLOSE")
            row.operator("mft.radialclone", text="Radial Clone", icon='CURSOR')

            row.label("")
            row.operator("object.data_transfer", text="Data Transfer")
            row.operator("object.datalayout_transfer", text="Data Layout")

            row.label("")
            row.menu("INFO_MT_file_import", "Import        ", icon='IMPORT')
            row.menu("INFO_MT_file_export", "Export    ", icon='EXPORT')

        ####--- LINE 05 ---####
            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.5
            row.operator("object.material_slot_remove", text="Del.Mat", icon="ZOOMOUT")

            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "color", text="")
            row.operator("meta.newmaterial", text="ObjColor ", icon='ZOOMIN')

            row.label("")
            row.operator("wm.save_mainfile", text="Save it...     ", icon='FILE_TICK')
            row.operator("wm.save_mainfile", text="Save as...     ", icon='FILE_TICK')

            row.label("")
            row.menu("OBJECT_MT_selected_export", text="Selected     ", icon='EXPORT')
            row.menu("INFO_MT_file_external_data", "External   ", icon='EXTERNAL_DATA')

        ####--- LINE 06 ---####
            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.5
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                if obj.type == 'CURVE':
                    #row.operator("curvetools2.operatorintersectcurves", text = "Intersect Curve  ")
                    row.operator("curve.switch_direction_obm", "Direction  ", icon="ARROW_LEFTRIGHT")
                    row.operator("curvetools2.operatorsweepandmorph", text="Morph")
                    row.operator("curvetools2.operatorbirail", text=" Birail")

                    row.label("")
                    row.operator("curvetools2.operatorloftcurves", text="Loft Curve   ")
                    row.operator("curvetools2.operatorsweepcurves", text="Sweep Curve   ")

                    row.label("")
                    scn = context.scene
                    row.operator("curvetools2.operatorselectioninfo", text="Info")
                    row.prop(context.scene.curvetools, "NrSelectedObjects", text="")
                    row.operator("curvetools2.operatororigintospline0start", text="", icon="PARTICLE_TIP")


# Objectmode
# -#-- PIE-BLOCK ---- 4_Top ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

    ####--- LINE 01 ---####
            """
            row = box.row(align=True)
            row.scale_x = 1.1            
            row.operator("object.camera_add"," ",icon='OUTLINER_OB_CAMERA')   
            row.operator("object.armature_add",text=" ",icon="OUTLINER_OB_ARMATURE")
            row.operator("object.empty_add",text=" ",icon="OUTLINER_OB_EMPTY")      
            row.operator("object.add",text=" ",icon="OUTLINER_OB_LATTICE").type="LATTICE"
            row.operator("object.text_add",text=" ",icon="OUTLINER_OB_FONT")                      
            row.menu("INFO_MT_mesh_add",text=" ",icon='OUTLINER_OB_MESH')                          
            row.menu("INFO_MT_curve_add",text=" ",icon='OUTLINER_OB_CURVE')            
            
            row.menu("expandbutton",icon='PMARKER_SEL',text=" ")           
            
            row.menu("INFO_MT_surface_add",text=" ",icon='OUTLINER_OB_SURFACE')
            row.menu("INFO_MT_metaball_add",text=" ",icon="OUTLINER_OB_META")             
            row.operator("object.lamp_add",icon='OUTLINER_OB_LAMP',text=" ")
            row.operator("object.speaker_add",icon='OUTLINER_OB_SPEAKER',text=" ")                   
            row.operator_menu_enum("object.effector_add", "type", text="        ", icon='SOLO_ON')  
            if len(bpy.data.groups) > 10:
                row.operator_context = 'INVOKE_REGION_WIN'
                row.operator("object.group_instance_add", text="        ", icon='OUTLINER_OB_EMPTY')
            else:
                row.operator_menu_enum("object.group_instance_add", "group", text="        ", icon='OUTLINER_OB_EMPTY')                
            """

        ####--- LINE 02 ---####
            row = box.row(align=True)
            row.alignment = "CENTER"
            row.scale_x = 1.25
            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")
            row.operator("screen.redo_last", text="Settings")

            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")

            row.operator("ed.undo_history", text="History")
            row.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER").use_hide_panels = True

        ####--- LINE 03 ---####
            row = box.row(align=True)
            row.alignment = "CENTER"
            row.scale_x = 1.55

            row.menu("INFO_MT_render", "", icon="SCENE")
            row.menu("VIEW3D_MT_object_animation", "", icon="RENDER_ANIMATION")
            row.menu("VIEW3D_MT_object_game", "", icon="GAME")

            row.operator("view3d.fly", "", icon="NDOF_FLY")
            row.menu("VIEW3D_MT_object_showhide", "", icon="VISIBLE_IPO_ON")
            row.operator("view3d.walk", "", icon="NDOF_TRANS")

            row.menu("meta_file", text="", icon='PREFERENCES')
            row.menu("meta_pieviewmenu", text="", icon="BORDERMOVE")
            row.menu("htk_modifly", text="", icon='MOD_SOFT')

        ####--- LINE 04 ---####
            row = box.row(align=True)
            row.alignment = "CENTER"
            row.scale_x = 1.55

            row.menu("INFO_MT_add", text="", icon='OBJECT_DATA')
            row.operator("view3d.select_border", text="", icon="BORDER_RECT")
            row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")
            row.menu("select.obm", text="", icon="HAND")
            row.operator("view3d.zoom_border", "", icon="ZOOM_PREVIOUS")
            row.operator("view3d.view_all", "", icon="ZOOM_OUT")
            row.menu("cameraviewmenu", text="", icon="CAMERA_DATA")


# Objectmode
# -#-- PIE-BLOCK ---- 5_Top_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1.1

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("object.align_tools", text="Adv. Aligner", icon="ROTATE")
            row = box.row(align=True)
            row.scale_x = 2.1
            row.operator("object.align_objects_scale_all", text="", icon='MAN_SCALE')
            row.operator("object.align_rotation_all", text="", icon='MAN_ROT')
            row.operator("object.align_location_all", text="", icon='MAN_TRANS')

            row = box.row(align=True)
            row.scale_x = 1.2
            row.operator("object.align_location_x", text="X")
            row.operator("object.align_location_y", text="Y")
            row.operator("object.align_location_z", text="Z")

            row = box.row(align=True)
            row.scale_x = 0.85
            row.menu("VIEW3D_MT_transform_object")
            row.menu("VIEW3D_MT_object_clear")
            row.menu("VIEW3D_MT_object_apply")


# Objectmode
# -#-- PIE-BLOCK ---- 6_Top_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1.2

            row = box.row(align=True)
            row.menu("modeset_edit", "Mode  ", icon="EDIT")
            #row.operator("object.editmode_toggle", text="Fast ", icon = "EDIT")
            row.menu("pie.obm_delete", text="Delete    ", icon="PANEL_CLOSE")

            row = box.row(align=True)
            #row.scale_x = 1.6
            row.operator("object.origin_set", text=" ", icon="OBJECT_DATAMODE").type = 'ORIGIN_GEOMETRY'
            row.operator("object.origin_set", text=" ", icon="FORCE_FORCE").type = 'ORIGIN_CURSOR'
            row.menu("originsetupmenu_obm", text="Origin", icon="LAYER_ACTIVE")

            row = box.row(align=True)
            #row.scale_x = 1.6
            row.operator("view3d.snap_cursor_to_center", " ", icon="OUTLINER_DATA_EMPTY")
            row.operator("view3d.snap_cursor_to_active", " ", icon="PMARKER")
            row.menu("mtk_snaptocursor", "Cursor", icon="OUTLINER_DATA_EMPTY")

            row = box.row(align=True)
            #row.scale_x = 1.6
            row.operator("view3d.snap_selected_to_cursor", " ", icon="RESTRICT_SELECT_OFF").use_offset = False
            row.operator("view3d.snap_selected_to_cursor", " ", icon="STICKY_UVS_VERT").use_offset = True
            row.menu("mtk_snaptoselect", "Select", icon="RESTRICT_SELECT_OFF")


# Objectmode
# -#-- PIE-BLOCK ---- 7_Bottom_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1.17

            row = box.row(align=True)
            row.scale_x = 0.675
            row.prop(view, "show_only_render", text="Render")

            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "show_x_ray", text="X-Ray  ")

            row.operator("object.shade_flat", text=" ", icon="SOLID")
            row.operator("object.shade_smooth", text=" ", icon="SMOOTH")
            row.operator("object.wire_all", text=" ", icon='WIRE')

            row = box.row(align=True)
            row.scale_x = 0.7
            row.prop(view, "show_backface_culling", text="Backface")
            row.prop(context.space_data.fx_settings, "use_ssao", "AOccl     ")

            row.operator("view3d.modifiers_subsurf_level_0")
            row.operator("view3d.modifiers_subsurf_level_1")
            row.operator("view3d.modifiers_subsurf_level_2")

            row = box.row(align=True)
            row.scale_x = 0.7
            row.prop(view, "use_matcap")
            row.prop(view, "show_textured_solid", text="Texture ")
            row.operator("view3d.modifiers_subsurf_level_3")
            row.operator("view3d.modifiers_subsurf_level_4")
            row.operator("view3d.modifiers_subsurf_level_5")

            row = box.row(align=True)
            row.scale_x = 0.6
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")

            gs = scene.game_settings
            if view.viewport_shade == 'TEXTURED':
                if scene.render.use_shading_nodes or gs.material_mode != 'GLSL':
                    row.prop(view, "show_textured_shadeless")

            if not scene.render.use_shading_nodes:
                row.prop(gs, "material_mode", text="")

            row.prop(context.space_data, "viewport_shade", "", expand=False)


# Objectmode
# -#-- PIE-BLOCK ---- 8_Bottom_Right ------------------------------------------------

            box = pie.split().box().column()
            box.scale_x = 0.95
            row = box.row(align=True)
            row.operator("object.loops1", text="X  ", icon="ARROW_LEFTRIGHT")
            row.operator("object.loops2", text="Y   ", icon="ARROW_LEFTRIGHT")
            row.operator("object.loops3", text="Z   ", icon="ARROW_LEFTRIGHT")

            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "show_wire", text="Wire")

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("object.distribute_osc", text="DIS", icon="ALIGN")
            row.operator("object.drop_on_active", text="D2A", icon="SNAP_SURFACE")
            row.operator("object.align_by_faces", text="F2F", icon="SNAP_SURFACE")

            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "show_all_edges", "Edges")

            row = box.row(align=True)
            row.prop(view, "show_floor", text="Grid")
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "show_axis", text="Axis")
                row.prop(obj, "show_name", text="Name")

            #row.prop(view, "show_all_objects_origin", "Origin")

            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "show_transparent", text="Trans")

            row = box.row(align=True)
            row.operator("objects.multiedit_enter_operator", "MultiEditEnter")

            sce = bpy.context.scene
            row.prop(sce, "Preserve_Location_Rotation_Scale", "G/R/S")
            row.prop(view, "show_world", "World ")


#######  EDITMODE  #######  EDITMODE  #######  EDITMODE  #######  EDITMODE  #######  EDITMODE  #######  EDITMODE  ######

        if ob.mode == 'EDIT_MESH':
            mesh = context.active_object.data
            # Edit mode

# Editmode
# -#-- PIE-BLOCK ---- 1_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.8

            row = box.row(align=True)
            row.scale_x = 1.4
            row.operator_menu_enum("object.modifier_add", "type", text="", icon="MODIFIER")
            row.operator("object.automirror", text="", icon="MOD_WIREFRAME")
            row.operator("view3d.fullmirror", text="X-Clip")
            row.operator("mesh.vert_connect", text="Connect", icon="MESH_DATA")

            row = box.row(align=True)
            row.scale_x = 1.4
            row.operator("view3d.display_modifiers_delete", "", icon='X')
            row.operator("view3d.display_modifiers_apply_edm", "", icon='FILE_TICK')
            row.operator("view3d.fullmirrory", text="Y-Clip")
            row.operator("mesh.vertex_distribute", text=" Spread ", icon="PARTICLE_POINT")

            row = box.row(align=True)
            row.scale_x = 1.4
            row.operator("view3d.display_modifiers_viewport_off", "", icon='VISIBLE_IPO_OFF')
            row.operator("view3d.display_modifiers_viewport_on", "", icon='RESTRICT_VIEW_OFF')

            row.operator("view3d.fullmirrorz", text="Z-Clip")
            row.operator("mesh.vertex_align", text="Straight", icon="ALIGN")

            row = box.row(align=True)
            row.scale_x = 1.4
            row.operator("view3d.display_modifiers_edit_off", "", icon='SNAP_VERTEX')
            row.operator("view3d.display_modifiers_edit_on", "", icon='EDITMODE_HLT')

            row.operator("object.easy_lattice", text="E-LT.", icon="LATTICE_DATA")
            row.operator("mesh.vertices_smooth", text="Smooth ", icon="SPHERECURVE")

            row = box.row(align=True)
            row.scale_x = 1.4
            row.operator("view3d.display_modifiers_cage_off", "", icon='OUTLINER_DATA_MESH')
            row.operator("view3d.display_modifiers_cage_on", "", icon='OUTLINER_OB_MESH')

            row.operator("mesh.retopomt", text="RMT", icon="ORTHO")
            row.operator("mesh.bridge_edge_loops", "Bridge", icon='SOUND')

            row = box.row(align=True)
            row.scale_x = 0.75
            row.operator("mesh.singleplane_x", text="X-Plane")
            row.operator("mesh.singleplane_y", text="Y-Plane")
            row.operator("mesh.singleplane_z", text="Z-Plane")

            row.operator("mesh.intersect", " ", icon='ZOOMIN').use_separate = False
            row.operator("mesh.intersect", " ", icon='ZOOMOUT').use_separate = True


# Editmode
# -#-- PIE-BLOCK ---- 2_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.95

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("snape.increment", "", icon="SNAP_INCREMENT")
            row.operator("snape.vertex", "", icon="SNAP_VERTEX")
            row.operator("snape.edge", "", icon="SNAP_EDGE")
            row.operator("snape.face", "", icon="SNAP_FACE")
            row.operator("snape.volume", "", icon="SNAP_VOLUME")

            row = box.row(align=True)
            row.scale_x = 1.3
            view = context.space_data
            toolsettings = context.tool_settings
            row.prop(toolsettings, "use_mesh_automerge", text="", icon='AUTOMERGE_ON')
            row.menu("htk_pivotorient", "Orientation", icon="EMPTY_DATA")
            row.prop(toolsettings, "use_snap_self", text="")

            row = box.row(align=True)
            row.scale_x = 1.3

            snap_meta = toolsettings.use_snap
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"
            row.menu("htk_snaptarget", "Snap Target", icon="SNAP_ON")
            row.prop(toolsettings, "use_snap_project", text="")

            row = box.row(align=True)
            toolsettings = context.tool_settings
            row.prop(toolsettings, "proportional_edit", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True)
            row.operator("view3d.ruler", text="Ruler")  # , icon="NOCURVE")
            row.prop(view, "use_occlude_geometry", text="L-2-V")

            row = box.row(align=True)
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho")


# Editmode
# -#-- PIE-BLOCK ---- 3_Bottom ------------------------------------------------
            box = pie.split().box().column()

            row = box.row(align=True)
            box.scale_x = 1.1

        ####--- LINE 01 ---####
            row = box.split()
            row.menu("VIEW3D_MT_edit_mesh_extrude", text="Extrusions")
            row.operator_menu_enum('mesh.offset_edges', 'geometry_mode', text="Offset Edge")

            row.operator("mesh.select_mode", text="Vertices", icon='VERTEXSEL').type = 'VERT'
            row.operator("mesh.select_mode", text="Edge", icon='EDGESEL').type = 'EDGE'
            row.operator("mesh.select_mode", text="Face", icon='FACESEL').type = 'FACE'
            row.operator("mesh.duplicate_move", "Duplicate")
            row.operator("mesh.remove_doubles", "Rem.Double")

        ####--- LINE 02 ---####
            row = box.split()
            row.menu("VIEW3D_MT_edit_mesh_tinycad", "TinyCAD")  # , icon ="GRID")
            row.operator("mesh.unsubdivide", text="Unsubdiv")
            row.operator("mesh.subdivide", text="1").number_cuts = 1
            row.operator("mesh.subdivide", text="2").number_cuts = 2
            row.operator("mesh.subdivide", text="3").number_cuts = 3
            # row.operator("mesh.subdivide",text="4").number_cuts=4
            # row.operator("mesh.subdivide",text="5").number_cuts=5
            # row.operator("mesh.subdivide",text="6").number_cuts=6
            row.operator("mesh.tris_convert_to_quads", text="Quads", icon="OUTLINER_OB_LATTICE")
            row.operator("mesh.quads_convert_to_tris", text="Tris", icon="OUTLINER_OB_MESH")

       ####--- LINE 03 ---####
            row = box.split()

            row.menu("VIEW3D_MT_edit_mesh_edgetools", text="EdgeTools",)
            #row.operator("transform.vert_slide", text="Vert-Slide  ", icon ="PARTICLE_TIP")
            #row.operator("transform.edge_slide", text="Edge-Slide", icon ="PARTICLE_PATH")
            row.operator('object.mextrude', text="MultiExt.")
            row.operator("mesh.fill_grid", "Grid Fill")
            row.operator("mesh.inset", text="Inset Faces")
            row.operator("faceinfillet.op0_id", text="Face Fillet")
            row.operator("mesh.bevel", "Bevel").vertex_only = False
            row.operator("mesh.poke", text="Poke")

        ####--- LINE 04 ---####
            row = box.split()
            row.operator('mesh.edge_roundifier', "EdgeRound")
            row.operator('fillet.op0_id', text='EdgeFillet')
            row.operator("mesh.solidify", "Solidify")
            row.operator("mesh.wireframe", text="FrameWire")
            row.operator("mesh.beautify_fill", "Beautify")
            row.operator("mechappo.create", text="Mechappo")
            row.operator("mesh.extrude_along_curve", text="AlongCurve")

        ####--- LINE 05 ---####
            row = box.split()
            row.operator("mesh.vertices_smooth_laplacian", text="Laplacian")
            row.operator("mesh.make_faces_planar", text="F-Planar")
            row.operator("mesh.spin", "Spin")
            row.operator("mesh.screw", "Screw")
            row.operator("mesh.rot_con", "F-Con-Rotate")
            row.operator("object.vertex_random", "Random")
            row.operator("mesh.separate", text="Separate")

        ####--- LINE 06 ---####
            row = box.split()
            row.operator("mesh.looptools_relax", text="LT-Relax")
            row.operator("mesh.looptools_flatten", text="LT-Flatten")
            row.operator("mesh.looptools_space", text="LT-Space")
            row.operator("mesh.looptools_circle", text="LT-Circle")
            row.operator("mesh.looptools_curve", text="LT-Curve")
            row.operator("mesh.looptools_bridge", text="LT-Loft").loft = True
            row.operator("mesh.looptools_bridge", text="LT-Bridge").loft = False

        ####--- LINE 07 ---####
            row = box.split()
            row.prop(context.tool_settings, "use_grease_pencil_sessions", text="Keep")
            row.operator("gpencil.draw", text="Hand", icon="GREASEPENCIL").mode = 'DRAW'
            row.operator("gpencil.draw", text="Straight", icon="ZOOMOUT").mode = 'DRAW_STRAIGHT'
            row.operator("gpencil.draw", text="Polyline", icon="MESH_DATA").mode = 'DRAW_POLY'
            row.operator("gpencil.draw", text="Eraser", icon="PANEL_CLOSE").mode = 'ERASER'
            row.operator("mesh.normals_make_consistent", text="Recalculate", icon='SNAP_NORMAL')
            row.operator("mesh.flip_normals", text="Flip N.", icon="FILE_REFRESH")

        ####--- LINE 08 ---####
            """
            row = box.split()                                                                                  
            row.operator("mesh.sct_smooth_vertices", text = "Smoothwrap", icon = 'MOD_SMOOTH')   
            row.operator("mesh.sct_shrinkwrap", text = "Shrinkwrap ", icon = 'MOD_SHRINKWRAP')              
            row.operator("gpencil.surfsk_add_surface", text="Bsurface", icon = 'MOD_DYNAMICPAINT') 
            row.operator("mesh.sct_mesh_brush", text = "Brush", icon = 'BRUSH_DATA')             
            row.prop(mesh, "use_auto_smooth","")
            row.prop(mesh, "auto_smooth_angle", text="AutoSmooth")             
            row.menu("VIEW3D_MT_hook", "Hook", icon ="HOOK") 
            row.menu("VIEW3D_MT_vertex_group", "Vertex Groups", icon ="GROUP_VERTEX")  
            """


# Editmode
# -#-- PIE-BLOCK ---- 4_Top ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.85

        ####--- LINE 01 ---####
            row = box.row(align=True)
            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")
            row.operator("screen.redo_last", text="Settings     ")
            row.scale_x = 1.55
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")

            row.operator("ed.undo_history", text=" History ")
            row.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER").use_hide_panels = True

        ####--- LINE 02 ---####
            row = box.row(align=True)

            row.menu("VIEW3D_MT_uv_map", text="UV Unwrap")
            row.operator("mesh.loop_multi_select", text=" Ring  ", icon="COLLAPSEMENU").ring = True
            row.menu("VIEW3D_MT_edit_mesh_showhide", " ", icon="VISIBLE_IPO_ON")

            row.operator("mesh.loop_multi_select", text=" Loop ", icon="ZOOMOUT").ring = False
            row.operator_menu_enum("mesh.sort_elements", "type", text="Sort by    ")

        ####--- LINE 03 ---####
            row = box.row(align=True)

            row.menu("INFO_MT_mesh_add", text="Add Mesh  ")

            row.operator("view3d.select_border", text=" ", icon="BORDER_RECT")
            row.operator("view3d.select_circle", text=" ", icon="BORDER_LASSO")
            row.menu("pie.mt_selection", text=" ", icon="HAND")
            row.operator("view3d.zoom_border", " ", icon="ZOOM_PREVIOUS")
            row.operator("view3d.view_all", " ", icon="ZOOM_OUT")
            row.operator("mesh.select_similar", text="Similar ")


# Editmode
# -#-- PIE-BLOCK ---- 5_Top_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.97

            row = box.row(align=True)
            row.scale_x = 1
            props = row.operator("mesh.knife_tool", text="Knife         ", icon="LINE_DATA")
            props.use_occlude_geometry = True
            props.only_selected = False
            row.operator("mesh.bisect", "Biscet ", icon="SCULPTMODE_HLT")
            row.operator("mesh.snap_utilities_line", text="Snap Line", icon="LINE_DATA")

            row = box.row(align=True)
            row.scale_x = 1
            props = row.operator("mesh.knife_tool", text="K-Select", icon="LINE_DATA")
            props.use_occlude_geometry = False
            props.only_selected = True
            row.operator("object.createhole", text="Hole", icon="RADIOBUT_OFF")
            row.operator("mesh.ext_cut_faces", text="FaceCut", icon="SNAP_EDGE")

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("mesh.knife_project", "K-Project ", icon="LINE_DATA")
            row.operator("mesh.split", icon="MOD_BOOLEAN")
            row.operator("mesh.loopcut_slide", "Loopcut", icon="GRIP")

            row = box.row(align=True)
            row.scale_x = 1
            row.menu("VIEW3D_MT_transform", "Transform   ")
            row.operator("mesh.fill_holes", "Fill Wire")
            row.operator("mesh.merge", text=" Merge  ", icon="AUTOMERGE_ON")


# Editmode
# -#-- PIE-BLOCK ---- 6_Top_Right ------------------------------------------------

            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(align=True)
            row.menu("modeset_object", "Mode      ", icon="EDIT")
            #row.operator("object.editmode_toggle", text="Fast      ", icon = "EDIT")
            row.menu("cleanup", text="Clean    ", icon="PANEL_CLOSE")
            row.menu("mesh.cleanvert", text="Vertices", icon="SNAP_VERTEX")

            row = box.row(align=True)
            #row.scale_x = 1.6
            row.operator("object.loops7", text=" ", icon="OBJECT_DATAMODE")
            row.operator("object.loops9", text=" ", icon="FORCE_FORCE")
            row.menu("originsetupmenu_edm", "Origin ", icon="LAYER_ACTIVE")
            row.menu("mesh.cleanedge", text="Edges", icon="SNAP_EDGE")

            row = box.row(align=True)
            #row.scale_x = 1.6
            row.operator("view3d.snap_cursor_to_center", " ", icon="OUTLINER_DATA_EMPTY")
            row.operator("view3d.snap_cursor_to_active", " ", icon="PMARKER")
            row.menu("mtk_snaptocursor", "Cursor", icon="OUTLINER_DATA_EMPTY")
            row.menu("mesh.cleanface", text="Faces", icon="SNAP_FACE")

            row = box.row(align=True)
            #row.scale_x = 1.6
            row.operator("view3d.snap_selected_to_cursor", " ", icon="RESTRICT_SELECT_OFF").use_offset = False
            row.operator("view3d.snap_selected_to_cursor", " ", icon="STICKY_UVS_VERT").use_offset = True
            row.menu("mtk_snaptoselect", "Select     ", icon="RESTRICT_SELECT_OFF")
            row.menu("mesh.cleandissolve", text="Dissolve", icon="SNAP_VOLUME")


# Editmode
# -#-- PIE-BLOCK ---- 7_Bottom_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1.17
            view = context.space_data
            obj = context.object

            row = box.row(align=True)
            row.scale_x = 0.675
            row.prop(view, "show_occlude_wire", "Hidden")

            row.prop(obj, "show_x_ray", text="X-Ray  ")
            row.operator("mesh.faces_shade_flat", text=" ", icon="MESH_CIRCLE")
            row.operator("mesh.faces_shade_smooth", text=" ", icon="SMOOTH")
            row.operator("object.wire_all", text=" ", icon='WIRE')

            row = box.row(align=True)
            row.scale_x = 0.7
            row.prop(view, "show_backface_culling", text="Backface")
            row.prop(context.space_data.fx_settings, "use_ssao", "AOccl     ")

            row.operator("view3d.modifiers_subsurf_level_0")
            row.operator("view3d.modifiers_subsurf_level_1")
            row.operator("view3d.modifiers_subsurf_level_2")

            row = box.row(align=True)
            row.scale_x = 0.7
            row.prop(view, "use_matcap")
            row.prop(view, "show_textured_solid", text="Texture ")
            row.operator("view3d.modifiers_subsurf_level_3")
            row.operator("view3d.modifiers_subsurf_level_4")
            row.operator("view3d.modifiers_subsurf_level_5")

            row = box.row(align=True)
            row.scale_x = 0.6
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")

            scene = context.scene
            gs = scene.game_settings
            if view.viewport_shade == 'TEXTURED':
                if scene.render.use_shading_nodes or gs.material_mode != 'GLSL':
                    row.prop(view, "show_textured_shadeless")

            if not scene.render.use_shading_nodes:
                row.prop(gs, "material_mode", text="")

            view = context.space_data
            row.prop(context.space_data, "viewport_shade", "", expand=False)


# Editmode
# -#-- PIE-BLOCK ---- 8_Bottom_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.9

            obj = context.object
            obj_type = obj.type
            is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'})
            is_wire = (obj_type in {'CAMERA', 'EMPTY'})
            is_empty_image = (obj_type == 'EMPTY' and obj.empty_draw_type == 'IMAGE')
            is_dupli = (obj.dupli_type != 'NONE')

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("mesh.face_align_x", "X      ", icon='COLOR_RED')
            row.operator("mesh.face_align_y", "Y      ", icon='COLOR_GREEN')
            row.operator("mesh.face_align_z", "Z      ", icon='COLOR_BLUE')
            row.prop(mesh, "show_extra_edge_length", text="E-Length")

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("mesh.face_align_xy", "Xy  ", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy  ", icon='TRIA_UP_BAR')
            row.operator("mesh.face_align_xz", "Zx  ", icon='TRIA_LEFT_BAR')
            row.prop(mesh, "show_extra_edge_angle", text="E-Angle")

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("object.loops1", text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="MZ", icon='ARROW_LEFTRIGHT')
            row.prop(mesh, "show_extra_face_area", text="F-Area")

            row = box.row(align=True)
            row.operator("objects.multiedit_exit_operator", "MultiEditExit")
            sce = bpy.context.scene
            row.prop(sce, "Preserve_Location_Rotation_Scale", "G/R/S  ")
            row.prop(mesh, "show_extra_face_angle", text="F-Angle")

            #row.prop(view, "show_world", "World  ")
            #row.prop(mesh, "show_weight","Weights")
            #row.prop(mesh, "show_edge_seams", text="Seams    ")


#######  CURVEMODE  #######  CURVEMODE  #######  CURVEMODE  #######  CURVEMODE  #######  CURVEMODE  #######  CURVEMODE  #######

        if ob.mode == 'EDIT_CURVE':

            # Curvemode
            # -#-- PIE-BLOCK ---- 1_Left ------------------------------------------------
            box = pie.split().box().column()

            row = box.row(align=True)
            row.scale_x = 0.9
            row.operator("curve.surfsk_reorder_splines", text="Reorder")
            row.operator("curve.spline_type_set", "Spline Type")

            row = box.row(align=True)
            row.scale_x = 0.9
            row.operator("curve.surfsk_first_points", text="First Point")
            row.operator("curve.radius_set", "Radius")

            row = box.row(align=True)
            row.scale_x = 0.9
            row.operator("curve.switch_direction", "Direction")
            row.operator("curve.smooth")

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("object.vertex_random")
            row.operator("curve.extrude_move", text="Extrude")


# Curvemode
# -#-- PIE-BLOCK ---- 2_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.95

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("snape.increment", "", icon="SNAP_INCREMENT")
            row.operator("snape.vertex", "", icon="SNAP_VERTEX")
            row.operator("snape.edge", "", icon="SNAP_EDGE")
            row.operator("snape.face", "", icon="SNAP_FACE")
            row.operator("snape.volume", "", icon="SNAP_VOLUME")

            row = box.row(align=True)
            row.scale_x = 1.3
            view = context.space_data
            toolsettings = context.tool_settings
            row.prop(toolsettings, "use_snap_align_rotation", text="", icon="SNAP_NORMAL")
            row.menu("htk_pivotorient", "Orientation", icon="EMPTY_DATA")
            row.prop(toolsettings, "use_snap_self", text="")

            row = box.row(align=True)
            row.scale_x = 1.3

            snap_meta = toolsettings.use_snap
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"

            row.menu("htk_snaptarget", "Snap Target", icon="SNAP_ON")
            row.prop(toolsettings, "use_snap_project", text="")

            row = box.row(align=True)
            toolsettings = context.tool_settings
            row.prop(toolsettings, "proportional_edit", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True)
            row.operator("view3d.ruler", text="Ruler")  # , icon="NOCURVE")

            row = box.row(align=True)
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho")


# Curvemode
# -#-- PIE-BLOCK ---- 3_Button ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(align=True)
            row.operator("curvetools2.operatorsplinesjoinneighbouring", text="Join")
            row.operator("curve.make_segment", text="Segment")
            row.operator("bpt.bezier_curve_split", text="Split")

            row = box.row(align=True)
            row.prop(context.scene.curvetools, "SplineJoinMode", text="")
            row.operator("curve.separate", "     Separate")

            row = box.row(align=True)
            row.prop(context.scene.curvetools, "SplineJoinDistance", text="")
            row.prop(context.scene.curvetools, "SplineJoinStartEnd", text="only start & end")

            row = box.row(align=True)
            row.operator("curvetools2.operatorsplinesremovezerosegment", text="remove 0-segment splines")

            row = box.row(align=True)
            row.operator("curvetools2.operatorsplinesremoveshort", text="rem. short")
            row.prop(context.scene.curvetools, "SplineRemoveLength", text="")


# Curvemode
# -#-- PIE-BLOCK ---- 4_Top ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.6

            row = box.row(1)
            row.scale_x = 1.55
            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")
            row.operator("screen.redo_last", text="Settings ")
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")
            row.operator("ed.undo_history", text="History")
            row.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER").use_hide_panels = True
            #row.operator("screen.screen_full_area", text = "", icon = "FULLSCREEN_ENTER")

            row = box.row(1)
            row.scale_x = 1.55
            row.operator("curve.select_random", text="Random")
            row.operator("curve.select_nth", text="Checker")
            row.menu("VIEW3D_MT_edit_curve_showhide", "", icon="VISIBLE_IPO_ON")
            row.operator("curve.select_linked", text="Linked ")
            row.operator("curve.select_all", text="Inverse  ").action = 'INVERT'

            row = box.row(1)
            row.scale_x = 1.55
            row.alignment = "CENTER"
            row.operator("object.curv_to_2d", text="2d", icon="CURVE_DATA")
            row.operator("view3d.select_border", text="", icon="BORDER_RECT")
            row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")
            row.menu("INFO_MT_curve_add", "", icon='OUTLINER_OB_CURVE')
            row.operator("view3d.zoom_border", "", icon="ZOOM_PREVIOUS")
            row.operator("view3d.view_all", "", icon="ZOOM_OUT")
            row.operator("object.curv_to_3d", text="3d", icon="CURVE_DATA")

# Curvemode
# -#-- PIE-BLOCK ---- 5_Top_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.85

            row = box.row(align=True)
            row.operator("curve.cyclic_toggle")
            row.operator("curve.normals_make_consistent")

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("curve.handle_type_set", text="Auto").type = 'AUTOMATIC'
            row.operator("curve.handle_type_set", text="Vector").type = 'VECTOR'

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("curve.handle_type_set", text="Align").type = 'ALIGNED'
            row.operator("curve.handle_type_set", text="Free").type = 'FREE_ALIGN'

            row = box.row(align=True)
            row.operator("curvetools2.operatorsplinessetresolution", text="Resolution")
            row.prop(context.scene.curvetools, "SplineResolution", text="")

# Curvemode
# -#-- PIE-BLOCK ---- 6_Top_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.95

            row = box.row(align=True)
            row.operator("object.editmode_toggle", text="Fast", icon="OBJECT_DATAMODE")
            row.operator("curve.delete")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("object.loops9", "", icon="EDITMODE_HLT")
            row.operator("object.loops7", "", icon="OBJECT_DATAMODE")
            row.menu("originsetup_mode", "Origin", icon="LAYER_ACTIVE")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_cursor_to_center", "", icon="OUTLINER_DATA_EMPTY")
            row.operator("view3d.snap_cursor_to_active", "", icon="PMARKER")
            row.menu("mtk_snaptocursor", "Cursor", icon="OUTLINER_DATA_EMPTY")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_selected_to_cursor", "", icon="RESTRICT_SELECT_OFF").use_offset = False
            row.operator("view3d.snap_selected_to_cursor", "", icon="STICKY_UVS_VERT").use_offset = True
            row.menu("mtk_snaptoselect", "Select", icon="RESTRICT_SELECT_OFF")


# Curvemode
# -#-- PIE-BLOCK ---- 7_Bottom_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(align=True)
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "show_x_ray", text="X-Ray  ")
            row.operator("object.wire_all", text=" ", icon='WIRE')
            row.operator("curve.subdivide", text="1").number_cuts = 1
            row.operator("curve.subdivide", text="2").number_cuts = 2

            row = box.row(align=True)
            row.prop(view, "use_matcap")
            row.operator("curve.subdivide", text="3").number_cuts = 3
            row.operator("curve.subdivide", text="4").number_cuts = 4
            row.operator("curve.subdivide", text="5").number_cuts = 5

            row = box.row(align=True)
            row.scale_x = 0.6
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")
            row.prop(context.space_data, "viewport_shade", "", expand=False)


# Curvemode
# -#-- PIE-BLOCK ---- 8_Bottom_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            curve = context.active_object.data
            row = box.row(align=True)

            row.scale_x = 1
            row.operator("mesh.face_align_x", "X  ", icon='COLOR_RED')
            row.operator("mesh.face_align_y", "Y  ", icon='COLOR_GREEN')
            row.operator("mesh.face_align_z", "Z ", icon='COLOR_BLUE')
            row.prop(curve, "show_handles", text="Handles")
            row = box.row(align=True)

            row.scale_x = 1
            row.operator("mesh.face_align_xy", "Xy", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy", icon='TRIA_UP_BAR')
            row.operator("mesh.face_align_xz", "Zx", icon='TRIA_LEFT_BAR')
            row.prop(curve, "show_normal_face", text="Normals")

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("object.loops1", text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="MZ", icon='ARROW_LEFTRIGHT')

            row.prop(context.scene.tool_settings, "normal_size", text="")


#######  Surfacemode  #######  Surfacemode  #######  Surfacemode  #######  Surfacemode  #######  Surfacemode  #######

        if ob.mode == 'EDIT_SURFACE':

            # Surfacemode
            # -#-- PIE-BLOCK ---- 1_Left ------------------------------------------------
            box = pie.split().box().column()
            row = box.row()
            row.operator("curve.extrude", text="Extrude")
            row = box.row()
            row.operator("curve.duplicate_move", text="Duplicate")
            row = box.row()
            row.operator("curve.switch_direction", "Direction")


# Surfacemode
# -#-- PIE-BLOCK ---- 2_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.95

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("snape.increment", "", icon="SNAP_INCREMENT")
            row.operator("snape.vertex", "", icon="SNAP_VERTEX")
            row.operator("snape.edge", "", icon="SNAP_EDGE")
            row.operator("snape.face", "", icon="SNAP_FACE")
            row.operator("snape.volume", "", icon="SNAP_VOLUME")

            row = box.row(align=True)
            row.scale_x = 1.3
            view = context.space_data
            toolsettings = context.tool_settings
            row.prop(toolsettings, "use_snap_align_rotation", text="", icon="SNAP_NORMAL")
            row.menu("htk_pivotorient", "Orientation", icon="EMPTY_DATA")
            row.prop(toolsettings, "use_snap_self", text="")

            row = box.row(align=True)
            row.scale_x = 1.3

            snap_meta = toolsettings.use_snap
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"

            row.menu("htk_snaptarget", "Snap Target", icon="SNAP_ON")
            row.prop(toolsettings, "use_snap_project", text="")

            row = box.row(align=True)
            toolsettings = context.tool_settings
            row.prop(toolsettings, "proportional_edit", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True)
            row.operator("view3d.ruler", text="Ruler")  # , icon="NOCURVE")

            row = box.row(align=True)
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho")


# Surfacemode
# -#-- PIE-BLOCK ---- 3_Button ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(1)
            row.operator("curve.split")
            row.operator("curve.make_segment", "Segment")
            row.operator("curve.separate")


# Surfacemode
# -#-- PIE-BLOCK ---- 4_Top ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.6

            row = box.row(1)
            row.scale_x = 1.55
            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")
            row.operator("screen.redo_last", text="Settings ")
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")
            row.operator("ed.undo_history", text="History")
            row.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER").use_hide_panels = True
            #row.operator("screen.screen_full_area", text = "", icon = "FULLSCREEN_ENTER")

            row = box.row(1)
            row.scale_x = 1.55
            row.operator("curve.select_random", text="Random")
            row.operator("curve.select_nth", text="Checker")
            row.menu("VIEW3D_MT_edit_curve_showhide", "", icon="VISIBLE_IPO_ON")

            row.operator("curve.select_linked", text="Linked ")
            row.operator("curve.select_all", text="Inverse  ").action = 'INVERT'

            row = box.row(1)
            row.scale_x = 1.55
            row.alignment = "CENTER"

            row.operator("view3d.select_border", text="", icon="BORDER_RECT")
            row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")
            row.menu("INFO_MT_surface_add", "", icon='OUTLINER_OB_SURFACE')
            row.operator("view3d.zoom_border", "", icon="ZOOM_PREVIOUS")
            row.operator("view3d.view_all", "", icon="ZOOM_OUT")


# Surfacemode
# -#-- PIE-BLOCK ---- 5_Top_Left ------------------------------------------------
            box = pie.split().box().column()
            row = box.row()
            row.menu("VIEW3D_MT_hook")
            row = box.row()
            row.operator("curve.cyclic_toggle")
            row = box.row()
            row.operator("object.vertex_random")


# Surfacemode
# -#-- PIE-BLOCK ---- 6_Top_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.85

            row = box.row(align=True)
            row.operator("object.editmode_toggle", text="Fast", icon="OBJECT_DATAMODE")
            row.operator("curve.delete")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("object.loops9", "", icon="EDITMODE_HLT")
            row.operator("object.loops7", "", icon="OBJECT_DATAMODE")
            row.menu("originsetup_mode", "Origin", icon="LAYER_ACTIVE")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_cursor_to_center", "", icon="OUTLINER_DATA_EMPTY")
            row.operator("view3d.snap_cursor_to_active", "", icon="PMARKER")
            row.menu("mtk_snaptocursor", "Cursor", icon="OUTLINER_DATA_EMPTY")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_selected_to_cursor", "", icon="RESTRICT_SELECT_OFF").use_offset = False
            row.operator("view3d.snap_selected_to_cursor", "", icon="STICKY_UVS_VERT").use_offset = True
            row.menu("mtk_snaptoselect", "Select", icon="RESTRICT_SELECT_OFF")


# Surfacemode
# -#-- PIE-BLOCK ---- 7_Bottom_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(align=True)
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "show_x_ray", text="X-Ray  ")
            row.operator("object.wire_all", text=" ", icon='WIRE')
            row.operator("curve.subdivide", text="1").number_cuts = 1
            row.operator("curve.subdivide", text="2").number_cuts = 2

            row = box.row(align=True)
            row.prop(view, "use_matcap")
            row.operator("curve.subdivide", text="3").number_cuts = 3
            row.operator("curve.subdivide", text="4").number_cuts = 4
            row.operator("curve.subdivide", text="5").number_cuts = 5

            row = box.row(align=True)
            row.scale_x = 0.6
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")
            row.prop(context.space_data, "viewport_shade", "", expand=False)


# Surfacemode
# -#-- PIE-BLOCK ---- 8_Bottom_Right ------------------------------------------------
            box = pie.split().box().column()
            row = box.row(align=True)

            row.scale_x = 1
            row.operator("mesh.face_align_x", "X  ", icon='COLOR_RED')
            row.operator("mesh.face_align_y", "Y  ", icon='COLOR_GREEN')
            row.operator("mesh.face_align_z", "Z ", icon='COLOR_BLUE')

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("mesh.face_align_xy", "Xy", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy", icon='TRIA_UP_BAR')
            row.operator("mesh.face_align_xz", "Zx", icon='TRIA_LEFT_BAR')

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("object.loops1", text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="MZ", icon='ARROW_LEFTRIGHT')


####### Latticemode ####### Latticemode ####### Latticemode ####### Latticemode ####### Latticemode ####### Latticemode #######

        if ob.mode == 'EDIT_LATTICE':

            # Latticemode
            # -#-- PIE-BLOCK ---- 1_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_viewport_on", "", icon='RESTRICT_VIEW_OFF')
            row.operator("view3d.display_modifiers_viewport_off", "", icon='VISIBLE_IPO_OFF')

            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_edit_on", "", icon='EDITMODE_HLT')
            row.operator("view3d.display_modifiers_edit_off", "", icon='SNAP_VERTEX')

            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_cage_on", "", icon='OUTLINER_OB_MESH')
            row.operator("view3d.display_modifiers_cage_off", "", icon='OUTLINER_DATA_MESH')

            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_delete", "", icon='X')
            row.operator_menu_enum("object.modifier_add", "type", text="", icon="MODIFIER")


# Latticemode
# -#-- PIE-BLOCK ---- 2_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.95

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("snape.increment", "", icon="SNAP_INCREMENT")
            row.operator("snape.vertex", "", icon="SNAP_VERTEX")
            row.operator("snape.edge", "", icon="SNAP_EDGE")
            row.operator("snape.face", "", icon="SNAP_FACE")
            row.operator("snape.volume", "", icon="SNAP_VOLUME")

            row = box.row(align=True)
            row.scale_x = 1.3
            view = context.space_data
            toolsettings = context.tool_settings
            row.operator("wm.context_toggle", text="", icon='MANIPUL').data_path = "space_data.show_manipulator"
            row.menu("htk_pivotorient", "Orientation", icon="EMPTY_DATA")
            row.prop(toolsettings, "use_snap_self", text="")

            row = box.row(align=True)
            row.scale_x = 1.3

            snap_meta = toolsettings.use_snap
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"
            row.menu("htk_snaptarget", "Snap Target", icon="SNAP_ON")
            row.prop(toolsettings, "use_snap_project", text="")

            row = box.row(align=True)
            toolsettings = context.tool_settings
            row.prop(toolsettings, "proportional_edit", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True)
            row.operator("view3d.ruler", text="Ruler")  # , icon="NOCURVE")

            row = box.row(align=True)
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho")


# Latticemode
# -#-- PIE-BLOCK ---- 3_Bottom ------------------------------------------------
            box = pie.split().box().column()

            row = box.row(align=True)
            row.operator("lattice.select_mirror", text="Sel. Mirror")
            row.operator("lattice.select_random", text="Sel. Random")

            row = box.row(align=True)
            row.operator("lattice.select_all", text="Sel. Inverse").action = 'INVERT'
            row.operator("lattice.select_ungrouped", text="Ungrouped Verts")


# Latticemode
# -#-- PIE-BLOCK ---- 4_Top ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.65

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55
            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")
            row.operator("screen.redo_last", text="Settings ")
            row.operator("ed.undo_history", text="History")
            row.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER").use_hide_panels = True

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55

            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55

            row.operator("view3d.select_border", text="", icon="BORDER_RECT")
            row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")

            row.operator("view3d.zoom_border", "", icon="ZOOM_PREVIOUS")
            row.operator("view3d.view_all", "", icon="ZOOM_OUT")


# Latticemode
# -#-- PIE-BLOCK ---- 5_Top_Left ------------------------------------------------
            box = pie.split().box().column()

            row = box.row(align=True)
            row.menu("VIEW3D_MT_hook", "Set Hook")

            row = box.row(align=True)
            row.operator("object.vertex_parent_set", "Vertex Parent")

            row = box.row(align=True)
            row.scale_x = 1.1
            row.operator("lattice.make_regular")


# Latticemode
# -#-- PIE-BLOCK ---- 6_Top_Right ------------------------------------------------

            box = pie.split().box().column()
            row = box.row(align=True)
            row.operator("object.editmode_toggle", text="Fast Toggle", icon="OBJECT_DATAMODE")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("object.loops9", "", icon="EDITMODE_HLT")
            row.operator("object.loops7", "", icon="OBJECT_DATAMODE")
            row.menu("originsetup_mode", "Origin", icon="LAYER_ACTIVE")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_cursor_to_center", "", icon="OUTLINER_DATA_EMPTY")
            row.operator("view3d.snap_cursor_to_active", "", icon="PMARKER")
            row.menu("mtk_snaptocursor", "Cursor", icon="OUTLINER_DATA_EMPTY")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_selected_to_cursor", "", icon="RESTRICT_SELECT_OFF").use_offset = False
            row.operator("view3d.snap_selected_to_cursor", "", icon="STICKY_UVS_VERT").use_offset = True
            row.menu("mtk_snaptoselect", "Select", icon="RESTRICT_SELECT_OFF")


# Latticemode
# -#-- PIE-BLOCK ---- 7_Bottom_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.column(align=True)
            row.operator("lattice.flip", text="Flip X  (U)").axis = "U"
            row.operator("lattice.flip", text="Flip Y  (V)").axis = "V"
            row.operator("lattice.flip", text="Flip Z  (W)").axis = "W"


# Latticemode
# -#-- PIE-BLOCK ---- 8_Bottom_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("mesh.face_align_x", "X      ", icon='COLOR_RED')
            row.operator("mesh.face_align_y", "Y      ", icon='COLOR_GREEN')
            row.operator("mesh.face_align_z", "Z      ", icon='COLOR_BLUE')

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("mesh.face_align_xy", "Xy  ", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy  ", icon='TRIA_UP_BAR')
            row.operator("mesh.face_align_xz", "Zx  ", icon='TRIA_LEFT_BAR')

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("object.loops1", text="X", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="Y", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="Z", icon='ARROW_LEFTRIGHT')


#### METABALL #### METABALL #### METABALL #### METABALL #### METABALL #### METABALL #### METABALL #### METABALL #### METABALL #### METABALL #### METABALL ####

        if context.mode == 'EDIT_METABALL':
            ###space###

            # METABALL
            # -#-- PIE-BLOCK ---- 1_Left ----------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_viewport_on", "", icon='RESTRICT_VIEW_OFF')
            row.operator("view3d.display_modifiers_viewport_off", "", icon='VISIBLE_IPO_OFF')

            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_edit_on", "", icon='EDITMODE_HLT')
            row.operator("view3d.display_modifiers_edit_off", "", icon='SNAP_VERTEX')

            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_cage_on", "", icon='OUTLINER_OB_MESH')
            row.operator("view3d.display_modifiers_cage_off", "", icon='OUTLINER_DATA_MESH')

            row = box.row(align=True)
            row.scale_x = 1.5
            row.operator("view3d.display_modifiers_delete", "", icon='X')
            row.operator_menu_enum("object.modifier_add", "type", text="", icon="MODIFIER")


# METABALL
# -#-- PIE-BLOCK ---- 2_Right ---------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.95

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("snape.increment", "", icon="SNAP_INCREMENT")
            row.operator("snape.vertex", "", icon="SNAP_VERTEX")
            row.operator("snape.edge", "", icon="SNAP_EDGE")
            row.operator("snape.face", "", icon="SNAP_FACE")
            row.operator("snape.volume", "", icon="SNAP_VOLUME")

            row = box.row(align=True)
            row.scale_x = 1.3
            view = context.space_data
            toolsettings = context.tool_settings
            row.operator("wm.context_toggle", text="", icon='MANIPUL').data_path = "space_data.show_manipulator"
            row.menu("htk_pivotorient", "Orientation", icon="EMPTY_DATA")
            row.prop(toolsettings, "use_snap_self", text="")

            row = box.row(align=True)
            row.scale_x = 1.3

            snap_meta = toolsettings.use_snap
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"
            row.menu("htk_snaptarget", "Snap Target", icon="SNAP_ON")
            row.prop(toolsettings, "use_snap_project", text="")

            row = box.row(align=True)
            toolsettings = context.tool_settings
            row.prop(toolsettings, "proportional_edit", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True)
            row.operator("view3d.ruler", text="Ruler")  # , icon="NOCURVE")

            row = box.row(align=True)
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho")


# METABALL
# -#-- PIE-BLOCK ---- 3_Bottom --------------------------------------------------
            box = pie.split().box().column()

            row = box.row(1)
            row.scale_x = 1.55
            row.operator("object.metaball_add", icon='META_BALL', text="").type = "BALL"
            row.operator("object.metaball_add", icon='META_CAPSULE', text="").type = "CAPSULE"
            row.operator("object.metaball_add", icon='META_PLANE', text="").type = "PLANE"
            row.operator("object.metaball_add", icon='META_ELLIPSOID', text="").type = "ELLIPSOID"
            row.operator("object.metaball_add", icon='META_CUBE', text="").type = "CUBE"


# METABALL
# -#-- PIE-BLOCK ---- 4_Top -----------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.65

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55

            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")
            row.operator("screen.redo_last", text="Settings ")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')
            row.operator("ed.undo_history", text="History")
            row.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER").use_hide_panels = True
            #row.operator("screen.screen_full_area", text = "", icon = "FULLSCREEN_ENTER")

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55

            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.menu("VIEW3D_MT_edit_meta_showhide", text="", icon="RESTRICT_VIEW_OFF")
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55

            row.operator("view3d.select_border", text="", icon="BORDER_RECT")
            row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")
            row.menu("pie.mt_selection", text="", icon="HAND")
            row.operator("view3d.zoom_border", "", icon="ZOOM_PREVIOUS")
            row.operator("view3d.view_all", "", icon="ZOOM_OUT")


# METABALL
# -#-- PIE-BLOCK ---- 5_Top_Left ------------------------------------------------
            box = pie.split().box().column()

            row = box.column(1)
            row.operator("mball.select_all").action = 'TOGGLE'
            row.operator("mball.select_all", text="Inverse").action = 'INVERT'
            row.operator("mball.select_random_metaelems")
            row.operator_menu_enum("mball.select_similar", "type", text="Similar")


# METABALL
# -#-- PIE-BLOCK ---- 6_Top_Right -----------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.85

            row = box.row(align=True)
            row.operator("object.editmode_toggle", text="Fast  ", icon="OBJECT_DATAMODE")
            row.operator("mball.delete_metaelems", "Delete", icon="PANEL_CLOSE")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("object.loops9", "", icon="EDITMODE_HLT")
            row.operator("object.loops7", "", icon="OBJECT_DATAMODE")
            row.menu("originsetup_mode", "Origin", icon="LAYER_ACTIVE")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_cursor_to_center", "", icon="OUTLINER_DATA_EMPTY")
            row.operator("view3d.snap_cursor_to_active", "", icon="PMARKER")
            row.menu("mtk_snaptocursor", "Cursor", icon="OUTLINER_DATA_EMPTY")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_selected_to_cursor", "", icon="RESTRICT_SELECT_OFF").use_offset = False
            row.operator("view3d.snap_selected_to_cursor", "", icon="STICKY_UVS_VERT").use_offset = True
            row.menu("mtk_snaptoselect", "Select", icon="RESTRICT_SELECT_OFF")


# METABALL
# -#-- PIE-BLOCK ---- 7_Bottom_Left ---------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.column(1)
            row.operator("mball.duplicate_metaelems", "Duplicate")
            row.operator("object.vertex_random", "Random Deform")


# METABALL
# -#-- PIE-BLOCK ---- 8_Bottom_Right --------------------------------------------
            box = pie.split().box().column()
            row = box.row(align=True)
            row.scale_x = 1
            row.operator("mesh.face_align_x", "X      ", icon='COLOR_RED')
            row.operator("mesh.face_align_y", "Y      ", icon='COLOR_GREEN')
            row.operator("mesh.face_align_z", "Z      ", icon='COLOR_BLUE')

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("mesh.face_align_xy", "Xy  ", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy  ", icon='TRIA_UP_BAR')
            row.operator("mesh.face_align_xz", "Zx  ", icon='TRIA_LEFT_BAR')

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("object.loops1", text="X", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="Y", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="Z", icon='ARROW_LEFTRIGHT')


####### Armature ####### Armature ####### Armature ####### Armature ####### Armature ####### Armature ####### Armature ####### Armature ####### Armature #######

        if ob.mode == 'EDIT_ARMATURE':
            ###space###
            arm = context.active_object.data

# Armature
# -#-- PIE-BLOCK ---- 1_Left ----------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.column()
            row.operator("armature.flip_names", icon="ARROW_LEFTRIGHT")

            row.operator("armature.autoside_names", text="AutoName Left/Right").type = 'XAXIS'
            row.operator("armature.autoside_names", text="AutoName Front/Back").type = 'YAXIS'
            row.operator("armature.autoside_names", text="AutoName Top/Bottom").type = 'ZAXIS'
            row.operator("armature.bone_layers")
            row.operator("armature.armature_layers")


# Armature
# -#-- PIE-BLOCK ---- 2_Right ---------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.95

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("snape.increment", "", icon="SNAP_INCREMENT")
            row.operator("snape.vertex", "", icon="SNAP_VERTEX")
            row.operator("snape.edge", "", icon="SNAP_EDGE")
            row.operator("snape.face", "", icon="SNAP_FACE")
            row.operator("snape.volume", "", icon="SNAP_VOLUME")

            row = box.row(align=True)
            row.scale_x = 1.3
            view = context.space_data
            toolsettings = context.tool_settings
            row.operator("wm.context_toggle", text="", icon='MANIPUL').data_path = "space_data.show_manipulator"
            row.menu("htk_pivotorient", "Orientation", icon="EMPTY_DATA")
            row.prop(toolsettings, "use_snap_self", text="")

            row = box.row(align=True)
            row.scale_x = 1.3

            snap_meta = toolsettings.use_snap
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"
            row.menu("htk_snaptarget", "Snap Target", icon="SNAP_ON")
            row.prop(toolsettings, "use_snap_project", text="")

            row = box.row(align=True)
            toolsettings = context.tool_settings
            row.prop(toolsettings, "proportional_edit", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True)
            row.operator("view3d.ruler", text="Ruler")  # , icon="NOCURVE")

            row = box.row(align=True)
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho")


# Armature
# -#-- PIE-BLOCK ---- 3_Bottom --------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.85

            row = box.row(align=True)
            row.scale_x = 1.55
            row.operator("armature.bone_primitive_add", text="", icon="BONE_DATA")

            row.operator("armature.merge", text="Merge", icon="AUTOMERGE_ON")
            row.operator("armature.split", text="Split", icon="UNLINKED")
            row.operator("armature.fill", text="Filler", icon="GROUP_BONE")
            row.prop(arm, "use_mirror_x", text="", icon='X')

            row = box.row(align=True)
            row.operator("armature.duplicate_move", text="Duplicate")
            row.operator("object.vertex_random")
            row.operator("armature.separate", text="Separate")

            row = box.row(align=True)
            row.operator("armature.calculate_roll", text="Recalc. Roll", icon="FRAME_PREV")
            row.operator("transform.transform", text="Set Roll", icon="MAN_ROT").mode = "BONE_ROLL"
            row.operator("armature.switch_direction", icon="ARROW_LEFTRIGHT")


# Armature
# -#-- PIE-BLOCK ---- 4_Top -----------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.65

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55

            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")
            row.operator("screen.redo_last", text="Settings ")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')
            row.operator("ed.undo_history", text="History")
            row.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER").use_hide_panels = True

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55

            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.menu("armature.hide_menu", text="", icon="RESTRICT_VIEW_OFF")
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55

            row.operator("view3d.select_border", text="", icon="BORDER_RECT")
            row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")
            row.menu("pie.mt_selection", text="", icon="HAND")

            row.operator("view3d.zoom_border", "", icon="ZOOM_PREVIOUS")
            row.operator("view3d.view_all", "", icon="ZOOM_OUT")


# Armature
# -#-- PIE-BLOCK ---- 5_Top_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(align=True)
            row.operator("armature.parent_set", text="Parent", icon="CONSTRAINT_BONE")
            row = box.row(align=True)
            row.operator("armature.parent_clear").type = "CLEAR"
            row = box.row(align=True)
            row.operator("armature.parent_clear", text="Disconnect Bone").type = "DISCONNECT"

            row = box.row(align=True)
            row.menu("VIEW3D_MT_bone_options_toggle", "Bone Option", icon="LONGDISPLAY")


# Armature
# -#-- PIE-BLOCK ---- 6_Top_Right -----------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.9

            row = box.row(align=True)
            #row.operator("object.editmode_toggle", text="Fast  ", icon = "OBJECT_DATAMODE")
            #row.operator("object.posemode_toggle", "Pose", icon = "POSE_HLT")
            row.operator_menu_enum("OBJECT_OT_mode_set", "mode", "Mode ", icon="OBJECT_DATAMODE")
            row.operator("armature.delete", text="Delete", icon="PANEL_CLOSE")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("object.loops9", "", icon="EDITMODE_HLT")
            row.operator("object.loops7", "", icon="OBJECT_DATAMODE")
            row.menu("originsetup_mode", "Origin", icon="LAYER_ACTIVE")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_cursor_to_center", "", icon="OUTLINER_DATA_EMPTY")
            row.operator("view3d.snap_cursor_to_active", "", icon="PMARKER")
            row.menu("mtk_snaptocursor", "Cursor", icon="OUTLINER_DATA_EMPTY")

            row = box.row(align=True)
            row.scale_x = 1.6
            row.operator("view3d.snap_selected_to_cursor", "", icon="RESTRICT_SELECT_OFF").use_offset = False
            row.operator("view3d.snap_selected_to_cursor", "", icon="STICKY_UVS_VERT").use_offset = True
            row.menu("mtk_snaptoselect", "Select", icon="RESTRICT_SELECT_OFF")


# Armature
# -#-- PIE-BLOCK ---- 7_Bottom_Left ---------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(align=True)
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "show_x_ray", text="X-Ray  ")
            row.operator("object.wire_all", text=" ", icon='WIRE')
            row.operator("armature.subdivide", text="1").number_cuts = 1
            row.operator("armature.subdivide", text="2").number_cuts = 2

            # row.operator("armature.subdivide",text="6").number_cuts=6

            row = box.row(align=True)
            row.prop(view, "use_matcap")
            row.operator("armature.subdivide", text="3").number_cuts = 3
            row.operator("armature.subdivide", text="4").number_cuts = 4
            row.operator("armature.subdivide", text="5").number_cuts = 5

            row = box.row(align=True)
            row.scale_x = 0.6
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")
            row.prop(context.space_data, "viewport_shade", "", expand=False)


# Armature
# -#-- PIE-BLOCK ---- 8_Bottom_Right --------------------------------------------
            box = pie.split().box().column()
            row = box.row(align=True)
            row.scale_x = 1
            row.operator("mesh.face_align_x", "X      ", icon='COLOR_RED')
            row.operator("mesh.face_align_y", "Y      ", icon='COLOR_GREEN')
            row.operator("mesh.face_align_z", "Z      ", icon='COLOR_BLUE')

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("mesh.face_align_xy", "Xy  ", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy  ", icon='TRIA_UP_BAR')
            row.operator("mesh.face_align_xz", "Zx  ", icon='TRIA_LEFT_BAR')

            row = box.row(align=True)
            row.scale_x = 1
            row.operator("object.loops1", text="X", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="Y", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="Z", icon='ARROW_LEFTRIGHT')


####### Pose ####### Pose ####### Pose ####### Pose ####### Pose ####### Pose ####### Pose ####### Pose ####### Pose ####### Pose ####### Pose ####### Pose #######

        if context.mode == 'POSE':
            ###space###
            arm = context.active_object.data

# Pose
# -#-- PIE-BLOCK ---- 1_Left ----------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.column()

            row.menu("VIEW3D_MT_object_parent")
            row.menu("VIEW3D_MT_pose_constraints")
            row.menu("VIEW3D_MT_pose_ik")

            row.operator("pose.bone_layers", text="Bone Layers")
            row.operator("armature.armature_layers", text="Armature Layers")
            row.menu("VIEW3D_MT_bone_options_toggle", "Bone Setting", icon="PREFERENCES")


# Pose
# -#-- PIE-BLOCK ---- 2_Right ---------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.95

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("snape.increment", "", icon="SNAP_INCREMENT")
            row.operator("snape.vertex", "", icon="SNAP_VERTEX")
            row.operator("snape.edge", "", icon="SNAP_EDGE")
            row.operator("snape.face", "", icon="SNAP_FACE")
            row.operator("snape.volume", "", icon="SNAP_VOLUME")

            row = box.row(align=True)
            row.scale_x = 1.3
            view = context.space_data
            toolsettings = context.tool_settings
            row.operator("wm.context_toggle", text="", icon='MANIPUL').data_path = "space_data.show_manipulator"
            row.menu("htk_pivotorient", "Orientation", icon="EMPTY_DATA")
            row.prop(toolsettings, "use_snap_self", text="")

            row = box.row(align=True)
            row.scale_x = 1.3

            snap_meta = toolsettings.use_snap
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"
            row.menu("htk_snaptarget", "Snap Target", icon="SNAP_ON")
            row.prop(toolsettings, "use_snap_project", text="")

            row = box.row(align=True)
            toolsettings = context.tool_settings
            row.prop(toolsettings, "proportional_edit", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True)
            row.operator("view3d.ruler", text="Ruler")  # , icon="NOCURVE")

            row = box.row(align=True)
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho")


# Pose
# -#-- PIE-BLOCK ---- 3_Bottom --------------------------------------------------
            box = pie.split().box().column()
            #box.scale_x = 0.65

            row = box.row(align=True)

            row.operator("pose.copy", text="Copy", icon='COPYDOWN')
            row.operator("pose.paste", text="Paste", icon='PASTEDOWN')
            row.operator("pose.paste", text="Flip Paste", icon='PASTEFLIPDOWN').flipped = 1

            row = box.row(align=True)
            row.operator("pose.push")
            row.operator("pose.relax")
            row.operator("pose.quaternions_flip")

            row = box.row(align=True)
            row.operator("pose.breakdown")


# Pose
# -#-- PIE-BLOCK ---- 4_Top -----------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.75

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55

            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")
            row.operator("screen.redo_last", text="Settings ")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')
            row.operator("ed.undo_history", text="History")
            row.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER").use_hide_panels = True
            #row.operator("screen.screen_full_area", text = "", icon = "FULLSCREEN_ENTER")

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55

            row.menu("VIEW3D_MT_pose_library")
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.menu("VIEW3D_MT_pose_showhide", text="", icon="RESTRICT_VIEW_OFF")
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")
            row.menu("VIEW3D_MT_pose_group")

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55

            row.operator("view3d.select_border", text="", icon="BORDER_RECT")
            row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")

            row.menu("pie.mt_selection", text="", icon="HAND")

            row.operator("view3d.zoom_border", "", icon="ZOOM_PREVIOUS")
            row.operator("view3d.view_all", "", icon="ZOOM_OUT")


# Pose
# -#-- PIE-BLOCK ---- 5_Top_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.95

            row = box.row(align=True)
            row.operator("pose.flip_names", text="FlipName", icon="ARROW_LEFTRIGHT")
            row.operator("pose.autoside_names", text="Left/Right").axis = 'XAXIS'

            row = box.row(align=True)
            row.operator("pose.autoside_names", text="Front/Back").axis = 'YAXIS'
            row.operator("pose.autoside_names", text="Top/Bottom").axis = 'ZAXIS'

            row = box.row(align=True)
            row.menu("VIEW3D_MT_transform_armature")
            row.menu("VIEW3D_MT_pose_transform", "Clear")
            row.menu("VIEW3D_MT_pose_apply")


# Pose
# -#-- PIE-BLOCK ---- 6_Top_Right -----------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.9

            row = box.row(align=True)
            #row.operator("object.editmode_toggle", text="Fast Toggle", icon = "OBJECT_DATAMODE")
            row.operator_menu_enum("OBJECT_OT_mode_set", "mode", "Set Mode ", icon="OBJECT_DATAMODE")

            row = box.row(align=True)
            row.menu("VIEW3D_MT_pose_slide")
            row.menu("VIEW3D_MT_pose_propagate")

            row = box.row(align=True)
            row.operator("poselib.pose_add", text="Add Pose")
            row.operator("poselib.pose_rename", text="Rename Pose")

            row = box.row(align=True)
            row.operator("poselib.browse_interactive", text="Browse Poses")
            row.operator("poselib.pose_remove", text="Remove Pose")


# Pose
# -#-- PIE-BLOCK ---- 7_Bottom_Left ---------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(align=True)
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "show_x_ray", text="X-Ray  ")
            arm = context.active_object.data
            row.prop(arm, "use_auto_ik")
            row.operator("object.wire_all", text=" ", icon='WIRE')

            row = box.row(align=True)
            row.prop(view, "use_matcap")
            row.operator("armature.subdivide", text="3").number_cuts = 3
            row.operator("armature.subdivide", text="4").number_cuts = 4
            row.operator("armature.subdivide", text="5").number_cuts = 5

            row = box.row(align=True)
            row.scale_x = 0.6
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")
            row.prop(context.space_data, "viewport_shade", "", expand=False)


# Pose
# -#-- PIE-BLOCK ---- 8_Bottom_Right --------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(align=True)
            row.scale_x = 1.55

            view = context.space_data
            obj = bpy.context.scene.objects.active
            scene = context.scene
            toolsettings = context.tool_settings
            screen = context.screen
            layout = self.layout
            self.scn = context.scene
            row.alignment = 'CENTER'
            row.operator("screen.frame_jump", text="", icon='REW').end = False
            row.operator("screen.keyframe_jump", text="", icon='PREV_KEYFRAME').next = False

            if not screen.is_animation_playing:
                # if using JACK and A/V sync:
                #   hide the play-reversed button
                #   since JACK transport doesn't support reversed playback
                if scene.sync_mode == 'AUDIO_SYNC' and context.user_preferences.system.audio_device == 'JACK':
                    row.operator("screen.animation_play", text="", icon='PLAY')
                else:
                    row.operator("screen.animation_play", text="", icon='PLAY_REVERSE').reverse = True
                    row.operator("screen.animation_play", text="", icon='PLAY')
            else:
                row.operator("screen.animation_play", text="", icon='PAUSE')

            row.operator("screen.keyframe_jump", text="", icon='NEXT_KEYFRAME').next = True
            row.operator("screen.frame_jump", text="", icon='FF').end = True

            if context.mode == "OBJECT" or context.mode == "POSE":

                if context.active_object and context.active_object.type in {'MESH', 'CURVE', 'SURFACE', 'ARMATURE', 'META', 'LATTICE'}:

                    row = box.row(align=True)
                    row.scale_x = 0.75
                    row.operator("anim.keyframe_insert_menu", icon='ZOOMIN', text=" ")
                    row.operator("anim.keyframe_delete_v3d", icon='ZOOMOUT', text=" ")
                    row.prop_search(context.scene.keying_sets_all, "active", context.scene, "keying_sets_all", text="")
                    row.operator("anim.keyframe_insert", text=" ", icon='KEY_HLT')
                    row.operator("anim.keyframe_delete", text=" ", icon='KEY_DEHLT')

                    row = box.row(align=True)

                    row.operator("pose.paths_calculate", text="Calculate")
                    row.operator("pose.paths_clear", text="Clear")
                    row.operator("nla.bake")


#########################################################################################################################
#########################################################################################################################

####### Sculptmode ####### Sculptmode ####### Sculptmode ####### Sculptmode ####### Sculptmode ####### Sculptmode #######

        if ob.mode == 'SCULPT':
            brush = context.tool_settings.sculpt.brush
            tex_slot = brush.texture_slot
            sculpt = toolsettings.sculpt

# Sculptmode
# -#-- PIE-BLOCK ---- 1_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1.7

            row = box.column_flow(2)
            row.scale_y = 1.25
            row.scale_x = 1.2

            props = row.operator("paint.hide_show", text="BBox Hide", icon='BORDER_RECT')
            props.action = 'HIDE'
            props.area = 'INSIDE'

            props = row.operator("paint.hide_show", text="BBox Show", icon='BORDERMOVE')
            props.action = 'SHOW'
            props.area = 'INSIDE'

            props = row.operator("paint.mask_flood_fill", text="Fill", icon='MATCAP_08')
            props.mode = 'VALUE'
            props.value = 1

            row.operator("paint.mask_flood_fill", text="Invert", icon='FILE_REFRESH').mode = 'INVERT'

            row.prop(brush, "use_frontface", text="Front only")

            #row = box.column_flow(2)
            row.scale_y = 1.25
            row.scale_x = 1.2
            row.operator("view3d.select_border", text="Box", icon="IMAGE_ZDEPTH")

            hidemask = row.operator("paint.hide_show", text="Hide", icon='BRUSH_TEXMASK')
            hidemask.action = 'HIDE'
            hidemask.area = 'MASKED'

            showmask = row.operator("paint.hide_show", text="Show", icon='SOLID')
            showmask.action = 'SHOW'
            showmask.area = 'MASKED'

            clearmask = row.operator("paint.mask_flood_fill", text="Clear", icon='BRUSH_TEXFILL')
            clearmask.mode = 'VALUE'
            clearmask.value = 0

            row.prop(brush, "direction", "")


# Sculptmode
# -#-- PIE-BLOCK ---- 2_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.75
            row = box.row()
            spl = row.split()
            row = spl.column()
            row.template_ID_preview(context.tool_settings.vertex_paint.brush, "texture", new="texture.new", rows=2, cols=6)

            row = box.row()
            row.prop(tex_slot, "map_mode", text="")

            if tex_slot.has_texture_angle:
                row.prop(tex_slot, "angle", text="Angle")
                if tex_slot.map_mode == 'STENCIL':
                    row = box.row()
                    row.operator("brush.stencil_reset_transform", icon='SCREEN_BACK')

                row = box.row()
                if tex_slot.has_texture_angle_source:
                    row.prop(tex_slot, "use_rake", text="Rake")
                    row.prop(tex_slot, "use_random", text="Random")

                    if tex_slot.use_random:
                        row.prop(tex_slot, "random_angle", text="")


# Sculptmode
# -#-- PIE-BLOCK ---- 3_Bottom ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.75

            row = box.row(1)
            spl = row.split()
            row = spl.column()
            row.template_ID_preview(context.tool_settings.sculpt, "brush", new="brush.add", rows=3, cols=8)

            """
            
            row = box.row(1)
            row.alignment ='CENTER'            
            row.scale_y = 1.5
            row.scale_x = 1.2            
            row.operator("paint.brush_select", text='Grab', icon='BRUSH_GRAB').sculpt_tool='GRAB'
            row.operator("paint.brush_select", text='Nudge', icon='BRUSH_NUDGE').sculpt_tool= 'NUDGE'
            row.operator("paint.brush_select", text='Twist', icon='BRUSH_ROTATE').sculpt_tool= 'ROTATE'
            row.operator("paint.brush_select", text='Snakehook', icon='BRUSH_SNAKE_HOOK').sculpt_tool= 'SNAKE_HOOK'
            row.operator("paint.brush_select", text='Thumb', icon='BRUSH_THUMB').sculpt_tool= 'THUMB'       
            
            
            row = box.row(1)
            row.alignment ='CENTER'            
            row.scale_y = 1.5
            row.scale_x = 1.2              
            row.operator("paint.brush_select", text='Smooth', icon='BRUSH_SMOOTH').sculpt_tool= 'SMOOTH'
            row.operator("paint.brush_select", text='Flatten', icon='BRUSH_FLATTEN').sculpt_tool='FLATTEN'
            row.operator("sculpt.polish", text='Polish', icon='BRUSH_FLATTEN')
            row.operator("paint.brush_select", text='Pinch/Magnify', icon='BRUSH_PINCH').sculpt_tool= 'PINCH'            
            row.operator("paint.brush_select", text='Fill/Deepen', icon='BRUSH_FILL').sculpt_tool='FILL'            
            row.operator("paint.brush_select", text='Scrape/Peaks', icon='BRUSH_SCRAPE').sculpt_tool= 'SCRAPE'

            row = box.row(1)
            row.scale_y = 1.5
            row.scale_x = 1.2                              
            row.operator("paint.brush_select", text='Blob', icon='BRUSH_BLOB').sculpt_tool= 'BLOB'
            row.operator("paint.brush_select", text="Clay", icon='BRUSH_CLAY').sculpt_tool='CLAY'        
            row.operator("paint.brush_select", text='Claystrips', icon='BRUSH_CLAY_STRIPS').sculpt_tool= 'CLAY_STRIPS'
            row.operator("paint.brush_select", text="Crease", icon='BRUSH_CREASE').sculpt_tool='CREASE'
            row.operator("paint.brush_select", text='Brush', icon='BRUSH_SCULPT_DRAW').sculpt_tool='DRAW'
            row.operator("paint.brush_select", text='In-/Deflate', icon='BRUSH_INFLATE').sculpt_tool='INFLATE'
            row.operator("paint.brush_select", text='Layer', icon='BRUSH_LAYER').sculpt_tool= 'LAYER'
            """

            #row.label("Mouse behavior:  RMB + Y-Axis = RADIUS  /  RMB + X-Axis = STRENGHT  /  Ctrl + RMB = INVERT TOOL")

            row = box.row(1)
            row.alignment = 'CENTER'
            ups = context.tool_settings.unified_paint_settings
            row = box.row()
            row.scale_y = 1.5
            row.scale_x = 1.55

            if ((ups.use_unified_size and ups.use_locked_size) or
                    ((not ups.use_unified_size) and brush.use_locked_size)):
                row.prop(ups, "use_pressure_size", text="", toggle=True, icon_only=True)
                row.prop(ups, "use_locked_size", "", icon='LOCKED')
                row.prop(ups, "unprojected_radius", slider=True, text="Radius")
            else:
                row.prop(ups, "use_pressure_size", text="", toggle=True, icon_only=True)
                row.prop(ups, "use_locked_size", "", icon='UNLOCKED')
                row.prop(ups, "size", slider=True, text="Radius")

            row.prop(ups, "strength", text="Strength", slider=False)
            row.prop(context.tool_settings.sculpt.brush, "use_space_attenuation", toggle=True, text="")
            row.prop(ups, "use_pressure_strength", text="", toggle=True, icon_only=True)

            row = box.row()
            row.scale_x = 1.55

            row.prop(brush, "use_inverse_smooth_pressure", toggle=True, text="")
            row.prop(brush, "auto_smooth_factor", slider=True)

            capabilities = brush.sculpt_capabilities

            # normal_weight
            if capabilities.has_normal_weight:

                row.prop(brush, "normal_weight", slider=True)

            # crease_pinch_factor
            if capabilities.has_pinch_factor:
                row.prop(brush, "crease_pinch_factor", slider=True, text="Pinch")

            # use_original_normal and sculpt_plane
            if capabilities.has_sculpt_plane:
                row.prop(brush, "sculpt_plane", text="")
                row.prop(brush, "use_original_normal", toggle=True, icon_only=True)

            if brush.sculpt_tool == 'MASK':
                row.prop(brush, "mask_tool", text="")

            # plane_offset, use_offset_pressure, use_plane_trim, plane_trim
            if capabilities.has_plane_offset:

                row = box.row()
                row.scale_x = 1.55
                row.prop(brush, "use_offset_pressure", text="")
                row.prop(brush, "plane_offset", slider=True)

                row.prop(brush, "use_plane_trim", text="Trim")
                row.active = brush.use_plane_trim
                row.prop(brush, "plane_trim", slider=True, text="Distance")

            # height
            if capabilities.has_height:
                row = box.row()
                row.prop(brush, "height", slider=True, text="Height")


# Sculptmode
# -#-- PIE-BLOCK ---- 4_Top ------------------------------------------------
            box = pie.split().box().column()

            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_x = 1.55
            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")
            row.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER").use_hide_panels = True

            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_x = 1
            row.operator("screen.redo_last", text="Settings")
            row.operator("view3d.zoom_border", " ", icon="ZOOM_PREVIOUS")
            row.operator("view3d.view_all", " ", icon="ZOOM_OUT")
            row.operator("ed.undo_history", text="History ")

            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_y = 1.25
            row.operator("brush.curve_preset", icon='SMOOTHCURVE', text=" ").shape = 'SMOOTH'
            row.operator("brush.curve_preset", icon='SPHERECURVE', text=" ").shape = 'ROUND'
            row.operator("brush.curve_preset", icon='ROOTCURVE', text=" ").shape = 'ROOT'
            row.operator("brush.curve_preset", icon='SHARPCURVE', text=" ").shape = 'SHARP'
            row.operator("brush.curve_preset", icon='LINCURVE', text=" ").shape = 'LINE'
            row.operator("brush.curve_preset", icon='NOCURVE', text=" ").shape = 'MAX'

            if context.sculpt_object.use_dynamic_topology_sculpting:
                row = box.row(1)
                row.prop(sculpt, "use_smooth_shading", "S-Shade")
                row.prop(sculpt, "symmetrize_direction", "")
                row.operator("sculpt.symmetrize", "Symmetry")
                row.operator("sculpt.optimize", " ", icon='GROUP_VERTEX')


# Sculptmode
# -#-- PIE-BLOCK ---- 5_Top_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row()
            if context.sculpt_object.use_dynamic_topology_sculpting:
                row.operator("sculpt.dynamic_topology_toggle", icon='X', text="Disable Dyntopo")
            else:
                row.operator("sculpt.dynamic_topology_toggle", icon='SCULPT_DYNTOPO', text="Enable Dyntopo")

            row = box.row()
            if (sculpt.detail_type_method == 'CONSTANT'):
                row.prop(sculpt, "constant_detail", text="const.")
                row = box.row()
                row.operator("sculpt.sample_detail_size", text=" ", icon='EYEDROPPER')
            else:
                row.prop(sculpt, "detail_size", text="detail")

            row = box.row()
            row.prop(sculpt, "detail_refine_method", text="")

            row = box.row()
            row.prop(sculpt, "detail_type_method", text="")


# Sculptmode
# -#-- PIE-BLOCK ---- 6_Top_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row()
            #row.operator("object.editmode_toggle", text=" ", icon = "EDIT")
            row.menu("modeset_edit", "Mode  ", icon="OBJECT_DATAMODE")
            row.prop(context.tool_settings.sculpt, "use_symmetry_feather", text="Feather")

            row = box.row(1)

            row.prop(sculpt, "use_symmetry_x", text="X", toggle=True, icon="TRIA_RIGHT")
            row.prop(sculpt, "use_symmetry_y", text="Y", toggle=True, icon="TRIA_UP")
            row.prop(sculpt, "use_symmetry_z", text="Z", toggle=True, icon="SPACE3")

            row = box.row(1)
            row.prop(sculpt, "lock_x", text="X", toggle=True, icon="LOCKED")
            row.prop(sculpt, "lock_y", text="Y", toggle=True, icon="LOCKED")
            row.prop(sculpt, "lock_z", text="Z", toggle=True, icon="LOCKED")


# Sculptmode
# -#-- PIE-BLOCK ---- 7_Bottom_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1.1

            row = box.row(1)
            row.scale_x = 0.7
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "show_x_ray", text="X-Ray  ")

            row.operator("object.wire_all", text=" ", icon='WIRE')
            row.operator("view3d.modifiers_subsurf_level_0")
            row.operator("view3d.modifiers_subsurf_level_1")

            row = box.row(1)
            row.scale_x = 0.7
            row.prop(view, "use_matcap")
            row.operator("view3d.modifiers_subsurf_level_2")
            row.operator("view3d.modifiers_subsurf_level_3")
            row.operator("view3d.modifiers_subsurf_level_4")

            row = box.row()
            row.scale_x = 0.6
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")
            row.prop(context.space_data, "viewport_shade", "", expand=False)


# Sculptmode
# -#-- PIE-BLOCK ---- 8_Bottom_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.7

            row = box.row(1)
            row.prop(context.tool_settings.sculpt.brush, "stroke_method", text="")
            row.prop(context.tool_settings.sculpt.brush, "use_smooth_stroke", text="Smooth")

            row = box.row()
            row.scale_x = 1.55
            jitter_meta = toolsettings.sculpt.brush.use_relative_jitter
            if jitter_meta == False:
                row.operator("wm.context_toggle", text="", icon="UNLOCKED").data_path = "tool_settings.sculpt.brush.use_relative_jitter"
            else:
                row.operator("wm.context_toggle", text="", icon="LOCKED").data_path = "tool_settings.sculpt.brush.use_relative_jitter"

            row.prop(context.tool_settings.sculpt.brush, "jitter", text="Jitter", slider=False)
            row.prop(context.tool_settings.sculpt.brush, "use_pressure_jitter", toggle=True, text="")

            row = box.row()
            row.scale_x = 1.55
            row.prop(context.tool_settings.sculpt.brush, "spacing", text="Spacing")
            row.prop(context.tool_settings.sculpt.brush, "use_pressure_spacing", toggle=True, text="")


####### Vertexpaint ####### Vertexpaint ####### Vertexpaint ####### Vertexpaint ####### Vertexpaint ####### Vertexpaint #######

        if ob.mode == 'PAINT_VERTEX':
            brush = context.tool_settings.image_paint.brush
            tex_slot = brush.texture_slot


# Vertexmode
# -#-- PIE-BLOCK ---- 1_Left ------------------------------------------------
            box = pie.split().box().column()
            row = box.row(1)
            row.operator("paint.vertex_color_set", text="Set Color ")
            row = box.row(1)
            row.operator("paint.vertex_color_smooth", text="Smooth Color ")
            row = box.row(1)
            row.operator("mesh.connected_vertex_colors", text="Connected Colors")
            row = box.row(1)
            row.operator("paint.vertex_color_dirt", text="Dirt Color ")
            row = box.row(1)
            row.operator("paint.worn_edges", text="Worn Edges")


# Vertexmode
# -#-- PIE-BLOCK ---- 2_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.75
            row = box.row()
            spl = row.split()
            row = spl.column()
            row.template_ID_preview(context.tool_settings.vertex_paint.brush, "texture", new="texture.new", rows=2, cols=6)

            row = box.row()
            row.prop(tex_slot, "tex_paint_map_mode", text="")

            if tex_slot.has_texture_angle:
                row.prop(tex_slot, "angle", text="Angle")
                if tex_slot.map_mode == 'STENCIL':
                    row = box.row()
                    row.operator("brush.stencil_reset_transform", icon='SCREEN_BACK')

                row = box.row()
                if tex_slot.has_texture_angle_source:
                    row.prop(tex_slot, "use_rake", text="Rake")
                    row.prop(tex_slot, "use_random", text="Random")

                    if tex_slot.use_random:
                        row.prop(tex_slot, "random_angle", text="")


# Vertexmode
# -#-- PIE-BLOCK ---- 3_Bottom ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.75

            row = box.row()
            #spl = row.split()
            #row = spl.column()
            #row.scale_x = 1
            row.template_palette(context.tool_settings.vertex_paint, "palette", color=True)

            row = box.row(1)
            spl = row.split()
            row = spl.column()
            row.template_ID_preview(context.tool_settings.vertex_paint, "brush", new="brush.add", rows=2, cols=6)

            row = box.row(1)
            #row.alignment ='CENTER'
            row.template_ID(context.tool_settings.vertex_paint, "palette", new="palette.new")

            """
            row = box.row(1)
            row.alignment ='CENTER'
            row.scale_y = 1.5
            row.scale_x = 1.3           
            row.operator("vertex.draw", text='Draw', icon='BRUSH_MIX')
            #row.operator("vertex.brush", text='Brush', icon='BRUSH_MIX')
            row.operator("paint.brush_select", text='Add', icon='BRUSH_ADD').vertex_paint_tool= 'ADD'
            row.operator("paint.brush_select", text='Substract', icon='BRUSH_SUBTRACT').vertex_paint_tool= 'SUB'                           
            row.operator("paint.brush_select", text='Blur', icon='BRUSH_MIX').vertex_paint_tool= 'BLUR' 
                      
            row = box.row(1)
            row.alignment ='CENTER'            
            row.scale_y = 1.5
            row.scale_x = 1.3
            row.operator("paint.brush_select", text='Mix', icon='BRUSH_MIX').vertex_paint_tool= 'MIX'                                           
            row.operator("paint.brush_select", text='Lighten', icon='BRUSH_LIGHTEN').vertex_paint_tool= 'LIGHTEN'              
            row.operator("paint.brush_select", text='Darken', icon='BRUSH_DARKEN').vertex_paint_tool= 'DARKEN'                           
            row.operator("paint.brush_select", text='Multiply', icon='BRUSH_MULTIPLY').vertex_paint_tool= 'MUL'         
            
            """

            row = box.row()
            row.alignment = 'CENTER'
            row.scale_y = 1.5
            row.scale_x = 1.55

            ups = context.tool_settings.unified_paint_settings
            row.prop(ups, "use_pressure_size", "")
            row.prop(ups, "size", text="Radius", slider=False)
            row.prop(ups, "strength", text="Strength", slider=False)
            row.prop(ups, "use_pressure_strength", "")


# Vertexmode
# -#-- PIE-BLOCK ---- 4_Top ------------------------------------------------
            box = pie.split().box().column()
            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_x = 1.55
            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")
            row.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER").use_hide_panels = True

            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_x = 1
            row.operator("screen.redo_last", text="Settings")
            row.operator("view3d.zoom_border", " ", icon="ZOOM_PREVIOUS")
            row.operator("view3d.view_all", " ", icon="ZOOM_OUT")
            row.operator("ed.undo_history", text="History ")

            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_y = 1.25
            row.operator("brush.curve_preset", icon='SMOOTHCURVE', text=" ").shape = 'SMOOTH'
            row.operator("brush.curve_preset", icon='SPHERECURVE', text=" ").shape = 'ROUND'
            row.operator("brush.curve_preset", icon='ROOTCURVE', text=" ").shape = 'ROOT'
            row.operator("brush.curve_preset", icon='SHARPCURVE', text=" ").shape = 'SHARP'
            row.operator("brush.curve_preset", icon='LINCURVE', text=" ").shape = 'LINE'
            row.operator("brush.curve_preset", icon='NOCURVE', text=" ").shape = 'MAX'


# Vertexmode
# -#-- PIE-BLOCK ---- 5_Top_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1.1

            row = box.row(1)
            row.scale_x = 0.7
            row.prop(view, "use_matcap")
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "show_x_ray", text="X-Ray  ")
            row.operator("object.wire_all", text=" ", icon='WIRE')

            row = box.row()
            row.scale_x = 0.6
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")
            row.prop(context.space_data, "viewport_shade", "", expand=False)


# Vertexmode
# -#-- PIE-BLOCK ---- 6_Top_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            ups = context.tool_settings.unified_paint_settings

            row = box.row()
            row.menu("modeset_edit", "Mode", icon="OBJECT_DATAMODE")
            row.operator("uniset.enable_wp", text=" ", icon="CHECKBOX_HLT")

            row = box.row()
            row.prop(context.tool_settings.vertex_paint, "use_normal")
            row.prop(context.tool_settings.vertex_paint, "use_spray")


# Vertexmode
# -#-- PIE-BLOCK ---- 7_Bottom_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1
            ups = context.tool_settings.unified_paint_settings

            row = box.row()
            row.prop(ups, "color", text="Color", slider=False)

            row = box.row()
            row.alignment = 'CENTER'
            row.scale_x = 1.55
            row.operator("wm.context_toggle", text="", icon="FACESEL_HLT").data_path = "vertex_paint_object.data.use_paint_mask"
            row.operator("paint.sample_color", text="", icon='EYEDROPPER')


# Vertexmode
# -#-- PIE-BLOCK ---- 8_Bottom_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.7

            row = box.row(1)
            row.prop(context.tool_settings.vertex_paint.brush, "stroke_method", "")
            row.prop(context.tool_settings.vertex_paint.brush, "use_smooth_stroke", text="Smooth")

            row = box.row()
            row.scale_x = 1.55

            jitter_meta = toolsettings.vertex_paint.brush.use_relative_jitter
            if jitter_meta == False:
                row.operator("wm.context_toggle", text="", icon="UNLOCKED").data_path = "tool_settings.vertex_paint.brush.use_relative_jitter"
            else:
                row.operator("wm.context_toggle", text="", icon="LOCKED").data_path = "tool_settings.vertex_paint.brush.use_relative_jitter"

            ups = context.tool_settings.vertex_paint.brush
            row.prop(ups, "jitter", text="Jitter", slider=False)
            row.prop(brush, "use_pressure_jitter", toggle=True, text="")

            row = box.row()
            row.scale_x = 1.55
            row.prop(brush, "spacing", text="Spacing")
            row.prop(brush, "use_pressure_spacing", toggle=True, text="")


####### Weightpaint ####### Weightpaint ####### Weightpaint ####### Weightpaint ####### Weightpaint ####### Weightpaint ####### Weightpaint ####### Weightpaint #######

        if ob.mode == 'PAINT_WEIGHT':

            # Weightmode
            # -#-- PIE-BLOCK ---- 1_Left ------------------------------------------------
            box = pie.split().box().column()

            row = box.column(1)
            row.operator("object.vertex_group_normalize_all", text="Normalize All")
            row.operator("object.vertex_group_normalize", text="Normalize")
            row.operator("object.vertex_group_mirror", text="Mirror")
            row.operator("object.vertex_group_invert", text="Invert")
            row.operator("object.vertex_group_clean", text="Clean")
            row.operator("object.vertex_group_quantize", text="Quantize")
            row.operator("object.vertex_group_levels", text="Levels")
            #row.operator("object.vertex_group_blend", text="Blend")


# Weightmode
# -#-- PIE-BLOCK ---- 2_Right ------------------------------------------------
            box = pie.split().box().column()

            row = box.column(1)
            row.operator("object.vertex_group_limit_total", text="Limit Total")
            row.operator("object.vertex_group_fix", text="Fix Deforms")
            row.operator("paint.weight_gradient")
            prop = row.operator("object.data_transfer", text="Transfer Weights")
            prop.use_reverse_transfer = True
            prop.data_type = 'VGROUP_WEIGHTS'
            row.operator("mesh.slope2vgroup", text="Slope")
            row.operator("mesh.height2vgroup", text="Height")
            row.operator("mesh.visiblevertices", text="Visible Vert.")


# Weightmode
# -#-- PIE-BLOCK ---- 3_Bottom ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.75

            row = box.row(1)
            spl = row.split()
            row = spl.column()
            row.template_ID_preview(context.tool_settings.weight_paint, "brush", new="brush.add", rows=2, cols=6)

            """
            
            row = box.row(1)
            row.alignment ='CENTER'
            row.scale_y = 1.5
            row.scale_x = 1.3          
            row.operator("vertex.draw", text='Draw', icon='BRUSH_MIX')
            #row.operator("vertex.brush", text='Brush', icon='BRUSH_MIX')
            row.operator("paint.brush_select", text='Add', icon='BRUSH_ADD').weight_paint_tool= 'ADD'
            row.operator("paint.brush_select", text='Substract', icon='BRUSH_SUBTRACT').weight_paint_tool= 'SUB'                           
            row.operator("paint.brush_select", text='Blur', icon='BRUSH_MIX').weight_paint_tool= 'BLUR' 
                      
            row = box.row(1)
            row.alignment ='CENTER'            
            row.scale_y = 1.5
            row.scale_x = 1.3
            row.operator("paint.brush_select", text='Mix', icon='BRUSH_MIX').weight_paint_tool= 'MIX'                                           
            row.operator("paint.brush_select", text='Lighten', icon='BRUSH_LIGHTEN').weight_paint_tool= 'LIGHTEN'              
            row.operator("paint.brush_select", text='Darken', icon='BRUSH_DARKEN').weight_paint_tool= 'DARKEN'                           
            row.operator("paint.brush_select", text='Multiply', icon='BRUSH_MULTIPLY').weight_paint_tool= 'MUL'         

            """

            row.alignment = 'CENTER'
            ups = context.tool_settings.unified_paint_settings
            row = box.row()
            row.scale_y = 1.5
            row.scale_x = 1.55

            row.prop(ups, "use_pressure_size", text="", toggle=True, icon_only=True)
            row.prop(ups, "size", text="Radius", slider=False)
            row.prop(ups, "strength", text="Strength", slider=False)
            row.prop(ups, "use_pressure_strength", text="", toggle=True, icon_only=True)

            row = box.row()
            row.scale_y = 1.5
            row.prop(ups, "weight", text="Weight", slider=False)


# Weightmode
# -#-- PIE-BLOCK ---- 4_Top ------------------------------------------------
            box = pie.split().box().column()
            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_x = 1.55
            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")
            row.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER").use_hide_panels = True
            #row.operator("screen.screen_full_area", text = "", icon = "FULLSCREEN_ENTER")

            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_x = 1
            row.operator("screen.redo_last", text="Settings")
            row.operator("view3d.zoom_border", " ", icon="ZOOM_PREVIOUS")
            row.operator("view3d.view_all", " ", icon="ZOOM_OUT")
            row.operator("ed.undo_history", text="History ")

            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_y = 1.25
            row.operator("brush.curve_preset", icon='SMOOTHCURVE', text=" ").shape = 'SMOOTH'
            row.operator("brush.curve_preset", icon='SPHERECURVE', text=" ").shape = 'ROUND'
            row.operator("brush.curve_preset", icon='ROOTCURVE', text=" ").shape = 'ROOT'
            row.operator("brush.curve_preset", icon='SHARPCURVE', text=" ").shape = 'SHARP'
            row.operator("brush.curve_preset", icon='LINCURVE', text=" ").shape = 'LINE'
            row.operator("brush.curve_preset", icon='NOCURVE', text=" ").shape = 'MAX'


# Weightmode
# -#-- PIE-BLOCK ---- 5_Top_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(1)
            row.prop(context.tool_settings.weight_paint, "use_spray", "Spray    ")
            row.prop(context.tool_settings.weight_paint, "use_normal")

            row = box.row(1)
            row.prop(obj.data, "use_mirror_x")
            row.prop(obj.data, "use_mirror_topology", "Topology")

            row = box.row(1)
            row.prop(toolsettings, "use_multipaint", text="Multi-Paint")
            row.prop(toolsettings, "use_auto_normalize", text="Auto-Normal")


# Weightmode
# -#-- PIE-BLOCK ---- 6_Top_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row()
            #row.operator("object.editmode_toggle", text=" ", icon = "OBJECT_DATAMODE")
            row.menu("modeset_edit", "Mode   ", icon="OBJECT_DATAMODE")
            row.operator("uniset.enable_wp", text=" ", icon="CHECKBOX_HLT")
            row.prop(context.tool_settings, "vertex_group_user", "")

            row = box.row(1)
            row.prop(context.tool_settings.weight_paint, "use_group_restrict")
            row.operator("mesh.visiblevertices")

            row = box.row(1)
            row.operator("mesh.slope2vgroup")
            row.operator("mesh.height2vgroup")


# Weightmode
# -#-- PIE-BLOCK ---- 7_Bottom_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1.1

            row = box.row(1)
            row.scale_x = 0.7
            row.prop(view, "use_occlude_geometry", text="L2V")
            row.operator("wm.context_toggle", text=" ", icon="FACESEL_HLT").data_path = "weight_paint_object.data.use_paint_mask"
            row.operator("wm.context_toggle", text=" ", icon="VERTEXSEL").data_path = "weight_paint_object.data.use_paint_mask_vertex"

            row = box.row(1)
            row.scale_x = 0.7
            row.prop(view, "use_matcap")
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "show_x_ray", text="X-Ray  ")
            row.operator("object.wire_all", text=" ", icon='WIRE')

            row = box.row()
            row.scale_x = 0.6
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")
            row.prop(context.space_data, "viewport_shade", "", expand=False)


# Weightmode
# -#-- PIE-BLOCK ---- 8_Bottom_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.7

            row = box.row(1)
            row.prop(context.tool_settings.weight_paint.brush, "stroke_method", text="")
            row.operator("wm.context_toggle", text="Smooth").data_path = "tool_settings.weight_paint.brush.use_smooth_stroke"

            row = box.row()
            row.scale_x = 1.55
            jitter_meta = toolsettings.weight_paint.brush.use_relative_jitter
            if jitter_meta == False:
                row.operator("wm.context_toggle", text="", icon="UNLOCKED").data_path = "tool_settings.weight_paint.brush.use_relative_jitter"
            else:
                row.operator("wm.context_toggle", text="", icon="LOCKED").data_path = "tool_settings.weight_paint.brush.use_relative_jitter"
            ups = context.tool_settings.weight_paint.brush

            row.prop(ups, "jitter", text="Jitter", slider=False)
            row.prop(context.tool_settings.weight_paint.brush, "use_pressure_jitter", toggle=True, text="")

            row = box.row()
            row.scale_x = 1.55
            row.prop(context.tool_settings.weight_paint.brush, "spacing", text="Spacing")
            row.prop(context.tool_settings.weight_paint.brush, "use_pressure_spacing", toggle=True, text="")


####### Texturepaint ####### Texturepaint ####### Texturepaint ####### Texturepaint ####### Texturepaint ####### Texturepaint #######

        if ob.mode == 'PAINT_TEXTURE':

            brush = context.tool_settings.image_paint.brush
            mask_tex_slot = brush.mask_texture_slot
            tex_slot = brush.texture_slot

# Texturemode
# -#-- PIE-BLOCK ---- 1_Left ------------------------------------------------

            box = pie.split().box().column()

            box.scale_x = 0.75
            row = box.row()
            spl = row.split()
            row = spl.column()
            row.template_ID_preview(brush, "mask_texture", new="texture.new", rows=3, cols=8)

            row = box.row()

            row.prop(mask_tex_slot, "mask_map_mode", text="")

            if mask_tex_slot.has_texture_angle:
                row.prop(mask_tex_slot, "angle", text="Angle")
                if mask_tex_slot.map_mode == 'STENCIL':
                    row = box.row()
                    row.operator("brush.stencil_reset_transform", icon='SCREEN_BACK').mask = True

                row = box.row()
                if mask_tex_slot.has_texture_angle_source:
                    row.prop(mask_tex_slot, "use_rake", text="Rake")
                    row.prop(mask_tex_slot, "use_random", text="Random")

                    if mask_tex_slot.use_random:
                        col.prop(mask_tex_slot, "random_angle", text="")


# Texturemode
# -#-- PIE-BLOCK ---- 2_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.75

            row = box.row()
            spl = row.split()
            row = spl.column()
            row.template_ID_preview(context.tool_settings.image_paint.brush, "texture", new="texture.new", rows=2, cols=6)

            row = box.row()
            row.prop(tex_slot, "tex_paint_map_mode", text="")

            if tex_slot.has_texture_angle:
                row.prop(tex_slot, "angle", text="Angle")
                if tex_slot.map_mode == 'STENCIL':
                    row = box.row()
                    row.operator("brush.stencil_reset_transform", icon='SCREEN_BACK')

                row = box.row()
                if tex_slot.has_texture_angle_source:
                    row.prop(tex_slot, "use_rake", text="Rake")
                    row.prop(tex_slot, "use_random", text="Random")

                    if tex_slot.use_random:
                        row.prop(tex_slot, "random_angle", text="")


# Texturemode
# -#-- PIE-BLOCK ---- 3_Bottom ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.65

            row = box.row()
            #spl = row.split()
            #row = spl.column()
            row.scale_x = 1.25
            row.template_palette(settings, "palette", color=True)

            row = box.row(1)
            spl = row.split()
            row = spl.column()
            row.template_ID_preview(context.tool_settings.image_paint, "brush", new="brush.add", rows=2, cols=6)

            row = box.row(1)
            #row.alignment ='CENTER'
            row = box.row()
            row.template_ID(settings, "palette", new="palette.new")

            row = box.row(1)
            row.alignment = 'CENTER'
            ups = context.tool_settings.unified_paint_settings
            row = box.row()
            row.scale_y = 1.5
            row.scale_x = 1.55
            row.prop(ups, "use_pressure_size", text="", toggle=True, icon_only=True)
            row.prop(ups, "size", text="Radius", slider=False)
            row.prop(ups, "strength", text="Strength", slider=False)
            row.prop(ups, "use_pressure_strength", text="", toggle=True, icon_only=True)

            row = box.row(1)
            row.alignment = 'CENTER'
            row.prop(brush, "use_alpha")
            row.prop(brush, "use_gradient", "Gradient")
            row.prop(brush, "use_accumulate")

            row = box.row()
            spl = row.split()
            row = spl.column()
            if brush.use_gradient:
                row.template_color_ramp(brush, "gradient", expand=True)

                if brush.image_tool == 'DRAW':
                    row = box.row(1)
                    row.prop(brush, "gradient_stroke_mode", text="")

                    if brush.gradient_stroke_mode in {'SPACING_REPEAT', 'SPACING_CLAMP'}:
                        row.prop(brush, "grad_spacing")

                elif brush.image_tool == 'FILL':
                    row = box.row(1)
                    row.prop(brush, "gradient_fill_mode", text="")

            if brush.image_tool == 'FILL':
                row.prop(brush, "fill_threshold")


# Texturemode
# -#-- PIE-BLOCK ---- 4_Top ------------------------------------------------

            box = pie.split().box().column()
            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_x = 1.55
            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")
            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")
            row.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER").use_hide_panels = True

            if context.space_data.type == 'VIEW_3D' and context.mode == 'PAINT_TEXTURE':
                row = box.row(1)
                row.alignment = 'CENTER'
                row.scale_x = 1
                row.operator("image.save_dirty", text="Save All Images")
                row.prop(context.tool_settings.image_paint, "use_stencil_layer", text="Mask")
                row.operator("ed.undo_history", text="History ")

            else:
                row = box.row(1)
                row.alignment = 'CENTER'
                row.scale_x = 1
                row.prop(context.tool_settings.image_paint.brush, "use_wrap")
                row.menu("IMAGE_MT_image_invert", text=" Invert")
                row.operator("ed.undo_history", text="History ")

            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_y = 1.25
            row.operator("brush.curve_preset", icon='SMOOTHCURVE', text=" ").shape = 'SMOOTH'
            row.operator("brush.curve_preset", icon='SPHERECURVE', text=" ").shape = 'ROUND'
            row.operator("brush.curve_preset", icon='ROOTCURVE', text=" ").shape = 'ROOT'
            row.operator("brush.curve_preset", icon='SHARPCURVE', text=" ").shape = 'SHARP'
            row.operator("brush.curve_preset", icon='LINCURVE', text=" ").shape = 'LINE'
            row.operator("brush.curve_preset", icon='NOCURVE', text=" ").shape = 'MAX'


# Texturemode
# -#-- PIE-BLOCK ---- 5_Top_Left ------------------------------------------------
            box = pie.split().box().column()

            if context.space_data.type == 'VIEW_3D' and context.mode == 'PAINT_TEXTURE':

                box.scale_x = 1.25
                row = box.row(1)
                row.scale_x = 0.7

                row.prop(context.space_data, "use_matcap")
                row.prop(context.object, "show_x_ray", text="X-Ray  ")
                row.operator("object.wire_all", text=" ", icon='WIRE')

                row = box.row()
                row.scale_x = 0.6
                row.scale_y = 0.17
                row.template_icon_view(context.space_data, "matcap_icon")
                row.prop(context.space_data, "viewport_shade", "", expand=False)

            else:

                box.scale_x = 1
                row = box.row(1)
                row.operator("image.external_edit", icon="GO_LEFT")

                row = box.row(1)

                row.scale_x = 1.55
                row.prop(context.space_data, "use_image_pin", text="")
                row.prop(context.space_data, "draw_channels", text="")

                row = box.row(1)
                row.scale_x = 1.55
                row.prop(context.space_data, "use_realtime_update", icon_only=True, icon='LOCKED')
                row.prop(context.tool_settings.image_paint.brush, "blend", text="", icon="LIGHTPAINT")


# Texturemode
# -#-- PIE-BLOCK ---- 6_Top_Right ------------------------------------------------
            box = pie.split().box().column()

            if context.space_data.type == 'VIEW_3D' and context.mode == 'PAINT_TEXTURE':

                box.scale_x = 0.9
                ups = context.tool_settings.unified_paint_settings

                row = box.row()
                row.scale_x = 1.55
                row.menu("modeset_edit", "Mode", icon="OBJECT_DATAMODE")

                row = box.row()
                row.prop(context.tool_settings.image_paint, "use_normal_falloff")
                row.prop(context.tool_settings.image_paint, "use_occlude")
                row.prop(context.tool_settings.image_paint, "use_backface_culling")

                row = box.row()
                row.prop(context.tool_settings.image_paint, "normal_angle", text="")
                row.prop(context.tool_settings.image_paint, "seam_bleed")

            else:
                box.scale_x = 0.7
                ups = context.tool_settings.unified_paint_settings

                row = box.row()
                row.scale_x = 1.55

                row.prop(context.space_data, "mode", text="")
                row.operator("object.view_menu", text="3D", icon='VIEW3D').variable = "VIEW_3D"

                row.prop(context.space_data, "show_repeat", text="Repeat")

                row = box.row()
                row.prop(context.tool_settings.image_paint, "use_normal_falloff")
                row.prop(context.tool_settings.image_paint, "use_occlude")
                row.prop(context.tool_settings.image_paint, "use_backface_culling")

                row = box.row()
                row.prop(context.tool_settings.image_paint, "normal_angle", text="")
                row.prop(context.tool_settings.image_paint, "seam_bleed")


# Texturemode
# -#-- PIE-BLOCK ---- 7_Bottom_Left ------------------------------------------------
            box = pie.split().box().column()

            if context.space_data.type == 'VIEW_3D' and context.mode == 'PAINT_TEXTURE':

                box.scale_x = 0.65
                box.scale_y = 0.95
                ups = context.tool_settings.unified_paint_settings

                row = box.row(1)
                row.alignment = 'CENTER'
                row.operator("uniset.enable_wp", text="", icon="CHECKBOX_HLT")
                row.prop(ups, "color", text="", slider=False)
                row.prop(ups, "secondary_color", text="", slider=True)
                row = box.row()
                row.scale_x = 1.55
                row.prop(brush, "use_pressure_masking", text="")
                if brush.mask_texture and brush.mask_texture.type == 'IMAGE':
                    row.operator("brush.stencil_fit_image_aspect", "", icon="ASSET_MANAGER").mask = True

                row.operator("wm.context_toggle", text="", icon="FACESEL_HLT").data_path = "object.data.use_paint_mask"
                row.operator("paint.sample_color", text="", icon='EYEDROPPER')
                row.operator("paint.brush_colors_flip", icon='FILE_REFRESH', text="")

            else:

                box.scale_x = 0.8
                box.scale_y = 0.95
                ups = context.tool_settings.unified_paint_settings

                row = box.row(1)
                row.alignment = 'CENTER'
                # row.label()
                row.scale_x = 2
                row.operator("uniset.enable_wp", text="", icon="CHECKBOX_HLT")
                row.prop(ups, "color", text="", slider=True)
                row.prop(ups, "secondary_color", text="", slider=True)

                row = box.row()
                row.scale_x = 1.55
                row.prop(brush, "use_pressure_masking", text="")
                if brush.mask_texture and brush.mask_texture.type == 'IMAGE':
                    row.operator("brush.stencil_fit_image_aspect", "", icon="ASSET_MANAGER").mask = True

                row.operator("paint.sample_color", text="", icon='EYEDROPPER')
                row.operator("paint.brush_colors_flip", icon='FILE_REFRESH', text="")

                row = box.row()
                row.prop(context.tool_settings.image_paint, "mode", text="")
                row.operator("wm.context_toggle", text=" ", icon="FACESEL_HLT").data_path = "image_paint_object.data.use_paint_mask"


# Texturemode
# -#-- PIE-BLOCK ---- 8_Bottom_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.7

            row = box.row(1)
            row.prop(context.tool_settings.image_paint.brush, "stroke_method", text="")
            row.prop(context.tool_settings.image_paint.brush, "use_smooth_stroke", text="Smooth")

            row = box.row()
            row.scale_x = 1.5
            jitter_meta = context.tool_settings.image_paint.brush.use_relative_jitter
            if jitter_meta == False:
                row.operator("wm.context_toggle", text="", icon="UNLOCKED").data_path = "tool_settings.image_paint.brush.use_relative_jitter"
            else:
                row.operator("wm.context_toggle", text="", icon="LOCKED").data_path = "tool_settings.image_paint.brush.use_relative_jitter"

            if brush.use_relative_jitter:
                row.prop(brush, "jitter", "Jitter", slider=True)
            else:
                row.prop(brush, "jitter_absolute", "Jitter")
            row.prop(brush, "use_pressure_jitter", toggle=True, text="")

            if brush.use_anchor:
                row = box.row()
                row.prop(brush, "use_edge_to_edge", "Edge To Edge")

            if brush.use_airbrush:
                row = box.row()
                row.prop(brush, "rate", text="Rate", slider=True)

            if brush.use_space:
                row = box.row()
                row.scale_x = 1.55
                row.prop(brush, "spacing", text="Spacing")
                row.prop(brush, "use_pressure_spacing", toggle=True, text="")

            if brush.use_line:
                row = box.row()
                row.prop(brush, "spacing", text="Spacing")

            if brush.use_curve:
                row = box.row()
                row.scale_x = 0.6
                row.operator("paintcurve.draw", " ", icon="BRUSH_DATA")
                row.prop(brush, "spacing", text="Spacing")
                row.template_ID(brush, "paint_curve", new="paintcurve.new")


####### Particle ####### Particle ####### Particle ####### Particle ####### Particle ####### Particle #######

        if ob.mode == 'PARTICLE':
            pe = context.tool_settings.particle_edit


# Particle
# -#-- PIE-BLOCK ---- 1_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1.5
            row = box.column_flow(2)

            row.operator("particle.select_all", "All").action = 'TOGGLE'
            row.operator("particle.select_more", "More")
            row.operator("particle.select_less", "Less")
            row.operator("particle.select_random", "Random")

            row.operator("particle.select_tips", text="Tips")
            row.operator("particle.select_roots", text="Roots")
            row.operator("particle.select_all", text="Inverse").action = 'INVERT'
            row.operator("particle.select_linked", "Linked")


# Particle
# -#-- PIE-BLOCK ---- 2_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.75

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            row.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            row.operator("view3d.pivot_active", "", icon="ROTACTIVE")
            row.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            row.operator("view3d.pivot_median", "", icon="ROTATECENTER")

            row = box.row(align=True)
            row.scale_x = 2
            row.operator("snape.increment", "", icon="SNAP_INCREMENT")
            row.operator("snape.vertex", "", icon="SNAP_VERTEX")
            row.operator("snape.edge", "", icon="SNAP_EDGE")
            row.operator("snape.face", "", icon="SNAP_FACE")
            row.operator("snape.volume", "", icon="SNAP_VOLUME")

            row = box.row(align=True)
            row.scale_x = 1.3
            view = context.space_data
            toolsettings = context.tool_settings
            row.prop(view, "use_occlude_geometry", text="", icon="ORTHO")
            row.menu("htk_pivotorient", "Orientation", icon="EMPTY_DATA")
            row.prop(toolsettings, "use_snap_self", text="")

            row = box.row(align=True)
            row.scale_x = 1.3

            snap_meta = toolsettings.use_snap
            if snap_meta == False:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
            else:
                row.operator("wm.context_toggle", text="", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"
            row.menu("htk_snaptarget", "Snap Target", icon="SNAP_ON")
            row.prop(toolsettings, "use_snap_project", text="")

            row = box.row(align=True)
            toolsettings = context.tool_settings
            row.prop(toolsettings, "proportional_edit", icon_only=True)
            row.prop(toolsettings, "proportional_edit_falloff", icon_only=True)
            row.operator("view3d.ruler", text="Ruler")  # , icon="NOCURVE")

            row = box.row(align=True)
            row.operator("view3d.localview", text="Global/Local")
            row.operator("view3d.view_persportho", text="Persp/Ortho")


# Particle
# -#-- PIE-BLOCK ---- 3_Bottom ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_x = 1.55
            row.operator("particle.path_select", text='', icon='PARTICLE_PATH')
            row.operator("particle.tip_select", text='', icon='PARTICLE_TIP')
            row.operator("particle.point_select", text='', icon='PARTICLE_POINT')

            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_y = 1.5
            row.scale_x = 1.3
            #row.operator("particle.none_select", text='None', icon='BRUSH_TEXDRAW')
            row.operator("particle.comb_select", text='Comb', icon='BRUSH_TEXDRAW')
            row.operator("particle.smooth_select", text='Smooth', icon='BRUSH_TEXDRAW')
            row.operator("particle.add_select", text='Add', icon='BRUSH_TEXDRAW')

            row = box.row(1)
            row.alignment = 'CENTER'
            row.scale_y = 1.5
            row.scale_x = 1.3
            row.operator("particle.length_select", text='Length', icon='BRUSH_TEXDRAW')
            row.operator("particle.puff_select", text='Puff', icon='BRUSH_TEXDRAW')
            row.operator("particle.cut_select", text='Cut', icon='BRUSH_TEXDRAW')
            row.operator("particle.weight_select", text='Weight', icon='BRUSH_TEXDRAW')

            row = box.column_flow(4)

            row.scale_x = 1.3
            brush = context.tool_settings.particle_edit.brush

            # 1
            row.label("Add:")
            row.label("Lenght:")

            row.active = pe.is_editable
            row.prop(pe, "use_emitter_deflect", text="Deflect")

            row.prop(pe, "type", text="")

            # 2
            row.prop(brush, "count")
            row.prop(brush, "length_mode", "")

            row.active = pe.use_emitter_deflect
            row.prop(pe, "emitter_distance", text="Distance")

            row.prop(pe, "draw_step", text="Path Steps")

            # 3
            row.prop(pe, "use_preserve_length", text="Lengths")
            row.label("Puff:")

            ob = pe.object
            row.prop(ob.data, "use_mirror_x")

            row.operator("particle.shape_cut")

            # 4
            row.prop(pe, "use_preserve_root", text="Root")
            row.prop(brush, "puff_mode", "")
            row.prop(brush, "use_puff_volume")

            row.prop(pe, "shape_object", "")


# Particle
# -#-- PIE-BLOCK ---- 4_Top ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.65

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55
            row.operator("screen.region_quadview", text="", icon="SPLITSCREEN")
            row.operator("screen.redo_last", text="Settings ")
            row.operator("wm.search_menu", text="", icon='VIEWZOOM')
            row.operator("ed.undo_history", text="History")
            row.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER").use_hide_panels = True

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55

            row.operator("ed.undo", text="", icon="LOOP_BACK")
            row.menu("VIEW3D_MT_particle_showhide", "", icon="VISIBLE_IPO_ON")
            row.operator("ed.redo", text="", icon="LOOP_FORWARDS")

            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.scale_x = 1.55

            row.operator("view3d.select_border", text="", icon="BORDER_RECT")
            row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")
            row.menu("pie.mt_selection", text="", icon="HAND")
            row.operator("view3d.zoom_border", "", icon="ZOOM_PREVIOUS")
            row.operator("view3d.view_all", "", icon="ZOOM_OUT")


# Particle
# -#-- PIE-BLOCK ---- 5_Top_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 0.85
            row = box.row(1)

            particle_edit = context.tool_settings.particle_edit

            row.operator("particle.mirror")

            if particle_edit.select_mode == 'POINT':
                row.operator("particle.subdivide")

            row = box.row(1)

            row.operator("particle.rekey")
            row.operator("particle.weight_set")


# Particle
# -#-- PIE-BLOCK ---- 6_Top_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1
            row = box.row(1)
            #row.operator("object.editmode_toggle", text=" ", icon = "OBJECT_DATAMODE")
            row.menu("modeset_object", "Mode     ", icon="OBJECT_DATAMODE")

            row.operator("particle.delete", icon="PANEL_CLOSE")

            row = box.row(1)
            pe = context.tool_settings.particle_edit
            row.prop(pe, "show_particles", text="Children")

            row.operator("particle.remove_doubles", "Doubles", icon="PANEL_CLOSE")


# Particle
# -#-- PIE-BLOCK ---- 7_Bottom_Left ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1.1

            row = box.row(1)
            row.scale_x = 0.7
            row.prop(view, "use_matcap")
            if bpy.context.area.type == 'VIEW_3D' and bpy.context.object:
                row.prop(obj, "show_x_ray", text="X-Ray  ")
            row.operator("object.wire_all", text=" ", icon='WIRE')

            row = box.row()
            row.scale_x = 0.6
            row.scale_y = 0.17
            row.template_icon_view(view, "matcap_icon")
            row.prop(context.space_data, "viewport_shade", "", expand=False)


# Particle
# -#-- PIE-BLOCK ---- 8_Bottom_Right ------------------------------------------------
            box = pie.split().box().column()
            box.scale_x = 1

            row = box.column(1)
            #row = box.row()

            brush = context.tool_settings.particle_edit.brush

            row.prop(brush, "size", slider=True)
            row.prop(brush, "strength", slider=True)

            #pe = context.tool_settings.particle_edit
            #ob = pe.object
            #row = box.row(1)
            #row.prop(pe, "type", text="")


##########################################################################################
#######   Sub Menu   #######   Sub Menu   #######   Sub Menu  #######   Sub Menu   #######

class ExpandButton(bpy.types.Menu):
    """TABs"""

    bl_label = "TAB Menus"
    bl_idname = "expandbutton"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.prop(bpy.context.scene, "osc_uvs", text="UVs", icon="UV_FACESEL")
        layout.prop(bpy.context.scene, "osc_material", text="Material", icon="MATERIAL")
        layout.prop(bpy.context.scene, "osc_arrays", text="Arrays", icon="MOD_ARRAY")
        layout.prop(bpy.context.scene, "osc_relation", text="Relation", icon="CONSTRAINT_DATA")

        layout.prop(bpy.context.scene, "osc_setup", text="Setup", icon="RESTRICT_SELECT_OFF")
        layout.prop(bpy.context.scene, "osc_scene", text="Scene", icon="RENDER_ANIMATION")
        layout.prop(bpy.context.scene, "osc_layer", text="Layer Mg.", icon="COLLAPSEMENU")
        layout.prop(bpy.context.scene, "osc_grouper", text="SGrouper", icon="RENDER_ANIMATION")

        layout.prop(bpy.context.scene, "osc_arewo", text="Arewo", icon="DRIVER")
        layout.prop(bpy.context.scene, "osc_sniper", text="Sniper", icon="DRIVER")
        layout.prop(bpy.context.scene, "osc_vfx", text="VFX-Tool", icon="DRIVER")

        layout.prop(bpy.context.scene, "osc_pathtex", text="Textur", icon="LOGIC")
        layout.prop(bpy.context.scene, "osc_snapshot", text="Snapshot", icon="OUTLINER_DATA_CAMERA")
        layout.prop(bpy.context.scene, "osc_quickpref", text="QuickPref", icon="LAMP_DATA")

bpy.utils.register_class(ExpandButton)


class ModeSet_Object(bpy.types.Menu):
    bl_label = "Mode Set"
    bl_idname = "modeset_object"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator("object.editmode_toggle", text="Objectmode", icon="EDIT")
        layout.operator("sculpt.sculptmode_toggle", text="Sculptmode", icon="SCULPTMODE_HLT")
        layout.operator("paint.vertex_paint_toggle", text="Vertexpaint", icon="VPAINT_HLT")
        layout.operator("paint.weight_paint_toggle", text="Weightpaint", icon="WPAINT_HLT")
        layout.operator("paint.texture_paint_toggle", text="Texturepaint", icon="TPAINT_HLT")


bpy.utils.register_class(ModeSet_Object)


class ModeSet_Edit(bpy.types.Menu):
    bl_label = "Mode Set"
    bl_idname = "modeset_edit"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        obj = context.active_object
        if obj:
            obj_type = obj.type

            if obj_type in {'CURVE', 'SURFACE', 'LATTICE', 'META', 'FONT'}:
                layout.operator_context = 'INVOKE_REGION_WIN'
                layout.operator("object.editmode_toggle", text="Editmode", icon="EDIT")

            if obj_type in {'EDIT_MESH', 'MESH'}:
                layout.operator_context = 'INVOKE_REGION_WIN'
                layout.operator("object.editmode_toggle", text="Editmode", icon="EDIT")
                layout.operator("sculpt.sculptmode_toggle", text="Sculptmode", icon="SCULPTMODE_HLT")
                layout.operator("paint.vertex_paint_toggle", text="Vertexpaint", icon="VPAINT_HLT")
                layout.operator("paint.weight_paint_toggle", text="Weightpaint", icon="WPAINT_HLT")
                layout.operator("paint.texture_paint_toggle", text="Texturepaint", icon="TPAINT_HLT")
                layout.operator("particle.particle_edit_toggle", text="Particlemode", icon="EDIT")

            if obj_type in {'POSE', 'ARMATURE'}:
                layout.operator("object.editmode_toggle", text="Editmode", icon="EDIT")
                layout.operator("object.posemode_toggle", text="Posemode", icon="POSE_HLT")


bpy.utils.register_class(ModeSet_Edit)


######################################################################################################
#######  Operator  #######  Operator  #######  Operator  #######  Operator  #######  Operator  #######


class UNISET_WP(bpy.types.Operator):
    """Enable Unified Settings"""
    bl_label = "enable Unified Settings"
    bl_idname = "uniset.enable_wp"

    def execute(self, context):

        bpy.context.scene.tool_settings.unified_paint_settings.use_unified_size = True
        bpy.context.scene.tool_settings.unified_paint_settings.use_unified_weight = True
        bpy.context.scene.tool_settings.unified_paint_settings.use_unified_strength = True
        bpy.context.scene.tool_settings.unified_paint_settings.use_unified_color = True

        return {'FINISHED'}

bpy.utils.register_class(UNISET_WP)


###########################################################################################
###########################################################################################

mod_data = [tuple(["meshes"] * 3), tuple(["armatures"] * 3),
            tuple(["cameras"] * 3), tuple(["curves"] * 3),
            tuple(["fonts"] * 3), tuple(["grease_pencil"] * 3),
            tuple(["groups"] * 3), tuple(["images"] * 3),
            tuple(["lamps"] * 3), tuple(["lattices"] * 3),
            tuple(["libraries"] * 3), tuple(["materials"] * 3),
            tuple(["actions"] * 3), tuple(["metaballs"] * 3),
            tuple(["node_groups"] * 3), tuple(["objects"] * 3),
            tuple(["sounds"] * 3), tuple(["texts"] * 3),
            tuple(["textures"] * 3), ]


def abs(val):
    if val > 0:
        return val
    return -val


###########################################################################################################
#######  Registery  #######  Registery  #######  Registery  #######  Registery  #######  Registery  #######


def register():
    bpy.utils.register_class(VIEW3D_EditPIE)

    bpy.types.Scene.Preserve_Location_Rotation_Scale = bpy.props.BoolProperty(name="Preserve Location/Rotation/Scale", description="Preserve the Location/Rotation/Scale values of the objects.", default=True)
    bpy.types.Scene.mod_list = bpy.props.EnumProperty(name="Target", items=mod_data, description="Module choice made for orphan deletion")

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:

        # change here the Location of your Menu_1
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')

        # change here the Hotkey of your Menu
        kmi = km.keymap_items.new('wm.call_menu_pie', 'SPACE', 'PRESS')

        # your idname for the menu
        kmi.properties.name = "meta.edit_pie"


def unregister():
    bpy.utils.unregister_class(VIEW3D_EditPIE)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:

        # change here the Location of your Menu_1
        km = kc.keymaps['3D View']

        ##########################
        for kmi in km.keymap_items:
            if kmi.idname == 'wm.call_menu_pie':
                if kmi.properties.name == "":
                    km.keymap_items.remove(kmi)
                    break


if __name__ == "__main__":
    register()

    # test the script inside blender text editor
    bpy.ops.wm.call_menu_pie(name="VIEW3D_EditPIE")
