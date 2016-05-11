# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
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
	"version": (0, 1, 4),
	"blender": (2, 68, 0),
	"location": "View3D > BMax",
	"description": "Blender 3ds Max UI emulation",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Tools"}

###################################################################################

import bpy
import mathutils
from mathutils import Vector
from mathutils import Matrix

bmax_HUGE = 1e9

###################################################################################
# Object Mode : Align
###################################################################################

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

###################################################################################

def bmaxAlign_StoreXFormData(self, ctx):
	self.pos_curs = ctx.scene.cursor_location.copy()
	for obj in ctx.selected_objects:
		p_min, p_mid, p_piv, p_max = bmaxAlign_GetPosData(obj)
		self.pos_list.append([p_min, p_mid, p_piv, p_max])
		self.rot_list.append(obj.rotation_euler.copy())
		self.scl_list.append(obj.scale.copy())

###################################################################################

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
	# set 3D cursor
	if self.c_mode == '3DC':
		if self.pos_x == True: ctx.scene.cursor_location.x = a_box[t_id].x
		else: ctx.scene.cursor_location.x = self.pos_curs.x
		if self.pos_y == True: ctx.scene.cursor_location.y = a_box[t_id].y
		else: ctx.scene.cursor_location.y = self.pos_curs.y
		if self.pos_z == True: ctx.scene.cursor_location.z = a_box[t_id].z
		else: ctx.scene.cursor_location.z = self.pos_curs.z
		return
	if self.t_mode == '3DC':
		scp = ctx.scene.cursor_location.copy()
		for i, obj in enumerate(ctx.selected_objects):
			if self.pos_x == True: obj.location.x = scp.x + (self.pos_list[i][2].x - self.pos_list[i][c_id].x)
			else: obj.location.x = self.pos_list[i][2].x
			if self.pos_y == True: obj.location.y = scp.y + (self.pos_list[i][2].y - self.pos_list[i][c_id].y)
			else: obj.location.y = self.pos_list[i][2].y
			if self.pos_z == True: obj.location.z = scp.z + (self.pos_list[i][2].z - self.pos_list[i][c_id].z)
			else: obj.location.z = self.pos_list[i][2].z
		return
	# set selection  
	for i, obj in enumerate(ctx.selected_objects):
		if obj != ctx.active_object:
			# position
			if self.pos_x == True: obj.location.x = a_box[t_id].x + (self.pos_list[i][2].x - self.pos_list[i][c_id].x)
			else: obj.location.x = self.pos_list[i][2].x
			if self.pos_y == True: obj.location.y = a_box[t_id].y + (self.pos_list[i][2].y - self.pos_list[i][c_id].y)
			else: obj.location.y = self.pos_list[i][2].y
			if self.pos_z == True: obj.location.z = a_box[t_id].z + (self.pos_list[i][2].z - self.pos_list[i][c_id].z)
			else: obj.location.z = self.pos_list[i][2].z
			# rotation
			if self.rot_x == True: obj.rotation_euler.x = a_rot.x
			else: obj.rotation_euler.x = self.rot_list[i].x
			if self.rot_y == True: obj.rotation_euler.y = a_rot.y
			else: obj.rotation_euler.y = self.rot_list[i].y
			if self.rot_z == True: obj.rotation_euler.z = a_rot.z
			else: obj.rotation_euler.z = self.rot_list[i].z
			# scale
			if self.scl_x == True: obj.scale.x = a_scl.x
			else: obj.scale.x = self.scl_list[i].x
			if self.scl_y == True: obj.scale.y = a_scl.y
			else: obj.scale.y = self.scl_list[i].y
			if self.scl_z == True: obj.scale.z = a_scl.z
			else: obj.scale.z = self.scl_list[i].z

###################################################################################

class BMAX_OM_Align_OT(bpy.types.Operator):
	bl_idname = "bmax.align_tool"
	bl_label = "Align Selection"
	bl_description = "Align selection dialog box"
	bl_options = {'REGISTER', 'UNDO'}

	pos_curs = Vector((0, 0, 0))
	pos_list = []
	rot_list = []
	scl_list = []
	
	c_mode = bpy.props.EnumProperty(
		name = '', description = 'Selection alignment point', default = 'MIN',
		items = [
			('MIN', 'Minimum', 'Minimum'),
			('MID', 'Center', 'Center'),
			('PIV', 'Pivot', 'Pivot'),
			('MAX', 'Maximum', 'Maximum'),
			('3DC', '3D Cursor', '3D Cursor')]
		)
	t_mode = bpy.props.EnumProperty(
		name = '', description = 'Target alignment point', default = 'MIN',
		items = [
			('MIN', 'Minimum', 'Minimum'),
			('MID', 'Center', 'Center'),
			('PIV', 'Pivot', 'Pivot'),
			('MAX', 'Maximum', 'Maximum'),
			('3DC', '3D Cursor', '3D Cursor')]
		)
	pos_x = bpy.props.BoolProperty(default = False)
	pos_y = bpy.props.BoolProperty(default = False)
	pos_z = bpy.props.BoolProperty(default = False)
	rot_x = bpy.props.BoolProperty(default = False)
	rot_y = bpy.props.BoolProperty(default = False)
	rot_z = bpy.props.BoolProperty(default = False)
	scl_x = bpy.props.BoolProperty(default = False)
	scl_y = bpy.props.BoolProperty(default = False)
	scl_z = bpy.props.BoolProperty(default = False)

	@classmethod
	def poll(self, ctx):
		return len(ctx.selected_objects) > 0 and ctx.active_object != None
	
	def check(self, ctx):
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
	
	def invoke(self, ctx, evt):
		self.pos_curs = Vector((0, 0, 0))
		self.pos_list = []
		self.rot_list = []
		self.scl_list = []
		bmaxAlign_StoreXFormData(self, ctx)
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}
		
###################################################################################
# Object Mode : Mirror
###################################################################################

class BMAX_OM_Mirror_OT(bpy.types.Operator):
	bl_idname = "bmax.mirror_tool"
	bl_label = "Mirror"
	bl_description = "Mirror object dialog box"
	bl_options = {'REGISTER', 'UNDO'}

	old_xfrm = None
	obj_orig = None
	obj_copy = None

	v_offs = bpy.props.FloatProperty(default = 0)
	t_mode = bpy.props.EnumProperty(
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
	c_mode = bpy.props.EnumProperty(
		name = 'Clone Selection', description = 'Clone mode', default = 'ORIG',
		items = [('ORIG', 'No Clone', 'No Clone'),('COPY', 'Copy', 'Copy'),('INST', 'Instance', 'Instance')]
		)

	@classmethod
	def poll(self, ctx):
		return len(ctx.selected_objects) == 1 and ctx.active_object != None
	
	def check(self, ctx):
		ctx.active_object.matrix_world = self.old_xfrm.copy()
		if self.c_mode == 'COPY':
			if self.obj_copy == None:
				bpy.ops.object.duplicate(linked = False, mode = 'INIT')
				self.obj_copy = ctx.active_object
				self.old_xfrm = self.obj_copy.matrix_world.copy()
		elif self.c_mode == 'INST':
			if self.obj_copy == None:
				bpy.ops.object.duplicate(linked = True, mode = 'INIT')
				self.obj_copy = ctx.active_object
				self.old_xfrm = self.obj_copy.matrix_world.copy()
		else:
			if self.obj_copy != None:
				bpy.ops.object.delete(use_global = False)
				ctx.scene.objects.active = self.obj_orig
				self.old_xfrm = self.obj_orig.matrix_world.copy()
				self.obj_orig.select = True
				self.obj_copy = None
		c_ax = (False, False, False)
		if   self.t_mode == 'X':  c_ax = (True, False, False)
		elif self.t_mode == 'Y':  c_ax = (False, True, False)
		elif self.t_mode == 'Z':  c_ax = (False, False, True)
		elif self.t_mode == 'XY': c_ax = (True, True, False)
		elif self.t_mode == 'YZ': c_ax = (False, True, True)
		elif self.t_mode == 'ZX': c_ax = (True, False, True)
		if self.t_mode != 'N':
			# mirror
			bpy.ops.transform.mirror(
				constraint_axis = c_ax, 
				constraint_orientation = ctx.space_data.transform_orientation, 
				proportional = 'DISABLED', 
				proportional_edit_falloff = 'SMOOTH', 
				proportional_size = 1, 
				release_confirm = False)
			#offset
			bpy.ops.transform.translate(
				value = (self.v_offs, self.v_offs, self.v_offs), 
				constraint_axis = c_ax,
				constraint_orientation = 'GLOBAL',
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
		return True
	
	def draw(self, ctx):
		ui = self.layout
		b = ui.box()
		b.row().prop(ctx.space_data, "transform_orientation", text = "Coord. System")
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
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}
	
###################################################################################
# Object Mode : Clone
###################################################################################

class BMAX_OM_Clone_OT(bpy.types.Operator):
	bl_idname = "bmax.clone_tool"
	bl_label = "Clone Options"
	bl_description = "Clone object dialog box"
	bl_options = {'REGISTER', 'UNDO'}
	
	new_name = bpy.props.StringProperty(default = "Default")
	new_copy = bpy.props.BoolProperty(default = True)
	
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

###################################################################################
# Object Mode : Select From Scene / Unhide By Name / Unfreeze By Name
###################################################################################

# object list data type
class BMAX_ObjList(bpy.types.PropertyGroup):
	name = bpy.props.StringProperty()

# filter data type
class BMAX_ObjFilter(bpy.types.PropertyGroup):
	b_mesh = bpy.props.BoolProperty(default = False, description = "Hide meshes")
	b_curv = bpy.props.BoolProperty(default = False, description = "Hide splines")
	b_bone = bpy.props.BoolProperty(default = False, description = "Hide bones")
	b_help = bpy.props.BoolProperty(default = False, description = "Hide helpers")
	b_lamp = bpy.props.BoolProperty(default = False, description = "Hide lights")
	b_cams = bpy.props.BoolProperty(default = False, description = "Hide cameras")
	b_latt = bpy.props.BoolProperty(default = False, description = "Hide lattices")
	b_surf = bpy.props.BoolProperty(default = False, description = "Hide surfaces")
	b_meta = bpy.props.BoolProperty(default = False, description = "Hide metaballs")
	b_font = bpy.props.BoolProperty(default = False, description = "Hide fonts")
	b_spkr = bpy.props.BoolProperty(default = False, description = "Hide speakers")

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
		if  (obj.type == 'MESH'		and self.o_filt.b_mesh == False) or	\
			(obj.type == 'CURVE'	and self.o_filt.b_curv == False) or	\
			(obj.type == 'SURFACE'	and self.o_filt.b_surf == False) or	\
			(obj.type == 'EMPTY'	and self.o_filt.b_help == False) or	\
			(obj.type == 'FONT'		and self.o_filt.b_font == False) or	\
			(obj.type == 'LAMP'		and self.o_filt.b_lamp == False) or	\
			(obj.type == 'CAMERA'	and self.o_filt.b_cams == False) or	\
			(obj.type == 'ARMATURE' and self.o_filt.b_bone == False) or	\
			(obj.type == 'META'		and self.o_filt.b_meta == False) or	\
			(obj.type == 'LATTICE'	and self.o_filt.b_latt == False) or	\
			(obj.type == 'SPEAKER'	and self.o_filt.b_spkr == False):
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
	
###################################################################################

class BMAX_OM_SelectFromScene_OT(bpy.types.Operator):
	bl_idname = "bmax.select_from_scene"
	bl_label = "Select From Scene"
	bl_description = "Select object from scene by name"
	bl_options = {'REGISTER', 'UNDO'}
	
	o_filt = bpy.props.PointerProperty(type = BMAX_ObjFilter)
	o_list = bpy.props.CollectionProperty(type = BMAX_ObjList)
	o_name = bpy.props.StringProperty()
	b_plus = bpy.props.BoolProperty(default = False)
	
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
		
###################################################################################

class BMAX_OM_UnhideByName_OT(bpy.types.Operator):
	bl_idname = "bmax.unhide_by_name"
	bl_label = "Unhide By Name"
	bl_description = "Unhide object by name"
	bl_options = {'REGISTER', 'UNDO'}
	
	o_filt = bpy.props.PointerProperty(type = BMAX_ObjFilter)
	o_list = bpy.props.CollectionProperty(type = BMAX_ObjList)
	o_name = bpy.props.StringProperty()
	
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
		
###################################################################################

class BMAX_OM_UnfreezeByName_OT(bpy.types.Operator):
	bl_idname = "bmax.unfreeze_by_name"
	bl_label = "Unfreeze By Name"
	bl_description = "Unfreeze object by name"
	bl_options = {'REGISTER', 'UNDO'}
	
	o_filt = bpy.props.PointerProperty(type = BMAX_ObjFilter)
	o_list = bpy.props.CollectionProperty(type = BMAX_ObjList)
	o_name = bpy.props.StringProperty()
	
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
		
###################################################################################
# Object Mode : Unhide All / Hide (Un)selected
###################################################################################

# Unhide All
class BMAX_OM_UnhideAll_OT(bpy.types.Operator):
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
class BMAX_OM_HideSelected_OT(bpy.types.Operator):
	bl_idname = "bmax.hide_selected"
	bl_label = "Hide Selected"
	bl_description = "Hide all selected objects"
		
	def execute(self, ctx):
		for obj in ctx.selected_objects:
			obj.hide = True
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)

# Hide Unselected
class BMAX_OM_HideUnselected_OT(bpy.types.Operator):
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

# Sub-Menu for last 3 operators
class BMAX_OM_Hide_MT(bpy.types.Menu):
	bl_label = "Hide/Unhide"
	bl_description = "Hide/Unhide operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.unhide_all")
		ui.operator("bmax.hide_selected")
		ui.operator("bmax.hide_unselected")

###################################################################################
# Object Mode : Unfreeze All / Freeze (Un)selected
###################################################################################

# Unfreeze All
class BMAX_OM_UnfreezeAll_OT(bpy.types.Operator):
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
class BMAX_OM_FreezeSelected_OT(bpy.types.Operator):
	bl_idname = "bmax.freeze_selected"
	bl_label = "Freeze Selected"
	bl_description = "Freeze all selected objects"
		
	def execute(self, ctx):
		for obj in ctx.selected_objects:
			obj.hide_select = True
		return {'FINISHED'}

	def invoke(self, ctx, evt):
		return self.execute(ctx)

# Freeze Unselected
class BMAX_OM_FreezeUnselected_OT(bpy.types.Operator):
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

# Sub-Menu for last 3 operators
class BMAX_OM_Freeze_MT(bpy.types.Menu):
	bl_label = "Freeze/Unfreeze"
	bl_description = "Freeze/Unfreeze operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.unfreeze_all")
		ui.operator("bmax.freeze_selected")
		ui.operator("bmax.freeze_unselected")

###################################################################################
# Object Mode : Align Pivot
###################################################################################

class BMAX_OM_AlignPivot_MT(bpy.types.Menu):
	bl_label = "Align Pivot"
	bl_description = "Pivot manipulation operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("object.origin_set", text = "Pivot To Object").type='ORIGIN_GEOMETRY'
		ui.operator("object.origin_set", text = "Object To Pivot").type='GEOMETRY_ORIGIN'
		ui.operator("object.origin_set", text = "Pivot To Cursor").type='ORIGIN_CURSOR'
		ui.operator("object.origin_set", text = "Pivot To COM").type='ORIGIN_CENTER_OF_MASS'

###################################################################################
# Object Mode : Link
###################################################################################

class BMAX_OM_Link_MT(bpy.types.Menu):
	bl_label = "Link"
	bl_description = "Hierarchy manipulation operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("object.parent_set", text="Link", icon = "LOCKVIEW_ON")
		ui.operator("object.parent_clear", text="Unlink", icon = "LOCKVIEW_OFF")
		ui.operator("object.parent_clear", text="Unlink Inverse").type = 'CLEAR_INVERSE'
		ui.operator("object.parent_clear", text="Unlink Keep XForm").type = 'CLEAR_KEEP_TRANSFORM'

###################################################################################
# Edit (Armature) Mode : Make Planar/Snap
###################################################################################

class BMAX_EM_EditAlign_MT(bpy.types.Menu):
	bl_label = "Align Selection"
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
		ui.operator("view3d.snap_cursor_to_selected", text = "Cursor To Selection")
		ui.operator("view3d.snap_cursor_to_center", text = "Cursor To Center")
		ui.operator("view3d.snap_cursor_to_active", text = "Cursor To Active")
		ui.separator()
		ui.operator("view3d.snap_selected_to_grid", text = "Selection To Grid")
		ui.operator("view3d.snap_cursor_to_grid", text = "Cursor To Grid")

###################################################################################

class BMAX_AM_EditAlign_MT(bpy.types.Menu):
	bl_label = "Align Selection"
	bl_description = "Align selection to specified point"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("view3d.snap_selected_to_cursor", text = "Selection To Cursor")
		ui.operator("view3d.snap_cursor_to_selected", text = "Cursor To Selection")
		ui.operator("view3d.snap_cursor_to_center", text = "Cursor To Center")
		ui.operator("view3d.snap_cursor_to_active", text = "Cursor To Active")
		ui.separator()
		ui.operator("view3d.snap_selected_to_grid", text = "Selection To Grid")		
		ui.operator("view3d.snap_cursor_to_grid", text = "Cursor To Grid")
		
###################################################################################
# Edit Mode : Sub-Object Selection
###################################################################################

# edit vertices
class BMAX_EM_SubObjectVerts_OT(bpy.types.Operator):
	bl_idname = "bmax.sub_object_verts"
	bl_label = "Edit Vertices"
	bl_description = "Select vertex sub-object level"
	def execute(self, ctx):
		ctx.tool_settings.mesh_select_mode = (True, False, False)
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)
		
# edit edges
class BMAX_EM_SubObjectEdges_OT(bpy.types.Operator):
	bl_idname = "bmax.sub_object_edges"
	bl_label = "Edit Edges"
	bl_description = "Select edge sub-object level"
	def execute(self, ctx):
		ctx.tool_settings.mesh_select_mode = (False, True, False)
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# edit faces
class BMAX_EM_SubObjectFaces_OT(bpy.types.Operator):
	bl_idname = "bmax.sub_object_faces"
	bl_label = "Edit Faces"
	bl_description = "Select face sub-object level"
	def execute(self, ctx):
		ctx.tool_settings.mesh_select_mode = (False, False, True)
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# edit edges+verts
class BMAX_EM_SubObjectEdgeVerts_OT(bpy.types.Operator):
	bl_idname = "bmax.sub_object_edge_verts"
	bl_label = "Edit Edges/Vertices"
	bl_description = "Select edge/vertex sub-object level"
	def execute(self, ctx):
		ctx.tool_settings.mesh_select_mode = (True, True, False)
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# Sub-Menu for last 3 operators
class BMAX_EM_SubObject_MT(bpy.types.Menu):
	bl_label = "Sub-Object"
	bl_description = "Select sub-object level"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.sub_object_verts", icon = 'VERTEXSEL')
		ui.operator("bmax.sub_object_edges", icon = 'EDGESEL')
		ui.operator("bmax.sub_object_faces", icon = 'FACESEL')
		ui.separator()
		ui.operator("bmax.sub_object_edge_verts", icon = 'SNAP_VERTEX')

###################################################################################
# Edit Mode : Show/Hide Selection
###################################################################################

class BMAX_EM_ShowHideElement_MT(bpy.types.Menu):
	bl_label = "Show/Hide"
	bl_description = "Show/hide sub-object selection"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("mesh.hide", text = "Hide Selected").unselected = False
		ui.operator("mesh.hide", text = "Hide Unselected").unselected = True
		ui.separator()
		ui.operator("mesh.reveal", text = "Unhide All")

###################################################################################
# Edit Mode : Create
###################################################################################

class BMAX_EM_Create_MT(bpy.types.Menu):
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

class BMAX_EM_Create_Panel_MT(bpy.types.Menu):
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

###################################################################################
# Edit Mode : Slice
###################################################################################

class BMAX_EM_Slice_MT(bpy.types.Menu):
	bl_label = "Slice"
	bl_description = "Slice geometry operators"
	def draw(self, ctx):
		ui = self.layout
		mode = ctx.tool_settings.mesh_select_mode
		ui.operator("mesh.knife_tool", text = "Cut", icon = "OUTLINER_DATA_CURVE")
		if bpy.app.version[0] >= 2 and bpy.app.version[1] > 68:
			try:
				ui.operator("mesh.bisect", text = "Bisect")
			except:
				pass
		ui.operator("mesh.subdivide", text = "Subdivide")
		ui.operator("mesh.unsubdivide", text = "(Un)subdivide")
		ui.operator("mesh.loopcut_slide", text = "Slice Plane")
		if mode[1] == True:
			ui.separator()
			ui.operator("mesh.edge_split", text = "Split", icon = "MOD_EDGESPLIT")

class BMAX_EM_Slice_Panel_MT(bpy.types.Menu):
	bl_label = "Slice"
	bl_description = "Slice geometry operators"
	def draw(self, ctx):
		ui = self.layout
		mode = ctx.tool_settings.mesh_select_mode
		if bpy.app.version[0] >= 2 and bpy.app.version[1] > 68:
			try:
				ui.operator("mesh.bisect", text = "Bisect")
			except:
				pass
		ui.operator("mesh.subdivide", text = "Subdivide")
		ui.operator("mesh.unsubdivide", text = "(Un)subdivide")
		ui.operator("mesh.loopcut_slide", text = "Slice Plane")
		if mode[1] == True:
			ui.separator()
			ui.operator("mesh.edge_split", text = "Split", icon = "MOD_EDGESPLIT")

###################################################################################
# Edit Mode : Weld
###################################################################################

class BMAX_EM_TargetWeldOn_OT(bpy.types.Operator):
	bl_idname = "bmax.target_weld_on"
	bl_label = "Target Weld On"
	bl_description = "Switch target weld on"
	def execute(self, ctx):
		ctx.tool_settings.snap_element = 'VERTEX'
		ctx.tool_settings.use_mesh_automerge = True
		ctx.tool_settings.use_snap = True
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)

class BMAX_EM_TargetWeldOn_OT(bpy.types.Operator):
	bl_idname = "bmax.target_weld_off"
	bl_label = "Target Weld Off"
	bl_description = "Switch target weld off"
	def execute(self, ctx):
		ctx.tool_settings.snap_element = 'INCREMENT'
		ctx.tool_settings.use_mesh_automerge = False
		ctx.tool_settings.use_snap = False
		return {'FINISHED'}
	def invoke(self, ctx, event):
		return self.execute(ctx)

class BMAX_EM_Weld_MT(bpy.types.Menu):
	bl_label = "Weld"
	bl_description = "Vertex weld operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("mesh.merge", text = "Merge", icon = "STICKY_UVS_DISABLE")
		ui.separator()
		ui.operator("bmax.target_weld_on")
		ui.operator("bmax.target_weld_off")

class BMAX_EM_Weld_Panel_MT(bpy.types.Menu):
	bl_label = "Weld"
	bl_description = "Vertex weld operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.target_weld_on")
		ui.operator("bmax.target_weld_off")
		
###################################################################################
# Edit Mode : Repair
###################################################################################

# remove isolated geometry operator
class BMAX_EM_RemoveIsolatedGeometry_OT(bpy.types.Operator):
	bl_idname = "bmax.remove_isolated_geometry"
	bl_label = "Remove Isolated Geometry"
	bl_description = "Remove isolated vertices and edges"
	def execute(self, ctx):
		bpy.ops.mesh.select_loose()
		bpy.ops.mesh.delete()
		bpy.ops.mesh.delete(type='EDGE')
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)
		
# repair sub-menu
class BMAX_EM_Repair_MT(bpy.types.Menu):
	bl_label = "Repair Geometry"
	bl_description = "Mesh repair operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.remove_isolated_geometry")
		ui.operator("mesh.remove_doubles", text = "Remove Doubles")
		ui.operator("mesh.flip_normals", text = "Flip Normals")

###################################################################################
# Edit Mode : Clone
###################################################################################

class BMAX_EM_Clone_OT(bpy.types.Operator):
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

###################################################################################
# Edit Armature Mode : Mirror
###################################################################################

class BMAX_AM_Mirror_OT(bpy.types.Operator):
	bl_idname = "bmax.mirror_bone_tool"
	bl_label = "Mirror"
	bl_description = "Mirror bone dialog box"
	bl_options = {'REGISTER', 'UNDO'}

	bone_list = []

	v_offs = bpy.props.FloatProperty(default = 0)
	t_mode = bpy.props.EnumProperty(
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
	c_mode = bpy.props.EnumProperty(
		name = 'Coord. System', description = 'Coordinate System', default = 'GLOBAL',
		items = [
			('GLOBAL', 'Global', 'Global'),
			('LOCAL', 'Local', 'Local')]
		)

	@classmethod
	def poll(self, ctx):
		return ctx.active_bone != None
	
	def check(self, ctx):
		ctx.space_data.transform_orientation = self.c_mode
		for i, b in enumerate(ctx.selected_bones):
			b.head = self.bone_list[i][0].copy()
			b.tail = self.bone_list[i][1].copy()
			b.roll = self.bone_list[i][2]

		c_ax = (False, False, False)
		if   self.t_mode == 'X':  c_ax = (True, False, False)
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
				constraint_orientation = 'GLOBAL',
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
		return True
	
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
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}
	
###################################################################################
# Edit Armature Mode : Clone
###################################################################################

class BMAX_AM_Clone_OT(bpy.types.Operator):
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

###################################################################################
# Edit Armature/Pose Mode : Auto-Names
###################################################################################

class BMAX_AM_AutoNames_MT(bpy.types.Menu):
	bl_label = "Auto-Names"
	bl_description = "Automatic name generators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("armature.autoside_names", text="Mirror Names - Left/Right").type='XAXIS'
		ui.operator("armature.autoside_names", text="Mirror Names - Front/Back").type='YAXIS'
		ui.operator("armature.autoside_names", text="Mirror Names - Top/Bottom").type='ZAXIS'
		ui.operator("armature.flip_names", text="Flip Names")
		
class BMAX_PM_AutoNames_MT(bpy.types.Menu):
	bl_label = "Auto-Names"
	bl_description = "Automatic name generators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("pose.autoside_names", text="Mirror Names - Left/Right").axis='XAXIS'
		ui.operator("pose.autoside_names", text="Mirror Names - Front/Back").axis='YAXIS'
		ui.operator("pose.autoside_names", text="Mirror Names - Top/Bottom").axis='ZAXIS'
		ui.operator("pose.flip_names", text="Flip Names")
		
###################################################################################
# Edit Armature/Pose Mode : Hide/Unhide
###################################################################################

class BMAX_AM_Hide_MT(bpy.types.Menu):
	bl_label = "Hide/Unhide"
	bl_description = "Hide/Unhide operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("armature.reveal", text="Unhide All")
		ui.operator("armature.hide", text="Hide Selected").unselected=False
		ui.operator("armature.hide", text="Hide Unselected").unselected=True

class BMAX_PM_Hide_MT(bpy.types.Menu):
	bl_label = "Hide/Unhide"
	bl_description = "Hide/Unhide operators"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("pose.reveal", text="Unhide All")
		ui.operator("pose.hide", text="Hide Selected").unselected=False
		ui.operator("pose.hide", text="Hide Unselected").unselected=True

###################################################################################
# Edit Pose Mode : Pose Library
###################################################################################

class BMAX_PM_PoseTools_MT(bpy.types.Menu):
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
	
class BMAX_PM_PoseLibrary_MT(bpy.types.Menu):
	bl_label = "Pose Library"
	bl_description = "Pose library access"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("poselib.pose_add", text="Save Pose", icon="DISCLOSURE_TRI_RIGHT")
		ui.operator("poselib.pose_remove", text="Delete Pose", icon="DISCLOSURE_TRI_DOWN")
		ui.operator("poselib.pose_rename", text="Rename Pose")
		ui.operator("poselib.browse_interactive", text="Browse Library")
	
###################################################################################
# Edit Object/Pose Mode : Constraints
###################################################################################

class BMAX_OM_Constraints_MT(bpy.types.Menu):
	bl_label = "Animation Constraints"
	bl_description = "Constraint tools"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("object.constraint_add_with_targets", text="Add", icon="DISCLOSURE_TRI_RIGHT")
		ui.operator("object.constraints_clear", text="Clear", icon="DISCLOSURE_TRI_DOWN")
		ui.operator("object.visual_transform_apply", text="Bake")
	
class BMAX_PM_Constraints_MT(bpy.types.Menu):
	bl_label = "Animation Constraints"
	bl_description = "Constraint tools"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("pose.constraint_add_with_targets", text="Add", icon="DISCLOSURE_TRI_RIGHT")
		ui.operator("pose.constraints_clear", text="Clear", icon="DISCLOSURE_TRI_DOWN")
		ui.operator("pose.visual_transform_apply", text="Bake")
	
###################################################################################
# Object Mode : Layers
###################################################################################

class BMAX_LayerNames(bpy.types.PropertyGroup):
	name = bpy.props.StringProperty()
	indx = bpy.props.IntProperty()
	show = bpy.props.BoolProperty(default = True)
	blok = bpy.props.BoolProperty(default = False)
	hide = bpy.props.BoolProperty(default = False)

bpy.utils.register_class(BMAX_LayerNames)
bpy.types.Scene.bmax_layers = bpy.props.CollectionProperty(type = BMAX_LayerNames)

# fill filtered object list	
def bmaxLayer_FillList(self, ctx, idx):
	self.o_list.clear()
	for obj in ctx.scene.objects:
		if obj.layers[idx] == True:
			item = self.o_list.add()
			item.name = obj.name

# fill filtered object list	
def bmaxLayer_SetLayer(obj, idx):
	obj.layers[idx] = True
	for i in range(20):
		if i != idx:
			obj.layers[i] = False			

# count visible layers
def bmaxLayer_GetVisibleCount(ctx):
	i = 0
	for item in ctx.scene.bmax_layers:
		if item.show == True:
			i += 1
	return i

###################################################################################

# hide/unhide layer content	
class BMAX_OM_LayerVisible_OT(bpy.types.Operator):
	bl_idname = "bmax.visible_layer_name"
	bl_label = "Hide Layer"
	bl_description = "Show/hide layer"
	i_indx = bpy.props.IntProperty()
	def execute(self, ctx):
		if bmaxLayer_GetVisibleCount(ctx) > 1:
			ctx.scene.bmax_layers[self.i_indx].show = not ctx.scene.bmax_layers[self.i_indx].show
			ctx.scene.layers[self.i_indx] = ctx.scene.bmax_layers[self.i_indx].show
		return {'FINISHED'}
		
	def invoke(self, ctx, evt):
		return self.execute(ctx)

class BMAX_OM_LayerVisibleAll_OT(bpy.types.Operator):
	bl_idname = "bmax.visible_layer_all"
	bl_label = "Show All"
	bl_description = "Show all layers"
	def execute(self, ctx):
		for item in ctx.scene.bmax_layers:
			item.show = True
			ctx.scene.layers[item.indx] = True
		return {'FINISHED'}
		
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# freeze/unfreeze layer content	
class BMAX_OM_LayerFreeze_OT(bpy.types.Operator):
	bl_idname = "bmax.freeze_layer_name"
	bl_label = "Freeze Layer"
	bl_description = "Freeze/unfreeze objects in layer"
	i_indx = bpy.props.IntProperty()
	
	def execute(self, ctx):
		ctx.scene.bmax_layers[self.i_indx].blok = not ctx.scene.bmax_layers[self.i_indx].blok
		for obj in ctx.scene.objects:
			if obj.layers[self.i_indx] == True:
				obj.hide_select = ctx.scene.bmax_layers[self.i_indx].blok
		return {'FINISHED'}
		
	def invoke(self, ctx, evt):
		return self.execute(ctx)

class BMAX_OM_LayerUnfreezeAll_OT(bpy.types.Operator):
	bl_idname = "bmax.unfreeze_layer_all"
	bl_label = "Unfreeze All"
	bl_description = "Unfreeze all layers"
	def execute(self, ctx):
		for item in ctx.scene.bmax_layers:
			item.blok = False
		for obj in ctx.scene.objects:
			obj.hide_select = False
		return {'FINISHED'}
		
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# rendering visibility on/off layer content	
class BMAX_OM_LayerRender_OT(bpy.types.Operator):
	bl_idname = "bmax.render_layer_name"
	bl_label = "Render Layer"
	bl_description = "Toggle rendering of objects in layer on/off"	
	i_indx = bpy.props.IntProperty()
	
	def execute(self, ctx):
		ctx.scene.bmax_layers[self.i_indx].hide = not ctx.scene.bmax_layers[self.i_indx].hide
		for obj in ctx.scene.objects:
			if obj.layers[self.i_indx] == True:
				obj.hide_render = ctx.scene.bmax_layers[self.i_indx].hide
		return {'FINISHED'}
		
	def invoke(self, ctx, evt):
		return self.execute(ctx)

class BMAX_OM_LayerRenderAll_OT(bpy.types.Operator):
	bl_idname = "bmax.render_layer_all"
	bl_label = "Render All"
	bl_description = "Enable rendering of all layers"
	def execute(self, ctx):
		for item in ctx.scene.bmax_layers:
			item.hide = False
		for obj in ctx.scene.objects:
			obj.hide_render = False
		return {'FINISHED'}
		
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# select from layer by name
class BMAX_OM_LayerSelect_OT(bpy.types.Operator):
	bl_idname = "bmax.select_from_layer"
	bl_label = "Select From Layer"
	bl_description = "Select object from layer by name"
	bl_options = {'REGISTER', 'UNDO'}
	
	o_list = bpy.props.CollectionProperty(type = BMAX_ObjList)
	o_name = bpy.props.StringProperty()
	b_plus = bpy.props.BoolProperty(default = False)
	i_indx = bpy.props.IntProperty()
	
	def check(self, ctx):
		bmaxLayer_FillList(self, ctx, self.i_indx)
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
		bmaxLayer_FillList(self, ctx, self.i_indx)
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}
		
# move selected	objects to layer
class BMAX_OM_LayerMoveTo_OT(bpy.types.Operator):
	bl_idname = "bmax.move_to_layer_name"
	bl_label = "Move Selected To"
	bl_description = "Move selected objects to layer"	
	i_indx = bpy.props.IntProperty()
	
	def execute(self, ctx):
		for obj in ctx.selected_objects:
			bmaxLayer_SetLayer(obj, self.i_indx)
			obj.hide_render = ctx.scene.bmax_layers[self.i_indx].hide
			obj.hide_select = ctx.scene.bmax_layers[self.i_indx].blok
		return {'FINISHED'}
		
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# delete layer		
class BMAX_OM_LayerDelete_OT(bpy.types.Operator):
	bl_idname = "bmax.delete_layer_name"
	bl_label = "Delete Layer"
	bl_description = "Delete layer name"	
	i_indx = bpy.props.IntProperty()
	
	def execute(self, ctx):
		for i in range(len(ctx.scene.bmax_layers)):
			if ctx.scene.bmax_layers[i].indx == self.i_indx:
				for obj in ctx.scene.objects:
					if obj.layers[self.i_indx] == True:
						bmaxLayer_SetLayer(obj, 0)
			elif ctx.scene.bmax_layers[i].indx > self.i_indx:
				id = ctx.scene.bmax_layers[i].indx
				for obj in ctx.scene.objects:
					if obj.layers[id] == True:
						bmaxLayer_SetLayer(obj, id-1)				
				ctx.scene.bmax_layers[i].indx = id-1			
		ctx.scene.bmax_layers.remove(self.i_indx)
		bpy.ops.view3d.layers()
		return {'FINISHED'}
		
	def invoke(self, ctx, evt):
		return self.execute(ctx)

# new layer		
class BMAX_OM_LayerCreate_OT(bpy.types.Operator):
	bl_idname = "bmax.create_layer_name"
	bl_label = "New Layer"
	bl_description = "Add new layer name"	
	l_name = bpy.props.StringProperty(name = "Name:", default = "Default")
	
	def execute(self, ctx):
		if len(ctx.scene.bmax_layers) < 20:
			item = ctx.scene.bmax_layers.add()
			item.name = self.l_name
			item.indx = len(ctx.scene.bmax_layers) - 1
			ctx.scene.layers[item.indx] = True
		return {'FINISHED'}
		
	def invoke(self, ctx, evt):
		ctx.window_manager.invoke_props_dialog(self)
		return {'RUNNING_MODAL'}
		
###################################################################################

# hide/show layer
class BMAX_OM_LayersVisible_MT(bpy.types.Menu):
	bl_label = "Hide Layer"
	bl_description = "Show/Hide layer"
	def draw(self, ctx):
		ui = self.layout
		if len(bpy.context.scene.bmax_layers) > 0:
			ui.operator("bmax.visible_layer_all")
			ui.separator()
		for item in bpy.context.scene.bmax_layers:
			ico = "ZOOMOUT"
			if item.show == False:
				ico = "RESTRICT_VIEW_OFF"
			ui.operator("bmax.visible_layer_name", text=item.name, icon=ico).i_indx = item.indx

# freeze/unfreeze layer
class BMAX_OM_LayersFreeze_MT(bpy.types.Menu):
	bl_label = "Freeze Layer"
	bl_description = "Freeze/unfreeze objects in layer"
	def draw(self, ctx):
		ui = self.layout
		if len(bpy.context.scene.bmax_layers) > 0:
			ui.operator("bmax.unfreeze_layer_all")
			ui.separator()
		for item in bpy.context.scene.bmax_layers:
			ico = "ZOOMOUT"
			if item.blok == True:
				ico = "FREEZE"
			ui.operator("bmax.freeze_layer_name", text=item.name, icon=ico).i_indx = item.indx

# render layer on/off
class BMAX_OM_LayersRender_MT(bpy.types.Menu):
	bl_label = "Render Layer"
	bl_description = "Toggle rendering of objects in layer on/off"	
	def draw(self, ctx):
		ui = self.layout
		if len(bpy.context.scene.bmax_layers) > 0:
			ui.operator("bmax.render_layer_all")
			ui.separator()
		for item in bpy.context.scene.bmax_layers:
			ico = "ZOOMOUT"
			if item.hide == True:
				ico = "RESTRICT_RENDER_OFF"
			ui.operator("bmax.render_layer_name", text=item.name, icon=ico).i_indx = item.indx

# select from layer
class BMAX_OM_LayersSelect_MT(bpy.types.Menu):
	bl_label = "Select From Layer"
	bl_description = "Select object from layer by name"
	def draw(self, ctx):
		ui = self.layout
		for item in bpy.context.scene.bmax_layers:
			ui.operator("bmax.select_from_layer", text=item.name).i_indx = item.indx

# move selected to layer
class BMAX_OM_LayersMoveTo_MT(bpy.types.Menu):
	bl_label = "Move Selected To"
	bl_description = "Move selected objects to layer"
	def draw(self, ctx):
		ui = self.layout		
		for item in bpy.context.scene.bmax_layers:
			ui.operator("bmax.move_to_layer_name", text=item.name).i_indx = item.indx

# remove layer
class BMAX_OM_LayersDelete_MT(bpy.types.Menu):
	bl_label = "Delete Layer"
	bl_description = "Delete layer name"
	def draw(self, ctx):
		ui = self.layout
		for item in bpy.context.scene.bmax_layers:
			ui.operator("bmax.delete_layer_name", text=item.name).i_indx = item.indx

# entry point
class BMAX_OM_Layers_MT(bpy.types.Menu):
	bl_label = "Layers..."
	bl_description = "Layer manager"
	def draw(self, ctx):
		ui = self.layout
		ui.operator("bmax.create_layer_name", text="New Layer...")
		ui.separator()
		ui.menu("BMAX_OM_LayersSelect_MT", icon="RESTRICT_SELECT_OFF")
		ui.menu("BMAX_OM_LayersMoveTo_MT")
		ui.separator()
		ui.menu("BMAX_OM_LayersVisible_MT", icon="RESTRICT_VIEW_OFF")
		ui.menu("BMAX_OM_LayersFreeze_MT", icon="FREEZE")
		ui.menu("BMAX_OM_LayersRender_MT", icon="RESTRICT_RENDER_OFF")
		ui.separator()
		ui.menu("BMAX_OM_LayersDelete_MT")

###################################################################################
# Blender 3ds Max tools emulation : Right-Click Menu Toggle
###################################################################################

class BMAX_RightClickToggle_OP(bpy.types.Operator):
	bl_idname = "bmax.toggle_right_click_menu"
	bl_label = "Right-Click Menu Toggle"
	bl_description = "Toggle right-click context menu on/off"
	def execute(self, ctx):
		b_found = False
		wm = bpy.context.window_manager
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
		return {'FINISHED'}
	def invoke(self, ctx, evt):
		return self.execute(ctx)


###################################################################################
# Blender 3ds Max tools emulation : Right-Click Menu
###################################################################################

class BMAX_MT_ToolMenu(bpy.types.Menu):
	bl_label = "BMax Tools"
	bl_description = "BMax right-click menu"

	def draw(self, ctx):
		ui = self.layout
		ui.operator_context = 'INVOKE_REGION_WIN'

		if ctx.mode == 'OBJECT':
			ui.menu("INFO_MT_add", text = "Create")
			if ctx.active_object:
				ui.operator("object.mode_set", text="Edit Object", icon="EDITMODE_HLT").mode='EDIT'
			else:
				ui.operator("object.mode_set", text="Edit Object", icon="EDITMODE_HLT")
			ui.separator()
			ui.menu("BMAX_OM_Link_MT")
			ui.operator("bmax.align_tool", text="Align Selection...", icon="ALIGN")
			ui.menu("BMAX_OM_AlignPivot_MT", icon="SNAP_OFF")
			ui.operator("bmax.mirror_tool", text="Mirror...", icon="MOD_MIRROR")
			ui.operator("object.join", text="Attach")
			ui.operator("bmax.clone_tool", icon="MOD_BOOLEAN")
			ui.separator()
			ui.menu("BMAX_OM_Constraints_MT", icon="CONSTRAINT_DATA")
			ui.separator()
			ui.menu("BMAX_OM_Layers_MT")
#			ui.operator("object.move_to_layer", text="Move To Layers...")
			ui.menu("VIEW3D_MT_make_single_user", text="Dereference")
#			ui.operator("object.make_single_user", text="Dereference").type='SELECTED_OBJECTS'
			op = ui.operator("object.transform_apply", text="Reset XForm")
			op.rotation = True
			op.scale = True
			ui.separator()
			ui.operator("bmax.select_from_scene", text="Select From Scene...", icon="RESTRICT_SELECT_OFF")
			ui.separator()
			ui.operator("bmax.unhide_by_name", text="Unhide By Name...", icon="RESTRICT_VIEW_OFF")
			ui.menu("BMAX_OM_Hide_MT")
			ui.operator("bmax.unfreeze_by_name", text="Unfreeze By Name...", icon="FREEZE")
			ui.menu("BMAX_OM_Freeze_MT")

		elif ctx.mode == 'EDIT_MESH':
			mode = ctx.tool_settings.mesh_select_mode
			ui.menu("BMAX_EM_SubObject_MT")
			ui.menu("BMAX_EM_ShowHideElement_MT", icon="RESTRICT_VIEW_OFF")
			ui.prop(ctx.space_data, "use_occlude_geometry", text="Ignore Backfacing")
			ui.separator()
			
			if mode[1] == True:
				ui.operator("mesh.loop_multi_select", icon="UV_VERTEXSEL", text="Loop").ring=False
				ui.operator("mesh.loop_multi_select", icon="UV_EDGESEL", text="Ring").ring=True
				ui.separator()
				
			ui.menu("BMAX_EM_Create_MT", icon="SNAP_FACE")
			ui.menu("BMAX_EM_Slice_MT", icon="MOD_DECIM")
			ui.menu("VIEW3D_MT_edit_mesh_extrude", icon="CURVE_PATH")
			ui.menu("BMAX_EM_Repair_MT", icon="MODIFIER")
			ui.separator()

			# sub-selection : face
			if mode[2] == True:
				ui.operator("mesh.inset", text="Inset")
				ui.operator("mesh.quads_convert_to_tris", text="Triangulate", icon="MOD_TRIANGULATE")
				ui.operator("mesh.tris_convert_to_quads", text="Quadify Mesh", icon="MOD_LATTICE")
			
			# sub-selection : edge
			if mode[1] == True:
				ui.operator("mesh.bevel", text="Bevel Edge", icon="MOD_BEVEL")			 
				ui.operator("transform.edge_slide", text="Slide Edge")
			
			# sub-selection : vertex
			if mode[0] == True:
				ui.menu("BMAX_EM_Weld_MT", icon="MOD_DISPLACE")
				ui.operator("mesh.vert_connect", text="Connect")
				ui.operator("transform.vert_slide", text="Slide Vertex")
			
			ui.separator()
			ui.menu("BMAX_EM_EditAlign_MT", icon="ALIGN")
			ui.operator("bmax.clone_mesh", icon="MOD_BOOLEAN")
			ui.operator("mesh.split", text="Detach To Element")
			if mode[2] == True and bpy.context.active_object.type == 'MESH':
				ui.operator("mesh.separate", text="Detach To Object")		 
			ui.separator()
			ui.menu("VIEW3D_MT_uv_map", icon="MOD_UVPROJECT")
			if mode[1] == True:
				ui.operator("mesh.mark_seam", text="Set Seams")
				ui.operator("mesh.mark_seam", text="Clear Seams").clear=True
			
			ui.separator()			
			ui.operator("object.mode_set", text="Exit Edit Mode", icon="OBJECT_DATAMODE").mode='OBJECT'
			
		elif ctx.mode == 'EDIT_ARMATURE':
			ui.menu("BMAX_AM_AutoNames_MT", icon="SCRIPTWIN")
			ui.separator()
			ui.operator("armature.parent_set", text="Link", icon="LOCKVIEW_ON")
			ui.operator("armature.parent_clear", text="Unlink", icon="LOCKVIEW_OFF")
			ui.separator()
			ui.operator("armature.extrude", text="Extrude", icon="CURVE_PATH")
			ui.operator("armature.subdivide", text="Refine", icon="GROUP_BONE")
			ui.operator("armature.merge", text="Merge Chain", icon="BONE_DATA")
			ui.operator("armature.fill", text="Connect Bones")
			ui.separator()			
			ui.operator("transform.transform", text="Roll").mode='BONE_ROLL'
			ui.operator("armature.calculate_roll", text="Set Roll", icon="OUTLINER_DATA_EMPTY")
			ui.operator("armature.switch_direction", text="Flip Direction")
			ui.menu("BMAX_AM_EditAlign_MT", icon="ALIGN")
			ui.separator()			
			ui.operator("bmax.mirror_bone_tool", text="Mirror...", icon="MOD_MIRROR")			
			ui.operator("bmax.clone_bones", icon="MOD_BOOLEAN")
			ui.operator("armature.separate", text="Detach To Armature")
			ui.separator()			
			ui.menu("BMAX_AM_Hide_MT", icon="RESTRICT_VIEW_OFF")
			ui.separator()			
			ui.operator("object.mode_set", text="Edit Pose", icon="POSE_HLT").mode='POSE'
			ui.operator("object.mode_set", text="Exit Edit Mode", icon="OBJECT_DATAMODE").mode='OBJECT'
			
		elif ctx.mode == 'POSE':
			ui.menu("BMAX_PM_AutoNames_MT", icon="SCRIPTWIN")
			ui.separator()
			ui.operator("object.parent_set", text="Link", icon="LOCKVIEW_ON")
			ui.operator("object.parent_clear", text="Unlink", icon="LOCKVIEW_OFF")
			ui.separator()
			ui.operator("pose.armature_apply", text="Freeze Transform", icon="NDOF_DOM")
			ui.operator("pose.transforms_clear", text="Transform To Zero", icon="ARMATURE_DATA")
			ui.operator("pose.rot_clear", text="Rotation To Zero")
			ui.operator("pose.quaternions_flip", text="Flip Rotation")
			ui.menu("BMAX_AM_EditAlign_MT", icon="ALIGN")
			ui.separator()
			ui.menu("BMAX_PM_PoseTools_MT", icon="POSE_DATA")
			ui.separator()
			ui.menu("BMAX_PM_Constraints_MT", icon="CONSTRAINT_DATA")
			ui.separator()
			ui.operator("anim.keyframe_insert", text="Keyframe", icon="KEY_HLT")
			ui.operator("anim.keyframe_delete_v3d", text="Delete Keyframe", icon="KEY_DEHLT")
			ui.operator("anim.keyframe_clear_v3d", text="Delete Animation")
			ui.separator()
			ui.menu("BMAX_PM_Hide_MT", icon="RESTRICT_VIEW_OFF")
			ui.separator()			
			ui.operator("object.mode_set", text="Edit Bones", icon="EDITMODE_HLT").mode='EDIT'
			ui.operator("object.mode_set", text="Exit Edit Mode", icon="OBJECT_DATAMODE").mode='OBJECT'

		ui.separator()
		ui.operator("transform.select_orientation", text="Coordinate System", icon="MANIPUL")
		if ctx.screen.show_fullscreen:
			ui.operator("screen.screen_full_area", text="Restore Viewport", icon="SPLITSCREEN")
		else:
			ui.operator("screen.screen_full_area", text="Maximize Viewport", icon="FULLSCREEN")
		
###################################################################################
# Blender 3ds Max tools emulation : UI panel
###################################################################################

class BMAX_OM_Panel_OP(bpy.types.Panel):
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_label = "BMax Panel"
	
	def draw(self, ctx):
		ui = self.layout
		
		mode = 'OBJECT'
		if ctx.active_object: mode = ctx.active_object.mode
		item = bpy.types.OBJECT_OT_mode_set.bl_rna.properties['mode'].enum_items[mode]
		ui.operator_menu_enum("object.mode_set", "mode", text=item.name, icon=item.icon)

		if ctx.mode == 'OBJECT':
			ui.menu("INFO_MT_add", text="Create")
			ui.separator()
			r = ui.row()
			r.operator("object.parent_set", text="Link", icon="LOCKVIEW_ON")
			r.operator("object.parent_clear", text="Unlink", icon="LOCKVIEW_OFF")
			r = ui.row()
			r.operator("bmax.align_tool", text="Align...", icon="ALIGN")
			r.operator("bmax.mirror_tool", text="Mirror...", icon="MOD_MIRROR")
			r = ui.row()
			r.operator("bmax.clone_tool", text="Clone...", icon="MOD_BOOLEAN")
			r.operator("object.join", text="Attach")
			ui.menu("BMAX_OM_AlignPivot_MT", icon="SNAP_OFF")
			ui.separator()
			ui.operator("bmax.select_from_scene", text="Select From Scene...", icon="RESTRICT_SELECT_OFF")
			ui.operator("bmax.unhide_by_name", text="Unhide By Name...", icon="RESTRICT_VIEW_OFF")
			ui.operator("bmax.unfreeze_by_name", text="Unfreeze By Name...", icon="FREEZE")
			r = ui.row()
			r.menu("BMAX_OM_Hide_MT", text="Hide")
			r.menu("BMAX_OM_Freeze_MT", text="Freeze")
			ui.separator()
			ui.operator("object.constraint_add_with_targets", text="Animation Constraints", icon="CONSTRAINT_DATA")
			r = ui.row()
			r.operator("object.constraints_clear", text="Clear")
			r.operator("object.visual_transform_apply", text="Bake")
			ui.separator()
			r = ui.row()
			r.menu("BMAX_OM_Layers_MT")
#			r.operator("object.move_to_layer", text="Layers...")
			r.menu("VIEW3D_MT_make_single_user", text="Dereference")
#			r.operator("object.make_single_user", text="Dereference").type='SELECTED_OBJECTS'
			op = ui.operator("object.transform_apply", text="Reset XForm")
			op.rotation = True
			op.scale = True
			
		elif ctx.mode == 'EDIT_MESH':
			mode = ctx.tool_settings.mesh_select_mode
			
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
			
			ui.menu("BMAX_EM_SubObject_MT", text=t, icon=i)
			ui.menu("BMAX_EM_ShowHideElement_MT", icon="RESTRICT_VIEW_OFF")
			ui.prop(ctx.space_data, "use_occlude_geometry", text="Ignore Backfacing")
			ui.separator()
			
			if mode[1] == True:
				r = ui.row()
				r.operator("mesh.loop_multi_select", icon="UV_VERTEXSEL", text="Loop").ring=False
				r.operator("mesh.loop_multi_select", icon="UV_EDGESEL", text="Ring").ring=True
				ui.separator()
				
			r = ui.row()
			r.operator("mesh.edge_face_add", text="Create", icon="MESH_PLANE")
			r.operator("mesh.knife_tool", text="Cut", icon="OUTLINER_DATA_CURVE")
			r = ui.row()
			r.menu("BMAX_EM_Create_Panel_MT", text="Fill", icon="SNAP_FACE")
			r.menu("BMAX_EM_Slice_Panel_MT", icon="MOD_DECIM")
			ui.menu("VIEW3D_MT_edit_mesh_extrude", icon="CURVE_PATH")
			ui.menu("BMAX_EM_Repair_MT", icon="MODIFIER")
			ui.separator()
			
			# sub-selection : face
			if mode[2] == True:
				ui.operator("mesh.inset", text="Inset")
				r = ui.row()
				r.operator("mesh.quads_convert_to_tris", text="To Tris", icon="MOD_TRIANGULATE")
				r.operator("mesh.tris_convert_to_quads", text="To Quads", icon="MOD_LATTICE")
			
			# sub-selection : edge
			if mode[1] == True:
				r = ui.row()
				r.operator("mesh.bevel", text="Bevel", icon="MOD_BEVEL")			 
				r.operator("transform.edge_slide", text="Slide Edge")
			
			# sub-selection : vertex
			if mode[0] == True:
				r = ui.row()
				r.operator("mesh.merge", text="Merge", icon="STICKY_UVS_DISABLE")
				r.menu("BMAX_EM_Weld_Panel_MT", icon="MOD_DISPLACE")
				r = ui.row()
				r.operator("mesh.vert_connect", text="Connect")
				r.operator("transform.vert_slide", text="Slide Vert")
			
			r = ui.row()
			r.operator("bmax.clone_mesh", text="Clone", icon="MOD_BOOLEAN")
			r.operator("mesh.split", text = "Detach")
			if mode[2] == True and bpy.context.active_object.type == 'MESH':
				ui.operator("mesh.separate", text="Detach To Object")		 
			ui.menu("BMAX_EM_EditAlign_MT", icon="ALIGN")
			ui.separator()
			ui.menu("VIEW3D_MT_uv_map", icon="MOD_UVPROJECT")
			if mode[1] == True:
				r = ui.row()
				r.operator("mesh.mark_seam", text="Set Seams")
				r.operator("mesh.mark_seam", text="Clear Seams").clear=True
			ui.separator()
			
		elif ctx.mode == 'EDIT_ARMATURE':
			ui.menu("BMAX_AM_AutoNames_MT", icon="SCRIPTWIN")
			ui.menu("BMAX_AM_Hide_MT", icon="RESTRICT_VIEW_OFF")			
			ui.separator()
			r = ui.row()
			r.operator("armature.parent_set", text="Link", icon="LOCKVIEW_ON")
			r.operator("armature.parent_clear", text="Unlink", icon="LOCKVIEW_OFF")
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
			r = ui.row()
			r.operator("bmax.clone_bones", text="Clone", icon="MOD_BOOLEAN")
			r.operator("bmax.mirror_bone_tool", text="Mirror...", icon="MOD_MIRROR")			
			ui.operator("armature.separate", text="Detach To Armature")
			ui.menu("BMAX_AM_EditAlign_MT", icon="ALIGN")
			ui.separator()
			
		elif ctx.mode == 'POSE':
			ui.menu("BMAX_PM_AutoNames_MT", icon="SCRIPTWIN")
			ui.menu("BMAX_PM_Hide_MT", icon="RESTRICT_VIEW_OFF")
			ui.menu("BMAX_AM_EditAlign_MT", icon="ALIGN")
			ui.separator()
			r = ui.row()
			r.operator("object.parent_set", text="Link", icon="LOCKVIEW_ON")
			r.operator("object.parent_clear", text="Unlink", icon="LOCKVIEW_OFF")
			ui.separator()
			r = ui.row()
			r.operator("pose.armature_apply", text="Freeze", icon="NDOF_DOM")
			r.operator("pose.transforms_clear", text="To Zero", icon="ARMATURE_DATA")
			r = ui.row()
			r.operator("pose.quaternions_flip", text="Flip", icon="MAN_ROT")
			r.operator("pose.rot_clear", text="To Zero", icon="MAN_ROT")
			ui.separator()
			r = ui.row()
			r.operator("pose.copy", text="Copy", icon="COPYDOWN")
			r.menu("BMAX_PM_PoseLibrary_MT", text="Library")
			r = ui.row()
			r.operator("pose.paste", text="Paste", icon="PASTEDOWN").flipped=False
			r.operator("pose.paste", text="Paste X", icon="PASTEFLIPDOWN").flipped=True
			ui.separator()
			ui.operator("pose.constraint_add_with_targets", text="Animation Constraints", icon="CONSTRAINT_DATA")
			r = ui.row()
			r.operator("pose.constraints_clear", text="Clear")
			r.operator("pose.visual_transform_apply", text="Bake")
			ui.separator()
			r = ui.row()
			r.operator("anim.keyframe_insert", text="Set", icon="KEY_HLT")
			r.operator("anim.keyframe_delete_v3d", text="Delete", icon="KEY_DEHLT")
			ui.operator("anim.keyframe_clear_v3d", text="Delete Animation")
			ui.prop_search(ctx.scene.keying_sets_all, "active", ctx.scene, "keying_sets_all", text="")
#			ui.operator("anim.keying_set_active_set", text="Key Filters...", icon="KEYINGSET")
			ui.separator()

		if ctx.screen.show_fullscreen:
			ui.operator("screen.screen_full_area", text="Restore Viewport", icon="SPLITSCREEN")
		else:
			ui.operator("screen.screen_full_area", text="Maximize Viewport", icon="FULLSCREEN")
		ui.operator("bmax.toggle_right_click_menu", icon="IMGDISPLAY")
		
###################################################################################
# registration code (c) Nik @ benzinestudios.com
###################################################################################

def register():
	bpy.utils.register_module(__name__)
	wm = bpy.context.window_manager
	km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
	kmi = km.keymap_items.new('wm.call_menu', 'RIGHTMOUSE', 'PRESS')
	kmi.properties.name = "BMAX_MT_ToolMenu"
	
def unregister():
	bpy.utils.unregister_module(__name__)
	wm = bpy.context.window_manager
	km = wm.keyconfigs.addon.keymaps['3D View']
	for kmi in km.keymap_items:
		if kmi.idname == 'wm.call_menu':
			if kmi.properties.name == "BMAX_MT_ToolMenu":
				km.keymap_items.remove(kmi)
				break
				
if __name__ == "__main__":
	register()  
