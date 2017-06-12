bl_info = {
	"name": "Bevel Weights",
	"author": "Mackraken",
	"version": (0, 1),
	"blender": (2, 6, 3),
	"location": "Select Edges -> Ctrl + Shift + E",
	"description": "Bevel Edges using Weights",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Mesh"}

import bpy
from bpy.props import FloatProperty


class Bevel_Weights(bpy.types.Operator):
	'''Change Bevel Weights.'''
	bl_idname = "mesh.bevel_weights"
	bl_label = "Bevel Weights"

	

	percent = FloatProperty(default = 0.2, min=0.1, max = 0.9, description = "Mouse Sensitivity")

	undo = []
	keys = ""
	
	numpad = [  'NUMPAD_0',
			'NUMPAD_1',
			'NUMPAD_2',
			'NUMPAD_3',
			'NUMPAD_4',
			'NUMPAD_5',
			'NUMPAD_6',
			'NUMPAD_7',
			'NUMPAD_8',
			'NUMPAD_9',
			'NUMPAD_PERIOD'
			]
				
	def modal(self, context, event):
		
		val = 0.0
	
		percent = self.percent
	
		if event.type == 'MOUSEMOVE' and self.keys=="":
						
			fullw = self.fullw
			
			x = (event.mouse_region_x/fullw)
			
			if x<percent/2.0:
				val = 0.0
			elif x>1-percent/2.0:
				val = 1.0
			else:
				val = ((x/(1-percent))-percent/2)
				
			for ed in context.object.data.edges:
				if ed.select:
					ed.bevel_weight = val

			context.area.header_text_set("Bevel Weight: %.4f" % (val))
		
		elif event.type == "BACK_SPACE" and event.value == "PRESS":

			self.keys = self.keys[0:-1]		 
			if len(self.keys)>0:
				val = float(self.keys)
				
			if context.mode == "EDIT":
				import bpy
				bpy.ops.object.editmode_toggle()
			
			for ed in context.object.data.edges:
				if ed.select:
					ed.bevel_weight = val
			context.area.header_text_set("Bevel Weight: " + self.keys)
			
		elif event.type in self.numpad:
			if event.value == "PRESS":
#			   print(event.type, event.value, event.type[-1])
				if event.type[-1].isnumeric():
					self.keys += event.type[-1]
				elif len(self.keys)==0:
					self.keys = "0."
				elif self.keys[-1]!=".":
					self.keys += "."
					
				if self.keys!="":
					val = float(self.keys)
				
				if context.mode == "EDIT":
					bpy.ops.object.editmode_toggle()
				for ed in context.object.data.edges:
					if ed.select:
						ed.bevel_weight = val
						
				context.area.header_text_set("Bevel Weight: " + self.keys)  
				
		elif event.type in {'LEFTMOUSE', 'NUMPAD_ENTER', 'RET'}:
		
			import bpy				
			bpy.ops.object.editmode_toggle()
			context.area.header_text_set()
			return {'FINISHED'}


		elif event.type in {'RIGHTMOUSE', 'ESC'}:
			#print(self.undo)
			for info in self.undo:
				context.object.data.edges[info[0]].bevel_weight = info[1]
			import bpy	
			bpy.ops.object.editmode_toggle()
			context.area.header_text_set()
			#context.object.location.x = self.first_value
			return {'CANCELLED'}
				
		return {'RUNNING_MODAL'}

	def invoke(self, context, event):
		#self.fullw = context.window_manager.windows[0].screen.areas[0].regions[0].width
		self.fullw = context.area.regions[0].width
		
		if context.object.mode == "EDIT":
			import bpy
			bpy.ops.object.editmode_toggle()
			
			for ed in context.object.data.edges:
				if ed.select:
					self.undo.append([ed.index, ed.bevel_weight])
					
			if self.undo == []:
				bpy.ops.object.editmode_toggle()
				return {'CANCELLED'}
			
			modfound = False
			for mod in context.object.modifiers:
				if mod.type == "BEVEL" and mod.limit_method == "WEIGHT":
					modfound = True
					break
			if not modfound:
				mod = context.object.modifiers.new(name = "Bevel", type = "BEVEL")
				mod.limit_method = "WEIGHT"
				
			#bpy.ops.object.editmode_toggle()
			context.window_manager.modal_handler_add(self)
			
			#self.first_mouse_x = event.mouse_x
			#self.first_value = context.object.location.x
			return {'RUNNING_MODAL'}
		else:
			self.report({'WARNING'}, "No active edge, could not finish")
			return {'CANCELLED'}



	


def register():
	bpy.utils.register_class(Bevel_Weights)
	try:
		kconf = bpy.context.window_manager.keyconfigs['Blender User']
		map = kconf.keymaps['Mesh']
	
		found = False
		for key in map.keymap_items:
			if key.name in {"Bevel Weights", "MESH_OT_bevel_weights"}:
				found = True
				break
	
		if not found:
			key = map.keymap_items.new(idname = "mesh.bevel_weights", type = "E", value = "PRESS")
			key.shift = True
			key.ctrl = True 
	except:
		pass
	
def unregister():
	try:
		kconf = bpy.context.window_manager.keyconfigs['Blender User']
		map = kconf.keymaps['Mesh']
	
		found = False
		for key in map.keymap_items:
			if key.name in {"Bevel Weights", "MESH_OT_bevel_weights"}:
				found = True
				break
		if found:
			map.keymap_items.remove(key)
	except:
		pass
	bpy.utils.unregister_class(Bevel_Weights)


if __name__ == "__main__":
	register()
	


	# test call
	#bpy.ops.object.modal_operator('INVOKE_DEFAULT')