"""
Pie toggle template.

This file contains the basic file structure and order for togglable menu types,
between classic list-style and modern pie-style menus.
"""

# Docstrings
"""
Quick, single line description.

In-depth description of the module or addon.
"""

# bl_info dictionary
bl_info = {
    "name": "",
    "description": "",
    "author": "",
    "version": "",
    "blender": "",
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": ""
    }

# import
import bpy
import bpy.ops

# from import
from bpy.types import Menu
from bpy.props import (
    BoolProperty, IntProperty, FloatProperty,
    StringProperty, EnumProperty
    )  # etc


# list-style classes here
class ListStyleMenu(Menu):
    """Docstring."""

    bl_label = "Menu Name"
    # bl_idname = "operator.name"  # Menu subtypes must not have bl_idname

    def draw(self, context):
        layout = self.layout

        # List menu layout here


# main pie-style class here
class PieStyleMenu(Menu):
    """Docstring."""

    bl_label = "Pie Name"
    # bl_idname = "operator.name"  # Menu subtypes must not have bl_idname

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # 1 (position 4)
        pie.operator("class bl_idname here",
                     text="Visible label here",
                     icon='icon (optional)')

        # 2 (numpad 6)

        # 3 (numpad 2)

        # 4 (numpad 8)

        # 5 (numpad 7)

        # 6 (numpad 9)

        # 7 (numpad 1)

        # 8 (numpad 3)


# secondary pie-style classes (subpies) here
class SubPieMenu(Menu):
    """Docstring."""

    bl_label = "Subpie Name"

    def draw(self, context):

        # subpie layout here, same as main pie above
        pass


# operator classes here - operators are called from the pie menu entries
class OperatorClass(bpy.types.Operator):
    """Docstring."""

    bl_label = "Operator Name"
    bl_idname = "operator.name"  # Operator subtypes must have bl_idname with exactly a single period

    def execute(self, context):
        # operation here
        pass


# USER PREFERENCES

# keymap update function ((un)register keymaps based on toggle state)
def update_prefs(self, context):
    """Function to toggle keymaps and menu style."""
    wm = bpy.context.window_manager
    kc = keyconfigs.addon

    if wm.keyconfigs.addon:
        for km in addon_keymaps:
            for kmi in km.keymap_items:
                km.keymap_items.remove(kmi)

            wm.keyconfigs.addon.keymaps.remove(km)

    addon_keymaps.clear()

    if kc:
        # Pie menu keymap
        if self.use_pie_prop:
            km = wm.keyconfigs.active.keymaps['']  # Keymap category (Mesh, 3D_View, Object, etc.)

            for kmi in km.keymaps_items:  # Unregister list-style menu keymaps
                if kmi.idname == 'wm.call_menu':
                    if kmi.properties.name == "ListStyleMenu":  # List-style menu class name
                        km.keymap_items.remove(kmi)
                        break

            # Register pie keymap
            kmi = km.keymap_items.new('wm.call_menu_pie', 'KEY', 'EVENT', MODIFIERS)  # pie menu call, key, key event type (press, release), modifiers (ctrl=True, shift=True, alt=True)
            kmi.properties.name = "PieStyleMenu"

        else:
            # List menu keymap
            km = wm.keyconfigs.active.keymaps['']

            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu_pie':
                    if kmi.properties.name == "PieStyleMenu":
                        km.keymap_items.remove(kmi)
                        break

            # Register list menu
            kmi = km.keymap_items.new('wm.call_menu', 'KEY', 'EVENT', MODIFIERS)  # list menu call, key, key event type (press, release), modifiers (ctrl=True, shift=True, alt=True)
            kmi.properties.name = "ListStyleMenu"


# addon preferences class here
class AddonPreferencesClass(
        AddonPreferences,
        bpy.types.AddonPreferences,
        bpy.types.PropertyGroup):
    """Addon preferences displayed after activation. displayed under addon description."""

    bl_idname = __name__

    use_pie_prop = BoolProperty(
        name="Toggle Pie",
        description="Toggle between pie-style menu and classic list-style menu",
        default=False,
        update=update_prefs)

    def draw(self, context):
        layout = self.layout
        col = layout.column()

        col.prop(self, "use_pie_prop")


# class list
classes = [
    ListStyleMenu,
    PieStyleMenu,
    SubPieMenu,
    OperatorClass,
    AddonPreferencesClass
    ]


# addon_keymaps = []
addon_keymaps = []


# register class
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    wm = bpy.context.window_manager

    # Unregister default keymap
    km = wm.keyconfigs.active.keymaps['']  # Keymap category (Mesh, Object, etc.)
    for kmi in km.keymap_items:
        if kmi.idname == 'wm.call_menu':
            if kmi.properties.name == "ORIGINAL_FUNCTION_NAME":
                km.keymap_items.remove(kmi)
                break

    # Register list menu keymap as new default, to be toggled with pie menu
    km = wm.keyconfigs.active.keymaps['']
    kmi = km.keymap_items.new('wm.call_menu', 'KEY', 'EVENT', MODIFIERS)  # list menu call, key, key event type (press, release), modifiers (ctrl=True, shift=True, alt=True)
    kmi.properties.name = "ListStyleMenu"


# unregister class
def unregister():
    for cls in classes[::-1]:
        bpy.utils.unregister_class(cls)
    wm = bpy.context.window_manager
    km = wm.keyconfigs.active.keymaps['']  # Keymap category (Mesh, Object, etc.)

    # Remove pie and list keymaps
    for kmi in km.keymap_items:
        if kmi.idname == 'wm.call_menu':
            if kmi.properties.name == "ListStyleMenu":
                km.keymap_items.remove(kmi)
                break
    for kmi in km.keymap_items:
        if kmi.idname == 'wm.call_menu_pie':
            if kmi.properties.name == "PieStyleMenu":
                km.keymap_items.remove(kmi)
                break

    # Replace default keymap
    kmi = km.keymap_items.new('wm.call_menu', 'KEY', 'EVENT', MODIFIERS)  # Original menu call, key, key event type (press, release), modifiers (ctrl=True, shift=True, alt=True)
    kmi.properties.name = "ORIGINAL_FUNCTION_NAME"


# register from text editor
if __name__ == "__main__":
    register()
