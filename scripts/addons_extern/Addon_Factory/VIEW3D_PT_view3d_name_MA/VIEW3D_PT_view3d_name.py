# 「3Dビュー」エリア > プロパティパネル > 「アイテム」パネル

import bpy

################
# オペレーター #
################

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
		row = self.layout.row(align=True)
		row.alignment = 'LEFT'
		row.label("Quick Rename", icon='LINKED')
		row = self.layout.row(align=True)
		row.alignment = 'LEFT'
		row.label("Clipboard", icon='COPYDOWN')
		row.operator('object.copy_object_name', icon='OBJECT_DATAMODE', text="")
		if (context.active_bone or context.active_pose_bone):
		    row.operator('object.copy_bone_name', icon='BONE_DATA', text="")
		row.operator('object.copy_data_name', icon='EDITMODE_HLT', text="")
		row = self.layout.row(align=True)
		row.alignment = 'LEFT'
		row.label("Name Sync", icon='LINKED')
		row.operator('object.object_name_to_data_name', icon='TRIA_DOWN_BAR', text="")
		row.operator('object.data_name_to_object_name', icon='TRIA_UP_BAR', text="")

	if (context.user_preferences.addons["Addon_Factory"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', text= "Toggle Quick Rename", icon='VISIBLE_IPO_ON').id = __name__.split('.')[-1]
