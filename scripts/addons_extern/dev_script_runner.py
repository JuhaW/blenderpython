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

# <pep8-80 compliant>



#====================Version History====================
#   1.0     Initial release.
#   1.1     Added error message handling and processing.
#   1.2     Added seamless handling of  modules/addons using '__name__' 
#   1.3     Added option to set the number of scriipts from the panels. 
#             Quieted down the 'Cancel' icon.
#====================================================



bl_info = {
           "name": "Script Runner",
           "author": "Christopher Barrett  (www.goodspiritgraphics.com)",
           "version": (1, 3),
           "blender": (2, 68, 0),
           "api": 58537,
           "location": "File > Import > Run Script (.py), & '3D View Tool Shelf', & 'Text Editor Tool Shelf'.",
           "description": "Run a python script from any file directory.",
           "warning": "",
           "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Import-Export/Script_Runner",
           "tracker_url": "",
           "category": "Development"
          }




from bpy_extras.io_utils import ImportHelper
import bpy
import os, sys, platform
import shutil
import fnmatch
import errno
import ntpath
import traceback
import importlib
import string
import random

from bpy.types import Operator, AddonPreferences
from bpy.props import EnumProperty, StringProperty,BoolProperty, IntProperty, FloatVectorProperty




#------------------------------Preferences

class ScriptRunnerAddonPreferences(AddonPreferences):
    bl_idname = __name__ 
    
    error_msg_verbose = BoolProperty(name="error_msg_verbose", default = False)
    display_num_scripts = BoolProperty(name="display_num_scripts", default = True)
    display_3d = BoolProperty(name="display_3d", default = True)
    display_text_editor = BoolProperty(name="display_text_editor", default = True)
    num_scripts = IntProperty(name="Number of Scripts", description = "Set to the number of scripts to display in the panel", min = 1, max = 10, default = 2)
    script0_path = StringProperty() 
    script1_path = StringProperty()
    script2_path = StringProperty()
    script3_path = StringProperty()
    script4_path = StringProperty()
    script5_path = StringProperty()
    script6_path = StringProperty()
    script7_path = StringProperty()
    script8_path = StringProperty()
    script9_path = StringProperty()
    
    
    def draw(self, context):
        user_settings = bpy.context.user_preferences.addons[__name__].preferences
  
        layout = self.layout
        split = layout.split()
                        
        #-----Column 1
        col1 = split.column()
        row = col1.row()
        row.label("Display Area: (Restart required)")
        row = col1.row()
        row.prop(self, "display_3d", text="3D View Toolshelf", toggle = True)
        row = col1.separator()
        row = col1.row()
        row.prop(self, "display_text_editor", text="Text Editor Toolshelf", toggle = True)

        #-----Column 2
        col2 = split.column()
        row = col2.row()
        row.label("Number of Script Slots to Display:")
        row = col2.row()
        row.prop(self, "num_scripts", text="Scripts", slider = False)
        row = col2.row()
        row.prop(self,  "display_num_scripts", text="Display scripts slider on panels", toggle = False)
        
        #-----Column 3
        col3 = split.column()
        row = col3.row()
        row.prop(self, "error_msg_verbose", text="Verbose Error Messages", toggle = False)
 
        row = layout.separator()
        row = layout.row()
        row.label("Script File Paths:")
        box = layout.box()
        row = box.row()
        row.label("File #1:    " + user_settings.script0_path)
        row = box.row()
        row.label("File #2:    " + user_settings.script1_path)
        row = box.row()
        row.label("File #3:    " + user_settings.script2_path)
        row = box.row()
        row.label("File #4:    " + user_settings.script3_path)
        row = box.row()
        row.label("File #5:    " + user_settings.script4_path)        
        row = box.row()
        row.label("File #6:    " + user_settings.script5_path)
        row = box.row()
        row.label("File #7:    " + user_settings.script6_path)
        row = box.row()
        row.label("File #8:    " + user_settings.script7_path)
        row = box.row()
        row.label("File #9:    " + user_settings.script8_path)
        row = box.row()
        row.label("File #10:  " + user_settings.script9_path)
        row = box.row()

        
def draw_scripts_slider(self, context):
    self.layout.prop(context.user_preferences.addons['script_runner'].preferences, "num_scripts",  text="Scripts")



#-------------------------------Panels

class ScriptRunnerPanel1(bpy.types.Panel):
    bl_label = "Script Runner"
    bl_space_type = "TEXT_EDITOR"
    bl_region_type = "UI"
    bl_context = "WINDOW"
    bl_options = {'DEFAULT_CLOSED'}
           
    
    def draw(self, context):
        user_settings = bpy.context.user_preferences.addons[__name__].preferences
        
        
        if user_settings.display_num_scripts: 
            #Copy the slider from the addon user preferences.
            draw_scripts_slider(self, context)
        
        layout = self.layout; 
        
        #Script 1
        row = layout.row(align = True)
        slot_0_load = row.operator("object.script_load", text = "", icon='FILESEL')
        slot_0_load.script_slot = 1
        
        slot_0_clear = row.operator("object.script_clear", text = "", icon='X')
        slot_0_clear.script_slot = 0

        if user_settings.script0_path != "": 
            label = path_leaf(user_settings.script0_path)
        else:
            label = ""    
                
        slot_0_run = row.operator("object.script_run", text = label)
        slot_0_run.script_slot = 0
        

        #Script 2
        if user_settings.num_scripts > 1:
            row = layout.row(align = True)
            slot_1_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_1_load.script_slot = 2
            
            slot_1_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_1_clear.script_slot = 1
            
            if user_settings.script1_path != "": 
                label = path_leaf(user_settings.script1_path)
            else:
                label = ""     
                
            slot_1_run = row.operator("object.script_run", text = label)
            slot_1_run.script_slot = 1
        
        
        #Script 3
        if user_settings.num_scripts > 2:
            row = layout.row(align = True)
            slot_2_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_2_load.script_slot = 3
            
            slot_2_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_2_clear.script_slot = 2
            
            if user_settings.script2_path != "": 
                label = path_leaf(user_settings.script2_path)
            else:
                label = ""    
                
            slot_2_run = row.operator("object.script_run", text = label)
            slot_2_run.script_slot = 2            
            

        #Script 4
        if user_settings.num_scripts > 3:
            row = layout.row(align = True)
            slot_3_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_3_load.script_slot = 4
            
            slot_3_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_3_clear.script_slot = 3
            
            if user_settings.script3_path != "": 
                label = path_leaf(user_settings.script3_path)
            else:
                label = ""    
                
            slot_3_run = row.operator("object.script_run", text = label)
            slot_3_run.script_slot = 3            
        
        
        #Script 5
        if user_settings.num_scripts > 4:
            row = layout.row(align = True)
            slot_4_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_4_load.script_slot = 5
            
            slot_4_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_4_clear.script_slot = 4
            
            if user_settings.script4_path != "": 
                label = path_leaf(user_settings.script4_path)
            else:
                label = ""    
                
            slot_4_run = row.operator("object.script_run", text = label)
            slot_4_run.script_slot = 4              
        
        
        #Script 6
        if user_settings.num_scripts > 5:
            row = layout.row(align = True)
            slot_5_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_5_load.script_slot = 6
            
            slot_5_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_5_clear.script_slot = 5
            
            if user_settings.script5_path != "": 
                label = path_leaf(user_settings.script5_path)
            else:
                label = ""    
                
            slot_5_run = row.operator("object.script_run", text = label)
            slot_5_run.script_slot = 5      
                                
        
        #Script 7
        if user_settings.num_scripts > 6:
            row = layout.row(align = True)
            slot_6_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_6_load.script_slot = 7
            
            slot_6_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_6_clear.script_slot = 6
            
            if user_settings.script6_path != "": 
                label = path_leaf(user_settings.script6_path)
            else:
                label = ""    
                
            slot_6_run = row.operator("object.script_run", text = label)
            slot_6_run.script_slot = 6      
                    
        
        #Script 8
        if user_settings.num_scripts > 7:
            row = layout.row(align = True)
            slot_7_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_7_load.script_slot = 8
            
            slot_7_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_7_clear.script_slot = 7
            
            if user_settings.script7_path != "": 
                label = path_leaf(user_settings.script7_path)
            else:
                label = ""    
                
            slot_7_run = row.operator("object.script_run", text = label)
            slot_7_run.script_slot = 7      
            
        
        #Script 9
        if user_settings.num_scripts > 8:
            row = layout.row(align = True)
            slot_8_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_8_load.script_slot = 9
            
            slot_8_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_8_clear.script_slot = 8
            
            if user_settings.script8_path != "": 
                label = path_leaf(user_settings.script8_path)
            else:
                label = ""     
                
            slot_8_run = row.operator("object.script_run", text = label)
            slot_8_run.script_slot = 8      
            
        
        #Script 10
        if user_settings.num_scripts > 9:
            row = layout.row(align = True)
            slot_9_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_9_load.script_slot = 10
            
            slot_9_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_9_clear.script_slot = 9
            
            if user_settings.script9_path != "": 
                label = path_leaf(user_settings.script9_path)
            else:
                label = ""    
                
            slot_9_run = row.operator("object.script_run", text = label)
            slot_9_run.script_slot = 9      
            


class ScriptRunnerPanel2(bpy.types.Panel):
    bl_label = "Script Runner"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_options = {'DEFAULT_CLOSED'}
        
    
    def draw(self, context):
        user_settings = bpy.context.user_preferences.addons[__name__].preferences
        
       
        if user_settings.display_num_scripts: 
            #Copy the slider from the addon user preferences.
            draw_scripts_slider(self, context)
            
        layout = self.layout; 
                
        #Script 1
        row = layout.row(align = True)
        slot_0_load = row.operator("object.script_load", text = "", icon='FILESEL')
        slot_0_load.script_slot = 1
        
        slot_0_clear = row.operator("object.script_clear", text = "", icon='X')
        slot_0_clear.script_slot = 0

        if user_settings.script0_path != "": 
            label = path_leaf(user_settings.script0_path)
        else:
            label = ""    
                
        slot_0_run = row.operator("object.script_run", text = label)
        slot_0_run.script_slot = 0
        

        #Script 2
        if user_settings.num_scripts > 1:
            row = layout.row(align = True)
            slot_1_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_1_load.script_slot = 2
            
            slot_1_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_1_clear.script_slot = 1
            
            if user_settings.script1_path != "": 
                label = path_leaf(user_settings.script1_path)
            else:
                label = ""     
                
            slot_1_run = row.operator("object.script_run", text = label)
            slot_1_run.script_slot = 1
        
        
        #Script 3
        if user_settings.num_scripts > 2:
            row = layout.row(align = True)
            slot_2_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_2_load.script_slot = 3
            
            slot_2_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_2_clear.script_slot = 2
            
            if user_settings.script2_path != "": 
                label = path_leaf(user_settings.script2_path)
            else:
                label = ""    
                
            slot_2_run = row.operator("object.script_run", text = label)
            slot_2_run.script_slot = 2            
            

        #Script 4
        if user_settings.num_scripts > 3:
            row = layout.row(align = True)
            slot_3_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_3_load.script_slot = 4
            
            slot_3_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_3_clear.script_slot = 3
            
            if user_settings.script3_path != "": 
                label = path_leaf(user_settings.script3_path)
            else:
                label = ""    
                
            slot_3_run = row.operator("object.script_run", text = label)
            slot_3_run.script_slot = 3            
        
        
        #Script 5
        if user_settings.num_scripts > 4:
            row = layout.row(align = True)
            slot_4_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_4_load.script_slot = 5
            
            slot_4_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_4_clear.script_slot = 4
            
            if user_settings.script4_path != "": 
                label = path_leaf(user_settings.script4_path)
            else:
                label = ""    
                
            slot_4_run = row.operator("object.script_run", text = label)
            slot_4_run.script_slot = 4              
        
        
        #Script 6
        if user_settings.num_scripts > 5:
            row = layout.row(align = True)
            slot_5_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_5_load.script_slot = 6
            
            slot_5_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_5_clear.script_slot = 5
            
            if user_settings.script5_path != "": 
                label = path_leaf(user_settings.script5_path)
            else:
                label = ""    
                
            slot_5_run = row.operator("object.script_run", text = label)
            slot_5_run.script_slot = 5      
                                
        
        #Script 7
        if user_settings.num_scripts > 6:
            row = layout.row(align = True)
            slot_6_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_6_load.script_slot = 7
            
            slot_6_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_6_clear.script_slot = 6
            
            if user_settings.script6_path != "": 
                label = path_leaf(user_settings.script6_path)
            else:
                label = ""    
                
            slot_6_run = row.operator("object.script_run", text = label)
            slot_6_run.script_slot = 6      
                    
        
        #Script 8
        if user_settings.num_scripts > 7:
            row = layout.row(align = True)
            slot_7_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_7_load.script_slot = 8
            
            slot_7_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_7_clear.script_slot = 7
            
            if user_settings.script7_path != "": 
                label = path_leaf(user_settings.script7_path)
            else:
                label = ""    
                
            slot_7_run = row.operator("object.script_run", text = label)
            slot_7_run.script_slot = 7      
            
        
        #Script 9
        if user_settings.num_scripts > 8:
            row = layout.row(align = True)
            slot_8_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_8_load.script_slot = 9
            
            slot_8_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_8_clear.script_slot = 8
            
            if user_settings.script8_path != "": 
                label = path_leaf(user_settings.script8_path)
            else:
                label = ""     
                
            slot_8_run = row.operator("object.script_run", text = label)
            slot_8_run.script_slot = 8      
            
        
        #Script 10
        if user_settings.num_scripts > 9:
            row = layout.row(align = True)
            slot_9_load = row.operator("object.script_load", text = "", icon='FILESEL')
            slot_9_load.script_slot = 10
            
            slot_9_clear = row.operator("object.script_clear", text = "", icon='X')
            slot_9_clear.script_slot = 9
            
            if user_settings.script9_path != "": 
                label = path_leaf(user_settings.script9_path)
            else:
                label = ""    
                
            slot_9_run = row.operator("object.script_run", text = label)
            slot_9_run.script_slot = 9      
                        
            
                                    
                                
#----------------------------------Operators    


#-------Menu (main program operation)

class ScriptRunner(bpy.types.Operator, ImportHelper):
    bl_idname = "file.run_script";
    bl_label = "Run Script";
    
    
    filter_glob = StringProperty(
            default="*.py",
            options={'HIDDEN'},
            )

    filename_ext = ".py";



    def execute(self, context):
                
        if (self.filepath == ""):
            pass
        
        else:
            #Check if file exists, could be a path.
            if os.path.isfile(self.filepath):
                ScriptRunner.checkDir(self.filepath)    
        
        return {'FINISHED'}
                               
                               
                           
    def checkDir(file_path):
               
        try:
            error = 0
            script_path = os.path.join( bpy.utils.script_path_user() ,  "modules")
            error = 1
            cache_path = os.path.join( bpy.utils.script_path_user() , "modules" )
            cache_path = os.path.join( cache_path,  "__pycache__"  )
            error = 2
            old_name = path_leaf(file_path).split(".")[0]
            new_name = "script_runner_" + ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10)) + "_" + old_name
            error = 3
            new_file_path =  os.path.join( script_path,  new_name + ".py")
            error = 4
            val = os.makedirs(script_path, exist_ok=True)
            error = 5
                       
            #No creation or mode error with 'makedirs'.
            ScriptRunner.runIt(file_path, new_name, new_file_path, cache_path)
        
        
        except OSError as exception:
            #errno.EEXIST = 17
            if exception.errno != errno.EEXIST:
                msg = "ScriptRunner error in 'checkDir': "
                print(msg, str(error) + ",  sysError: " + str(exception.errno) )
                
            else:
                #Shouldn't get here, but could with directory exists with mode error?
                ScriptRunner.runIt(file_path, new_name, new_file_path, cache_path)    
                
                
        return

        

    def runIt(file_path, new_name, new_file_path, cache_path):
    
        try:
            error = 0
            
            #Allow seamless 'addon' usage by replacing '__main__' with the modules temp name.
            f = open(ScriptRunner.check_escape_string(file_path), encoding="utf8")
            lines = f.readlines()
            f.close()
            
            found = False
            for each in lines:
                if each.find("__main__"):
                    found = True
                    break
                    
            if  found:
                f = open(ScriptRunner.check_escape_string(new_file_path),'w')
                for each in lines:
                    line = each.replace("__main__", new_name)
                    f.writelines(line)
                f.close()
                 
            else:
                shutil.copy(file_path, new_file_path)
            
            
            error = 1
            bpy.utils.load_scripts(refresh_scripts = True)
            error = 2
            file_name = path_leaf(file_path) 
            error = 3
            print("\n")
            importlib.import_module(new_name)                
            
            print("\n" + "Script Runner - running file: " + '"' + file_name + '"' + "......Success!")
            
            ScriptRunner.cleanUp(new_name, new_file_path, cache_path)            
             
        except:
          
            if error == 3:
                user_settings = bpy.context.user_preferences.addons[__name__].preferences
                
                if user_settings.error_msg_verbose:
                    msg = "\n" + "Script Runner - script error in file: " + '"' + file_name + '"'
                    print(msg)
                    
                    formatted_lines = traceback.format_exc().splitlines()
                    for each in formatted_lines:
                        #Ignore the errors created by 'Script Runner'.
                        if each.find("frozen importlib") == -1:
                            if each.find(new_file_path) != -1:
                                each = each.replace(new_file_path, file_path)
                                
                            print(each)
                    
                else:
                    msg = "\n" + "Script Runner - script error in file: " + '"' + file_name + '"  '
                    formatted_lines = traceback.format_exc().splitlines()
                                       
                    for i in range(len(formatted_lines) - 4, len(formatted_lines)):
                        if formatted_lines[i].find(new_file_path) != -1:
                            formatted_lines[i] = formatted_lines[i].replace(new_file_path, file_path)
                        
                        pos = formatted_lines[i].rfind('line ')
                        if pos != -1:
                            line_num = formatted_lines[i][pos::]
          
                     
                    print(msg + line_num)
                    print(formatted_lines[-3])
                    print(formatted_lines[-2])
                    print(formatted_lines[-1])    
                                      
            else:
                msg = "Script Runner error in 'runIt': "
                print(msg, error)       
            
            
            ScriptRunner.cleanUp(new_name, new_file_path, cache_path)    
        
        return


    def check_escape_string(s):
        backslash_map = { '\a': r'\a', '\b': r'\b', '\f': r'\f', '\n': r'\n', '\r': r'\r', '\t': r'\t', '\v': r'\v' }
        for key, value in backslash_map.items():
            s = s.replace(key, value)
        return s
        
        
    def cleanUp(new_name, new_file_path, cache_path):
        try:
            error = 4
            #Clean up the files.
            os.remove(new_file_path)
            error = 5
            #print(ScriptRunner.findFile(new_name + ".*", cache_path))                        
            cache_file = ScriptRunner.findFile(new_name + ".*", cache_path)[0]
            error = 6
            os.remove(cache_file)   
        
        except:
            #If import fails then there is no 'cache_file' to clean up so error 4 gets reported.
            if error != 5:
                msg = "ScriptRunner error in 'cleanUp':  "
                print(msg, error)   
        
        
        return
        
        
    
    def findFile(pattern, path):
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return result
    
    
    
    
    
#----------Script buttons  

class ScriptLoad(bpy.types.Operator, ImportHelper):
    bl_idname = "object.script_load"
    bl_label = "Load Script"
    bl_description = "Assign a script to this slot."

    
    script_slot = IntProperty()
            
    filter_glob = StringProperty(
        default="*.py",
        options={'HIDDEN'},
        )

    filename_ext = ".py";


    def execute(self, context):
                
        if (self.filepath == ""):
            pass
        else:
            #Check if file exists, could be a path.
            if os.path.isfile(self.filepath):
                user_settings = bpy.context.user_preferences.addons[__name__].preferences
               
                if self.script_slot == 1: user_settings.script0_path = self.filepath
                if self.script_slot == 2: user_settings.script1_path = self.filepath
                if self.script_slot == 3: user_settings.script2_path = self.filepath
                if self.script_slot == 4: user_settings.script3_path = self.filepath
                if self.script_slot == 5: user_settings.script4_path = self.filepath
                if self.script_slot == 6: user_settings.script5_path = self.filepath
                if self.script_slot == 7: user_settings.script6_path = self.filepath
                if self.script_slot == 8: user_settings.script7_path = self.filepath
                if self.script_slot == 9: user_settings.script8_path = self.filepath
                if self.script_slot == 10: user_settings.script9_path = self.filepath
                
        return {'FINISHED'}


        
class ScriptClear(bpy.types.Operator):
    bl_idname = "object.script_clear"
    bl_label = ""
    bl_description = "Clear the script from this slot."


    script_slot = IntProperty()
    
    
    def execute(self, context):
        clearSlot(self.script_slot)
        
        return {'FINISHED'}            



class ScriptRun(bpy.types.Operator):
    bl_idname = "object.script_run"
    bl_label = "Script 1"
    bl_description = "Run the script in this slot."


    script_slot = IntProperty()
    
    
    def execute(self, context):
        
        user_settings = context.user_preferences.addons[__name__].preferences
        
        if self.script_slot == 0: file_path = user_settings.script0_path
        if self.script_slot == 1: file_path = user_settings.script1_path
        if self.script_slot == 2: file_path = user_settings.script2_path
        if self.script_slot == 3: file_path = user_settings.script3_path
        if self.script_slot == 4: file_path = user_settings.script4_path
        if self.script_slot == 5: file_path = user_settings.script5_path
        if self.script_slot == 6: file_path = user_settings.script6_path
        if self.script_slot == 7: file_path = user_settings.script7_path
        if self.script_slot == 8: file_path = user_settings.script8_path
        if self.script_slot == 9: file_path = user_settings.script9_path
        
        
        if os.path.isfile(file_path):
            ScriptRunner.checkDir(file_path)
        else:
            clearSlot(self.script_slot)    
            
        return {'FINISHED'}



    


#------------------------Functions

        
def clearSlot(script_slot):
    user_settings = bpy.context.user_preferences.addons[__name__].preferences
        
    if script_slot == 0: user_settings.script0_path = ""
    if script_slot == 1: user_settings.script1_path = ""
    if script_slot == 2: user_settings.script2_path = ""
    if script_slot == 3: user_settings.script3_path = ""
    if script_slot == 4: user_settings.script4_path = ""
    if script_slot == 5: user_settings.script5_path = ""
    if script_slot == 6: user_settings.script6_path = ""
    if script_slot == 7: user_settings.script7_path = ""
    if script_slot == 8: user_settings.script8_path = ""
    if script_slot == 9: user_settings.script9_path = ""  

    return
        
 
 
#If the file ends with a slash, the basename will be empty.
def path_leaf(path):
    head, tail = ntpath.split(path)
    
    return tail or ntpath.basename(head)



#Stored paths in user prefs may no longer be valid.
def checkFiles():
    user_settings = bpy.context.user_preferences.addons[__name__].preferences
    
    if not os.path.isfile(user_settings.script0_path): user_settings.script0_path = ""
    if not os.path.isfile(user_settings.script1_path): user_settings.script1_path = ""
    if not os.path.isfile(user_settings.script2_path): user_settings.script2_path = ""
    if not os.path.isfile(user_settings.script3_path): user_settings.script3_path = ""
    if not os.path.isfile(user_settings.script4_path): user_settings.script4_path = ""
    if not os.path.isfile(user_settings.script5_path): user_settings.script5_path = ""
    if not os.path.isfile(user_settings.script6_path): user_settings.script6_path = ""
    if not os.path.isfile(user_settings.script7_path): user_settings.script7_path = ""
    if not os.path.isfile(user_settings.script8_path): user_settings.script8_path = ""
    if not os.path.isfile(user_settings.script9_path): user_settings.script9_path = ""  


#----------------Register/Unregister

def create_menu(self, context):
   self.layout.operator(ScriptRunner.bl_idname,text="Run Script (.py)");


    
def register():
    bpy.utils.register_class(ScriptRunnerAddonPreferences)
    bpy.utils.register_class(ScriptRunner)
    
    user_settings = bpy.context.user_preferences.addons[__name__].preferences
    if user_settings.display_text_editor:
        bpy.utils.register_class(ScriptRunnerPanel1)
    
    if user_settings.display_3d:
        bpy.utils.register_class(ScriptRunnerPanel2)
        
        
    bpy.utils.register_class(ScriptLoad)
    bpy.utils.register_class(ScriptClear)
    bpy.utils.register_class(ScriptRun)
 
    bpy.types.INFO_MT_file_import.append(create_menu);
    
    checkFiles()
  
    
def unregister():
        
    try:
        if bpy.types.ScriptRunnerPanel1 != None:
            bpy.utils.unregister_class(ScriptRunnerPanel1)    
    except:
        pass

    try:
        if bpy.types.ScriptRunnerPanel2 != None:
            bpy.utils.unregister_class(ScriptRunnerPanel2)    
    except:
        pass
    
        
    bpy.utils.unregister_class(ScriptRunner)
    
    bpy.utils.unregister_class(ScriptLoad)
    bpy.utils.unregister_class(ScriptClear)
    bpy.utils.unregister_class(ScriptRun)
    

    bpy.types.INFO_MT_file_import.remove(create_menu)
    
    bpy.utils.unregister_class(ScriptRunnerAddonPreferences) 
       

       

if (__name__ == "__main__"):
   register();
   
   