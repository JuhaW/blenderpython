# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

bl_info = {
	"name": "BMax Tools",
	"author": "Ozzkar",
	"version": (0, 2, 3),
	"blender": (2, 77, 0),
	"location": "View3D > BMax",
	"description": "Blender 3ds Max/Maya inspired UI",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "",
	"category": "3D View"}

#*********************************************************************************#

import bpy
import mathutils
from mathutils import Vector, Matrix
from bpy.types import Panel, Menu, UIList, Operator, PropertyGroup
from bpy.props import IntProperty, BoolProperty, StringProperty, PointerProperty, EnumProperty, CollectionProperty, FloatProperty

bmax_FULL = False # set to 'True' to display non-compacted menus

#*********************************************************************************#
# Object Mode : Align
#*********************************************************************************#

def bmaxAlign_GetPosData(obj):
	# get AABB
	cld = []
	msh = obj.data
	if obj.type == 'MESH' and len(msh.vertices) > 0:
		for vert in msh.vertices:
			cld.append(obj.matrix_world * vert.co)
	elif obj.type == 'CURVE' and len(msh.splines) > 0:
		for spn in msh.splines:
			for pts in spn.bezier_points:
				cld.append(obj.matrix_world * pts.co)
	elif obj.type == 'SURFACE' and len(msh.splines) > 0:
		for spn in msh.splines:
			for pts in spn.points:
				cld.append(obj.matrix_world * pts.co)
	elif obj.type == 'FONT' and len(msh.splines) > 0:
		for s in msh.splines:
			for pts in s.bezier_points:
				cld.append(obj.matrix_world * pts.co)
	# get min/max/center/pivot data
	if len(cld) == 0 or obj.type not in {'MESH', 'CURVE', 'SURFACE', 'FONT'}:
		return obj.location.copy(), obj.location.copy(), obj.location.copy(), obj.location.copy()
	p_min = cld[0].copy()
	p_max = cld[0].copy()
	for v in cld:
		if p_min.x > v.x: p_min.x = v.x
		if p_min.y > v.y: p_min.y = v.y
		if p_min.z > v.z: p_min.z = v.z
		if p_max.x < v.x: p_max.x = v.x
		if p_max.y < v.y: p_max.y = v.y
		if p_max.z < v.z: p_max.z = v.z
	return p_min, (p_min + ((p_max - p_min) / 2)), obj.location.copy(), p_max

#*********************************************************************************#

def bmaxAlign_StoreXFormData(self, ctx):
	self.pos_curs = ctx.scene.cursor_location.copy()
	for obj in ctx.selected_objects:
		p_min, p_mid, p_piv, p_max = bmaxAlign_GetPosData(obj)
		self.pos_list.append([p_min, p_mid, p_piv, p_max])
		self.rot_list.append(obj.rotation_euler.copy())
		self.scl_list.append(obj.scale.copy())

#*********************************************************************************#

def bmaxAlign_Execute(self, ctx):
	a_box = bmaxAlign_GetPosData(ctx.active_object)
	a_rot = ctx.active_object.rotation_euler
	a_scl = ctx.active_object.scale
	# set modes
	c_id = 0
	t_id = 0
	if self.c_mode == 'MID': c_id = 1
	if self.c_mode == 'PIV': c_id = 2
	if self.c_mode == 'MAX': c_id = 3
	if self.t_mode == 'MID': t_id = 1
	if self.t_mode == 'PIV': t_id = 2
	if self.t_mode == 'MAX': t_id = 3
	# check cursor to cursor
	if self.c_mode == '3DC' and self.t_mode == '3DC':
		return
	# check active object agains itself
	if len(ctx.selected_objects) == 1 and self.c_mode != '3DC' and self.t_mode != '3DC':
		return
	# set 3D cursor
	if self.c_mode == '3DC':
		if self.pos_x == True: ctx.scene.cursor_location.x = a_box[t_id].x
		if self.pos_y == True: ctx.scene.cursor_location.y = a_box[t_id].y
		if self.pos_z == True: ctx.scene.cursor_location.z = a_box[t_id].z
		return
	if self.t_mode == '3DC':
		scp = ctx.scene.cursor_location.copy()
		for i, obj in enumerate(ctx.selected_objects):
			if self.pos_x == True: obj.location.x = scp.x + (self.pos_list[i][2].x - self.pos_list[i][c_id].x)
			if self.pos_y == True: obj.location.y = scp.y + (self.pos_list[i][2].y - self.pos_list[i][c_id].y)
			if self.pos_z == True: obj.location.z = scp.z + (self.pos_list[i][2].z - self.pos_list[i][c_id].z)
		return
	# set selection
	for i, obj in enumerate(ctx.selected_objects):
		if obj != ctx.active_object:
			# position
			if self.pos_x == True: obj.location.x = a_box[t_id].x + (self.pos_list[i][2].x - self.pos_list[i][c_id].x)
			if self.pos_y == True: obj.location.y = a_box[t_id].y + (self.pos_list[i][2].y - self.pos_list[i][c_id].y)
			if self.pos_z == True: obj.location.z = a_box[t_id].z + (self.pos_list[i][2].z - self.pos_list[i][c_id].z)
			# rotation
			if self.rot_x == True: obj.rotation_euler.x = a_rot.x
			if self.rot_y == True: obj.rotation_euler.y = a_rot.y
			if self.rot_z == True: obj.rotation_euler.z = a_rot.z
			# scale
			if self.scl_x == True: obj.scale.x = a_scl.x
			if self.scl_y == True: obj.scale.y = a_scl.y
			if self.scl_z == True: obj.scale.z = a_scl.z

#*********************************************************************************#

def bmaxAlign_Reset(self, ctx):
	ctx.scene.cursor_location.x = self.pos_curs.x
	ctx.scene.cursor_location.y = self.pos_curs.y
	ctx.scene.cursor_location.z = self.pos_curs.z
	for i, obj in enumerate(ctx.selected_objects):
		# position
		obj.location.x = self.pos_list[i][2].x
		obj.location.y = self.pos_list[i][2].y
		obj.location.z = self.pos_list[i][2].z
		# rotation
		obj.rotation_euler.x = self.rot_list[i].x
		obj.rotation_euler.y = self.rot_list[i].y
		obj.rotation_euler.z = self.rot_list[i].z
		# scale
		obj.scale.x = self.scl_list[i].x
		obj.scale.y = self.scl_list[i].y
		obj.scale.z = self.scl_list[i].z

	ctx.scene.update()

#*********************************************************************************#

class BMAX_OM_Align_OT(Operator):
	bl_idname = "bmax.align_tool"
	bl_label = "Align Selection"
	bl_description = "Align selection dialog box"
	bl_options = {'REGISTER', 'UNDO'}

	pos_curs = Vector((0, 0, 0))
	pos_list = []
	rot_list = []
	scl_list = []

	c_mode = EnumProperty(
		name = '', description = 'Selection alignment point', default = 'MIN',
		items = [
			('MIN', 'Minimum', 'Minimum'),
			('MID', 'Center', 'Center'),
			('PIV', 'Pivot', 'Pivot'),
			('MAX', 'Maximum', 'Maximum'),
			('3DC', '3D Cursor', '3D Cursor')]
		)
	t_mode = EnumProperty(
		name = '', description = 'Target alignment point', default = 'MIN',
		items = [
			('MIN', 'Minimum', 'Minimum'),
			('MID', 'Center', 'Center'),
			('PIV', 'Pivot', 'Pivot'),
			('MAX', 'Maximum', 'Maximum'),
			('3DC', '3D Cursor', '3D Cursor')]
		)
	pos_x = BoolProperty(default = False)
	pos_y = BoolProperty(default = False)
	pos_z = BoolProperty(default = False)
	rot_x = BoolProperty(default = False)
	rot_y = BoolProperty(default = False)
	rot_z = BoolProperty(default = False)
	scl_x = BoolProperty(default = False)
	scl_y = BoolProperty(default = False)
	scl_z = BoolProperty(default = False)

	@classmethod
	def poll(self, ctx):
		return len(ctx.selected_objects) > 0 and ctx.active_object != None

	def check(self, ctx):
		bmaxAlign_Reset(self, ctx)
		bmaxAlign_Execute(self, ctx)
		return True

	def draw(self, ctx):
		ui = self.layout
		b = ui.box()
		r = b.row()
		r.label("Align Position (World):")
		r = b.row()
		r.prop(self, "pos_x", text = "X Position")
		r.prop(self, "pos_y", text = "Y Position")
		r.prop(self, "pos_z", text = "Z Position")
		r = b.row()
		r.label("Current Object:")
		r.label("Taget Object:")
		r = b.row()
		r.prop(self, "c_mode")
		r.prop(self, "t_mode")
		b = ui.box()
		r = b.row()
		r.label("Align Orientation (Local):")
		r = b.row()
		r.prop(self, "rot_x", text = "X Axis")
		r.prop(self, "rot_y", text = "Y Axis")
		r.prop(self, "rot_z", text = "Z Axis")
		b = ui.box()
		r = b.row()
		r.label("Match Scale:")
		r = b.row()
		r.prop(self, "scl_x", text = "X Axis")
		r.prop(self, "scl_y", text = "Y Axis")
		r.prop(self, "scl_z", text = "Z Axis")

	def execute(self, ctx):
		return {'FINISHED'}

	def cancel(self, ctx):
		bmaxAlign_Reset(self, ctx)

	def invoke(self, ctx, evt):
		self.pos_curs = Vector((0, 0, 0))
		self.pos_list = []
		self.rot_list = []
		self.scl_list = []
		bmaxAlign_StoreXFormData(self, ctx)
		bmaxAlign_Execute(self, ctx)
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}

#*********************************************************************************#
# Object Mode : Mirror
#*********************************************************************************#

def bmaxMirror_Execute_OM(self, ctx):
	ctx.active_object.matrix_world = self.old_xfrm.copy()
	if self.c_mode == 'COPY':
		if self.obj_copy == None:
			bpy.ops.object.duplicate(linked = False, mode = 'INIT')
			self.obj_copy = ctx.active_object
	elif self.c_mode == 'INST':
		if self.obj_copy == None:
			bpy.ops.object.duplicate(linked = True, mode = 'INIT')
			self.obj_copy = ctx.active_object
	else:
		if self.obj_copy != None:
			bpy.ops.object.delete(use_global = False)
			ctx.scene.objects.active = self.obj_orig
			self.obj_orig.select = True
			self.obj_copy = None
	c_ax = (False, False, False)
	if	 self.t_mode == 'X':  c_ax = (True, False, False)
	elif self.t_mode == 'Y':  c_ax = (False, True, False)
	elif self.t_mode == 'Z':  c_ax = (False, False, True)
	elif self.t_mode == 'XY': c_ax = (True, True, False)
	elif self.t_mode == 'YZ': c_ax = (False, True, True)
	elif self.t_mode == 'ZX': c_ax = (True, False, True)
	if self.t_mode != 'N':
		# mirror
		bpy.ops.transform.mirror(
			constraint_axis = c_ax,
			constraint_orientation = self.dlg_csys.transform_orientation,
			proportional = 'DISABLED',
			proportional_edit_falloff = 'SMOOTH',
			proportional_size = 1,
			release_confirm = False)
		#offset
		bpy.ops.transform.translate(
			value = (self.v_offs, self.v_offs, self.v_offs),
			constraint_axis = c_ax,
			constraint_orientation = self.dlg_csys.transform_orientation,
			mirror = False,
			proportional = 'DISABLED',
			proportional_edit_falloff = 'SMOOTH',
			proportional_size = 1,
			snap = False,
			snap_target = 'CLOSEST',
			snap_point = (0, 0, 0),
			snap_align = False,
			snap_normal = (0, 0, 0),
			texture_space = False,
			release_confirm = False)

#*********************************************************************************#

class BMAX_OM_Mirror_OT(Operator):
	bl_idname = "bmax.mirror_tool"
	bl_label = "Mirror"
	bl_description = "Mirror object dialog box"
	bl_options = {'REGISTER', 'UNDO'}

	old_xfrm = None
	obj_orig = None
	obj_copy = None
	dlg_csys = None

	v_offs = FloatProperty(default = 0)
	t_mode = EnumProperty(
		name = 'Axis', description = 'Mirror axis', default = 'N',
		items = [
			('N', 'None', 'None'),
			('X', 'X', 'X'),
			('Y', 'Y', 'Y'),
			('Z', 'Z', 'Z'),
			('XY', 'XY', 'XY'),
			('YZ', 'YZ', 'YZ'),
			('ZX', 'ZX', 'ZX')]
		)
	c_mode = EnumProperty(
		name = 'Clone Selection', description = 'Clone mode', default = 'ORIG',
		items = [('ORIG', 'No Clone', 'No Clone'),('COPY', 'Copy', 'Copy'),('INST', 'Instance', 'Instance')]
		)

	@classmethod
	def poll(self, ctx):
		return len(ctx.selected_objects) == 1 and ctx.active_object != None

	def check(self, ctx):
		bmaxMirror_Execute_OM(self, ctx)
		return True

	def cancel(self, ctx):
		if self.obj_copy != None:
			bpy.ops.object.delete(use_global = False)
			ctx.scene.objects.active = self.obj_orig
		self.obj_orig.select = True
		self.obj_orig.matrix_world = self.old_xfrm.copy()

	def draw(self, ctx):
		ui = self.layout
		b = ui.box()
		b.row().prop(self.dlg_csys, "transform_orientation", text = "Coord. System")
		b = ui.box()
		r = b.row()
		r.prop(self, "t_mode")
		r.prop(self, "v_offs", text = "Offset")
		r = b.row()
		r.prop(self, "c_mode")

	def execute(self, ctx):
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		self.obj_copy = None
		self.obj_orig = ctx.scene.objects.active
		self.old_xfrm = self.obj_orig.matrix_world.copy()
		self.dlg_csys = ctx.space_data
		bmaxMirror_Execute_OM(self, ctx)
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}

#*********************************************************************************#
# Object Mode : Clone
#*********************************************************************************#

class BMAX_OM_Clone_OT(Operator):
	bl_idname = "bmax.clone_tool"
	bl_label = "Clone Options"
	bl_description = "Clone object dialog box"
	bl_options = {'REGISTER', 'UNDO'}

	new_name = StringProperty(default = "Default")
	new_copy = BoolProperty(default = True)

	@classmethod
	def poll(self, ctx):
		return len(ctx.selected_objects) == 1 and ctx.active_object != None

	def draw(self, ctx):
		bx = self.layout.box()
		bx.row().prop(self, "new_name", text = "Name")
		bx.row().prop(self, "new_copy", text = "Copy")

	def execute(self, ctx):
		bpy.ops.object.duplicate(linked = not self.new_copy, mode = 'INIT')
		ctx.active_object.name = self.new_name
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		self.new_name = ctx.active_object.name
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}

#*********************************************************************************#
# Object Mode : Select From Scene / Unhide By Name / Unfreeze By Name
#*********************************************************************************#

# object list data type
class BMAX_ObjList(PropertyGroup):
	name = StringProperty()

# filter data type
class BMAX_ObjFilter(PropertyGroup):
	b_mesh = BoolProperty(default = False, description = "Show meshes")
	b_curv = BoolProperty(default = False, description = "Show splines")
	b_bone = BoolProperty(default = False, description = "Show bones")
	b_help = BoolProperty(default = False, description = "Show helpers")
	b_lamp = BoolProperty(default = False, description = "Show lights")
	b_cams = BoolProperty(default = False, description = "Show cameras")
	b_latt = BoolProperty(default = False, description = "Show lattices")
	b_surf = BoolProperty(default = False, description = "Show surfaces")
	b_meta = BoolProperty(default = False, description = "Show metaballs")
	b_font = BoolProperty(default = False, description = "Show fonts")
	b_spkr = BoolProperty(default = False, description = "Show speakers")

# name to object
def bmaxSelect_GetObjectFromName(ctx, name):
	for obj in ctx.scene.objects:
		if obj.name == name:
			return obj
	return None

# fill filtered object list
def bmaxSelect_FillList(self, ctx, mode):
	self.o_list.clear()
	for obj in ctx.scene.objects:
		if	(obj.type == 'MESH'		and self.o_filt.b_mesh == True) or	\
			(obj.type == 'CURVE'	and self.o_filt.b_curv == True) or	\
			(obj.type == 'SURFACE'	and self.o_filt.b_surf == True) or	\
			(obj.type == 'EMPTY'	and self.o_filt.b_help == True) or	\
			(obj.type == 'FONT'		and self.o_filt.b_font == True) or	\
			(obj.type == 'LAMP'		and self.o_filt.b_lamp == True) or	\
			(obj.type == 'CAMERA'	and self.o_filt.b_cams == True) or	\
			(obj.type == 'ARMATURE' and self.o_filt.b_bone == True) or	\
			(obj.type == 'META'		and self.o_filt.b_meta == True) or	\
			(obj.type == 'LATTICE'	and self.o_filt.b_latt == True) or	\
			(obj.type == 'SPEAKER'	and self.o_filt.b_spkr == True):
			do = False
			if mode == 'SELECT':
				if obj.hide == False and obj.hide_select == False:
					do = True
			elif mode == 'UNHIDE':
				if obj.hide == True:
					do = True
			elif mode == 'UNFREEZE':
				if obj.hide_select == True:
					do = True
			if do == True:
				item = self.o_list.add()
				item.name = obj.name
				item.type = obj.type

# display filter
def bmaxSelect_DrawFilter(self):
	row = self.layout.box().row()
	row.prop(self.o_filt, "b_mesh", text = "", icon = "OUTLINER_OB_MESH")
	row.prop(self.o_filt, "b_curv", text = "", icon = "OUTLINER_OB_CURVE")
	row.prop(self.o_filt, "b_bone", text = "", icon = "OUTLINER_OB_ARMATURE")
	row.prop(self.o_filt, "b_help", text = "", icon = "OUTLINER_OB_EMPTY")
	row.prop(self.o_filt, "b_lamp", text = "", icon = "OUTLINER_OB_LAMP")
	row.prop(self.o_filt, "b_cams", text = "", icon = "OUTLINER_OB_CAMERA")
	row.prop(self.o_filt, "b_latt", text = "", icon = "OUTLINER_OB_LATTICE")
	row.prop(self.o_filt, "b_surf", text = "", icon = "OUTLINER_OB_SURFACE")
	row.prop(self.o_filt, "b_meta", text = "", icon = "OUTLINER_OB_META")
	row.prop(self.o_filt, "b_font", text = "", icon = "OUTLINER_OB_FONT")
	row.prop(self.o_filt, "b_spkr", text = "", icon = "OUTLINER_OB_SPEAKER")

# display object selector
def bmaxSelect_DrawSelect(self):
	row = self.layout.box().row()
	row.prop_search(self, "o_name", self, "o_list", text = "Select Object:", icon = "OBJECT_DATAMODE")

#*********************************************************************************#

class BMAX_OM_SelectFromScene_OT(Operator):
	bl_idname = "bmax.select_from_scene"
	bl_label = "Select From Scene..."
	bl_description = "Select object from scene by name"
	bl_options = {'REGISTER', 'UNDO'}

	o_filt = PointerProperty(type = BMAX_ObjFilter)
	o_list = CollectionProperty(type = BMAX_ObjList)
	o_name = StringProperty()
	b_plus = BoolProperty(default = False)

	def check(self, ctx):
		bmaxSelect_FillList(self, ctx, 'SELECT')
		return False

	def draw(self, ctx):
		bmaxSelect_DrawFilter(self)
		self.layout.box().row().prop(self, "b_plus", text = "Extend Selection")
		bmaxSelect_DrawSelect(self)

	def execute(self, ctx):
		if self.b_plus == False:
			bpy.ops.object.select_all(action = 'DESELECT')
		obj = bmaxSelect_GetObjectFromName(ctx, self.o_name)
		if obj is not None:
			obj.select = True
			ctx.scene.objects.active = obj
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		bmaxSelect_FillList(self, ctx, 'SELECT')
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}

#*********************************************************************************#
# Object Mode : Unhide All / Hide (Un)selected
#*********************************************************************************#

# Unhide by name dialog
class BMAX_OM_UnhideByName_OT(Operator):
	bl_idname = "bmax.unhide_by_name"
	bl_label = "Unhide By Name..."
	bl_description = "Unhide object by name"
	bl_options = {'REGISTER', 'UNDO'}

	o_filt = PointerProperty(type = BMAX_ObjFilter)
	o_list = CollectionProperty(type = BMAX_ObjList)
	o_name = StringProperty()

	def check(self, ctx):
		bmaxSelect_FillList(self, ctx, 'UNHIDE')
		return False

	def draw(self, ctx):
		bmaxSelect_DrawFilter(self)
		bmaxSelect_DrawSelect(self)

	def execute(self, ctx):
		obj = bmaxSelect_GetObjectFromName(ctx, self.o_name)
		if obj is not None:
			obj.hide = False
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		bmaxSelect_FillList(self, ctx, 'UNHIDE')
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}

# Unhide All
class BMAX_OM_UnhideAll_OT(Operator):
	bl_idname = "bmax.unhide_all"
	bl_label = "Unhide All"
	bl_description = "Unhide all hidden objects"

	def execute(self, ctx):
		for obj in ctx.scene.objects:
			if obj.hide == True:
				obj.hide = False
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)

# Hide Selected
class BMAX_OM_HideSelected_OT(Operator):
	bl_idname = "bmax.hide_selected"
	bl_label = "Hide Selected"
	bl_description = "Hide all selected objects"

	def execute(self, ctx):
		for obj in ctx.selected_objects:
			obj.hide = True
		for obj in ctx.scene.objects:
			if obj.select == True:
				obj.select = False
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)

# Hide Unselected
class BMAX_OM_HideUnselected_OT(Operator):
	bl_idname = "bmax.hide_unselected"
	bl_label = "Hide Unselected"
	bl_description = "Hide all unselected objects"

	def execute(self, ctx):
		for obj in ctx.scene.objects:
			if obj.select == False:
				obj.hide = True
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)

# Sub-Menu for last 4 operators
class BMAX_OM_Hide_MT(Menu):
	bl_label = "Hide/Unhide"
	bl_description = "Hide/Unhide operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.hide_selected")
		ui.operator("bmax.hide_unselected")
		ui.separator()
		ui.operator("bmax.unhide_by_name")
		ui.operator("bmax.unhide_all")

#*********************************************************************************#
# Object Mode : Unfreeze All / Freeze (Un)selected
#*********************************************************************************#

# Unfreeze by name dialog
class BMAX_OM_UnfreezeByName_OT(Operator):
	bl_idname = "bmax.unfreeze_by_name"
	bl_label = "Unfreeze By Name..."
	bl_description = "Unfreeze object by name"
	bl_options = {'REGISTER', 'UNDO'}

	o_filt = PointerProperty(type = BMAX_ObjFilter)
	o_list = CollectionProperty(type = BMAX_ObjList)
	o_name = StringProperty()

	def check(self, ctx):
		bmaxSelect_FillList(self, ctx, 'UNFREEZE')
		return False

	def draw(self, ctx):
		bmaxSelect_DrawFilter(self)
		bmaxSelect_DrawSelect(self)

	def execute(self, ctx):
		obj = bmaxSelect_GetObjectFromName(ctx, self.o_name)
		if obj is not None:
			obj.hide_select = False
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		bmaxSelect_FillList(self, ctx, 'UNFREEZE')
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}

# Unfreeze All
class BMAX_OM_UnfreezeAll_OT(Operator):
	bl_idname = "bmax.unfreeze_all"
	bl_label = "Unfreeze All"
	bl_description = "Unfreeze all hidden objects"

	def execute(self, ctx):
		for obj in ctx.scene.objects:
			if obj.hide_select == True:
				obj.hide_select = False
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)

# Freeze Selected
class BMAX_OM_FreezeSelected_OT(Operator):
	bl_idname = "bmax.freeze_selected"
	bl_label = "Freeze Selected"
	bl_description = "Freeze all selected objects"

	def execute(self, ctx):
		for obj in ctx.selected_objects:
			obj.hide_select = True
		for obj in ctx.scene.objects:
			if obj.select == True:
				obj.select = False
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)

# Freeze Unselected
class BMAX_OM_FreezeUnselected_OT(Operator):
	bl_idname = "bmax.freeze_unselected"
	bl_label = "Freeze Unselected"
	bl_description = "Freeze all unselected objects"

	def execute(self, ctx):
		for obj in ctx.scene.objects:
			if obj.select == False:
				obj.hide_select = True
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)

# Sub-Menu for last 4 operators
class BMAX_OM_Freeze_MT(Menu):
	bl_label = "Freeze/Unfreeze"
	bl_description = "Freeze/Unfreeze operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.freeze_selected")
		ui.operator("bmax.freeze_unselected")
		ui.separator()
		ui.operator("bmax.unfreeze_by_name")
		ui.operator("bmax.unfreeze_all")

#*********************************************************************************#
# Object Mode : Group
#*********************************************************************************#

class BMAX_OM_Group_MT(Menu):
	bl_label = "Group"
	bl_description = "Group manipulation operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("group.create", text="Group")
		ui.operator("group.objects_remove", text="Detach From Group")
		ui.operator("group.objects_remove_all", text="Detach From All")
		ui.separator()
		ui.operator("group.objects_add_active", text="Attach To Active")
		ui.operator("group.objects_remove_active", text="Detach From Active")
		ui.separator()
		ui.operator("object.select_grouped", text="Select Grouped")

#*********************************************************************************#
# Any Mode : Link
#*********************************************************************************#

class BMAX_OM_Link_MT(Menu):
	bl_label = "Link"
	bl_description = "Hierarchy manipulation operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("object.parent_set", text="Link", icon = "LOCKVIEW_ON")
		ui.operator("object.parent_clear", text="Unlink", icon = "LOCKVIEW_OFF")
		ui.operator("object.parent_clear", text="Unlink Inverse").type = 'CLEAR_INVERSE'
		ui.operator("object.parent_clear", text="Unlink Keep XForm").type = 'CLEAR_KEEP_TRANSFORM'

class BMAX_AM_Link_MT(Menu):
	bl_label = "Link"
	bl_description = "Hierarchy manipulation operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("armature.parent_set", text="Link", icon = "LOCKVIEW_ON")
		ui.operator("armature.parent_clear", text="Unlink", icon = "LOCKVIEW_OFF")

class BMAX_PM_Link_MT(Menu):
	bl_label = "Link"
	bl_description = "Hierarchy manipulation operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("object.parent_set", text="Link", icon="LOCKVIEW_ON")
		ui.operator("object.parent_clear", text="Unlink", icon="LOCKVIEW_OFF")

#*********************************************************************************#
# Align Special
#*********************************************************************************#

class BMAX_OM_AlignPivot_MT(Menu):
	bl_label = "Align Special"
	bl_description = "Pivot and 3D Cursor manipulation operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("object.origin_set", text = "Object To Pivot").type='GEOMETRY_ORIGIN'
		ui.operator("object.origin_set", text = "Pivot To Object").type='ORIGIN_GEOMETRY'
		ui.operator("object.origin_set", text = "Pivot To Cursor").type='ORIGIN_CURSOR'
		ui.operator("object.origin_set", text = "Pivot To COM").type='ORIGIN_CENTER_OF_MASS'
		ui.separator()
		ui.operator("view3d.snap_cursor_to_center", text = "Cursor To Center")
		ui.operator("view3d.snap_cursor_to_active", text = "Cursor To Active")
		ui.operator("view3d.snap_cursor_to_selected", text = "Cursor To Selection")
		ui.operator("view3d.snap_cursor_to_grid", text = "Cursor To Grid")

#*********************************************************************************#

class BMAX_EM_EditAlign_MT(Menu):
	bl_label = "Align Special"
	bl_description = "Align selection to specified plane/point"
	def draw(self, ctx):
		ui = self.layout
		# average normal
		op = ui.operator("transform.resize", text = "Make Planar", icon = 'MANIPUL')
		op.constraint_axis = (False, False, True)
		op.value = (1,1,0)
		op.constraint_orientation = 'NORMAL'
		ui.separator()
		# local X
		op = ui.operator("transform.resize", text = "Make Planar - X", icon = 'AXIS_SIDE')
		op.constraint_axis = (True, False, False)
		op.value = (0,1,1)
		op.constraint_orientation = 'LOCAL'
		# local Y
		op = ui.operator("transform.resize", text = "Make Planar - Y", icon = 'AXIS_FRONT')
		op.constraint_axis = (False, True, False)
		op.value = (1,0,1)
		op.constraint_orientation = 'LOCAL'
		# local Z
		op = ui.operator("transform.resize", text = "Make Planar - Z", icon = 'AXIS_TOP')
		op.constraint_axis = (False, False, True)
		op.value = (1,1,0)
		op.constraint_orientation = 'LOCAL'
		# Blender native
		ui.separator()
		ui.operator("view3d.snap_selected_to_cursor", text = "Selection To Cursor")
		ui.operator("view3d.snap_selected_to_grid", text = "Selection To Grid")
		ui.separator()
		ui.operator("view3d.snap_cursor_to_center", text = "Cursor To Center")
		ui.operator("view3d.snap_cursor_to_active", text = "Cursor To Active")
		ui.operator("view3d.snap_cursor_to_selected", text = "Cursor To Selection")
		ui.operator("view3d.snap_cursor_to_grid", text = "Cursor To Grid")

#*********************************************************************************#

class BMAX_AM_EditAlign_MT(Menu):
	bl_label = "Align Special"
	bl_description = "Align selection to specified point"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("view3d.snap_selected_to_cursor", text = "Selection To Cursor")
		ui.operator("view3d.snap_selected_to_grid", text = "Selection To Grid")
		ui.separator()
		ui.operator("view3d.snap_cursor_to_center", text = "Cursor To Center")
		ui.operator("view3d.snap_cursor_to_active", text = "Cursor To Active")
		ui.operator("view3d.snap_cursor_to_selected", text = "Cursor To Selection")
		ui.operator("view3d.snap_cursor_to_grid", text = "Cursor To Grid")

#*********************************************************************************#
# Edit Mode : Sub-Object Selection
#*********************************************************************************#

# edit vertices
class BMAX_EM_SubObjectVerts_OT(Operator):
	bl_idname = "bmax.sub_object_verts"
	bl_label = "Edit Vertices"
	bl_description = "Select vertex sub-object level"
	def execute(self, ctx):
		ctx.tool_settings.mesh_select_mode = (True, False, False)
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# edit edges
class BMAX_EM_SubObjectEdges_OT(Operator):
	bl_idname = "bmax.sub_object_edges"
	bl_label = "Edit Edges"
	bl_description = "Select edge sub-object level"
	def execute(self, ctx):
		ctx.tool_settings.mesh_select_mode = (False, True, False)
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# edit faces
class BMAX_EM_SubObjectFaces_OT(Operator):
	bl_idname = "bmax.sub_object_faces"
	bl_label = "Edit Faces"
	bl_description = "Select face sub-object level"
	def execute(self, ctx):
		ctx.tool_settings.mesh_select_mode = (False, False, True)
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# edit edges+verts
class BMAX_EM_SubObjectEdgeVerts_OT(Operator):
	bl_idname = "bmax.sub_object_edge_verts"
	bl_label = "Edit Edges/Vertices"
	bl_description = "Select edge/vertex sub-object level"
	def execute(self, ctx):
		ctx.tool_settings.mesh_select_mode = (True, True, False)
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# Sub-Menu for last 4 operators
class BMAX_EM_SubObject_MT(Menu):
	bl_label = "Sub-Object"
	bl_description = "Select sub-object level"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.sub_object_verts", icon = 'VERTEXSEL')
		ui.operator("bmax.sub_object_edges", icon = 'EDGESEL')
		ui.operator("bmax.sub_object_faces", icon = 'FACESEL')
		ui.separator()
		ui.operator("bmax.sub_object_edge_verts", icon = 'SNAP_VERTEX')

class BMAX_EM_SelectSpecial_MT(Menu):
	bl_label = "Select Special"
	bl_description = "Select special sub-set"
	def draw(self, ctx):
		ui = self.layout
		if ctx.tool_settings.mesh_select_mode[1] == True or bmax_FULL == False:
			ui.operator("mesh.loop_multi_select", icon="UV_VERTEXSEL", text="Edge Loops").ring=False
			ui.operator("mesh.loop_multi_select", icon="UV_EDGESEL", text="Edge Rings").ring=True
		ui.operator("mesh.select_linked", icon="UV_ISLANDSEL", text="Select Element")

#*********************************************************************************#
# Edit Mode : Show/Hide Selection
#*********************************************************************************#

class BMAX_EM_ShowHideElement_MT(Menu):
	bl_label = "Hide/Unhide"
	bl_description = "Hide/Unhide operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("mesh.hide", text = "Hide Selected").unselected = False
		ui.operator("mesh.hide", text = "Hide Unselected").unselected = True
		ui.separator()
		ui.operator("mesh.reveal", text = "Unhide All")

#*********************************************************************************#
# Edit Mode : Create
#*********************************************************************************#

class BMAX_EM_Create_MT(Menu):
	bl_label = "Create"
	bl_description = "Create geometry operators"
	def draw(self, ctx):
		ui = self.layout
		mode = ctx.tool_settings.mesh_select_mode
		ui.operator("mesh.edge_face_add", text = "Face", icon = 'MESH_PLANE')
		ui.operator("mesh.fill", text = "Fill", icon = 'OUTLINER_DATA_MESH')
		ui.operator("mesh.fill_grid", text = "Grid Fill", icon = 'MESH_GRID')
		ui.operator("mesh.beautify_fill", text = "Beautify Fill", icon = 'MESH_ICOSPHERE')
		if mode[1] == True:
			ui.separator()
			ui.operator("mesh.bridge_edge_loops", text = "Bridge", icon = 'OUTLINER_DATA_LATTICE')

class BMAX_EM_Create_Panel_MT(Menu):
	bl_label = "Create"
	bl_description = "Create geometry operators"
	def draw(self, ctx):
		ui = self.layout
		mode = ctx.tool_settings.mesh_select_mode
		ui.operator("mesh.fill", text = "Fill", icon = 'OUTLINER_DATA_MESH')
		ui.operator("mesh.fill_grid", text = "Grid Fill", icon = 'MESH_GRID')
		ui.operator("mesh.beautify_fill", text = "Beautify Fill", icon = 'MESH_ICOSPHERE')
		if mode[1] == True:
			ui.separator()
			ui.operator("mesh.bridge_edge_loops", text = "Bridge", icon = 'OUTLINER_DATA_LATTICE')

#*********************************************************************************#
# Edit Mode : Slice
#*********************************************************************************#

class BMAX_EM_Slice_MT(Menu):
	bl_label = "Slice"
	bl_description = "Slice geometry operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("mesh.knife_tool", text = "Cut", icon = "OUTLINER_DATA_CURVE")
		ui.separator()
		ui.operator("mesh.subdivide", text = "Subdivide")
		ui.operator("mesh.loopcut_slide", text = "Slice Plane")
		ui.operator("mesh.offset_edge_loops_slide", text="Offset Edge")
		ui.operator("mesh.bisect", text = "Bisect")
		ui.separator()
		ui.operator("mesh.rip", text = "Break Vertex", icon = "MOD_EDGESPLIT")
		ui.operator("mesh.edge_split", text = "Split Edge", icon = "MOD_EDGESPLIT")

class BMAX_EM_Slice_Panel_MT(Menu):
	bl_label = "Slice"
	bl_description = "Slice geometry operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("mesh.subdivide", text = "Subdivide")
		ui.operator("mesh.loopcut_slide", text = "Slice Plane")
		ui.operator("mesh.offset_edge_loops_slide", text="Offset Edge")
		ui.operator("mesh.bisect", text = "Bisect")
		ui.separator()
		ui.operator("mesh.rip", text = "Break Vertex", icon = "MOD_EDGESPLIT")
		ui.operator("mesh.edge_split", text = "Split Edge", icon = "MOD_EDGESPLIT")

#*********************************************************************************#
# Edit Mode : Target Weld
#*********************************************************************************#

# fill filtered object list
def bmaxWeld_Check(ctx):
	b_snap = ctx.tool_settings.use_snap
	b_elem = ctx.tool_settings.snap_element
	b_targ = ctx.tool_settings.snap_target
	b_auto = ctx.tool_settings.use_mesh_automerge
	b_self = ctx.tool_settings.use_snap_self
	return b_elem == 'VERTEX' and b_targ == 'CLOSEST' and b_auto == True and b_snap == True and b_self == True

class BMAX_EM_TargetWeldOn_OT(Operator):
	bl_idname = "bmax.target_weld_on"
	bl_label = "Target Weld"
	bl_description = "Switch target weld on"
	def execute(self, ctx):
		ctx.tool_settings.snap_element = 'VERTEX'
		ctx.tool_settings.snap_target = 'CLOSEST'
		ctx.tool_settings.use_mesh_automerge = True
		ctx.tool_settings.use_snap_self = True
		ctx.tool_settings.use_snap = True
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

class BMAX_EM_TargetWeldOff_OT(Operator):
	bl_idname = "bmax.target_weld_off"
	bl_label = "Target Weld"
	bl_description = "Switch target weld off"
	def execute(self, ctx):
		ctx.tool_settings.snap_element = 'INCREMENT'
		ctx.tool_settings.use_mesh_automerge = False
		ctx.tool_settings.use_snap = False
		return {'FINISHED'}
	def invoke(self, ctx, event):
		return self.execute(ctx)

#*********************************************************************************#
# Edit Mode : Set Quad Diagonal
#*********************************************************************************#

class BMAX_EM_TurnQuadDiagonal_OT(Operator):
	bl_idname = "bmax.turn_quad_diagonal"
	bl_label = "Turn Edge"
	bl_description = "Turns quad's hidden diagonal edge"

	@classmethod
	def poll(self, ctx):
		return ctx.object.data.total_face_sel == 1

	def execute(self, ctx):
		bpy.ops.mesh.quads_convert_to_tris(quad_method='FIXED_ALTERNATE')
		bpy.ops.mesh.tris_convert_to_quads()
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)

#*********************************************************************************#
# Edit Mode : Mesh tools
#*********************************************************************************#

class BMAX_EM_Meshtools_MT(Menu):
	bl_label = "Mesh Tools"
	bl_description = "Selection of mesh tools"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.turn_quad_diagonal", icon="MAN_ROT")
		ui.operator("mesh.edge_rotate", text="Rotate Edge CW", icon="MAN_ROT").use_ccw=False
		ui.operator("mesh.edge_rotate", text="Rotate Edge CCW", icon="MAN_ROT").use_ccw=True
		ui.separator()
		ui.operator("transform.shrink_fatten", text = "Shrink/Fatten", icon="MESH_MONKEY")
		ui.operator("transform.tosphere", text = "Spherify", icon="MESH_ICOSPHERE")
		ui.operator("transform.shear", text = "Shear")
		ui.operator("transform.push_pull", text = "Push/Pull", icon="MOD_MESHDEFORM")
		ui.operator("mesh.inset", text="Inset", icon="MOD_MESHDEFORM")
		ui.operator("mesh.vertices_smooth", text="Smooth", icon="MOD_SMOOTH")
		ui.operator("mesh.bevel", text="Bevel", icon="MOD_BEVEL")
		ui.separator()
		ui.operator("mesh.vert_connect", text="Connect")
		ui.operator("transform.edge_slide", text="Slide Edge")
		ui.operator("transform.vert_slide", text="Slide Vertex")
		ui.separator()
		ui.operator("mesh.remove_doubles", text="Weld", icon="MOD_DISPLACE")
		ui.operator("mesh.merge", text="Merge", icon="STICKY_UVS_DISABLE")
		if bmax_FULL == False:
			ui.separator()
			ui.operator("mesh.flip_normals", text="Flip Normals")

#*********************************************************************************#
# Edit Mode : Repair
#*********************************************************************************#

# remove isolated geometry operator
class BMAX_EM_RemoveIsolatedGeometry_OT(Operator):
	bl_idname = "bmax.remove_isolated_geometry"
	bl_label = "Remove Isolated Geometry"
	bl_description = "Remove isolated vertices and edges"
	def execute(self, ctx):
		mode = ctx.tool_settings.mesh_select_mode
		bpy.ops.mesh.select_loose()
		if mode[0]:
			bpy.ops.mesh.delete(type='VERT')
		if mode[1]:
			bpy.ops.mesh.delete(type='EDGE')
		if mode[2]:
			bpy.ops.mesh.delete(type='FACE')
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# repair sub-menu
class BMAX_EM_Repair_MT(Menu):
	bl_label = "Repair Geometry"
	bl_description = "Mesh repair operators"
	def draw(self, ctx):
		ui = self.layout
		labl = "Remove Isolated Geometry"
		mode = ctx.tool_settings.mesh_select_mode
		if mode[0] and not mode [1] and not mode[2]:
			labl = "Remove Isolated Vertices"
		elif mode[1] and not mode [0] and not mode[2]:
			labl = "Remove Isolated Edges"
		elif mode[2] and not mode [0] and not mode[1]:
			labl = "Remove Isolated Faces"
		ui.operator("bmax.remove_isolated_geometry", text = labl)
		ui.operator("mesh.flip_normals", text = "Flip Normals")

#*********************************************************************************#
# Edit Mode : Clone
#*********************************************************************************#

class BMAX_EM_Clone_OT(Operator):
	bl_idname = "bmax.clone_mesh"
	bl_label = "Clone To Element"
	bl_description = "Clone selection into new element"
	def execute(self, ctx):
		bpy.ops.mesh.duplicate_move(
			MESH_OT_duplicate={"mode":1},
			TRANSFORM_OT_translate={
				"value":(0, 0, 0),
				"constraint_axis":(False, False, False),
				"constraint_orientation":'GLOBAL',
				"mirror":False,
				"proportional":'DISABLED',
				"proportional_edit_falloff":'SMOOTH',
				"proportional_size":1,
				"snap":False,
				"snap_target":'CLOSEST',
				"snap_point":(0, 0, 0),
				"snap_align":False,
				"snap_normal":(0, 0, 0),
				"texture_space":False,
				"release_confirm":False})
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

#*********************************************************************************#

class BMAX_EM_CloneCompact_MT(Menu):
	bl_label = "Clone/Detach"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.clone_mesh", icon="MOD_BOOLEAN")
		ui.separator()
		ui.operator("mesh.split", text="Detach To Element", icon="MOD_BUILD")
		ui.operator("mesh.separate", text="Detach To Object", icon="MOD_BUILD")

#*********************************************************************************#
# Edit Armature Mode : Create
#*********************************************************************************#

class BMAX_AM_CreatePrimitive_MT(Menu):
	bl_label = "Create"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("armature.bone_primitive_add", text="Single Bone", icon='BONE_DATA')

#*********************************************************************************#
# Edit Armature Mode : Bone Tools for compact mode
#*********************************************************************************#

class BMAX_AM_BoneToolsCompact_MT(Menu):
	bl_label = "Bone Tools"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("armature.subdivide", text="Refine", icon="GROUP_BONE")
		ui.operator("armature.merge", text="Merge Chain", icon="BONE_DATA")
		ui.operator("armature.fill", text="Connect Bones")
		ui.separator()
		ui.operator("transform.transform", text="Roll").mode='BONE_ROLL'
		ui.operator("armature.calculate_roll", text="Set Roll", icon="OUTLINER_DATA_EMPTY")

#*********************************************************************************#
# Edit Armature Mode : Mirror
#*********************************************************************************#

def bmaxMirror_Execute_AM(self, ctx):
	ctx.space_data.transform_orientation = self.c_mode
	for i, b in enumerate(ctx.selected_bones):
		b.head = self.bone_list[i][0].copy()
		b.tail = self.bone_list[i][1].copy()
		b.roll = self.bone_list[i][2]

	c_ax = (False, False, False)
	if	 self.t_mode == 'X':  c_ax = (True, False, False)
	elif self.t_mode == 'Y':  c_ax = (False, True, False)
	elif self.t_mode == 'Z':  c_ax = (False, False, True)
	elif self.t_mode == 'XY': c_ax = (True, True, False)
	elif self.t_mode == 'YZ': c_ax = (False, True, True)
	elif self.t_mode == 'ZX': c_ax = (True, False, True)
	if self.t_mode != 'N':
		# mirror
		bpy.ops.transform.mirror(
			constraint_axis = c_ax,
			constraint_orientation = self.c_mode,
			proportional = 'DISABLED',
			proportional_edit_falloff = 'SMOOTH',
			proportional_size = 1,
			release_confirm = False)
		#offset
		bpy.ops.transform.translate(
			value = (self.v_offs, self.v_offs, self.v_offs),
			constraint_axis = c_ax,
			constraint_orientation = self.c_mode,
			mirror = False,
			proportional = 'DISABLED',
			proportional_edit_falloff = 'SMOOTH',
			proportional_size = 1,
			snap = False,
			snap_target = 'CLOSEST',
			snap_point = (0, 0, 0),
			snap_align = False,
			snap_normal = (0, 0, 0),
			texture_space = False,
			release_confirm = False)

#*********************************************************************************#

class BMAX_AM_Mirror_OT(Operator):
	bl_idname = "bmax.mirror_bone_tool"
	bl_label = "Mirror"
	bl_description = "Mirror bone dialog box"
	bl_options = {'REGISTER', 'UNDO'}

	bone_list = []

	v_offs = FloatProperty(default = 0)
	t_mode = EnumProperty(
		name = 'Axis', description = 'Mirror axis', default = 'N',
		items = [
			('N', 'None', 'None'),
			('X', 'X', 'X'),
			('Y', 'Y', 'Y'),
			('Z', 'Z', 'Z'),
			('XY', 'XY', 'XY'),
			('YZ', 'YZ', 'YZ'),
			('ZX', 'ZX', 'ZX')]
		)
	c_mode = EnumProperty(
		name = 'Coord. System', description = 'Coordinate System', default = 'GLOBAL',
		items = [
			('GLOBAL', 'Global', 'Global'),
			('LOCAL', 'Local', 'Local')]
		)

	@classmethod
	def poll(self, ctx):
		return ctx.active_bone != None and len(ctx.selected_bones) > 0

	def check(self, ctx):
		bmaxMirror_Execute_AM(self, ctx)
		return True

	def cancel(self, ctx):
		for i, b in enumerate(ctx.selected_bones):
			b.head = self.bone_list[i][0].copy()
			b.tail = self.bone_list[i][1].copy()
			b.roll = self.bone_list[i][2]

	def draw(self, ctx):
		ui = self.layout
		b = ui.box()
		b.row().prop(self, "c_mode")
		b = ui.box()
		r = b.row()
		r.prop(self, "t_mode")
		r.prop(self, "v_offs", text = "Offset")

	def execute(self, ctx):
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		self.bone_list = []
		for b in ctx.selected_bones:
			self.bone_list.append([b.head.copy(), b.tail.copy(), b.roll])
		bmaxMirror_Execute_AM(self, ctx)
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}

#*********************************************************************************#
# Edit Armature Mode : Clone
#*********************************************************************************#

class BMAX_AM_Clone_OT(Operator):
	bl_idname = "bmax.clone_bones"
	bl_label = "Clone To Element"
	bl_description = "Clone selection into new element"
	def execute(self, ctx):
		bpy.ops.armature.duplicate_move(
			ARMATURE_OT_duplicate={},
			TRANSFORM_OT_translate={"value":(0, 0, 0),
				"constraint_axis":(False, False, False),
				"constraint_orientation":'GLOBAL',
				"mirror":False,
				"proportional":'DISABLED',
				"proportional_edit_falloff":'SMOOTH',
				"proportional_size":1,
				"snap":False,
				"snap_target":'CLOSEST',
				"snap_point":(0, 0, 0),
				"snap_align":False,
				"snap_normal":(0, 0, 0),
				"texture_space":False,
				"release_confirm":False})
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

#*********************************************************************************#
# Edit Armature/Pose Mode : Auto-Names
#*********************************************************************************#

class BMAX_AM_AutoNames_MT(Menu):
	bl_label = "Auto-Names"
	bl_description = "Automatic name generators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("armature.autoside_names", text="Mirror Names - Left/Right").type='XAXIS'
		ui.operator("armature.autoside_names", text="Mirror Names - Front/Back").type='YAXIS'
		ui.operator("armature.autoside_names", text="Mirror Names - Top/Bottom").type='ZAXIS'
		ui.operator("armature.flip_names", text="Flip Names")

class BMAX_PM_AutoNames_MT(Menu):
	bl_label = "Auto-Names"
	bl_description = "Automatic name generators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("pose.autoside_names", text="Mirror Names - Left/Right").axis='XAXIS'
		ui.operator("pose.autoside_names", text="Mirror Names - Front/Back").axis='YAXIS'
		ui.operator("pose.autoside_names", text="Mirror Names - Top/Bottom").axis='ZAXIS'
		ui.operator("pose.flip_names", text="Flip Names")

#*********************************************************************************#
# Edit Armature/Pose Mode : Hide/Unhide
#*********************************************************************************#

class BMAX_AM_Hide_MT(Menu):
	bl_label = "Hide/Unhide"
	bl_description = "Hide/Unhide operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("armature.hide", text="Hide Selected").unselected=False
		ui.operator("armature.hide", text="Hide Unselected").unselected=True
		ui.separator()
		ui.operator("armature.reveal", text="Unhide All")

class BMAX_PM_Hide_MT(Menu):
	bl_label = "Hide/Unhide"
	bl_description = "Hide/Unhide operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("pose.hide", text="Hide Selected").unselected=False
		ui.operator("pose.hide", text="Hide Unselected").unselected=True
		ui.separator()
		ui.operator("pose.reveal", text="Unhide All")

#*********************************************************************************#
# Edit Pose Mode : Pose Library
#*********************************************************************************#

class BMAX_PM_PoseTools_MT(Menu):
	bl_label = "Poses"
	bl_description = "Pose tools"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("pose.copy", text="Copy", icon="COPYDOWN")
		ui.operator("pose.paste", text="Paste", icon="PASTEDOWN").flipped=False
		ui.operator("pose.paste", text="Paste Opposite", icon="PASTEFLIPDOWN").flipped=True
		ui.separator()
		ui.operator("poselib.pose_add", text="Save To Library", icon="DISCLOSURE_TRI_RIGHT")
		ui.operator("poselib.pose_remove", text="Delete From Library", icon="DISCLOSURE_TRI_DOWN")
		ui.operator("poselib.pose_rename", text="Rename")
		ui.operator("poselib.browse_interactive", text="Browse Library")

class BMAX_PM_PoseLibrary_MT(Menu):
	bl_label = "Pose Library"
	bl_description = "Pose library access"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("poselib.pose_add", text="Save Pose", icon="DISCLOSURE_TRI_RIGHT")
		ui.operator("poselib.pose_remove", text="Delete Pose", icon="DISCLOSURE_TRI_DOWN")
		ui.operator("poselib.pose_rename", text="Rename Pose")
		ui.operator("poselib.browse_interactive", text="Browse Library")

#*********************************************************************************#
# Edit Object/Pose Mode : Constraints
#*********************************************************************************#

class BMAX_OM_Constraints_MT(Menu):
	bl_label = "Animation Constraints"
	bl_description = "Animation constraint tools"
	def draw(self, ctx):
		ui = self.layout
		ui.operator_menu_enum("object.constraint_add", "type", text="Add (With Targets)", icon="DISCLOSURE_TRI_RIGHT")
		ui.operator("object.constraints_clear", text="Clear Constraints", icon="DISCLOSURE_TRI_DOWN")
		ui.operator("object.constraints_copy", text="Copy To Selected", icon="ARROW_LEFTRIGHT")

class BMAX_PM_Constraints_MT(Menu):
	bl_label = "Animation Constraints"
	bl_description = "Animation constraint tools"
	def draw(self, ctx):
		ui = self.layout
		ui.operator_menu_enum("pose.constraint_add", "type", text="Add (With Targets)", icon="DISCLOSURE_TRI_RIGHT")
		ui.operator("pose.constraints_clear", text="Clear Constraints", icon="DISCLOSURE_TRI_DOWN")
		ui.operator("pose.constraints_copy", text="Copy To Selected", icon="ARROW_LEFTRIGHT")

#*********************************************************************************#
# Curve Edit Mode : Show/Hide Selection
#*********************************************************************************#

class BMAX_CM_Hide_MT(Menu):
	bl_label = "Hide/Unhide"
	bl_description = "Hide/unhide operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("curve.hide", text = "Hide Selected").unselected = False
		ui.operator("curve.hide", text = "Hide Unselected").unselected = True
		ui.separator()
		ui.operator("curve.reveal", text = "Unhide All")

#*********************************************************************************#
# Curve Edit Mode : Clone
#*********************************************************************************#

class BMAX_CM_Clone_OT(Operator):
	bl_idname = "bmax.clone_curve"
	bl_label = "Clone To Element"
	bl_description = "Clone selection into new element"
	def execute(self, ctx):
		bpy.ops.curve.duplicate_move(
			CURVE_OT_duplicate={"mode":1},
			TRANSFORM_OT_translate={
				"value":(0, 0, 0),
				"constraint_axis":(False, False, False),
				"constraint_orientation":'GLOBAL',
				"mirror":False,
				"proportional":'DISABLED',
				"proportional_edit_falloff":'SMOOTH',
				"proportional_size":1,
				"snap":False,
				"snap_target":'CLOSEST',
				"snap_point":(0, 0, 0),
				"snap_align":False,
				"snap_normal":(0, 0, 0),
				"texture_space":False,
				"release_confirm":False})
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

#*********************************************************************************#
# 3D View background toggle
#*********************************************************************************#

class BMAX_ViewportBackground_OT(Operator):
	bl_idname = "bmax.viewport_background"
	bl_label = "3D View Color"
	bl_description = "Cycle 3D view background colors"

	i_indx = IntProperty(default = 1)

	def execute(self, ctx):
		grad = ctx.user_preferences.themes[0].view_3d.space.gradients
		grad.show_grad = False

		if self.i_indx == 1:
			#black
			grad.high_gradient[0] = 0.0
			grad.high_gradient[1] = 0.0
			grad.high_gradient[2] = 0.0
		elif self.i_indx == 2:
			#7f7f7f - XSI
			grad.high_gradient[0] = 0.498
			grad.high_gradient[1] = 0.498
			grad.high_gradient[2] = 0.498
		elif self.i_indx == 3:
			#a2a2a2 - maya light
			grad.high_gradient[0] = 0.635
			grad.high_gradient[1] = 0.635
			grad.high_gradient[2] = 0.635
		elif self.i_indx == 4:
			#697b8f - maya gradient
			grad.show_grad = True
			grad.gradient[0] = 0.0
			grad.gradient[1] = 0.0
			grad.gradient[2] = 0.0
			grad.high_gradient[0] = 0.412
			grad.high_gradient[1] = 0.482
			grad.high_gradient[2] = 0.561
		elif self.i_indx == 5:
			#dark blue gradient
			grad.show_grad = True
			grad.gradient[0] = 0.251
			grad.gradient[1] = 0.251
			grad.gradient[2] = 0.251
			grad.high_gradient[0] = 0.267
			grad.high_gradient[1] = 0.302
			grad.high_gradient[2] = 0.341
		else:
			#4b4b4b
			grad.high_gradient[0] = 0.294
			grad.high_gradient[1] = 0.294
			grad.high_gradient[2] = 0.294

		if self.i_indx == 5:
			self.i_indx = 0
		else:
			self.i_indx += 1
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)

# selection menu
class BMAX_PickViewportBackground_MT(Menu):
	bl_label = "Viewport Background"
	bl_description = "3D viewport background color"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.viewport_background", text="Elsyiun").i_indx = 0
		ui.operator("bmax.viewport_background", text="Black").i_indx = 1
		ui.operator("bmax.viewport_background", text="XSI").i_indx = 2
		ui.operator("bmax.viewport_background", text="Maya Light").i_indx = 3
		ui.operator("bmax.viewport_background", text="Maya Gradient").i_indx = 4
		ui.operator("bmax.viewport_background", text="Grey Blue Gradient").i_indx = 5

#*********************************************************************************#
# Object display settings
#*********************************************************************************#

def bmaxObjectDisplay_CheckMeshObject(ctx):
	if ctx.active_object and ctx.mode == 'OBJECT':
		return (ctx.active_object.type == 'MESH')
	return False

# wireframe toggle
class BMAX_OM_ObjectWireframeToggle_OT(Operator):
	bl_idname = "bmax.object_wireframe_toggle"
	bl_label = "Edged Faces"
	bl_description = "Show/hide edged faces"
	@classmethod
	def poll(self, ctx):
		return bmaxObjectDisplay_CheckMeshObject(ctx)
	def execute(self, ctx):
		if ctx.active_object.show_wire and ctx.active_object.show_all_edges:
			ctx.active_object.show_wire = False
			ctx.active_object.show_all_edges = False
		else:
			ctx.active_object.show_wire = True
			ctx.active_object.show_all_edges = True
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# smooth shading
class BMAX_OM_ObjectShadeSmooth_OT(Operator):
	bl_idname = "bmax.object_shade_smooth"
	bl_label = "Shade Smooth"
	bl_description = "Set smooth shading for active mesh object"
	@classmethod
	def poll(self, ctx):
		return bmaxObjectDisplay_CheckMeshObject(ctx) and len(ctx.selected_objects) > 0
	def execute(self, ctx):
		bpy.ops.object.shade_smooth()
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# flat shading
class BMAX_OM_ObjectShadeFlat_OT(Operator):
	bl_idname = "bmax.object_shade_flat"
	bl_label = "Shade Flat"
	bl_description = "Set flat shading for active mesh object"
	@classmethod
	def poll(self, ctx):
		return bmaxObjectDisplay_CheckMeshObject(ctx) and len(ctx.selected_objects) > 0
	def execute(self, ctx):
		bpy.ops.object.shade_flat()
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# set scene OpenGL light
class BMAX_OM_SetSceneLighting_OT(Operator):
	bl_idname = "bmax.set_scene_lighting"
	bl_label = "Solid OpenGL Scene Light"
	bl_description = "Access OpenGL scene light properties"

	s_text = "Reset Solid Light Properties"
	v_ldir = []
	c_diff = []
	c_spec = []
	b_defs = BoolProperty(default = False)

	@classmethod
	def poll(self, ctx):
		return (ctx.space_data.use_matcap == False)

	def check(self, ctx):
		if self.b_defs == True:
			ctx.user_preferences.system.solid_lights[0].direction[0] = -0.009523809887468815
			ctx.user_preferences.system.solid_lights[0].direction[1] = 0.17142857611179352
			ctx.user_preferences.system.solid_lights[0].direction[2] = 0.9851505756378174
			for i in range(0,3): ctx.user_preferences.system.solid_lights[0].diffuse_color[i] = 0.944
			for i in range(0,3): ctx.user_preferences.system.solid_lights[0].specular_color[i] = 0.0
			self.s_text = "Reset successful. Click again to continue edit."
		else:
			self.s_text = "Reset Solid Light Properties"
		return True

	def draw(self, ctx):
		ui = self.layout
		ui.label("Light direction:")
		ui.prop(ctx.user_preferences.system.solid_lights[0], "direction", text="")
		r = ui.row()
		r.label("Diffuse color:")
		r.label("Specular color:")
		r = ui.row()
		r.prop(ctx.user_preferences.system.solid_lights[0], "diffuse_color", text="")
		r.prop(ctx.user_preferences.system.solid_lights[0], "specular_color", text="")
		ui.prop(self, "b_defs", text=self.s_text, icon="LAMP")

	def cancel(self, ctx):
		for i in range(0,3): ctx.user_preferences.system.solid_lights[0].direction[i] = self.v_ldir[i]
		for i in range(0,3): ctx.user_preferences.system.solid_lights[0].diffuse_color[i] = self.c_diff[i]
		for i in range(0,3): ctx.user_preferences.system.solid_lights[0].specular_color[i] = self.c_spec[i]

	def execute(self, ctx):
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		self.b_defs = False
		self.v_ldir = ctx.user_preferences.system.solid_lights[0].direction.copy()
		self.c_diff = ctx.user_preferences.system.solid_lights[0].diffuse_color.copy()
		self.c_spec = ctx.user_preferences.system.solid_lights[0].specular_color.copy()
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}

# menu for last 4 operators
class BMAX_ObjectDisplay_MT(Menu):
	bl_label = "Object Display"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.object_wireframe_toggle", icon="WIRE")
		ui.operator("bmax.object_shade_flat", icon="MESH_ICOSPHERE")
		ui.operator("bmax.object_shade_smooth", icon="MATSPHERE")
		ui.separator()
		ui.prop(ctx.space_data, "use_matcap", icon="IMAGEFILE", text="Use Scene Matcap")
		ui.operator("bmax.set_scene_lighting", icon="LAMP")

#*********************************************************************************#
# 3D View settings
#*********************************************************************************#

class BMAX_Viewport_MT(Menu):
	bl_label = "Viewport Settings"
	bl_description = "3D Viewport settings"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("view3d.view_persportho", text="Perspective Toggle", icon = "OUTLINER_DATA_CAMERA")
		ui.separator()
		ui.operator("view3d.viewnumpad", text = "Front Ortho", icon = "ARMATURE_DATA").type='FRONT'
		ui.operator("view3d.viewnumpad", text = "Left Ortho", icon = "TRIA_LEFT").type='LEFT'
		ui.operator("view3d.viewnumpad", text = "Top Ortho", icon = "TRIA_UP").type='TOP'
		ui.operator("view3d.viewnumpad", text = "Back Ortho", icon = "ARMATURE_DATA").type='BACK'
		ui.operator("view3d.viewnumpad", text = "Right Ortho", icon = "TRIA_RIGHT").type='RIGHT'
		ui.operator("view3d.viewnumpad", text = "Bottom Ortho", icon = "TRIA_DOWN").type='BOTTOM'
		ui.separator()
		if bmax_FULL == True:
			ui.menu("BMAX_ObjectDisplay_MT", icon="MATCUBE")
			ui.separator()
		ui.operator("wm.context_menu_enum", text="Viewport Shading", icon="BBOX").data_path='space_data.viewport_shade'
		if bmax_FULL == True:
			ui.operator("wm.call_menu", text="Viewport Background", icon="IMAGE_ALPHA").name='BMAX_PickViewportBackground_MT'
		ui.separator()
		if ctx.screen.show_fullscreen:
			ui.operator("screen.screen_full_area", text="Restore Viewport", icon="SPLITSCREEN")
		else:
			ui.operator("screen.screen_full_area", text="Maximize Viewport", icon="FULLSCREEN")

#*********************************************************************************#
# Blender 3ds Max tools emulation : Right-Click Menu Toggle
#*********************************************************************************#

class BMAX_RightClickToggle_OP(Operator):
	bl_idname = "bmax.toggle_right_click_menu"
	bl_label = "Right-Click Menu Toggle"
	bl_description = "Toggle right-click context menu on/off"

	def execute(self, ctx):
		wm = bpy.context.window_manager

		b_found = False
		km = wm.keyconfigs.addon.keymaps['3D View']
		for kmi in km.keymap_items:
			if kmi.idname == 'wm.call_menu':
				if kmi.properties.name == "BMAX_MT_ToolMenu":
					km.keymap_items.remove(kmi)
					b_found = True
					break
		if b_found == False:
			km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
			kmi = km.keymap_items.new('wm.call_menu', 'RIGHTMOUSE', 'PRESS')
			kmi.properties.name = "BMAX_MT_ToolMenu"

		km = wm.keyconfigs.addon.keymaps['UV Editor']
		b_found = False
		for kmi in km.keymap_items:
			if kmi.idname == 'wm.call_menu':
				if kmi.properties.name == "BMAX_MT_ToolMenuUV":
					km.keymap_items.remove(kmi)
					b_found = True
					break
		if b_found == False:
			km = wm.keyconfigs.addon.keymaps.new(name='UV Editor', space_type='EMPTY')
			kmi = km.keymap_items.new('wm.call_menu', 'RIGHTMOUSE', 'PRESS')
			kmi.properties.name = "BMAX_MT_ToolMenuUV"

		b_found = False
		km = wm.keyconfigs.addon.keymaps['Graph Editor']
		for kmi in km.keymap_items:
			if kmi.idname == 'wm.call_menu':
				if kmi.properties.name == "BMAX_MT_ToolMenuGraph":
					km.keymap_items.remove(kmi)
					b_found = True
					break
		if b_found == False:
			km = wm.keyconfigs.addon.keymaps.new(name='Graph Editor', space_type='GRAPH_EDITOR')
			kmi = km.keymap_items.new('wm.call_menu', 'RIGHTMOUSE', 'PRESS')
			kmi.properties.name = "BMAX_MT_ToolMenuGraph"

		b_found = False
		km = wm.keyconfigs.addon.keymaps['Dopesheet']
		for kmi in km.keymap_items:
			if kmi.idname == 'wm.call_menu':
				if kmi.properties.name == "BMAX_MT_ToolMenuDopesheet":
					km.keymap_items.remove(kmi)
					b_found = True
					break
		if b_found == False:
			km = wm.keyconfigs.addon.keymaps.new(name='Dopesheet', space_type='DOPESHEET_EDITOR')
			kmi = km.keymap_items.new('wm.call_menu', 'RIGHTMOUSE', 'PRESS')
			kmi.properties.name = "BMAX_MT_ToolMenuDopesheet"

		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)


#*********************************************************************************#
# Blender 3ds Max tools emulation : generic helpers
#*********************************************************************************#

def bmax_GetMeshSubObject(mode):
	t = "Edit Custom"
	i = "SNAP_FACE"
	if mode[0] and mode [1] and not mode[2]:
		t = "Edit Edges/Vertices"
		i = "SNAP_VERTEX"
	elif mode[0] and not mode[1] and not mode[2]:
		t = "Edit Vertices"
		i = "VERTEXSEL"
	elif mode[1] and not mode[0] and not mode[2]:
		t = "Edit Edges"
		i = "EDGESEL"
	elif mode[2] and not mode[1] and not mode[0]:
		t = "Edit Faces"
		i = "FACESEL"
	return t, i

#*********************************************************************************#
# Blender 3ds Max tools emulation : Right-Click Menu
#*********************************************************************************#

class BMAX_MT_ToolMenu(Menu):
	bl_label = "BMax Tools"
	bl_description = "BMax right-click menu"

	def draw(self, ctx):
		ui = self.layout
		ui.operator_context = 'INVOKE_REGION_WIN'

		ui.operator("screen.redo_last", text = "Edit Last Action...", icon = "UI")
		ui.separator()

		if ctx.mode == 'OBJECT':
			ui.menu("INFO_MT_add", text = "Create", icon="SOLO_ON")
			ui.menu("BMAX_OM_Hide_MT", icon="RESTRICT_VIEW_OFF")
			ui.menu("BMAX_OM_Freeze_MT", icon="FREEZE")
			if bmax_FULL == True:
				ui.operator("bmax.select_from_scene", text="Select From Scene...", icon="RESTRICT_SELECT_OFF")
			ui.separator()
			if ctx.active_object and ctx.active_object.type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE', 'LATTICE'}:
				ui.operator("object.mode_set", text="Edit Object", icon="EDITMODE_HLT").mode='EDIT'
				if ctx.active_object.type == 'ARMATURE':
					ui.operator("object.mode_set", text="Edit Pose", icon="POSE_HLT").mode='POSE'
			else:
				ui.operator("object.mode_set", text="Edit Object", icon="EDITMODE_HLT")
			ui.separator()
			ui.menu("BMAX_OM_Link_MT", icon="LINK_AREA")
			if bmax_FULL == True:
				ui.menu("BMAX_OM_Group_MT", icon="GROUP")
			ui.operator("object.join", text="Attach")
			ui.separator()
			ui.operator("bmax.align_tool", text="Align Selection...", icon="ALIGN")
			ui.menu("BMAX_OM_AlignPivot_MT", icon="ALIGN")
			ui.operator("bmax.mirror_tool", text="Mirror...", icon="MOD_MIRROR")
			ui.operator("bmax.clone_tool", icon="MOD_BOOLEAN")
			op = ui.operator("object.transform_apply", text="Reset XForm")
			op.rotation = True
			op.scale = True
			ui.separator()

		# edit mesh
		elif ctx.mode == 'EDIT_MESH':
			ui.menu("INFO_MT_mesh_add", text="Create", icon='SOLO_ON')
			t, i = bmax_GetMeshSubObject(ctx.tool_settings.mesh_select_mode)
			ui.menu("BMAX_EM_SubObject_MT", icon=i)
			ui.menu("BMAX_EM_ShowHideElement_MT", icon="RESTRICT_VIEW_OFF")
			ui.prop(ctx.space_data, "use_occlude_geometry", text="Ignore Backfacing")
			ui.separator()
			ui.menu("BMAX_EM_SelectSpecial_MT", icon="RESTRICT_SELECT_OFF")
			ui.separator()
			ui.menu("BMAX_EM_EditAlign_MT", icon="ALIGN")
			if bmax_FULL == True:
				ui.operator("bmax.clone_mesh", icon="MOD_BOOLEAN")
				ui.operator("mesh.split", text="Detach To Element", icon="MOD_BUILD")
				ui.operator("mesh.separate", text="Detach To Object", icon="MOD_BUILD")
			else:
				ui.menu("BMAX_EM_CloneCompact_MT", icon="MOD_BOOLEAN")
			ui.separator()
			ui.menu("BMAX_EM_Create_MT", icon="SNAP_FACE")
			ui.menu("BMAX_EM_Slice_MT", icon="MOD_DECIM")
			ui.menu("VIEW3D_MT_edit_mesh_extrude", icon="CURVE_PATH")
			if bmax_FULL == True:
				ui.menu("BMAX_EM_Repair_MT", icon="MODIFIER")
			ui.separator()
			#tools
			ui.menu("BMAX_EM_Meshtools_MT", icon="GRID")
			if bmaxWeld_Check(ctx):
				ui.operator("bmax.target_weld_off", icon="SNAP_ON")
			else:
				if ctx.tool_settings.use_mesh_automerge == True:
					ui.operator("bmax.target_weld_off", icon="AUTOMERGE_ON")
				else:
					ui.operator("bmax.target_weld_on", icon="SNAP_OFF")
			ui.separator()
			###
			ui.menu("VIEW3D_MT_uv_map", icon="MOD_UVPROJECT")
			ui.operator("mesh.mark_seam", text="Set Seams")
			if bmax_FULL == True:
				ui.operator("mesh.mark_seam", text="Clear Seams").clear=True
			ui.separator()

		# edit armature
		elif ctx.mode == 'EDIT_ARMATURE':
			ui.menu("BMAX_AM_CreatePrimitive_MT", icon="SOLO_ON")
			ui.menu("BMAX_AM_Hide_MT", icon="RESTRICT_VIEW_OFF")
			ui.menu("BMAX_AM_AutoNames_MT", icon="SCRIPTWIN")
			ui.separator()
			ui.operator("object.mode_set", text="Edit Pose", icon="POSE_HLT").mode='POSE'
			ui.separator()
			ui.menu("BMAX_AM_Link_MT", icon="LINK_AREA")
			ui.separator()
			ui.menu("BMAX_AM_EditAlign_MT", icon="ALIGN")
			ui.operator("bmax.mirror_bone_tool", text="Mirror...", icon="MOD_MIRROR")
			ui.operator("bmax.clone_bones", icon="MOD_BOOLEAN")
			ui.operator("armature.separate", text="Detach To Object", icon="MOD_BUILD")
			ui.separator()
			ui.operator("armature.extrude", text="Extrude", icon="CURVE_PATH")
			if bmax_FULL == True:
				ui.operator("armature.subdivide", text="Refine", icon="GROUP_BONE")
				ui.operator("armature.merge", text="Merge Chain", icon="BONE_DATA")
				ui.operator("armature.fill", text="Connect Bones")
				ui.separator()
				ui.operator("transform.transform", text="Roll").mode='BONE_ROLL'
				ui.operator("armature.calculate_roll", text="Set Roll", icon="OUTLINER_DATA_EMPTY")
			else:
				ui.menu("BMAX_AM_BoneToolsCompact_MT", icon="GROUP_BONE")
			ui.operator("armature.switch_direction", text="Flip Direction")
			ui.separator()

		# edit pose
		elif ctx.mode == 'POSE':
			ui.menu("BMAX_PM_Hide_MT", icon="RESTRICT_VIEW_OFF")
			ui.menu("BMAX_PM_AutoNames_MT", icon="SCRIPTWIN")
			ui.separator()
			ui.operator("object.mode_set", text="Edit Bones", icon="EDITMODE_HLT").mode='EDIT'
			ui.separator()
			ui.menu("BMAX_PM_Link_MT", icon="LINK_AREA")
			ui.separator()
			ui.menu("BMAX_AM_EditAlign_MT", icon="ALIGN")
			ui.separator()
			ui.operator("pose.armature_apply", text="Freeze Transform", icon="NDOF_DOM")
			ui.operator("pose.transforms_clear", text="Transform To Zero", icon="ARMATURE_DATA")
			ui.operator("pose.rot_clear", text="Rotation To Zero")
			ui.operator("pose.quaternions_flip", text="Flip Rotation")
			ui.separator()
			ui.menu("BMAX_PM_PoseTools_MT", icon="POSE_DATA")
			ui.separator()

		# edit curve
		elif ctx.mode == 'EDIT_CURVE':
			ui.menu("INFO_MT_curve_add", text="Create", icon='SOLO_ON')
			ui.menu("BMAX_CM_Hide_MT", icon="RESTRICT_VIEW_OFF")
			ui.separator()
			ui.menu("VIEW3D_MT_snap", "Align Special", icon="ALIGN")
			ui.operator("transform.mirror", text="Mirror", icon="MOD_MIRROR")
			ui.operator("bmax.clone_curve", text="Clone To Element", icon="MOD_BOOLEAN")
			ui.operator("curve.separate", text="Detach To Object", icon="MOD_BUILD")
			ui.separator()
			ui.operator("curve.make_segment", text="Create Segment", icon="SPHERECURVE")
			ui.operator("curve.handle_type_set", icon="CURVE_BEZCURVE")
			ui.operator("curve.subdivide")
			ui.operator("curve.switch_direction", text="Reverse Direction")
			ui.operator("transform.tilt", icon="MAN_TRANS")
			ui.operator("curve.tilt_clear", icon="MAN_TRANS")
			ui.separator()

		if ctx.mode in {'OBJECT', 'POSE'}:
			if ctx.mode == 'OBJECT':
				ui.menu("BMAX_OM_Constraints_MT", icon="CONSTRAINT_DATA")
			else:
				ui.menu("BMAX_PM_Constraints_MT", icon="CONSTRAINT_DATA")
			ui.separator()
			ui.operator("anim.keyframe_insert", text="Keyframe", icon="KEY_HLT")
			ui.operator("anim.keyframe_delete_v3d", text="Delete Keyframe", icon="KEY_DEHLT")
			if bmax_FULL == True:
				ui.operator("anim.keyframe_clear_v3d", text="Delete Animation")
			ui.separator()

		if ctx.mode != 'OBJECT':
			ui.operator("object.mode_set", text="Exit Edit Mode", icon="OBJECT_DATAMODE").mode='OBJECT'
			ui.separator()

		if ctx.mode in {'OBJECT', 'EDIT_MESH', 'EDIT_ARMATURE', 'POSE', 'EDIT_CURVE'}:
			ui.operator("transform.select_orientation", text="Coordinate System", icon="EMPTY_DATA")
			ui.operator("wm.context_menu_enum", text="Rotation/Scale Pivot", icon="ROTATE").data_path='space_data.pivot_point'

		ui.menu("BMAX_Viewport_MT", icon="FCURVE")

#*********************************************************************************#
# Blender 3ds Max tools emulation : UI panel
#*********************************************************************************#

class BMAX_OM_Panel_OP(Panel):
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_label = "BMax Tool Panel"

	def draw(self, ctx):
		ui = self.layout
		#quick display access
		r = ui.row()
		r.operator("wm.call_menu", icon="IMAGE_ALPHA", text="").name='BMAX_PickViewportBackground_MT'
		r.operator("wm.context_menu_enum", icon="BBOX", text="").data_path='space_data.viewport_shade'
		r.operator("bmax.object_wireframe_toggle", icon="WIRE", text="")
		r.operator("bmax.object_shade_flat", icon="MESH_ICOSPHERE", text="")
		r.operator("bmax.object_shade_smooth", icon="MATSPHERE", text="")
		r.operator("bmax.set_scene_lighting", icon="LAMP", text="")
		r.prop(ctx.space_data, "use_matcap", icon="IMAGEFILE", text="")
		#create
		if ctx.mode == 'OBJECT':
			ui.menu("INFO_MT_add", text="Create", icon="SOLO_ON")
		elif ctx.mode == 'EDIT_MESH':
			ui.menu("INFO_MT_mesh_add", text="Create", icon='SOLO_ON')
		elif ctx.mode == 'EDIT_ARMATURE':
			ui.menu("BMAX_AM_CreatePrimitive_MT", icon='SOLO_ON')
		elif ctx.mode == 'EDIT_CURVE':
			ui.menu("INFO_MT_curve_add", text="Create", icon='SOLO_ON')
		#mode
		ctxn = "object" #ctx name
		mode = 'OBJECT'
		if ctx.active_object:
			mode = ctx.active_object.mode
		item = bpy.types.OBJECT_OT_mode_set.bl_rna.properties['mode'].enum_items[mode]
		ui.operator_menu_enum("object.mode_set", "mode", text=item.name, icon=item.icon)

		if ctx.mode == 'OBJECT':
			ui.menu("BMAX_OM_Hide_MT", icon="RESTRICT_VIEW_OFF")
			ui.menu("BMAX_OM_Freeze_MT", icon="FREEZE")
			ui.operator("bmax.select_from_scene", text="Select From Scene...", icon="RESTRICT_SELECT_OFF")
			ui.separator()
			r = ui.row()
			r.operator("object.parent_set", text="Link", icon="LOCKVIEW_ON")
			r.operator("object.parent_clear", text="Unlink", icon="LOCKVIEW_OFF")
			r = ui.row()
			r.operator("wm.call_menu", text="Group", icon="GROUP").name='BMAX_OM_Group_MT'
			r.operator("object.join", text="Attach")
			r = ui.row()
			r.operator("bmax.align_tool", text="Align...", icon="ALIGN")
			r.menu("BMAX_OM_AlignPivot_MT", text="Special", icon="ALIGN")
			r = ui.row()
			r.operator("bmax.mirror_tool", text="Mirror...", icon="MOD_MIRROR")
			r.operator("bmax.clone_tool", text="Clone...", icon="MOD_BOOLEAN")
			op = ui.operator("object.transform_apply", text="Reset XForm")
			op.rotation = True
			op.scale = True
			ui.separator()

		# edit mesh
		elif ctx.mode == 'EDIT_MESH':
			t, i = bmax_GetMeshSubObject(ctx.tool_settings.mesh_select_mode)
			ui.menu("BMAX_EM_SubObject_MT", text=t, icon=i)
			ui.menu("BMAX_EM_ShowHideElement_MT", icon="RESTRICT_VIEW_OFF")
			ui.prop(ctx.space_data, "use_occlude_geometry", text="Ignore Backfacing")
			ui.separator()

			if bmax_FULL == True:
				if ctx.tool_settings.mesh_select_mode[1] == True:
					r = ui.row()
					r.operator("mesh.loop_multi_select", icon="UV_VERTEXSEL", text="Loop").ring=False
					r.operator("mesh.loop_multi_select", icon="UV_EDGESEL", text="Ring").ring=True
				ui.operator("mesh.select_linked", icon="UV_ISLANDSEL", text="Select Element")
			else:
				r = ui.row()
				r.operator("mesh.loop_multi_select", icon="UV_VERTEXSEL", text="Loop").ring=False
				r.operator("mesh.loop_multi_select", icon="UV_EDGESEL", text="Ring").ring=True

			r = ui.row()
			r.menu("BMAX_EM_EditAlign_MT", text="Special", icon="ALIGN")
			r.operator("bmax.clone_mesh", text="Clone", icon="MOD_BOOLEAN")
			r = ui.row()
			r.operator("mesh.split", text = "Detach", icon="MOD_BUILD")
			r.operator("mesh.separate", text="To Object", icon="MOD_BUILD")
			ui.separator()

			r = ui.row()
			r.operator("mesh.edge_face_add", text="Create", icon="MESH_PLANE")
			r.operator("mesh.knife_tool", text="Cut", icon="OUTLINER_DATA_CURVE")
			r = ui.row()
			r.menu("BMAX_EM_Create_Panel_MT", text="Fill", icon="SNAP_FACE")
			r.menu("BMAX_EM_Slice_Panel_MT", icon="MOD_DECIM")
			r = ui.row()
			r.menu("VIEW3D_MT_edit_mesh_extrude", icon="CURVE_PATH")
			r.menu("BMAX_EM_Repair_MT", text="Repair", icon="MODIFIER")
			ui.separator()
			###### tools start
			r = ui.row()
			r.operator("bmax.turn_quad_diagonal", text="Turn", icon="MAN_ROT")
			r.operator("mesh.edge_rotate", text="Rotate", icon="MAN_ROT")
			r = ui.row()
			r.operator("transform.shrink_fatten", text="Shrink", icon="MESH_MONKEY")
			r.operator("transform.tosphere", text="Spherify", icon="MESH_ICOSPHERE")
			r = ui.row()
			r.operator("transform.push_pull", text="Push", icon="MOD_MESHDEFORM")
			r.operator("transform.shear", text="Shear")
			r = ui.row()
			r.operator("mesh.inset", text="Inset", icon="MOD_MESHDEFORM")
			r.operator("mesh.vertices_smooth", text="Smooth", icon="MOD_SMOOTH")
			r = ui.row()
			r.operator("mesh.bevel", text="Bevel", icon="MOD_BEVEL")
			r.operator("transform.edge_slide", text="Slide Edge")
			r = ui.row()
			r.operator("mesh.vert_connect", text="Connect")
			r.operator("transform.vert_slide", text="Slide Vert")
			r = ui.row()
			r.operator("mesh.remove_doubles", text="Weld", icon="MOD_DISPLACE")
			r.operator("mesh.merge", text="Merge", icon="STICKY_UVS_DISABLE")
			if bmaxWeld_Check(ctx):
				ui.operator("bmax.target_weld_off", icon="SNAP_ON")
			else:
				if ctx.tool_settings.use_mesh_automerge == True:
					ui.operator("bmax.target_weld_off", icon="AUTOMERGE_ON")
				else:
					ui.operator("bmax.target_weld_on", icon="SNAP_OFF")
			###### tools end
			ui.separator()
			ui.menu("VIEW3D_MT_uv_map", icon="MOD_UVPROJECT")
			r = ui.row()
			r.operator("mesh.mark_seam", text="Set Seams")
			r.operator("mesh.mark_seam", text="Clear Seams").clear=True
			ui.separator()

		# edit armature
		elif ctx.mode == 'EDIT_ARMATURE':
			ui.menu("BMAX_AM_Hide_MT", icon="RESTRICT_VIEW_OFF")
			ui.menu("BMAX_AM_AutoNames_MT", icon="SCRIPTWIN")
			ui.separator()
			r = ui.row()
			r.operator("armature.parent_set", text="Link", icon="LOCKVIEW_ON")
			r.operator("armature.parent_clear", text="Unlink", icon="LOCKVIEW_OFF")
			r = ui.row()
			r.menu("BMAX_AM_EditAlign_MT", text="Special", icon="ALIGN")
			r.operator("bmax.mirror_bone_tool", text="Mirror...", icon="MOD_MIRROR")
			r = ui.row()
			r.operator("bmax.clone_bones", text="Clone", icon="MOD_BOOLEAN")
			r.operator("armature.separate", text="To Object", icon="MOD_BUILD")
			ui.separator()
			r = ui.row()
			r.operator("armature.extrude", text="Extrude", icon="CURVE_PATH")
			r.operator("armature.subdivide", text="Refine", icon="GROUP_BONE")
			r = ui.row()
			r.operator("armature.fill", text="Connect")
			r.operator("armature.merge", text="Merge", icon="BONE_DATA")
			r = ui.row()
			r.operator("transform.transform", text="Roll").mode='BONE_ROLL'
			r.operator("armature.calculate_roll", text="Set Roll", icon="OUTLINER_DATA_EMPTY")
			ui.operator("armature.switch_direction", text="Flip Direction")
			ui.separator()

		# edit pose
		elif ctx.mode == 'POSE':
			ctxn = "pose"
			ui.menu("BMAX_PM_Hide_MT", icon="RESTRICT_VIEW_OFF")
			ui.menu("BMAX_PM_AutoNames_MT", icon="SCRIPTWIN")
			ui.separator()
			r = ui.row()
			r.menu("BMAX_PM_Link_MT", icon="LINK_AREA")
			r.menu("BMAX_AM_EditAlign_MT", text="Special", icon="ALIGN")
			ui.separator()
			r = ui.row()
			r.operator("pose.armature_apply", text="Freeze", icon="NDOF_DOM")
			r.operator("pose.transforms_clear", text="To Zero", icon="ARMATURE_DATA")
			r = ui.row()
			r.operator("pose.quaternions_flip", text="Flip", icon="MAN_ROT")
			r.operator("pose.rot_clear", text="To Zero", icon="MAN_ROT")
			r = ui.row()
			r.operator("pose.copy", text="Copy", icon="COPYDOWN")
			r.operator("pose.paste", text="Paste", icon="PASTEDOWN").flipped=False
			r = ui.row()
			r.menu("BMAX_PM_PoseLibrary_MT", text="Library", icon="POSE_DATA")
			r.operator("pose.paste", text="Paste X", icon="PASTEFLIPDOWN").flipped=True
			ui.separator()

		# edit curve
		elif ctx.mode == 'EDIT_CURVE':
			ui.menu("BMAX_CM_Hide_MT", icon="RESTRICT_VIEW_OFF")
			ui.separator()
			r = ui.row()
			r.menu("VIEW3D_MT_snap", "Special", icon="ALIGN")
			r.operator("curve.separate", text="To Object", icon="MOD_BUILD")
			r = ui.row()
			r.operator("bmax.clone_curve", text="Clone", icon="MOD_BOOLEAN")
			r.operator("transform.mirror", text="Mirror", icon="MOD_MIRROR")
			ui.separator()
			r = ui.row()
			r.operator("curve.make_segment", text="Create", icon="SPHERECURVE")
			r.operator("curve.handle_type_set", text="Set Handle", icon="CURVE_BEZCURVE")
			r = ui.row()
			r.operator("curve.subdivide")
			r.operator("curve.switch_direction", text="Reverse")
			r = ui.row()
			r.operator("transform.tilt", icon="MAN_TRANS")
			r.operator("curve.tilt_clear", icon="MAN_TRANS")
			ui.separator()

		if ctx.mode in {'OBJECT', 'POSE'}:
			ui.operator_menu_enum("%s.constraint_add" % ctxn, "type", text="Add Animation Constraint", icon="CONSTRAINT_DATA")
			r = ui.row()
			r.operator("%s.constraints_clear" % ctxn, text="Clear")
			r.operator("%s.constraints_copy" % ctxn, text="Copy")
			ui.separator()
			r = ui.row()
			r.operator("anim.keyframe_insert", text="Set", icon="KEY_HLT")
			r.operator("anim.keyframe_delete_v3d", text="Delete", icon="KEY_DEHLT")
			ui.operator("anim.keyframe_clear_v3d", text="Delete Animation")
			ui.prop_search(ctx.scene.keying_sets_all, "active", ctx.scene, "keying_sets_all", text="")
			ui.separator()

		ui.operator("wm.call_menu", text="Viewport Settings", icon="FCURVE").name='BMAX_Viewport_MT'
		ui.operator("bmax.toggle_right_click_menu", icon="IMGDISPLAY")

#*********************************************************************************#
#
#								BMax Named Layers
#
#*********************************************************************************#

class BMAX_LayerNames(PropertyGroup):
	name = StringProperty()
	show = BoolProperty(default = True)
	blok = BoolProperty(default = False)
	hide = BoolProperty(default = False)

bpy.utils.register_class(BMAX_LayerNames)

bpy.types.Scene.bmax_layers_index = IntProperty(default = 0)
bpy.types.Scene.bmax_layers = CollectionProperty(type = BMAX_LayerNames)

#*********************************************************************************#

# fill object list
def bmaxLayer_FillList(self, ctx):
	scn = ctx.scene
	self.o_list.clear()
	for obj in scn.objects:
		if obj.layers[scn.bmax_layers_index] == True:
			item = self.o_list.add()
			item.name = obj.name

# move object to layer
def bmaxLayer_MoveToLayer(scn, obj, idx):
	obj.layers[idx] = True
	for i in range(0, 20):
		if i != idx:
			obj.layers[i] = False
	obj.hide_select = scn.bmax_layers[idx].blok
	obj.hide_render = scn.bmax_layers[idx].hide

# set layer param
def bmaxLayer_SetLayerSelect(scn, idx, onOff):
	for obj in scn.objects:
		if obj.layers[idx] == True:
			obj.hide_select = onOff
		
# set layer param
def bmaxLayer_SetLayerRender(scn, idx, onOff):
	for obj in scn.objects:
		if obj.layers[idx] == True:
			obj.hide_render = onOff
		
# query layer
def bmaxLayer_IsEmpty(scn, idx):
	for obj in scn.objects:
		if obj.layers[idx] == True:
			return False
	return True

# query layer
def bmaxLayer_IsLastVisible(scn, idx):
	num = 0
	val = -1
	for i, v in enumerate(scn.layers):
		if v == True:
			val = i
			num += 1
	return num == 1 and idx == val

#*********************************************************************************#

class bmaxLayer_Poll:
	@classmethod
	def poll(self, ctx):
		return len(ctx.scene.bmax_layers) > 0
		
#*********************************************************************************#
# layer operators
#*********************************************************************************#

# init layers - deletes names, shows all occupied, special zero
class BMAX_OT_LayerCreate(Operator):
	bl_idname = "bmax.create_layer_name"
	bl_label = "Initialize Layer Manager"
	bl_description = "Initialize layer manager"

	def execute(self, ctx):
		scn = ctx.scene
		scn.bmax_layers.clear()
		scn.bmax_layers_index = 0
		for i in range(0, 20):
			item = scn.bmax_layers.add()
			item.name = ""
			if i == 0:
				item.name = "Default"
				item.show = True
				scn.layers[i] = True
			if bmaxLayer_IsEmpty(scn, i) and i != 0:
				item.show = False
				scn.layers[i] = False
			else:
				item.show = True
				scn.layers[i] = True
				bmaxLayer_SetLayerSelect(scn, i, item.blok)
				bmaxLayer_SetLayerRender(scn, i, item.hide)
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)


#*********************************************************************************#

# hide/unhide layer content
class BMAX_OT_LayerVisible(bmaxLayer_Poll, Operator):
	bl_idname = "bmax.visible_layer_name"
	bl_label = "Hide Layer"
	bl_description = "Toggle layer visibility"

	def execute(self, ctx):
		scn = ctx.scene
		idx = scn.bmax_layers_index
		if bmaxLayer_IsLastVisible(scn, idx):
			scn.bmax_layers[idx].show = True
			scn.layers[idx] = True
		else:
			scn.bmax_layers[idx].show = not scn.bmax_layers[idx].show
			scn.layers[idx] = scn.bmax_layers[idx].show
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)


class BMAX_OT_LayerVisibleAll(bmaxLayer_Poll, Operator):
	bl_idname = "bmax.visible_layer_all"
	bl_label = "Show All"
	bl_description = "Show all occupied layers"

	def execute(self, ctx):
		scn = ctx.scene
		obj = len(scn.objects)
		if obj > 0:
			for i in range(0, 20):
				if bmaxLayer_IsEmpty(scn, i) and not bmaxLayer_IsLastVisible(scn, i):
					scn.layers[i] = False
					scn.bmax_layers[i].show = False
				else:
					scn.layers[i] = True
					scn.bmax_layers[i].show = True
		else:
			scn.layers[0] = True
			scn.bmax_layers[0].show = True
			for i in range(1, 20):
				scn.layers[i] = False
				scn.bmax_layers[i].show = False
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)


#*********************************************************************************#

# freeze/unfreeze layer content
class BMAX_OT_LayerFreeze(bmaxLayer_Poll, Operator):
	bl_idname = "bmax.freeze_layer_name"
	bl_label = "Freeze Layer"
	bl_description = "Freeze/unfreeze objects in a layer"

	def execute(self, ctx):
		scn = ctx.scene
		idx = scn.bmax_layers_index
		scn.bmax_layers[idx].blok = not scn.bmax_layers[idx].blok
		bmaxLayer_SetLayerSelect(scn, idx, scn.bmax_layers[idx].blok)
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)


class BMAX_OT_LayerFreezeAll(bmaxLayer_Poll, Operator):
	bl_idname = "bmax.freeze_layer_all"
	bl_label = "Unfreeze All"
	bl_description = "Unfreeze all layers"

	def execute(self, ctx):
		scn = ctx.scene
		for item in scn.bmax_layers:
			item.blok = False
		for obj in scn.objects:
			obj.hide_select = False
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)


#*********************************************************************************#

# rendering visibility on/off layer content
class BMAX_OT_LayerRender(bmaxLayer_Poll, Operator):
	bl_idname = "bmax.render_layer_name"
	bl_label = "Render Layer"
	bl_description = "Toggle rendering of objects in a layer"

	def execute(self, ctx):
		scn = ctx.scene
		idx = scn.bmax_layers_index
		scn.bmax_layers[idx].hide = not scn.bmax_layers[idx].hide
		bmaxLayer_SetLayerRender(scn, idx, scn.bmax_layers[idx].hide)
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)


class BMAX_OT_LayerRenderAll(bmaxLayer_Poll, Operator):
	bl_idname = "bmax.render_layer_all"
	bl_label = "Render All"
	bl_description = "Enable rendering of all layers"

	def execute(self, ctx):
		scn = ctx.scene
		for item in scn.bmax_layers:
			item.hide = False
		for obj in scn.objects:
			obj.hide_render = False
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)


#*********************************************************************************#

class BMAX_OT_LayerSelect(bmaxLayer_Poll, Operator):
	bl_idname = "bmax.select_from_layer"
	bl_label = "Select From Layer"
	bl_description = "Select object from layer by name"
	bl_options = {'REGISTER', 'UNDO'}

	o_list = CollectionProperty(type = BMAX_ObjList)
	o_name = StringProperty()
	b_plus = BoolProperty(default = False)

	def check(self, ctx):
		bmaxLayer_FillList(self, ctx)
		return False

	def draw(self, ctx):
		self.layout.box().row().prop(self, "b_plus", text = "Extend Selection")
		bmaxSelect_DrawSelect(self)

	def execute(self, ctx):
		if self.b_plus == False:
			bpy.ops.object.select_all(action = 'DESELECT')
		obj = bmaxSelect_GetObjectFromName(ctx, self.o_name)
		if obj is not None:
			obj.select = True
			ctx.scene.objects.active = obj
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		bmaxLayer_FillList(self, ctx)
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}


class BMAX_OT_LayerSelectAll(bmaxLayer_Poll, Operator):
	bl_idname = "bmax.select_from_layer_all"
	bl_label = "Select Layer"
	bl_description = "Select all objects from a layer"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, ctx):
		scn = ctx.scene
		idx = scn.bmax_layers_index
		bpy.ops.object.select_all(action = 'DESELECT')
		for obj in scn.objects:
			if obj.layers[idx]:
				obj.select = True
				ctx.scene.objects.active = obj
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)


#*********************************************************************************#

# move selected	objects to layer
class BMAX_OT_LayerMoveTo(bmaxLayer_Poll, Operator):
	bl_idname = "bmax.move_to_layer_name"
	bl_label = "Move Selected To"
	bl_description = "Move selected objects to a layer"

	def execute(self, ctx):
		scn = ctx.scene
		idx = scn.bmax_layers_index
		for obj in ctx.selected_objects:
			bmaxLayer_MoveToLayer(scn, obj, idx)
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)


#*********************************************************************************#
# UI
#*********************************************************************************#

def bmaxLayer_DrawListItem(row, flag, cls, icon):
	if flag == False:
		row.operator("bmax.%s_layer_name" % cls, icon="ZOOMOUT", text="", emboss=False)
	else:
		row.operator("bmax.%s_layer_name" % cls, icon=icon, text="", emboss=False)


class BMAX_UL_Layer(UIList):

	def draw_item(self, ctx, ui, data, item, icon, active_data, active_propname, index):
		r = ui.row()
		r.prop(item, "name", text="", icon="COLLAPSEMENU", emboss=False, translate=False)
		r = r.row()
		r.alignment = 'RIGHT'
		bmaxLayer_DrawListItem(r, item.show, "visible", "LAMP")
		bmaxLayer_DrawListItem(r, item.blok, "freeze", "FREEZE")
		bmaxLayer_DrawListItem(r, item.hide == False, "render", "RESTRICT_RENDER_OFF")

	def invoke(self, context, event):
		pass

#*********************************************************************************#

class BMAX_OM_LayerPanel_OP(Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_label = "BMax Layer Manager"
	bl_options = {'DEFAULT_CLOSED'}

	@classmethod
	def poll(self, ctx):
		return ctx.mode == 'OBJECT'
		
	def draw(self, ctx):
		scn = ctx.scene
		ui = self.layout

		ui.operator("bmax.create_layer_name")
		ui.separator()
		ui.template_list("BMAX_UL_Layer", "", scn, "bmax_layers", scn, "bmax_layers_index")

		r = ui.row()
		r = r.row()
		r.operator("bmax.select_from_layer_all", text="", icon="COLLAPSEMENU")
		r.operator("bmax.select_from_layer", text="", icon="RESTRICT_SELECT_OFF")
		r.operator("bmax.move_to_layer_name", text="", icon="FORWARD")
		r = r.row()
		r.alignment = 'RIGHT'
		r.operator("bmax.visible_layer_all", text="", icon='LAMP')
		r.operator("bmax.freeze_layer_all", text="", icon='FREEZE')
		r.operator("bmax.render_layer_all", text="", icon='RESTRICT_RENDER_OFF')


#*********************************************************************************#
#
#							UV Right-Click Menu
#
#*********************************************************************************#

# edit vertices
class BMAX_EM_SubObjectVertsUV_OT(Operator):
	bl_idname = "bmax.sub_object_verts_uv"
	bl_label = "Edit Vertices"
	bl_description = "Select vertex sub-object level"
	def execute(self, ctx):
		ctx.tool_settings.uv_select_mode = 'VERTEX'
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# edit edges
class BMAX_EM_SubObjectEdgesUV_OT(Operator):
	bl_idname = "bmax.sub_object_edges_uv"
	bl_label = "Edit Edges"
	bl_description = "Select edge sub-object level"
	def execute(self, ctx):
		ctx.tool_settings.uv_select_mode = 'EDGE'
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# edit faces
class BMAX_EM_SubObjectFacesUV_OT(Operator):
	bl_idname = "bmax.sub_object_faces_uv"
	bl_label = "Edit Faces"
	bl_description = "Select face sub-object level"
	def execute(self, ctx):
		ctx.tool_settings.uv_select_mode = 'FACE'
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# edit islands
class BMAX_EM_SubObjectIslandsUV_OT(Operator):
	bl_idname = "bmax.sub_object_islands_uv"
	bl_label = "Edit Islands"
	bl_description = "Select island sub-object level"
	def execute(self, ctx):
		ctx.tool_settings.uv_select_mode = 'ISLAND'
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# Sub-Menu for last 4 operators
class BMAX_EM_SubObjectUV_MT(Menu):
	bl_label = "Sub-Object"
	bl_description = "Select sub-object level"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.sub_object_verts_uv", icon = 'UV_VERTEXSEL')
		ui.operator("bmax.sub_object_edges_uv", icon = 'UV_EDGESEL')
		ui.operator("bmax.sub_object_faces_uv", icon = 'UV_FACESEL')
		ui.operator("bmax.sub_object_islands_uv", icon = 'UV_ISLANDSEL')

#*********************************************************************************#
# Show/Hide Selection
#*********************************************************************************#

class BMAX_EM_ShowHideElementUV_MT(Menu):
	bl_label = "Hide/Unhide"
	bl_description = "Hide/Unhide sub-object selection"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("uv.hide", text = "Hide Selected").unselected = False
		ui.operator("uv.hide", text = "Hide Unselected").unselected = True
		ui.separator()
		ui.operator("uv.reveal", text = "Unhide All")

#*********************************************************************************#
# Space UVs
# based on code by (c) 2012 Dan Wheeler
#*********************************************************************************#

def bmaxUV_Distribute(ctx, dox, doy):
	#collect selection
	sel = {}
	obj = ctx.active_object
	uvw = obj.data.uv_layers.active
	for loop in obj.data.loops:
		if uvw.data[loop.index].select:
			u = uvw.data[loop.index].uv[0]
			v = uvw.data[loop.index].uv[1]
			uv = u, v
			if not uv in sel:
				sel[uv] = []
			sel[uv].append(loop.index)
	#space UVs
	if len(sel) >= 3:
		sx = []
		sy = []
		selx = {}
		sely = {}
		for k in sel.keys():
			sx.append(k[0])
			sy.append(k[1])
		sx.sort()
		sy.sort()
		dx = sx[-1] - sx[0]
		dy = sy[-1] - sy[0]
		i=0
		for x in sx:
			selx[x] = i
			i += 1
		i=0
		for y in sy:
			sely[y] = i
			i += 1
		szx = len(selx) - 1
		szy = len(sely) - 1
		for k in sel.keys():
			u = k[0]
			v = k[1]
			x = u
			y = v
			if szx > 0 and dox == True: x = (selx[u] / szx) * dx + sx[0]
			if szy > 0 and doy == True: y = (sely[v] / szy) * dy + sy[0]
			a = sel[k]
			for id in a:
				uvw.data[id].uv[0] = x
				uvw.data[id].uv[1] = y

#*********************************************************************************#

class BMAX_EM_SpaceHorizontalUV_OT(Operator):
	bl_idname = "bmax.space_horizontal_uv"
	bl_label = "Space Horizontal"
	bl_description = "Evenly space UVs horizontally"
	bl_options = {'REGISTER', 'UNDO'}
	def execute(self, ctx):
		bpy.ops.object.editmode_toggle()
		bmaxUV_Distribute(ctx, True, False)
		bpy.ops.object.editmode_toggle()
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

#*********************************************************************************#

class BMAX_EM_SpaceVerticalUV_OT(Operator):
	bl_idname = "bmax.space_vertical_uv"
	bl_label = "Space Vertical"
	bl_description = "Evenly space UVs vertically"
	bl_options = {'REGISTER', 'UNDO'}
	def execute(self, ctx):
		bpy.ops.object.editmode_toggle()
		bmaxUV_Distribute(ctx, False, True)
		bpy.ops.object.editmode_toggle()
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

#*********************************************************************************#
# Rotate Selection
#*********************************************************************************#

class BMAX_EM_RotatePlusUV_OT(Operator):
	bl_idname = "bmax.rotate_plus_uv"
	bl_label = "Rotate 90 CW"
	bl_description = "Rotate the selection 90 degrees"
	def execute(self, ctx):
		bpy.ops.transform.rotate(
			value=1.5708,
			axis=(-0, -0, -1),
			constraint_axis=(False, False, False),
			constraint_orientation='GLOBAL',
			mirror=False,
			proportional='DISABLED',
			proportional_edit_falloff='SMOOTH',
			proportional_size=1)
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

#*********************************************************************************#

class BMAX_EM_RotateMinusUV_OT(Operator):
	bl_idname = "bmax.rotate_minus_uv"
	bl_label = "Rotate 90 CCW"
	bl_description = "Rotate the selection -90 degrees"
	def execute(self, ctx):
		bpy.ops.transform.rotate(
			value=-1.5708,
			axis=(-0, -0, -1),
			constraint_axis=(False, False, False),
			constraint_orientation='GLOBAL',
			mirror=False,
			proportional='DISABLED',
			proportional_edit_falloff='SMOOTH',
			proportional_size=1)
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

#*********************************************************************************#
# Flip Selection
#*********************************************************************************#

class BMAX_EM_FlipHorizontalUV_OT(Operator):
	bl_idname = "bmax.flip_horizontal_uv"
	bl_label = "Flip Horizontal"
	bl_description = "Detach edge verts and mirror horizontally"
	def execute(self, ctx):
		if ctx.tool_settings.use_uv_select_sync == False:
			bpy.ops.uv.select_split()
		bpy.ops.transform.mirror(
			constraint_axis=(True, False, False),
			constraint_orientation='GLOBAL',
			proportional='DISABLED',
			proportional_edit_falloff='SMOOTH',
			proportional_size=1)
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

#*********************************************************************************#

class BMAX_EM_FlipVerticalUV_OT(Operator):
	bl_idname = "bmax.flip_vertical_uv"
	bl_label = "Flip Vertical"
	bl_description = "Detach edge verts and mirror vertically"
	def execute(self, ctx):
		if ctx.tool_settings.use_uv_select_sync == False:
			bpy.ops.uv.select_split()
		bpy.ops.transform.mirror(
			constraint_axis=(False, True, False),
			constraint_orientation='GLOBAL',
			proportional='DISABLED',
			proportional_edit_falloff='SMOOTH',
			proportional_size=1)
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

#*********************************************************************************#
# UV Tools
#*********************************************************************************#

class BMAX_EM_ToolsUV_MT(Menu):
	bl_label = "Tools"
	bl_description = "UV Tools"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("uv.weld", text = "Weld Selected", icon = "MOD_DISPLACE")
		ui.operator("uv.stitch", text = "Stitch Selected")
		ui.separator()
		ui.operator("uv.select_split", text = "Detach Edge Verts")
		ui.separator()
		ui.operator("uv.unwrap", icon = "MOD_UVPROJECT")
		ui.operator("uv.mark_seam", text = "Set Seams").clear=False
		ui.operator("uv.mark_seam", text = "Clear Seams").clear=True
		ui.separator()
		ui.operator("uv.pack_islands", text = "Pack UVs")
		ui.operator("uv.minimize_stretch", text = "Relax")
		ui.separator()
		ui.operator("uv.export_layout", text = "Render UVW Template", icon = "IMAGEFILE")

#*********************************************************************************#
# BMax UV Tools Right-Click Menu
#*********************************************************************************#

class BMAX_MT_ToolMenuUV(Menu):
	bl_label = "BMax UV Tools"
	bl_description = "BMax right-click menu"

	def draw(self, ctx):
		ui = self.layout
		ui.operator_context = 'INVOKE_REGION_WIN'

		ui.operator("screen.redo_last", text = "Edit Last Action...", icon = "UI")
		ui.separator()
		if ctx.tool_settings.use_uv_select_sync == True:
			ui.menu("BMAX_EM_SubObject_MT")
		else:
			ui.menu("BMAX_EM_SubObjectUV_MT")
		ui.menu("BMAX_EM_ShowHideElementUV_MT", icon="RESTRICT_VIEW_OFF")
		ui.prop(ctx.tool_settings, "use_uv_select_sync", text="Sync Selection")
		ui.separator()
		ui.operator("uv.select_linked", icon="UV_ISLANDSEL", text="Select Element")
		ui.separator()
		ui.menu("IMAGE_MT_uvs_snap", text = "Align Selection", icon = "ALIGN")
		ui.operator("uv.align", text = "Align Vertical").axis='ALIGN_X'
		ui.operator("uv.align", text = "Align Horizontal").axis='ALIGN_Y'
		ui.separator()
		ui.operator("bmax.space_vertical_uv")
		ui.operator("bmax.space_horizontal_uv")
		ui.separator()
		ui.operator("bmax.rotate_plus_uv")
		ui.operator("bmax.rotate_minus_uv")
		ui.operator("bmax.flip_vertical_uv")
		ui.operator("bmax.flip_horizontal_uv")
		ui.separator()
		ui.menu("BMAX_EM_ToolsUV_MT", icon = "MOD_UVPROJECT")
		ui.separator()
		ui.operator("wm.context_menu_enum", text="Rotation/Scale Pivot", icon="ROTATE").data_path='space_data.pivot_point'
		if ctx.screen.show_fullscreen:
			ui.operator("screen.screen_full_area", text="Restore Viewport", icon="SPLITSCREEN")
		else:
			ui.operator("screen.screen_full_area", text="Maximize Viewport", icon="FULLSCREEN")

#*********************************************************************************#
#
#							  Graph Editor Right-Click Menu
#
#*********************************************************************************#

class BMAX_EM_EditAlignGraph_MT(Menu):
	bl_label = "Align Special"
	bl_description = "Align selection to specified point"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("graph.snap", text = "Flatten Handles").type='HORIZONTAL'
		ui.separator()
		ui.operator("graph.snap", text = "Selection To Cursor Value").type='VALUE'
		ui.operator("graph.snap", text = "Selection To Cursor Frame").type='CFRA'
		ui.operator("graph.snap", text = "Selection To Nearest Frame").type='NEAREST_FRAME'
		ui.operator("graph.snap", text = "Selection To Nearest Second").type='NEAREST_SECOND'
		ui.operator("graph.snap", text = "Selection To Nearest Marker").type='NEAREST_MARKER'
		ui.separator()
		ui.operator("graph.frame_jump", text = "Cursor To Selection")

#*********************************************************************************#

class BMAX_MT_ToolMenuGraph(Menu):
	bl_label = "BMax Graph Tools"
	bl_description = "BMax right-click menu"

	def draw(self, ctx):
		ui = self.layout
		ui.operator_context = 'INVOKE_REGION_WIN'

		ui.operator("screen.redo_last", text = "Edit Last Action...", icon = "UI")
		ui.separator()
		ui.menu("BMAX_EM_EditAlignGraph_MT", icon="ALIGN")
		ui.operator("graph.duplicate_move", text = "Clone And Move", icon="MOD_BOOLEAN")
		ui.separator()
		ui.operator("graph.handle_type", text = "Handle Type", icon="CURVE_BEZCURVE")
		ui.operator("graph.easing_type", text = "Easing Type", icon="IPO_EASE_IN_OUT")
		ui.operator("graph.interpolation_type", text = "Interpolation", icon="IPO_CONSTANT")
		ui.separator()
		op = ui.operator("wm.context_set_enum", text = "Switch To Dopesheet", icon="ACTION")
		op.data_path = 'area.type'
		op.value = 'DOPESHEET_EDITOR'
		ui.separator()
		ui.operator("wm.context_menu_enum", text="Rotation/Scale Pivot", icon="ROTATE").data_path='space_data.pivot_point'
		if ctx.screen.show_fullscreen:
			ui.operator("screen.screen_full_area", text="Restore Viewport", icon="SPLITSCREEN")
		else:
			ui.operator("screen.screen_full_area", text="Maximize Viewport", icon="FULLSCREEN")

#*********************************************************************************#
#
#							  Dopesheet Right-Click Menu
#
#*********************************************************************************#

class BMAX_EM_EditAlignDopesheet_MT(Menu):
	bl_label = "Align Special"
	bl_description = "Align selection to specified point"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("action.snap", text = "Selection To Cursor Frame").type='CFRA'
		ui.operator("action.snap", text = "Selection To Nearest Frame").type='NEAREST_FRAME'
		ui.operator("action.snap", text = "Selection To Nearest Second").type='NEAREST_SECOND'
		ui.operator("action.snap", text = "Selection To Nearest Marker").type='NEAREST_MARKER'
		ui.separator()
		ui.operator("action.frame_jump", text = "Cursor To Selection")

#*********************************************************************************#

class BMAX_MT_ToolMenuDopesheet(Menu):
	bl_label = "BMax Dopesheet Tools"
	bl_description = "BMax right-click menu"

	def draw(self, ctx):
		ui = self.layout
		ui.operator_context = 'INVOKE_REGION_WIN'

		ui.operator("screen.redo_last", text = "Edit Last Action...", icon = "UI")
		ui.separator()
		ui.menu("BMAX_EM_EditAlignDopesheet_MT", icon="ALIGN")
		ui.operator("action.duplicate_move", text = "Clone And Move", icon="MOD_BOOLEAN")
		ui.separator()
		ui.operator("action.handle_type", text = "Handle Type", icon="CURVE_BEZCURVE")
		ui.operator("action.keyframe_type", text = "Keyframe Type", icon="SPACE3")
		ui.operator("action.interpolation_type", text = "Interpolation", icon="IPO_CONSTANT")
		ui.separator()
		op = ui.operator("wm.context_set_enum", text = "Switch To Graph", icon="IPO")
		op.data_path = 'area.type'
		op.value = 'GRAPH_EDITOR'
		ui.separator()
		if ctx.screen.show_fullscreen:
			ui.operator("screen.screen_full_area", text="Restore Viewport", icon="SPLITSCREEN")
		else:
			ui.operator("screen.screen_full_area", text="Maximize Viewport", icon="FULLSCREEN")

#*********************************************************************************#
#
#						 BMax Tools registration
#
#*********************************************************************************#

# based on original code (c) Nik @ benzinestudios.com

def register():
	bpy.utils.register_module(__name__)
	wm = bpy.context.window_manager
	km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
	kmi = km.keymap_items.new('wm.call_menu', 'RIGHTMOUSE', 'PRESS')
	kmi.properties.name = "BMAX_MT_ToolMenu"
	km = wm.keyconfigs.addon.keymaps.new(name='UV Editor', space_type='EMPTY')
	kmi = km.keymap_items.new('wm.call_menu', 'RIGHTMOUSE', 'PRESS')
	kmi.properties.name = "BMAX_MT_ToolMenuUV"
	km = wm.keyconfigs.addon.keymaps.new(name='Graph Editor', space_type='GRAPH_EDITOR')
	kmi = km.keymap_items.new('wm.call_menu', 'RIGHTMOUSE', 'PRESS')
	kmi.properties.name = "BMAX_MT_ToolMenuGraph"
	km = wm.keyconfigs.addon.keymaps.new(name='Dopesheet', space_type='DOPESHEET_EDITOR')
	kmi = km.keymap_items.new('wm.call_menu', 'RIGHTMOUSE', 'PRESS')
	kmi.properties.name = "BMAX_MT_ToolMenuDopesheet"


#*********************************************************************************#

def unregister():
	bpy.utils.unregister_module(__name__)
	wm = bpy.context.window_manager
	km = wm.keyconfigs.addon.keymaps['3D View']
	for kmi in km.keymap_items:
		if kmi.idname == 'wm.call_menu':
			if kmi.properties.name == "BMAX_MT_ToolMenu":
				km.keymap_items.remove(kmi)
				break
	km = wm.keyconfigs.addon.keymaps['UV Editor']
	for kmi in km.keymap_items:
		if kmi.idname == 'wm.call_menu':
			if kmi.properties.name == "BMAX_MT_ToolMenuUV":
				km.keymap_items.remove(kmi)
				break
	km = wm.keyconfigs.addon.keymaps['Graph Editor']
	for kmi in km.keymap_items:
		if kmi.idname == 'wm.call_menu':
			if kmi.properties.name == "BMAX_MT_ToolMenuGraph":
				km.keymap_items.remove(kmi)
				break
	km = wm.keyconfigs.addon.keymaps['Dopesheet']
	for kmi in km.keymap_items:
		if kmi.idname == 'wm.call_menu':
			if kmi.properties.name == "BMAX_MT_ToolMenuDopesheet":
				km.keymap_items.remove(kmi)
				break

#*********************************************************************************#
# entry point
#*********************************************************************************#

if __name__ == "__main__":
	register()
