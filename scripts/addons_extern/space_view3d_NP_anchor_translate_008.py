
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


# DESCRIPTION
#
# Translates objects using anchor and target points.
#
# Emulates the functionality of the standard 'move' command in CAD applications, with start and end points. This way, it does pretty much what the basic 'grab' function does, only it locks the snap ability to one designated point in selected group, giving more control and precision to the user.
#
# INSTALATION
#
# Two ways:
#
# A. Paste the the .py file to text editor and run (ALT+P)
# B. Unzip and place .py file to addons_contrib. In User Preferences / Addons tab search under Testing / NP Anchor Translate and check the box.
#
# Now you have the operator in your system. If you press Save User Preferences, you will have it at your disposal every time you run Bl.
#
# SHORTCUTS
#
# After succesful instalation of the addon, or it's activation from the text editor, the NP Anchor Translate operator should be registered in your system. Enter User Preferences / Input, and under that, 3DView / Object Mode. Search for definition assigned to simple M key (provided that you don't use it for placing objects into layers, instead of now almost-standard 'Layer manager' addon) and instead object.move_to_layer, type object.np_anchor_translate_xxx (xxx being the number of the version). I suggest asigning hotkey only for the Object Mode because the addon doesn't work in other modes. Also, this way the basic G command should still be available and at your disposal.
#
# USAGE
#
# Select one or more objects.
# Run operator (spacebar search - NP Anchor Translate, or keystroke if you assigned it)
# Select a point anywhere in the scene (holding CTRL enables snapping). This will be your anchor point.
# Place objects anywhere in the scene, in relation to the anchor point (again CTRL - snap).
# Middle mouse button (MMB) enables axis constraint, numpad keys enable numerical input of distance, and RMB and ESC key interrupt the operation.
#
# IMPORTANT PERFORMANCE NOTES
#
# Should be key-mapped only for Object Mode. Other modes are not supported and key definitions should not be replaced.
#
# WISH LIST
#
# Bgl overlay for snapping modes and eventualy the translate path
# Blf instructions on screen, preferably interactive
# Smarter code and faster performance
#
# WARNINGS
#
# None so far


bl_info = {
    'name': 'NP Anchor Translate 008',
    'author': 'Okavango with CoDEmanX, lukas_t, matali',
    'version': (0, 0, 8),
    'blender': (2, 71, 0),
    'location': 'View3D',
    'description': 'Translate objects using anchor and target points - install, assign shortcut, save user settings',
    'category': '3D View'}

import bpy
import bgl
import blf

# Defining the main class - the macro:


class NPAnchorTranslate008(bpy.types.Macro):
    bl_idname = 'object.np_anchor_translate_008'
    bl_label = 'NP Anchor Translate 008'
    bl_options = {'REGISTER', 'UNDO'}

# Defining the storage class that will serve as a varable-bank for exchange among the classes. Later, this bank will recieve more variables with their values for safe keeping, as the program goes on:


class Storage:
    use_snap = None
    snap_element = None
    snap_target = None

# Defining the first of the operational classes for aquiring the list of selected objects and storing them for later re-calls:


class NPATGetSelection(bpy.types.Operator):
    bl_idname = 'object.np_at_get_selection'
    bl_label = 'NP AT Get Selection'
    bl_options = {'INTERNAL'}

    def execute(self, context):
        # First, storing all of the system preferences set by the user, that will be changed during the process, in order to restore them when the operation is completed:
        Storage.use_snap = bpy.context.tool_settings.use_snap
        Storage.snap_element = bpy.context.tool_settings.snap_element
        Storage.snap_target = bpy.context.tool_settings.snap_target
        Storage.pivot_point = bpy.context.space_data.pivot_point
        Storage.trans_orient = bpy.context.space_data.transform_orientation
        # Reading and storing the selection:
        selob = bpy.context.selected_objects
        Storage.selob = selob
        # Deselecting objects in prepare for other proceses in the script:
        for ob in selob:
            ob.select = False
        return {'FINISHED'}

# Defining the operator that will add a dummy object on the original point of cursor location. 3D cursor will leave this position, go to the pointer, serve as an anchor generation location and come back, so there needs to be an object to safeguard his original position. After that, this dummy gets deleted:


class NPATAddCursorDummy(bpy.types.Operator):
    bl_idname = 'object.np_at_add_cursor_dummy'
    bl_label = 'NP AT Add Cursor Dummy'
    bl_options = {'INTERNAL'}

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        cdummy = bpy.context.object
        cdummy.name = 'NP_AT_cdummy'
        Storage.cdummy = cdummy
        # print('020')
        return{'FINISHED'}

# Defining the operator that will generate a one-vertex mesh i call anchor, at the spot marked by 3d cursor:


class NPATAddAnchor(bpy.types.Operator):
    bl_idname = 'object.np_at_add_anchor'
    bl_label = 'NP AT Add Anchor'
    bl_options = {'INTERNAL'}

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(enter_editmode=True)
        bpy.ops.mesh.select_all
        bpy.ops.mesh.delete(type='VERT')
        bpy.ops.object.mode_set(mode='OBJECT')
        anchor = bpy.context.object
        anchor.name = 'NP_AT_anchor'
        Storage.anchor = anchor
        # print('030')
        return{'FINISHED'}

# Activating dummy object for 3D cursor's return home:


class NPATActivateCursorDummy(bpy.types.Operator):
    bl_idname = 'object.np_at_activate_cursor_dummy'
    bl_label = 'NP AT Activate Cursor Dummy'
    bl_options = {'INTERNAL'}

    def execute(self, context):
        cdummy = Storage.cdummy
        bpy.context.scene.objects.active = cdummy
        Storage.cdummyloc = cdummy.location
        # print('040')
        return{'FINISHED'}

# Deleting dummy object and activating anchor for it's use in the select-point process:


class NPATActivateAnchor(bpy.types.Operator):
    bl_idname = 'object.np_at_activate_anchor'
    bl_label = 'NP AT Activate Anchor'
    bl_options = {'INTERNAL'}

    def execute(self, context):
        cdummy = Storage.cdummy
        bpy.ops.object.select_all(action='DESELECT')
        cdummy.select = True
        bpy.ops.object.delete('EXEC_DEFAULT')
        anchor = Storage.anchor
        bpy.context.scene.objects.active = anchor
        anchor.select = True
        # Preparing for the move operator, that will enable us to carry the anchor to desired point for the translation. For this, we need to enable the specific snap parameters:
        bpy.context.tool_settings.use_snap = False
        bpy.context.tool_settings.snap_element = 'VERTEX'
        bpy.context.tool_settings.snap_target = 'ACTIVE'
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'
        bpy.context.space_data.transform_orientation = 'GLOBAL'
        # print('050')
        return{'FINISHED'}

# Defining the operator that will let the user translate the anchor to the desired point. It also uses some listening operators that clean up the leftovers should the user interrupt the command. Many thanks to CoDEmanX and lukas_t:


def draw_callback_px(self, context):
    sel = bpy.context.selected_objects
    lensel = len(sel)

    if lensel == 1:
        main = 'SELECT ANCHOR POINT'

    else:
        main = 'SELECT TARGET POINT'

    font_id = 0
    bgl.glColor4f(1, 1, 1, 0.25)
    blf.size(font_id, 88, 72)
    blf.position(font_id, 5, 75, 0)
    blf.draw(font_id, 'N')
    blf.size(font_id, 28, 72)
    blf.position(font_id, 22, 75, 0)
    blf.draw(font_id, 'P')
    bgl.glColor4f(1, 1, 1, 1)
    blf.position(font_id, 75, 125, 0)
    blf.size(font_id, 16, 72)
    blf.draw(font_id, main)
    bgl.glColor4f(0, 0.5, 0, 1)
    blf.size(font_id, 11, 72)
    blf.position(font_id, 75, 105, 0)
    blf.draw(font_id, 'LMB - select, CTRL - snap')
    blf.position(font_id, 75, 90, 0)
    blf.draw(font_id, 'MMB - change axis')
    blf.position(font_id, 75, 75, 0)
    blf.draw(font_id, 'NUMPAD - value')
    bgl.glColor4f(1, 0, 0, 1)
    blf.position(font_id, 75, 55, 0)
    blf.draw(font_id, 'ESC, RMB - quit')


class NPATRunTranslate(bpy.types.Operator):
    bl_idname = 'object.np_at_run_translate'
    bl_label = 'NP AT Run Translate'
    bl_options = {'REGISTER', 'INTERNAL'}

    count = 0

    def modal(self, context, event):
        self.count += 1
        selob = Storage.selob
        anchor = Storage.anchor
        # print('080')
        if self.count == 1:
            bpy.ops.transform.translate('INVOKE_DEFAULT')
        elif event.type in ('LEFTMOUSE', 'RET', 'NUMPAD_ENTER', 'SPACE') and event.value == 'RELEASE':
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return{'FINISHED'}
        elif event.type in ('ESC', 'RIGHTMOUSE'):
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            bpy.ops.object.select_all(action='DESELECT')
            anchor.select = True
            bpy.ops.object.delete('EXEC_DEFAULT')
            for ob in selob:
                ob.select = True
            bpy.context.tool_settings.use_snap = Storage.use_snap
            bpy.context.tool_settings.snap_element = Storage.snap_element
            bpy.context.tool_settings.snap_target = Storage.snap_target
            bpy.context.space_data.pivot_point = Storage.pivot_point
            bpy.context.space_data.transform_orientation = Storage.trans_orient
            return{'CANCELLED'}
        return{'PASS_THROUGH'}

    def invoke(self, context, event):
        # print("START_____")
        args = (self, context)
        self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, args, 'WINDOW', 'POST_PIXEL')
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

# Reselecting the objects from the list of originaly selected objects:


class NPATReselectStored(bpy.types.Operator):
    bl_idname = "object.np_at_reselect_stored"
    bl_label = "NP AT Reselect Stored"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        selob = Storage.selob
        for ob in selob:
            ob.select = True
        bpy.context.tool_settings.use_snap = False
        bpy.context.tool_settings.snap_element = 'VERTEX'
        bpy.context.tool_settings.snap_target = 'ACTIVE'
        bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
        bpy.context.space_data.transform_orientation = 'GLOBAL'
        return {'FINISHED'}

# Deleting the anchor after succesfull translation:


class NPATDeleteAnchor(bpy.types.Operator):
    bl_idname = "object.np_at_delete_anchor"
    bl_label = "NP AT Delete Anchor"
    bl_options = {'INTERNAL'}

    def execute(self, context):
        selob = Storage.selob
        anchor = Storage.anchor
        bpy.ops.object.select_all(action='DESELECT')
        anchor.select = True
        bpy.ops.object.delete('EXEC_DEFAULT')
        for ob in selob:
            ob.select = True
            bpy.context.scene.objects.active = ob
        bpy.context.tool_settings.use_snap = Storage.use_snap
        bpy.context.tool_settings.snap_element = Storage.snap_element
        bpy.context.tool_settings.snap_target = Storage.snap_target
        bpy.context.space_data.pivot_point = Storage.pivot_point
        bpy.context.space_data.transform_orientation = Storage.trans_orient
        return {'FINISHED'}

# This is the actual addon process, the algorithm that defines the order of operator activation inside the main macro:


def register():
    bpy.utils.register_module(__name__)

    NPAnchorTranslate008.define('OBJECT_OT_np_at_get_selection')
    NPAnchorTranslate008.define('OBJECT_OT_np_at_add_cursor_dummy')
    NPAnchorTranslate008.define('VIEW3D_OT_cursor3d')
    NPAnchorTranslate008.define('OBJECT_OT_np_at_add_anchor')
    NPAnchorTranslate008.define('OBJECT_OT_np_at_activate_cursor_dummy')
    NPAnchorTranslate008.define('VIEW3D_OT_snap_cursor_to_active')
    NPAnchorTranslate008.define('OBJECT_OT_np_at_activate_anchor')
    NPAnchorTranslate008.define('OBJECT_OT_np_at_run_translate')
    NPAnchorTranslate008.define('OBJECT_OT_np_at_reselect_stored')
    NPAnchorTranslate008.define('OBJECT_OT_np_at_run_translate')
    NPAnchorTranslate008.define('OBJECT_OT_np_at_delete_anchor')


def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
