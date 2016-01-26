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
# by meta-androcto, parts based on work by Erich Toven #

bl_info = {
    "name": "AF: 3d View Menus",
    "author": "Meta Androcto, ",
    "version": (0, 2),
    "blender": (2, 75, 0),
    "location": "View3D > Add Menu",
    "description": "Extended View, Select & Object Menu's",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6"\
        "/Py/Scripts",
    "tracker_url": "",
    "category": "Addon Factory"}


if "bpy" in locals():
    import importlib
    importlib.reload(VIEW3D_MT_object)
    importlib.reload(VIEW3D_MT_object_apply)
    importlib.reload(VIEW3D_MT_select_object)
    importlib.reload(VIEW3D_MT_make_links)
    importlib.reload(VIEW3D_MT_object_showhide)
    importlib.reload(VIEW3D_MT_view)
    importlib.reload(VIEW3D_MT_view_align)
    importlib.reload(VIEW3D_MT_view_align_selected)


else:
    from . import VIEW3D_MT_object
    from . import VIEW3D_MT_object_apply
    from . import VIEW3D_MT_select_object
    from . import VIEW3D_MT_make_links
    from . import VIEW3D_MT_object_showhide
    from . import VIEW3D_MT_view
    from . import VIEW3D_MT_view_align
    from . import VIEW3D_MT_view_align_selected

import bpy
# Addons Preferences
class AddonPreferences(bpy.types.AddonPreferences):
	bl_idname = __name__

	view_savedata = bpy.props.StringProperty(name="View Saved Data", default="")
	
	def draw(self, context):
		layout = self.layout
		layout.label(text="Save your Views to addons preferences")
		layout.label(text="Per Session ues only")
		layout.label(text="Save User Settings to store permenantly")
		layout.prop(self, 'view_savedata')

		layout.label(text="----3d View Menu's----")
		layout.label(text="Adds additional features & concepts")
		layout.label(text="View Menu: Pies, Switch Local, Save View Prefs, Align Menu")
		layout.label(text="Select Menu: Additional selection methods: Object mode")
		layout.label(text="Object Menu:")
		layout.label(text="Pies, Shortcut Concept, Show Hide & Make Links Menu's")


def register():
    bpy.utils.register_module(__name__)

    bpy.types.VIEW3D_MT_object.append(VIEW3D_MT_object.menu)
    bpy.types.VIEW3D_MT_object_apply.append(VIEW3D_MT_object_apply.menu)
    bpy.types.VIEW3D_MT_select_object.append(VIEW3D_MT_select_object.menu)
    bpy.types.VIEW3D_MT_make_links.append(VIEW3D_MT_make_links.menu)
    bpy.types.VIEW3D_MT_object_showhide.append(VIEW3D_MT_object_showhide.menu)
    bpy.types.VIEW3D_MT_view.append(VIEW3D_MT_view.menu)
    bpy.types.VIEW3D_MT_view_align.append(VIEW3D_MT_view_align.menu)
    bpy.types.VIEW3D_MT_view_align_selected.append(VIEW3D_MT_view_align_selected.menu)

def unregister():
	bpy.utils.unregister_module(__name__)

	bpy.types.VIEW3D_MT_object.remove(VIEW3D_MT_object.menu)
	bpy.types.VIEW3D_MT_object_apply.remove(VIEW3D_MT_object_apply.menu)
	bpy.types.VIEW3D_MT_select_object.remove(VIEW3D_MT_select_object.menu)
	bpy.types.VIEW3D_MT_make_links.remove(VIEW3D_MT_make_links.menu)
	bpy.types.VIEW3D_MT_object_showhide.remove(VIEW3D_MT_object_showhide.menu)
	bpy.types.VIEW3D_MT_view.remove(VIEW3D_MT_view.menu)
	bpy.types.VIEW3D_MT_view_align.remove(VIEW3D_MT_view_align.menu)
	bpy.types.VIEW3D_MT_view_align_selected.remove(VIEW3D_MT_view_align_selected.menu)

if __name__ == "__main__":
    register()
