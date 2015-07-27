# -*- coding: utf-8 -*-   

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####  

# Blender Addon Information
bl_info = {
	"name" : "CG Cookie",
	"author" : "meta-androcto",
	"version" : (0, 1, 1),
	"blender" : (2, 7, 5),
	"location" : "Help Menu",
	"description" : "Access CGCookie Tutorials & Sites",
	"warning" : "",
	"wiki_url" : "http://github.com/",
	"tracker_url" : "http://github.com/",
	"category" : "CG Cookie"
}

import bpy
import urllib.request, os

class Info_MT_cookie_links(bpy.types.Menu):
    # Define the "Extras" menu
	bl_idname = "Info_MT_cookie_links"
	bl_label = "CG Cookie Links"

	def draw(self, context):
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'

		layout.operator("wm.url_open", text="CG Cookie.com", icon='URL').url = "https://cgcookie.com/"
		layout.operator("wm.url_open", text="CG Cookie Tutorials", icon='URL').url = "https://cgcookie.com/learn-blender/"
		layout.operator("wm.url_open", text="Blender Artists Forum", icon='URL').url = "http://blenderartists.org/forum/index.php"
		layout.operator("wm.url_open", text="Blender Market", icon='URL').url = "https://cgcookiemarkets.com/blender/"

def menu_func(self, context):
	layout = self.layout
	self.layout.separator()

	self.layout.menu(Info_MT_cookie_links.bl_idname, icon="URL")

def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_help.append(menu_func)

def unregister():
    bpy.types.INFO_MT_help.remove(menu_func)
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
