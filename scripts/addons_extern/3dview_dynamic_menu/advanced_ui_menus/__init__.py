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


""" Copyright 2011 GPL licence applies"""

bl_info = {
    "name": "Advanced UI Menus",
    "description": "Menus for advanced interaction with blender's UI",
    "author": "Ryan Inch",
    "version": (1, 1),
    "blender": (2, 72),
    "location": "View3D - Multiple menus in multiple modes.",
    "warning": '',  # used for warning icon and text in addons panel
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/Advanced_UI_Menus",
    "category": "3D View"}
import bpy
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'advanced_ui_menus'))

from core import *

import brush_options
import brushes
import curve_menu
import delete_menu
import dyntopo_menu
import extrude_menu
import manipulator_menu
import mode_menu
import paint_control
import operators
import pivot_menu
import proportional_menu
import custom_menu
import selection_menu
import shade_menu
import snap_menu
import stroke_options
import symmetry_options
import texture_options
import view_menu

addon_files = [brushes,
              brush_options, curve_menu, 
              delete_menu, dyntopo_menu,
              extrude_menu, manipulator_menu,
              mode_menu, paint_control,
              operators, pivot_menu, 
              proportional_menu, custom_menu,
              selection_menu, shade_menu,
              snap_menu, stroke_options,
              symmetry_options, texture_options,
              view_menu]

# this is a list of keys to deactivate with a list of modes to deactivate them in
keymodes = [  #    modes            key    any   shift  ctrl   alt   oskey
            [['Object Non-modal'], 'TAB', False, False, True, False, False],

            [['Mesh'], 'TAB', False, False, True, False, False],

            [['Object Non-modal'], 'TAB', False, False, False, False, False],

            [['Object Mode', 'Object Non-modal','Mesh','Curve','Metaball','Lattice','Particle'], 'O', False, False,
              False, False, False],
            
            [['Object Mode', 'Object Non-modal','Mesh','Curve','Metaball','Lattice','Particle'], 'O', False, True,
              False, False, False],
            
            [['Mesh'], 'X', False, False, False, False, False],

            [['Object Non-modal', 'Weight Paint'], 'V', False, False, False, False, False],
            
            [['3D View'], 'TAB', False, True, False, False, False],
            
            [['3D View'], 'TAB', False, True, True, False, False],
            [['Mesh'], 'E', False, False, False, False, False]
            ]

blender_on = False

def register():
    global blender_on
    
    # register all files

    for addon_file in addon_files:
            addon_file.register()
    
    # start a thread for disabling the opposing keymaps if this is blenders first start
    if not blender_on:
        thread = Thread(target=opposingkeys, args=(keymodes, False, True))
        thread.start()
    
    # else just disable the opposing keymaps
    else:
        opposingkeys(keymodes, False)
        
    # mark blender as on
    blender_on = True
    bpy.utils.register_module(__name__)
def unregister():
    
    # unregister all files
    for addon_file in addon_files:
        addon_file.unregister()
        
    # re-enable all the keymaps you disabled
    opposingkeys(keymodes, True)
    
    # delete all the properties you have created
    del_props()

    bpy.utils.unregister_module(__name__)
if __name__ == "__main__":
    register()
