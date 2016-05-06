import bpy
import bmesh
from math import pi, sin, sqrt, radians, degrees
from mathutils import Vector

bl_info = {
    "name": "Circles",
    "author": "Juha Wiiala (TynkaTopi), Oren Titane (Genome36)",
    "version": (0, 1, 0),
    "blender": (2, 72, 0),
    "location": "Object",
    "description": "Create circles using a selected object and an array modifier",
    "warning": "beta",
    "wiki_url": "",
    "category": "Object",
}


def print_vert_details(selected_verts, object_reference, corners):
    num_verts = len(selected_verts)
    # print("number of verts: {}".format(num_verts))
    # print("vert indices: {}".format([id.index for id in selected_verts]))

    if num_verts == 2:

        coord = {}
        objver = object_reference.data.vertices
        ob = bpy.context.active_object
        wmtx = ob.matrix_world

        c = 0
        for id in selected_verts:
            # coord[c] = (objver[id.index].co.x*wmtx,objver[id.index].co.y *wmtx ,objver[id.index].co.z * wmtx)
            coord[c] = wmtx * objver[id.index].co
            print("coord=", c, coord[c])
            # print("id=",id,id.index)
            # print(object_reference.data.vertices[id.index].co)
            c += 1

        # print ("c=",c)
        diffx = coord[0][0] - coord[1][0]
        diffy = coord[0][1] - coord[1][1]
        # print ("diffx=",abs(diffx))
        # print ("diffy=",abs(diffy))
        middlex = (coord[0][0] + coord[1][0]) / 2
        # print ("middlex=", middlex)
        # corners = 12

        distcorner = abs(diffx / sin(pi / corners) / 2)
        distmiddle = sqrt(distcorner ** 2 - ((diffx / 2) ** 2))
        # print ("distancecorner=", distcorner)
        # print ("distancemiddle=", distmiddle)
        # SQRT(F10^2-((D10/2)^2))

        # print ("selected verts=", selected_verts)
        # objx = coord[0][0],coord[0][1],coord[0][2]
        # print ("objx=",objx)
        # print (locmat*objx)

        bpy.context.scene.cursor_location = (middlex, coord[0][1] + distmiddle, coord[0][2])

        # add an empty object
        obj = bpy.ops.object
        obj.mode_set(mode='OBJECT')
        obj.origin_set(type='ORIGIN_CURSOR')
        empty = bpy.data.objects.new("empty", None)
        emptyname = empty.name
        print("emptyname=", emptyname)
        empty.location = bpy.context.scene.cursor_location
        bpy.context.scene.objects.link(empty)

        bpy.context.scene.update()

        plane = bpy.context.scene.objects.active
        print("plane=", plane)

        bpy.ops.object.select_all(action='DESELECT')

        bpy.context.scene.objects.active = empty
        empty.select = True

        bpy.ops.transform.rotate(value=radians(360 / corners), axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        # parent
        plane.select = True
        # bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = plane
        obj = bpy.ops.object
        obj.modifier_add(type='ARRAY')
        bpy.context.object.modifiers["Array"].use_relative_offset = False
        bpy.context.object.modifiers["Array"].use_object_offset = True
        bpy.context.object.modifiers["Array"].offset_object = bpy.data.objects[emptyname]
        bpy.context.object.modifiers["Array"].count = corners
        bpy.context.object.modifiers["Array"].use_merge_vertices = True
        bpy.context.object.modifiers["Array"].use_merge_vertices_cap = True
        bpy.context.object.modifiers["Array"].show_on_cage = True

        # cempty.select = true
        bpy.context.scene.objects.active = plane
        plane.select = True

        bpy.ops.object.mode_set(mode='EDIT')
        # bpy.context.space_data.pivot_point = 'CURSOR'

        # bpy.context.scene.update()

    else:
        print("Vertex count must be 2")


class Create(bpy.types.Operator):
    bl_idname = "wm.create_spiral"
    bl_label = "Create spiral"

    def execute(self, context):
        def get_vertex_data(object_reference):
            bm = bmesh.from_edit_mesh(object_reference.data)
            selected_verts = [vert for vert in bm.verts if vert.select]
            print_vert_details(selected_verts, object_reference, context.scene.prop.corners)

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.mode_set(mode='EDIT')
        object_reference = bpy.context.active_object
        get_vertex_data(object_reference)
        # bpy.ops.object.mode_set(mode = 'OBJECT')
        return {'FINISHED'}


class RENDER_PT_publish(bpy.types.Panel):
    bl_idname = "scene.spiral"
    bl_label = "Spiral"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    # @classmethod
    # def poll(cls, context):
    #     scene = context.scene
    #     return scene and (scene.render.engine == "BLENDER_GAME")

    def draw(self, context):
        p = context.scene.prop
        layout = self.layout

        # initial options
        layout.label("Options", icon="FILE_SCRIPT")
        layout.prop(p, "corners")

        layout.operator(Create.bl_idname, "Create spiral")


class Properties(bpy.types.PropertyGroup):
    corners = bpy.props.IntProperty(
        name="Corners",
        description="Number of object in array",
        min=2,
        step=1
    )


def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.prop = bpy.props.PointerProperty(type=Properties)


def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.prop


if __name__ == "__main__":
    try:
        unregister()
    except:
        pass
    register()
