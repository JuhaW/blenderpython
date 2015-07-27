# Help Menu

import bpy
import zipfile, urllib.request, os, sys, re
import csv
import collections
import subprocess
try:
	import winreg
except:
	pass

################
# Update Function
################



class UpdateScrambleAddon(bpy.types.Operator):
	bl_idname = "script.update_scramble_addon"
	bl_label = "Blender-Scramble-Addon Upddate"
	bl_description = "Blender-Scramble-Addon"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
#		response = urllib.request.urlopen("https://github.com/saidenka/Blender-Scramble-Addon/archive/master.zip")
		tempDir = bpy.app.tempdir
		zipPath = os.path.join(tempDir, "Blender-Scramble-Addon-master.zip")
		addonDir = os.path.dirname(__file__)
		f = open(zipPath, "wb")
		f.write(response.read())
		f.close()
		zf = zipfile.ZipFile(zipPath, "r")
		for f in zf.namelist():
			if not os.path.basename(f):
				pass
			else:
				if ("Addon_Factory" in f):
					uzf = open(os.path.join(addonDir, os.path.basename(f)), 'wb')
					uzf.write(zf.read(f))
					uzf.close()
		zf.close()
		self.report(type={"INFO"}, message="It has been updated add-on, restart the Blender")
		return {'FINISHED'}

class ToggleDisabledMenu(bpy.types.Operator):
	bl_idname = "wm.toggle_disabled_menu"
	bl_label = "Display switching of additional items of on / off"
	bl_description = "I will switch the display / non-display of additional items of on / off button at the end of the menu by ScrambleAddon"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		context.user_preferences.addons["Addon_Factory"].preferences.use_disabled_menu = not context.user_preferences.addons["Addon_Factory"].preferences.use_disabled_menu
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
		layout = self.layout
		self.layout.separator()
#		self.layout.operator(UpdateScrambleAddon.bl_idname, icon="PLUGIN")
		layout.operator("wm.url_open", text="Ask Olson", icon='HELP').url = "http://www.getblended.org/"
	if (context.user_preferences.addons["Addon_Factory"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='VISIBLE_IPO_ON').id = __name__.split('.')[-1]
	self.layout.operator(ToggleDisabledMenu.bl_idname, icon='VISIBLE_IPO_ON')
