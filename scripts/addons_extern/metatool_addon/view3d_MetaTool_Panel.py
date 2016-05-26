# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# bl_info = {
#    "name": "MetaTool",
#    "author": "marvin.k.breuer",
#    "version": (0, 1, 7),
#    "blender": (2, 72, 0),
#    "location": "View3D > Toolbar",
#    "warning": "",
#    "description": "Addon Collection",
#    "wiki_url": "",
#    "category": "User Interface",
#}


import bpy
from bpy import*


######################################################################################################################################################
############--------------------############
# Extesion Buttons  ##############################-------------------------------------------------------
# Extesion Buttons  ##############################-------------------------------------------------------
############--------------------############
######################################################################################################################################################

# create the Buttons in the Main Panel for the Sub Panels
bpy.types.Scene.osc_add = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_arrays = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_cad = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_manager = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_layer = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_layergroup = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_bonelayer = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_path = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_pathtex = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_modifier = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_visual = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_flymode = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_quickpref = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_snapshot = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_relation = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_uvs = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_clean = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_material = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_vfx = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_arewo = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_sniper = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_setup = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_scene = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_editing = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_curve = bpy.props.BoolProperty(default=False)
bpy.types.Scene.osc_grouper = bpy.props.BoolProperty(default=False)

######################################################################################################################################################
######################################################################################################################################################

# sgrouper
NUM_LAYERS = 20
SCENE_SGR = '#SGR'
UNIQUE_ID_NAME = 'sg_belong_id'


######################################################################################################################################################
########-------------#################
# Help Text  ##############################-------------------------------------------------------
# Help Text  ##############################-------------------------------------------------------
########-------------#################
######################################################################################################################################################

class VIEW3D_help1(bpy.types.Operator):
    """how to"""
    bl_idname = 'help.operator1'
    bl_label = ''

    def draw(self, context):
        layout = self.layout
        layout.label('a. > set pivot')
        layout.label('b. > mirror editable local')
        layout.label('c. > flatten vertices like scale+(xyz)+0+enter')

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=250)

bpy.utils.register_class(VIEW3D_help1)


class VIEW3D_help2(bpy.types.Operator):
    """how to"""
    bl_idname = 'help.operator2'
    bl_label = ''

    def draw(self, context):
        layout = self.layout
        layout.label('a. > as middle point for mirror')
        layout.label('b. > to align location to other objects')
        layout.label('c. > for local rotation on large objects')

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=200)

bpy.utils.register_class(VIEW3D_help2)


class VIEW3D_help3(bpy.types.Operator):
    bl_idname = 'help.operator3'
    bl_label = ''

    def draw(self, context):
        layout = self.layout
        layout.label('down turn view by use...')
        layout.label('or your view jump out of range...')
        layout.label('select any vertex after execute for stable view...')

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=300)

bpy.utils.register_class(VIEW3D_help3)


class VIEW3D_help4(bpy.types.Operator):
    bl_idname = "help.operator4"
    bl_label = ''

    def draw(self, context):
        layout = self.layout
        layout.label('> Make single from duplication (object property) <')
        layout.label('1. parent selected to activ / 2. apply Make Duplicates Real')
        layout.label('3. clear Parent / 4. to Join > selected Linked Object Data')

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=300)

bpy.utils.register_class(VIEW3D_help4)


######################################################################################################################################################
########-----------------#################
# History Menus  ##############################-------------------------------------------------------
# History Menus  ##############################-------------------------------------------------------
########-----------------#################
######################################################################################################################################################

# History A  ##################-------------------------------------------------------
# History A  ##################-------------------------------------------------------

def draw_A_history_tools(context, layout):
    lt = context.window_manager.metawindow

    box = layout.box().column(True)
    row = box.row(align=True)

    row.operator("screen.redo_last", text="", icon="SCRIPTWIN")
    row.menu("VIEW3D_CameraView", text="", icon="CAMERA_DATA")
    row.operator("view3d.ruler", text="Ruler")
    row.menu("VIEW3D_MTK_Datablock", text="", icon="PANEL_CLOSE")

    row = box.row(align=True)
    row.operator("ed.undo", text="", icon="LOOP_BACK")
    row.operator("ed.redo", text="", icon="LOOP_FORWARDS")
    row.operator("ed.undo_history", text="History")

    if lt.display_extension:
        row.prop(lt, "display_extension", text="", icon='COPYDOWN')
    else:
        row.prop(lt, "display_extension", text="", icon='PASTEDOWN')

    if lt.display_extension:
        col = layout.column(align=True)
        box = col.column(align=True).box().column()
        col_top = box.column(align=True)

        row = col_top.row(align=True)
        # WIP
        row.prop(bpy.context.scene, "osc_editing", text="Compact Tools", icon="EDIT")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_relation", text="Relation", icon="CONSTRAINT_DATA")
        row.prop(bpy.context.scene, "osc_arrays", text="Arrays", icon="MOD_ARRAY")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_uvs", text="UVs", icon="UV_FACESEL")
        row.prop(bpy.context.scene, "osc_clean", text="Delete", icon="PANEL_CLOSE")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_material", text="Material", icon="MATERIAL")
        row.prop(bpy.context.scene, "osc_pathtex", text="Textur", icon="LOGIC")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_vfx", text="VFX", icon="DRIVER")
        row.prop(bpy.context.scene, "osc_sniper", text="Sniper", icon="DRIVER")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_arewo", text="Arewo", icon="DRIVER")
        row.prop(bpy.context.scene, "osc_snapshot", text="Snapshot", icon="OUTLINER_DATA_CAMERA")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_scene", text="Scene", icon="RENDER_ANIMATION")
        row.prop(bpy.context.scene, "osc_grouper", text="SGrouper", icon="RESTRICT_SELECT_OFF")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_layer", text="Layer Mg.", icon="COLLAPSEMENU")
        row.prop(bpy.context.scene, "osc_layergroup", text="Layer Grp.", icon="COLLAPSEMENU")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_path", text="Path", icon="UI")
        row.prop(bpy.context.scene, "osc_quickpref", text="QuickPref", icon="LAMP_DATA")

    draw_name_tools(context, layout)


# History B  ##################-------------------------------------------------------
# History B  ##################-------------------------------------------------------

def draw_B_history_tools(context, layout):
    lt = context.window_manager.metawindow

    box = layout.box().column(True)

    row = box.row(align=True)
    row.operator("screen.redo_last", text="", icon="SCRIPTWIN")
    row.menu("VIEW3D_CameraView", text="", icon="CAMERA_DATA")
    row.operator("view3d.ruler", text="Ruler")  # , icon="NOCURVE")

    obj = context.active_object
    mode_string = context.mode
    edit_object = context.edit_object

    if mode_string == 'EDIT_MESH':
        row.menu("mesh.cleandelete", "", icon="PANEL_CLOSE")
    elif mode_string == 'EDIT_CURVE':
        row.operator("curve.delete", "", icon="PANEL_CLOSE")
    elif mode_string == 'EDIT_SURFACE':
        row.operator("curve.delete", "", icon="PANEL_CLOSE")
    elif mode_string == 'EDIT_METABALL':
        row.operator("mball.delete_metaelems", "", icon="PANEL_CLOSE")
    elif mode_string == 'EDIT_ARMATURE':
        row.operator("armature.delete", "", icon="PANEL_CLOSE")

    row = box.row(align=True)
    row.operator("ed.undo", text="", icon="LOOP_BACK")
    row.operator("ed.redo", text="", icon="LOOP_FORWARDS")
    row.operator("ed.undo_history", text="History")

    if lt.display_extension:
        row.prop(lt, "display_extension", text="", icon='COPYDOWN')
    else:
        row.prop(lt, "display_extension", text="", icon='PASTEDOWN')

    if lt.display_extension:
        col = layout.column(align=True)
        box = col.column(align=True).box().column()
        col_top = box.column(align=True)

        #row = col_top.row(align=True)
        # WIP
        #row.prop(bpy.context.scene, "osc_editing", text="Compact Tools", icon="EDIT")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_relation", text="Relation", icon="CONSTRAINT_DATA")
        row.prop(bpy.context.scene, "osc_arrays", text="Arrays", icon="MOD_ARRAY")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_uvs", text="UVs", icon="UV_FACESEL")
        row.prop(bpy.context.scene, "osc_clean", text="Delete", icon="PANEL_CLOSE")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_material", text="Material", icon="MATERIAL")
        row.prop(bpy.context.scene, "osc_pathtex", text="Textur", icon="LOGIC")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_vfx", text="VFX", icon="DRIVER")
        row.prop(bpy.context.scene, "osc_sniper", text="Sniper", icon="DRIVER")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_arewo", text="Arewo", icon="DRIVER")
        row.prop(bpy.context.scene, "osc_snapshot", text="Snapshot", icon="OUTLINER_DATA_CAMERA")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_scene", text="Scene", icon="RENDER_ANIMATION")
        row.prop(bpy.context.scene, "osc_grouper", text="SGrouper", icon="RESTRICT_SELECT_OFF")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_layer", text="Layer Mg.", icon="COLLAPSEMENU")
        row.prop(bpy.context.scene, "osc_layergroup", text="Layer Grp.", icon="COLLAPSEMENU")

        row = col_top.row(align=True)
        row.prop(bpy.context.scene, "osc_path", text="Path", icon="UI")
        row.prop(bpy.context.scene, "osc_quickpref", text="QuickPref", icon="LAMP_DATA")

    draw_name_tools(context, layout)


# Keyframing  ##################-------------------------------------------------------
# Keyframing  ##################-------------------------------------------------------

def draw_keyframing_tools(context, layout):
    if context.mode == "OBJECT" or context.mode == "POSE":

        if context.active_object and context.active_object.type in {'MESH', 'CURVE', 'SURFACE', 'ARMATURE', 'META', 'LATTICE'}:

            col = layout.column(align=True)
            row = col.row(align=True)
            row.operator("anim.keyframe_insert_menu", icon='ZOOMIN', text="")
            row.operator("anim.keyframe_delete_v3d", icon='ZOOMOUT', text="")
            row.prop_search(context.scene.keying_sets_all, "active", context.scene, "keying_sets_all", text="")
            row.operator("anim.keyframe_insert", text="", icon='KEY_HLT')
            row.operator("anim.keyframe_delete", text="", icon='KEY_DEHLT')


# Name  ##################-------------------------------------------------------
# Name  ##################-------------------------------------------------------

def draw_name_tools(context, layout):
    lt = context.window_manager.metawindow
    ### space ###
    active_obj = context.active_object
    obj = context.object

    box = layout.box().column()
    row = box.row(align=True)

    row.prop(bpy.context.object, "name", text="Active")

    # Rename Settings
    #--------------------#
    scn = context.scene
    rs = bpy.context.scene
    #--------------------#

    if lt.display_objrename:
        row.prop(lt, "display_objrename_adv", text="", icon='SCRIPTPLUGINS')

    else:
        row.prop(lt, "display_objrename_adv", text="", icon='SCRIPTPLUGINS')

    if lt.display_objrename_adv:

        col_top = box.column(align=True)
        row = layout.row(align=True)
        row.alignment = 'EXPAND'

        # ----------- RESPECT ORDER ------------------ #

        col = row.column()
        subrow = col.row()
        subrow.prop(context.scene, 'rno_bool_keepOrder', text='')
        subrow.enabled = False
        col = row.column()
        subrow = col.row()
        subrow.operator("object.rno_keep_selection_order", "Respect Selection")

        # ----------- NEW NAME ------------------ #

        row = layout.row()
        box = row.box()
        rbox = box.row(align=True)
        rbox.prop(context.scene, "rno_str_new_name")
        rbox = box.row(align=True)
        rbox.prop(context.scene, "rno_bool_numbered")
        rbox.prop(context.scene, "rno_str_numFrom")
        rbox = box.row()
        rbox.operator("object.rno_setname", "Set new Name")
        rbox.operator("object.copynametodata", "Copy to Data Name")

        # ----------- REPLACE NAME ------------------ #

        row = layout.row()
        box = row.box()
        rbox = box.column(align=True)
        rbox.prop(context.scene, "rno_str_old_string")
        rbox.prop(context.scene, "rno_str_new_string")
        box.operator("object.rno_replace_in_name", "Replace Name")

        # ----------- ADD SUBFIX / PREFIX NAME ------------------ #
        row = layout.row()
        box = row.box()
        rbox = box.row()

        box.prop(context.scene, 'rno_bool_keepIndex', text='keep object Index')
        rbox.prop(context.scene, "rno_str_prefix")
        rbox.prop(context.scene, "rno_str_subfix")

        box.operator("object.rno_add_subfix_prefix", "Add Subfix / Prefix")

        # ----------- MATERIAL RENAME ------------------ #

        row = layout.row()
        box1 = row.box()
        row = box1.row()

        row.operator("rename.initbutton", text="Activate to get Materialname (!)")
        row = box1.row()
        row.prop(scn, 'naming_base', expand=True)
        row = box1.row()
        row.prop(scn, 'rename_custom', "")

        ###

        row = box1.row()
        row.prop(scn, 'rename_use_prefix', text="Prefix")
        row.prop(scn, 'rename_prefix', text="")

        row = box1.row()
        row.prop(scn, 'rename_object', "Object")
        row.prop(scn, 'rename_data', 'Data')
        row.prop(scn, 'rename_material', 'Material')

        row = box1.row()
        row.operator("rename.button", text="Rename", icon='GREASEPENCIL')

        ###

        """
        row=layout.row()
        box2 = row.box()
        row = box2.row()  
        row.label('Datablocks to Rename:')
        
        row = box2.row()  
        row.prop(scn, 'rename_object', "Object") 
        row.prop(scn, 'rename_data', 'Data') 
        row.prop(scn, 'rename_material', 'Material')
        

        ### 
      
        row = box2.row() 
        row.label ("Where to add?")
        
        row = box2.row() 
        row.prop(scn, 'prefix_object')     
        row.prop(scn,'prefix_data')       
        row.prop(scn, 'prefix_material')
        """


######################################################################################################################################################
########-------------#################
# TAB-Panel  ##############################-------------------------------------------------------
# TAB-Panel  ##############################-------------------------------------------------------
########-------------#################
######################################################################################################################################################

######  Objectmode  #############
######  Objectmode  #############

class VIEW3D_ObjectMode(bpy.types.Panel):
    bl_category = 'META'
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_label = "MetaTool"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'OBJECT'))

    def draw(self, context):
        lt = context.window_manager.metawindow
        layout = self.layout

        obj = context.object
        scene = context.scene
        scn = context.scene
        rs = bpy.context.scene
        ob = context.object
        layout.operator_context = 'INVOKE_REGION_WIN'

        # --------------------------

        col = layout.column(align=True)
        box = col.column(align=True).box().column()
        col_top = box.column(align=True)

        row = col_top.row(align=True)
        row.alignment = 'CENTER'
        sub = row.row(1)
        sub.scale_x = 1
        sub.menu("INFO_MT_mesh_add", text="", icon='OUTLINER_OB_MESH')
        sub.menu("INFO_MT_curve_add", text="", icon='OUTLINER_OB_CURVE')
        sub.menu("INFO_MT_surface_add", text="", icon='OUTLINER_OB_SURFACE')
        sub.menu("INFO_MT_metaball_add", text="", icon="OUTLINER_OB_META")
        sub.operator("object.camera_add", icon='OUTLINER_OB_CAMERA', text="")
        sub.operator("object.armature_add", text="", icon="OUTLINER_OB_ARMATURE")
        row.operator("object.bounding_boxers", text="", icon="BBOX")

        row = col_top.row(align=True)
        row.alignment = 'CENTER'
        sub = row.row(1)
        sub.scale_x = 1
        sub.operator("object.empty_add", text="", icon="OUTLINER_OB_EMPTY")
        sub.operator("object.add", text="", icon="OUTLINER_OB_LATTICE").type = "LATTICE"
        sub.operator("object.text_add", text="", icon="OUTLINER_OB_FONT")
        sub.operator("object.lamp_add", icon='OUTLINER_OB_LAMP', text="")
        sub.operator("object.speaker_add", icon='OUTLINER_OB_SPEAKER', text="")
        sub.operator_menu_enum("object.effector_add", "type", text="", icon="SOLO_ON")
        row.operator("mesh.emptyroom_cen", text="", icon='RETOPO')


# -------------------------------------------------------
# Im-Export  #######-------------------------------------------------------
# Im-Export  #######-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        if context.mode == 'OBJECT':

            ###space1###
            if lt.display_imexport:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_imexport", text="", icon='TRIA_DOWN')
            else:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_imexport", text="", icon='TRIA_RIGHT')

            row.label("Im-Export...")
            row.menu("INFO_MT_file_import", text="", icon='IMPORT')
            row.menu("INFO_MT_file_export", text="", icon='EXPORT')
            row.operator("wm.link", text="", icon='LINK_BLEND')
            row.operator("wm.append", text="", icon='APPEND_BLEND')
            ###space1###
            if lt.display_imexport:
                ###space2###
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row()
                row.alignment = 'CENTER'
                row.scale_x = 1.25
                row.menu("OBJECT_MT_selected_export", text="Export Selected", icon='EXPORT')

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("object.make_local")
                row.operator("object.proxy_make")

                col = layout.column(align=True)
                split = col.split()  # percentage=0.15)

                if lt.display_imexmanage:
                    split.prop(lt, "display_imexmanage", text="...Pack & Pathes...", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_imexmanage", text="...Pack & Pathes...", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("", text="", icon="")

                if lt.display_imexmanage:

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

                    col = layout.column(align=True)
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

                if lt.display_imexfolder:
                    split.prop(lt, "display_imexfolder", text="...Production Setup...", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_imexfolder", text="...Production Setup...", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("", text="", icon="")

                if lt.display_imexfolder:
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


# -------------------------------------------------------
# Transform  ######-------------------------------------------------------
# Transform  ######-------------------------------------------------------
# -------------------------------------------------------

        #col = layout.column(align=True)
        if lt.display_transform:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_transform", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_transform", text="", icon='TRIA_RIGHT')

        row.label("Transform...")
        row.operator("mesh.snap_utilities_move", text="", icon="NDOF_TRANS")
        row.operator("mesh.snap_utilities_rotate", text="", icon="NDOF_TURN")
        row.operator("freeze_transform.selected", text="", icon="NDOF_DOM")

        if lt.display_transform:

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("transform.translate", text="(G)", icon="MAN_TRANS")
            row.operator("transform.rotate", text="(R)", icon="MAN_ROT")
            row.operator("transform.resize", text="(S)", icon="MAN_SCALE")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            if context.object:

                row = col_top.row(align=True)
                row.label(text="", icon="MAN_TRANS")
                row.prop(context.object, 'location', text="")

                row = col_top.row(align=True)
                row.label(text="", icon="MAN_ROT")
                row.prop(context.object, 'rotation_euler', text="")

                row = col_top.row(align=True)
                row.label(text="", icon="MAN_SCALE")
                row.prop(context.object, 'scale', text="")

                row = col_top.row(align=True)
                row.label(text="", icon="MOD_MESHDEFORM")
                row.prop(context.object, 'dimensions', text="")

            col_top = box.column(align=True)
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.duplicate", text="Duplicate Object", icon="ZOOMIN")


# ------------------------------------------------------------
# Selection  ######------------------------------------------------------------
# Selection  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_selection:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selection", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selection", text="", icon='TRIA_RIGHT')

        row.label("Select...")
        row.operator("object.move_to_layer", text="", icon="NLA")
        row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")
        row.operator("view3d.select_border", text="", icon="BORDER_RECT")
        row.menu("VIEW3D_MT_object_showhide", "", icon="VISIBLE_IPO_ON")

        if lt.display_selection:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("object.select_all", text="Inverse", icon="FILE_REFRESH").action = 'INVERT'
            row.operator("object.select_camera", text="Camera", icon="OUTLINER_DATA_CAMERA")

            row = col_top.row(align=True)
            row.operator("object.select_random", text="Random", icon="RNDCURVE")
            row.operator("object.select_mirror", text="Mirror", icon="ARROW_LEFTRIGHT")

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.select_linked", text="Linked", icon="LINKED")
            row.operator("object.select_grouped", text="Group", icon="GROUP")

            row = col_top.row(align=True)
            row.operator("object.select_by_type", text="Type", icon="ZOOM_ALL")
            row.operator("object.select_pattern", text="Name", icon="OUTLINER_DATA_FONT")

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("object.select_by_layer", text="Select by Layer")
            row.operator("object.throughselected", text="Cycle through")

            row = col_top.row(align=True)
            row.operator("view3d.view_selected", "", icon="ZOOM_SELECTED")
            row.operator("object.select_linked", text="Separate Active").type = 'OBDATA'
            row.operator("view3d.view_all", "", icon="ZOOM_OUT")

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("vfxtoolbox.freeze_selected_objects", text="Freeze", icon="RESTRICT_SELECT_ON")
            row.operator("vfxtoolbox.defreeze_all_objects", text="Unfreeze", icon="RESTRICT_SELECT_OFF")
            row = col_top.row(align=True)
            row.menu("mtk_freezeall", text="(Un)Freeze by Type", icon="FREEZE")


# ------------------------------------------------------------
# Align Location ######------------------------------------------------------------
# Align Location ######------------------------------------------------------------
# ------------------------------------------------------------

        #col = layout.column(align=True)

        if lt.display_location:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_location", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_location", text="", icon='TRIA_RIGHT')

        row.label("Align...")
        row.operator("object.align_location_all", text="", icon='MAN_TRANS')
        row.operator("object.align_rotation_all", text="", icon='MAN_ROT')
        row.operator("object.align_objects_scale_all", text="", icon='MAN_SCALE')
        row.operator("object.align_tools", text="", icon="ROTATE")

        if lt.display_location:
            ###space2###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("object.loops1", text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="MZ", icon='ARROW_LEFTRIGHT')

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("object.align_by_faces", text="Active Face to Active Face", icon="SNAP_SURFACE")

            row = col_top.row(align=True)
            row.operator("object.drop_on_active", text="Drop down to Active", icon="NLA_PUSHDOWN")

            row = col_top.row(align=True)
            row.operator("object.distribute_osc", text="Distribute Objects", icon="ALIGN")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("object.make_single_user", "", icon="UNLINKED")
            row.operator("mft.radialclone", text="Radial Instance Clone", icon="RECOVER_LAST")

            row = col_top.row(align=True)
            row.operator("object.simplearewo", text="Replicator", icon="NEXT_KEYFRAME")
            row.operator("object.cursor_array", text="Copy 2 Cursor", icon="FORCE_FORCE")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("object.align_location_all", text=" ", icon='MAN_TRANS')
            row.operator("object.align_location_x", text="X")
            row.operator("object.align_location_y", text="Y")
            row.operator("object.align_location_z", text="Z")

            sub = row.row(1)
            sub.scale_x = 2.0
            sub.operator("object.location_clear", text="", icon="X")

            props = row.operator("object.transform_apply", text="", icon="FILE_TICK")
            props.location = True
            props.rotation = False
            props.scale = False

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.align_rotation_all", text=" ", icon='MAN_ROT')
            row.operator("object.align_rotation_x", text="X")
            row.operator("object.align_rotation_y", text="Y")
            row.operator("object.align_rotation_z", text="Z")

            sub = row.row(1)
            sub.scale_x = 2.0
            sub.operator("object.rotation_clear", text="", icon="X")
            row. operator("object.loops8", "", icon="FILE_TICK")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.align_objects_scale_all", text=" ", icon='MAN_SCALE')
            row.operator("object.align_objects_scale_x", text="X")
            row.operator("object.align_objects_scale_y", text="Y")
            row.operator("object.align_objects_scale_z", text="Z")

            sub = row.row(1)
            sub.scale_x = 2.0
            sub.operator("object.scale_clear", text="", icon="X")

            props = row.operator("object.transform_apply", text="", icon="FILE_TICK")
            props.location = False
            props.rotation = False
            props.scale = True

    # -------------------------------------------------------
    # 1D Align Tool  ######-----------------------------------------
    # 1D Align Tool  ######-----------------------------------------
    # -------------------------------------------------------

            if lt.display_1d:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_1d", text="...1d Script...", icon='DOWNARROW_HLT')
            else:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_1d", text="...1d Script...", icon='RIGHTARROW')

            if lt.display_1d:
                ###space2###

                col = layout.column(align=True)

                split = col.split()

                if lt.display_align:
                    split.prop(lt, "display_align", text="Align Edges", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_align", text="Align Edges", icon='RIGHTARROW_THIN')

                box = col.column(align=True)
                if lt.display_align and context.mode == 'EDIT_MESH':
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

                if lt.display_align and context.mode == 'OBJECT':
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
                if lt.display_3dmatch:
                    split.prop(lt, "display_3dmatch", text="3D Match", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_3dmatch", text="3D Match", icon='RIGHTARROW_THIN')

                if lt.display_3dmatch:
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
                if lt.display_offset:
                    split.prop(lt, "display_offset", text="SideShift", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_offset", text="SideShift", icon='RIGHTARROW_THIN')

                if lt.display_offset:
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
                if lt.disp_cp:
                    split.prop(lt, "disp_cp", text="Polycross", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "disp_cp", text="Polycross", icon='RIGHTARROW_THIN')

                if lt.disp_cp:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    split = row.split()
                    if lt.disp_cp_project:
                        split.prop(lt, "disp_cp_project", text="Project active", icon='DISCLOSURE_TRI_DOWN_VEC')
                    else:
                        split.prop(lt, "disp_cp_project", text="Project active", icon='RIGHTARROW_THIN')

                    if lt.disp_cp_project:
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
                    if lt.disp_cp_filter:
                        split.prop(lt, "disp_cp_filter", text="Selection Filter", icon='DISCLOSURE_TRI_DOWN_VEC')
                    else:
                        split.prop(lt, "disp_cp_filter", text="Selection Filter", icon='RIGHTARROW_THIN')

                    if lt.disp_cp_filter:
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
                if lt.disp_matExtrude:
                    split.prop(lt, "disp_matExtrude", text="AutoExtrude", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "disp_matExtrude", text="AutoExtrude", icon='RIGHTARROW_THIN')

                if lt.disp_matExtrude:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.get_mat4extrude", text='Get Mats')
                    row = col_top.row(align=True)
                    row.operator("mesh.mat_extrude", text='Template Extrude')

                # Spread Loop  ######-----------------------------------------
                split = col.split(percentage=0.15, align=True)
                if lt.display:
                    split.prop(lt, "display", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display", text="", icon='RIGHTARROW_THIN')

                spread_op = split.operator("mesh.spread_operator", text='Spread Loop')

                if lt.display:
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


# ------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_orient:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orient", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orient", text="", icon='TRIA_RIGHT')

        # row.label("Route...")
        sub = row.row(1)
        sub.scale_x = 7
        sub.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
        sub.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
        sub.operator("view3d.pivot_active", "", icon="ROTACTIVE")
        sub.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
        sub.operator("view3d.pivot_median", "", icon="ROTATECENTER")

        if lt.display_orient:
            ###space###

            # Origin Setup Alternative ######------------------------------------------------------------
            # Origin Setup Alternative ######------------------------------------------------------------

            """
            col = layout.column(align=True)  
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)                          

            row = col_top.row(align=True)  
            #row.menu("originsetupmenu_obm", text="Set Origin")
            row.operator_menu_enum("object.origin_set", "type", text="Set Origin")
            row.menu("object.bbox_origin_side_menu","Side")             
            row.operator("object.origin_set", text="", icon="OBJECT_DATAMODE").type='ORIGIN_GEOMETRY'

            row = col_top.row(align=True)
            row.menu("object.bbox_origin_corner_menu","Corner")
            row.menu("object.bbox_origin_edge_menu","Edge")
            row.operator("object.origin_set", text="", icon="FORCE_FORCE").type='ORIGIN_CURSOR' 


            col = layout.column(align=True)  
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.menu("mtk_snaptocursor","Cursor to... ")     
            row.operator("view3d.snap_cursor_to_active", "", icon = "PMARKER")
            row.operator("view3d.snap_cursor_to_center", "", icon = "OUTLINER_DATA_EMPTY")            

            row = col_top.row(align=True)
            row.menu("mtk_snaptoselect","Selection to... ")
            row.operator("view3d.snap_selected_to_cursor","", icon="STICKY_UVS_VERT").use_offset = True   
            row.operator("view3d.snap_selected_to_cursor","", icon="RESTRICT_SELECT_OFF").use_offset = False
            """

            ###space###
            col = layout.column(align=True)
            obj = context.active_object
            if obj:
                obj_type = obj.type
                ###space2###
                if obj_type in {'MESH', 'CURVE', 'SURFACE', 'ARMATURE', 'FONT', 'LATTICE', 'META'}:

                    if context.mode == 'OBJECT':
                        box = col.column(align=True).box().column()
                        col_top = box.column(align=True)
                        row = col_top.row(align=True)
                        row.alignment = 'CENTER'
                        row.label("Set Origin", icon="LAYER_ACTIVE")
                        col_top = box.column(align=True)
                        row = col_top.column_flow(2)
                        row.operator("object.origin_set", text="to Cursor").type = 'ORIGIN_CURSOR'
                        row.operator("object.origin_set", text="to Mass ").type = 'ORIGIN_CENTER_OF_MASS'
                        row.operator("object.origin_set", text="to Geometry").type = 'ORIGIN_GEOMETRY'
                        row.operator("object.origin_set", text="Geometry to").type = 'GEOMETRY_ORIGIN'

            ###space###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            if lt.display_bboxback:
                row.scale_y = 1.2
                row.prop(lt, "display_bboxback", text="Back +Y", icon='TRIA_DOWN')

            else:
                row.scale_y = 1
                row.prop(lt, "display_bboxback", text="Back +Y", icon='TRIA_RIGHT')

            ###space1###
            if lt.display_bboxback:
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                # Top
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubeback_cornertop_minus_xy", "", icon="LAYER_ACTIVE")  # "Back- Left -Top")
                row.operator("object.cubeback_edgetop_minus_y", "", icon="LAYER_ACTIVE")  # "Back - Top")
                row.operator("object.cubeback_cornertop_plus_xy", "", icon="LAYER_ACTIVE")  # "Back- Right -Top ")

                # Middle
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55
                row.operator("object.cubefront_edgemiddle_minus_x", "", icon="LAYER_ACTIVE")  # "Back- Left")
                row.operator("object.cubefront_side_plus_y", "", icon="LAYER_ACTIVE")  # "Back")
                row.operator("object.cubefront_edgemiddle_plus_x", "", icon="LAYER_ACTIVE")  # "Back- Right")

                # Bottom
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55
                row.operator("object.cubeback_cornerbottom_minus_xy", "", icon="LAYER_ACTIVE")  # "Back- Left -Bottom")
                row.operator("object.cubefront_edgebottom_plus_y", "", icon="LAYER_ACTIVE")  # "Back - Bottom")
                row.operator("object.cubeback_cornerbottom_plus_xy", "", icon="LAYER_ACTIVE")  # "Back- Right -Bottom")

                ##############################
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = box.column(1)

            ###space1###

            #col = layout.column(align=True)
            if lt.display_bboxmiddle:
                row.scale_y = 1.2
                row.prop(lt, "display_bboxmiddle", text="Middle", icon='TRIA_DOWN')

            else:
                row.scale_y = 1
                row.prop(lt, "display_bboxmiddle", text="Middle", icon='TRIA_RIGHT')

            ###space1###
            if lt.display_bboxmiddle:
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                # Top
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubefront_edgetop_minus_x", "", icon="LAYER_ACTIVE")  # "Middle - Left Top")
                row.operator("object.cubefront_side_plus_z", "", icon="LAYER_ACTIVE")  # "Top")
                row.operator("object.cubefront_edgetop_plus_x", "", icon="LAYER_ACTIVE")  # "Middle - Right Top")

                # Middle
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubefront_side_minus_x", "", icon="LAYER_ACTIVE")  # "Left")
                obj = context.object
                if obj and obj.mode == 'EDIT':
                    row.operator("mesh.origincenter", text="", icon="LAYER_ACTIVE")
                else:
                    row.operator("object.origin_set", text="", icon="LAYER_ACTIVE").type = 'ORIGIN_GEOMETRY'

                row.operator("object.cubefront_side_plus_x", "", icon="LAYER_ACTIVE")  # "Right")

                # Bottom
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubefront_edgebottom_minus_x", "", icon="LAYER_ACTIVE")  # "Middle - Left Bottom")
                row.operator("object.cubefront_side_minus_z", "", icon="LAYER_ACTIVE")  # "Bottom")
                row.operator("object.cubefront_edgebottom_plus_x", "", icon="LAYER_ACTIVE")  # "Middle - Right Bottom")

                ##############################
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)

            ###space1###

            if lt.display_bboxfront:
                row.scale_y = 1.2
                row.prop(lt, "display_bboxfront", text="Front -Y", icon='TRIA_DOWN')

            else:
                row.scale_y = 1
                row.prop(lt, "display_bboxfront", text="Front -Y", icon='TRIA_RIGHT')

            ###space1###
            if lt.display_bboxfront:
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                # Top
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubefront_cornertop_minus_xy", "", icon="LAYER_ACTIVE")  # "Front- Left -Top"
                row.operator("object.cubeback_edgetop_plus_y", "", icon="LAYER_ACTIVE")  # "Front - Top"
                row.operator("object.cubefront_cornertop_plus_xy", "", icon="LAYER_ACTIVE")  # "Front- Right -Top"

                # Middle
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubefront_edgemiddle_minus_y", "", icon="LAYER_ACTIVE")  # "Front- Left"
                row.operator("object.cubefront_side_minus_y", "", icon="LAYER_ACTIVE")  # "Front"
                row.operator("object.cubefront_edgemiddle_plus_y", "", icon="LAYER_ACTIVE")  # "Front- Right"

                # Bottom
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubefront_cornerbottom_minus_xy", "", icon="LAYER_ACTIVE")  # "Front- Left -Bottom"
                row.operator("object.cubefront_edgebottom_minus_y", "", icon="LAYER_ACTIVE")  # "Front - Bottom"
                row.operator("object.cubefront_cornerbottom_plus_xy", "", icon="LAYER_ACTIVE")  # "Front- Right -Bottom")

            ###space1###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Cursor", icon="FORCE_FORCE")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)
            row.operator("view3d.snap_cursor_to_grid", "to Grid")
            row.operator("view3d.snap_cursor_to_active", "to Active")
            row.operator("view3d.snap_cursor_to_center", "to Center")
            row.operator("view3d.snap_cursor_to_selected", "to Selected")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Selected", icon="RESTRICT_SELECT_OFF")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)
            row.operator("view3d.snap_selected_to_grid", "to Grid")
            row.operator("view3d.snap_selected_to_cursor", "to Offset").use_offset = True
            row.operator("mesh.snapcenteroffset", " to Center")
            row.operator("view3d.snap_selected_to_cursor", "to Cursor").use_offset = False


# -------------------------------------------------------
# CAD Tools  ############-------------------------------------------------------
# CAD Tools  ############-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        if context.mode == 'OBJECT':

            obj = context.active_object
            if obj:
                obj_type = obj.type

                if obj_type in {'MESH', 'CURVE'}:

                    ###space1###
                    #col = layout.column(align=True)
                    if lt.display_bool:
                        ###space2###
                        box = layout.box()
                        row = box.row()
                        row.prop(lt, "display_bool", text="", icon='TRIA_DOWN')
                    else:
                        box = layout.box()
                        row = box.row()
                        row.prop(lt, "display_bool", text="", icon='TRIA_RIGHT')

                    row.label("CAD...")

                    obj = context.active_object
                    if obj:
                        obj_type = obj.type

                        if obj_type in {'MESH'}:

                            row.operator("object.join", text="", icon="FULLSCREEN_EXIT")

                            union = row.operator("mesh.boolean", "", icon='ZOOMIN')
                            union.modOp = 'UNION'

                            intersect = row.operator("mesh.boolean", "", icon='PANEL_CLOSE')
                            intersect.modOp = 'INTERSECT'

                            difference = row.operator("mesh.boolean", "", icon='ZOOMOUT')
                            difference.modOp = 'DIFFERENCE'

                        if obj_type in {'CURVE'}:
                            row.operator("object.convert", text="to Mesh", icon="MESH_DATA").target = "MESH"

                    ###space1###
                    if lt.display_bool:
                        ###space2###
                        col = layout.column(align=True)
                        box = col.column(align=True).box().column()

                        col_top = box.column(align=True)
                        row = col_top.row(align=True)
                        row.operator("object.set_instance", "Set Instance", icon="LINKED")
                        row.operator("mesh.intersect_meshes", text="Intersect Line", icon="GROUP")

                        row = col_top.row(align=True)
                        row.operator("retopo.latticeapply", "Apply E-Lattice", icon="OUTLINER_DATA_LATTICE")
                        row.operator("object.editnormals_transfer", text="Transfer Normals", icon="SNAP_NORMAL")

                        if obj_type in {'MESH'}:
                            box = col.column(align=True).box().column()

                            col_top = box.column(align=True)
                            row = col_top.row(align=True)
                            row.operator("object.convert", text="Convert to Curve", icon="CURVE_DATA").target = "CURVE"

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


# -------------------------------------------------------
# Auto Mirror  #######-------------------------------------------------------
# Auto Mirror  #######-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        obj = context.active_object
        if obj:
            obj_type = obj.type

            if obj_type in {'MESH'}:

                if lt.display_mirrcut:
                    ###space2###
                    box = layout.box()
                    row = box.row()
                    row.prop(lt, "display_mirrcut", text="", icon='TRIA_DOWN')

                else:
                    box = layout.box()
                    row = box.row()
                    row.prop(lt, "display_mirrcut", text="", icon='TRIA_RIGHT')

                row.label("MirrorCut...")
                row.operator("view3d.display_modifiers_viewport_off", "", icon='VISIBLE_IPO_OFF')
                row.operator("view3d.display_modifiers_viewport_on", "", icon='RESTRICT_VIEW_OFF')
                row.operator("object.automirror", text="", icon="MOD_WIREFRAME")

                ###space1###
                if lt.display_mirrcut:
                    col = layout.column(align=True)
                    ###space2###
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.prop(context.scene, "AutoMirror_orientation", text="")
                    row.prop(context.scene, "AutoMirror_axis", text="")

                    row = col_top.row(align=True)
                    row.prop(context.scene, "AutoMirror_threshold", text="Threshold")

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.prop(context.scene, "AutoMirror_toggle_edit", text="Toggle edit")
                    row = col_top.row(align=True)
                    row.prop(context.scene, "AutoMirror_cut", text="Cut+Mirror")
                    if bpy.context.scene.AutoMirror_cut:
                        row.prop(context.scene, "AutoMirror_use_clip", text="Use Clip")
                        row = col_top.row(align=True)
                        row.prop(context.scene, "AutoMirror_show_on_cage", text="Editable")
                        row.prop(context.scene, "AutoMirror_apply_mirror", text="Apply")

                    else:
                        row.label(icon="ERROR", text="No mesh selected")


# ------------------------------------------------------------
# Curve Tools  ######------------------------------------------------------------
# Curve Tools  ######------------------------------------------------------------
# ------------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)

        if context.mode == 'OBJECT':
            obj = context.active_object
            if obj:
                obj_type = obj.type

                if obj_type in {'CURVE'}:

                    ###space1###
                    if lt.display_curveloft:
                        ###space2###
                        box = layout.box()
                        row = box.row()
                        row.prop(lt, "display_curveloft", text="", icon='TRIA_DOWN')

                    else:
                        ###space2###
                        box = layout.box()
                        row = box.row()
                        row.prop(lt, "display_curveloft", text="", icon='TRIA_RIGHT')

                    row.label("CurveT2...")
                    row.operator("curvetools2.operatororigintospline0start", text="", icon="PARTICLE_TIP")
                    row.operator("curve.switch_direction_obm", text="", icon="ARROW_LEFTRIGHT")

                    ###space1###
                    if lt.display_curveloft:
                        ###space2###

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
                        row.alignment = "CENTER"
                        row.label("", icon="INFO")  # ("...Curve Info...", icon ="")

                        row = col_top.row(align=True)
                        row.operator("curvetools2.operatorcurveinfo", text="Curve")
                        row.operator("curvetools2.operatorsplinesinfo", text="Splines")
                        row.operator("curvetools2.operatorsegmentsinfo", text="Segments")

                        # --------------------------

                        col_top = box.column(align=True)
                        col_top = box.column(align=True)
                        col_top = box.column(align=True)

                        row = col_top.row(align=True)
                        row.operator("curvetools2.operatorselectioninfo", text="Selection Info:")
                        row.prop(context.scene.curvetools, "NrSelectedObjects", text="")

                        row = col_top.row(align=True)
                        row.operator("curvetools2.operatorcurvelength", text="Calc Length")
                        row.prop(context.scene.curvetools, "CurveLength", text="")

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
                        row.operator("curvetools2.operatorintersectcurves", text="Intersect Curves")
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
                        row.prop(context.scene.curvetools, "SplineJoinStartEnd", text="Only at start & end")

                        row = col_top.row(align=0.5)
                        row.prop(context.scene.curvetools, "SplineJoinMode", text="Join")

                        # --------------------------

                        col = layout.column(align=True)
                        box = col.column(align=True).box().column()
                        col_top = box.column(align=True)

                        row = col_top.row(align=True)
                        row.operator("curvetools2.operatorsplinesremovezerosegment", text="del 0-segments")
                        row.operator("curvetools2.operatorsplinesremoveshort", text="del short splines")

                        row = col_top.row(align=True)
                        row.prop(context.scene.curvetools, "SplineRemoveLength", text="Threshold remove")


# -------------------------------------------------------
# Modifier  ############-------------------------------------------------------
# Modifier  ############-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)

        if lt.display_modif:
            ###space2###
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_modif", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_modif", text="", icon='TRIA_RIGHT')

        row.label("Modifier...")

        if context.mode == 'OBJECT':
            row.operator_menu_enum("object.modifier_add", "type", text="", icon="MODIFIER")
            row.operator("view3d.display_modifiers_delete", "", icon='X')
            row.operator("view3d.display_modifiers_apply", "", icon='FILE_TICK')

        if context.mode == 'EDIT_MESH':
            row.operator_menu_enum("object.modifier_add", "type", text="", icon="MODIFIER")
            row.operator("view3d.display_modifiers_delete", "", icon='X')
            row.operator("view3d.display_modifiers_apply_edm", "", icon='FILE_TICK')

        ###space1###
        if lt.display_modif:
            ###space2###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)

            row.label("SubSurf Levels")

            row = col_top.row(align=True)
            row.operator("view3d.modifiers_subsurf_level_0")
            row.operator("view3d.modifiers_subsurf_level_1")
            row.operator("view3d.modifiers_subsurf_level_2")
            row.operator("view3d.modifiers_subsurf_level_3")
            row.operator("view3d.modifiers_subsurf_level_4")
            row.operator("view3d.modifiers_subsurf_level_5")
            row.operator("view3d.modifiers_subsurf_level_6")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.label("Mirror Modifier / all enabled")

            row = col_top.row(align=True)
            row.operator("view3d.fullmirror", text="X-Clip")
            row.operator("view3d.fullmirrory", text="Y-Clip")
            row.operator("view3d.fullmirrorz", text="Z-Clip")

            ###space2###
            if context.mode == 'OBJECT':
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.label("Move over the Modifier Stack")

                row = col_top.row(align=True)
                row.operator("view3d.display_modifiers_expand", icon='DISCLOSURE_TRI_DOWN_VEC')
                row.operator("view3d.display_modifiers_collapse", icon='DISCLOSURE_TRI_RIGHT_VEC')

            ###space2###
            if context.mode == 'EDIT_MESH':
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("view3d.display_modifiers_viewport_on", icon='RESTRICT_VIEW_OFF')
                row.operator("view3d.display_modifiers_edit_on", icon='EDITMODE_HLT')
                row.operator("view3d.display_modifiers_cage_on", icon='OUTLINER_OB_MESH')

                row = col_top.row(align=True)
                row.operator("view3d.display_modifiers_viewport_off", icon='VISIBLE_IPO_OFF')
                row.operator("view3d.display_modifiers_edit_off", icon='SNAP_VERTEX')
                row.operator("view3d.display_modifiers_cage_off", icon='OUTLINER_DATA_MESH')


# -------------------------------------------------------
# SnapShot Mesh  ############-------------------------------------------------------
# SnapShot Mesh  ############-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        if context.mode == 'OBJECT':
            obj = context.active_object
            if obj:
                obj_type = obj.type

                if obj_type in {'MESH'}:

                    ###space1###
                    if lt.display_snapshot:
                        ###space2###
                        box = layout.box()
                        row = box.row()
                        row.prop(lt, "display_snapshot", text="", icon='TRIA_DOWN')
                    else:
                        box = layout.box()
                        row = box.row()
                        row.prop(lt, "display_snapshot", text="", icon='TRIA_RIGHT')

                    row.label("SnapShot...")
                    row.operator("vtools.capturesnapshot", icon='ZOOMIN', text="")
                    row.operator("vtools.deletesnapshot", icon='ZOOMOUT', text="")

                    ###space1###
                    if lt.display_snapshot:
                        ###space2###
                        col = layout.column(align=True)
                        box = col.column(align=True).box().column()
                        col_top = box.column(align=True)

                        row = col_top.row(align=True)
                        row.template_list('UI_UL_list', "snapShotMesh_ID", obj, "snapShotMeshes", obj, "snapShotMesh_ID_index", rows=2)

                        col = layout.column(align=True)
                        box = col.column(align=True).box().column()
                        col_top = box.column(align=True)

                        row = col_top.row(align=True)
                        row.operator("vtools.recalculatesnapshotfromchildren", icon='BORDERMOVE', text="Recalculate")
                        row.operator("vtools.usesnapshot", icon='OUTLINER_OB_MESH', text="Set Geometry")

                        col = layout.column(align=True)
                        box = col.column(align=True).box().column()
                        col_top = box.column(align=True)

                        row = col_top.row(align=True)
                        row.operator("vtools.deleteallsnapshot", icon='X', text="Del. All")
                        row.operator("vtools.deleteunusedsnapshotlist", icon='CANCEL', text="Del. Unused")

                        row = col_top.row(align=True)
                        row.prop(context.scene, "mod_list", text="")
                        row.operator("ba.delete_data_obs", "DelOrphan", icon="PANEL_CLOSE")


# -------------------------------------------------------
# SGrouper  ############-------------------------------------------------------
# SGrouper  ############-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        if context.mode == 'OBJECT':

            ###space1###
            if lt.display_sgrouper:
                ###space2###
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_sgrouper", text="", icon='TRIA_DOWN')
            else:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_sgrouper", text="", icon='TRIA_RIGHT')

            row.label("SGrp...")

            op = row.operator("super_grouper.change_selected_objects", text="", emboss=False, icon='WIRE')
            op.sg_objects_changer = 'WIRE_SHADE'

            op = row.operator("super_grouper.change_selected_objects", text="", emboss=False, icon='MATERIAL')
            op.sg_objects_changer = 'MATERIAL_SHADE'

            row.operator("view3d.display_wire_off", "", icon='MESH_PLANE')
            row.operator("view3d.display_wire_on", "", icon='MESH_GRID')

            ###space1###
            if lt.display_sgrouper:
                ###space2###
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator('sjoin.join', "Smart Join")
                row.operator('sjoin.separate', "Separate Join")
                row.operator('sjoin.join_add', "Add 2 Smart")

                row = col_top.row(align=True)
                row.operator('sjoin.expand', "Expand")
                row.operator('sjoin.collapse', "Collapse")
                row.operator('sjoin.update_rec', "Update")

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)

                if context.scene.name.endswith(SCENE_SGR) is False:
                    sg_settings = scene.sg_settings

                    row.operator("super_grouper.super_group_add", icon='ZOOMIN', text="")
                    row.operator("super_grouper.super_group_remove", icon='ZOOMOUT', text="")

                    row.label()
                    op = row.operator("super_grouper.change_selected_objects", text="", emboss=False, icon='BBOX')
                    op.sg_objects_changer = 'BOUND_SHADE'

                    row.label()
                    op = row.operator("super_grouper.super_group_move", icon='TRIA_UP', text="")
                    op.do_move = 'UP'

                    op = row.operator("super_grouper.super_group_move", icon='TRIA_DOWN', text="")
                    op.do_move = 'DOWN'

                    #op = row.operator("super_grouper.change_selected_objects", text="", emboss=False, icon='WIRE')
                    #op.sg_objects_changer = 'WIRE_SHADE'

                    #op = row.operator("super_grouper.change_selected_objects", text="", emboss=False, icon='MATERIAL')
                    #op.sg_objects_changer = 'MATERIAL_SHADE'

                    #op = row.operator("super_grouper.change_selected_objects", text="", emboss=False, icon='MESH_GRID')
                    #op.sg_objects_changer = 'SHOW_WIRE'

                    #op = row.operator("super_grouper.change_selected_objects", text="", emboss=False, icon='MESH_PLANE')
                    #op.sg_objects_changer = 'HIDE_WIRE'

                    row = col_top.row()
                    row.template_list("SG_named_super_groups", "", scene, "super_groups", scene, "super_groups_index")

                    row = col_top.row(1)
                    row.operator("super_grouper.add_to_group", text="Add")
                    row.operator("super_grouper.super_remove_from_group", text="Remove")
                    row.operator("super_grouper.clean_object_ids", text="Clean")

                    #layout.label(text="Selection Settings:")
                    row = col_top.row()
                    row.prop(sg_settings, "select_all_layers", text='L')
                    row.prop(sg_settings, "unlock_obj", text='L')
                    row.prop(sg_settings, "unhide_obj", text='H')


# -------------------------------------------------------
# Visual  #######-------------------------------------------------------
# Visual  #######-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        if lt.display_shading:
            ###space2###
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_RIGHT')

        row.label("Visual...")
        row.prop(context.space_data.fx_settings, "use_ssao", text="", icon='GROUP')
        row.operator("object.shade_smooth", text="", icon="SOLID")
        row.operator("object.shade_flat", text="", icon="MESH_CIRCLE")
        row.operator("object.wire_all", text="", icon='WIRE')

        ###space1###
        if lt.display_shading:
            ###space2###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("wm.context_toggle", text="Xray", icon='META_CUBE').data_path = "object.show_x_ray"
            row.menu("htk_modifly", text="Flymode", icon='MOD_SOFT')

            col_top = box.column(align=True)
            view = context.space_data
            obj = context.object

            row = col_top.row(align=True)
            row.prop(view, "show_backface_culling", text="BF Culling")
            row.prop(view, "use_matcap")
            if view.use_matcap:
                row = col_top.row(align=True)
                row.template_icon_view(view, "matcap_icon")

            col_top = box.column(align=True)
            col_top = box.column(align=True)
            row = col_top.row(align=True)

            row = col_top.row(align=True)
            row.operator("wm.context_toggle", text="Bounds on/off", icon='BBOX').data_path = "object.show_bounds"
            scene = context.scene
            row.prop(context.object, "draw_bounds_type", text="")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("view3d.display_double_sided_on", "DSided On", icon='OUTLINER_OB_MESH')
            row.operator("view3d.display_double_sided_off", "DSided Off", icon='MESH_DATA')


# -------------------------------------------------------
# Multi Edit  #######-------------------------------------------------------
# Multi Edit  #######-------------------------------------------------------
# -------------------------------------------------------

        ###space###
        if lt.display_multiedit:
            box = layout.box()
            row = box.row(True)
            row.prop(lt, "display_multiedit", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row(True)
            row.prop(lt, "display_multiedit", text="", icon='TRIA_RIGHT')

        op = row.operator("object.editmode_toggle", text="Edit Toggle", icon="EDITMODE_HLT")

        if lt.display_multiedit:
            sce = bpy.context.scene
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("objects.multiedit_enter_operator")
            row = col_top.row(align=True)
            row.operator("objects.multiedit_exit_operator")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.prop(sce, "Preserve_Location_Rotation_Scale", "Keep G/R/S & Pivot")


# -------------------------------------------------------
# Expand  ######------------------------------------------------------------
# Expand  ######------------------------------------------------------------
# -------------------------------------------------------

        ###space###
        if lt.display_expand:
            row.prop(lt, "display_expand", text="", icon='PINNED')
        else:
            row.prop(lt, "display_expand", text="", icon='UNPINNED')

        #split.operator("", text="", icon="")

        if lt.display_expand:
            col = layout.column(align=True)

    # -------------------------------------------------------
    # Add Geometry   #######-------------------------------------------------------
    # Add Geometry   #######-------------------------------------------------------
    # -------------------------------------------------------

            ###space###
            split = col.split()  # percentage=0.15)
            if lt.display_geom:
                split.prop(lt, "display_geom", text="...Add...", icon='DOWNARROW_HLT')

            else:
                split.prop(lt, "display_geom", text="...Geometry...", icon='RIGHTARROW')

            #row.menu("INFO_MT_add",text="", icon="OBJECT_DATAMODE")

            if lt.display_geom:

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

            #col = layout.column(align=True)
            split = col.split()  # percentage=0.15)

            if lt.display_anim:
                split.prop(lt, "display_anim", text="...Animation...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_anim", text="...Animation...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_anim:

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

        # -------------------------------------------------------
        # Render  #######-------------------------------------------------------
        # Render  #######-------------------------------------------------------
        # -------------------------------------------------------

            #col = layout.column(align=True)
            split = col.split()  # percentage=0.15)

            if lt.display_render:
                split.prop(lt, "display_render", text="...Render...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_render", text="...Render...", icon='RIGHTARROW')

            #spread_op = split.operator("", text="", icon="")

            if lt.display_render:

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

    # -------------------------------------------------------
    # Array Tools  #######-------------------------------------------------------
    # Array Tools  #######-------------------------------------------------------
    # -------------------------------------------------------

            ###space###
            split = col.split()  # percentage=0.15)

            if lt.display_array:
                split.prop(lt, "display_array", text="...ArrayTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_array", text="...ArrayTools...", icon='RIGHTARROW')

            #split.operator("",text="", icon = "")

            if lt.display_array:
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

                ###space###
                split = col.split()  # percentage=0.15)

                if lt.display_arraycurve:
                    split.prop(lt, "display_arraycurve", text="Curve", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_arraycurve", text="Curve", icon='DISCLOSURE_TRI_RIGHT_VEC')

                if lt.display_arraycurve:
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

                ###space###
                split = col.split()  # percentage=0.15)

                if lt.display_arraycircle:
                    split.prop(lt, "display_arraycircle", text="Empty", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_arraycircle", text="Empty", icon='DISCLOSURE_TRI_RIGHT_VEC')

                # row.label()

                if lt.display_arraycircle:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("objects.circle_array_operator1", text="1/4-90°", icon="MOD_ARRAY")
                    row.operator("objects.circle_array_operator2", text="1/6-60°", icon="MOD_ARRAY")

                    row = col_top.row(align=True)
                    row.operator("objects.circle_array_operator3", text="1/8-45°", icon="MOD_ARRAY")
                    row.operator("objects.circle_array_operator4", text="1/12-30°", icon="MOD_ARRAY")

    # -------------------------------------------------------
    # Copy Tools  #######-------------------------------------------------------
    # Copy Tools  #######-------------------------------------------------------
    # -------------------------------------------------------

            ###space###
            split = col.split()  # percentage=0.15)

            if lt.display_copy:
                split.prop(lt, "display_copy", text="...CopyShop...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_copy", text="...CopyShop...", icon='RIGHTARROW')

            #split.operator("", text="", icon="")

            if lt.display_copy:
                operator_context_default = layout.operator_context
                wm = bpy.context.window_manager
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                layout.operator_context = 'INVOKE_REGION_WIN'

                row = col_top.row(align=True)
                row.label("Make Links (CTRL+L)", icon="LINKED")

                row = col_top.row(align=True)
                row.operator_enum("object.make_links_data", "type")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("object.join_uvs")

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

    # -------------------------------------------------------
    # Relations  #######-------------------------------------------------------
    # Relations  #######-------------------------------------------------------
    # -------------------------------------------------------

            ###space###
            split = col.split()  # percentage=0.15)

            if lt.display_relations:
                split.prop(lt, "display_relations", text="...Relations...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_relations", text="...Relations...", icon='RIGHTARROW')

            #split.operator("", text="", icon="")

            if lt.display_relations:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.menu("VIEW3D_MT_make_single_user", text="Make Single User")

                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("object.visual_transform_apply", icon="NDOF_DOM")

                row = col_top.row(align=True)
                row.operator("object.duplicates_make_real", icon="MOD_PARTICLES")
                row.operator("help.operator4", text="", icon="INFO")

                row = col_top.row(align=True)
                row.operator("object.set_instance", text="Set as Instance", icon="LINK_AREA")

    # Group  ######-------------------------------------
    # Group  ######-------------------------------------

                split = col.split(percentage=0.15, align=True)

                if lt.display_relagroup:
                    split.prop(lt, "display_relagroup", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_relagroup", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

                spread_op = split.operator("group.create", text="Group", icon="STICKY_UVS_LOC")

                if lt.display_relagroup:
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

                if lt.display_relaparent:
                    split.prop(lt, "display_relaparent", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_relaparent", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

                spread_op = split.operator("object.parent_set", text="Parent", icon="CONSTRAINT")

                if lt.display_relaparent:
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

                if lt.display_relaconstraint:
                    split.prop(lt, "display_relaconstraint", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_relaconstraint", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

                spread_op = split.operator_menu_enum("object.constraint_add", "type", text="  Constraint", icon="CONSTRAINT_DATA")

                if lt.display_relaconstraint:
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

    # -------------------------------------------------------
    # Material Tools  #######-------------------------------------------------------
    # Material Tools  #######-------------------------------------------------------
    # -------------------------------------------------------

            ###space###
            split = col.split()  # percentage=0.15)

            if lt.display_material:
                split.prop(lt, "display_material", text="...MatTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_material", text="...MatTools...", icon='RIGHTARROW')

            #split.operator("", text="", icon="")

            if lt.display_material:

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
                row.operator("meta.newmaterial", text="ID Obj.Color", icon='ZOOMIN')
                row.prop(obj, "color", text="")

    # Material Option  ######-------------------------------------------------
    # Material Option  ######-------------------------------------------------

                split = col.split()  # percentage=0.15)

                if lt.display_matoption:
                    split.prop(lt, "display_matoption", text="Mat Options", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_matoption", text="Mat Options", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("",text="", icon = "")

                if lt.display_matoption:
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

                if lt.display_matclean:
                    split.prop(lt, "display_matclean", text="Remove Mat", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_matclean", text="Remove Mat", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("",text="", icon = "")

                if lt.display_matclean:

                    box = col.column(align=True).box().column()

                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("object.clean_images")

                    row = col_top.row(align=True)
                    row.operator("object.clean_materials")

                    row = col_top.row(align=True)
                    row.operator("view3d.material_remove", text="Remove until 1 Slots", icon='CANCEL')

                    row = col_top.row(align=True)
                    row.operator("material.remove", text="Remove all Slot Mat", icon='CANCEL')

    # Node Materials  ######-------------------------------------------------
    # Node Materials  ######-------------------------------------------------

                split = col.split()  # percentage=0.15)

                if lt.display_node:
                    split.prop(lt, "display_node", text="Node Presets", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_node", text="Node Presets", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("",text="", icon = "")

                if lt.display_node:
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

                if lt.display_matrandom:
                    split.prop(lt, "display_matrandom", text="Random Face", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_matrandom", text="Random Face", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("",text="", icon = "")

                if lt.display_matrandom:
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

                if lt.display_matwireset:
                    split.prop(lt, "display_matwireset", text="Mat Wire Render", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_matwireset", text="Mat Wire Render", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("",text="", icon = "")

                if lt.display_matwireset:
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

    # -------------------------------------------------------
    # UV Mapping  #######-------------------------------------------------------
    # UV Mapping  #######-------------------------------------------------------
    # -------------------------------------------------------

            split = col.split()  # percentage=0.15)

            if lt.display_unwrap:
                split.prop(lt, "display_unwrap", text="...UvTools ...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_unwrap", text="...UvTools....", icon='RIGHTARROW')

            #split.operator("",text="", icon = "")

            if lt.display_unwrap:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("transform.translate", text="Move Texture Space").texture_space = True

                row = col_top.row(align=True)
                row.operator("uv.uv_equalize", text="UV Equalize")

    # UV Utility  ######-------------------------------------------------
    # UV Utility  ######-------------------------------------------------

                split = col.split()  # percentage=0.15)

                if lt.display_uvut:
                    split.prop(lt, "display_uvut", text="UV Utility", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_uvut", text="UV Utility", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("",text="", icon = "")

                if lt.display_uvut:
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

                if lt.display_uvsure:
                    split.prop(lt, "display_uvsure", text="SureUVW", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_uvsure", text="SureUVW", icon='DISCLOSURE_TRI_RIGHT_VEC')

                #split.operator("",text="", icon = "")

                if lt.display_uvsure:
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

    # -------------------------------------------------------
    # Delete & Clear  #######-------------------------------------------------------
    # Delete & Clear  #######-------------------------------------------------------
    # -------------------------------------------------------

            #col = layout.column(align=True)
            split = col.split()  # percentage=0.15)

            if lt.display_delete:
                split.prop(lt, "display_delete", text="...Delete...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_delete", text="...Delete...", icon='RIGHTARROW')

            #split.operator("", text="", icon="")

            if lt.display_delete:
                box = col.column(align=True).box().column()

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("meshlint.select", "Meshlint > Object Data")

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

    # -------------------------------------------------------
    # Grease Pencil  #######-------------------------------------------------------
    # Grease Pencil  #######-------------------------------------------------------
    # -------------------------------------------------------

            #col = layout.column(align=True)
            split = col.split()  # percentage=0.15)

            if lt.display_pencil:
                split.prop(lt, "display_pencil", text="...PencilTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_pencil", text="...PencilTools...", icon='RIGHTARROW')

            #split.operator("", text="", icon="")

            if lt.display_pencil:
                box = col.column(align=True).box().column()
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

        #####################################
        draw_A_history_tools(context, layout)
        #####################################


######################################################################################################################################################
########--------------#################
# Sculptmode  ##############################-------------------------------------------------------
# Sculptmode  ##############################-------------------------------------------------------
########--------------#################
######################################################################################################################################################

class VIEW3D_SculptMask(bpy.types.Panel):
    bl_category = "META"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_label = "MetaTool"

    @classmethod
    def poll(cls, context):
        return (context.sculpt_object)

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        box = col.column(align=True).box().column()
        col_top = box.column(align=True)

        row = col_top.column_flow(2)

        props = row.operator("paint.hide_show", text="BBox Hide", icon="BORDER_RECT")
        props.action = 'HIDE'
        props.area = 'INSIDE'

        props = row.operator("paint.hide_show", text="BBox Show", icon="BORDERMOVE")
        props.action = 'SHOW'
        props.area = 'INSIDE'

        props = row.operator("paint.mask_flood_fill", text="Fill Mask", icon="MATCAP_08")
        props.mode = 'VALUE'
        props.value = 1

        row.operator("paint.mask_flood_fill", text="Invert Mask", icon="FILE_REFRESH").mode = 'INVERT'

        row.operator("view3d.select_border", text="Box Mask", icon="IMAGE_ZDEPTH")

        props = row.operator("paint.hide_show", text="Hide Masked", icon="BRUSH_TEXMASK")
        props.area = 'MASKED'
        props.action = 'HIDE'

        props = row.operator("paint.hide_show", text="Show All", icon="SOLID")
        props.action = 'SHOW'
        props.area = 'ALL'

        props = row.operator("paint.mask_flood_fill", text="Clear Mask", icon="BRUSH_TEXFILL")
        props.mode = 'VALUE'
        props.value = 0

        #col = layout.column(align=True)
        #col.label(text="Box Masking:")
        #col.label(text="1. Fill > Box Hide")
        #col.label(text="2. Invert > Show All")

        #####################################
        draw_B_history_tools(context, layout)
        #####################################


######################################################################################################################################################
########----------------#################
# Vertex Paint  ##############################-------------------------------------------------------
# Vertex Paint  ##############################-------------------------------------------------------
########----------------#################
######################################################################################################################################################

class VIEW3D_VertexPaint(bpy.types.Panel):
    bl_category = "META"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    #bl_context = "vertexpaint"
    bl_label = "MetaTool"

    @classmethod
    def poll(cls, context):
        return (context.vertex_paint_object)

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        box = col.column(align=True).box().column()
        col_top = box.column(align=True)

        row = col_top.column(align=True)
        row.operator("paint.vertex_color_set", text="Set Color ")
        row.operator("paint.vertex_color_smooth", text="Smooth Color ")
        row.operator("mesh.connected_vertex_colors", text="Connected Vertex Colors")

        col = layout.column(align=True)
        box = col.column(align=True).box().column()
        col_top = box.column(align=True)

        row = col_top.column(align=True)
        row.operator("paint.vertex_color_dirt", text="Dirt Color ")
        row.operator("paint.worn_edges", text="Worn Edges")

        #### History ########################
        draw_B_history_tools(context, layout)
        #####################################


######################################################################################################################################################
########----------------#################
# Weight Paint  ##############################-------------------------------------------------------
# Weight Paint  ##############################-------------------------------------------------------
########----------------#################
######################################################################################################################################################

class VIEW3D_WeightPaint(bpy.types.Panel):
    bl_category = "META"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    #bl_context = "weightpaint"
    bl_label = "MetaTool"

    @classmethod
    def poll(cls, context):
        return (context.weight_paint_object)

    def draw(self, context):
        lt = context.window_manager.metawindow
        layout = self.layout

        col = layout.column(align=True)
        box = col.column(align=True).box().column()
        col_top = box.column(align=True)

        row = col_top.column(align=True)
        row.operator("mesh.weightlifterweight", text="Weight Lifter")
        row.operator("mesh.slope2vgroup", text="Slope 2 VertGroup")
        row.operator("mesh.height2vgroup", text="Height 2 VertGroup")
        row.operator("mesh.visiblevertices", text="Visible Vertices in Cam View")
        row.operator("vp.convert_vertex_group_to_vertex_paint")

        col = layout.column(align=True)
        box = col.column(align=True).box().column()
        col_top = box.column(align=True)

        row = col_top.row(align=True)
        row.alignment = 'CENTER'
        row.scale_x = 1
        row.label("Set Weight only to:")

        box = col.column(align=True).box().column()
        col_top = box.column(align=True)
        row = col_top.row(align=True)
        row.label(text="> selected Vertex Group")

        row = col_top.row(align=True)
        row.operator("assignonly.selected", text="Set Weight")
        row.operator("del.unselected", text="Del All")
        row.operator("remall.vertex", text="Del Others")

        col_top = box.column(align=True)
        row = col_top.row(align=True)
        row.label(text="> all Vertex Groups")

        row = col_top.row(align=True)
        row.operator("all_assignonly.selected", text="Set Weight")
        row.operator("all_del.unselected", text="Del All")
        row.operator("all_remall.vertex", text="Del Others")

        #### History ########################
        draw_B_history_tools(context, layout)
        #####################################


######################################################################################################################################################
########------------#################
# Posemode  ##############################-------------------------------------------------------
# Posemode  ##############################-------------------------------------------------------
########------------#################
######################################################################################################################################################

class VIEW3D_PosePanel(bpy.types.Panel):
    bl_category = "META"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_label = "MetaTool"
    bl_context = "posemode"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'POSE'))

    def draw(self, context):
        layout = self.layout

        ob = context.active_object
        row = layout.row()
        row.label(text="", icon='OBJECT_DATA')
        row.prop(ob, "name", text="")

        if ob.type == 'ARMATURE' and ob.mode in {'EDIT', 'POSE'}:
            bone = context.active_bone
            if bone:
                row = layout.row()
                row.label(text="", icon='BONE_DATA')
                row.prop(bone, "name", text="")

        row.operator("wm.save_mainfile", text="", icon="FILE_TICK")
        row.operator("wm.save_as_mainfile", text="", icon="SAVE_AS")

    def draw(self, context):
        lt = context.window_manager.metawindow

        layout = self.layout

        col = layout.column(align=True)

# ------------------------------------------------------------
# Selection Pose  #######-------------------------------------------------------
# Selection Pose  #######-------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_poseselect:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_poseselect", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_poseselect", text="", icon='TRIA_RIGHT')

        row.label("Select...")
        row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")
        row.operator("view3d.select_border", text="", icon="BORDER_RECT")
        row.operator("armature.armature_layers", text="", icon="ARMATURE_DATA")
        row.operator("pose.bone_layers", text="", icon="BONE_DATA")

        if lt.display_poseselect:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator_menu_enum("pose.select_grouped", "type", text="Grouped...")
            row.operator("object.select_pattern", text="Pattern...")

            row = col_top.row(align=True)
            row.operator("pose.select_mirror", text="Flip Active")
            row.operator("pose.select_all", text="Inverse").action = 'INVERT'

            row = col_top.row(align=True)
            row.operator("pose.select_constraint_target", text="Constraint Target")
            row.operator("pose.select_linked", text="Linked")

            row = col_top.row(align=True)
            row.operator("pose.select_hierarchy", text="Parent").direction = 'PARENT'
            row.operator("pose.select_hierarchy", text="Child").direction = 'CHILD'

            row = col_top.row(align=True)
            props = row.operator("pose.select_hierarchy", text="Extend Parent")
            props.extend = True
            props.direction = 'PARENT'

            props = row.operator("pose.select_hierarchy", text="Extend Child")
            props.extend = True
            props.direction = 'CHILD'


# ------------------------------------------------------------
# Align Pose  ######------------------------------------------------------------
# Align Pose  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_alignpose:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_alignpose", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_alignpose", text="", icon='TRIA_RIGHT')

        row.label("Align...")
        row.operator("pose.quaternions_flip", "", icon="ARROW_LEFTRIGHT")

        if lt.display_alignpose:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("object.loops1", text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="MZ", icon='ARROW_LEFTRIGHT')


# ------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_orient:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orient", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orient", text="", icon='TRIA_RIGHT')

        sub = row.row(1)
        sub.scale_x = 7
        sub.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
        sub.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
        sub.operator("view3d.pivot_active", "", icon="ROTACTIVE")
        sub.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
        sub.operator("view3d.pivot_median", "", icon="ROTATECENTER")

        if lt.display_orient:

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Origin", icon="LAYER_ACTIVE")
            col_top = box.column(align=True)
            row = col_top.column_flow(2)
            row.operator("object.origin_set", text="to Cursor").type = 'ORIGIN_CURSOR'
            row.operator("object.origin_set", text="to Mass ").type = 'ORIGIN_CENTER_OF_MASS'
            row.operator("object.origin_set", text="to Geometry").type = 'ORIGIN_GEOMETRY'
            row.operator("object.origin_set", text="Geometry to").type = 'GEOMETRY_ORIGIN'
            ###space1###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Cursor", icon="FORCE_FORCE")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)
            row.operator("view3d.snap_cursor_to_grid", "to Grid")
            row.operator("view3d.snap_cursor_to_active", "to Active")
            row.operator("view3d.snap_cursor_to_center", "to Center")
            row.operator("view3d.snap_cursor_to_selected", "to Selected")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Selected", icon="RESTRICT_SELECT_OFF")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)
            row.operator("view3d.snap_selected_to_grid", "to Grid")
            row.operator("view3d.snap_selected_to_cursor", "to Offset").use_offset = True
            row.operator("mesh.snapcenteroffset", " to Center")
            row.operator("view3d.snap_selected_to_cursor", "to Cursor").use_offset = False


# ------------------------------------------------------------
# PoseTools  #######-------------------------------------------------------
# PoseTools  #######-------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_posebonetools:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_posebonetools", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_posebonetools", text="", icon='TRIA_RIGHT')

        row.label("Pose Tools...")
        row.operator("pose.copy", text="", icon='COPYDOWN')
        row.operator("pose.paste", text="", icon='PASTEDOWN').flipped = False
        row.operator("pose.paste", text="", icon='PASTEFLIPDOWN').flipped = True

        if lt.display_posebonetools:

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(True)
            row.alignment = 'CENTER'
            row.scale_x = 1.5
            row.menu("VIEW3D_MT_bone_options_toggle", text="Bone Settings", icon="PREFERENCES")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)

            row.operator("pose.push")
            row.operator("pose.relax")

            row = col_top.row(align=True)
            row.operator("pose.breakdown")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("pose.paste", text="Paste X-Flipped Pose").flipped = True

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("pose.propagate").mode = 'WHILE_HELD'

            row = col_top.row(align=True)
            row.operator("pose.propagate", text="Next Keyframe").mode = 'NEXT_KEY'
            row = col_top.row(align=True)
            row.operator("pose.propagate", text="Last Keyframe (Cyclic)").mode = 'LAST_KEY'

            row = col_top.row(align=True)
            row.operator("pose.propagate", text="On Selected Markers").mode = 'SELECTED_MARKERS'

# ------------------------------------------------------------
# Clear Pose  #######-------------------------------------------------------
# Clear Pose  #######-------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_poseclear:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_poseclear", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_poseclear", text="", icon='TRIA_RIGHT')

        row.label("Pose Clear...")
        row.operator("pose.transforms_clear", "", icon="PANEL_CLOSE")
        row.menu("VIEW3D_MT_pose_apply", text="", icon="FILE_TICK")

        if lt.display_poseclear:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)

            row.operator("pose.user_transforms_clear", text="Reset unkeyed")
            row = col_top.row(align=True)
            row.operator("pose.loc_clear", text="Location")
            row.operator("pose.rot_clear", text="Rotation")
            row.operator("pose.scale_clear", text="Scale")

# ------------------------------------------------------------
# Relations Pose  #######------------------------------------------------------------
# Relations Pose  #######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_poserelations:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_poserelations", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_poserelations", text="", icon='TRIA_RIGHT')

        row.label("Pose Relations...")
        op = row.menu("VIEW3D_MT_posecopypopup", "", icon="CONSTRAINT_BONE")

        if lt.display_poserelations:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.label("Inverse Kinematics")

            row = col_top.row(align=True)
            row.operator("pose.ik_add")
            row = col_top.row(align=True)
            row.operator("pose.ik_clear")

            row = col_top.row(align=True)
            arm = context.active_object.data
            row.prop(arm, "use_auto_ik")

            # ---------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.label("Constraints")
            row = col_top.row(align=True)
            row.operator("pose.constraint_add_with_targets", text="Add (With Targets)")
            row = col_top.row(align=True)
            row.operator("pose.constraints_copy", "Copy to Selected")

            row = col_top.row(align=True)
            row.operator("pose.constraints_clear")

            # ---------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.label("Parent")
            row = col_top.row(align=True)
            row.operator_enum("object.parent_set", "type")

            # ---------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.label("Clear Parent")
            row = col_top.row(align=True)
            row.operator_enum("object.parent_clear", "type")


# ------------------------------------------------------------
# Pose Library  ######------------------------------------------------------------
# Pose Library  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_poselib:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_poselib", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_poselib", text="", icon='TRIA_RIGHT')

        row.label("Pose Library...")
        row.operator("poselib.pose_add", text="", icon="PLUS")

        if lt.display_poselib:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("poselib.pose_add", text="Add Pose...")
            row = col_top.row(align=True)
            row.operator("poselib.pose_rename", text="Rename Pose...")

            row = col_top.row(align=True)
            row.operator("poselib.browse_interactive", text="Browse Poses...")
            row = col_top.row(align=True)
            row.operator("poselib.pose_remove", text="Remove Pose...")

# ------------------------------------------------------------
# Autoname  #######------------------------------------------------------------
# Autoname  #######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_posename:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_posename", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_posename", text="", icon='TRIA_RIGHT')

        row.label("Pose Autoname...")
        #row.operator("pose.transforms_clear","", icon="PANEL_CLOSE")

        if lt.display_posename:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator_context = 'EXEC_AREA'
            row.operator("pose.autoside_names", text="Left/Right").axis = 'XAXIS'
            row.operator("pose.autoside_names", text="Front/Back").axis = 'YAXIS'
            row = col_top.row(align=True)
            row.operator("pose.autoside_names", text="Top/Bottom").axis = 'ZAXIS'
            row.operator("pose.flip_names", text="Flip Name")

# -------------------------------------------------------
# Animation  #######-------------------------------------------------------
# Animation  #######-------------------------------------------------------
# -------------------------------------------------------

        lt = context.window_manager.metawindow
        view = context.space_data
        obj = bpy.context.scene.objects.active
        scene = context.scene
        toolsettings = context.tool_settings
        screen = context.screen
        layout = self.layout
        self.scn = context.scene

        if lt.display_pose_anim:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_pose_anim", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_pose_anim", text="", icon='TRIA_RIGHT')

        row.label("Pose Animation...")
        #row.operator("pose.transforms_clear","", icon="PANEL_CLOSE")

        if lt.display_pose_anim:
            col = layout.column(align=True)
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
            row.operator("pose.paths_calculate", text="Calculate Motion Path", icon="ANIM_DATA")
            row = col_top.row(align=True)
            row.operator("pose.paths_clear", text="Clear Path Catch", icon="PANEL_CLOSE")

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("nla.bake", text="Bake new Action", icon="ACTION_TWEAK")

# ------------------------------------------------------------
# Bone Groups  #######------------------------------------------------------------
# Bone Groups  #######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_poseparent:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_poseparent", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_poseparent", text="", icon='TRIA_RIGHT')

        row.label("Bone Groups...")
        op = row.operator("pose.group_assign", "", icon="GROUP_BONE")

        if lt.display_poseparent:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)

            row.operator_context = 'EXEC_AREA'
            row.operator("pose.group_assign", text="Assign to New Group").type = 0

            pose = context.active_object.pose
            if pose.bone_groups:
                active_group = pose.bone_groups.active_index + 1
                row = col_top.row(align=True)
                row.operator("pose.group_assign", text="Assign to Group").type = active_group

                row = col_top.row(align=True)
                layout.operator_context = 'INVOKE_AREA'
                row.operator("pose.group_unassign")

                row = col_top.row(align=True)
                row.operator("pose.group_remove")


############################################################################################
        box = layout.box()
        row = box.row(True)
        row.operator("object.posemode_toggle", "Object Toggle", icon="OBJECT_DATAMODE")
        row.operator("object.editmode_toggle", text="Edit Toggle", icon="BONE_DATA")

        #### History ########################
        draw_B_history_tools(context, layout)
        #####################################


######################################################################################################################################################
########-----------------#################
# Editmode Mesh  ##############################-------------------------------------------------------
# Editmode Mesh  ##############################-------------------------------------------------------
########-----------------#################
######################################################################################################################################################

class VIEW3D_EditMode(bpy.types.Panel):
    bl_category = "META"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_label = "MetaTool"
    bl_context = "mesh_edit"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_MESH'))

    def draw(self, context):
        layout = self.layout
        obj = context.object

        if obj != None:
            row = layout.row()
            row.label(text="Active object is: ", icon='OBJECT_DATA')
            row.label(obj.name, icon='EDITMODE_HLT')

    def draw(self, context):
        lt = context.window_manager.metawindow

        layout = self.layout
        obj = context.object
        mesh = context.active_object.data

        col = layout.column(align=True)
        box = col.column(align=True).box().column()
        col_top = box.column(align=True)

        row = col_top.row(align=True)
        row.alignment = 'CENTER'
        sub = row.row(1)
        sub.scale_x = 1.7
        sub.operator("mesh.primitive_plane_add", icon='MESH_PLANE', text="")
        sub.operator("mesh.primitive_cube_add", icon='MESH_CUBE', text="")
        sub.operator("mesh.primitive_circle_add", icon='MESH_CIRCLE', text="")
        sub.operator("mesh.primitive_uv_sphere_add", icon='MESH_UVSPHERE', text="")
        sub.operator("mesh.primitive_ico_sphere_add", icon='MESH_ICOSPHERE', text="")

        row = col_top.row(align=True)
        row.alignment = 'CENTER'
        sub = row.row(1)
        sub.scale_x = 1.7
        sub.operator("mesh.primitive_cylinder_add", icon='MESH_CYLINDER', text="")
        sub.operator("mesh.primitive_torus_add", icon='MESH_TORUS', text="")
        sub.operator("mesh.primitive_cone_add", icon='MESH_CONE', text="")
        sub.operator("mesh.primitive_grid_add", icon='MESH_GRID', text="")
        sub.operator("mesh.primitive_monkey_add", icon='MESH_MONKEY', text="")

        row = col_top.row(1)
        row.alignment = 'CENTER'
        row.scale_x = 1
        row.operator("mesh.singlevertex", text="", icon="STICKY_UVS_DISABLE")
        row.operator("mesh.singleplane_x", text="X")
        row.operator("mesh.singleplane_y", text="Y")
        row.operator("mesh.singleplane_z", text="Z")
        row.operator("object.easy_lattice", text="", icon="OUTLINER_DATA_LATTICE")
        row.operator("mesh.add_curvebased_tube", text="", icon="CURVE_DATA")

        col_top = box.column(align=True)


# ------------------------------------------------------------
# Selection  ######------------------------------------------------------------
# Selection  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_selectionedm:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selectionedm", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selectionedm", text="", icon='TRIA_RIGHT')

        row.label("Select...")
        row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")
        row.operator("view3d.select_border", text="", icon="BORDER_RECT")
        row.menu("VIEW3D_MT_edit_mesh_showhide", "", icon="VISIBLE_IPO_ON")
        row.menu("VIEW3D_MT_edit_multi", text="", icon="UV_SYNC_SELECT")

        if lt.display_selectionedm:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            sub = row.row()
            sub.scale_x = 0.3
            sub.operator("mesh.select_more", text="+")
            sub.operator("mesh.select_all", text="All")
            sub.operator("mesh.select_less", text="-")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("mesh.loop_multi_select", text="Ring").ring = True
            row.operator("mesh.loop_multi_select", text="Loop").ring = False

            row = col_top.row(align=True)
            row.operator("mesh.select_nth", "Checker")
            row.operator("mesh.select_all", text="Inverse").action = 'INVERT'

            row = col_top.row(align=True)
            row.operator("mesh.select_linked", text="Linked")
            row.operator("mesh.faces_select_linked_flat", text="Linked Faces")

            row = col_top.row(align=True)
            row.operator("mesh.select_face_by_sides", text="nSide")
            row.operator("mesh.select_similar", text="Similar")

            row = col_top.row(align=True)
            row.operator("mesh.edges_select_sharp", text="Sharp")
            row.operator("mesh.select_loose", text="Loose")

            row = col_top.row(align=True)
            row.operator("mesh.select_interior_faces", text="Interior Faces")
            if context.scene.tool_settings.mesh_select_mode[2] is False:
                row.operator("mesh.select_non_manifold", text="Non Manifold")


# ------------------------------------------------------------
# Align Location ######------------------------------------------------------------
# Align Location ######------------------------------------------------------------
# ------------------------------------------------------------

        #col = layout.column(align=True)

        if lt.display_location:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_location", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_location", text="", icon='TRIA_RIGHT')

        row.label("Align...")
        row.operator("mesh.vertex_align", text="", icon="ALIGN")
        row.operator("mesh.vertex_distribute", text="", icon="PARTICLE_POINT")
        row.operator("mesh.vertices_smooth", "", icon="SPHERECURVE")

        if lt.display_location:
            ###space2###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.loops1", text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="MZ", icon='ARROW_LEFTRIGHT')

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("mesh.face_align_x", "X", icon='COLOR_RED')
            row.operator("mesh.face_align_y", "Y", icon='COLOR_GREEN')
            row.operator("mesh.face_align_z", "Z", icon='COLOR_BLUE')

            row = col_top.row(align=True)
            row.operator("mesh.face_align_xy", "Xy", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy", icon='TRIA_UP_BAR')
            row.operator("mesh.face_align_xz", "Zx", icon='TRIA_LEFT_BAR')

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("fan.move_faces_along_normals_operator", "Move Along Normals", icon="SNAP_NORMAL")

    # -------------------------------------------------------
    # 1D Align Tool  ######-----------------------------------------
    # 1D Align Tool  ######-----------------------------------------
    # -------------------------------------------------------

            if lt.display_1d:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_1d", text="...1d Script...", icon='DOWNARROW_HLT')
            else:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_1d", text="...1d Script...", icon='RIGHTARROW')

            if lt.display_1d:
                ###space2###

                col = layout.column(align=True)

                split = col.split()

                if lt.display_align:
                    split.prop(lt, "display_align", text="Align Edges", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_align", text="Align Edges", icon='RIGHTARROW_THIN')

                box = col.column(align=True)
                if lt.display_align and context.mode == 'EDIT_MESH':
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

                if lt.display_align and context.mode == 'OBJECT':
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
                if lt.display_3dmatch:
                    split.prop(lt, "display_3dmatch", text="3D Match", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_3dmatch", text="3D Match", icon='RIGHTARROW_THIN')

                if lt.display_3dmatch:
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
                if lt.display_offset:
                    split.prop(lt, "display_offset", text="SideShift", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_offset", text="SideShift", icon='RIGHTARROW_THIN')

                if lt.display_offset:
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
                if lt.disp_cp:
                    split.prop(lt, "disp_cp", text="Polycross", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "disp_cp", text="Polycross", icon='RIGHTARROW_THIN')

                if lt.disp_cp:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    split = row.split()
                    if lt.disp_cp_project:
                        split.prop(lt, "disp_cp_project", text="Project active", icon='DISCLOSURE_TRI_DOWN_VEC')
                    else:
                        split.prop(lt, "disp_cp_project", text="Project active", icon='RIGHTARROW_THIN')

                    if lt.disp_cp_project:
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
                    if lt.disp_cp_filter:
                        split.prop(lt, "disp_cp_filter", text="Selection Filter", icon='DISCLOSURE_TRI_DOWN_VEC')
                    else:
                        split.prop(lt, "disp_cp_filter", text="Selection Filter", icon='RIGHTARROW_THIN')

                    if lt.disp_cp_filter:
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
                if lt.disp_matExtrude:
                    split.prop(lt, "disp_matExtrude", text="AutoExtrude", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "disp_matExtrude", text="AutoExtrude", icon='RIGHTARROW_THIN')

                if lt.disp_matExtrude:
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.get_mat4extrude", text='Get Mats')
                    row = col_top.row(align=True)
                    row.operator("mesh.mat_extrude", text='Template Extrude')

                # Spread Loop  ######-----------------------------------------
                split = col.split(percentage=0.15, align=True)
                if lt.display:
                    split.prop(lt, "display", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display", text="", icon='RIGHTARROW_THIN')

                spread_op = split.operator("mesh.spread_operator", text='Spread Loop')

                if lt.display:
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


# ------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_orientedm:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orientedm", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orientedm", text="", icon='TRIA_RIGHT')

        # row.label("Align...")
        sub = row.row(1)
        sub.scale_x = 5
        sub.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
        sub.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
        sub.operator("view3d.pivot_active", "", icon="ROTACTIVE")
        sub.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
        sub.operator("view3d.pivot_median", "", icon="ROTATECENTER")

        if lt.display_orientedm:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.scale_y = 1.2
            row.operator("origin.selected_edm", "Origin to Select", icon="EDITMODE_HLT")
            row.operator("origin.selected_obm", "Origin to Select", icon="OBJECT_DATAMODE")

            row = col_top.row(align=True)
            if lt.display_bboxback:
                row.scale_y = 1.2
                row.prop(lt, "display_bboxback", text="Back", icon='TRIA_DOWN')

            else:
                row.scale_y = 1
                row.prop(lt, "display_bboxback", text="Back", icon='TRIA_RIGHT')

            ###space1###
            if lt.display_bboxback:
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                # Top
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubeback_cornertop_minus_xy", "", icon="LAYER_ACTIVE")  # "Back- Left -Top")
                row.operator("object.cubeback_edgetop_minus_y", "", icon="LAYER_ACTIVE")  # "Back - Top")
                row.operator("object.cubeback_cornertop_plus_xy", "", icon="LAYER_ACTIVE")  # "Back- Right -Top ")

                # Middle
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55
                row.operator("object.cubefront_edgemiddle_minus_x", "", icon="LAYER_ACTIVE")  # "Back- Left")
                row.operator("object.cubefront_side_plus_y", "", icon="LAYER_ACTIVE")  # "Back")
                row.operator("object.cubefront_edgemiddle_plus_x", "", icon="LAYER_ACTIVE")  # "Back- Right")

                # Bottom
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55
                row.operator("object.cubeback_cornerbottom_minus_xy", "", icon="LAYER_ACTIVE")  # "Back- Left -Bottom")
                row.operator("object.cubefront_edgebottom_plus_y", "", icon="LAYER_ACTIVE")  # "Back - Bottom")
                row.operator("object.cubeback_cornerbottom_plus_xy", "", icon="LAYER_ACTIVE")  # "Back- Right -Bottom")

                ##############################
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = box.column(1)

            ###space1###

            #col = layout.column(align=True)
            if lt.display_bboxmiddle:
                row.scale_y = 1.2
                row.prop(lt, "display_bboxmiddle", text="Middle", icon='TRIA_DOWN')

            else:
                row.scale_y = 1
                row.prop(lt, "display_bboxmiddle", text="Middle", icon='TRIA_RIGHT')

            ###space1###
            if lt.display_bboxmiddle:
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                # Top
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubefront_edgetop_minus_x", "", icon="LAYER_ACTIVE")  # "Middle - Left Top")
                row.operator("object.cubefront_side_plus_z", "", icon="LAYER_ACTIVE")  # "Top")
                row.operator("object.cubefront_edgetop_plus_x", "", icon="LAYER_ACTIVE")  # "Middle - Right Top")

                # Middle
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubefront_side_minus_x", "", icon="LAYER_ACTIVE")  # "Left")
                obj = context.object
                if obj and obj.mode == 'EDIT':
                    row.operator("mesh.origincenter", text="", icon="LAYER_ACTIVE")
                else:
                    row.operator("object.origin_set", text="", icon="LAYER_ACTIVE").type = 'ORIGIN_GEOMETRY'

                row.operator("object.cubefront_side_plus_x", "", icon="LAYER_ACTIVE")  # "Right")

                # Bottom
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubefront_edgebottom_minus_x", "", icon="LAYER_ACTIVE")  # "Middle - Left Bottom")
                row.operator("object.cubefront_side_minus_z", "", icon="LAYER_ACTIVE")  # "Bottom")
                row.operator("object.cubefront_edgebottom_plus_x", "", icon="LAYER_ACTIVE")  # "Middle - Right Bottom")

                ##############################
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)

            ###space1###

            if lt.display_bboxfront:
                row.scale_y = 1.2
                row.prop(lt, "display_bboxfront", text="Front", icon='TRIA_DOWN')

            else:
                row.scale_y = 1
                row.prop(lt, "display_bboxfront", text="Front", icon='TRIA_RIGHT')

            ###space1###
            if lt.display_bboxfront:
                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                # Top
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubefront_cornertop_minus_xy", "", icon="LAYER_ACTIVE")  # "Front- Left -Top"
                row.operator("object.cubeback_edgetop_plus_y", "", icon="LAYER_ACTIVE")  # "Front - Top"
                row.operator("object.cubefront_cornertop_plus_xy", "", icon="LAYER_ACTIVE")  # "Front- Right -Top"

                # Middle
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubefront_edgemiddle_minus_y", "", icon="LAYER_ACTIVE")  # "Front- Left"
                row.operator("object.cubefront_side_minus_y", "", icon="LAYER_ACTIVE")  # "Front"
                row.operator("object.cubefront_edgemiddle_plus_y", "", icon="LAYER_ACTIVE")  # "Front- Right"

                # Bottom
                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.scale_x = 1.55

                row.operator("object.cubefront_cornerbottom_minus_xy", "", icon="LAYER_ACTIVE")  # "Front- Left -Bottom"
                row.operator("object.cubefront_edgebottom_minus_y", "", icon="LAYER_ACTIVE")  # "Front - Bottom"
                row.operator("object.cubefront_cornerbottom_plus_xy", "", icon="LAYER_ACTIVE")  # "Front- Right -Bottom")

            ###space###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Cursor", icon="FORCE_FORCE")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)

            row.operator("view3d.snap_cursor_to_grid", "to Grid")
            row.operator("view3d.snap_cursor_to_active", "to Active")
            row.operator("mesh.snapcenteroffset", "to Offset")
            row.operator("view3d.snap_cursor_to_center", "to Center")
            row.operator("view3d.snap_cursor_to_selected", "to Selected")

            row.operator("mesh.circlecenter", text="to Circle")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Selection", icon="RESTRICT_SELECT_OFF")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)
            row.operator("view3d.snap_selected_to_grid", "to Grid")
            row.operator("view3d.snap_selected_to_cursor", "to Offset").use_offset = True
            row.operator("mesh.snapcenteroffset", " to Center")
            row.operator("view3d.snap_selected_to_cursor", "to Cursor").use_offset = False


# ------------------------------------------------------------
# Editing  ######------------------------------------------------------------
# Editing  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_edit:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_edit", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_edit", text="", icon='TRIA_RIGHT')

        row.label("Edit...")

        row.operator("mesh.select_mode", text="", icon='VERTEXSEL').type = 'VERT'
        row.operator("mesh.select_mode", text="", icon='EDGESEL').type = 'EDGE'
        row.operator("mesh.select_mode", text="", icon='FACESEL').type = 'FACE'

        row.menu("VIEW3D_MT_edit_mesh_looptools", "", icon="SORTALPHA")

        if lt.display_edit:
            ###space###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("transform.translate", text="(G)", icon="MAN_TRANS")
            row.operator("transform.rotate", text="(R)", icon="MAN_ROT")
            row.operator("transform.resize", text="(S)", icon="MAN_SCALE")

            row = col_top.row(align=True)
            row.operator("object.vertex_warp", "Warp")
            row.operator("transform.tosphere", "to Sphere")

            row = col_top.row(align=True)
            row.operator("transform.shrink_fatten", text="Shrink/Fatten")
            row.operator("transform.push_pull", text="Push/Pull")

            row = col_top.row(align=True)
            row.operator("fan.move_faces_along_normals_operator", "Along Normals")
            row.operator("mesh.rot_con", "Rotate Face")

            row = col_top.row(align=True)
            row.operator("mesh.noise")
            row.operator("object.vertex_random")

            # --------------------------------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("mesh.remove_doubles")
            row.menu("VIEW3D_MT_edit_mesh_delete")

            row = col_top.row(align=True)
            row.operator("mesh.merge", "Merge Center").type = 'CENTER'
            row.operator_menu_enum("mesh.merge", "type")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("mesh.duplicate_move", "Duplicate", icon="MOD_DISPLACE")

            row = col_top.row(align=True)
            row.operator("mesh.split", icon="MOD_BOOLEAN")
            row.operator("mesh.separate", text="Separate", icon="ORTHO")

            row = col_top.row(align=True)
            row.operator("mesh.spin", icon="MOD_SIMPLEDEFORM")
            row.operator("mesh.screw", icon="MOD_SCREW")

            # --------------------------------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Cutting")

            row = col_top.row(align=True)
            row.operator("mesh.snap_utilities_line", "SnapLine", icon="LINE_DATA")
            row.operator("mesh.loopcut_slide", "Loop Cut / Slide", icon="COLLAPSEMENU")

            row = col_top.row(align=True)
            props = row.operator("mesh.knife_tool", text="Knife", icon="LINE_DATA")
            props.use_occlude_geometry = True
            props.only_selected = False

            props = row.operator("mesh.knife_tool", text="Knife Select", icon="LINE_DATA")
            props.use_occlude_geometry = False
            props.only_selected = True

            row = col_top.row(align=True)
            row.operator("mesh.knife_project", icon="LINE_DATA")
            row.operator("mesh.bisect", icon="SCULPTMODE_HLT")

            row = col_top.row(align=True)
            row.operator("mesh.ext_cut_faces", text="Face Cut", icon="SNAP_EDGE")
            row.operator("object.createhole", text="Face Hole", icon="RADIOBUT_OFF")

            # --------------------------------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Subdivide / Tri / Quads")

            row = col_top.row(align=True)
            row.operator("mesh.subdivide", text="1").number_cuts = 1
            row.operator("mesh.subdivide", text="2").number_cuts = 2
            row.operator("mesh.subdivide", text="3").number_cuts = 3
            row.operator("mesh.subdivide", text="4").number_cuts = 4
            row.operator("mesh.subdivide", text="5").number_cuts = 5
            row.operator("mesh.subdivide", text="6").number_cuts = 6

            row = col_top.row(align=True)
            row.operator("mesh.tris_convert_to_quads", text="", icon="OUTLINER_OB_LATTICE")
            row.operator("mesh.unsubdivide", text="(Un-)Subdivide")
            row.operator("screen.redo_last", text="", icon="SCRIPTWIN")

            row.operator("mesh.quads_convert_to_tris", text="", icon="OUTLINER_OB_MESH")

            # --------------------------------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Connect")

            row = col_top.row(align=True)
            row.operator("mesh.vert_connect", "Vert Face")
            row.operator("mesh.vert_connect_path", "Vert Path")

            row = col_top.row(align=True)
            row.operator("mesh.edge_face_add", "Edge / Face")
            row.operator("mesh.bridge_edge_loops", "Edge Bridge")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Arrange")

            row = col_top.row(align=True)
            row.operator("mesh.vertex_align", text="Align", icon="ALIGN")
            row.operator("transform.edge_slide", text="Slide Edge")

            row = col_top.row(align=True)
            row.operator("mesh.vertex_distribute", text="Distribute", icon="PARTICLE_POINT")

            row.operator("transform.vert_slide", text="Slide Vertex")

            row = col_top.row(align=True)
            row.operator("mesh.vertices_smooth", "Smooth Vert", icon="SPHERECURVE")
            row.operator("mesh.vertices_smooth_laplacian", "Laplacian")

            # --------------------------------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Fill / Extrude / Inset")

            row = col_top.row(align=True)
            row.operator_menu_enum('mesh.offset_edges', 'geometry_mode')
            row.menu("VIEW3D_MT_edit_mesh_extrude", text="Extrude")

            row = col_top.row(align=True)
            row.operator("mesh.fill_grid", "Grid Fill")

            row.operator('object.mextrude', text='Multi Extrude')

            row = col_top.row(align=True)
            row.operator('faceinfillet.op0_id', text='Face Fillet')
            row.operator("fillet.op0_id", text="Edge Fillet")

            row = col_top.row(align=True)
            row.operator("mesh.poke", text="Poke")
            row.operator("mesh.beautify_fill", text="Beautify")

            row = col_top.row(align=True)
            row.operator("mesh.solidify", text="Solidify")
            row.operator("mesh.wireframe", text="Wire")

            row = col_top.row(align=True)
            row.operator("mesh.extrude_along_curve", text="Along Curve")
            row.operator("mechappo.create", text="Mechappo")

            # --------------------------------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("LoopTools")

            row = col_top.row(align=True)
            row.operator("mesh.looptools_circle")
            row.operator("mesh.looptools_relax")

            row = col_top.row(align=True)
            row.operator("mesh.looptools_bridge", text="Bridge").loft = False
            row.operator("mesh.looptools_flatten")

            row = col_top.row(align=True)
            row.operator("mesh.looptools_bridge", text="Loft").loft = True
            row.operator("mesh.looptools_space")

            row = col_top.row(align=True)
            row.operator("mesh.looptools_gstretch")
            row.operator("mesh.looptools_curve")

            # --------------------------------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            Automerge = context.tool_settings
            row.prop(Automerge, "use_mesh_automerge", text="Auto Merge")

            row = col_top.row(align=True)
            row.operator("double.threshold01", text="TSHD 0.1")
            row.operator("double.threshold0001", text="TSHD 0.001")

            tool_settings = context.tool_settings
            row = col_top.row(align=True)
            row.label("Double Threshold:")
            row = col_top.row(align=True)
            row.prop(tool_settings, "double_threshold", text="")


# -------------------------------------------------------
# CadTools  #######-------------------------------------------------------
# CadTools  #######-------------------------------------------------------
# -------------------------------------------------------

        if lt.display_cadtools:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_cadtools", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_cadtools", text="", icon='TRIA_RIGHT')

        row.label("CAD...")

        row.operator("mesh.snap_utilities_line", "", icon="LINE_DATA")
        row.operator("mesh.intersect", "", icon='ZOOMIN').use_separate = False
        row.operator("mesh.intersect", "", icon='ZOOMOUT').use_separate = True
        row.operator("mesh.bridge_edge_loops", "", icon="SOUND")

        if lt.display_cadtools:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("view3d.autovtx", text="Auto-VTX")
            row.operator("mesh.circlecenter", text="Circle Center")

            row = col_top.row(align=True)
            row.operator("mesh.vertintersect", text="V2X")
            row.operator("mesh.intersectal", text="X-All")
            row.operator("mesh.linetobisect", text="BIX")
            row.operator("mesh.cutonperp", text="PERP CUT")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.column(align=True)
            row.operator("bpt.boolean_2d_union", text="Union 2d Faces", icon="LOCKVIEW_ON")
            row.operator("mesh.perpbisector", icon="OUTLINER_DATA_MESH")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.column(align=True)
            row.operator("mesh.retopomt", text="Retopo MT", icon="ORTHO")


# -------------------------------------------------------
# Mira Tools  ############-------------------------------------------------------
# Mira Tools  ############-------------------------------------------------------
# -------------------------------------------------------

        ####
        if lt.display_miraedit:

            box = layout.box()
            row = box.row()
            row.prop(lt, "display_miraedit", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_miraedit", text="", icon='TRIA_RIGHT')

        row.label("Deform...")  # Mira
        row.operator("mira.draw_extrude", text="", icon="FORCE_MAGNETIC")
        row.operator("mira.linear_deformer", text="", icon="OUTLINER_OB_MESH")
        row.operator("mira.curve_stretch", text="", icon="CURVE_NCURVE")

        ###space1###
        if lt.display_miraedit:
            ###space2###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.label("Deform")

            row = col_top.row(align=True)
            row.operator("mira.noise", text="Noise")
            row.operator("mira.deformer", text="Deformer")

            row = col_top.row(align=True)
            row.operator("mira.linear_deformer", text="LinearDeformer")
            row.prop(context.scene.mi_ldeformer_settings, "manual_update", text='ManualUpdate')
            # ----------------------------------------------------------------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.label("Modify")

            row = col_top.column()
            row.operator("mira.draw_extrude", text="Draw Extrude")

            row.prop(context.scene.mi_extrude_settings, "extrude_mode", text='Mode')
            row.prop(context.scene.mi_extrude_settings, "extrude_step_type", text='Step')

            if context.scene.mi_extrude_settings.extrude_step_type == 'Asolute':
                row.prop(context.scene.mi_extrude_settings, "absolute_extrude_step", text='')
            else:
                row.prop(context.scene.mi_extrude_settings, "relative_extrude_step", text='')

            if context.scene.mi_extrude_settings.extrude_mode == 'Screen':
                row.prop(context.scene.mi_extrude_settings, "do_symmetry", text='Symmetry')
                if context.scene.mi_extrude_settings.do_symmetry:
                    row.prop(context.scene.mi_extrude_settings, "symmetry_axys", text='Axys')

            # ----------------------------------------------------------------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.label(text="CurveStretch:")

            row = col_top.column(1)
            row.operator("mira.curve_stretch", text="CurveStretch")
            row.prop(context.scene.mi_cur_stretch_settings, "points_number", text='PointsNumber')

            row.separator()
            row.prop(context.scene.mi_cur_stretch_settings, "spread_mode", text='Spread')

            # ----------------------------------------------------------------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.label(text="CurveGuide:")

            row = col_top.column(align=True)
            row.operator("mira.curve_guide", text="CurveGuide")
            row.prop(context.scene.mi_curguide_settings, "points_number", text='PointsNumber')

            row = col_top.column(align=True)
            row.prop(context.scene.mi_curguide_settings, "deform_type", text='DeformType')

            # ----------------------------------------------------------------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.label("CurveSettings")

            row = col_top.column(align=True)
            row.prop(context.scene.mi_curve_settings, "curve_resolution", text='Resolution')
            row.prop(context.scene.mi_curve_settings, "draw_handlers", text='Handlers')
            row.operator("mira.curve_test", text="Curve Test")


# -------------------------------------------------------
# Edge Tools  #######-------------------------------------------------------
# Edge Tools  #######-------------------------------------------------------
# -------------------------------------------------------

            col = layout.column(align=True)

            split = col.split()  # percentage=0.15, align=True)

            if lt.display_saveedge:
                split.prop(lt, "display_saveedge", text="Edge Save Tool", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                split.prop(lt, "display_saveedge", text="Edge Save Tool", icon='DISCLOSURE_TRI_RIGHT_VEC')

            # split.operator("")

            if lt.display_saveedge:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.prop(context.scene, 'isEdgerActive')
                row.prop(context.scene, 'isEdgerDebugActive')

                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("wm.lock_edge_loop_idname", text="Lock Edge Loop", icon="GROUP_VERTEX")
                row = col_top.row(align=True)
                row.operator("wm.clear_edger_oops_idname", text="Clear Loops", icon="MOD_SOLIDIFY")
                col = layout.column(align=True)

            split = col.split()  # percentage=0.15, align=True)

            if lt.display_tooledge:
                split.prop(lt, "display_tooledge", text="Edge Extend Tools", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                split.prop(lt, "display_tooledge", text="Edge Extend Tools", icon='DISCLOSURE_TRI_RIGHT_VEC')

            # split.operator("")

            if lt.display_tooledge:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("object.mesh_edge_lengthchange", "Edge Length")
                row = col_top.row(align=True)
                row.operator('mesh.edge_roundifier')
                row = col_top.row(align=True)
                row.operator("mesh.edgetune", text="Edgetune Slider")

                col = layout.column(align=True)
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
# Normals  #######-------------------------------------------------------
# Normals  #######-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        if context.mode == 'EDIT_MESH':

            ###space1###
            #col = layout.column(align=True)
            if lt.display_normals:
                ###space2###
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_normals", text="", icon='TRIA_DOWN')

            else:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_normals", text="", icon='TRIA_RIGHT')

            row.label("Normals...")
            row.operator("mesh.flip_normals", text="", icon="FILE_REFRESH")
            row.operator("mesh.normals_make_consistent", text="", icon='SNAP_NORMAL')
            ###space1###
            if lt.display_normals:
                col = layout.column(align=True)
                ###space2###
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("mesh.normals_make_consistent", text="Recalculate")
                row.operator("mesh.flip_normals", text="Flip")

                row = col_top.row(align=True)
                row.operator("mesh.normals_make_consistent", text="Rec-Inside").inside = True
                row.operator("mesh.normals_make_consistent", text="Rec-Outside").inside = False

                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.prop(mesh, "show_normal_vertex", text="", icon='VERTEXSEL')
                row.prop(mesh, "show_normal_face", text="", icon='FACESEL')

                row.active = mesh.show_normal_vertex or mesh.show_normal_face
                row.prop(context.scene.tool_settings, "normal_size", text="Size")

                row = col_top.row(align=True)
                row.prop(mesh, "show_double_sided")
                row = col_top.row(align=True)
                row.prop(mesh, "use_auto_smooth")

                row = col_top.row(align=True)
                row.active = mesh.use_auto_smooth
                row.prop(mesh, "auto_smooth_angle", text="Angle")


# -------------------------------------------------------
# Auto Mirror  #######-------------------------------------------------------
# Auto Mirror  #######-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        if lt.display_mirrcut_edm:
            ###space2###
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_mirrcut_edm", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_mirrcut_edm", text="", icon='TRIA_RIGHT')

        row.label("MirrorCut...")
        row.operator("view3d.display_modifiers_viewport_off", "", icon='VISIBLE_IPO_OFF')
        row.operator("view3d.display_modifiers_viewport_on", "", icon='RESTRICT_VIEW_OFF')
        row.operator("object.automirror", text="", icon="MOD_WIREFRAME")

        ###space1###
        if lt.display_mirrcut_edm:
            ###space2###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.prop(context.scene, "AutoMirror_orientation", text="")
            row.prop(context.scene, "AutoMirror_axis", text="")

            row = col_top.row(align=True)
            row.prop(context.scene, "AutoMirror_threshold", text="Threshold")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.prop(context.scene, "AutoMirror_toggle_edit", text="Toggle edit")
            row = col_top.row(align=True)
            row.prop(context.scene, "AutoMirror_cut", text="Cut+Mirror")
            if bpy.context.scene.AutoMirror_cut:
                row.prop(context.scene, "AutoMirror_use_clip", text="Use Clip")
                row = col_top.row(align=True)
                row.prop(context.scene, "AutoMirror_show_on_cage", text="Editable")
                row.prop(context.scene, "AutoMirror_apply_mirror", text="Apply")

            else:
                row.label(icon="ERROR", text="No mesh selected")


# -------------------------------------------------------
# Modifier  ############-------------------------------------------------------
# Modifier  ############-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        if lt.display_modif_edm:
            ###space2###
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_modif_edm", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_modif_edm", text="", icon='TRIA_RIGHT')

        row.label("Modifier...")
        row.operator_menu_enum("object.modifier_add", "type", text="", icon="MODIFIER")
        row.operator("view3d.display_modifiers_delete", "", icon='X')
        row.operator("view3d.display_modifiers_apply_edm", "", icon='FILE_TICK')

        ###space1###
        if lt.display_modif_edm:
            ###space2###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)

            row.label("SubSurf Levels")

            row = col_top.row(align=True)
            row.operator("view3d.modifiers_subsurf_level_0")
            row.operator("view3d.modifiers_subsurf_level_1")
            row.operator("view3d.modifiers_subsurf_level_2")
            row.operator("view3d.modifiers_subsurf_level_3")
            row.operator("view3d.modifiers_subsurf_level_4")
            row.operator("view3d.modifiers_subsurf_level_5")
            row.operator("view3d.modifiers_subsurf_level_6")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.label("Mirror Modifier / all enabled")

            row = col_top.row(align=True)
            row.operator("view3d.fullmirror", text="X-Clip")
            row.operator("view3d.fullmirrory", text="Y-Clip")
            row.operator("view3d.fullmirrorz", text="Z-Clip")

            ###space2###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("view3d.display_modifiers_viewport_on", icon='RESTRICT_VIEW_OFF')
            row.operator("view3d.display_modifiers_edit_on", icon='EDITMODE_HLT')
            row.operator("view3d.display_modifiers_cage_on", icon='OUTLINER_OB_MESH')

            row = col_top.row(align=True)
            row.operator("view3d.display_modifiers_viewport_off", icon='VISIBLE_IPO_OFF')
            row.operator("view3d.display_modifiers_edit_off", icon='SNAP_VERTEX')
            row.operator("view3d.display_modifiers_cage_off", icon='OUTLINER_DATA_MESH')

            ###space2###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("view3d.display_modifiers_delete", icon='X')
            row.operator("view3d.display_modifiers_apply_edm", icon='FILE_TICK')

            row = col_top.row(align=True)
            row.operator("view3d.display_modifiers_expand", icon='DISCLOSURE_TRI_DOWN_VEC')
            row.operator("view3d.display_modifiers_collapse", icon='DISCLOSURE_TRI_RIGHT_VEC')


# -------------------------------------------------------
# SnapShot Mesh  ############-------------------------------------------------------
# SnapShot Mesh  ############-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        if lt.display_snapshot:
            ###space2###
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_snapshot", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_snapshot", text="", icon='TRIA_RIGHT')

        row.label("SnapShot...")
        row.operator("vtools.capturesnapshot", icon='ZOOMIN', text="")
        row.operator("vtools.deletesnapshot", icon='ZOOMOUT', text="")

        ###space1###
        if lt.display_snapshot:
            ###space2###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.template_list('UI_UL_list', "snapShotMesh_ID", obj, "snapShotMeshes", obj, "snapShotMesh_ID_index", rows=2)

            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("vtools.usesnapshot", icon='OUTLINER_OB_MESH', text="Set Geometry")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("vtools.recalculatesnapshotfromchildren", icon='BORDERMOVE', text="Recalulate")

            row = col_top.row(align=True)
            row.operator("vtools.deleteallsnapshot", icon='X', text="Del. All")
            row.operator("vtools.deleteunusedsnapshotlist", icon='CANCEL', text="Del. Unused")


# -------------------------------------------------------
# Shading  #######-------------------------------------------------------
# Shading  #######-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        if lt.display_shading:
            ###space2###
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_RIGHT')

        row.label("Visual...")
        row.prop(context.space_data.fx_settings, "use_ssao", text="", icon='GROUP')
        row.operator("object.shade_smooth", text="", icon="SOLID")
        row.operator("object.shade_flat", text="", icon="MESH_CIRCLE")
        row.operator("object.wire_all", text="", icon='WIRE')

        ###space1###
        if lt.display_shading:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("wm.context_toggle", text="Xray", icon='META_CUBE').data_path = "object.show_x_ray"
            row.menu("htk_modifly", text="Flymode", icon='MOD_SOFT')

            row = col_top.row(align=True)
            row.operator("wm.context_toggle", text="Hide Wire", icon='GHOST_ENABLED').data_path = "space_data.show_occlude_wire"
            row.operator("wm.context_toggle", text="Limit 2 Visible", icon='ORTHO').data_path = "space_data.use_occlude_geometry"

            view = context.space_data
            obj = context.object

            row = col_top.row(align=True)
            row.prop(view, "show_backface_culling", text="BF Culling")
            row.prop(view, "use_matcap")
            if view.use_matcap:
                row = col_top.row(align=True)
                row.template_icon_view(view, "matcap_icon")


# -------------------------------------------------------
# Multi Edit  #######-------------------------------------------------------
# Multi Edit  #######-------------------------------------------------------
# -------------------------------------------------------

        #box = layout.box()
        #split = box.split(percentage=0.15, align=True)

        if lt.display_multiedit:
            box = layout.box()
            row = box.row(True)
            row.prop(lt, "display_multiedit", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row(True)
            row.prop(lt, "display_multiedit", text="", icon='TRIA_RIGHT')

        spread_op = row.operator("object.editmode_toggle", text="Object Toggle", icon="OBJECT_DATAMODE")

        if lt.display_multiedit:
            sce = bpy.context.scene

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("objects.multiedit_enter_operator")  # icon = something

            row = col_top.row(align=True)
            row.operator("objects.multiedit_exit_operator")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.prop(sce, "Preserve_Location_Rotation_Scale", "Keep G/R/S & Pivot")


# ------------------------------------------------------------
# Expand  ######------------------------------------------------------------
# Expand  ######------------------------------------------------------------
# ------------------------------------------------------------

        #col = layout.column(align=True)
        # split = col.split()#percentage=0.15)

        if lt.display_expand:
            row.prop(lt, "display_expand", text="", icon='PINNED')
        else:
            row.prop(lt, "display_expand", text="", icon='UNPINNED')

        #split.operator("", text="", icon="")

        if lt.display_expand:
            col = layout.column(align=True)

    # -------------------------------------------------------
    # Shrink Retopo  #######-------------------------------------------------------
    # Shrink retopo  #######-------------------------------------------------------
    # -------------------------------------------------------

            #col = layout.column(align=True)
            split = col.split()  # percentage=0.15)

            if lt.display_shrinkretop:
                split.prop(lt, "display_shrinkretop", text="...ShrinkKit...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_shrinkretop", text="...ShrinkKit...", icon='RIGHTARROW')

            #split.operator("object.modifier_add", text="Subdivision Level", icon = 'MOD_SUBSURF').type="SUBSURF"

            if lt.display_shrinkretop:
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
                row.operator("view3d.display_modifiers_apply_edm", icon='FILE_TICK')

    # -------------------------------------------------------
    # Copy Tools  #######-------------------------------------------------------
    # Copy Tools  #######-------------------------------------------------------
    # -------------------------------------------------------

            #col = layout.column(align=True)
            split = col.split()  # percentage=0.15)

            if lt.display_copy_edm:
                split.prop(lt, "display_copy_edm", text="...CopyShop...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_copy_edm", text="...CopyShop...", icon='RIGHTARROW')

            #split.operator("", text="", icon="")

            if lt.display_copy_edm:

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

    # -------------------------------------------------------
    # Material Tools  #######-------------------------------------------------------
    # Material Tools  #######-------------------------------------------------------
    # -------------------------------------------------------

            #col = layout.column(align=True)
            split = col.split()  # percentage=0.15)

            if lt.display_material_edm:
                split.prop(lt, "display_material_edm", text="...MatTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_material_edm", text="...MatTools...", icon='RIGHTARROW')

            #split.operator("", text="", icon="")

            if lt.display_material_edm:

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

    # -------------------------------------------------------
    # UV Mapping Edit  #######-------------------------------------------------------
    # UV Mapping Edit  #######-------------------------------------------------------
    # -------------------------------------------------------

            split = col.split()  # percentage=0.15)

            if lt.display_unwrap:
                split.prop(lt, "display_unwrap", text="...UVTools ...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_unwrap", text="...UVTools....", icon='RIGHTARROW')

            #split.operator("object.modifier_add", text="Subdivision Level", icon = 'MOD_SUBSURF').type="SUBSURF"

            if lt.display_unwrap:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)

                row.operator("mesh.mark_seam").clear = False
                row.operator("mesh.mark_seam", text="Clear Seam").clear = True

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("uv.copy_uv")
                row.operator("uv.paste_uv")

                row = col_top.row(align=True)
                row.operator("uv.copy_uv_sel_seq", "Copy UV Sel. Seq.")
                row.operator("uv.paste_uv_sel_seq", "Paste UV Sel. Seq.")

                row = col_top.row(align=True)
                row.menu("uv.copy_uv_map", "Copy UV Map")
                row.menu("uv.paste_uv_map", "Paste UV Map")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.operator("uv.reproject_image", text="Reproject Image")

    # Unwrap  ######-------------------------------------------------------
    # Unwrap  ######-------------------------------------------------------

                split = col.split()  # percentage=0.15)

                if lt.display_unwrapset:
                    split.prop(lt, "display_unwrapset", text="Unwrap", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_unwrapset", text="Unwrap", icon='DISCLOSURE_TRI_RIGHT_VEC')

                # split.operator("uv.reset",text="Reset")

                if lt.display_unwrapset:
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

                split = col.split()  # percentage=0.15)

                if lt.display_uvsure:
                    split.prop(lt, "display_uvsure", text="SureUVW", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_uvsure", text="SureUVW", icon='DISCLOSURE_TRI_RIGHT_VEC')

                # split.operator("uv.reset",text="Reset")

                if lt.display_uvsure:
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

                split = col.split()  # percentage=0.15)

                if lt.display_uvnext:
                    split.prop(lt, "display_uvnext", text="TexSpace / Freestyle", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    split.prop(lt, "display_uvnext", text="TexSpace / Freestyle", icon='DISCLOSURE_TRI_RIGHT_VEC')

                # split.operator("uv.reset",text="Reset")

                if lt.display_uvnext:
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

    # -------------------------------------------------------
    # Weight Only  #######-------------------------------------------------------
    # Weight Only  #######-------------------------------------------------------
    # -------------------------------------------------------

            #col = layout.column(align=True)
            split = col.split()  # percentage=0.15)

            if lt.display_weight:
                split.prop(lt, "display_weight", text="...Weights...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_weight", text="...Weights...", icon='RIGHTARROW')

            #split.operator("", text="", icon="")

            if lt.display_weight:
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

    # -------------------------------------------------------
    # Hook  ######-------------------------------------------------------
    # Hook  ######-------------------------------------------------------
    # -------------------------------------------------------

            split = col.split()  # percentage=0.15)

            if lt.display_hook:
                split.prop(lt, "display_hook", text="...Hook...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_hook", text="...Hook...", icon='RIGHTARROW')

            #split.operator_menu_enum("object.constraint_add", "type", text="Constraint", icon="CONSTRAINT_DATA")

            if lt.display_hook:
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

    # -------------------------------------------------------
    # CleanUp  #######-------------------------------------------------------
    # CleanUp  #######-------------------------------------------------------
    # -------------------------------------------------------

            #col = layout.column(align=True)
            split = col.split()

            if lt.display_cleanup:
                split.prop(lt, "display_cleanup", text="...Delete...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_cleanup", text="...Delete...", icon='RIGHTARROW')

            if lt.display_cleanup:
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)
                row = col_top.row(align=True)
                row.operator("meshlint.select", "Meshlint > Object Data")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.menu("VIEW3D_MT_edit_mesh_showhide", "Show / Hide", icon="RESTRICT_VIEW_OFF")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("mesh.delete", "Vertices", icon="SNAP_VERTEX").type = "VERT"
                row = col_top.row(align=True)
                row.operator("mesh.dissolve_verts")
                row.operator("mesh.remove_doubles")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("mesh.delete", "Edges", icon="SNAP_EDGE").type = "EDGE"
                row = col_top.row(align=True)
                row.operator("mesh.dissolve_edges")
                row.operator("mesh.delete_edgeloop", text="Remove Edge Loop")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("mesh.delete", "Faces", icon="SNAP_FACE").type = "FACE"
                row = col_top.row(align=True)
                row.operator("mesh.dissolve_faces")
                row.operator("mesh.delete", "Remove only Faces").type = "ONLY_FACE"

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("mesh.dissolve_limited", icon="MATCUBE")
                row = col_top.row(align=True)
                row.operator("mesh.dissolve_degenerate")
                row.operator("mesh.delete", "Remove Edge & Faces").type = "EDGE_FACE"

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("mesh.delete_loose", text="Loose", icon="STICKY_UVS_DISABLE")
                row.operator("mesh.fill_holes")
                row = col_top.row(align=True)
                row.operator("mesh.dissolve_degenerate")
                row.operator("mesh.vert_connect_nonplanar")

    # -------------------------------------------------------
    # Bsurf  ############-------------------------------------------------------
    # Bsurf  ############-------------------------------------------------------
    # -------------------------------------------------------

            scn = context.scene
            #col = layout.column(align=True)
            split = col.split()  # percentage=0.15)

            if lt.display_bsurf:
                ###space2###
                split.prop(lt, "display_bsurf", text="..Bsurfaces...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_bsurf", text="...Bsurfaces...", icon='RIGHTARROW')

            ###space1###
            if lt.display_bsurf:
                col = layout.column(align=True)
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

    # -------------------------------------------------------
    # Grease Pencil  #######-------------------------------------------------------
    # Grease Pencil  #######-------------------------------------------------------
    # -------------------------------------------------------

            #col = layout.column(align=True)
            split = col.split()  # percentage=0.15)

            if lt.display_pencil:
                split.prop(lt, "display_pencil", text="...PencilTools...", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "display_pencil", text="...PencilTools...", icon='RIGHTARROW')

            #split.operator("", text="", icon="")

            if lt.display_pencil:
                box = col.column(align=True).box().column()
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

        #####################################
        draw_B_history_tools(context, layout)
        #####################################


######################################################################################################################################################
########------------------#################
# Editmode Curve  ##############################-------------------------------------------------------
# Editmode Curve  ##############################-------------------------------------------------------
########------------------#################
######################################################################################################################################################

class VIEW3D_CurveEditMode(bpy.types.Panel):
    bl_category = "META"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_context = "curve_edit"
    bl_label = "MetaTool"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_CURVE'))

    def draw(self, context):
        lt = context.window_manager.metawindow
        layout = self.layout
        obj = context.object

        col = layout.column(align=True)
        box = col.column(align=True).box().column()
        col_top = box.column(align=True)

        row = col_top.row(align=True)
        row.alignment = 'CENTER'
        sub = row.row(1)
        sub.scale_x = 1.2

        sub.operator("curve.primitive_bezier_curve_add", icon='CURVE_BEZCURVE', text="")
        sub.operator("curve.primitive_bezier_circle_add", icon='CURVE_BEZCIRCLE', text="")
        sub.operator("curve.primitive_nurbs_curve_add", icon='CURVE_NCURVE', text="")
        sub.operator("curve.primitive_nurbs_circle_add", icon='CURVE_NCIRCLE', text="")
        sub.operator("curve.primitive_nurbs_path_add", icon='CURVE_PATH', text="")
        #row.menu("INFO_MT_curve_add", text="Add")
        row.operator("object.curv_to_2d", text="2d")
        row.operator("object.curv_to_3d", text="3d")


# ------------------------------------------------------------
# Selection Curve  ######------------------------------------------------------------
# Selection Curve  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_selectionbezi:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selectionbezi", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selectionbezi", text="", icon='TRIA_RIGHT')

        row.label("Select...")
        row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")
        row.operator("view3d.select_border", text="", icon="BORDER_RECT")
        row.menu("VIEW3D_MT_edit_curve_showhide", "", icon="VISIBLE_IPO_ON")

        if lt.display_selectionbezi:
            col = layout.column(align=True)
            box = col.column(align=True).box().column(1)
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("curve.select_all", text="Inverse").action = 'INVERT'
            row.operator("curve.select_random", text="Random")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("curve.select_linked", text="Linked")
            row.operator("curve.select_nth", text="Checker")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("curve.de_select_first", text="First")
            row.operator("curve.de_select_last", text="Last")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("curve.select_next", text="Next")
            row.operator("curve.select_previous", text="Previous")


# ------------------------------------------------------------
# Curve Info   ######------------------------------------------------------------
# Curve Info  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_curveinfo:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_curveinfo", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_curveinfo", text="", icon='TRIA_RIGHT')

        row.label("Selections Info...")
        op = row.operator("curvetools2.operatorcurveinfo", text="", icon="INFO")

        if lt.display_curveinfo:

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("curvetools2.operatorsplinesinfo", text="Curve splines info")

            row = col_top.row(align=True)
            row.operator("curvetools2.operatorsegmentsinfo", text="Curve segments info")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("curvetools2.operatorselectioninfo", text="Selection Info:")
            row = col_top.row(align=True)
            row.prop(context.scene.curvetools, "NrSelectedObjects", text="")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("curvetools2.operatorcurvelength", text="Calc Length")
            row = col_top.row(align=True)
            row.prop(context.scene.curvetools, "CurveLength", text="")


# ------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_orientedm:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orientedm", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orientedm", text="", icon='TRIA_RIGHT')

        # row.label("Orientation...")
        sub = row.row(1)
        sub.scale_x = 7
        sub.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
        sub.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
        sub.operator("view3d.pivot_active", "", icon="ROTACTIVE")
        sub.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
        sub.operator("view3d.pivot_median", "", icon="ROTATECENTER")

        if lt.display_orientedm:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.loops1", text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="MZ", icon='ARROW_LEFTRIGHT')

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("mesh.face_align_x", "FX", icon='TRIA_RIGHT')
            row.operator("mesh.face_align_y", "FY", icon='TRIA_UP')
            row.operator("mesh.face_align_z", "FZ", icon='SPACE3')

            row = col_top.row(align=True)
            row.operator("mesh.face_align_xy", "Xy", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy", icon='TRIA_UP_BAR')
            row.operator("mesh.face_align_xz", "Zx", icon='TRIA_LEFT_BAR')


# ---------------------
# ---------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.loops7", "Ob-Mode", icon="OBJECT_DATAMODE")
            row.operator("object.loops9", "Ed-Mode", icon="EDITMODE_HLT")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Cursor", icon="FORCE_FORCE")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)
            row.operator("view3d.snap_cursor_to_grid", "to Grid")
            row.operator("view3d.snap_cursor_to_active", "to Active")
            row.operator("view3d.snap_cursor_to_center", "to Center")
            row.operator("view3d.snap_cursor_to_selected", "to Selected")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Selected", icon="RESTRICT_SELECT_OFF")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)
            row.operator("view3d.snap_selected_to_grid", "to Grid")
            row.operator("view3d.snap_selected_to_cursor", "to Offset").use_offset = True
            row.operator("mesh.snapcenteroffset", " to Center")
            row.operator("view3d.snap_selected_to_cursor", "to Cursor").use_offset = False


# ------------------------------------------------------------
# Editing  ######------------------------------------------------------------
# Editing  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_edit:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_edit", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_edit", text="", icon='TRIA_RIGHT')

        row.label("Edit...")

        row.operator("curve.surfsk_first_points", "", icon="PARTICLE_TIP")
        row.operator("curve.switch_direction", "", icon="ARROW_LEFTRIGHT")

        if lt.display_edit:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("object._curve_outline", text="Outline")
            row.operator("bpt.bezier_curve_split", text="Split")
            row.operator("curve.make_segment", text="Segment")

            row = col_top.row(align=True)
            row.operator("curve.subdivide", text="1").number_cuts = 1
            row.operator("curve.subdivide", text="2").number_cuts = 2
            row.operator("curve.subdivide", text="3").number_cuts = 3
            row.operator("curve.subdivide", text="4").number_cuts = 4
            row.operator("curve.subdivide", text="5").number_cuts = 5
            row.operator("curve.subdivide", text="6").number_cuts = 6

            # ---------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("curve.radius_set", "Radius")
            row.operator("curve.smooth")

            # ---------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("curve.handle_type_set", text="Auto").type = 'AUTOMATIC'
            row.operator("curve.handle_type_set", text="Vector").type = 'VECTOR'
            row = col_top.row(align=True)
            row.operator("curve.handle_type_set", text="Align").type = 'ALIGNED'
            row.operator("curve.handle_type_set", text="Free").type = 'FREE_ALIGN'

            # ---------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("curve.spline_type_set", "Spline Type")
            row.operator("curve.cyclic_toggle", text="Toggle Cyclic")


# ------------------------------------------------------------
# Curve Tools   ######------------------------------------------------------------
# Curve Tools   ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_curveloft:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_curveloft", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_curveloft", text="", icon='TRIA_RIGHT')

        row.label("CurveT2...")

        row.operator("curvetools2.operatorsplinessetresolution", text="Resolution")
        row.prop(context.scene.curvetools, "SplineResolution", text="")

        if lt.display_curveloft:

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


# -------------------------------------------------------
# Shading  #######-------------------------------------------------------
# Shading  #######-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        if lt.display_shading:
            ###space2###
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_RIGHT')

        row.label("Visual...")
        row.prop(context.space_data.fx_settings, "use_ssao", text="", icon='GROUP')
        row.operator("object.wire_all", text="", icon='WIRE')

        ###space1###
        if lt.display_shading:
            col = layout.column(align=True)
            ###space2###
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("wm.context_toggle", text="Xray", icon='META_CUBE').data_path = "object.show_x_ray"

            view = context.space_data
            obj = context.object

            row = col_top.row(align=True)
            row.prop(view, "use_matcap")
            if view.use_matcap:
                row = col_top.row(align=True)
                row.template_icon_view(view, "matcap_icon")


# -------------------------------------------------------
# Grease Pencil  #######-------------------------------------------------------
# Grease Pencil  #######-------------------------------------------------------
# -------------------------------------------------------

        if lt.display_pencil:
            ###space2###
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_pencil", text="", icon='TRIA_DOWN')
        else:
            ###space2###
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_pencil", text="", icon='TRIA_RIGHT')

        row.label("PencilTools...")
        row.operator("curve.surfsk_reorder_splines", text="", icon="ALIGN")
        row.operator("gpencil.draw", text="", icon="GREASEPENCIL").mode = 'DRAW'

        if lt.display_pencil:
            col = layout.column(align=True)
            ###space2###
            box = col.column(align=True).box().column()
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

        # --------------------------

        box = layout.box()
        row = box.row(True)
        row.operator("object.editmode_toggle", text="Object Toggle", icon="OBJECT_DATAMODE")

        #####################################
        draw_B_history_tools(context, layout)
        #####################################


######################################################################################################################################################
########--------------------#################
# Editmode Surface  ##############################-------------------------------------------------------
# Editmode Surface  ##############################-------------------------------------------------------
########--------------------#################
######################################################################################################################################################

class VIEW3D_SurfaceEditmode(bpy.types.Panel):
    bl_category = "META"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_label = "MetaTool"
    bl_context = "surface_edit"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_SURFACE'))

    def draw(self, context):
        lt = context.window_manager.metawindow
        layout = self.layout
        obj = context.object

        col = layout.column(align=True)
        box = col.column(align=True).box().column()
        col_top = box.column(align=True)

        row = col_top.row(align=True)
        row.alignment = 'CENTER'
        sub = row.row(1)
        sub.scale_x = 1.2

        sub.operator("surface.primitive_nurbs_surface_curve_add", icon='SURFACE_NCURVE', text="")
        sub.operator("surface.primitive_nurbs_surface_circle_add", icon='SURFACE_NCIRCLE', text="")
        sub.operator("surface.primitive_nurbs_surface_surface_add", icon='SURFACE_NSURFACE', text="")
        sub.operator("surface.primitive_nurbs_surface_cylinder_add", icon='SURFACE_NCYLINDER', text="")
        sub.operator("surface.primitive_nurbs_surface_sphere_add", icon='SURFACE_NSPHERE', text="")
        sub.operator("surface.primitive_nurbs_surface_torus_add", icon='SURFACE_NTORUS', text="")
        #row.menu("INFO_MT_surface_add", text="Add")


# ------------------------------------------------------------
# Selection Surface  ######------------------------------------------------------------
# Selection Surface  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_selectioncurv:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selectioncurv", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selectioncurv", text="", icon='TRIA_RIGHT')

        row.label("Select...")
        row.operator("view3d.select_circle", text="", icon="BORDER_RECT")

        if lt.display_selectioncurv:
            col = layout.column(align=True)
            box = col.column(align=True).box().column(True)
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("curve.select_row", text="Control Point")
            row.operator("curve.select_all", "(De)select").action = 'TOGGLE'

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("curve.select_random", text="Random")
            row.operator("curve.select_nth", text="Checker")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("curve.select_linked", text="Linked")
            row.operator("curve.select_all", text="Inverse").action = 'INVERT'

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)

            if lt.display_selectsum:
                row.prop(lt, "display_selectsum", text="Selection Sets", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                row.prop(lt, "display_selectsum", text="Selection Sets", icon='DISCLOSURE_TRI_RIGHT_VEC')

            if lt.display_selectsum:
                sets = bpy.context.scene.selection_sets
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.template_list("SelectionSetsSetList", "sets", bpy.context.scene, "selection_sets", bpy.context.scene, "selection_sets_active")

                row = col_top.row(align=True)
                row.operator("selset.add_set", icon='ZOOMIN', text="")
                row.operator("selset.rem_set", icon='ZOOMOUT', text="")

                row = col_top.row(align=True)
                row.label("Items")

                row = col_top.row(align=True)

                index = bpy.context.scene.selection_sets_active
                if index > len(sets) - 1:
                    index = len(sets) - 1

                if index >= 0:
                    row.template_list("UI_UL_list", "items", sets[index], "set", bpy.context.scene, "selection_sets_item")

                row = col_top.row(align=True)
                row.operator("selset.add_item", icon='ZOOMIN', text="")
                row.operator("selset.rem_item", icon='ZOOMOUT', text="")


# ------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_orientedm:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orientedm", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orientedm", text="", icon='TRIA_RIGHT')

        row.label("Orientation...")
        op = row.operator("object.align_tools", text="", icon="ROTATE")

        if lt.display_orientedm:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)


# Pivot Point  ######-----------------------------------------------------------
# Pivot Point  ######------------------------------------------------------------

            row = col_top.row(align=True)
            sub = row.row()
            sub.scale_x = 2.0
            sub.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
            sub.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
            sub.operator("view3d.pivot_active", "", icon="ROTACTIVE")
            sub.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
            sub.operator("view3d.pivot_median", "", icon="ROTATECENTER")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.loops1", text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="MZ", icon='ARROW_LEFTRIGHT')

            row = col_top.row(align=True)
            row.operator("mesh.face_align_x", "FX", icon='TRIA_RIGHT')
            row.operator("mesh.face_align_y", "FY", icon='TRIA_UP')
            row.operator("mesh.face_align_z", "FZ", icon='SPACE3')

            # ---------------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.loops7", "Ob-Mode", icon="OBJECT_DATAMODE")
            row.operator("object.loops9", "Ed-Mode", icon="EDITMODE_HLT")

            row = col_top.row(align=True)
            row.operator("view3d.snap_cursor_to_center", "", icon="OUTLINER_DATA_EMPTY")
            row.operator("view3d.snap_cursor_to_active", "", icon="PMARKER")
            row.menu("mtk_snaptocursor", " > Cursor to... ")

            row = col_top.row(align=True)
            row.operator("view3d.snap_selected_to_cursor", "", icon="RESTRICT_SELECT_OFF").use_offset = False
            row.operator("view3d.snap_selected_to_cursor", "", icon="STICKY_UVS_VERT").use_offset = True
            row.menu("mtk_snaptoselect", " > Selection to... ")


# ------------------------------------------------------------
# Editing  ######------------------------------------------------------------
# Editing  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_edit:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_edit", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_edit", text="", icon='TRIA_RIGHT')

        row.label("Editing...")
        op = row.operator("curve.cyclic_toggle", text="", icon="OUTLINER_DATA_CURVE")

        if lt.display_edit:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("curve.split", text="Split")
            row.operator("curve.make_segment", text="Segment")

            row = col_top.row(align=True)
            row.operator("curve.subdivide", text="1").number_cuts = 1
            row.operator("curve.subdivide", text="2").number_cuts = 2
            row.operator("curve.subdivide", text="3").number_cuts = 3
            row.operator("curve.subdivide", text="4").number_cuts = 4
            row.operator("curve.subdivide", text="5").number_cuts = 5
            row.operator("curve.subdivide", text="6").number_cuts = 6

            row = col_top.row(align=True)
            row.operator("curve.switch_direction")

# -------------------------------------------------------
# Shading  #######-------------------------------------------------------
# Shading  #######-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        if lt.display_shading:
            ###space2###
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_RIGHT')

        row.label("Visual...")
        op = row.operator("object.wire_all", text="", icon='WIRE')

        ###space1###
        if lt.display_shading:
            col = layout.column(align=True)
            ###space2###
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("wm.context_toggle", text="Xray", icon='META_CUBE').data_path = "object.show_x_ray"

            view = context.space_data
            obj = context.object

            row = col_top.row(align=True)
            row.prop(view, "use_matcap")
            if view.use_matcap:
                row = col_top.row(align=True)
                row.template_icon_view(view, "matcap_icon")

        box = layout.box()
        row = box.row(True)
        row.operator("object.editmode_toggle", text="Fast Toggle", icon="OBJECT_DATAMODE")

        #####################################
        draw_B_history_tools(context, layout)
        #####################################


######################################################################################################################################################
########--------------------#################
# Editmode Lattice  ##############################-------------------------------------------------------
# Editmode Lattice  ##############################-------------------------------------------------------
########--------------------#################
######################################################################################################################################################

class VIEW3D_LatticeEditMode(bpy.types.Panel):
    bl_category = "META"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_label = "MetaTool"
    bl_context = "lattice_edit"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_LATTICE'))

    def draw(self, context):
        lt = context.window_manager.metawindow
        layout = self.layout
        obj = context.object

# ------------------------------------------------------------
# Selection Lattice  ######-----------------------------------------------
# Selection Lattice  ######-----------------------------------------------
# ------------------------------------------------------------

        if lt.display_selectionlatt:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selectionlatt", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selectionlatt", text="", icon='TRIA_RIGHT')

        row.label("Select...")
        row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")
        row.operator("view3d.select_border", text="", icon="BORDER_RECT")
        row.menu("VIEW3D_MT_edit_lattice_showhide", "", icon="VISIBLE_IPO_ON")

        if lt.display_selectionlatt:
            col = layout.column(align=True)
            box = col.column(align=True).box().column(True)
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("lattice.select_mirror", text="Mirror")
            row.operator("lattice.select_random", text="Random")

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("lattice.select_all").action = 'TOGGLE'
            row.operator("lattice.select_all", text="Inverse").action = 'INVERT'

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("lattice.select_ungrouped", text="Ungrouped Verts")


# ------------------------------------------------------------
# Align Meta  ######------------------------------------------------------------
# Align Meta  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_alignmeta:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_alignmeta", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_alignmeta", text="", icon='TRIA_RIGHT')

        row.label("Align...")
        row.operator("lattice.make_regular", text="", icon="PARTICLE_POINT")

        if lt.display_alignmeta:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)

            row.operator("object.loops1", text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="MZ", icon='ARROW_LEFTRIGHT')

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("mesh.face_align_x", "FX", icon='TRIA_RIGHT')
            row.operator("mesh.face_align_y", "FY", icon='TRIA_UP')
            row.operator("mesh.face_align_z", "FZ", icon='SPACE3')

            row = col_top.row(align=True)
            row.operator("mesh.face_align_xy", "Xy", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy", icon='TRIA_UP_BAR')
            row.operator("mesh.face_align_xz", "Zx", icon='TRIA_LEFT_BAR')

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("lattice.flip", text="FlipX").axis = "U"
            row.operator("lattice.flip", text="FlipY").axis = "V"
            row.operator("lattice.flip", text="FlipZ").axis = "W"


# ------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_orientedm:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orientedm", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orientedm", text="", icon='TRIA_RIGHT')

        sub = row.row(1)
        sub.scale_x = 7
        sub.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
        sub.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
        sub.operator("view3d.pivot_active", "", icon="ROTACTIVE")
        sub.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
        sub.operator("view3d.pivot_median", "", icon="ROTATECENTER")

        if lt.display_orientedm:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("object.loops7", "Ob-Mode", icon="OBJECT_DATAMODE")
            row.operator("object.loops9", "Ed-Mode", icon="EDITMODE_HLT")

            ###space1###
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Cursor", icon="FORCE_FORCE")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)
            row.operator("view3d.snap_cursor_to_grid", "to Grid")
            row.operator("view3d.snap_cursor_to_active", "to Active")
            row.operator("view3d.snap_cursor_to_center", "to Center")
            row.operator("view3d.snap_cursor_to_selected", "to Selected")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Selected", icon="RESTRICT_SELECT_OFF")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)
            row.operator("view3d.snap_selected_to_grid", "to Grid")
            row.operator("view3d.snap_selected_to_cursor", "to Offset").use_offset = True
            row.operator("mesh.snapcenteroffset", " to Center")
            row.operator("view3d.snap_selected_to_cursor", "to Cursor").use_offset = False


# -------------------------------------------------------
# Shading  #######-------------------------------------------------------
# Shading  #######-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        if lt.display_shading:
            ###space2###
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_RIGHT')

        row.label("Visual...")
        row.prop(context.space_data.fx_settings, "use_ssao", text="", icon='GROUP')
        row.operator("object.wire_all", text="", icon='WIRE')

        ###space1###
        if lt.display_shading:
            col = layout.column(align=True)
            ###space2###
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("wm.context_toggle", text="Xray", icon='META_CUBE').data_path = "object.show_x_ray"

            view = context.space_data
            obj = context.object

            row = col_top.row(align=True)
            row.prop(view, "use_matcap")
            if view.use_matcap:
                row = col_top.row(align=True)
                row.template_icon_view(view, "matcap_icon")

        box = layout.box()
        row = box.row(True)
        row.operator("object.editmode_toggle", text="Object Toggle", icon="OBJECT_DATAMODE")

        #####################################
        draw_B_history_tools(context, layout)
        #####################################


######################################################################################################################################################
########---------------------#################
# Editmode Armature  ##############################-------------------------------------------------------
# Editmode Armature  ##############################-------------------------------------------------------
########---------------------#################
######################################################################################################################################################

class VIEW3D_ArmatureEditMode(bpy.types.Panel):
    bl_category = "META"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_label = "MetaTool"
    bl_context = "armature_edit"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_ARMATURE'))

    def draw(self, context):
        lt = context.window_manager.metawindow
        layout = self.layout
        obj = context.object

        col = layout.column(align=True)
        box = col.column(align=True).box().column()
        col_top = box.column(align=True)

        row = col_top.row(align=True)
        row.alignment = 'CENTER'

        row.operator("armature.bone_primitive_add", text="Single Bone", icon="BONE_DATA")


# -------------------------------------------------------
# Selection  Armature  ######------------------------------------------
# Selection  Armature  ######------------------------------------------
# -------------------------------------------------------

        if lt.display_selectionarm:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selectionarm", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selectionarm", text="", icon='TRIA_RIGHT')

        row.label("Select...")
        row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")
        row.operator("view3d.select_border", text="", icon="BORDER_RECT")
        row.menu("armature.hide_menu", "", icon="VISIBLE_IPO_ON")

        if lt.display_selectionarm:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("armature.select_mirror", text="Mirror").extend = False
            row.operator("armature.select_all", text="Inverse").action = 'INVERT'

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("armature.select_hierarchy", text="Parent").direction = 'PARENT'
            row.operator("armature.select_hierarchy", text="Child").direction = 'CHILD'

            col_top = box.column(align=True)
            row = col_top.row(align=True)

            props = row.operator("armature.select_hierarchy", text="Extend Parent")
            props.extend = True
            props.direction = 'PARENT'

            props = row.operator("armature.select_hierarchy", text="Extend Child")
            props.extend = True
            props.direction = 'CHILD'

            col_top = box.column(align=True)
            row = col_top.row(align=True)

            row.operator_menu_enum("armature.select_similar", "type", text="Similar")
            row.operator("object.select_pattern", text="Pattern...")


# ------------------------------------------------------------
# Align Bone  ######------------------------------------------------------------
# Align Bone  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_alignbone:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_alignbone", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_alignbone", text="", icon='TRIA_RIGHT')

        row.label("Align...")
        row.operator("armature.align", "", icon="COLLAPSEMENU")

        if lt.display_alignbone:

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.loops1", text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="MZ", icon='ARROW_LEFTRIGHT')

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("mesh.face_align_x", "FX", icon='TRIA_RIGHT')
            row.operator("mesh.face_align_y", "FY", icon='TRIA_UP')
            row.operator("mesh.face_align_z", "FZ", icon='SPACE3')

            row = col_top.row(align=True)
            row.operator("mesh.face_align_xy", "Xy", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy", icon='TRIA_UP_BAR')
            row.operator("mesh.face_align_xz", "Zx", icon='TRIA_LEFT_BAR')


# ------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_orientedm:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orientedm", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orientedm", text="", icon='TRIA_RIGHT')

        sub = row.row(1)
        sub.scale_x = 7
        sub.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
        sub.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
        sub.operator("view3d.pivot_active", "", icon="ROTACTIVE")
        sub.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
        sub.operator("view3d.pivot_median", "", icon="ROTATECENTER")

        if lt.display_orientedm:

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.loops7", "Ob-Mode", icon="OBJECT_DATAMODE")
            row.operator("object.loops9", "Ed-Mode", icon="EDITMODE_HLT")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Cursor", icon="FORCE_FORCE")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)

            row.operator("view3d.snap_cursor_to_grid", "to Grid")
            row.operator("view3d.snap_cursor_to_active", "to Active")
            row.operator("mesh.snapcenteroffset", "to Offset")
            row.operator("view3d.snap_cursor_to_center", "to Center")
            row.operator("view3d.snap_cursor_to_selected", "to Selected")

            row.operator("mesh.circlecenter", text="to Circle")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Selection", icon="RESTRICT_SELECT_OFF")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)
            row.operator("view3d.snap_selected_to_grid", "to Grid")
            row.operator("view3d.snap_selected_to_cursor", "to Offset").use_offset = True
            row.operator("mesh.snapcenteroffset", " to Center")
            row.operator("view3d.snap_selected_to_cursor", "to Cursor").use_offset = False


# ------------------------------------------------------------
# Editing  ######------------------------------------------------------------
# Editing  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_bonetool:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_bonetool", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_bonetool", text="", icon='TRIA_RIGHT')

        row.label("Editing...")
        arm = context.active_object.data
        row.prop(arm, "use_mirror_x", text="", icon='X')
        #row.prop(arm, "use_mirror_x")

        if lt.display_bonetool:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("armature.subdivide", text="1").number_cuts = 1
            row.operator("armature.subdivide", text="2").number_cuts = 2
            row.operator("armature.subdivide", text="3").number_cuts = 3
            row.operator("armature.subdivide", text="4").number_cuts = 4
            row.operator("armature.subdivide", text="5").number_cuts = 5
            row.operator("armature.subdivide", text="6").number_cuts = 6

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("armature.merge", text="Merge", icon="AUTOMERGE_ON")
            row.operator("armature.split", text="Split")
            row = col_top.row(align=True)
            row.operator("armature.fill", text="Filler", icon="GROUP_BONE")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("transform.transform", text="Set Roll", icon="MAN_ROT").mode = "BONE_ROLL"
            row = col_top.row(align=True)
            row.operator("armature.calculate_roll", text="Recalculate Roll", icon="FRAME_PREV")
            row = col_top.row(align=True)
            row.operator("armature.switch_direction", icon="ARROW_LEFTRIGHT")

# -------------------------------------------------------
# Shading  #######-------------------------------------------------------
# Shading  #######-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        if lt.display_shading:
            ###space2###
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_RIGHT')

        row.label("Visual...")
        row.prop(context.space_data.fx_settings, "use_ssao", text="", icon='GROUP')
        row.operator("object.wire_all", text="", icon='WIRE')

        ###space1###
        if lt.display_shading:
            col = layout.column(align=True)
            ###space2###
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("wm.context_toggle", text="Xray", icon='META_CUBE').data_path = "object.show_x_ray"

            view = context.space_data
            obj = context.object

            row = col_top.row(align=True)
            row.prop(view, "use_matcap")
            if view.use_matcap:
                row = col_top.row(align=True)
                row.template_icon_view(view, "matcap_icon")


# Relations  #######-------------------------------------------------------
# Relations  #######-------------------------------------------------------

        if lt.display_relations:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_relations", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_relations", text="", icon='TRIA_RIGHT')

        row.label("Relations...")
        op = row.menu("VIEW3D_MT_bone_options_toggle", text="", icon="LONGDISPLAY")

        if lt.display_relations:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("armature.parent_set", text="Parent", icon="CONSTRAINT_BONE")
            row = col_top.row(align=True)
            row.operator("armature.parent_clear").type = "CLEAR"
            row = col_top.row(align=True)
            row.operator("armature.parent_clear", text="Disconnect Bone").type = "DISCONNECT"


# Auotname  ######-----------------------------------------
# Autoname  ######-----------------------------------------

        if lt.display_armname:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_armname", text="", icon='TRIA_DOWN')
        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_armname", text="", icon='TRIA_RIGHT')

        row.label("Autoname...")
        op = row.operator("armature.flip_names", text="", icon="ARROW_LEFTRIGHT")

        if lt.display_armname:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator_context = 'EXEC_AREA'
            row.operator("armature.autoside_names", text="AutoName Left/Right").type = 'XAXIS'
            row = col_top.row(align=True)
            row.operator("armature.autoside_names", text="AutoName Front/Back").type = 'YAXIS'
            row = col_top.row(align=True)
            row.operator("armature.autoside_names", text="AutoName Top/Bottom").type = 'ZAXIS'
            col_top = box.column(align=True)
            row = col_top.row(align=True)

        box = layout.box()
        row = box.row(True)
        row.operator("object.editmode_toggle", text="Object Toggle", icon="OBJECT_DATAMODE")
        row.operator("object.posemode_toggle", "Pose Toggle", icon="POSE_HLT")
        #####################################
        draw_B_history_tools(context, layout)
        #####################################


######################################################################################################################################################
########------------------#################
# Editmode MBall  ##############################-------------------------------------------------------
# Editmode MBall  ##############################-------------------------------------------------------
########------------------#################
######################################################################################################################################################

class VIEW3D_MBallEditMode(bpy.types.Panel):
    bl_category = "META"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_label = "MetaTool"
    bl_context = "mball_edit"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_METABALL'))

    def draw(self, context):
        lt = context.window_manager.metawindow
        layout = self.layout
        obj = context.object

        col = layout.column(align=True)
        box = col.column(align=True).box().column()
        col_top = box.column(align=True)

        row = col_top.row(align=True)
        row.alignment = 'CENTER'
        sub = row.row(1)
        sub.scale_x = 1.2

        sub.operator("object.metaball_add", icon='META_BALL', text="").type = "BALL"
        sub.operator("object.metaball_add", icon='META_CAPSULE', text="").type = "CAPSULE"
        sub.operator("object.metaball_add", icon='META_PLANE', text="").type = "PLANE"
        sub.operator("object.metaball_add", icon='META_ELLIPSOID', text="").type = "ELLIPSOID"
        sub.operator("object.metaball_add", icon='META_CUBE', text="").type = "CUBE"
        #row.menu("INFO_MT_metaball_add", text="Add")


# ------------------------------------------------------------
# Selection Mball  ######-------------------------------------------------
# Selection Mball  ######-------------------------------------------------
# ------------------------------------------------------------

        if lt.display_selectionball:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selectionball", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_selectionball", text="", icon='TRIA_RIGHT')

        row.label("Select...")
        row.operator("view3d.select_circle", text="", icon="BORDER_LASSO")
        row.operator("view3d.select_border", text="", icon="BORDER_RECT")
        row.menu("VIEW3D_MT_edit_meta_showhide", "", icon="VISIBLE_IPO_ON")

        if lt.display_selectionball:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator_menu_enum("mball.select_similar", "type", text="Similar")
            row.operator("mball.select_all").action = 'TOGGLE'

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("mball.select_random_metaelems", text="Random")
            row.operator("mball.select_all", text="Inverse").action = 'INVERT'

            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)

            if lt.display_selectmbm:
                row.prop(lt, "display_selectmbm", text="Selection Sets", icon='DISCLOSURE_TRI_DOWN_VEC')
            else:
                row.prop(lt, "display_selectmbm", text="Selection Sets", icon='DISCLOSURE_TRI_RIGHT_VEC')

            if lt.display_selectmbm:
                sets = bpy.context.scene.selection_sets
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.template_list("SelectionSetsSetList", "sets", bpy.context.scene, "selection_sets", bpy.context.scene, "selection_sets_active")

                row = col_top.row(align=True)
                row.operator("selset.add_set", icon='ZOOMIN', text="")
                row.operator("selset.rem_set", icon='ZOOMOUT', text="")

                row = col_top.row(align=True)
                row.label("Items")

                row = col_top.row(align=True)

                index = bpy.context.scene.selection_sets_active
                if index > len(sets) - 1:
                    index = len(sets) - 1

                if index >= 0:
                    row.template_list("UI_UL_list", "items", sets[index], "set", bpy.context.scene, "selection_sets_item")

                row = col_top.row(align=True)
                row.operator("selset.add_item", icon='ZOOMIN', text="")
                row.operator("selset.rem_item", icon='ZOOMOUT', text="")


# ------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# Orientation  ######------------------------------------------------------------
# ------------------------------------------------------------

        if lt.display_orientedm:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orientedm", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_orientedm", text="", icon='TRIA_RIGHT')

        # row.label("Orientation...")
        sub = row.row(1)
        sub.scale_x = 7
        sub.operator("view3d.pivot_bounding_box", "", icon="ROTATE")
        sub.operator("view3d.pivot_3d_cursor", "", icon="CURSOR")
        sub.operator("view3d.pivot_active", "", icon="ROTACTIVE")
        sub.operator("view3d.pivot_individual", "", icon="ROTATECOLLECTION")
        sub.operator("view3d.pivot_median", "", icon="ROTATECENTER")

        if lt.display_orientedm:
            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.loops1", text="MX", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops2", text="MY", icon='ARROW_LEFTRIGHT')
            row.operator("object.loops3", text="MZ", icon='ARROW_LEFTRIGHT')

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("mesh.face_align_x", "FX", icon='TRIA_RIGHT')
            row.operator("mesh.face_align_y", "FY", icon='TRIA_UP')
            row.operator("mesh.face_align_z", "FZ", icon='SPACE3')

            row = col_top.row(align=True)
            row.operator("mesh.face_align_xy", "Xy", icon='TRIA_RIGHT_BAR')
            row.operator("mesh.face_align_yz", "Zy", icon='TRIA_UP_BAR')
            row.operator("mesh.face_align_xz", "Zx", icon='TRIA_LEFT_BAR')


# ---------------------
# ---------------------

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator("object.loops7", "Ob-Mode", icon="OBJECT_DATAMODE")
            row.operator("object.loops9", "Ed-Mode", icon="EDITMODE_HLT")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Cursor", icon="FORCE_FORCE")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)
            row.operator("view3d.snap_cursor_to_grid", "to Grid")
            row.operator("view3d.snap_cursor_to_active", "to Active")
            row.operator("view3d.snap_cursor_to_center", "to Center")
            row.operator("view3d.snap_cursor_to_selected", "to Selected")

            col = layout.column(align=True)
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.alignment = 'CENTER'
            row.label("Set Selected", icon="RESTRICT_SELECT_OFF")

            col_top = box.column(align=True)
            row = col_top.column_flow(2)
            row.operator("view3d.snap_selected_to_grid", "to Grid")
            row.operator("view3d.snap_selected_to_cursor", "to Offset").use_offset = True
            row.operator("mesh.snapcenteroffset", " to Center")
            row.operator("view3d.snap_selected_to_cursor", "to Cursor").use_offset = False


# -------------------------------------------------------
# Shading  #######-------------------------------------------------------
# Shading  #######-------------------------------------------------------
# -------------------------------------------------------

        ###space1###
        #col = layout.column(align=True)
        if lt.display_shading:
            ###space2###
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_DOWN')

        else:
            box = layout.box()
            row = box.row()
            row.prop(lt, "display_shading", text="", icon='TRIA_RIGHT')

        row.label("Visual...")
        row.prop(context.space_data.fx_settings, "use_ssao", text="", icon='GROUP')
        row.operator("object.wire_all", text="", icon='WIRE')

        ###space1###
        if lt.display_shading:
            col = layout.column(align=True)
            ###space2###
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("wm.context_toggle", text="Xray", icon='META_CUBE').data_path = "object.show_x_ray"

            view = context.space_data
            obj = context.object

            row = col_top.row(align=True)
            row.prop(view, "use_matcap")
            if view.use_matcap:
                row = col_top.row(align=True)
                row.template_icon_view(view, "matcap_icon")

        box = layout.box()
        row = box.row(True)
        row.operator("object.editmode_toggle", text="Object Toggle", icon="OBJECT_DATAMODE")

        #####################################
        draw_B_history_tools(context, layout)
        #####################################


######################################################################################################################################################
#######-------------#################
#######  Sub Menus  #################
#######-------------#################
######################################################################################################################################################

# Menus Origin  #######-------------------------------------------------------
# Menus Origin  #######-------------------------------------------------------

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

######################################################################################################################################################
############-----------------------------############
############  DRAW into existing Menus   ############
############-----------------------------############
######################################################################################################################################################

# MENU for Specialmenu


class VIEW3D_MTK_toSpecial(bpy.types.Menu):
    bl_label = "to Special"

    def draw(self, context):
        layout = self.layout

        layout.menu("mtk_camview")


# Draw function for integration in menus
def menu_func(self, context):
    self.layout.menu("VIEW3D_MTK_toSpecial")  # draw menu into Specialmenu

    self.layout.separator()  # separate the follow operator


######################################################################################################################################################
############-------------------------------############
############  DROPDOWN FOR PANEL-BOX-MENU  ############
############-------------------------------############
######################################################################################################################################################

# property group containing all properties for the gui in the panel
# Dropdown Arrow ### general display properties = arrow tooltips
class DropdownMetaToolProps(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.metawindow
    """

######-----------------------#######################################################################################
######  MAIN PANEL DROPDOWN  #######################################################################################
######  MAIN PANEL DROPDOWN  #######################################################################################
######-----------------------#######################################################################################

    # 2.74
    display_transform = bpy.props.BoolProperty(name="Transform", description="Display Transform Tools", default=False)
    display_placegeom = bpy.props.BoolProperty(name="Copy & Rearrange Objects", description="Display Copy & Rearrange Objects Tools", default=False)
    display_bool = bpy.props.BoolProperty(name="Boolean, Join, Convert", description="Display Boolean, Join, Convert Tools", default=False)
    display_sgrouper = bpy.props.BoolProperty(name="SGrouper", description="Display Group Tools", default=False)
    display_bboxfront = bpy.props.BoolProperty(name="Front", description="9 Places for Origin on BBox Frontside / -Y", default=False)
    display_bboxmiddle = bpy.props.BoolProperty(name="Middle", description="9 Places for  Origin on BBox Middle / XYZ", default=False)
    display_bboxback = bpy.props.BoolProperty(name="Back", description="9 Places for  Origin on BBox Backside / +Y", default=False)
    display_modif = bpy.props.BoolProperty(name="Modifier Tools", description="Display Modifier Tools", default=False)
    display_mirrcut = bpy.props.BoolProperty(name="Auto Mirror Cut", description="Display Auto Mirror Cut Tools", default=False)
    display_alignmeta = bpy.props.BoolProperty(name="Align Metaball", description="Display Align Metaball Tools", default=False)
    display_alignbone = bpy.props.BoolProperty(name="Align Bones", description="Display Align Bone Tools", default=False)
    display_alignpose = bpy.props.BoolProperty(name="Align Pose", description="Display Align Pose Tools", default=False)
    display_snapshot = bpy.props.BoolProperty(name="SnapShot Mesh", description="Display SnapShot Mesh Tools", default=False)
    display_miraedit = bpy.props.BoolProperty(name="Mira Edit Tools", description="Display Mira Edit Tools", default=False)

    # Expand
    display_expand = bpy.props.BoolProperty(name="Expand", description="Display Editing Tools", default=False)
    display_objrename = bpy.props.BoolProperty(name="Rename", description="Display Rename Tools", default=False)
    display_objrename_adv = bpy.props.BoolProperty(name="Advance Rename", description="Display Advance Rename Tools", default=False)
    display_shading = bpy.props.BoolProperty(name="Shading", description="Display Shading Tools", default=False)
    display_bsurf = bpy.props.BoolProperty(name="Shading", description="Display Shading Tools", default=False)

    display_modif_obm = bpy.props.BoolProperty(name="Modifier", description="Display Modifier Tools", default=False)
    display_mirrcut_obm = bpy.props.BoolProperty(name="AutoMirror", description="Display AutoMirror Tools", default=False)
    display_modif_edm = bpy.props.BoolProperty(name="Modifier", description="Display Modifier Tools", default=False)
    display_mirrcut_edm = bpy.props.BoolProperty(name="AutoMirror", description="Display AutoMirrorg Tools", default=False)

    ### Align / Transfrom / Orient
    display_location = bpy.props.BoolProperty(name="Align Objects", description="Display Align Location Tools", default=False)
    display_rotation = bpy.props.BoolProperty(name="Align Objects", description="Display Align Rotation Tools", default=False)
    display_scale = bpy.props.BoolProperty(name="Align Objects", description="Display Align Scale Tools", default=False)
    display_transform = bpy.props.BoolProperty(name="Transform", description="Display Transform Tools", default=False)
    display_place = bpy.props.BoolProperty(name="Place Tools", description="Display Place Tools", default=False)
    display_orient = bpy.props.BoolProperty(name="Orientation ", description="Display Orientation Tools", default=False)
    display_orientedm = bpy.props.BoolProperty(name="Orientation ", description="Display Orientation Tools", default=False)
    display_edit = bpy.props.BoolProperty(name="Editing ", description="Display Editing Tools", default=False)

    # Selection
    display_selection = bpy.props.BoolProperty(name="Selection", description="Display Selection Tools", default=False)
    display_selectionedm = bpy.props.BoolProperty(name="Selection", description="Display Selection Tools", default=False)
    display_moreselect = bpy.props.BoolProperty(name="Additional Selection", description="Display Additional Selection Tools", default=False)
    display_moreselectedm = bpy.props.BoolProperty(name="Additional Selection", description="Display Additional Selection Tools", default=False)
    display_selectionlatt = bpy.props.BoolProperty(name="Selection", description="Display Selection Tools", default=False)
    display_selectionball = bpy.props.BoolProperty(name="Selection", description="Display Selection Tools", default=False)
    display_selectionarm = bpy.props.BoolProperty(name="Selection", description="Display Selection Tools", default=False)
    display_selectioncurv = bpy.props.BoolProperty(name="Selection", description="Display Selection Tools", default=False)
    display_selectionbezi = bpy.props.BoolProperty(name="Selection", description="Display Selection Tools", default=False)

    # Selection Sets
    display_selectobm = bpy.props.BoolProperty(name="Selection Sets", description="Display Selection Sets", default=False)
    display_selectedm = bpy.props.BoolProperty(name="Selection Sets", description="Display Selection Sets", default=False)
    display_selectcum = bpy.props.BoolProperty(name="Selection Sets", description="Display Selection Sets", default=False)
    display_selectsum = bpy.props.BoolProperty(name="Selection Sets", description="Display Selection Sets", default=False)
    display_selectmbm = bpy.props.BoolProperty(name="Selection Sets", description="Display Selection Sets", default=False)
    display_selectbom = bpy.props.BoolProperty(name="Selection Sets", description="Display Selection Sets", default=False)
    display_selectltm = bpy.props.BoolProperty(name="Selection Sets", description="Display Selection Sets", default=False)

    # Multi edit Tools
    display_multiedit = bpy.props.BoolProperty(name="Multi Edit Tools", description="Display Multi Edit Tools", default=False)

    # Geometry
    display_geometry = bpy.props.BoolProperty(name="Geometry ", description="Display Geometry Tools", default=False)
    display_geom = bpy.props.BoolProperty(name="Geometry ", description="Display Geometry Tools", default=False)

    # Curve Tools
    display_curveinfo = bpy.props.BoolProperty(name="Curve Info", description="Display Curve Info", default=False)
    display_curveloft = bpy.props.BoolProperty(name="Curve Tools 2", description="Display Curve Tools", default=False)

    # Cad Tools
    display_cadtools = bpy.props.BoolProperty(name="CAD Tools", description="Display CAD Tools", default=False)
    display_cadedge = bpy.props.BoolProperty(name="Edge Tools", description="Display Edge Tools", default=False)
    display_tooledge = bpy.props.BoolProperty(name="Edge Tools", description="Display Edge Tools", default=False)
    display_saveedge = bpy.props.BoolProperty(name="Edge Saver Tools", description="Display Edge Saver Tools / Create VertexGroups", default=False)
    display_intersectedge = bpy.props.BoolProperty(name="Intersection", description="Display Intersection Tools", default=False)
    display_extrude = bpy.props.BoolProperty(name="Extrude", description="Display Extrude Tools", default=False)
    display_normals = bpy.props.BoolProperty(name="Normals", description="Display Normal Tools", default=False)
    display_alignbox = bpy.props.BoolProperty(name="Align Direction", description="Display Align Direction Tools", default=False)
    display_rotface = bpy.props.BoolProperty(name="Rotate Face", description="Display Rotate Face Setup", default=False)

    # Curve Tools
    display_curveinfo = bpy.props.BoolProperty(name="Curve Info", description="Display Curve Info", default=False)
    display_curveloft = bpy.props.BoolProperty(name="Curve Tools", description="Display Curve Tools", default=False)

    # Grease Pencil
    display_pencil = bpy.props.BoolProperty(name="Grease Pencil", description="Display Fast Grease Pencil Tools", default=False)

    # Shrink Retopo
    display_shrinkretop = bpy.props.BoolProperty(name="Shrink Retopo", description="Display Shrink Retopo Tools", default=False)

    # Clean Up
    display_cleanup = bpy.props.BoolProperty(name="Clean Up Mesh", description="Display Clean Up Mesh Tools", default=False)

    # Modifier Tools
    display_modifier = bpy.props.BoolProperty(name="Modifier Tools", description="Display Modifier Tools", default=False)
    display_subdiv = bpy.props.BoolProperty(name="Subdivision Level", description="Display Subdivision Level Tools", default=False)
    display_modivisual = bpy.props.BoolProperty(name="Visual", description="Display Visual Tools", default=False)
    display_mirrorcut = bpy.props.BoolProperty(name="Auto Mirror", description="Display Auto Mirror Tools", default=False)
    display_hook = bpy.props.BoolProperty(name="Hook", description="Display Hook Tools", default=False)

    # ArrayTools
    display_array = bpy.props.BoolProperty(name="Subdivision Level", description="Display Subdivision Level Tools", default=False)
    display_arraycurve = bpy.props.BoolProperty(name="Visual", description="Display Visual Tools", default=False)
    display_arraycircle = bpy.props.BoolProperty(name="Shink Retopo", description="Display Shrink Retopo Tools", default=False)

    # MaterialTools
    display_material = bpy.props.BoolProperty(name="Material Tools", description="Display Material Tools", default=False)
    display_material_edm = bpy.props.BoolProperty(name="Material Tools", description="Display Material Tools", default=False)
    display_matoption = bpy.props.BoolProperty(name="Material Option", description="Display Material Option", default=False)
    display_matclean = bpy.props.BoolProperty(name="Clean Material", description="Display Clean Material Tools", default=False)
    display_matwireset = bpy.props.BoolProperty(name="Wireset", description="Display Wireset Tools", default=False)
    display_matrandom = bpy.props.BoolProperty(name="Random Face", description="Display Random Face Tools", default=False)
    display_node = bpy.props.BoolProperty(name="Random Face", description="Display Random Face Tools", default=False)

    # Scene Tools
    display_nav = bpy.props.BoolProperty(name="Navigation", description="Display Navigation Tools", default=False)
    displa_view = bpy.props.BoolProperty(name="3D View", description="Display 3D View Tools", default=False)
    display_cam = bpy.props.BoolProperty(name="Camera View", description="Display Camera & View Tools", default=False)
    display_light = bpy.props.BoolProperty(name="Lightning", description="Display Lightning Tools", default=False)
    display_anim = bpy.props.BoolProperty(name="Animation", description="Display Animation Tools & Key Mover in Timeline ", default=False)
    display_render = bpy.props.BoolProperty(name="Animation", description="Display Animation Tools & Key Mover in Timeline ", default=False)

    # CopyTool
    display_copy = bpy.props.BoolProperty(name="Copy Tools", description="Display Copy Tools", default=False)
    display_copy_edm = bpy.props.BoolProperty(name="Copy Tools", description="Display Copy Tools", default=False)

    # Relations
    display_relations = bpy.props.BoolProperty(name="Subdivision Level", description="Display Subdivision Level Tools", default=False)
    display_relagroup = bpy.props.BoolProperty(name="Visual", description="Display Visual Tools", default=False)
    display_relaparent = bpy.props.BoolProperty(name="Shink Retopo", description="Display Shrink Retopo Tools", default=False)
    display_relaconstraint = bpy.props.BoolProperty(name="Node Preset", description="Display Node Preset Tools", default=False)

    # Im-& Export Tools
    display_imexfolder = bpy.props.BoolProperty(name="Production Folder Tools", description="Display Production Folder Tools", default=False)
    display_imexport = bpy.props.BoolProperty(name="Im-& Export Tools", description="Display Im-& Export Tools", default=False)
    display_imexmanage = bpy.props.BoolProperty(name="Pack & Pathes Tools", description="Display Pack & Pathes Tools", default=False)

    # Delete & Clear Tools
    display_delete = bpy.props.BoolProperty(name="Delete & Clear Tools", description="Display Delete & Clear Tools", default=False)

    # UV Unwrap Tools
    display_unwrap = bpy.props.BoolProperty(name="UV Unwrap", description="Display UV Unwrap Tools", default=False)
    display_uvut = bpy.props.BoolProperty(name="UV Utility", description="Display UV Utility Tools", default=False)
    display_uvsure = bpy.props.BoolProperty(name="SureUVW", description="Display SureUVW Tools", default=False)
    display_unwrapset = bpy.props.BoolProperty(name="UV Unwrap", description="Display UV Unwrap Tools", default=False)
    display_uvnext = bpy.props.BoolProperty(name="TextureSpace / Freestyle", description="Display TextureSpace / Freestyle Tools", default=False)

    # Armature Tools
    display_bonetool = bpy.props.BoolProperty(name="Bone Tools", description="Display Bone Tools", default=False)
    display_armname = bpy.props.BoolProperty(name="Autoname", description="Display Autoname Tools", default=False)
    display_armparent = bpy.props.BoolProperty(name="Bone Groups", description="Display Bone Group Tools", default=False)

    # Pose Mode Tools
    display_posename = bpy.props.BoolProperty(name="Autoname", description="Display Autoname Tools", default=False)
    display_poseparent = bpy.props.BoolProperty(name="Bone Groups", description="Display Bone Group Tools", default=False)
    display_poserelations = bpy.props.BoolProperty(name="Pose Realtions", description="Display Pose Realtions Tools", default=False)
    display_poselib = bpy.props.BoolProperty(name="Pose Libary", description="Display Pose Libary Tools", default=False)
    display_poseclear = bpy.props.BoolProperty(name="Clear Pose", description="Display Clear Pose Tools", default=False)
    display_posebonetools = bpy.props.BoolProperty(name="Pose Tools", description="Display Pose Tools", default=False)
    display_poseselect = bpy.props.BoolProperty(name="Pose Selection", description="Display Pose Selection Tools", default=False)
    display_pose_anim = bpy.props.BoolProperty(name="Animation", description="Display Animation Tools & Key Mover in Timeline ", default=False)

    # Weight
    display_weight = bpy.props.BoolProperty(name="Weight Tools", description="Display Weight Tools", default=False)

    # Extension
    display_extension = bpy.props.BoolProperty(name="Additional Panels", description="Display Additional Panel", default=False)

    # 1d Script
    display_align = bpy.props.BoolProperty(name="Align Edges", description="Display Align Edges Tools", default=False)
    display_1d = bpy.props.BoolProperty(name="1D Align Tool", description="Display 1D Align Tools", default=False)
    display_offset = bpy.props.BoolProperty(name="SideShift", description="Display SideShift Tools", default=False)
    display = bpy.props.BoolProperty(name='display')
    display_3dmatch = bpy.props.BoolProperty(name='display_3dmatch')
    disp_cp = bpy.props.BoolProperty(name='disp_cp', default=False)
    disp_cp_project = bpy.props.BoolProperty(name='disp_cp_project', default=False)
    disp_cp_filter = bpy.props.BoolProperty(name='disp_cp_filter', default=False)
    disp_matExtrude = bpy.props.BoolProperty(name='disp_matExtrude', default=False)


######---------------------#######################################################################################
######  TAB POLL DROPDOWN  #######################################################################################
######  TAB POLL DROPDOWN  #######################################################################################
######---------------------#######################################################################################

    # TAB Align
    display_tab_add = bpy.props.BoolProperty(name="Add Tools", description="Display Add Tools", default=False)
    display_tab_multiedit = bpy.props.BoolProperty(name="Multi Edit Tools", description="Display Multi Edit Tools", default=False)

    # TAB ARRAY
    display_tab_array = bpy.props.BoolProperty(name="Subdivision Level", description="Display Subdivision Level Tools", default=False)
    display_tab_arraycurve = bpy.props.BoolProperty(name="Visual", description="Display Visual Tools", default=False)
    display_tab_arraycircle = bpy.props.BoolProperty(name="Shink Retopo", description="Display Shrink Retopo Tools", default=False)

    # TAB CAD
    display_tab_cadtools = bpy.props.BoolProperty(name="CAD Tools", description="Display CAD Tools", default=False)
    display_tab_rotface = bpy.props.BoolProperty(name="Rotate Face", description="Display Rotate Face Setup", default=False)
    display_tab_extrude = bpy.props.BoolProperty(name="Extrude", description="Display Extrude Tools", default=False)
    display_tab_intersectedge = bpy.props.BoolProperty(name="Intersection", description="Display Intersection Tools", default=False)
    display_tab_cadedge = bpy.props.BoolProperty(name="Edge Tools", description="Display Edge Tools", default=False)
    display_tab_tooledge = bpy.props.BoolProperty(name="Edge Tools", description="Display Edge Tools", default=False)
    display_tab_alignbox = bpy.props.BoolProperty(name="Align Direction", description="Display Align Direction Tools", default=False)

    # Shrink Retopo
    display_tab_shrinkretop = bpy.props.BoolProperty(name="Shrink Retopo", description="Display Shrink Retopo Tools", default=False)

    # Normals
    display_tab_normals = bpy.props.BoolProperty(name="Normals", description="Display Normal Tools", default=False)

    # TAB Material
    display_tab_material = bpy.props.BoolProperty(name="Material Tools", description="Display Material Tools", default=False)
    display_tab_matoption = bpy.props.BoolProperty(name="Material Option", description="Display Material Option", default=False)
    display_tab_matclean = bpy.props.BoolProperty(name="Clean Material", description="Display Clean Material Tools", default=False)
    display_tab_matwireset = bpy.props.BoolProperty(name="Wireset", description="Display Wireset Tools", default=False)
    display_tab_matrandom = bpy.props.BoolProperty(name="Random Face", description="Display Random Face Tools", default=False)
    display_tab_node = bpy.props.BoolProperty(name="Random Face", description="Display Random Face Tools", default=False)

    # TAB Modifier
    display_tab_modifier = bpy.props.BoolProperty(name="Modifier Tools", description="Display Modifier Tools", default=False)
    display_tab_subdiv = bpy.props.BoolProperty(name="Subdivision Level", description="Display Subdivision Level Tools", default=False)
    display_tab_modvisual = bpy.props.BoolProperty(name="Visualisation", description="Display Visualisation Tools", default=False)
    display_tab_mirrorcut = bpy.props.BoolProperty(name="Auto Mirror", description="Display Auto Mirror Tools", default=False)
    display_tab_hook = bpy.props.BoolProperty(name="Hook", description="Display Hook Tools", default=False)

    # TAB Relations
    display_tab_relations = bpy.props.BoolProperty(name="Subdivision Level", description="Display Subdivision Level Tools", default=False)
    display_tab_relagroup = bpy.props.BoolProperty(name="Visual", description="Display Visual Tools", default=False)
    display_tab_relaparent = bpy.props.BoolProperty(name="Shink Retopo", description="Display Shrink Retopo Tools", default=False)
    display_tab_relaconstraint = bpy.props.BoolProperty(name="Node Preset", description="Display Node Preset Tools", default=False)

    # Im-& Export Tools
    display_tab_imexfolder = bpy.props.BoolProperty(name="Production Folder Tools", description="Display Production Folder Tools", default=False)
    display_tab_imexport = bpy.props.BoolProperty(name="Im-& Export Tools", description="Display Im-& Export Tools", default=False)
    display_tab_imexmanage = bpy.props.BoolProperty(name="Pack & Pathes Tools", description="Display Pack & Pathes Tools", default=False)

    # Delete & Clear Tools
    display_tab_delete = bpy.props.BoolProperty(name="Delete & Clear Tools", description="Display Delete & Clear Tools", default=False)

    # UV Unwrap Tools
    display_tab_unwrap = bpy.props.BoolProperty(name="UV Tools", description="Display UV Tools", default=False)
    display_tab_uvut = bpy.props.BoolProperty(name="UV Utility", description="Display UV Utility Tools", default=False)
    display_tab_uvsure = bpy.props.BoolProperty(name="SureUVW", description="Display SureUVW Tools", default=False)
    display_tab_unwrapset = bpy.props.BoolProperty(name="UV Unwrap", description="Display UV Unwrap Tools", default=False)
    display_tab_uvnext = bpy.props.BoolProperty(name="TextureSpace / Freestyle", description="Display TextureSpace / Freestyle Tools", default=False)

    # Scene Tools
    display_tab_nav = bpy.props.BoolProperty(name="Navigation", description="Display Navigation Tools", default=False)
    display_tab_view = bpy.props.BoolProperty(name="3D View", description="Display 3D View Tools", default=False)
    display_tab_cam = bpy.props.BoolProperty(name="Camera View", description="Display Camera & View Tools", default=False)
    display_tab_light = bpy.props.BoolProperty(name="Lightning", description="Display Lightning Tools", default=False)
    display_tab_anim = bpy.props.BoolProperty(name="Animation", description="Display Animation Tools & Key Mover in Timeline ", default=False)
    display_tab_render = bpy.props.BoolProperty(name="Animation", description="Display Animation Tools & Key Mover in Timeline ", default=False)

    # 1d Script
    display_tab_align = bpy.props.BoolProperty(name="Align Edges", description="Display Align Edges Tools", default=False)
    display_tab_1d = bpy.props.BoolProperty(name="1D Align Tool", description="Display 1D Align Tools", default=False)
    display_tab_offset = bpy.props.BoolProperty(name="SideShift", description="Display SideShift Tools", default=False)
    display_tab = bpy.props.BoolProperty(name='display')
    display_tab_3dmatch = bpy.props.BoolProperty(name='display_3dmatch')
    disp_cp = bpy.props.BoolProperty(name='disp_cp', default=False)
    disp_cp_project = bpy.props.BoolProperty(name='disp_cp_project', default=False)
    disp_cp_filter = bpy.props.BoolProperty(name='disp_cp_filter', default=False)
    disp_tab_matExtrude = bpy.props.BoolProperty(name='disp_matExtrude', default=False)

    ### 1d Script functions ###
    spread_x = bpy.props.BoolProperty(name='spread_x', default=False)
    spread_y = bpy.props.BoolProperty(name='spread_y', default=False)
    spread_z = bpy.props.BoolProperty(name='spread_z', default=True)
    relation = bpy.props.BoolProperty(name='relation', default=False)
    edge_idx_store = bpy.props.IntProperty(name="edge_idx_store")
    object_name_store = bpy.props.StringProperty(name="object_name_store")
    object_name_store_v = bpy.props.StringProperty(name="object_name_store_v")
    object_name_store_c = bpy.props.StringProperty(name="object_name_store_c")
    align_dist_z = bpy.props.BoolProperty(name='align_dist_z')
    align_lock_z = bpy.props.BoolProperty(name='align_lock_z')
    step_len = bpy.props.FloatProperty(name="step_len")
    vec_store = bpy.props.FloatVectorProperty(name="vec_store")
    vert_store = bpy.props.IntProperty(name="vert_store")
    coner_edge1_store = bpy.props.IntProperty(name="coner_edge1_store")
    coner_edge2_store = bpy.props.IntProperty(name="coner_edge2_store")
    active_edge1_store = bpy.props.IntProperty(name="active_edge1_store", default=-1)
    active_edge2_store = bpy.props.IntProperty(name="active_edge2_store", default=-1)
    variant = bpy.props.IntProperty(name="variant")
    instance = bpy.props.BoolProperty(name="instance")
    flip_match = bpy.props.BoolProperty(name="flip_match")

    shift_lockX = bpy.props.BoolProperty(name='shift_lockX', default=False)
    shift_lockY = bpy.props.BoolProperty(name='shift_lockY', default=False)
    shift_lockZ = bpy.props.BoolProperty(name='shift_lockZ', default=False)
    shift_copy = bpy.props.BoolProperty(name='shift_copy', default=False)
    shift_local = bpy.props.BoolProperty(name='shift_local', default=False)

    SPLIT = bpy.props.BoolProperty(name='SPLIT', default=False)
    inner_clear = bpy.props.BoolProperty(name='inner_clear', default=False)
    outer_clear = bpy.props.BoolProperty(name='outer_clear', default=False)
    fill_cuts = bpy.props.BoolProperty(name='fill_cuts', default=False)
    filter_edges = bpy.props.BoolProperty(name='filter_edges', default=False)
    filter_verts_top = bpy.props.BoolProperty(name='filter_verts_top', default=False)
    filter_verts_bottom = bpy.props.BoolProperty(name='filter_verts_bottom', default=False)

    shape_inf = bpy.props.IntProperty(name="shape_inf", min=0, max=200, default=0)
    shape_spline = bpy.props.BoolProperty(name="shape_spline", default=False)
    spline_Bspline2 = bpy.props.BoolProperty(name="spline_Bspline2", default=True)


######---------------------#######################################################################################
######  COMPLETE DROPDOWN  #######################################################################################
######  COMPLETE DROPDOWN  #######################################################################################
######---------------------#######################################################################################

    # Geoemtry
    display_cpt_geometry = bpy.props.BoolProperty(name="Geometry ", description="Display Geometry Tools", default=False)
    display_cpt_geom = bpy.props.BoolProperty(name="Geometry ", description="Display Geometry Tools", default=False)

    # Grease Pencil
    display_cpt_pencil = bpy.props.BoolProperty(name="Grease Pencil", description="Display Fast Grease Pencil Tools", default=False)
    display_cpt_bsurf = bpy.props.BoolProperty(name="Shading", description="Display Shading Tools", default=False)

    # Cad Tools
    display_cpt_cadtools = bpy.props.BoolProperty(name="CAD Tools", description="Display CAD Tools", default=False)
    display_cpt_cadedge = bpy.props.BoolProperty(name="Edge Tools", description="Display Edge Tools", default=False)
    display_cpt_tooledge = bpy.props.BoolProperty(name="Edge Tools", description="Display Edge Tools", default=False)
    display_cpt_intersectedge = bpy.props.BoolProperty(name="Intersection", description="Display Intersection Tools", default=False)
    display_cpt_extrude = bpy.props.BoolProperty(name="Extrude", description="Display Extrude Tools", default=False)
    display_cpt_normals = bpy.props.BoolProperty(name="Normals", description="Display Normal Tools", default=False)
    display_cpt_alignbox = bpy.props.BoolProperty(name="Align Direction", description="Display Align Direction Tools", default=False)
    display_cpt_rotface = bpy.props.BoolProperty(name="Rotate Face", description="Display Rotate Face Setup", default=False)

    # Curve Tools
    display_tab_curveinfo = bpy.props.BoolProperty(name="Curve Info", description="Display Curve Info", default=False)
    display_tab_curveloft = bpy.props.BoolProperty(name="Curve Tools", description="Display Curve Tools", default=False)

    # Shrink Retopo
    display_cpt_shrinkretop = bpy.props.BoolProperty(name="Shrink Retopo", description="Display Shrink Retopo Tools", default=False)

    # Clean Up
    display_cpt_cleanup = bpy.props.BoolProperty(name="Clean Up Mesh", description="Display Clean Up Mesh Tools", default=False)

    # Modifier Tools
    display_cpt_modifier = bpy.props.BoolProperty(name="Modifier Tools", description="Display Modifier Tools", default=False)
    display_cpt_subdiv = bpy.props.BoolProperty(name="Subdivision Level", description="Display Subdivision Level Tools", default=False)
    display_cpt_modivisual = bpy.props.BoolProperty(name="Visual", description="Display Visual Tools", default=False)
    display_cpt_mirrorcut = bpy.props.BoolProperty(name="Auto Mirror", description="Display Auto Mirror Tools", default=False)
    display_cpt_hook = bpy.props.BoolProperty(name="Hook", description="Display Hook Tools", default=False)

    # ArrayTools
    display_cpt_array = bpy.props.BoolProperty(name="Subdivision Level", description="Display Subdivision Level Tools", default=False)
    display_cpt_arraycurve = bpy.props.BoolProperty(name="Visual", description="Display Visual Tools", default=False)
    display_cpt_arraycircle = bpy.props.BoolProperty(name="Shink Retopo", description="Display Shrink Retopo Tools", default=False)

    # MaterialTools
    display_cpt_material = bpy.props.BoolProperty(name="Material Tools", description="Display Material Tools", default=False)
    display_cpt_material_edm = bpy.props.BoolProperty(name="Material Tools", description="Display Material Tools", default=False)
    display_cpt_matoption = bpy.props.BoolProperty(name="Material Option", description="Display Material Option", default=False)
    display_cpt_matclean = bpy.props.BoolProperty(name="Clean Material", description="Display Clean Material Tools", default=False)
    display_cpt_matwireset = bpy.props.BoolProperty(name="Wireset", description="Display Wireset Tools", default=False)
    display_cpt_matrandom = bpy.props.BoolProperty(name="Random Face", description="Display Random Face Tools", default=False)
    display_cpt_node = bpy.props.BoolProperty(name="Random Face", description="Display Random Face Tools", default=False)

    # Scene Tools
    display_cpt_nav = bpy.props.BoolProperty(name="Navigation", description="Display Navigation Tools", default=False)
    displa_cpt_view = bpy.props.BoolProperty(name="3D View", description="Display 3D View Tools", default=False)
    display_cpt_cam = bpy.props.BoolProperty(name="Camera View", description="Display Camera & View Tools", default=False)
    display_cpt_light = bpy.props.BoolProperty(name="Lightning", description="Display Lightning Tools", default=False)
    display_cpt_anim = bpy.props.BoolProperty(name="Animation", description="Display Animation Tools & Key Mover in Timeline ", default=False)
    display_cpt_render = bpy.props.BoolProperty(name="Animation", description="Display Animation Tools & Key Mover in Timeline ", default=False)

    # CopyTooly
    display_cpt_copy = bpy.props.BoolProperty(name="Copy Tools", description="Display Copy Tools", default=False)
    display_cpt_copy_edm = bpy.props.BoolProperty(name="Copy Tools", description="Display Copy Tools", default=False)

    # Relations
    display_cpt_relations = bpy.props.BoolProperty(name="Subdivision Level", description="Display Subdivision Level Tools", default=False)
    display_cpt_relagroup = bpy.props.BoolProperty(name="Visual", description="Display Visual Tools", default=False)
    display_cpt_relaparent = bpy.props.BoolProperty(name="Shink Retopo", description="Display Shrink Retopo Tools", default=False)
    display_cpt_relaconstraint = bpy.props.BoolProperty(name="Node Preset", description="Display Node Preset Tools", default=False)

    # Im-& Export Tools
    display_cpt_imexfolder = bpy.props.BoolProperty(name="Production Folder Tools", description="Display Production Folder Tools", default=False)
    display_cpt_imexport = bpy.props.BoolProperty(name="Im-& Export Tools", description="Display Im-& Export Tools", default=False)
    display_cpt_imexmanage = bpy.props.BoolProperty(name="Pack & Pathes Tools", description="Display Pack & Pathes Tools", default=False)

    # Delete & Clear Tools
    display_cpt_delete = bpy.props.BoolProperty(name="Delete & Clear Tools", description="Display Delete & Clear Tools", default=False)

    # UV Unwrap Tools
    display_cpt_unwrap = bpy.props.BoolProperty(name="UV Unwrap", description="Display UV Unwrap Tools", default=False)
    display_cpt_uvut = bpy.props.BoolProperty(name="UV Utility", description="Display UV Utility Tools", default=False)
    display_cpt_uvsure = bpy.props.BoolProperty(name="SureUVW", description="Display SureUVW Tools", default=False)
    display_cpt_unwrapset = bpy.props.BoolProperty(name="UV Unwrap", description="Display UV Unwrap Tools", default=False)
    display_cpt_uvnext = bpy.props.BoolProperty(name="TextureSpace / Freestyle", description="Display TextureSpace / Freestyle Tools", default=False)

    # Weight
    display_cpt_weight = bpy.props.BoolProperty(name="Weight Tools", description="Display Weight Tools", default=False)

    # Extension
    display_cpt_extension = bpy.props.BoolProperty(name="Additional Panels", description="Display Additional Panel", default=False)

    # 1d Script
    display_cpt_align = bpy.props.BoolProperty(name="Align Edges", description="Display Align Edges Tools", default=False)
    display_cpt_1d = bpy.props.BoolProperty(name="1D Align Tool", description="Display 1D Align Tools", default=False)
    display_cpt_offset = bpy.props.BoolProperty(name="SideShift", description="Display SideShift Tools", default=False)
    display_cpt_spread = bpy.props.BoolProperty(name='display spread loop')
    display_cpt_3dmatch = bpy.props.BoolProperty(name='display_cpt_3dmatch')
    disp_cpt = bpy.props.BoolProperty(name='disp_cp', default=False)
    disp_cpt_project = bpy.props.BoolProperty(name='disp_cp_project', default=False)
    disp_cpt_filter = bpy.props.BoolProperty(name='disp_cp_filter', default=False)
    disp_cpt_matExtrude = bpy.props.BoolProperty(name='disp_matExtrude', default=False)


######################################################################################################################################################
############------------############
############  REGISTER  ############
############------------############
######################################################################################################################################################


# define all classes for registration
classes = [DropdownMetaToolProps,

           # add to existing Menu
           VIEW3D_MTK_toSpecial,

           # Objectmode
           VIEW3D_ObjectMode,
           VIEW3D_SculptMask,
           VIEW3D_VertexPaint,
           VIEW3D_WeightPaint,
           VIEW3D_PosePanel,

           # Editmode
           VIEW3D_EditMode,
           VIEW3D_CurveEditMode,
           VIEW3D_SurfaceEditmode,
           VIEW3D_LatticeEditMode,
           VIEW3D_ArmatureEditMode,
           VIEW3D_MBallEditMode,
           ]


# registering and menu integration
def register():
    for c in classes:
        bpy.utils.register_class(c)  # register for all class in classes

    bpy.types.VIEW3D_MTK_toSpecial.prepend(menu_func)  # class id of Specialmenu

    bpy.types.WindowManager.metawindow = bpy.props.PointerProperty(type=DropdownMetaToolProps)


# unregistering and removing menus
def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)  # unregister for all class in classes

    bpy.types.VIEW3D_MTK_toSpecial.remove(menu_func)  # class id of Specialmenu

    try:
        del bpy.types.WindowManager.metawindowtool
    except:
        pass


if __name__ == "__main__":
    register()
