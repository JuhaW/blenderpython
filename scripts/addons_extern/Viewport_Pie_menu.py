bl_info = {
    "name": "Viewport Pie menu",
    "author": "TARDIS Maker, pitiwazou",
    "version": (0, 0, 0),
    "blender": (2, 72, 2),
    "description": "A pie menu for selecting the new viewport type, splitting the viewport, and joining viewports. Original code by pitiwazou, modified to work for me",
    "location": "Hotkey: SHIFT + Spacebar",
    "category": "Pie menu",}

import bpy

from bpy.types import Menu, Header
from bpy.props import IntProperty, FloatProperty, BoolProperty



class SplitHorizontal(bpy.types.Operator):
	bl_idname = "split.horizontal"
	bl_label = "split horizontal"
	def execute(self, context):
		bpy.ops.screen.area_split(direction='HORIZONTAL')
		return {'FINISHED'}


# Split area vertical
class SplitVertical(bpy.types.Operator):
	bl_idname = "split.vertical"
	bl_label = "split vertical"
	def execute(self, context):
		bpy.ops.screen.area_split(direction='VERTICAL')
		return {'FINISHED'}


# Join area
class JoinArea(bpy.types.Operator):
	"""Click on the second area to join"""
	bl_idname = "area.joinarea"
	bl_label = "Join Area"
	min_x = IntProperty()
	min_y = IntProperty()
	def modal(self, context, event):
		if event.type == 'LEFTMOUSE':
			self.max_x = event.mouse_x
			self.max_y = event.mouse_y
			bpy.ops.screen.area_join(min_x=self.min_x, min_y=self.min_y, max_x=self.max_x, max_y=self.max_y)
			bpy.ops.screen.screen_full_area()
			bpy.ops.screen.screen_full_area()
			return {'FINISHED'}
		return {'RUNNING_MODAL'}
	def invoke(self, context, event):
		self.min_x = event.mouse_x
		self.min_y = event.mouse_y
		context.window_manager.modal_handler_add(self)
		return {'RUNNING_MODAL'}


#View Class menu
class ViewMenu(bpy.types.Operator):
	"""Menu to change views"""
	bl_idname = "object.view_menu"
	bl_label = "View Menu"
	variable = bpy.props.StringProperty()
	@classmethod
	def poll(cls, context):
		return True
	def execute(self, context):
		bpy.context.area.type = self.variable
		return {'FINISHED'}
		
		
#Pie Views - Space

class PieSplitViewport(Menu):
	bl_idname = "pie.split_viewport"
	bl_label = "Split Viewport"
	def draw(self, context):
		layout = self.layout
		pie = layout.menu_pie()
		pie = layout.menu_pie()
        
		pie.operator("split.vertical", text="Split Vertical", icon= 'TRIA_RIGHT')
		pie.operator("split.horizontal", text="Split Horizontal", icon= 'TRIA_DOWN')


class PieAreaViews(Menu):
    bl_idname = "pie.areaviews"
    bl_label = "Pie Views"
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie = layout.menu_pie()



        pie.operator("object.view_menu", text="Node Editor", icon= 'NODETREE').variable="NODE_EDITOR"
        pie.operator("object.view_menu", text="UV Image Editor", icon= 'IMAGE_COL').variable="IMAGE_EDITOR"
        #pie.operator_context="INVOKE_DEFAULT"
        pie.operator("screen.screen_full_area",text="Toggle Full Screen",icon='FULLSCREEN_ENTER')
        pie.operator("object.view_menu", text="3D View", icon= 'VIEW3D').variable="VIEW_3D"

        box = pie.split().box().column()
        col = box.column(align=True)
        col.operator("object.view_menu", text="Properties", icon= 'BUTS').variable="PROPERTIES"
        col.operator("object.view_menu", text="Outliner", icon= 'OOPS').variable="OUTLINER"
        col.operator("object.view_menu", text="File Browser", icon= 'FILESEL').variable="FILE_BROWSER"
        col.operator("object.view_menu", text="Text Editor", icon= 'TEXT').variable="TEXT_EDITOR"
        col.operator("object.view_menu", text="Python Console", icon= 'CONSOLE').variable="CONSOLE"


        box = pie.split().box().column()
        col = box.column(align=True)
        col.operator("object.view_menu", text="Timeline", icon= 'TIME').variable="TIMELINE"
        col.operator("object.view_menu", text="Dope Sheet", icon= 'ACTION').variable="DOPESHEET_EDITOR"
        col.operator("object.view_menu", text="Graph Editor", icon= 'IPO').variable="GRAPH_EDITOR"
        col.operator("object.view_menu", text="Movie Clip Editor", icon= 'CLIP').variable="CLIP_EDITOR"
        col.operator("object.view_menu", text="Video Sequece Editor", icon= 'SEQUENCE').variable="SEQUENCE_EDITOR"
        		
        pie.operator("area.joinarea",text="Join Viewports",icon='X')
        pie.operator("wm.call_menu_pie", text="Split Viewport", icon='PLUS').name="pie.split_viewport"


addon_keymaps = []
def register():
    # View Menu
    bpy.utils.register_class(PieAreaViews)
    bpy.utils.register_class(JoinArea)
    bpy.utils.register_class(SplitHorizontal)
    bpy.utils.register_class(SplitVertical)
    bpy.utils.register_class(PieSplitViewport)
    bpy.utils.register_class(ViewMenu)


    # Keympa Config
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        #Views
        km = wm.keyconfigs.addon.keymaps.new(name='Screen')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'SPACE', 'PRESS', shift=True)
        kmi.properties.name = "pie.areaviews"
        addon_keymaps.append(km)

# Register / Unregister Classes
def unregister():
    # View Menu
    bpy.utils.unregister_class(PieAreaViews)
    bpy.utils.unregister_class(JoinArea)
    bpy.utils.unregister_class(SplitHorizontal)
    bpy.utils.unregister_class(SplitVertical)
    bpy.utils.unregister_class(PieSplitViewport)
    bpy.utils.unregister_class(ViewMenu)


    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        for km in addon_keymaps:
            for kmi in km.keymap_items:
                km.keymap_items.remove(kmi)
                wm.keyconfigs.addon.keymaps.remove(km)
    # clear the list
    del addon_keymaps[:]


if __name__ == "__main__":
	register()
