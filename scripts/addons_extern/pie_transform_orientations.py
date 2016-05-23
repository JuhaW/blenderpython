"""Replace default list-style menu for transform orientations with a pie."""

bl_info = {
    "name": "Orientation Pie",
    "author": "Italic_",
    "version": (1, 0, 0),
    "blender": (2, 77, 0),
    "description": "",
    "location": "Hotkey: ALT + Spacebar",
    "category": "Pie Menu"}


import bpy
from bpy.types import Menu, Operator


class OrientPoll(Operator):
    bl_idname = "pie.orientation"
    bl_label = "Orientation Poll"
    bl_options = {'INTERNAL'}
    space = bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.context.space_data.transform_orientation = self.space
        return {'FINISHED'}


class OrientPie(Menu):
    bl_label = "Orientation Pie"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator("pie.orientation", text="Global").space = 'GLOBAL'
        pie.operator("pie.orientation", text="Local").space = 'LOCAL'
        pie.operator("pie.orientation", text="Normal").space = 'NORMAL'
        pie.operator("pie.orientation", text="Gimbal").space = 'GIMBAL'
        pie.operator("pie.orientation", text="View").space = 'VIEW'


addon_keymaps = []


def register():
    bpy.utils.register_class(OrientPoll)
    bpy.utils.register_class(OrientPie)

    wm = bpy.context.window_manager
    if wm.keyconfigs.user:
        km = wm.keyconfigs.user.keymaps['3D View']
        kmi = km.keymap_items.new('wm.call_menu_pie', 'SPACE', 'PRESS', alt=True)
        kmi.properties.name = "OrientPie"

        for kmi in km.keymap_items:
            if kmi.idname == 'transform.select_orientation':
                km.keymap_items.remove(kmi)


def unregister():
    bpy.utils.unregister_class(OrientPie)
    bpy.utils.unregister_class(OrientPoll)

    wm = bpy.context.window_manager
    if wm.keyconfigs.user:
        km = wm.keyconfigs.user.keymaps['3D View']
        for kmi in km.keymap_items:
            if kmi.idname == 'wm.call_menu_pie' and \
                    kmi.properties.name == 'OrientPie':
                km.keymap_items.remove(kmi)

        km.keymap_items.new('transform.select_orientation', 'SPACE', 'PRESS', alt=True)


if __name__ == "__main__":
    register()
