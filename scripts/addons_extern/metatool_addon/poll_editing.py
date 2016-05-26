# bl_info = {
#    "name": "Extension Add",
#    "author": "marvin.k.breuer",
#    "version": (0, 1, 0),
#    "blender": (2, 72, 0),
#    "location": "View3D > Toolbar",
#    "warning": "",
#    "description": "Toolkit Extension",
#    "wiki_url": "",
#    "category": "User Panel",
#}


import bpy
from bpy import *

##########################################################
###----------------  EDITING  -------------------------###
###----------------  EDITING  -------------------------###
##########################################################


# Sub Location
class SubLoc_EDIT():
    """EDIT Tools"""
    bl_category = "META"
    #bl_region_type = 'TOOLS'
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(cls, context):
        return context.scene.osc_editing

# Sub Panel


class META_TAB_EDIT(SubLoc_EDIT, bpy.types.Panel):
    """Complete Edit Tools"""
    bl_idname = "complete_tools"
    bl_label = "[COMPACT TOOLS (WIP)]"

    def draw(self, context):
        lt = context.window_manager.metawindow
        layout = self.layout
        mesh = context.active_object.data
        obj = context.object
        scene = context.scene

        col = layout.column(align=True)

        ### modespace a ###

        if obj.mode == 'OBJECT':
            ### modespace b ###

            # -------------------------------------------------------
            # Im-Export  #######-------------------------------------------------------
            # Im-Export  #######-------------------------------------------------------
            # -------------------------------------------------------

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_imexport:
                split.prop(lt, "display_cpt_imexport", text="...Im-Export...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_imexport", text="...Im-Export...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_cpt_imexport:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.menu("INFO_MT_file_import", icon='IMPORT')
                #row = col_top.row(align=True)
                row.menu("INFO_MT_file_export", icon='EXPORT')
                row = col_top.row(align=True)
                row.menu("OBJECT_MT_selected_export", text="Export Selected", icon='EXPORT')

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator_context = 'INVOKE_AREA'
                row.operator("wm.link", text="Link", icon='LINK_BLEND')
                row.operator("wm.append", text="Append", icon='APPEND_BLEND')

                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("object.make_local")
                row.operator("object.proxy_make")

                split = col.split()  # percentage=0.15)

                if lt.display_cpt_imexmanage:
                    split.prop(lt, "display_cpt_imexmanage", text="...Pack & Pathes...", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_imexmanage", text="...Pack & Pathes...", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #spread_op = split.operator("", text="", icon="")

                if lt.display_cpt_imexmanage:

                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    pack_all = box.row()
                    pack_all.operator("file.pack_all")
                    pack_all.active = not bpy.data.use_autopack

                    unpack_all = box.row()
                    unpack_all.operator("file.unpack_all")
                    unpack_all.active = not bpy.data.use_autopack

                    icon = 'CHECKBOX_HLT' if bpy.data.use_autopack else 'CHECKBOX_DEHLT'
                    row.operator("file.autopack_toggle", text="autom. Pack into .blend", icon=icon)

                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("file.make_paths_relative")

                    row = col_top.row(align=True)
                    row.operator("file.make_paths_absolute")

                    row = col_top.row(align=True)
                    row.operator("file.report_missing_files")

                    row = col_top.row(align=True)
                    row.operator("file.find_missing_files")

                split = col.split()  # percentage=0.15)

                if lt.display_cpt_imexfolder:
                    split.prop(lt, "display_cpt_imexfolder", text="...Production Setup...", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_imexfolder", text="...Production Setup...", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #spread_op = split.operator("", text="", icon="")

                if lt.display_cpt_imexfolder:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("productionfolder_scene.selected", text="Create Production Folder", icon="FILE_FOLDER")

                    row = col_top.row(align=True)
                    row.operator("production_scene.selected", text="Save Production Scene", icon="FILE_TICK")

                    row = col_top.row(align=True)
                    row.operator("file.production_folder", text="Show Production Folder", icon="GO_LEFT")

                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("image.imagesave", text="Collect Image Folder", icon="IMAGE_COL")

                #col = layout.column(align=True)

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Add Geometry   #######-------------------------------------------------------
    # Add Geometry   #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()
            if lt.display_cpt_geom:
                split.prop(lt, "display_cpt_geom", text="...Geometry...", icon='DOWNARROW_HLT')

            else:
                split.prop(lt, "display_cpt_geom", text="...Geometry...", icon='RIGHTARROW')

            #spread_op = row.menu("INFO_MT_add",text="", icon="OBJECT_DATAMODE")

            if lt.display_cpt_geom:

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.menu("INFO_MT_mesh_add", text="", icon='OUTLINER_OB_MESH')
                row.menu("INFO_MT_curve_add", text="", icon='OUTLINER_OB_CURVE')
                row.menu("INFO_MT_surface_add", text="", icon='OUTLINER_OB_SURFACE')
                row.menu("INFO_MT_metaball_add", text="", icon="OUTLINER_OB_META")
                row.operator("object.armature_add", text="", icon="OUTLINER_OB_ARMATURE")
                row.operator("object.lamp_add", icon='OUTLINER_OB_LAMP', text="")
                row.operator("object.bounding_boxers", text="", icon="BBOX")

                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.operator_menu_enum("object.effector_add", "type", text="", icon="SOLO_ON")
                row.operator("object.text_add", text="", icon="OUTLINER_OB_FONT")
                row.operator("object.speaker_add", icon='OUTLINER_OB_SPEAKER', text="")
                row.operator("object.camera_add", icon='OUTLINER_OB_CAMERA', text="")
                row.operator("object.add", text="", icon="OUTLINER_OB_LATTICE").type = "LATTICE"
                row.operator("object.empty_add", text="", icon="OUTLINER_OB_EMPTY")
                row.operator("mesh.emptyroom_cen", text="", icon='RETOPO')

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                if len(bpy.data.groups) > 10:
                    row.operator_context = 'INVOKE_REGION_WIN'
                    row.operator("object.group_instance_add", text="Group Instance...", icon='OUTLINER_OB_EMPTY')
                else:
                    row.operator_menu_enum("object.group_instance_add", "group", text="Group Instance", icon='OUTLINER_OB_EMPTY')

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("object.name_objects", icon="OUTLINER_DATA_FONT")

                row = col_top.row(align=True)
                row.operator("object.vertices_numbers3d", icon="MESH_DATA")

                if context.selected_objects:
                    if context.selected_objects[0].type == 'MESH':

                        row = col_top.row(align=True)
                        row.operator("object.connect2objects", icon="MESH_DATA")

                        row = col_top.row(align=True)
                        row.prop(bpy.context.scene, "shift_verts", text="shift")

                        row = col_top.row(align=True)
                        row.prop(bpy.context.scene, "hook_or_not", text="hook new vertices?")

                box = col.column(align=True).box().column()

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("set.tmpcamera", text="BoxCamera", icon="FACESEL_HLT")
                col_top = box.column(align=True)
                row.label("Timeline 1-2-3 Key")

                box = col.column(align=True).box().column()

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("object.add_fracture_cell_objects", text="Cell Fracture")
                row.menu("VIEW3D_MT_object_quick_effects")

                box = col.column(align=True).box().column()

        # -------------------------------------------------------
        # Animation  #######-------------------------------------------------------
        # Animation  #######-------------------------------------------------------
        # -------------------------------------------------------

            ###space###

            view = context.space_data
            obj = bpy.context.scene.objects.active
            scene = context.scene
            toolsettings = context.tool_settings
            screen = context.screen
            self.scn = context.scene

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()
            if lt.display_cpt_anim:
                split.prop(lt, "display_cpt_anim", text="...Animation...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_anim", text="...Animation...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_cpt_anim:

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
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

                        box = col.column(align=True).box().column()
                        col_top = box.column(align=True)
                        row = col_top.row(align=True)

                        row.operator("anim.keyframe_insert_menu", icon='ZOOMIN', text="")
                        row.operator("anim.keyframe_delete_v3d", icon='ZOOMOUT', text="")
                        row.prop_search(context.scene.keying_sets_all, "active", context.scene, "keying_sets_all", text="")
                        row.operator("anim.keyframe_insert", text="", icon='KEY_HLT')
                        row.operator("anim.keyframe_delete", text="", icon='KEY_DEHLT')

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.prop(scene, "use_preview_range", text="", toggle=True)
                row.prop(scene, "lock_frame_selection_to_range", text="", toggle=True)

                row.prop(scene, "frame_current", text="")

                row = col_top.row(align=True)
                if not scene.use_preview_range:
                    row.prop(scene, "frame_start", text="Start")
                    row.prop(scene, "frame_end", text="End")
                else:
                    row.prop(scene, "frame_preview_start", text="Start")
                    row.prop(scene, "frame_preview_end", text="End")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("object.paths_calculate", text="Calculate Motion Path", icon="ANIM_DATA")
                row = col_top.row(align=True)
                row.operator("object.paths_clear", text="Clear Path Catch", icon="PANEL_CLOSE")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("nla.bake", text="Bake new Action", icon="ACTION_TWEAK")

                box = col.column(align=True).box().column()

        # -------------------------------------------------------
        # Render  #######-------------------------------------------------------
        # Render  #######-------------------------------------------------------
        # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()
            if lt.display_cpt_render:
                split.prop(lt, "display_cpt_render", text="...Render...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_render", text="...Render...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_cpt_render:

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("render.render", text="Still", icon='RENDER_STILL')
                row.operator("render.render", text="Animation", icon='RENDER_ANIMATION').animation = True

                row = col_top.row(align=True)
                row.operator("render.opengl", text="Still_OpGL", icon='RENDER_STILL')
                row.operator("render.opengl", text="Anim_OpGL", icon='RENDER_ANIMATION').animation = True

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.operator("render.play_rendered_anim", text="Play rendered Animation", icon='PLAY')

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # CadTools  #######-------------------------------------------------------
    # CadTools  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_cadtools:
                split.prop(lt, "display_cpt_cadtools", text="...CAD...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_cadtools", text="...CAD...", icon='RIGHTARROW')

            #split.operator("", text = "", icon = "")

            if lt.display_cpt_cadtools:
                box = col.column(align=True).box().column()

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("object.set_instance", icon="LINKED")
                row.operator("mesh.intersect_meshes", text="Intersection", icon="GROUP")

                row = col_top.row(align=True)
                row.operator("retopo.latticeapply", "Apply E-Lattice", icon="OUTLINER_DATA_LATTICE")
                row.operator("object.editnormals_transfer", text="Transfer Normals", icon="SNAP_NORMAL")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("object.convert", text="Convert to Curve", icon="CURVE_DATA").target = "CURVE"
                row = col_top.row(align=True)
                row.operator("object.convert", text="Convert to Mesh", icon="MESH_DATA").target = "MESH"

                col_top = box.column(align=True)
                col_top = box.column(align=True)
                row = col_top.row(align=True)

                o = context.object
                if o.type == "MESH":
                    row.label("Non-Des-Curve:")
                    #row = col_top.row(align=True)
                    row.prop(o, "names")
                    row = col_top.row(align=True)
                    row.prop(o, "rscale", "Keep Scale")
                    row.operator("mesh.convert_update")
                else:
                    row.label("Non Destructiv Conversion:")
                    row = col_top.row(align=True)
                    row.label("select Mesh Object", icon="ERROR")

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Modifier  ############-------------------------------------------------------
    # Modifier  ############-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_modifier:

                split.prop(lt, "display_cpt_modifier", text="...ModTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_modifier", text="...ModTools...", icon='RIGHTARROW')

            #spread_op = split.operator("",text="", icon = "")

            if lt.display_cpt_modifier:

                box = col.column(align=True).box().column()

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator_menu_enum("object.modifier_add", "type", text="> Add Modifier <", icon="MODIFIER")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.label("Mirror Modifier / all enabled")

                row = col_top.row(align=True)
                row.operator("view3d.fullmirror", text="X-Clip")
                row.operator("view3d.fullmirrory", text="Y-Clip")
                row.operator("view3d.fullmirrorz", text="Z-Clip")

    # Subdivision Level  #######-------------------------------------------------------
    # Subdivision Level  #######-------------------------------------------------------

                #col = layout.column(align=True)
                split = col.split()  # percentage=0.15)

                if lt.display_cpt_subdiv:
                    split.prop(lt, "display_cpt_subdiv", text="Subdivision Level", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_subdiv", text="Subdivision Level", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #spread_op = split.operator("",text="", icon = "")

                if lt.display_cpt_subdiv:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)

                    # row.label("Levels")

                    row = col_top.row(align=True)
                    row.operator("view3d.modifiers_subsurf_level_0")
                    row.operator("view3d.modifiers_subsurf_level_1")
                    row.operator("view3d.modifiers_subsurf_level_2")
                    row.operator("view3d.modifiers_subsurf_level_3")
                    row.operator("view3d.modifiers_subsurf_level_4")
                    row.operator("view3d.modifiers_subsurf_level_5")
                    row.operator("view3d.modifiers_subsurf_level_6")

    # Visual  #######-------------------------------------------------------
    # Visual  #######-------------------------------------------------------

               #col = layout.column(align=True)
                split = col.split()  # percentage=0.15)

                if lt.display_cpt_modivisual:
                    split.prop(lt, "display_cpt_modivisual", text="Visualisation", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_modivisual", text="Visualisation", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #spread_op = split.operator("",text="", icon = "")

                if lt.display_cpt_modivisual:
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("object.wire_all", text="Wire All", icon='WIRE')

                    row = col_top.row(align=True)
                    row.operator("view3d.display_modifiers_viewport_on", icon='RESTRICT_VIEW_OFF')
                    row.operator("view3d.display_modifiers_viewport_off", icon='VISIBLE_IPO_OFF')

                    row = col_top.row(align=True)
                    row.operator("view3d.display_modifiers_apply", icon='FILE_TICK')
                    row.operator("view3d.display_modifiers_delete", icon='X')

                    row = col_top.row(align=True)
                    row.operator("view3d.display_modifiers_expand", icon='DISCLOSURE_TRI_DOWN_VEC')
                    row.operator("view3d.display_modifiers_collapse", icon='DISCLOSURE_TRI_RIGHT_VEC')

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Auto Mirror  #######-------------------------------------------------------
    # Auto Mirror  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_mirrorcut:
                split.prop(lt, "display_cpt_mirrorcut", text="...MirrorTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_mirrorcut", text="...MirrorTools...", icon='RIGHTARROW')

            #spread_op = split.operator("",text="", icon = "")

            if lt.display_cpt_mirrorcut:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("object.automirror", text=" >  Auto Mirror Cut  < ")

                row = col_top.row(align=True)
                row.prop(context.scene, "AutoMirror_axis", text="")
                row = col_top.row(align=True)
                row.prop(context.scene, "AutoMirror_orientation", text="")
                row = col_top.row(align=True)
                row.prop(context.scene, "AutoMirror_threshold", text="Threshold")

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.prop(context.scene, "AutoMirror_toggle_edit", text="Toggle edit")
                row = col_top.row(align=True)
                row.prop(context.scene, "AutoMirror_cut", text="Cut and mirror")
                row = col_top.row(align=True)
                if bpy.context.scene.AutoMirror_cut:
                    row.prop(context.scene, "AutoMirror_apply_mirror", text="Apply mirror")
                else:
                    row.label(icon="ERROR", text="No mesh selected")

                box = col.column(align=True).box().column()

    # ------------------------------------------------------------
    # Curve Tools   ######------------------------------------------------------------
    # Curve Tools  ######------------------------------------------------------------
    # ------------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_tab_curveloft:
                split.prop(lt, "display_tab_curveloft", text="...CurveTools...", icon='DOWNARROW_HLT')

            else:
                split.prop(lt, "display_tab_curveloft", text="...CurveTools...", icon='RIGHTARROW')

            if lt.display_tab_curveloft:

                # ------------------------------------------------------------
                # Curve Info   ######------------------------------------------------------------
                # Curve Info  ######------------------------------------------------------------
                # ------------------------------------------------------------

                split = col.split()  # percentage=0.15)
                if lt.display_tab_curveinfo:
                    split.prop(lt, "display_tab_curveinfo", text="Selections Info", icon='DISCLOSURE_TRI_DOWN_VEC')

                else:
                    split.prop(lt, "display_tab_curveinfo", text="Selections Info", icon='DISCLOSURE_TRI_RIGHT_VEC')

                if lt.display_tab_curveinfo:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("curvetools2.operatorcurveinfo", text="Curve Info")

                    row = col_top.row(align=True)
                    row.operator("curvetools2.operatorsplinesinfo", text="Splines Info")

                    row = col_top.row(align=True)
                    row.operator("curvetools2.operatorsegmentsinfo", text="Segments Info")

                    col = layout.column(align=True)
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("curvetools2.operatorcurvelength", text="Calc Length")
                    row = col_top.row(align=True)
                    row.prop(context.scene.curvetools, "CurveLength", text="")

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("curve.bevelcurve", "Curve as Bevel", icon="CURVE_BEZCIRCLE")
                row.operator("curve.tapercurve", "Curve as Taper", icon="CURVE_BEZCURVE")

                # --------------------------

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("curvetools2.operatororigintospline0start", text="Origin 2 Start", icon="PARTICLE_TIP")
                row.operator("curve.switch_direction_obm", "Direction", icon="ARROW_LEFTRIGHT")

                # --------------------------

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("curvetools2.operatorsplinessetresolution", text="Set resolution")
                row.prop(context.scene.curvetools, "SplineResolution", text="")

                # --------------------------

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.scale_y = 1.5
                row.operator("curvetools2.operatorsweepcurves", text="Sweep")
                row.operator("curvetools2.operatorloftcurves", text="Loft")

                row = col_top.row(align=True)
                row.scale_y = 1.5
                row.operator("curvetools2.operatorbirail", text="Birail")
                row.operator("curvetools2.operatorsweepandmorph", text="Morph")

                row = col_top.row(align=True)
                row.scale_y = 1.5
                row.operator("curvetools2.operatorrevolvecurves", text="Revolver")
                row.prop(context.scene.curvetools, "AngularResolution", text="AngRes")

                # --------------------------

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("curvetools2.operatorselectioninfo", text="Selection Info:")
                row = col_top.row(align=True)
                row.prop(context.scene.curvetools, "NrSelectedObjects", text="")

                # --------------------------

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("curvetools2.operatorintersectcurves", text="Intersect curves")

                row = col_top.row(align=True)
                row.prop(context.scene.curvetools, "LimitDistance", text="LimitDistance")
                #row.active = (context.scene.curvetools.IntersectCurvesAlgorithm == '3D')

                col_top = box.column(align=True)
                col_top = box.column(align=True)

                row = col_top.row(align=0)
                row.prop(context.scene.curvetools, "IntersectCurvesAlgorithm", text="Algorithm")

                row = col_top.row(align=0.1)
                row.prop(context.scene.curvetools, "IntersectCurvesMode", text="Mode")

                row = col_top.row(align=0.1)
                row.prop(context.scene.curvetools, "IntersectCurvesAffect", text="Affect")

                # --------------------------

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("curvetools2.operatorsplinesjoinneighbouring", text="Join neighbouring splines")

                row = col_top.row(align=True)
                row.prop(context.scene.curvetools, "SplineJoinDistance", text="Threshold join")

                col_top = box.column(align=True)
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.prop(context.scene.curvetools, "SplineJoinDistance", text="Threshold join")

                row = col_top.row(align=True)
                row.prop(context.scene.curvetools, "SplineJoinStartEnd", text="Only at start & end")

                row = col_top.row(align=0.5)
                row.prop(context.scene.curvetools, "SplineJoinMode", text="Join")

                # --------------------------

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("curvetools2.operatorsplinesremovezerosegment", text="Remove 0-segments")

                row = col_top.row(align=True)
                row.operator("curvetools2.operatorsplinesremoveshort", text="Remove short splines")

                row = col_top.row(align=True)
                row.prop(context.scene.curvetools, "SplineRemoveLength", text="Threshold remove")

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Array Tools  #######-------------------------------------------------------
    # Array Tools  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_array:
                split.prop(lt, "display_cpt_array", text="...ArrayTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_array", text="...ArrayTools...", icon='RIGHTARROW')

            #spread_op = split.operator("",text="", icon = "")

            if lt.display_cpt_array:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("object.simplearewo", text="Replicator")
                row.operator("object.cursor_array", text="2 Cursor")

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("object.add_2array", text="2d Grid")
                row.operator("object.add_3array", text="3d Grid")

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                mifthTools = bpy.context.scene.mifthTools

                row.operator("mft.clonetoselected", text="CloneToSelected")

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("mft.radialclone", text="Radial Clone")

                row = col_top.row(align=True)
                row.prop(mifthTools, "radialClonesAxis", text='')
                row.prop(mifthTools, "radialClonesAxisType", text='')

    # Curve  ######--------------------------------------
    # Curve  ######--------------------------------------

                #col_top = box.column(align=True)
                split = col.split()  # percentage=0.15)

                if lt.display_cpt_arraycurve:
                    split.prop(lt, "display_cpt_arraycurve", text="Curve", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_arraycurve", text="Curve", icon='DISCLOSURE_TRI_RIGHT_VEC')

                if lt.display_cpt_arraycurve:
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("object.loops12", text="", icon="CURVE_BEZCURVE")
                    row.operator("object.loops13", text="Beziér Curve",)

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("object.loops10", text="", icon="CURVE_BEZCIRCLE")
                    row.operator("object.loops11", text="Beziér Circle",)

    # Empty  ######--------------------------------------
    # Empty  ######-------------------------------------

                #col_top = box.column(align=True)
                split = col.split()  # percentage=0.15)

                if lt.display_cpt_arraycircle:
                    split.prop(lt, "display_cpt_arraycircle", text="Empty", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_arraycircle", text="Empty", icon='DISCLOSURE_TRI_RIGHT_VEC')

                    #spread_op = split.operator("",text="", icon = "")

                if lt.display_cpt_arraycircle:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("objects.circle_array_operator1", text="1/4-90°", icon="MOD_ARRAY")
                    row.operator("objects.circle_array_operator2", text="1/6-60°", icon="MOD_ARRAY")

                    row = col_top.row(align=True)
                    row.operator("objects.circle_array_operator3", text="1/8-45°", icon="MOD_ARRAY")
                    row.operator("objects.circle_array_operator4", text="1/12-30°", icon="MOD_ARRAY")

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # 1D Align Tool  ######-----------------------------------------
    # 1D Align Tool  ######-----------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_1d:
                split.prop(lt, "display_cpt_1d", text="...AlignTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_1d", text="...AlignTools...", icon='RIGHTARROW')

            if lt.display_cpt_1d:

                #col_top = box.column(align=True)

                split = col.split()

                if lt.display_cpt_align:
                    split.prop(lt, "display_cpt_align", text="Align Edges", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_align", text="Align Edges", icon='RIGHTARROW_THIN')

                box = col.column(align=True)
                if lt.display_cpt_align and context.mode == 'EDIT_MESH':
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.align_operator", text='Store Edge').type_op = 1
                    row = col_top.row(align=True)
                    align_op = row.operator("mesh.align_operator", text='Align').type_op = 0
                    row = col_top.row(align=True)
                    row.prop(lt, 'align_dist_z', text='Superpose')
                    row = col_top.row(align=True)
                    row.prop(lt, 'align_lock_z', text='lock Z')

                if lt.display_cpt_align and context.mode == 'OBJECT':
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.align_operator", text='Store Edge').type_op = 1
                    row = col_top.row(align=True)
                    align_op = row.operator("mesh.align_operator", text='Align').type_op = 2
                    row = col_top.row(align=True)
                    row.prop(context.scene, 'AxesProperty', text='Axis')
                    row = col_top.row(align=True)
                    row.prop(context.scene, 'ProjectsProperty', text='Projection')

                # 3D Match  ######-----------------------------------------
                split = col.split()
                if lt.display_cpt_3dmatch:
                    split.prop(lt, "display_cpt_3dmatch", text="3D Match", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_3dmatch", text="3D Match", icon='RIGHTARROW_THIN')

                if lt.display_cpt_3dmatch:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.align_operator", text='Store key').type_op = 3
                    row = col_top.row(align=True)
                    split = row.split(0.33, True)
                    split.scale_y = 1.5
                    split.operator("mesh.align_operator", text='Flip').type_op = 6
                    split.operator("mesh.align_operator", text='3D Match').type_op = 5

                # SideShift  ######-----------------------------------------
                split = col.split()
                if lt.display_cpt_offset:
                    split.prop(lt, "display_cpt_offset", text="SideShift", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_offset", text="SideShift", icon='RIGHTARROW_THIN')

                if lt.display_cpt_offset:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.align_operator", text='Store dist').type_op = 1
                    row = col_top.row(align=True)
                    row.operator("mesh.offset_operator", text='Active » Cursor').type_op = 3

                    row = col_top.row(align=True)
                    lockX_op = row.prop(lt, "shift_lockX", text="X", icon='FREEZE')
                    lockY_op = row.prop(lt, "shift_lockY", text="Y", icon='FREEZE')
                    lockZ_op = row.prop(lt, "shift_lockZ", text="Z", icon='FREEZE')
                    row = col_top.row(align=True)
                    row.prop(lt, "shift_local", text="Local")

                    row = col_top.row(align=True)
                    split = col_top.split(percentage=0.76)
                    split.prop(lt, 'step_len', text='dist')
                    getlenght_op = split.operator("mesh.offset_operator", text="Get dist").type_op = 1
                    row = col_top.row(align=True)
                    split = col_top.split(percentage=0.5)
                    left_op = split.operator("mesh.offset_operator", text="", icon='TRIA_LEFT')
                    left_op.type_op = 0
                    left_op.sign_op = -1
                    right_op = split.operator("mesh.offset_operator", text="", icon='TRIA_RIGHT')
                    right_op.type_op = 0
                    right_op.sign_op = 1
                    row = col_top.row(align=True)
                    if context.mode == 'EDIT_MESH':
                        row.prop(lt, "shift_copy", text="Copy")
                    else:
                        row.prop(lt, "instance", text='Instance')
                        row = col_top.row(align=True)
                        row.prop(lt, "shift_copy", text="Copy")

                # Polycross  ######-----------------------------------------
                split = col.split()
                if lt.disp_cpt:
                    split.prop(lt, "disp_cpt", text="Polycross", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "disp_cpt", text="Polycross", icon='RIGHTARROW_THIN')

                if lt.disp_cpt:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    split = row.split()
                    if lt.disp_cpt_project:
                        split.prop(lt, "disp_cpt_project", text="Project active", icon='DISCLOSURE_TRI_DOWN_VEC')
                    else:
                        split.prop(lt, "disp_cpt_project", text="Project active", icon='RIGHTARROW_THIN')

                    if lt.disp_cpt_project:
                        row = col_top.row(align=True)
                        split = row.split(0.5, True)
                        split.operator("mesh.polycross", text='Section').type_op = 0  # section and clear filter
                        split.operator("mesh.polycross", text='Cut').type_op = 1  # cross
                        row = col_top.row(align=True)
                        row.prop(lt, "fill_cuts", text="fill cut")
                        row = col_top.row(align=True)
                        row.prop(lt, "outer_clear", text="remove front")
                        row = col_top.row(align=True)
                        row.prop(lt, "inner_clear", text="remove bottom")

                    ######  Selection Filter  ######
                    row = col_top.row(align=True)
                    split = row.split()
                    if lt.disp_cpt_filter:
                        split.prop(lt, "disp_cpt_filter", text="Selection Filter", icon='DISCLOSURE_TRI_DOWN_VEC')
                    else:
                        split.prop(lt, "disp_cpt_filter", text="Selection Filter", icon='RIGHTARROW_THIN')

                    if lt.disp_cpt_filter:
                        row = col_top.row(align=True)
                        #row.active = lt.filter_edges or lt.filter_verts_bottom or lt.filter_verts_top
                        row.operator("mesh.polycross", text='to SELECT').type_op = 2  # only filter
                        row = col_top.row(align=True)
                        row.prop(lt, "filter_edges", text="Filter Edges")
                        row = col_top.row(align=True)
                        row.prop(lt, "filter_verts_top", text="Filter Top")
                        row = col_top.row(align=True)
                        row.prop(lt, "filter_verts_bottom", text="Filter Bottom")

                # AutoExtrude  ######-----------------------------------------
                split = col.split()
                if lt.disp_cpt_matExtrude:
                    split.prop(lt, "disp_cpt_matExtrude", text="AutoExtrude", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "disp_cpt_matExtrude", text="AutoExtrude", icon='RIGHTARROW_THIN')

                if lt.disp_cpt_matExtrude:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.get_mat4extrude", text='Get Mats')
                    row = col_top.row(align=True)
                    row.operator("mesh.mat_extrude", text='Template Extrude')

                # Spread Loop  ######-----------------------------------------
                split = col.split(percentage=0.15, align=True)
                if lt.display_cpt_spread:
                    split.prop(lt, "display_cpt_spread", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_spread", text="", icon='RIGHTARROW_THIN')

                spread_op = split.operator("mesh.spread_operator", text='Spread Loop')

                if lt.display_cpt_spread:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.prop(lt, 'spread_x', text='Spread X')
                    row = col_top.row(align=True)
                    row.prop(lt, 'spread_y', text='Spread Y')
                    row = col_top.row(align=True)
                    row.prop(lt, 'spread_z', text='Spread Z')
                    row = col_top.row(align=True)
                    row.prop(lt, 'relation', text='Relation')
                    box = box.box().column()
                    row = box.row(align=True)
                    row.prop(lt, 'shape_spline', text='Shape spline')
                    row = box.row(align=True)
                    row.active = lt.shape_spline
                    row.prop(lt, 'spline_Bspline2', text='Smooth transition')
                    row = box.row(align=True)

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Copy Tools  #######-------------------------------------------------------
    # Copy Tools  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_copy:
                split.prop(lt, "display_cpt_copy", text="...CopyShop...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_copy", text="...CopyShop...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_cpt_copy:
                operator_context_default = layout.operator_context
                wm = bpy.context.window_manager
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                layout.operator_context = 'INVOKE_REGION_WIN'

                row = col_top.row(align=True)
                row.label("Make Links (CTRL+L)", icon="LINKED")

                row = col_top.row(align=True)
                row.operator_enum("object.make_links_data", "type")  # inline

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("object.join_uvs")  # stupid place to add this!

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                if len(bpy.data.scenes) > 10:
                    row = col_top.row(align=True)
                    layout.operator_context = 'INVOKE_REGION_WIN'
                    row.operator("object.make_links_scene", text="Objects to Scene", icon='SCENE_DATA')
                else:
                    row = col_top.row(align=True)
                    layout.operator_context = 'EXEC_REGION_WIN'
                    row.operator_menu_enum("object.make_links_scene", "scene", text="Objects to Scene", icon='SCENE_DATA')

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.menu("VIEW3D_MT_copypopup", text="Copy Option", icon="DISCLOSURE_TRI_RIGHT")

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Relations  #######-------------------------------------------------------
    # Relations  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_relations:
                split.prop(lt, "display_cpt_relations", text="...Relations...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_relations", text="...Relations...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_cpt_relations:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.menu("VIEW3D_MT_make_links", text="M.Links", icon="LINKED")
                row.menu("VIEW3D_MT_make_single_user", text="Single User")

                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("object.visual_transform_apply", icon="NDOF_DOM")

                row = col_top.row(align=True)
                row.operator("object.duplicates_make_real", icon="MOD_PARTICLES")
                row.operator("help_operator", text="", icon="INFO")

                row = col_top.row(align=True)
                row.operator("object.set_instance", text="Set as Instance", icon="LINK_AREA")

    # Group  ######-------------------------------------
    # Group  ######-------------------------------------

                split = col.split(percentage=0.15, align=True)

                if lt.display_cpt_relagroup:
                    split.prop(lt, "display_cpt_relagroup", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_relagroup", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

                spread_op = split.operator("group.create", text="Group", icon="STICKY_UVS_LOC")

                if lt.display_cpt_relagroup:
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("group.create", text="Group to Selected")
                    row = col_top.row(align=True)
                    row.operator("group.objects_remove", text="Remove Group from Selected")

                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("group.objects_add_active", text="Group to Active")
                    row = col_top.row(align=True)
                    row.operator("group.objects_remove_active", text="Remove Group from Active")

    # Parent  ######-------------------------------------
    # Parent  ######-------------------------------------

                split = col.split(percentage=0.15, align=True)

                if lt.display_cpt_relaparent:
                    split.prop(lt, "display_cpt_relaparent", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_relaparent", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

                spread_op = split.operator("object.parent_set", text="Parent", icon="CONSTRAINT")

                if lt.display_cpt_relaparent:
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("object.parent_clear").type = "CLEAR"
                    row = col_top.row(align=True)
                    row.operator("object.parent_clear", text="Clear Inverse").type = "CLEAR_INVERSE"
                    row = col_top.row(align=True)
                    row.operator("object.parent_clear", text="Clear Keep Transform").type = "CLEAR_KEEP_TRANSFORM"

    # Constraint  ######-------------------------------------
    # Constraint  ######-------------------------------------

                split = col.split(percentage=0.15, align=True)

                if lt.display_cpt_relaconstraint:
                    split.prop(lt, "display_cpt_relaconstraint", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_relaconstraint", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

                spread_op = split.operator_menu_enum("object.constraint_add", "type", text="  Constraint", icon="CONSTRAINT_DATA")

                if lt.display_cpt_relaconstraint:
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("lookat.it", text="Look @ Obj")
                    row.operator("lookat.cursor", text="Look @ Cursor")

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.label(text="to Selected:", icon="LAYER_ACTIVE")

                    row = col_top.row(align=True)
                    row.operator("track.to", text="Track To")
                    row.operator("damped.track", text="Damped Track")
                    row.operator("lock.track", text="Lock Track")

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.label(text="to CursorPos+Empty:", icon="LAYER_ACTIVE")

                    row = col_top.row(align=True)
                    row.operator("track.toempty", text="Track To")
                    row.operator("damped.trackempty", text="Damped Track")
                    row.operator("lock.trackempty", text="Lock Track")

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Material Tools  #######-------------------------------------------------------
    # Material Tools  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_material:
                split.prop(lt, "display_cpt_material", text="...MatTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_material", text="...MatTools...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_cpt_material:

                wm = bpy.context.window_manager
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                layout.operator_context = 'INVOKE_REGION_WIN'

                row = col_top.row(align=True)
                row.operator("view3d.assign_material", text="New", icon='ZOOMIN')
                row.operator("object.material_slot_remove", text="Delete", icon="ZOOMOUT")

                row = col_top.row(align=True)
                row.menu("VIEW3D_MT_assign_material", text="Assign Material", icon='ZOOMIN')
                row = col_top.row(align=True)
                row.menu("VIEW3D_MT_select_material", text="Select by Material", icon='RESTRICT_SELECT_OFF')
                row = col_top.row(align=True)
                row.operator("meta.newmaterial", text="ObjColor", icon='ZOOMIN')
                row.prop(obj, "color", text="")

    # Material Option  ######-------------------------------------------------
    # Material Option  ######-------------------------------------------------

                split = col.split()  # percentage=0.15)

                if lt.display_cpt_matoption:
                    split.prop(lt, "display_cpt_matoption", text="Mat Options", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_matoption", text="Mat Options", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("",text="", icon = "")

                if lt.display_cpt_matoption:
                    wm = bpy.context.window_manager
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("view3d.material_to_texface", text="Material to Texface", icon='MATERIAL_DATA')

                    row = col_top.row(align=True)
                    row.operator("view3d.texface_to_material", text="Texface to Material", icon='MATERIAL_DATA')

                    row = col_top.row(align=True)
                    row.operator("view3d.fake_user_set", text='Set Fake User', icon='UNPINNED')

                    row = col_top.row(align=True)
                    row.operator("object.materials_to_data", text="Data", icon="MATERIAL_DATA")
                    row.operator("object.materials_to_object", text="Object", icon="MATERIAL_DATA")

    # Clean Material  ######-------------------------------------------------
    # Clean Material  ######-------------------------------------------------

                split = col.split()  # percentage=0.15)

                if lt.display_cpt_matclean:
                    split.prop(lt, "display_cpt_matclean", text="Remove Mat", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_matclean", text="Remove Mat", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("",text="", icon = "")

                if lt.display_cpt_matclean:

                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("object.clean_images")

                    row = col_top.row(align=True)
                    row.operator("object.clean_materials")

                    #row = col_top.row(align=True)
                    #row.operator("view3d.clean_material_slots", text="Clean Material Slots", icon='CANCEL')

                    row = col_top.row(align=True)
                    row.operator("view3d.material_remove", text="Remove until 1 Slots", icon='CANCEL')

                    row = col_top.row(align=True)
                    row.operator("material.remove", text="Remove all Slot Mat", icon='CANCEL')

    # Node Materials  ######-------------------------------------------------
    # Node Materials  ######-------------------------------------------------

                split = col.split()  # percentage=0.15)

                if lt.display_cpt_node:
                    split.prop(lt, "display_cpt_node", text="Node Presets", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_node", text="Node Presets", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #spread_op = split.operator("",text="", icon = "")

                if lt.display_cpt_node:
                    wm = bpy.context.window_manager
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("materials.rgbcmyw", text="RGB / CMYK", icon='ZOOMIN')

                    row = col_top.row(align=True)
                    row.operator("node.idgenerator", text="Add ID Color Node", icon='ZOOMIN')

                    row = col_top.row(align=True)
                    row.operator("mat.cellook", text="Cellook Material", icon='ZOOMIN')

    # Random Face Materials  ######-------------------------------------------------
    # Random Face Materials  ######-------------------------------------------------

                split = col.split()  # percentage=0.15)

                if lt.display_cpt_matrandom:
                    split.prop(lt, "display_cpt_matrandom", text="Random Face", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_matrandom", text="Random Face", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #spread_op = split.operator("",text="", icon = "")

                if lt.display_cpt_matrandom:
                    wm = bpy.context.window_manager
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)

                    row = col_top.row(align=True)

                    props = context.scene.face_assigner  # Create reference material assigner property group

                    row = col_top.row(align=True)
                    row.label(text="skip to apply")

                    row = col_top.row(align=True)
                    row.prop(props, "rand_seed")  # Create randomization seed property on column

                    row = col_top.row(align=True)
                    row.label(text="material prefix:")

                    row = col_top.row(align=True)
                    row.prop(props, "mat_prefix", text="")  # Material prefix property too

                    row = col_top.row(align=True)
                    row.label(text="assignment method:")

                    row = col_top.row(align=True)
                    row.prop(props, "assign_method", text="")  # Material assignment method prop

    # Setup Wire Render  ######-------------------------------------------------
    # Setup Wire Render  ######-------------------------------------------------

                split = col.split()  # percentage=0.15)

                if lt.display_cpt_matwireset:
                    split.prop(lt, "display_cpt_matwireset", text="Mat Wire Render", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_matwireset", text="Mat Wire Render", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("",text="", icon = "")

                if lt.display_cpt_matwireset:
                    wm = bpy.context.window_manager
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("scene.wire_render", text="Apply Setup")

                    row = col_top.row(align=True)
                    row.prop(wm, 'col_clay')
                    row.prop(wm, 'col_wire')

                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.prop(wm, 'selected_meshes')

                    row = col_top.row(align=True)
                    row.prop(wm, 'shadeless_mat')

                    row = col_top.row(align=True)
                    row.prop(wm, 'wire_view')

                    row = col_top.row(align=True)
                    row.prop(wm, 'wire_object')

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # UV Mapping  #######-------------------------------------------------------
    # UV Mapping  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_unwrap:
                split.prop(lt, "display_cpt_unwrap", text="...UvTools ...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_unwrap", text="...UvTools....", icon='RIGHTARROW')

           #spread_op = split.operator("",text="", icon = "")

            if lt.display_cpt_unwrap:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("transform.translate", text="Move Texture Space").texture_space = True

                row = col_top.row(align=True)
                row.operator("uv.uv_equalize", text="UV Equalize")

    # UV Utility  ######-------------------------------------------------
    # UV Utility  ######-------------------------------------------------

                split = col.split()  # percentage=0.15)

                if lt.display_cpt_uvut:
                    split.prop(lt, "display_cpt_uvut", text="UV Utility", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_uvut", text="UV Utility", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("",text="", icon = "")

                if lt.display_cpt_uvut:
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("uvutil.change_index", text="Drop Active UV Back")

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.prop(scene, "UVTexRenderActive")

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("uvutil.select_index", text="Select UVTexCoord")
                    row = col_top.row(align=True)
                    row.prop(scene, "UVTexIndex", text="UVTexCoord")

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("uvutil.select_name", text="Select UV Name")
                    row = col_top.row(align=True)
                    row.prop(scene, "UVTexGetName", text="")

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("uvutil.remove_active", text="Remove Active UV")

    # SureUVW  ######-------------------------------------------------
    # SureUVW  ######-------------------------------------------------

                split = col.split()  # percentage=0.15)

                if lt.display_cpt_uvsure:
                    split.prop(lt, "display_cpt_uvsure", text="SureUVW", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_uvsure", text="SureUVW", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("",text="", icon = "")

                if lt.display_cpt_uvsure:
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)

                    row.label("Press this button first:")
                    row = col_top.row(align=True)
                    row.operator("object.sureuvw_operator", text="Show active texture on object").action = 'showtex'
                    row = col_top.row(align=True)
                    row.label("UVW Mapping:")
                    row = col_top.row(align=True)
                    row.operator("object.sureuvw_operator", text="UVW Box Map").action = 'box'
                    row = col_top.row(align=True)
                    row.operator("object.sureuvw_operator", text="Best Planar Map").action = 'bestplanar'
                    row = col_top.row(align=True)
                    row.label("1. Make Material With Raster Texture!")
                    row = col_top.row(align=True)
                    row.label("2. Set Texture Mapping Coords: UV!")
                    row = col_top.row(align=True)
                    row.label("3. Use Addon buttons")

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Delete & Clear  #######-------------------------------------------------------
    # Delete & Clear  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_delete:
                split.prop(lt, "display_cpt_delete", text="...Delete...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_delete", text="...Delete...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_cpt_delete:

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("object.delete")
                row = col_top.row(align=True)
                row.operator("object.delete_from_all_scenes", text="Delete From All Scenes")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                scn = context.scene
                row.operator("ba.delete_data_obs", "Clear Orphan")
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.prop(scn, "mod_list")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.menu("VIEW3D_MT_object_showhide", "Clear Hide")

                row = col_top.row(align=True)
                row.menu("VIEW3D_MT_object_clear", text="Clear Location")
                row = col_top.row(align=True)
                row.menu("clearparent", text="Clear Parenting")
                row = col_top.row(align=True)
                row.menu("cleartrack", text="Clear Tracking")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("object.constraints_clear", text="Clear Constraint")
                row = col_top.row(align=True)
                row.operator("anim.keyframe_clear_v3d", text="Clear Keyframe")
                row = col_top.row(align=True)
                row.operator("object.game_property_clear")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("meshlint.select", "Meshlint > Object Data")

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Grease Pencil  #######-------------------------------------------------------
    # Grease Pencil  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_pencil:
                split.prop(lt, "display_cpt_pencil", text="...PencilTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_pencil", text="...PencilTools...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_cpt_pencil:
                #box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.prop(context.tool_settings, "use_grease_pencil_sessions", text="Keep Session")
                row = col_top.row(align=True)
                row.operator("gpencil.draw", text="Hand", icon="GREASEPENCIL").mode = 'DRAW'
                row = col_top.row(align=True)
                row.operator("gpencil.draw", text="Straight", icon="ZOOMOUT").mode = 'DRAW_STRAIGHT'
                row = col_top.row(align=True)
                row.operator("gpencil.draw", text="Polyline", icon="MESH_DATA").mode = 'DRAW_POLY'
                row = col_top.row(align=True)
                row.operator("gpencil.draw", text="Eraser", icon="PANEL_CLOSE").mode = 'ERASER'


#######  EDITMODE  #######  EDITMODE #######  EDITMODE  #######  EDITMODE  #######  EDITMODE  #######  EDITMODE  #######  EDITMODE #######
#######  EDITMODE  #######  EDITMODE #######  EDITMODE  #######  EDITMODE  #######  EDITMODE  #######  EDITMODE  #######  EDITMODE #######

        ### modespace a ###
        obj = context
        if obj and obj.mode == 'EDIT_MESH':
            mesh = context.active_object.data
            obj = context.object
            scene = context.scene
            ### modespace b ###
            box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Add Geometry   #######-------------------------------------------------------
    # Add Geometry   #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_geom:
                split.prop(lt, "display_cpt_geom", text="...Geometry...", icon='DOWNARROW_HLT')

            else:
                split.prop(lt, "display_cpt_geom", text="...Geometry...", icon='RIGHTARROW')

            #spread_op = row.menu("INFO_MT_add",text="", icon="OBJECT_DATAMODE")

            if lt.display_cpt_geom:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("mesh.singlevertex", text="Vertex", icon="LAYER_ACTIVE")
                row.operator("mesh.singleline", text="Line", icon="LAYER_ACTIVE")
                row = col_top.row(align=True)
                row.operator("mesh.singleplane", text="Plane", icon="LAYER_ACTIVE")
                row.operator("mesh.primitive_circle_add", text="Circle", icon="LAYER_ACTIVE")

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Modifier  #######-------------------------------------------------------
    # Modifier  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_modifier:

                split.prop(lt, "display_cpt_modifier", text="...ModTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_modifier", text="...ModTools...", icon='RIGHTARROW')

            #spread_op = split.operator("view3d.select_border", text="Placer", icon="SNAP_SURFACE")

            if lt.display_cpt_modifier:

                box = col.column(align=True).box().column()

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator_menu_enum("object.modifier_add", "type", text=">> Add Modifier <<", icon="MODIFIER")

    # Subdivision Level  #######-------------------------------------------------------
    # Subdivision Level  #######-------------------------------------------------------

                #col = layout.column(align=True)
                split = col.split()  # percentage=0.15)

                if lt.display_cpt_subdiv:
                    split.prop(lt, "display_cpt_subdiv", text="Subdivision Level", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_subdiv", text="Subdivision Level", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #spread_op = split.operator("object.modifier_add", text="Subdivision Level", icon = 'MOD_SUBSURF').type="SUBSURF"

                if lt.display_cpt_subdiv:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)

                    # row.label("Levels")

                    row = col_top.row(align=True)
                    row.operator("view3d.modifiers_subsurf_level_0")
                    row.operator("view3d.modifiers_subsurf_level_1")
                    row.operator("view3d.modifiers_subsurf_level_2")
                    row.operator("view3d.modifiers_subsurf_level_3")
                    row.operator("view3d.modifiers_subsurf_level_4")
                    row.operator("view3d.modifiers_subsurf_level_5")
                    row.operator("view3d.modifiers_subsurf_level_6")

    # Visual  #######-------------------------------------------------------
    # Visual  #######-------------------------------------------------------

                #col = layout.column(align=True)
                split = col.split()  # percentage=0.15)

                if lt.display_cpt_modivisual:
                    split.prop(lt, "display_cpt_modivisual", text="Visual", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_modivisual", text="Visual", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #spread_op = split.operator("object.shade_smooth", text="Visual", icon="MESH_CUBE")

                if lt.display_cpt_modivisual:
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("object.wire_all", text="Wire All", icon='WIRE')

                    row = col_top.row(align=True)
                    row.operator("view3d.display_modifiers_viewport_on", icon='RESTRICT_VIEW_OFF')
                    row.operator("view3d.display_modifiers_edit_on", icon='EDITMODE_HLT')
                    row.operator("view3d.display_modifiers_cage_on", icon='OUTLINER_OB_MESH')

                    row = col_top.row(align=True)
                    row.operator("view3d.display_modifiers_viewport_off", icon='VISIBLE_IPO_OFF')
                    row.operator("view3d.display_modifiers_edit_off", icon='SNAP_VERTEX')
                    row.operator("view3d.display_modifiers_cage_off", icon='OUTLINER_DATA_MESH')

                    row = col_top.row(align=True)
                    row.operator("view3d.display_modifiers_apply_edm", icon='FILE_TICK')
                    row.operator("view3d.display_modifiers_delete", icon='X')

                    row = col_top.row(align=True)
                    row.operator("view3d.display_modifiers_expand", icon='DISCLOSURE_TRI_DOWN_VEC')
                    row.operator("view3d.display_modifiers_collapse", icon='DISCLOSURE_TRI_RIGHT_VEC')

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # CadTools  #######-------------------------------------------------------
    # CadTools  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_cadtools:
                split.prop(lt, "display_cpt_cadtools", text="...CAD...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_cadtools", text="...CAD...", icon='RIGHTARROW')

            # split.operator()

            if lt.display_cpt_cadtools:
                box = col.column(align=True).box().column()

                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("bpt.boolean_2d_union", text="Union 2d Faces", icon="LOCKVIEW_ON")
                row = col_top.row(align=True)
                row.operator("fan.move_faces_along_normals_operator", "Move Along Normals", icon="SNAP_NORMAL")

    # ExtrudeSpecial  ######-----------------------------------------
    # ExtrudeSpecial  ######-----------------------------------------

                split = col.split()  # percentage=0.15, align=True)

                if lt.display_cpt_extrude:
                    split.prop(lt, "display_cpt_extrude", text="Extrusion", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_extrude", text="Extrusion", icon='DISCLOSURE_TRI_RIGHT_VEC')

                # split.operator()

                if lt.display_cpt_extrude:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.menu("VIEW3D_MT_edit_mesh_extrude", text="Extrude", icon="FACESEL")

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator('object.mextrude', text="Multi Extrude")

                    row = col_top.row(align=True)
                    row.operator("faceinfillet.op0_id", text="Face Inset Fillet")

                    row = col_top.row(align=True)
                    row.operator("f.op0_id", text="Edge Fillet")

                    row = col_top.row(align=True)
                    row.operator("mesh.extrude_along_curve", text="Extrude Along Curve")

                    row = col_top.row(align=True)
                    row.operator("mechappo.select", text="Mechappo_Random Select")
                    row = col_top.row(align=True)
                    row.operator("mechappo.create", text="Mechappo_Extrude")

    # Rotate Face  ######-----------------------------------------
    # Rotate Face  ######-----------------------------------------

                split = col.split()  # percentage=0.15, align=True)

                if lt.display_cpt_rotface:
                    split.prop(lt, "display_cpt_rotface", text="Rotate Face", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_rotface", text="Rotate Face", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("mesh.rot_con", "Rotate Face")

                if lt.display_cpt_rotface:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("mesh.rot_con", "Rotate Face")

                    row = col_top.row(align=True)
                    row.operator("mesh.face_rotate_xz45", "Xz 45°")
                    row.operator("mesh.face_rotate_yz45", "Yz 45°")
                    row.operator("mesh.face_rotate_zx45", "Zx 45°")

                    row = col_top.row(align=True)
                    row.operator("mesh.face_rotate_xy45", "Xy 45°")
                    row.operator("mesh.face_rotate_yx45", "Yx 45°")
                    row.operator("mesh.face_rotate_zy45", "Zy 45°")

                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("mesh.face_rotate_mxz45", "Xz -45°")
                    row.operator("mesh.face_rotate_myz45", "Yz -45°")
                    row.operator("mesh.face_rotate_mzx45", "Zx -45°")

                    row = col_top.row(align=True)
                    row.operator("mesh.face_rotate_mxy45", "Xy -45°")
                    row.operator("mesh.face_rotate_myx45", "Yx -45°")
                    row.operator("mesh.face_rotate_mzy45", "Zy -45°")

    # Intersection  ######-----------------------------------------
    # Intersection  ######-----------------------------------------

                #col_top = box.column(align=True)
                split = col.split()  # percentage=0.15, align=True)

                if lt.display_cpt_intersectedge:
                    split.prop(lt, "display_cpt_intersectedge", text="Intersection", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_intersectedge", text="Intersection", icon='DISCLOSURE_TRI_RIGHT_VEC')

                # split.operator()

                if lt.display_cpt_intersectedge:
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("mesh.intersect", "Intersect Self/Select").mode = "SELECT"
                    row = col_top.row(align=True)
                    row.operator("mesh.intersect", "Intersect Select/UnSelect").mode = "SELECT_UNSELECT"

                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("bpt.smart_vtx", text="Auto View-XVT")

                    row = col_top.row(align=True)
                    row.operator('mesh.intersections', text="T").mode = 0
                    row.operator('mesh.intersections', text="X").mode = 1
                    row.operator('mesh.intersections', text="V").mode = -1

    # Offset Edges Setup  ######-----------------------------------------
    # Offset Edges Setup  ######-----------------------------------------

                #col_top = box.column(align=True)

                split = col.split()  # percentage=0.15, align=True)

                if lt.display_cpt_cadedge:
                    split.prop(lt, "display_cpt_cadedge", text="Offset Edges", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_cadedge", text="Offset Edges", icon='DISCLOSURE_TRI_RIGHT_VEC')

                # split.operator("")

                if lt.display_cpt_cadedge:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("mesh.offset_edges", text="Offset Edges")

                    # inside
                    row = col_top.row(align=True)
                    row.label("Inside Extrude")

                    row = col_top.row(align=True)
                    row.operator("edge.offsetseven", text="1")
                    row.operator("edge.offseteight", text="2")

                    row = col_top.row(align=True)
                    row.operator("edge.offsetnine", text="4")
                    row.operator("edge.offsetten", text="6")

                    row = col_top.row(align=True)
                    row.operator("edge.offseteleven", text="8")
                    row.operator("edge.offsettwelve", text="10")

                    # outside
                    row = col_top.row(align=True)
                    row.label("Outside Extrude")

                    row = col_top.row(align=True)
                    row.operator("edge.offsetone", text="1")
                    row.operator("edge.offsettwo", text="2")

                    row = col_top.row(align=True)
                    row.operator("edge.offsetthree", text="4")
                    row.operator("edge.offsetfour", text="6")

                    row = col_top.row(align=True)
                    row.operator("edge.offsetfive", text="8")
                    row.operator("edge.offsetsix", text="10")

    # -------------------------------------------------------
    # Edge Tools  #######-------------------------------------------------------
    # Edge Tools  #######-------------------------------------------------------
    # -------------------------------------------------------

                #col_top = box.column(align=True)

                split = col.split()  # percentage=0.15, align=True)

                if lt.display_cpt_tooledge:
                    split.prop(lt, "display_cpt_tooledge", text="Edge Extend Tools", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_tooledge", text="Edge Extend Tools", icon='DISCLOSURE_TRI_RIGHT_VEC')

                # split.operator("")

                if lt.display_cpt_tooledge:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator('mesh.vertex_chamfer')

                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("object.mesh_edge_lengthchange", "Edge Length")
                    row = col_top.row(align=True)
                    row.operator('mesh.edge_roundifier')
                    row = col_top.row(align=True)
                    row.operator("mesh.edgetune", text="Edgetune Slider")

                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.edgetools_extend")
                    row = col_top.row(align=True)
                    row.operator("mesh.edgetools_spline")
                    row = col_top.row(align=True)
                    row.operator("mesh.edgetools_ortho")
                    row = col_top.row(align=True)
                    row.operator("mesh.edgetools_shaft")
                    row = col_top.row(align=True)
                    row.operator("mesh.edgetools_slice")
                    row = col_top.row(align=True)
                    row.operator("mesh.edgetools_project")
                    row = col_top.row(align=True)
                    row.operator("mesh.edgetools_project_end")
                    row = col_top.row(align=True)
                    if bpy.app.debug:
                        # Not ready for prime-time yet:
                        row.operator("mesh.edgetools_fillet")
                        row = col_top.row(align=True)
                        # For internal testing ONLY:
                        row.operator("mesh.edgetools_ilf")

    # -------------------------------------------------------
    # Align Direction  ######-----------------------------------------
    # Align Direction  ######-----------------------------------------
    # -------------------------------------------------------

                split = col.split()  # percentage=0.15, align=True)

                if lt.display_cpt_alignbox:
                    split.prop(lt, "display_cpt_alignbox", text="Align to BoundBox", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_alignbox", text="Align to BoundBox", icon='DISCLOSURE_TRI_RIGHT_VEC')

                # split.operator()

                if lt.display_cpt_alignbox:
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("alignx.left", text="X Left", icon='TRIA_LEFT')
                    row.operator("alignx.right", text="X Right", icon='TRIA_RIGHT')
                    row = col_top.row(align=True)
                    row.operator("aligny.front", text="Y Front", icon='PLUS')
                    row.operator("aligny.back", text="Y Back", icon='DISCLOSURE_TRI_DOWN')
                    row = col_top.row(align=True)
                    row.operator("alignz.top", text="Z Top", icon='TRIA_UP')
                    row.operator("alignz.bottom", text="Z Bottom", icon='TRIA_DOWN')

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Shrink Retopo  #######-------------------------------------------------------
    # Shrink retopo  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_shrinkretop:
                split.prop(lt, "display_cpt_shrinkretop", text="...ShrinkKit...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_shrinkretop", text="...ShrinkKit...", icon='RIGHTARROW')

            #spread_op = split.operator("object.modifier_add", text="Subdivision Level", icon = 'MOD_SUBSURF').type="SUBSURF"

            if lt.display_cpt_shrinkretop:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("view3d.fullshrink", icon='MOD_SHRINKWRAP', text="Shrink Vertex Group")

                row = col_top.row(align=True)
                row.operator("object.vertex_group_select", text="Select", icon="RESTRICT_SELECT_OFF")
                row.operator("object.vertex_group_assign", text="Assign", icon="ZOOMIN")

                row = col_top.row(align=True)

                row.operator("object.vertex_group_deselect", text="Deselect", icon="RESTRICT_SELECT_ON")
                row.operator("object.vertex_group_remove_from", text="Remove", icon="ZOOMOUT")

                row = col_top.row(align=True)
                row.operator("object.vertex_group_add", icon='STICKY_UVS_LOC', text="Add Vertex Group")
                row = col_top.row(align=True)
                row.operator("object.vertex_group_remove", icon='STICKY_UVS_LOC', text="Delete Vertex Group").all = False

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("view3d.display_cpt_modifiers_apply_edm", icon='FILE_TICK')

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Auto Mirror #######-------------------------------------------------------
    # Auto Mirror #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_mirrorcut:
                split.prop(lt, "display_cpt_mirrorcut", text="...AutoMirror...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_mirrorcut", text="...AutoMirror...", icon='RIGHTARROW')

            #spread_op = split.operator("object.modifier_add", text="Mirrorcut", icon="MOD_MIRROR").type="MIRROR"

            if lt.display_cpt_mirrorcut:
                box = col.column(align=True).box().column()

                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("view3d.fullmirror", text="MX", icon="ARROW_LEFTRIGHT")
                row.operator("view3d.fullmirrory", text="MY", icon="ARROW_LEFTRIGHT")
                row.operator("view3d.fullmirrorz", text="MZ", icon="ARROW_LEFTRIGHT")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("object.automirror", text=" >  Auto Mirror Cut  < ")

                row = col_top.row(align=True)
                row.prop(context.scene, "AutoMirror_axis", text="")
                row = col_top.row(align=True)
                row.prop(context.scene, "AutoMirror_orientation", text="")
                row = col_top.row(align=True)
                row.prop(context.scene, "AutoMirror_threshold", text="Threshold")

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.prop(context.scene, "AutoMirror_toggle_edit", text="Toggle edit")
                row = col_top.row(align=True)
                row.prop(context.scene, "AutoMirror_cut", text="Cut and mirror")
                row = col_top.row(align=True)
                if bpy.context.scene.AutoMirror_cut:
                    row.prop(context.scene, "AutoMirror_apply_mirror", text="Apply mirror")
                else:
                    row.label(icon="ERROR", text="No mesh selected")

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # 1D Align Tool  ######-----------------------------------------
    # 1D Align Tool  ######-----------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_1d:
                split.prop(lt, "display_cpt_1d", text="...AlignTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_1d", text="...AlignTools...", icon='RIGHTARROW')

            if lt.display_cpt_1d:

                #col_top = box.column(align=True)

                split = col.split()

                if lt.display_cpt_align:
                    split.prop(lt, "display_cpt_align", text="Align Edges", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_align", text="Align Edges", icon='RIGHTARROW_THIN')

                box = col.column(align=True)
                if lt.display_cpt_align and context.mode == 'EDIT_MESH':
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.align_operator", text='Store Edge').type_op = 1
                    row = col_top.row(align=True)
                    align_op = row.operator("mesh.align_operator", text='Align').type_op = 0
                    row = col_top.row(align=True)
                    row.prop(lt, 'align_dist_z', text='Superpose')
                    row = col_top.row(align=True)
                    row.prop(lt, 'align_lock_z', text='lock Z')

                if lt.display_cpt_align and context.mode == 'OBJECT':
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.align_operator", text='Store Edge').type_op = 1
                    row = col_top.row(align=True)
                    align_op = row.operator("mesh.align_operator", text='Align').type_op = 2
                    row = col_top.row(align=True)
                    row.prop(context.scene, 'AxesProperty', text='Axis')
                    row = col_top.row(align=True)
                    row.prop(context.scene, 'ProjectsProperty', text='Projection')

                # 3D Match  ######-----------------------------------------
                split = col.split()
                if lt.display_cpt_3dmatch:
                    split.prop(lt, "display_cpt_3dmatch", text="3D Match", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_3dmatch", text="3D Match", icon='RIGHTARROW_THIN')

                if lt.display_cpt_3dmatch:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.align_operator", text='Store key').type_op = 3
                    row = col_top.row(align=True)
                    split = row.split(0.33, True)
                    split.scale_y = 1.5
                    split.operator("mesh.align_operator", text='Flip').type_op = 6
                    split.operator("mesh.align_operator", text='3D Match').type_op = 5

                # SideShift  ######-----------------------------------------
                split = col.split()
                if lt.display_cpt_offset:
                    split.prop(lt, "display_cpt_offset", text="SideShift", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_offset", text="SideShift", icon='RIGHTARROW_THIN')

                if lt.display_cpt_offset:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.align_operator", text='Store dist').type_op = 1
                    row = col_top.row(align=True)
                    row.operator("mesh.offset_operator", text='Active » Cursor').type_op = 3

                    row = col_top.row(align=True)
                    lockX_op = row.prop(lt, "shift_lockX", text="X", icon='FREEZE')
                    lockY_op = row.prop(lt, "shift_lockY", text="Y", icon='FREEZE')
                    lockZ_op = row.prop(lt, "shift_lockZ", text="Z", icon='FREEZE')
                    row = col_top.row(align=True)
                    row.prop(lt, "shift_local", text="Local")

                    row = col_top.row(align=True)
                    split = col_top.split(percentage=0.76)
                    split.prop(lt, 'step_len', text='dist')
                    getlenght_op = split.operator("mesh.offset_operator", text="Get dist").type_op = 1
                    row = col_top.row(align=True)
                    split = col_top.split(percentage=0.5)
                    left_op = split.operator("mesh.offset_operator", text="", icon='TRIA_LEFT')
                    left_op.type_op = 0
                    left_op.sign_op = -1
                    right_op = split.operator("mesh.offset_operator", text="", icon='TRIA_RIGHT')
                    right_op.type_op = 0
                    right_op.sign_op = 1
                    row = col_top.row(align=True)
                    if context.mode == 'EDIT_MESH':
                        row.prop(lt, "shift_copy", text="Copy")
                    else:
                        row.prop(lt, "instance", text='Instance')
                        row = col_top.row(align=True)
                        row.prop(lt, "shift_copy", text="Copy")

                # Polycross  ######-----------------------------------------
                split = col.split()
                if lt.disp_cpt:
                    split.prop(lt, "disp_cpt", text="Polycross", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "disp_cpt", text="Polycross", icon='RIGHTARROW_THIN')

                if lt.disp_cpt:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    split = row.split()
                    if lt.disp_cpt_project:
                        split.prop(lt, "disp_cpt_project", text="Project active", icon='DISCLOSURE_TRI_DOWN_VEC')
                    else:
                        split.prop(lt, "disp_cpt_project", text="Project active", icon='RIGHTARROW_THIN')

                    if lt.disp_cpt_project:
                        row = col_top.row(align=True)
                        split = row.split(0.5, True)
                        split.operator("mesh.polycross", text='Section').type_op = 0  # section and clear filter
                        split.operator("mesh.polycross", text='Cut').type_op = 1  # cross
                        row = col_top.row(align=True)
                        row.prop(lt, "fill_cuts", text="fill cut")
                        row = col_top.row(align=True)
                        row.prop(lt, "outer_clear", text="remove front")
                        row = col_top.row(align=True)
                        row.prop(lt, "inner_clear", text="remove bottom")

                    ######  Selection Filter  ######
                    row = col_top.row(align=True)
                    split = row.split()
                    if lt.disp_cpt_filter:
                        split.prop(lt, "disp_cpt_filter", text="Selection Filter", icon='DISCLOSURE_TRI_DOWN_VEC')
                    else:
                        split.prop(lt, "disp_cpt_filter", text="Selection Filter", icon='RIGHTARROW_THIN')

                    if lt.disp_cpt_filter:
                        row = col_top.row(align=True)
                        #row.active = lt.filter_edges or lt.filter_verts_bottom or lt.filter_verts_top
                        row.operator("mesh.polycross", text='to SELECT').type_op = 2  # only filter
                        row = col_top.row(align=True)
                        row.prop(lt, "filter_edges", text="Filter Edges")
                        row = col_top.row(align=True)
                        row.prop(lt, "filter_verts_top", text="Filter Top")
                        row = col_top.row(align=True)
                        row.prop(lt, "filter_verts_bottom", text="Filter Bottom")

                # AutoExtrude  ######-----------------------------------------
                split = col.split()
                if lt.disp_cpt_matExtrude:
                    split.prop(lt, "disp_cpt_matExtrude", text="AutoExtrude", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "disp_cpt_matExtrude", text="AutoExtrude", icon='RIGHTARROW_THIN')

                if lt.disp_cpt_matExtrude:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.get_mat4extrude", text='Get Mats')
                    row = col_top.row(align=True)
                    row.operator("mesh.mat_extrude", text='Template Extrude')

                # Spread Loop  ######-----------------------------------------

                split = col.split(percentage=0.15, align=True)

                if lt.display_cpt_spread:
                    split.prop(lt, "display_cpt_spread", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_spread", text="", icon='RIGHTARROW_THIN')

                spread_op = split.operator("mesh.spread_operator", text='Spread Loop')

                if lt.display_cpt_spread:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.prop(lt, 'spread_x', text='Spread X')
                    row = col_top.row(align=True)
                    row.prop(lt, 'spread_y', text='Spread Y')
                    row = col_top.row(align=True)
                    row.prop(lt, 'spread_z', text='Spread Z')
                    row = col_top.row(align=True)
                    row.prop(lt, 'relation', text='Relation')
                    box = box.box().column()
                    row = box.row(align=True)
                    row.prop(lt, 'shape_spline', text='Shape spline')
                    row = box.row(align=True)
                    row.active = lt.shape_spline
                    row.prop(lt, 'spline_Bspline2', text='Smooth transition')
                    row = box.row(align=True)

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Copy Tools  #######-------------------------------------------------------
    # Copy Tools  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_copy_edm:
                split.prop(lt, "display_cpt_copy_edm", text="...CopyShop...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_copy_edm", text="...CopyShop...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_cpt_copy_edm:

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.label("Material / UV / Image", icon="LINKED")

                mesh = context.object.data
                uv = len(mesh.uv_textures) > 1
                vc = len(mesh.vertex_colors) > 1

                row = col_top.row(align=True)
                op = row.operator("mesh.copy_face_settings", text="Copy Material")
                op['layer'] = ''
                op['mode'] = 'MAT'

                if mesh.uv_textures.active:

                    row = col_top.row(align=True)
                    op = row.operator("mesh.copy_face_settings", text="Copy Image")
                    op['layer'] = ''
                    op['mode'] = 'IMAGE'

                    row = col_top.row(align=True)
                    op = row.operator("mesh.copy_face_settings", text="Copy UV Coords")
                    op['layer'] = ''
                    op['mode'] = 'UV'

                if mesh.vertex_colors.active:

                    row = col_top.row(align=True)
                    op = row.operator("mesh.copy_face_settings", text="Copy Vertex Colors")
                    op['layer'] = ''
                    op['mode'] = 'VCOL'

                if uv or vc:
                    if uv:
                        row = col_top.row(align=True)
                        row.menu("MESH_MT_CopyImagesFromLayer")

                        row = col_top.row(align=True)
                        row.menu("MESH_MT_CopyUVCoordsFromLayer")

                    if vc:
                        row = col_top.row(align=True)
                        row.menu("MESH_MT_CopyVertexColorsFromLayer")

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Material Tools  #######-------------------------------------------------------
    # Material Tools  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_material_edm:
                split.prop(lt, "display_cpt_material_edm", text="...MatTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_material_edm", text="...MatTools...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_cpt_material_edm:

                wm = bpy.context.window_manager
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                layout.operator_context = 'INVOKE_REGION_WIN'

                row = col_top.row(align=True)
                row.menu("VIEW3D_MT_assign_material", text="Assign Material", icon='ZOOMIN')

                row = col_top.row(align=True)
                row.menu("VIEW3D_MT_select_material", text="Select by Material", icon='RESTRICT_SELECT_OFF')

                row = col_top.row(align=True)
                row.operator("meta.newmaterial", text="ObjColor", icon='ZOOMIN')
                row.prop(obj, "color", text="")

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # UV Mapping Edit  #######-------------------------------------------------------
    # UV Mapping Edit  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_unwrap:
                split.prop(lt, "display_cpt_unwrap", text="...UVTools ...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_unwrap", text="...UVTools....", icon='RIGHTARROW')

            #spread_op = split.operator("object.modifier_add", text="Subdivision Level", icon = 'MOD_SUBSURF').type="SUBSURF"

            if lt.display_cpt_unwrap:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)

                row.operator("mesh.mark_seam").clear = False
                row.operator("mesh.mark_seam", text="Clear Seam").clear = True

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("view3d.move_uv", text="Move UV [ALT+G]")
                row = col_top.row(align=True)
                row.operator("uv.reproject_image", text="Reproject Image")

                row = col_top.row(align=True)
                row.operator("uv.copy_uvs")
                row.operator("uv.paste_uvs")

    # Unwrap  ######-------------------------------------------------------
    # Unwrap  ######-------------------------------------------------------

                split = col.split()

                if lt.display_cpt_unwrapset:
                    split.prop(lt, "display_cpt_unwrapset", text="Unwrap", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_unwrapset", text="Unwrap", icon='DISCLOSURE_TRI_RIGHT_VEC')

                # split.operator("uv.reset",text="Reset")

                if lt.display_cpt_unwrapset:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("uv.unwrap", text="Unwrap")
                    row.operator("uv.reset", text="Reset")

                    row = col_top.row(align=True)
                    row.operator("uv.smart_project", text="Smart UV Project")

                    row = col_top.row(align=True)
                    row.operator("uv.lightmap_pack", text="Lightmap Pack")

                    row = col_top.row(align=True)
                    row.operator("uv.follow_active_quads", text="Follow Active Quads")

                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("uv.cube_project", text="Cube Project")

                    row = col_top.row(align=True)
                    row.operator("uv.cylinder_project", text="Cylinder Project")

                    row = col_top.row(align=True)
                    row.operator("uv.sphere_project", text="Sphere Project")

                    row = col_top.row(align=True)
                    row.operator("uv.tube_uv_unwrap", text="Tube Project")

                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("uv.project_from_view", text="Project from View").scale_to_bounds = False

                    row = col_top.row(align=True)
                    row.operator("uv.project_from_view", text="Project from View > Bounds").scale_to_bounds = True

    # SureUVW  ######-------------------------------------------------
    # SureUVW  ######-------------------------------------------------

                split = col.split()

                if lt.display_cpt_uvsure:
                    split.prop(lt, "display_cpt_uvsure", text="SureUVW", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_uvsure", text="SureUVW", icon='DISCLOSURE_TRI_RIGHT_VEC')

                # split.operator("uv.reset",text="Reset")

                if lt.display_cpt_uvsure:
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)

                    row.label("Press this button first:")
                    row = col_top.row(align=True)
                    row.operator("object.sureuvw_operator", text="Show active texture on editor").action = 'showtex'
                    row = col_top.row(align=True)
                    row.label("UVW Mapping:")
                    row = col_top.row(align=True)
                    row.operator("object.sureuvw_operator", text="UVW Box Map").action = 'box'
                    row = col_top.row(align=True)
                    row.operator("object.sureuvw_operator", text="Best Planar Map").action = 'bestplanar'
                    row = col_top.row(align=True)
                    row.label("1. Make Material With Raster Texture!")
                    row = col_top.row(align=True)
                    row.label("2. Set Texture Mapping Coords: UV!")
                    row = col_top.row(align=True)
                    row.label("3. Use Addon buttons")

    # TexSpace / Freestyle  ######-------------------------------------------------
    # TexSpace / Freestyle  ######-------------------------------------------------

                split = col.split()

                if lt.display_cpt_uvnext:
                    split.prop(lt, "display_cpt_uvnext", text="TexSpace / Freestyle", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_cpt_uvnext", text="TexSpace / Freestyle", icon='DISCLOSURE_TRI_RIGHT_VEC')

                # split.operator("uv.reset",text="Reset")

                if lt.display_cpt_uvnext:
                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.label(text="Texture Space:")

                    row = col_top.row(align=True)
                    row.operator("transform.translate", text="Move").texture_space = True
                    row.operator("mesh.mark_seam", text="Scale").clear = True

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.label(text="Freestyle:")

                    row = col_top.row(align=True)
                    row.operator("mesh.mark_freestyle_face", text="Mark Face").clear = False
                    row.operator("mesh.mark_freestyle_face", text="Clear Face").clear = True

                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Weight Only  #######-------------------------------------------------------
    # Weight Only  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_weight:
                split.prop(lt, "display_cpt_weight", text="...Weights...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_weight", text="...Weights...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_cpt_weight:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)

                row.label(text="> Set Weight Only Selected Vertices <")

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.label(text="to selected Vertex Group")

                row = col_top.row(align=True)
                row.operator("assignonly.selected", text="Set Weight")
                row.operator("del.unselected", text="Del All")
                row.operator("remall.vertex", text="Del Others")

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.label(text="to all Vertex Groups")

                row = col_top.row(align=True)
                row.operator("all_assignonly.selected", text="Set Weight")
                row.operator("all_del.unselected", text="Del All")
                row.operator("all_remall.vertex", text="Del Others")
                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Hook  ######-------------------------------------------------------
    # Hook  ######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_hook:
                split.prop(lt, "display_cpt_hook", text="...Hook...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_hook", text="...Hook...", icon='RIGHTARROW')

            #spread_op = split.operator_menu_enum("object.constraint_add", "type", text="Constraint", icon="CONSTRAINT_DATA")

            if lt.display_cpt_hook:
                box = col.column(align=True).box().column()

                col_top = box.column(align=True)
                row = col_top.row(align=True)

                row.operator_context = 'EXEC_AREA'
                row.operator("object.hook_add_newob", text="to New")
                row.operator("object.hook_add_selob", text="to Selected").use_bone = False

                row = col_top.row(align=True)
                row.operator("object.hook_add_selob", text="to Selected Object Bone").use_bone = True

                if [mod.type == 'HOOK' for mod in context.active_object.modifiers]:

                    row = col_top.row(align=True)
                    row.operator_menu_enum("object.hook_assign", "modifier")
                    row = col_top.row(align=True)
                    row.operator_menu_enum("object.hook_remove", "modifier")

                    row = col_top.row(align=True)
                    row.operator_menu_enum("object.hook_select", "modifier")
                    row = col_top.row(align=True)
                    row.operator_menu_enum("object.hook_reset", "modifier")
                    row = col_top.row(align=True)
                    row.operator_menu_enum("object.hook_recenter", "modifier")
                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # CleanUp  #######-------------------------------------------------------
    # CleanUp  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_cleanup:

                split.prop(lt, "display_cpt_cleanup", text="...Delete...", icon='DOWNARROW_HLT')
            else:

                split.prop(lt, "display_cpt_cleanup", text="...Delete...", icon='RIGHTARROW')

            if lt.display_cpt_cleanup:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("meshlint.select", "Meshlint > Mesh Data")

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.menu("VIEW3D_MT_edit_mesh_showhide", "Show / Hide")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.menu("mesh.cleandelete", text="Delete")
                row = col_top.row(align=True)
                row.operator("mesh.remove_doubles", "Remove Doubles")

                row = col_top.row(align=True)
                row.operator("mesh.delete_loose", text="Loose")
                row.operator("mesh.fill_holes")

                row = col_top.row(align=True)
                row.operator("mesh.vert_connect_nonplanar")

                row = col_top.row(align=True)
                row.operator("mesh.dissolve_degenerate")
                row = col_top.row(align=True)
                row.operator("mesh.dissolve_limited")
                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Bsurf  ############-------------------------------------------------------
    # Bsurf  ############-------------------------------------------------------
    # -------------------------------------------------------

            scn = context.scene

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_bsurf:
                ###space2###
                split.prop(lt, "display_cpt_bsurf", text="..Bsurfaces...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cpt_bsurf", text="...Bsurfaces...", icon='RIGHTARROW')

            ###space1###
            if lt.display_cpt_bsurf:

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                ###space2###

                row = col_top.row(align=True)
                row.operator("gpencil.surfsk_add_surface", text="Draw Mesh", icon='MOD_DYNAMICPAINT')
                row = col_top.row(align=True)
                row.operator("gpencil.surfsk_edit_strokes", text="Edit Strokes", icon="UV_SYNC_SELECT")

                row = col_top.row(align=True)
                row.prop(scn, "SURFSK_cyclic_cross")
                row = col_top.row(align=True)
                row.prop(scn, "SURFSK_cyclic_follow")
                row = col_top.row(align=True)
                row.prop(scn, "SURFSK_loops_on_strokes")
                row = col_top.row(align=True)
                row.prop(scn, "SURFSK_automatic_join")
                row = col_top.row(align=True)
                row.prop(scn, "SURFSK_keep_strokes")
                box = col.column(align=True).box().column()

    # -------------------------------------------------------
    # Grease Pencil  #######-------------------------------------------------------
    # Grease Pencil  #######-------------------------------------------------------
    # -------------------------------------------------------

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            split = row.split()

            if lt.display_cpt_pencil:
                split.prop(lt, "display_cpt_pencil", text="...PencilTools...", icon='DOWNARROW_HLT')
            else:

                split.prop(lt, "display_cpt_pencil", text="...PencilTools...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_cpt_pencil:
                #box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.prop(context.tool_settings, "use_grease_pencil_sessions", text="Keep Session")
                row = col_top.row(align=True)
                row.operator("gpencil.draw", text="Hand", icon="GREASEPENCIL").mode = 'DRAW'
                row = col_top.row(align=True)
                row.operator("gpencil.draw", text="Straight", icon="ZOOMOUT").mode = 'DRAW_STRAIGHT'
                row = col_top.row(align=True)
                row.operator("gpencil.draw", text="Polyline", icon="MESH_DATA").mode = 'DRAW_POLY'
                row = col_top.row(align=True)
                row.operator("gpencil.draw", text="Eraser", icon="PANEL_CLOSE").mode = 'ERASER'


############------------############
############  REGISTER  ############
############------------############


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
