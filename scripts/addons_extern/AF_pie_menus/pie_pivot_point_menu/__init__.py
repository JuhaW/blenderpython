
bl_info = {
    "name": "Pivot Point: Key: 'Alt Q' ",
    "description": "Pivot Point Menu",
    "author": "pitiwazou, meta-androcto",
    "version": (0, 1, 0),
    "blender": (2, 77, 0),
    "location": "Alt Q",
    "warning": "",
    "wiki_url": "",
    "category": "Pie"
}

import bpy
from .utils import AddonPreferences, SpaceProperty
from bpy.types import Menu, Header
from bpy.props import IntProperty, FloatProperty, BoolProperty
import rna_keymap_ui

class PivotPointVariable(bpy.types.Operator):
    bl_idname = "pivotpoint.variable"
    bl_label = "PivotPointVariable"
    bl_options = {'REGISTER', 'UNDO'}
    variable = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.context.space_data.pivot_point = self.variable
        return {'FINISHED'}


class UsePivotAlign(bpy.types.Operator):
    bl_idname = "use.pivotalign"
    bl_label = "Use Pivot Align"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if bpy.context.space_data.use_pivot_point_align == (False):
            bpy.context.space_data.use_pivot_point_align = True
        elif bpy.context.space_data.use_pivot_point_align == (True):
            bpy.context.space_data.use_pivot_point_align = False
        return {'FINISHED'}
# Pie Pivot Point
class PiePivotPoint(Menu):
    bl_idname = "pie.pivotpoint"
    bl_label = "Pie Pivot Point"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # 4 - LEFT
        pie.operator("pivotpoint.variable", text="Active Element", icon='ROTACTIVE').variable = 'ACTIVE_ELEMENT'
        # 6 - RIGHT
        pie.operator("pivotpoint.variable", text="Median Point", icon='ROTATECENTER').variable = 'MEDIAN_POINT'
        # 2 - BOTTOM
        pie.operator("pivotpoint.variable", text="Individual Origins", icon='ROTATECOLLECTION').variable = 'INDIVIDUAL_ORIGINS'
        # 8 - TOP
        pie.operator("pivotpoint.variable", text="Cursor", icon='CURSOR').variable = 'CURSOR'
        # 7 - TOP - LEFT
        pie.operator("pivotpoint.variable", text="Bounding Box Center", icon='ROTATE').variable = 'BOUNDING_BOX_CENTER'
        # 9 - TOP - RIGHT
        pie.operator("use.pivotalign", text="Use Pivot Align", icon='ALIGN')
        # 1 - BOTTOM - LEFT
        # 3 - BOTTOM - RIGHT



classes = [
    PiePivotPoint,
    PivotPointVariable,
    UsePivotAlign,
    ]  

addon_keymaps = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    wm = bpy.context.window_manager

    if wm.keyconfigs.addon:
        # Pivot Point
        km = wm.keyconfigs.addon.keymaps.new(name='3D View Generic', space_type='VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'Q', 'PRESS', alt=True)
        kmi.properties.name = "pie.pivotpoint"
#        kmi.active = True
        addon_keymaps.append((km, kmi))


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    wm = bpy.context.window_manager

    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps['3D View Generic']
        for kmi in km.keymap_items:
            if kmi.idname == 'wm.call_menu_pie':
                if kmi.properties.name == "pie.pivotpoint":
                    km.keymap_items.remove(kmi)

if __name__ == "__main__":
    register()
