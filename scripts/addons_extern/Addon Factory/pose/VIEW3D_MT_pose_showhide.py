# 3Dビュー > ポーズモード > 「ポーズ」メニュー > 「表示/隠す」メニュー

import bpy

################
# オペレーター #
################

class HideSelectBones(bpy.types.Operator):
	bl_idname = "armature.hide_select_bones"
	bl_label = "Disable select the one you have selected"
	bl_description = "I want to not be selected the bone that has been selected"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for bone in context.selected_pose_bones:
			obj = context.active_object
			if (obj.type == "ARMATURE"):
				obj.data.bones[bone.name].hide_select = True
		return {'FINISHED'}

class HideSelectAllReset(bpy.types.Operator):
	bl_idname = "armature.hide_select_all_reset"
	bl_label = "And release all not be selected"
	bl_description = "I want to be selected bone of all the non-selectable settings"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type == "ARMATURE"):
			for bone in context.active_object.data.bones:
				bone.hide_select = False
				bone.select = False
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューのオン/オフの判定
def IsMenuEnable(self_id):
	for id in bpy.context.user_preferences.addons["Addon Factory"].preferences.disabled_menu.split(','):
		if (id == self_id):
			return False
	else:
		return True

# メニューを登録する関数
def menu(self, context):
	if (IsMenuEnable(__name__.split('.')[-1])):
		self.layout.separator()
		self.layout.operator(HideSelectBones.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.operator(HideSelectAllReset.bl_idname, icon="PLUGIN")
	if (context.user_preferences.addons["Addon Factory"].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', icon='VISIBLE_IPO_ON').id = __name__.split('.')[-1]