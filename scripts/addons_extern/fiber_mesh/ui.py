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
import threading, time
from bpy_extras.object_utils import AddObjectHelper

from .util import OBJECT_PREFIX
from .util import FIBER_OB_PREFIX
from .util import ENTRY_NAME

from .util import to_console
from .util import returnNameDroppedPrefix

from .events import reviewBounceFibers

############################################################################
# Thread processing for parameters that are invalid to set in a DRAW context.
# By performing those operations in these threads we can get around the invalid CONTEXT error within a draw event.
# This is fairly abusive to the system and may result in instability of operation.
# Then again as long as you trap for stale data it just might work..?
# For best result keep the sleep time as quick as possible...no long delays here.
############################################################################
def BounceFibers_new_source(lock, passedSourceName, passedSleepTime):
	time.sleep(passedSleepTime) # Feel free to alter time in seconds as needed.   
	to_console("Bounce Fibers threading: BounceFibers_new_source")
	ob_source = bpy.data.objects.get(passedSourceName)
	if ob_source !=None:
			ob_source.show_name = True
			# Populate the new entry in the collection list.
			collection = ob_source.BounceFibers_List
			collection.add()
			l = len(collection)
			#bounce_fibers_name = returnNameDroppedPrefix(ob_source)
			collection[-1].name= returnNameDroppedPrefix(ob_source)	#("%s-%i" % (ENTRY_NAME,l))("%s-%i" % (bounce_fibers_name,l))
			#collection[-1].name= (ENTRY_NAME + str(l))
			to_console("Bounce Fibers threading: New entry established on [%s]." % passedSourceName)
	else:
		to_console("Bounce Fibers threading: Source not found [%s]." % passedSourceName) 

############################################################################
# PANEL code.
############################################################################   
supported_types = ['MESH'] 
			
class OBJECT_PT_BounceFibers(bpy.types.Panel):
	bl_label = "Bounce Fibers"
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_context = "object"

	@classmethod
	def poll(cls, context):
		result = False
		if context != None:
			ob = context.object
			if ob != None:
				if ob.type in supported_types:
					result = True
		return result

	def draw(self, context):
		if context != None:
			ob = context.object
			if ob != None:
				if ob.type in supported_types:
					layout = self.layout
					try:
						# Looks like all is good, we can proceed.
						ob = context.object
						can_proceed = True
					except:
						# We got an error, we are in a crash/rendering state.
						# Skip this update.
						can_proceed = False
					if can_proceed == True:
						if ob != None:
							if ob.type in supported_types:
								l = len(OBJECT_PREFIX)
								if ob.name[:l] == OBJECT_PREFIX:
									try:
										l = len(ob.BounceFibers_List)
									except:
										l = 0
									if l > 0:
										if  ob.BounceFibers_List_Index >= len(ob.BounceFibers_List):
											# If you use an arrow down when the list box has focus you can end up here.
											#ob.Selection_List_Index = len(ob.Selection_List)-1
											pass
										else:
											entry = ob.BounceFibers_List[ob.BounceFibers_List_Index]
											layout.prop(entry,"use_selection")
											box = layout.box()
											box.prop(entry,"bounce_count")
											box.prop(entry,"sub_steps")
											box.prop(entry,"rnd_noise")
											box.prop(entry,"rnd_seed")
											#box.prop(entry,"smoothness")
											box.prop(entry,"thickness")
											box.prop(entry,"rnd_thickness")
											box.prop(entry,"height_offset")
									else:
										# We have no collections so we have to add one.
										# But Blender has a WriteID lock in place at this time.
										# So we launch a thread that will run in a very, very short time from now.
										# Meanwhile we simply exit because the def the thread calls will do the work we intended to do here.
										#ob.BounceFibers_List.add()
										
										# Launch a thread to set the remaining values that would generate a CONTEXT error if issued now. (listed below)
										lock = threading.Lock()
										lock_holder = threading.Thread(target=BounceFibers_new_source, args=(lock,ob.name,0.02), name='BounceFibers_New_Source')
										lock_holder.setDaemon(True)
										lock_holder.start()
								else:
									# Common to end up here for other non-BounceFibers objects.
									layout.label("Not a Bounce Fiber object yet.",icon='INFO')  
									layout.operator("op.rename_to_bounce_fibers", icon="SORTALPHA", text="(rename with '" + OBJECT_PREFIX +"' prefix to enable)")
							else:
								# Unsupported object type.
								layout.label("Only Empties can be Bounce Fibers objects.",icon='ERROR') 
						else:
							to_console("We fetch None for the context object without throwing an error..?")
					else:
						to_console("ERROR: Can not proceed..?")
		else:
			# This can happen sometimes after a render.
			to_console ("Bounce Fibers was given an invalid context, imagine that..")
			self.layout.label("Bounce Fibers was given an invalid context.",icon='HELP')
   
def register():
	bpy.utils.register_class(OBJECT_PT_BounceFibers)

def unregister():
	bpy.utils.unregister_class(OBJECT_PT_BounceFibers)

