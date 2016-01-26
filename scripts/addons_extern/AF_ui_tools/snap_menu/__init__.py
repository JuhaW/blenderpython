# 3Dビュー > Shift+S
bl_info = {
    'name': 'Snap Menu',
    'author': 'meta-androcto, saidenka',
    'version': (2, 0),
    'blender': (2, 7, 6),
    'location': 'View3D > Shift/s ',
    'warning': '',
    'description': 'Added options for snapping & cursor',
    'category': '3D View'}

from .utils import AddonPreferences, SpaceProperty
import bpy
from bpy.types import PropertyGroup, Menu
################
# オペレーター #
################

class SnapMesh3DCursor(bpy.types.Operator):
	bl_idname = "view3d.snap_mesh_3d_cursor"
	bl_label = "3D cursor snap to mesh"
	bl_description = "(Please use the shortcuts) mesh surface under the mouse move the 3D cursor"
	bl_options = {'REGISTER'}
	
	mouse_co = bpy.props.IntVectorProperty(name="Mouse position", size=2)
	
	def execute(self, context):
		preGp = context.scene.grease_pencil
		preGpSource = context.scene.tool_settings.grease_pencil_source
		context.scene.tool_settings.grease_pencil_source = 'SCENE'
		if (preGp):
			tempGp = preGp
		else:
			try:
				tempGp = bpy.data.grease_pencil["temp"]
			except KeyError:
				tempGp = bpy.data.grease_pencil.new("temp")
		context.scene.grease_pencil = tempGp
		tempLayer = tempGp.layers.new("temp", set_active=True)
		tempGp.draw_mode = 'SURFACE'
		bpy.ops.gpencil.draw(mode='DRAW_POLY', stroke=[{"name":"", "pen_flip":False, "is_start":True, "location":(0, 0, 0),"mouse":self.mouse_co, "pressure":1, "time":0, "size":0}, {"name":"", "pen_flip":False, "is_start":True, "location":(0, 0, 0),"mouse":(0, 0), "pressure":1, "time":0, "size":0}])
		bpy.context.space_data.cursor_location = tempLayer.frames[-1].strokes[-1].points[0].co
		tempGp.layers.remove(tempLayer)
		context.scene.grease_pencil = preGp
		context.scene.tool_settings.grease_pencil_source = preGpSource
		return {'FINISHED'}
	def invoke(self, context, event):
		self.mouse_co[0] = event.mouse_region_x
		self.mouse_co[1] = event.mouse_region_y
		return self.execute(context)

class Move3DCursorToViewLocation(bpy.types.Operator):
	bl_idname = "view3d.move_3d_cursor_to_view_location"
	bl_label = "3D Navigation view"
	bl_description = "Move the 3D cursor center position of"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		bpy.context.space_data.cursor_location = context.region_data.view_location[:]
		return {'FINISHED'}

class Move3DCursorFar(bpy.types.Operator):
	bl_idname = "view3d.move_3d_cursor_far"
	bl_label = "3D cursor invisible in the (distant)"
	bl_description = "Pretend to hide the 3D cursor to move far far away"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		bpy.context.space_data.cursor_location = (24210, 102260, 38750)
		return {'FINISHED'}
## Origin To Selected Edit Mode ##
def main(context):
    cursorPositionX = bpy.context.scene.cursor_location[0]
    cursorPositionY = bpy.context.scene.cursor_location[1]
    cursorPositionZ = bpy.context.scene.cursor_location[2]
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.mode_set()
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.context.scene.cursor_location[0] = cursorPositionX
    bpy.context.scene.cursor_location[1] = cursorPositionY
    bpy.context.scene.cursor_location[2] = cursorPositionZ
    
class SetOriginToSelected(bpy.types.Operator):
    '''Tooltip'''
    bl_idname = "object.setorigintoselected"
    bl_label = "Set Origin to Selected"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        
        
        return {'FINISHED'}

# menu
def menu_func(self, context):

	self.layout.separator()
	self.layout.operator(Move3DCursorToViewLocation.bl_idname, text="Cursor To View")
	self.layout.operator(Move3DCursorFar.bl_idname, text="Temp Hide Cursor")
	self.layout.operator(SnapMesh3DCursor.bl_idname, text="Cursor → mesh surface")
	self.layout.separator()
	self.layout.label(text="Object Origin")
	self.layout.operator(SetOriginToSelected.bl_idname, text="Origin To F/V/E")

classes = [
    SnapMesh3DCursor,
    Move3DCursorToViewLocation,
    Move3DCursorFar,
    SetOriginToSelected
    ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_MT_snap.append(menu_func)



def unregister():

    bpy.types.VIEW3D_MT_snap.remove(menu_func)


    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register