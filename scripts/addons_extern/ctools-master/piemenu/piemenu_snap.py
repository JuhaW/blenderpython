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


bl_info = {
    "name": "Snap Menu (3D View: Shift + TAB, Shift + Ctrl + TAB)",
    # "description": "",
    # "category": "User Interface"
}


from types import MethodType

import bpy

# import piemenus


def get_enum_items(obj, prop_name):
    prop = obj.bl_rna.properties[prop_name]
    return list(prop.enum_items)


class Empty:
    def __init__(self, label=""):
        self.label = label


class EmptyMenu:
    def __init__(self, context):
        pass


class SnapElement:
    idname = "snap_element"
    label = "Snap Element"
    next = "snap_target"
    radius = 0

    keymap_items = [["3D View", {"type": 'TAB', "value": 'PRESS',
                                 "shift": True}]]

    def __init__(self, context):
        self.items = []
        ToolSettings = bpy.types.ToolSettings

        enum_items = {e.identifier: e for e in
                      get_enum_items(ToolSettings, "snap_element")}
        identifiers = ['VERTEX', None, 'EDGE', None, 'FACE', 'VOLUME',
                       'INCREMENT', None]
        for identifier in identifiers:
            if identifier is None:
                self.items.append(None)
            else:
                enum_item = enum_items[identifier]
                item = Empty(enum_item.name)
                item.description = enum_item.description
                item.icon = enum_item.icon
                item.execute = "bpy.ops.wm.context_set_enum(" \
                               "data_path='tool_settings.snap_element', " \
                               "value='{}')".format(identifier)
                if identifier == 'INCREMENT':
                    item.execute += (
                        "\nbpy.ops.wm.context_set_boolean(data_path="
                        "'tool_settings.use_snap_grid_absolute', value=False)")
                self.items.append(item)

        prop = ToolSettings.bl_rna.properties["use_snap_grid_absolute"]
        item = Empty(prop.name)
        item.description = prop.description
        item.icon = prop.icon
        item.execute = (
            "bpy.ops.wm.context_set_enum("
            "data_path='tool_settings.snap_element', "
            "value='INCREMENT')\n"
            "bpy.ops.wm.context_set_boolean(data_path="
            "'tool_settings.use_snap_grid_absolute', value=True)")
        self.items[-1] = item

        item = Empty("Toggle Snap")
        prop = ToolSettings.bl_rna.properties["use_snap"]
        item.description = prop.description
        item.icon = 'SNAP_ON'
        item.execute = "wm.context_toggle(" \
                       "data_path='tool_settings.use_snap')"
        item.shortcut = 'TAB'
        self.items[1] = item


class SnapTarget:
    idname = "snap_target"
    label = "Snap Target"
    prev = "snap_element"
    item_order = 'OFFICIAL'

    keymap_items = [["3D View", {"type": 'TAB', "value": 'PRESS',
                                 "shift": True, "ctrl": True}]]

    def __init__(self, context):
        self.items = []
        for enum_item in get_enum_items(bpy.types.ToolSettings,
                                        "snap_target"):
            item = Empty(enum_item.name)
            item.description = enum_item.description
            item.icon = enum_item.icon
            item.execute = "wm.context_set_enum(" \
                           "data_path='tool_settings.snap_target', " \
                           "value='{}')".format(enum_item.identifier)
            self.items.append(item)


class Snap:
    idname = "snap"
    label = "Snap"
    item_order = 'CW6'
    # draw_type = 'BOX'
    # highlight = 'LAST'
    # highlight_index = 2
    # quick_action = 'LAST'

    keymap_items = [["3D View", {"type": 'S', "value": 'PRESS',
                                 "shift": True}]]

    def __init__(self, context):
        def add(name):
            item = Empty(name)
            self.items.append(item)
            return item

        self.menus = {}

        self.items = []
        item = add("Selection to Grid")
        # item.icon = 'GRID'
        item.icon = 'VERTEXSEL'
        item.execute = "view3d.snap_selected_to_grid"

        item = add("Selection to Cursor")
        # item.icon = 'CURSOR'
        item.icon = 'VERTEXSEL'
        item.execute = "view3d.snap_selected_to_cursor(use_offset=False)"

        item = add("Selection to Cursor (Offset)")
        # item.icon = 'CURSOR'
        item.icon = 'VERTEXSEL'
        item.execute = "view3d.snap_selected_to_cursor(use_offset=True)"

        item = add("Selection to Active")
        # item.icon = 'CURSOR'
        item.icon = 'VERTEXSEL'
        item.execute = "view3d.snap_selected_to_active"

        item = add("Cursor to Selected")
        # item.icon = 'FACESEL'
        item.icon = 'CURSOR'
        item.execute = "view3d.snap_cursor_to_selected"

        item = add("Cursor to Center")
        item.icon = "CURSOR"
        item.execute = "view3d.snap_cursor_to_center"

        item = add("Cursor to Grid")
        # item.icon = 'GRID'
        item.icon = 'CURSOR'
        item.execute = "view3d.snap_cursor_to_grid"

        item = add("Cursor to Active")
        # item.icon = 'VERTEXSEL'
        item.icon = 'CURSOR'
        item.execute = "view3d.snap_cursor_to_active"

        # if context.area.type == 'VIEW_3D':
        #     v3d = context.space_data
        #     value = v3d.use_cursor_snap_grid
        #     item = self.add_item(
        #         "Cursor Snapping -> " + ('OFF' if value else 'ON'))
        #     item.icon = 'GRID'
        #     item.execute = "wm.context_toggle(" \
        #                     "data_path='space_data.use_cursor_snap_grid')"
        # else:
        #     self.add_item(empty=True)

        try:
            import ctools.utils.unitsystem
            add_item = True
        except:
            add_item = False
        if add_item and context.mode == 'EDIT_MESH':
            item = Empty("Mesh Selection to View Grid")
            item.icon = 'VERTEXSEL'
            item.poll = "return context.mode == 'EDIT_MESH'"

            def execute(self, context):
                import bmesh
                import ctools.utils.unitsystem
                from mathutils import Matrix
                rv3d = context.region_data
                mat4 = rv3d.view_matrix.to_3x3().to_4x4()
                v3d = context.space_data
                if hasattr(v3d, "use_local_grid") and v3d.use_local_grid:
                    mat4 = mat4 * Matrix.Translation(
                        -v3d.local_grid_location)
                unit_system = ctools.utils.unitsystem.UnitSystem(context)
                actob = context.active_object
                mat = mat4 * actob.matrix_world
                imat = mat.inverted()
                bm = bmesh.from_edit_mesh(actob.data)
                for eve in (v for v in bm.verts if v.select and not v.hide):
                    co = mat * eve.co
                    co[0] = unit_system.snap_value(
                        co[0],unit_system.grid_view)
                    co[1] = unit_system.snap_value(
                        co[1], unit_system.grid_view)
                    eve.co = imat * co
                bm.normal_update()
                bmesh.update_edit_mesh(actob.data, True)
            item.execute = MethodType(execute, item)

            self.shift_items = self.items[:]
            self.shift_items[0] = item

        # Sub Menu
        try:
            import ctools._space_view3d_snap_cursor
            add_menu = True
        except:
            import traceback
            traceback.print_exc()
            add_menu = False
        if add_menu:
            menu = type("Menu", (EmptyMenu,), {})
            menu.idname = "snap_ex"
            menu.label = "Snap EX"
            menu.items = []
            menu.prev = self.idname
            self.next = menu.idname
            self.menus[menu.idname] = menu

            def add(name):
                item = Empty(name)
                menu.items.append(item)
                return item

            item = add("Cursor to Circle")
            item.icon = 'MESH_CIRCLE'
            item.execute = "view3d.snap_cursor(mode='circle')"

            item = add("Cursor to Sphere")
            item.icon = 'MESH_UVSPHERE'
            item.execute = "view3d.snap_cursor(mode='sphere')"

            item = add("Cursor to Median")
            item.icon = 'MESH_CIRCLE'
            item.execute = "view3d.snap_cursor(mode='median')"

            item = add("Cursor to Bounding Box")
            item.icon = 'ROTATE'
            item.execute = "view3d.snap_cursor(mode='boundbox')"


pie_menus = [
    SnapElement,
    SnapTarget,
    Snap,
]

keymap_items = []


def register():
    # piemenus.register_addon()

    # for menu in pie_menus:
    #     if hasattr(menu, "keymap_items"):
    #         for km_name, kwargs in menu.keymap_items:
    #             km = piemenus.get_keymap(km_name)
    #             if km:
    #                 kmi = km.keymap_items.new("wm.pie_menu", **kwargs)
    #                 kmi.properties.menu = menu.idname
    #                 keymap_items.append((km, kmi))
    pass


def unregister():
    # piemenus.unregister_addon()

    for km, kmi in keymap_items:
        km.keymap_items.remove(kmi)
    keymap_items.clear()
