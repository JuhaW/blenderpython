# AddOn Bounce Fibers
# Bounce Fibers 1.0.
# Bounces a point around inside a mesh to create a curve or set of curves.
# Last Revision 04-07-2014
# Bounce code by Liero.
# AddOn functionality by Atom.

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

import bpy
import os,sys,colorsys

import mathutils
from mathutils import Vector, Matrix

import random
from random import randint, uniform


#####################################################################
# Globals.
#####################################################################
# Global busy flag. Try to avoid events if we are already busy.
isBusy = False
isRendering = False
lastFrameUpdated = 0.0
frameChangeCount = 0
      
# Objects are managed by name prefix. Customize here...
OBJECT_PREFIX = "fiber_"      	#For master control object naming.
FIBER_OB_PREFIX = "bf_"			# For curves that get generated.
ENTRY_NAME = "Fiber"			#For new list entries.
                
MAX_NAME_SIZE = 64
GLOBAL_ZERO_PADDING = 6             # The number of zeros to padd strings with when converting INTs to STRINGs.
DELIMITER = ","

#####################################################################
# Simple debug message control.
#####################################################################
SHOW_MESSAGES = True
MSG_PREFIX = "fiber> "
def to_console(passedItem):
    if SHOW_MESSAGES == True:
        if len(passedItem) == 0:
            print("")
        else:
            s = str(passedItem)
            print(MSG_PREFIX + s)

#####################################################################
# Memory Management.
#####################################################################
def removeCurveFromMemory (passedName):
    # Extra test because this can crash Blender if not done correctly.
    result = False
    curve = bpy.data.curves.get(passedName)
    if curve != None:
        if curve.users == 0:
            try:
                curve.user_clear()
                can_continue = True
            except:
                can_continue = False
            
            if can_continue == True:
                try:
                    bpy.data.curves.remove(curve)
                    result = True
                    #to_console("removeCurveFromMemory: CURVE [" + passedName + "] removed from memory.")
                except:
                    result = False
                    to_console("removeCurveFromMemory: FAILED to remove [" + passedName + "] from memory.")
            else:
                # Unable to clear users, something is holding a reference to it.
                # Can't risk removing. Favor leaving it in memory instead of risking a crash.
                to_console("removeCurveFromMemory: Unable to clear users for MESH, something is holding a reference to it.")
                result = False
        else:
            to_console ("removeCurveFromMemory: Unable to remove CURVE because it still has [" + str(curve.users) + "] users.")
    else:
        # We could not fetch it, it does not exist in memory, essentially removed.
        result = True
    return result
    
#####################################################################
# Name management
##################################################################### 
def returnAllObjectNames (scene):
    # NOTE: This returns all object names in the passed scene.
    result = []
    for ob in scene.objects:
        result.append(ob.name)
    return result 

def returnObjectNamesLike(passedScene, passedName):
    # Return objects named like our passedName in the passed scene.
    result = []
    isLike = passedName
    l = len(isLike)
    all_obs = returnAllObjectNames(passedScene)
    for name in all_obs:
        candidate = name[0:l]
        if isLike == candidate:
            result.append(name)
    return result

def returnNameForNumber(passedFrame):
    frame_number = str(passedFrame)
    post_fix = frame_number.zfill(GLOBAL_ZERO_PADDING)
    return post_fix

def returnNameDroppedPrefix(ob):
    # Use only right half of name, i.e. discard xxxx_ prefix.
    lst_name = ob.name.split('_')
    return lst_name[1]

def returnFiberOBName (passedName,face_index):
    return  "%s%s_%s" % (FIBER_OB_PREFIX,passedName,returnNameForNumber(face_index))
    
def returnFiberCurveName (passedName,face_index):
    return  "%scu_%s_%s" % (FIBER_OB_PREFIX,passedName,returnNameForNumber(face_index))
