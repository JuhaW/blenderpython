
bl_info = {
    "name": "Mode Switch: Key: 'Tab' ",
    "description": "Switch between 3dview modes",
    "author": "pitiwazou, meta-androcto",
    "version": (0, 1, 0),
    "blender": (2, 77, 0),
    "location": "Tab key",
    "warning": "",
    "wiki_url": "",
    "category": "3D View"
}

import bpy
from ..utils import AddonPreferences, SpaceProperty
from bpy.types import Menu, Header
from bpy.props import IntProperty, FloatProperty, BoolProperty

# Define Class Object Mode
class ClassObject(bpy.types.Operator):
    bl_idname = "class.object"
    bl_label = "Class Object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode == "OBJECT":
            bpy.ops.object.mode_set(mode="EDIT")
        else:
            bpy.ops.object.mode_set(mode="OBJECT")
        return {'FINISHED'}

# Define Class Vertex
class ClassVertex(bpy.types.Operator):
    bl_idname = "class.vertex"
    bl_label = "Class Vertex"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
        if bpy.ops.mesh.select_mode != "EDGE, FACE":
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
            return {'FINISHED'}

# Define Class Edge
class ClassEdge(bpy.types.Operator):
    bl_idname = "class.edge"
    bl_label = "Class Edge"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        if bpy.ops.mesh.select_mode != "VERT, FACE":
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
            return {'FINISHED'}

# Define Class Face
class ClassFace(bpy.types.Operator):
    bl_idname = "class.face"
    bl_label = "Class Face"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
        if bpy.ops.mesh.select_mode != "VERT, EDGE":
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
            return {'FINISHED'}
# Define Class Texture Paint


class ClassTexturePaint(bpy.types.Operator):
    bl_idname = "class.pietexturepaint"
    bl_label = "Class Texture Paint"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.paint.texture_paint_toggle()
        else:
            bpy.ops.paint.texture_paint_toggle()
        return {'FINISHED'}

# Define Class Weight Paint


class ClassWeightPaint(bpy.types.Operator):
    bl_idname = "class.pieweightpaint"
    bl_label = "Class Weight Paint"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.paint.weight_paint_toggle()
        else:
            bpy.ops.paint.weight_paint_toggle()
        return {'FINISHED'}

# Define Class Vertex Paint


class ClassVertexPaint(bpy.types.Operator):
    bl_idname = "class.pievertexpaint"
    bl_label = "Class Vertex Paint"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.paint.vertex_paint_toggle()
        else:
            bpy.ops.paint.vertex_paint_toggle()
        return {'FINISHED'}

# Define Class Particle Edit


class ClassParticleEdit(bpy.types.Operator):
    bl_idname = "class.pieparticleedit"
    bl_label = "Class Particle Edit"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout

        if bpy.context.object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.particle.particle_edit_toggle()
        else:
            bpy.ops.particle.particle_edit_toggle()

        return {'FINISHED'}

# Components Selection Mode
class VertsEdges(bpy.types.Operator):
    bl_idname = "verts.edges"
    bl_label = "Verts Edges"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.context.tool_settings.mesh_select_mode = (True, True, False)
        if bpy.context.object.mode == "EDIT":
            bpy.context.tool_settings.mesh_select_mode = (True, True, False)
            return {'FINISHED'}


class EdgesFaces(bpy.types.Operator):
    bl_idname = "edges.faces"
    bl_label = "EdgesFaces"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.context.tool_settings.mesh_select_mode = (False, True, True)
        if bpy.context.object.mode == "EDIT":
            bpy.context.tool_settings.mesh_select_mode = (False, True, True)
            return {'FINISHED'}


class VertsFaces(bpy.types.Operator):
    bl_idname = "verts.faces"
    bl_label = "Verts Faces"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.context.tool_settings.mesh_select_mode = (True, False, True)
        if bpy.context.object.mode == "EDIT":
            bpy.context.tool_settings.mesh_select_mode = (True, False, True)
            return {'FINISHED'}


class VertsEdgesFaces(bpy.types.Operator):
    bl_idname = "verts.edgesfaces"
    bl_label = "Verts Edges Faces"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        layout = self.layout
        if bpy.context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.context.tool_settings.mesh_select_mode = (True, True, True)
        if bpy.context.object.mode == "EDIT":
            bpy.context.tool_settings.mesh_select_mode = (True, True, True)
            return {'FINISHED'}

# Pie Edit/Object Others modes - Tab
class PieObjectEditotherModes(Menu):
    bl_idname = "pie.objecteditmodeothermodes"
    bl_label = "Select Other Modes"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # 4 - LEFT
        pie.operator("class.pieweightpaint", text="Weight Paint", icon='WPAINT_HLT')
        # 6 - RIGHT
        pie.operator("class.pietexturepaint", text="Texture Paint", icon='TPAINT_HLT')
        # 2 - BOTTOM
        pie.operator("class.pieparticleedit", text="Particle Edit", icon='PARTICLEMODE')
        # 8 - TOP
        pie.operator("class.pievertexpaint", text="Vertex Paint", icon='VPAINT_HLT')
        # 7 - TOP - LEFT
        # 9 - TOP - RIGHT
        # 1 - BOTTOM - LEFT
        # 3 - BOTTOM - RIGHT

# Pie Vertex/Edges/Faces Modes - Tab
class PieVertexEdgesFacesModes(Menu):
    bl_idname = "pie.vertexedgesfacesmodes"
    bl_label = "Select Multi Components"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # 4 - LEFT
        pie.operator("verts.faces", text="Vertex/Faces", icon='LOOPSEL')
        # 6 - RIGHT
        pie.operator("verts.edges", text="Vertex/Edges", icon='VERTEXSEL')
        # 2 - BOTTOM
        pie.operator("verts.edgesfaces", text="Vertex/Edges/Faces", icon='OBJECT_DATAMODE')
        # 8 - TOP
        pie.operator("edges.faces", text="Edges/Faces", icon='FACESEL')
        # 7 - TOP - LEFT
        # 9 - TOP - RIGHT
        # 1 - BOTTOM - LEFT
        # 3 - BOTTOM - RIGHT

# Pie Modes Switch- Tab key
class PieObjectEditMode(Menu):
    bl_idname = "pie.objecteditmode"
    bl_label = "Select Mode"

    def draw(self, context):
        layout = self.layout
        toolsettings = context.tool_settings
        obj = context.object
        
        if obj and obj.type == 'MESH' and obj.mode in {'OBJECT'}:
            pie = layout.menu_pie()
            pie.operator_enum("OBJECT_OT_mode_set", "mode")

        ## Mesh Edit Mode ##
        if obj and obj.type == 'MESH' and obj.mode in {'EDIT'}:
            pie = layout.menu_pie()
            # 4 - LEFT
            pie.operator("class.vertex", text="Vertex", icon='VERTEXSEL')
            # 6 - RIGHT
            pie.operator("class.face", text="Face", icon='FACESEL')
            # 2 - BOTTOM
            pie.operator("class.edge", text="Edge", icon='EDGESEL')
            # 8 - TOP
            pie.operator("class.object", text="Edit/Object", icon='OBJECT_DATAMODE')
            # 7 - TOP - LEFT
            pie.operator("wm.context_toggle", text="Limit to Visible", icon="ORTHO").data_path = "space_data.use_occlude_geometry"
            # 9 - TOP - RIGHT
            pie.operator("sculpt.sculptmode_toggle", text="Sculpt", icon='SCULPTMODE_HLT')
            # 1 - BOTTOM - LEFT
            pie.operator("wm.call_menu_pie", text="Other Modes", icon='TPAINT_HLT').name = "pie.objecteditmodeothermodes"
            # 3 - BOTTOM - RIGHT
            box = pie.split().column()
            row = box.row(align=True)
            row.prop(toolsettings, "use_mesh_automerge", text="Auto Merge")
            row = box.row(align=True)
            row.operator("wm.call_menu_pie", text="V/E/F Modes", icon='UV_VERTEXSEL').name = "pie.vertexedgesfacesmodes"

        if obj and obj.type == 'CURVE':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')

        if obj and obj.type == 'ARMATURE':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit Mode", icon='OBJECT_DATAMODE')
            pie.operator("object.posemode_toggle", text="Pose", icon='POSE_HLT')
            pie.operator("class.object", text="Object Mode", icon='OBJECT_DATAMODE')

        if obj and obj.type == 'FONT':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')

        if obj and obj.type ==  'SURFACE':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')

        if obj and obj.type ==  'ARMATURE':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')

        if obj and obj.type ==  'META':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')

        if obj and obj.type ==  'LATTICE':
            pie = layout.menu_pie()
            pie.operator("object.editmode_toggle", text="Edit/Object", icon='OBJECT_DATAMODE')

classes = [
    PieObjectEditMode,
    ClassObject,
    ClassVertex,
    ClassEdge,
    ClassFace,
    PieObjectEditotherModes,
    ClassTexturePaint,
    ClassWeightPaint,
    ClassVertexPaint,
    ClassParticleEdit,
    PieVertexEdgesFacesModes,
    VertsEdges,
    EdgesFaces,
    VertsFaces,
    VertsEdgesFaces
    ]

addon_keymaps = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:
        # Select Mode
        km = wm.keyconfigs.addon.keymaps.new(name='Object Non-modal')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'TAB', 'PRESS')
        kmi.properties.name = "pie.objecteditmode"
#        kmi.active = True
        addon_keymaps.append((km, kmi))


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    wm = bpy.context.window_manager

    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps['Object Non-modal']
        for kmi in km.keymap_items:
            if kmi.idname == 'wm.call_menu_pie':
                if kmi.properties.name == "pie.objecteditmode":
                    km.keymap_items.remove(kmi)

if __name__ == "__main__":
    register()
