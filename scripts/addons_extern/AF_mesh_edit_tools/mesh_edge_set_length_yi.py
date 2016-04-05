# 本工具遵循Blender使用协议

bl_info = {
	'name': "Edges set length", # and angle
	'description': "edges set length", # and angle
	'author': "Yi Danyang",
	'version': (0, 0, 1, 1),
	'blender': (2, 7, 0, 5),
	'api': 'a8282da',
	'location': 'Shit+Alt+E or [Toolbar][Tools][Mesh Tools] Edges Length', # and Angle
	'warning': "",
	'category': 'Mesh',
	"wiki_url": "mailto:yidanyang@gmail.com",
	"tracker_url": "mailto:yidanyang@gmail.com",
}


#引入blender核心
import bpy

#基本类型
from bpy.props import (BoolProperty,
					   BoolVectorProperty,
					   IntProperty,
					   FloatProperty,
					   EnumProperty)

#定义操作
class LengthChange(bpy.types.Operator):
	#操作名称(2.70.5 原本是mesh.edge，但现在工具栏是OT，要加入这个位置还只能是object，也许以后会修改)
	bl_idname = "object.mesh_edge_lengthchange"
	#标签
	bl_label = "length_change"
	bl_description = " Set the Length of a single edge"
	#返回
	bl_options = {'REGISTER', 'UNDO'}
	#缩放中心
	pin_point = EnumProperty(
		name="pin",
		items=(("s", "start", "start"), 
			   ("c", "center", "center"), 
			   ("e", "end", "end")),
		default='s',
		description="center for scale")
	#目标长度
	target_length = FloatProperty( name = 'length', default = 1, min = 0.0000001, step = 1, precision = 3 )
	
	#中心
	@classmethod
	def poll(cls, context):
		return (context.active_object and context.active_object.type == 'MESH' and context.mode == 'EDIT_MESH')

	#运行
	def execute(self, context):
		# message = "Popup Values: %s, %f" % \
			# (self.pin_point, self.target_length )
		# self.report({'INFO'}, message)
		
		
		ob = context.active_object
		if not ob or ob.type != 'MESH':
			self.report({'ERROR'}, '需要激活模型')
			return {'CANCELLED'}
		if ob.data.total_edge_sel == 1:
			# bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
			bpy.ops.object.editmode_toggle()
			bpy.ops.object.editmode_toggle()
			last_cursor_location = context.scene.cursor_location.copy()
			# ob.data.update(calc_edges=True)
			
			# 准备
			vts = ob.data.vertices
			vts_select_id = []
			for i,v in enumerate(vts):
				if v.select == True:
					vts_select_id.append(i)
			# 实现
			current_length = (vts[vts_select_id[0]].co - vts[vts_select_id[1]].co).magnitude
			if abs(current_length - self.target_length) > 0.00001:
				# 输入值 与 当前值 差的大
				if current_length == 0:
					self.report({'ERROR'}, '无法操作重叠点')
					return {'CANCELLED'}
				else:
					target_scale_size = self.target_length / current_length
					# print("%s / %s = %s" % (self.target_length, current_length, target_scale_size))

				# 缩放点
				if self.pin_point == 's':
					context.scene.cursor_location = ob.matrix_world * (vts[vts_select_id[0]].co)
				elif self.pin_point == 'e':
					context.scene.cursor_location = ob.matrix_world * (vts[vts_select_id[1]].co)
				else:
					context.scene.cursor_location = ob.matrix_world * ((vts[vts_select_id[0]].co + vts[vts_select_id[1]].co)/2)

				# 缩放中心
				last_pivot_point = context.space_data.pivot_point
				context.space_data.pivot_point = 'CURSOR'
				
				# 缩放
				bpy.ops.transform.resize(value=(target_scale_size, target_scale_size, target_scale_size))
				
				# 还原
				context.space_data.pivot_point = last_pivot_point
				
			else:
				# 差不多，算了
				pass
				
			# ob.data.update(calc_edges=True)
			context.scene.cursor_location = last_cursor_location
			
		else:
			self.report({'ERROR'}, '仅能操作 1 根线段')
			# 多线段 端点不好决定
			return {'CANCELLED'}	
		return {'FINISHED'}
		
	def invoke(self, context, event):
		wm = context.window_manager
		return wm.invoke_props_dialog(self)
		
		
## TODO 有空再做
# class AngleChange(bpy.types.Operator):
	# #操作名称
	# bl_idname = "mesh.edge_anglechange"
	# #标签
	# bl_label = "angle_change"
	# #返回
	# bl_options = {'REGISTER', 'UNDO'}
	# #角度
	# target_angle = FloatProperty( name = 'angle', default = 30, min = 0.00001, max = 360.0, step = 1, precision = 3 )
	# #目标长度
	# target_length = FloatProperty( name = 'length', default = 0.5, min = 0.00001, max = 10.0, step = 1, precision = 3 )
	
	# @classmethod
	# def poll(cls, context):
		# return (context.active_object and context.active_object.type == 'MESH' and context.mode == 'EDIT_MESH')

	# #运行
	# def execute(self, context):
		# ob = context.active_object
		# if not ob:
			# self.report({'ERROR'}, 'missing active object')
			# return {'CANCELLED'}	
		# if ob.data.total_edge_sel == 2 and ob.data.total_vert_sel == 3:
			# # TODO
			# pass
		# else:
			# self.report({'ERROR'}, 'missing 2 edge and 3 point this time')
			# return {'CANCELLED'}	
		# return {'FINISHED'}

		
#定义面板
def menu_func(self, context):
	#位置
	self.layout.operator_context = 'INVOKE_DEFAULT'
	#按键
	self.layout.label(text="Edges Length:")	# and Angle
	row = self.layout.row(align=True)
	# row.operator(AngleChange.bl_idname, "Angle")
	row.operator(LengthChange.bl_idname, "Length")
	#分割
	#self.layout.separator()
		
def register():
	#注册操作方法
	bpy.utils.register_class(LengthChange)
	# bpy.utils.register_class(AngleChange)
	bpy.types.VIEW3D_PT_tools_meshedit.append(menu_func)

	# hotkey
	kc = bpy.context.window_manager.keyconfigs.default.keymaps['Mesh']
	kc.keymap_items.new(LengthChange.bl_idname, 'E', 'PRESS', shift = True, alt = True)

def unregister():
	#与register对应，卸载功能
	bpy.utils.unregister_class(LengthChange)
	# bpy.utils.unregister_class(AngleChange)
	bpy.types.VIEW3D_PT_tools_meshedit.remove(menu_func)
	
	# hotkey
	kc = bpy.context.window_manager.keyconfigs.default.keymaps['Mesh']
	kc.keymap_items.remove(kc.keymap_items[LengthChange.bl_idname])

#方便文本编辑器中测试
if __name__ == "__main__":
	register()
