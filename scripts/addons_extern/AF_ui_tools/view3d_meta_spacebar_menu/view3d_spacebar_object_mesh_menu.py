# bl_info = {
#    "name": "Spacebar Object & Mesh",
#    "author": "Multiple Authors, mkbreuer",
#    "version": (0,1),
#    "blender": (2, 7, 2),
#    "location": "3D View",
#    "description": "",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "User Menu"}


import bpy
from bpy import *

###########################################################################################################################################################
###########################################################################################################################################################
# Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator
# Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator ### Operator
###########################################################################################################################################################
###########################################################################################################################################################


# WireAll  ######-------------------------------------------------------
# WireAll  ######-------------------------------------------------------

class WireAll(bpy.types.Operator):
    bl_idname = "object.wireall"
    bl_label = "Wire All"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        for obj in bpy.data.objects:
            if obj.show_wire:
                obj.show_all_edges = False
                obj.show_wire = False
            else:
                obj.show_all_edges = True
                obj.show_wire = True
        return {'FINISHED'}

bpy.utils.register_class(WireAll)


# Mesh Overlay  ######-------------------------------------------------------
# Mesh Overlay  ######-------------------------------------------------------

class MeshOverlays(bpy.types.Menu):
    bl_label = "Mesh Display: Overlays"
    bl_idname = "meshoverlays"

    def draw(self, context):
        layout = self.layout

        with_freestyle = bpy.app.build_options.freestyle

        mesh = context.active_object.data
        scene = context.scene

        layout.prop(mesh, "show_faces", text="Faces")
        layout.prop(mesh, "show_edges", text="Edges")
        layout.prop(mesh, "show_edge_crease", text="Creases")
        layout.prop(mesh, "show_weight", text="Weights")

        if with_freestyle:
            layout.prop(mesh, "show_edge_seams", text="Seams")

        if not with_freestyle:
            layout.prop(mesh, "show_edge_seams", text="Seams")

        layout.prop(mesh, "show_edge_sharp", text="Sharp")
        layout.prop(mesh, "show_edge_bevel_weight", text="Bevel")

        if with_freestyle:
            layout.prop(mesh, "show_freestyle_edge_marks", text="Edge Marks")
            layout.prop(mesh, "show_freestyle_face_marks", text="Face Marks")

        if bpy.app.debug:
            layout.prop(mesh, "show_extra_indices")

bpy.utils.register_class(MeshOverlays)


# Material  ######-------------------------------------------------------
# Material  ######-------------------------------------------------------

class NewObjMaterial(bpy.types.Operator):
    """add a new material and enable color object in options"""
    bl_idname = "mat.newmaterial"
    bl_label = "add Material"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.assign_material()
        bpy.context.object.active_material.use_object_color = True

        return {'FINISHED'}

bpy.utils.register_class(NewObjMaterial)


class VIEW3D_OT_material_remove(bpy.types.Operator):
    """Remove material slots from active objects"""
    bl_idname = "view3d.material_remove"
    bl_label = "Remove All Material Slots)"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        remove_materials()
        return {'FINISHED'}

bpy.utils.register_class(VIEW3D_OT_material_remove)


#############################################################################################################################################################
#############################################################################################################################################################
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ### Main Menu ###
#############################################################################################################################################################
#############################################################################################################################################################


# Object Display Menu  ######-------------------------------------------------------
# Object Display Menu  ######-------------------------------------------------------

class VIEW3D_Space_Object(bpy.types.Menu):
    bl_label = "Object & Mesh"
    bl_idname = "space_object"

    def draw(self, context):
        layout = self.layout

        # Display Object
        obj = context.object
        obj_type = obj.type
        is_geometry = (obj_type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'})
        is_wire = (obj_type in {'CAMERA', 'EMPTY'})
        is_empty_image = (obj_type == 'EMPTY' and obj.empty_draw_type == 'IMAGE')
        is_dupli = (obj.dupli_type != 'NONE')

        # Data
        mesh = context.active_object.data

        # Editmode
        if obj and obj.mode == 'EDIT':

            layout.operator("wm.context_toggle", text="Limit to Visible", icon="ORTHO").data_path = "space_data.use_occlude_geometry"
            layout.menu("meshoverlays", icon="RETOPO")

            layout.separator()

            layout.prop(mesh, "show_extra_edge_angle", text="Edge Angle Info")
            layout.prop(mesh, "show_extra_edge_length", text="Edge Length Info")

            layout.separator()

            layout.prop(mesh, "show_extra_face_area", text="Face Area Info")
            layout.prop(mesh, "show_extra_face_angle", text="Face Angle Info")

            layout.separator()

        layout.prop(obj, "show_axis", text="Axis")
        layout.prop(obj, "show_name", text="Name")

        layout.operator("object.wireall", text="Wire all", icon="CHECKBOX_DEHLT")

        if is_geometry or is_dupli:
            layout.prop(obj, "show_wire", text="Wire")
        if obj_type == 'MESH' or is_dupli:
            layout.prop(obj, "show_all_edges")

        layout.prop(obj, "show_x_ray", text="X-Ray")

        if obj and obj.mode == 'OBJECT':
            if obj_type == 'MESH' or is_empty_image:
                layout.prop(obj, "show_transparent", text="Transparency")

        layout.separator()

        if obj and obj.mode == 'OBJECT':
            layout.prop(obj, "show_bounds", text="Bounds")
            layout.prop(obj, "draw_bounds_type", text="", icon="BBOX")

            layout.separator()

        if is_geometry:
            layout.prop(obj, "show_texture_space", text="Texture Space")

        if is_wire:
            # wire objects only use the max. draw type for duplis
            layout.active = is_dupli
            layout.label(text="Maximum Dupli Draw Type:")
        else:
            layout.label(text="Maximum Draw Type:")

        layout.prop(obj, "draw_type", text="", icon="BRUSH_DATA")

        layout.separator()

        layout.operator("mat.newmaterial", text="New Material", icon="STYLUS_PRESSURE")
        layout.operator("view3d.material_remove", text="Delete All Materials")

        if is_geometry or is_empty_image:
            # Only useful with object having faces/materials...

            layout.label(text="Object Color:", icon="COLOR")
            layout.prop(obj, "color", text="")

        layout.separator()

        layout.prop(mesh, "show_double_sided", text="Normals: Double Sided")
        layout.prop(mesh, "use_auto_smooth", text="Normals: Auto Smooth")
        #layout.active = mesh.use_auto_smooth
        layout.prop(mesh, "auto_smooth_angle", text="Auto Smooth Angle")


###########################################################################################################################################################
###########################################################################################################################################################
# Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register
# Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register ### Register
###########################################################################################################################################################
###########################################################################################################################################################

def register():

    bpy.utils.register_class(VIEW3D_Space_Object)

    # bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_class(VIEW3D_Space_Object)

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_Space_Object.bl_idname)
