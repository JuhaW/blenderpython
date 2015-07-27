# 3Dビュー > オブジェクトモード > Ctrl+Aキー

if "bpy" in locals():
    import importlib
    importlib.reload(apply_transform_multiuser)

else:
    from . import apply_transform_multiuser

import bpy

################
# オペレーター #
################

class TransformApplyAll(bpy.types.Operator):
	bl_idname = "object.transform_apply_all"
	bl_label = "Apply position / rotation / scaling"
	bl_description = "I apply the position / rotation / scaling of objects"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
		bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューのオン/オフの判定
def IsMenuEnable(self_id):
	for id in bpy.context.user_preferences.addons["Addon_Factory"].preferences.disabled_menu.split(','):
		if (id == self_id):
			return False
	else:
		return True

# メニューを登録する関数
def menu(self, context):
	if (IsMenuEnable(__name__.split('.')[-1])):
		self.layout.separator()
		operator = self.layout.operator(TransformApplyAll.bl_idname, text="Position and rotation and scaling", icon="PLUGIN")
		self.layout.separator()
		self.layout.menu("VIEW3D_MT_object_apply_transform_multiuser", icon="PLUGIN")
	if (context.user_preferences.addons["Addon_Factory"].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', icon='VISIBLE_IPO_ON').id = __name__.split('.')[-1]
