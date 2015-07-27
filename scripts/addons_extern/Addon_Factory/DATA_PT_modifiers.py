# 「プロパティ」エリア > 「モディファイア」タブ

import bpy

################
# オペレーター #
################

class ApplyAllModifiers(bpy.types.Operator):
	bl_idname = "object.apply_all_modifiers"
	bl_label = "All modifiers applied"
	bl_description = "Applies to all modifiers of the selected object"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for obj in context.selected_objects:
			for mod in obj.modifiers[:]:
				bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
		return {'FINISHED'}

class DeleteAllModifiers(bpy.types.Operator):
	bl_idname = "object.delete_all_modifiers"
	bl_label = "Remove all modifiers"
	bl_description = "Remove all modifiers of the selected object"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for obj in context.selected_objects:
			modifiers = obj.modifiers[:]
			for modi in modifiers:
				obj.modifiers.remove(modi)
		return {'FINISHED'}

class ToggleApplyModifiersView(bpy.types.Operator):
	bl_idname = "object.toggle_apply_modifiers_view"
	bl_label = "Modifiers apply to the view switching"
	bl_description = "Shows or hides the application to view all modifiers of the selected object"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		is_apply = True
		for mod in context.active_object.modifiers:
			if (mod.show_viewport):
				is_apply = False
				break
		for obj in context.selected_objects:
			for mod in obj.modifiers:
				mod.show_viewport = is_apply
		if is_apply:
			self.report(type={"INFO"}, message="Applying modifiers to view")
		else:
			self.report(type={"INFO"}, message="Unregistered modifiers apply to the view")
		return {'FINISHED'}

class SyncShowModifiers(bpy.types.Operator):
	bl_idname = "object.sync_show_modifiers"
	bl_label = "Synchronized modifier use"
	bl_description = "The synchronized modifier used when rendering the selection / view"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("1", "Rendering → view", "", 1),
		("0", "View-rendering", "", 2),
		]
	mode = bpy.props.EnumProperty(items=items, name="Calculus", default="0")
	
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)
	def execute(self, context):
		for obj in context.selected_objects:
			for mod in obj.modifiers:
				if (int(self.mode)):
					mod.show_viewport = mod.show_render
				else:
					mod.show_render = mod.show_viewport
		return {'FINISHED'}

class ToggleAllShowExpanded(bpy.types.Operator):
	bl_idname = "wm.toggle_all_show_expanded"
	bl_label = "All modifiers expand / collapse toggle"
	bl_description = "Expand / collapse all modifiers of the active objects to the switch (toggle)"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		obj = context.active_object
		if (len(obj.modifiers)):
			vs = 0
			for mod in obj.modifiers:
				if (mod.show_expanded):
					vs += 1
				else:
					vs -= 1
			is_close = False
			if (0 < vs):
				is_close = True
			for mod in obj.modifiers:
				mod.show_expanded = not is_close
		else:
			self.report(type={'WARNING'}, message="Not a single modifier")
			return {'CANCELLED'}
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class ApplyModifiersAndJoin(bpy.types.Operator):
	bl_idname = "object.apply_modifiers_and_join"
	bl_label = "Modifiers apply + integration"
	bl_description = "The integration from the object\'s modifiers to apply all"
	bl_options = {'REGISTER', 'UNDO'}
	
	unapply_subsurf = bpy.props.BoolProperty(name="Excluding the Subsurf", default=True)
	unapply_armature = bpy.props.BoolProperty(name="Except the armature", default=True)
	unapply_mirror = bpy.props.BoolProperty(name="Except for mirrors", default=False)
	
	@classmethod
	def poll(cls, context):
		if (len(context.selected_objects) <= 1):
			return False
		return True
	def execute(self, context):
		pre_active_object = context.active_object
		for obj in context.selected_objects:
			context.scene.objects.active = obj
			for mod in obj.modifiers[:]:
				if (self.unapply_subsurf and mod.type == 'SUBSURF'):
					continue
				if (self.unapply_armature and mod.type == 'ARMATURE'):
					continue
				if (self.unapply_mirror and mod.type == 'MIRROR'):
					continue
				bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
		context.scene.objects.active = pre_active_object
		bpy.ops.object.join()
		return {'FINISHED'}

class AutoRenameModifiers(bpy.types.Operator):
	bl_idname = "object.auto_rename_modifiers"
	bl_label = "Modifier name auto-rename."
	bl_description = "Rename the selected object modifier name refers to, for example,"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for obj in context.selected_objects:
			for mod in obj.modifiers:
				try:
					if (mod.subtarget):
						mod.name = mod.subtarget
					continue
				except AttributeError: pass
				try:
					if (mod.target):
						mod.name = mod.target.name
					continue
				except AttributeError: pass
				try:
					if (mod.object):
						mod.name = mod.object.name
					continue
				except AttributeError: pass
				try:
					if (mod.vertex_group):
						mod.name = mod.vertex_group
					continue
				except AttributeError: pass
		return {'FINISHED'}

############################
# オペレーター(ブーリアン) #
############################

class AddBoolean(bpy.types.Operator):
	bl_idname = "object.add_boolean"
	bl_label = "Add a Boolean"
	bl_description = "Additional Boolean selected objects to an active object"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("INTERSECT", "Cross", "", 1),
		("UNION", "Integration", "", 2),
		("DIFFERENCE", "Difference", "", 3),
		]
	mode = bpy.props.EnumProperty(items=items, name="Calculus")
	
	def execute(self, context):
		activeObj = context.active_object
		for obj in context.selected_objects:
			if (obj.type == "MESH" and activeObj.name != obj.name):
				modi = activeObj.modifiers.new("Boolean", "BOOLEAN")
				modi.object = obj
				modi.operation = self.mode
				obj.draw_type = "BOUNDS"
		return {'FINISHED'}

class ApplyBoolean(bpy.types.Operator):
	bl_idname = "object.apply_boolean"
	bl_label = "Apply the Boolean"
	bl_description = "Active objects for other Boolean objects"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("INTERSECT", "Cross", "", 1),
		("UNION", "Integration", "", 2),
		("DIFFERENCE", "Difference", "", 3),
		]
	mode = bpy.props.EnumProperty(items=items, name="Calculus")
	
	def execute(self, context):
		activeObj = context.active_object
		for obj in context.selected_objects:
			if (obj.type == "MESH" and activeObj.name != obj.name):
				modi = activeObj.modifiers.new("Boolean", "BOOLEAN")
				modi.object = obj
				modi.operation = self.mode
				bpy.ops.object.modifier_apply (modifier=modi.name)
				bpy.ops.object.select_all(action='DESELECT')
				obj.select = True
				bpy.ops.object.delete()
				activeObj.select = True
		return {'FINISHED'}

############################
# オペレーター(サブサーフ) #
############################

class SetRenderSubsurfLevel(bpy.types.Operator):
	bl_idname = "object.set_render_subsurf_level"
	bl_label = "Rendering subdivision number"
	bl_description = "Sets the number of subdivisions during rendering of the selected object subsurfmodifaia"
	bl_options = {'REGISTER', 'UNDO'}
	
	level = bpy.props.IntProperty(name="Split number", default=2, min=0, max=6)
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type=="MESH" or obj.type=="CURVE" or obj.type=="SURFACE" or obj.type=="FONT" or obj.type=="LATTICE"):
				for modi in obj.modifiers:
					if (modi.type == "SUBSURF"):
						modi.render_levels = self.level
		return {'FINISHED'}

class EqualizeSubsurfLevel(bpy.types.Operator):
	bl_idname = "object.equalize_subsurf_level"
	bl_label = "Equivalent to a subdivision of the preview rendering"
	bl_description = "Set in the same subdivision of the subsurfmodifaia of the selected object when you preview and rendering time"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("ToRender", "Preview-rendering", "", 1),
		("ToPreview", "Rendering-preview", "", 2),
		]
	mode = bpy.props.EnumProperty(items=items, name="How to set up")
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type=="MESH" or obj.type=="CURVE" or obj.type=="SURFACE" or obj.type=="FONT" or obj.type=="LATTICE"):
				for modi in obj.modifiers:
					if (modi.type == "SUBSURF"):
						if (self.mode == "ToRender"):
							modi.render_levels = modi.levels
						else:
							modi.levels = modi.render_levels
		return {'FINISHED'}

class SetSubsurfOptimalDisplay(bpy.types.Operator):
	bl_idname = "object.set_subsurf_optimal_display"
	bl_label = "Set the defragmentation display"
	bl_description = "Sets optimization for the subsurfmodifaia of the selected object"
	bl_options = {'REGISTER', 'UNDO'}
	
	mode =  bpy.props.BoolProperty(name="Optimized view")
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type=="MESH" or obj.type=="CURVE" or obj.type=="SURFACE" or obj.type=="FONT" or obj.type=="LATTICE"):
				for modi in obj.modifiers:
					if (modi.type == "SUBSURF"):
						modi.show_only_control_edges = self.mode
		return {'FINISHED'}

class DeleteSubsurf(bpy.types.Operator):
	bl_idname = "object.delete_subsurf"
	bl_label = "Delete select Subsurf"
	bl_description = "Removes the selected object subsurfmodifaia"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type=="MESH" or obj.type=="CURVE" or obj.type=="SURFACE" or obj.type=="FONT" or obj.type=="LATTICE"):
				for modi in obj.modifiers:
					if (modi.type == "SUBSURF"):
						obj.modifiers.remove(modi)
		return {'FINISHED'}

class AddSubsurf(bpy.types.Operator):
	bl_idname = "object.add_subsurf"
	bl_label = "Add a Subsurf on selected objects"
	bl_description = "Add subsurfmodifaia to the selected object"
	bl_options = {'REGISTER', 'UNDO'}
	
	
	subdivision_type = bpy.props.EnumProperty(items=[("CATMULL_CLARK", "Catmulclark", "", 1), ("SIMPLE", "Simple", "", 2)], name="Subdivision method")
	levels = bpy.props.IntProperty(name="Number of views", default=2, min=0, max=6)
	render_levels = bpy.props.IntProperty(name="Split number render", default=2, min=0, max=6)
	use_subsurf_uv =  bpy.props.BoolProperty(name="Subdivided UVs", default=True)
	show_only_control_edges =  bpy.props.BoolProperty(name="Optimized view")
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type=="MESH" or obj.type=="CURVE" or obj.type=="SURFACE" or obj.type=="FONT" or obj.type=="LATTICE"):
				modi = obj.modifiers.new("Subsurf", "SUBSURF")
				modi.subdivision_type = self.subdivision_type
				modi.levels = self.levels
				modi.render_levels = self.render_levels
				modi.use_subsurf_uv = self.use_subsurf_uv
				modi.show_only_control_edges = self.show_only_control_edges
		return {'FINISHED'}

##############################
# オペレーター(アーマチュア) #
##############################

class SetArmatureDeformPreserveVolume(bpy.types.Operator):
	bl_idname = "object.set_armature_deform_preserve_volume"
	bl_label = "Set keep up the volume the armature"
	bl_description = "Maintain volume in the armtuamodifaia of the selected objects together off and on the"
	bl_options = {'REGISTER', 'UNDO'}
	
	use_deform_preserve_volume =  bpy.props.BoolProperty(name="Use the preserve volume", default=True)
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type == "MESH"):
				for mod in obj.modifiers:
					if (mod.type == 'ARMATURE'):
						mod.use_deform_preserve_volume = self.use_deform_preserve_volume
		return {'FINISHED'}

########################
# オペレーター(カーブ) #
########################

class QuickCurveDeform(bpy.types.Operator):
	bl_idname = "object.quick_curve_deform"
	bl_label = "Quick curve deformation"
	bl_description = "Quickly apply the curve modifier"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		('POS_X', "+X", "", 1),
		('POS_Y', "+Y", "", 2),
		('POS_Z', "+Z", "", 3),
		('NEG_X', "-X", "", 4),
		('NEG_Y', "-Y", "", 5),
		('NEG_Z', "-Z", "", 6),
		]
	deform_axis = bpy.props.EnumProperty(items=items, name="Axial deformation")
	is_apply = bpy.props.BoolProperty(name="Modifiers applied", default=False)
	
	@classmethod
	def poll(cls, context):
		if (not context.object):
			return False
		if (context.object.type != 'MESH'):
			return False
		if (len(context.selected_objects) != 2):
			return False
		for obj in context.selected_objects:
			if (obj.type == 'CURVE'):
				return True
		return False
	def execute(self, context):
		mesh_obj = context.active_object
		if (mesh_obj.type != 'MESH'):
			self.report(type={"ERROR"}, message="Please run the mesh object is active")
			return {"CANCELLED"}
		if (len(context.selected_objects) != 2):
			self.report(type={"ERROR"}, message="By selecting only the two meshes, curves, please run")
			return {"CANCELLED"}
		for obj in context.selected_objects:
			if (mesh_obj.name != obj.name):
				if (obj.type == 'CURVE'):
					curve_obj = obj
					break
		else:
			self.report(type={"ERROR"}, message="Curve objects run in the selected state")
			return {"CANCELLED"}
		curve = curve_obj.data
		pre_use_stretch = curve.use_stretch
		pre_use_deform_bounds = curve.use_deform_bounds
		curve.use_stretch = True
		curve.use_deform_bounds = True
		bpy.ops.object.transform_apply_all()
		mod = mesh_obj.modifiers.new("temp", 'CURVE')
		mod.object = curve_obj
		mod.deform_axis = self.deform_axis
		for i in range(len(mesh_obj.modifiers)):
			bpy.ops.object.modifier_move_up(modifier=mod.name)
		if (self.is_apply):
			bpy.ops.object.modifier_apply(modifier=mod.name)
			curve.use_stretch = pre_use_stretch
			curve.use_deform_bounds = pre_use_deform_bounds
		return {'FINISHED'}

class QuickArrayAndCurveDeform(bpy.types.Operator):
	bl_idname = "object.quick_array_and_curve_deform"
	bl_label = "Quick array replication + curve deformation"
	bl_description = "Quickly apply the curve modifier with the modifiers array replication"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		('POS_X', "+X", "", 1),
		('POS_Y', "+Y", "", 2),
		('POS_Z', "+Z", "", 3),
		('NEG_X', "-X", "", 4),
		('NEG_Y', "-Y", "", 5),
		('NEG_Z', "-Z", "", 6),
		]
	deform_axis = bpy.props.EnumProperty(items=items, name="Axial deformation")
	use_merge_vertices = bpy.props.BoolProperty(name="Vertex binding", default=True)
	is_apply = bpy.props.BoolProperty(name="Modifiers applied", default=False)
	
	@classmethod
	def poll(cls, context):
		if (not context.object):
			return False
		if (context.object.type != 'MESH'):
			return False
		if (len(context.selected_objects) != 2):
			return False
		for obj in context.selected_objects:
			if (obj.type == 'CURVE'):
				return True
		return False
	def execute(self, context):
		mesh_obj = context.active_object
		if (mesh_obj.type != 'MESH'):
			self.report(type={'ERROR'}, message="Please run the mesh object is active")
			return {'CANCELLED'}
		if (len(context.selected_objects) != 2):
			self.report(type={'ERROR'}, message="By selecting only the two meshes, curves, please run")
			return {'CANCELLED'}
		for obj in context.selected_objects:
			if (mesh_obj.name != obj.name):
				if (obj.type == 'CURVE'):
					curve_obj = obj
					break
		else:
			self.report(type={'ERROR'}, message="Curve objects run in the selected state")
			return {'CANCELLED'}
		curve = curve_obj.data
		pre_use_stretch = curve.use_stretch
		pre_use_deform_bounds = curve.use_deform_bounds
		curve.use_stretch = True
		curve.use_deform_bounds = True
		bpy.ops.object.transform_apply_all()
		
		mod_array = mesh_obj.modifiers.new("Array", 'ARRAY')
		mod_array.fit_type = 'FIT_CURVE'
		mod_array.curve = curve_obj
		mod_array.use_merge_vertices = self.use_merge_vertices
		mod_array.use_merge_vertices_cap = self.use_merge_vertices
		if (self.deform_axis == 'POS_Y'):
			mod_array.relative_offset_displace = (0, 1, 0)
		elif (self.deform_axis == 'POS_Z'):
			mod_array.relative_offset_displace = (0, 0, 1)
		elif (self.deform_axis == 'NEG_X'):
			mod_array.relative_offset_displace = (-1, 0, 0)
		elif (self.deform_axis == 'NEG_Y'):
			mod_array.relative_offset_displace = (0, -1, 0)
		elif (self.deform_axis == 'NEG_Z'):
			mod_array.relative_offset_displace = (0, 0, -1)
		
		mod_curve = mesh_obj.modifiers.new("Curve", 'CURVE')
		mod_curve.object = curve_obj
		mod_curve.deform_axis = self.deform_axis
		
		for i in range(len(mesh_obj.modifiers)):
			bpy.ops.object.modifier_move_up(modifier=mod_curve.name)
		for i in range(len(mesh_obj.modifiers)):
			bpy.ops.object.modifier_move_up(modifier=mod_array.name)
		
		if (self.is_apply):
			bpy.ops.object.modifier_apply(modifier=mod_array.name)
			bpy.ops.object.modifier_apply(modifier=mod_curve.name)
			curve.use_stretch = pre_use_stretch
			curve.use_deform_bounds = pre_use_deform_bounds
		return {'FINISHED'}

################
# サブメニュー #
################

class ModifierMenu(bpy.types.Menu):
	bl_idname = "DATA_PT_modifiers_specials"
	bl_label = "Modifier action"
	bl_description = "Is working with modifiers"
	
	def draw(self, context):
		self.layout.menu(SubsurfMenu.bl_idname, icon='PLUGIN')
		self.layout.menu(ArmatureMenu.bl_idname, icon='PLUGIN')
		self.layout.menu(BooleanMenu.bl_idname, icon='PLUGIN')
		self.layout.menu(CurveMenu.bl_idname, icon='PLUGIN')
		self.layout.separator()
		self.layout.operator(ApplyModifiersAndJoin.bl_idname, icon='PLUGIN')

class SubsurfMenu(bpy.types.Menu):
	bl_idname = "DATA_PT_modifiers_subsurf"
	bl_label = "Save surf related"
	bl_description = "Is the relationship between subsurface operations"
	
	def draw(self, context):
		self.layout.operator(AddSubsurf.bl_idname, icon='PLUGIN')
		self.layout.operator(DeleteSubsurf.bl_idname, icon='PLUGIN')
		self.layout.separator()
		self.layout.operator(SetRenderSubsurfLevel.bl_idname, icon='PLUGIN')
		self.layout.operator(EqualizeSubsurfLevel.bl_idname, icon='PLUGIN')
		self.layout.operator(SetSubsurfOptimalDisplay.bl_idname, icon='PLUGIN')

class BooleanMenu(bpy.types.Menu):
	bl_idname = "DATA_PT_modifiers_boolean"
	bl_label = "Boolean related"
	bl_description = "Is the relationship between Boolean operations"
	
	def draw(self, context):
		self.layout.operator(AddBoolean.bl_idname, icon='PLUGIN', text="Boolean Add (cross)").mode = "INTERSECT"
		self.layout.operator(AddBoolean.bl_idname, icon='PLUGIN', text="Boolean Add (integrated)").mode = "UNION"
		self.layout.operator(AddBoolean.bl_idname, icon='PLUGIN', text="Boolean Add (diff)").mode = "DIFFERENCE"
		self.layout.separator()
		self.layout.operator(ApplyBoolean.bl_idname, icon='PLUGIN', text="Boolean apply (cross)").mode = "INTERSECT"
		self.layout.operator(ApplyBoolean.bl_idname, icon='PLUGIN', text="Boolean apply (integrated)").mode = "UNION"
		self.layout.operator(ApplyBoolean.bl_idname, icon='PLUGIN', text="Boolean apply (diff)").mode = "DIFFERENCE"

class ArmatureMenu(bpy.types.Menu):
	bl_idname = "DATA_PT_modifiers_armature"
	bl_label = "Armature connection"
	bl_description = "Armature connection operation"
	
	def draw(self, context):
		self.layout.operator(SetArmatureDeformPreserveVolume.bl_idname, icon='PLUGIN')

class CurveMenu(bpy.types.Menu):
	bl_idname = "DATA_PT_modifiers_curve"
	bl_label = "Relationship between curves"
	bl_description = "Operation of curve relationships"
	
	def draw(self, context):
		self.layout.operator(QuickCurveDeform.bl_idname, icon='PLUGIN')
		self.layout.operator(QuickArrayAndCurveDeform.bl_idname, icon='PLUGIN')

################
# メニュー追加 #
################

# メニューのオン/オフの判定
def IsMenuEnable(self_id):
	for id in bpy.context.user_preferences.addons['Addon_Factory'].preferences.disabled_menu.split(','):
		if (id == self_id):
			return False
	else:
		return True

# メニューを登録する関数
def menu(self, context):
	if (IsMenuEnable(__name__.split('.')[-1])):
		if (context.active_object):
			if (len(context.active_object.modifiers)):
				col = self.layout.column(align=True)
				row = col.row(align=True)
				row.operator(AutoRenameModifiers.bl_idname, icon='SCRIPT', text="Rename all")
				row.operator(ApplyAllModifiers.bl_idname, icon='IMPORT', text="All applicable")
				row.operator(DeleteAllModifiers.bl_idname, icon='X', text="Delete all")
				row = col.row(align=True)
				row.operator(ToggleApplyModifiersView.bl_idname, icon='RESTRICT_VIEW_OFF', text="View")
				row.operator(ToggleAllShowExpanded.bl_idname, icon='FULLSCREEN_ENTER', text="Expand / collapse")
				row.operator(SyncShowModifiers.bl_idname, icon='LINKED', text="Use over the")
		self.layout.menu(ModifierMenu.bl_idname, icon='PLUGIN')
	if (context.user_preferences.addons['Addon_Factory'].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='VISIBLE_IPO_ON').id = __name__.split('.')[-1]
