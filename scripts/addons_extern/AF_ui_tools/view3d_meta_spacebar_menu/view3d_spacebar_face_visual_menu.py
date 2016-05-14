# bl_info = {
#    "name": "Spacebar Face_B",
#    "author": "Multiple Authors, mkbreuer",
#    "version": (0, 1, 0),
#    "blender": (2, 7, 2),
#    "location": "View3D",
#    "description": "",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "User Menu"}


import bpy
from bpy import *


#############################################################################################################################################################
#############################################################################################################################################################
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
#############################################################################################################################################################
#############################################################################################################################################################


# Face Visual  ##################-------------------------------------------------------
# Face Visual  ##################-------------------------------------------------------

class VIEW3D_Space_Face_two_edm(bpy.types.Menu):
    bl_label = "Face Visual"
    bl_idname = "space_face_two_edm"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_MESH'))

    def draw(self, context):
        layout = self.layout
        with_freestyle = bpy.app.build_options.freestyle

        layout.operator_context = 'INVOKE_REGION_WIN'
        mesh = context.active_object.data
        scene = context.scene

        layout.operator("mesh.uvs_rotate", icon="UV_FACESEL")
        layout.operator("mesh.uvs_reverse", icon="UV_FACESEL")
        layout.operator("view3d.move_uv", text="Move UV [ALT+G]", icon="UV_FACESEL")
        layout.operator("uv.copy_uv", icon="PASTEFLIPUP")
        layout.operator("uv.paste_uv", icon="PASTEFLIPDOWN")

        layout.separator()

        # UV Map Menu
        layout.menu("VIEW3D_MT_uv_map", icon='MOD_UVPROJECT')

        layout.separator()

        layout.operator("mesh.colors_rotate")
        layout.operator("mesh.colors_reverse")

        layout.separator()

        if with_freestyle and not scene.render.use_shading_nodes:
            layout.operator("mesh.mark_freestyle_face").clear = False
            layout.operator("mesh.mark_freestyle_face", text="Clear Freestyle Face").clear = True

            layout.separator()

        layout.prop(mesh, "show_extra_face_area", text="Face Area Info", icon="INFO")
        layout.prop(mesh, "show_extra_face_angle", text="Face Angle Info", icon="INFO")


class VIEW3D_Space_Normals_edm(bpy.types.Menu):
    bl_label = "Normal Menu"
    bl_idname = "space_normal_edm"

    @classmethod
    def poll(cls, context):
        return ((context.mode == 'EDIT_MESH'))

    def draw(self, context):
        layout = self.layout
        with_freestyle = bpy.app.build_options.freestyle

        layout.operator_context = 'INVOKE_REGION_WIN'
        mesh = context.active_object.data
        scene = context.scene

        layout = self.layout
        with_freestyle = bpy.app.build_options.freestyle

        layout.operator_context = 'INVOKE_REGION_WIN'
        mesh = context.active_object.data
        scene = context.scene

        layout.operator("mesh.normals_make_consistent", text="Recalculate", icon="SNAP_NORMAL")
        layout.operator("mesh.normals_make_consistent", text="-> Inside").inside = True
        layout.operator("mesh.normals_make_consistent", text="-> Outside").inside = False

        layout.separator()

        layout.operator("mesh.flip_normals", icon="SNAP_NORMAL")

        layout.separator()

        layout.prop(mesh, "show_normal_vertex", text="Show Vertex", icon='VERTEXSEL')
        layout.prop(mesh, "show_normal_face", text="Show Face", icon='FACESEL')
        #layout.active = mesh.show_normal_vertex or mesh.show_normal_face
        layout.prop(context.scene.tool_settings, "normal_size", text="Normal Size")

        layout.separator()

        # Display Object
        obj = context.object
        obj_type = obj.type
        is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'})
        is_wire = (obj_type in {'CAMERA', 'EMPTY'})
        is_empty_image = (obj_type == 'EMPTY' and obj.empty_draw_type == 'IMAGE')
        is_dupli = (obj.dupli_type != 'NONE')

        # Data
        mesh = context.active_object.data

        layout.prop(mesh, "show_double_sided", text="Double Sided")
        layout.prop(mesh, "use_auto_smooth", text="Auto Smooth")
        #layout.active = mesh.use_auto_smooth
        layout.prop(mesh, "auto_smooth_angle", text="Auto Smooth Angle")


###########################################################################################################################################################
###########################################################################################################################################################
# Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register
# Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register
###########################################################################################################################################################
###########################################################################################################################################################


def register():

    bpy.utils.register_class(VIEW3D_Space_Face_two_edm)
    bpy.utils.register_class(VIEW3D_Space_Normals_edm)


def unregister():

    bpy.utils.unregister_class(VIEW3D_Space_Face_two_edm)
    bpy.utils.unregister_class(VIEW3D_Space_Normals_edm)

    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_Space_Face_two_edm.bl_idname)
