#VSE Quick Functions
#
#
#Features that this script includes:
#
#Quickfades - 
#   Can be found in the sequence editor properties panel, or by pressing the 
#        'f' key over the sequencer.
#   Fade Length - The target length for fade editing or creating.
#   Set Fadein/Set Fadeout - Allows easy adding, detecting and changing of 
#       fade in/out.  The script will check the curve for any fades already 
#       applied to the sequence (either manually or by the script), and edit them 
#       if found.  Can apply the same fade to multiple sequences at once.
#   Transition Type - Selects the type of transition for adding.
#   Crossfade Prev/Next Sequence - Allows easy adding of transitions between sequences.
#       Will simply find an overlapping sequence from the active sequence and add 
#       a transition.
#   Smart Cross to Prev/Next - Adjust the length of the active sequence and the 
#       next sequence to create a transition of the target fade length.  Will also
#       attempt to avoid extending the sequences past their end points if possible.
#
#Quicksnaps - 
#   Can be found in the sequence editor 'Strip' menu, or by pressing the 
#       's' key over the sequencer.
#   Allows quickly snapping sequences to each other or moving the cursor to sequences.
#   Cursor To Nearest Second - Will round the cursor position to the nearest 
#       second, based on framerate.
#   Cursor To Beginning/End Of Sequence - Will move the cursor to the beginning or 
#       end of the active sequence.
#   Selected To Cursor - The same as the 'shift-s' shortcut in the VSE.
#   Sequence Beginning/End To Cursor - Moves all selected sequences so their 
#       beginning/end is at the cursor.
#   Sequence To Previous/Next Sequence - Detects the previous or next sequence in the 
#       timeline from the active sequence.  Moves the active sequence so it's beginning
#       or end matches the previous sequence's end or beginning.
#
#Quickzooms - 
#   Can be found in the sequence editor 'View' menu, or by pressing the 
#       'z' key over the sequencer.
#   Zoom All - Zooms the sequencer out to show all sequences.
#   Zoom Selected - Zooms the sequencer to show the currently selected sequence(s).
#   Zoom Cursor - Zooms the sequencer to an amount of frames around the cursor.
#   Size - How many frames should be shown by using Zoom Cursor.  
#       Changing this value will automatically activate Zoom Cursor.
#   Zoom ______ - Several preset zoom values for convenience.
#
#Quickparents - 
#   Can be found in the sequence editor properties panel, or by pressing the 
#       'Ctrl-p' key over the sequencer.
#   This implements a parenting system for sequences, allowing easy 
#       selecting of multiple related sequences.  Note that any relationships will
#       be broken if a sequence is renamed!
#   Select Children - Selects any child sequences found for the currently selected
#       sequence(s).  Also can be accomplished with the shortcut 'Shift-p'.
#   Select Parent - Selects a parent sequence for the currently selected sequence(s).
#   Set Active As Parent - If multiple sequences are selected, this will set
#       selected sequences as children of the active (last selected) sequence.
#   Clear Parent - Removes parent relationships from selected children sequences.
#   Clear Children - Removes child relationships from selected parent sequences.
#   Children or Parents of selected sequence will be shown at the bottom of
#       the Panel/Menu.
#
#QuickContinuous - 
#   Settings can be found in the sequence editor 'View' menu.
#   When Quickcontinuous is enabled, it will constantly run and detect sequence 
#       editing events. 
#   Cursor Following - Automatically moves the sequencer timeline to try and 
#       follow the cursor.  Unfortunately, this can be fooled if the cursor is
#       offscreen, or if the cursor is moved a large amount.
#   Cut/Move Sequence Children - Works with  Quickparents by finding any children 
#       of a moved or cut sequence and performing the same operation on them.  
#       If the sequence is cut, any children under the cursor will be cut as well, 
#       and the script will duplicate parent/child relationships to the 
#       cut sequences.  If the parent sequence is resized and a child sequences have
#       the same endpoints, they will be resized as well.
#   Auto-Select Sequence Children - Works with Quickparents by automatically
#       selecting any child sequences when a sequence is selected.
#   Toggle Quick____ Panel - This set of options can be used to disable panels
#       for QuickFunctions that are not needed.
#
#Quicktitling - 
#   Can be found in the sequence editor properties panel.
#   This will create and edit simple scenes for title overlays.
#   The top area displays the current QuickTitling preset and gives the ability
#       to select different presets, with options to Copy the current preset, 
#       create a New preset, or Delete the selected preset.  The selected 
#       preset can be renamed here as well.
#       When a title scene is selected, the preset of that scene will
#       automatically be loaded here.
#   Create Title Scene - This will create a title scene with the settings
#       shown below.
#   Update Title Scene - If an already created title scene is selected, 
#       this will apply the current shown settings to that scene.
#   Scene Length - The length in frames of the title scene.
#   Text - Title text.
#   Text Font - A menu of the currently loaded fonts in the blend file.
#       Press the '+' button to load a new font.
#   Text Material - A menu of all materials in the blend file.
#       Press the '+' button to create a new material.
#       Use the color square to easily change the color of the current material.
#   X/Y Loc - Determines the center point of the text with 0,0 being
#       the center of the screen.
#   Size - Scale of the text.
#   Extrude Amount - Amount of extrusion to create a 3D look.
#   Bevel Size - Amount of beveling to apply to the text.
#   Bevel Resolution - Subdivisions of the bevel.
#   Shadow Amount - Determines the opacity of the drop shadow.
#   Distance - How far away the shadow plane is from the text object, larger
#       values result in a larger shadow
#   Soft - The amount of blur applied to the drop shadow.
#
#Quicklist - 
#   Can be found in the sequence editor properties panel.
#   Displays a list of loaded sequences and allows you to change various settings.
#   Display Mode - Changes the way the sequences are displayed in the panel:
#       Standard - The largest mode, displays all information on 2 or more lines.
#       Standard Compact - Like Standard, but does not display child sequences,
#           and meta strip sub-sequences.
#       One Line - Displays most information on one line.
#       One Line Compact - Like One Line, but does not display child sequences,
#           and meta strip sub-sequences.
#   Select All - Like pressing the 'a' key in the sequencer, this will toggle
#       the selection of all sequences.
#   Sort by - Reorders the list based on timeline position, title, or length.
#   Eye Icon - Mutes/unmutes sequence.
#   Padlock Icon - Locks/unlocks sequence.
#   Sequence Type Button - Allows selecting and deselecting sequence.
#   Sequence Title - Allows editing of sequence name.
#   Len/Pos - Move or resize the sequence.
#   Proxy settings - Enable/disable proxy and sizes.
#   In non-compact modes, the child sequences will be displayed here, as well as
#       any sub-sequences in a meta strip.
#   If a sequence is an effect, and it is applied to another sequence,
#       it will be indented and placed below it's parent.
#
#
#Known Bugs:
#   Parent/child relationship copy info not showing - self.report doesn't seem to work, but I don't know what else to report the dialog to.
#   Parenting info cant always be copied to cut sequences if a lot of sequences with similar names are cut at once
#   Cursor following is inconsistant - I have not found a way to determine the current zoom level.
#   Continuous mode may stop working and need to be disabled and re-enabled... still no idea why
#
#Todo:
#   Possibly add an autozoom continuous function that will attempt to zoom to the most appropriate size depending on what is being done
#   Add ability to manually change auto-scroll speed, or see if it is possible to determine zoom distance
#   Add quickproxy to auto-generate proxys of a certain size for all sequences in sequencer, and all imported sequences, unless they already exist
#   Add functions for quicklist - swap sequence with previous or next if in position sort
#
#Changelog:
#   0.86
#       Fixed transparency in title scenes
#       Fixed no sequences in a scene throwing an error
#       Added auto-parenting of movie sequences with sound
#       Cleaned up quicklist, meta strips now list sub-sequences, effects are indented under the parent sequence
#   0.87
#       Continuous functions should work inside meta strips now
#       Fixed a couple small bugs
#   0.88
#       Added drop shadows to titler
#       Added color picker and material duplicate button to titler
#       Hopefully fixed continuous functions from throwing errors when no strips are loaded
#       Improved adding/changing fades, added a clear fades button
#   0.89
#       Fixed zoom to cursor not working inside meta strips
#       Fixed zoom to cursor not working in Blender 2.74
#       Fixed child sequences being moved twice if they were manually moved along with the parent
#       Recoded continuous function - parenting is more reliable, all cut sequences are detected and parented properly, fades are now moved when a sequence is resized
#       Removed continuous snapping, snapping is now built-in in blender as of 2.73
#       Added quick zoom presets
#       Added settings to hide different Quick panels
#       Added QuickParenting option to auto-select child sequences, also child sequences' endpoints will be moved when a parent is resized if they match up.
#       Added font loading button to QuickTitler
#       Added templates to QuickTitler
#       Added display modes for QuickList
#       Cleaned and commented code
#   0.89.1
#       Removed an extra check in the modal function that wasn't doing anything but slowing down the script

import bpy
import math
import os
from bpy.app.handlers import persistent


bl_info = {
    "name": "VSE Quick Functions",
    "description": "Improves functionality of the sequencer by adding new menus for snapping, adding fades, zooming, sequence parenting, playback speed, and easy creation of title scenes.",
    "author": "Hudson Barkley (Snu)",
    "version": (0, 89, 1),
    "blender": (2, 74, 0),
    "location": "Sequencer Panels; Sequencer Menus; Sequencer S, F, Z, Ctrl-P, Shift-P Shortcuts",
    "wiki_url": "none yet",
    "category": "Sequencer"
}


#Functions used by various features

#Toggle Quick panels off and on
def panels_toggle(panel):
    scene = bpy.context.scene
    panel_settings = scene.quickenabledpanels.split(',')
    if panel in panel_settings:
        panel_settings.pop(panel_settings.index(panel))
    else:
        panel_settings.append(panel)
    scene.quickenabledpanels = ','.join(panel_settings)

#Draws the menu for settings
def draw_quicksettings_menu(self, context):
    layout = self.layout
    layout.menu('vseqf.settings_menu', text="Quick Settings")

#Returns an array of sequences sorted by distance from a sequence
def find_close_sequence(sequences, selected_sequence, direction, mode='overlap'):
    #'sequences' is a list of sequences to search through
    #'selected_sequence' is the active sequence
    #'direction' needs to be 'next' or 'previous'
    #'mode' 
    #   if mode is overlap, will only return overlapping sequences
    #   if mode is channel, will only return sequences in sequence's channel
    #   if mode is set to other, all sequences are considered
    
    overlap_nexts = []
    overlap_previous = []
    nexts = []
    previous = []
    
    #iterate through sequences to find all sequences to one side of the selected sequence
    for current_sequence in sequences:
        #don't bother with sound type sequences
        if (current_sequence.type != 'SOUND'):
            if current_sequence.frame_final_start >= selected_sequence.frame_final_end:
                #current sequence is after selected sequence
                #dont append if channel mode and sequences are not on same channel
                if (mode == 'channel') & (selected_sequence.channel != current_sequence.channel):
                    pass
                else:
                    nexts.append(current_sequence)
            elif current_sequence.frame_final_end <= selected_sequence.frame_final_start:
                #current sequence is before selected sequence
                #dont append if channel mode and sequences are not on same channel
                if (mode == 'channel') & (selected_sequence.channel != current_sequence.channel):
                    pass
                else:
                    previous.append(current_sequence)

            elif (current_sequence.frame_final_start > selected_sequence.frame_final_start) & (current_sequence.frame_final_start < selected_sequence.frame_final_end) & (current_sequence.frame_final_end > selected_sequence.frame_final_end):
                #current sequence startpoint is overlapping selected sequence
                overlap_nexts.append(current_sequence)
            elif (current_sequence.frame_final_end > selected_sequence.frame_final_start) & (current_sequence.frame_final_end < selected_sequence.frame_final_end) & (current_sequence.frame_final_start < selected_sequence.frame_final_start):
                #current sequence endpoint is overlapping selected sequence
                overlap_previous.append(current_sequence)

    nexts_all = nexts + overlap_nexts
    previous_all = previous + overlap_previous
    if direction == 'next':
        if mode == 'overlap':
            if len(overlap_nexts) > 0:
                return min(overlap_nexts, key=lambda overlap: abs(overlap.channel - selected_sequence.channel))
            else:
                #overlap mode, but no overlaps
                return False
        else:
            if len(nexts_all) > 0:
                return min(nexts_all, key=lambda next: (next.frame_final_start - selected_sequence.frame_final_end))
            else:
                #no next sequences
                return False
    else:
        if mode == 'overlap':
            if len(overlap_previous) > 0:
                return min(overlap_previous, key=lambda overlap: abs(overlap.channel - selected_sequence.channel))
            else:
                return False
        else:
            if len(previous_all) > 0:
                return min(previous_all, key=lambda prev: (selected_sequence.frame_final_start - prev.frame_final_end))
            else:
                return False

#Converts a frame number to a standard timecode in the format HH:MM:SS:FF
def timecode_from_frames(frame, framespersecond, levels=0, subsecondtype='miliseconds'):
    #the 'levels' variable limits the larger timecode elements
    #   a levels = 3 will return MM:SS:FF
    #   a levels = 0 will auto format the returned value to cut off any zero divisors
    #   a levels = 4 will return the entire timecode every time
    #the 'subsecondtime' variable determines the fraction denominator for the FF section,
    #   the default of 'miliseconds' will return the last value as a division of 100 (0-99)
    #   setting it to 'frames' will return the last value as a division of the frames per second
    
    #ensure the levels value is sane
    if (levels > 4):
        levels = 4
    
    #set the sub second divisor type
    if (subsecondtype == 'frames'):
        subseconddivisor = framespersecond
    else:
        subseconddivisor = 100
    
    #check for negative values
    if frame < 0:
        negative = True
        frame = abs(frame)
    else:
        negative = False
    
    #calculate divisions, starting at largest and taking the remainder of each to calculate the next smaller
    totalhours = math.modf(frame/framespersecond/60/60)
    totalminutes = math.modf(totalhours[0] * 60)
    remainingseconds = math.modf(totalminutes[0] * 60)
    hours = int(totalhours[1])
    minutes = int(totalminutes[1])
    seconds = int(remainingseconds[1])
    subseconds = int(remainingseconds[0] * subseconddivisor)

    #format and return the time value
    time = str(hours).zfill(2)+':'+str(minutes).zfill(2)+':'+str(seconds).zfill(2)+':'+str(subseconds).zfill(2)[-2:]
    if levels == 0:
        #cut off any larger divisors that are zero
        while (time[0:3] == '00:'):
            time = time[3:len(time)]
        if negative:
            time = '-'+time
        return time
    else:
        time = time.split(':', 4 - levels)[-1]
        if negative:
            time = '-'+time
        return time



#Functions related to continuous update

#Enable or disable Quick Continuous functions
@persistent
def toggle_continuous(self, context=bpy.context):
    if bpy.context.scene.quickcontinuousenable:
        bpy.ops.vseqf.continuous('INVOKE_DEFAULT')

#Function to guess the name of a new object who's name already exists
def renamed(name):
    split_name = name.rsplit('.', 1)
    if len(split_name) <= 1:
        #name has no extension or number
        return name + '.001'
    
    #name has an ending number such as 'name.001' or extension
    if split_name[1].isdigit():
        #name ends in number
        old_number = int(split_name[1])
        new_number = old_number + 1
        return split_name[0] + '.' + str(new_number).zfill(3)
        
    else:
        #name ends in an extension
        return split_name[0] + '.001'

#Function to get the base name of an object
def base_name(name):
    split_name = name.rsplit('.', 1)
    if len(split_name) <= 1:
        return name
    if split_name[1].isdigit():
        return split_name[0]
    else:
        return name


#Functions related to QuickTitling

#If the active sequence is a title scene, return that scene, otherwise return the current scene
def find_titling_scene():
    selected = titling_scene_selected()
    if selected:
        return selected
    else:
        return bpy.context.scene

#determines if a titling scene is selected
def titling_scene_selected():
    sequence_editor = bpy.context.scene.sequence_editor
    if hasattr(sequence_editor, 'active_strip'):
        active_sequence = sequence_editor.active_strip
    else:
        active_sequence = None
    if active_sequence == None:
        #if there is no active sequence, this will prevent an error message
        return False
    elif (('QuickTitle: ' in active_sequence.name) & (active_sequence.type == 'SCENE')):
        #the active sequence is probably a quicktitle scene, return that scene
        return active_sequence.scene
    else:
        #the active sequence exists, but its probably not a quicktitle scene, return the current scene
        return False

#Function to return the current QuickTitle preset depending on what is selected in the sequencer
def current_quicktitle():
    scene = find_titling_scene()
    if len(scene.quicktitles) > 0:
        return scene.quicktitles[0]
    else:
        return False

#Function to copy one QuickTitle preset to another
def copy_title_preset(old_title, title):
    title.name = old_title.name
    title.font = old_title.font
    title.x = old_title.x
    title.y = old_title.y
    title.size = old_title.size
    title.extrude = old_title.extrude
    title.bevel = old_title.bevel
    title.bevelres = old_title.bevelres
    title.shadowsize = old_title.shadowsize
    title.shadowamount = old_title.shadowamount
    title.shadowsoft = old_title.shadowsoft
    title.material = old_title.material
    title.text = old_title.text
    title.length = old_title.length

#Function to update a QuickTitle sequence
def quicktitle_update(sequence, quicktitle):
    
    #attempt to find the objects that need to be updated
    scene = sequence.scene
    text = None
    shadow = None
    shadowLamp = None
    for object in scene.objects:
        if (object.type == 'FONT'):
            text = object
        if ("QuickTitlerShadow" in object.name):
            shadow = object
        if ("QuickTitlerLamp" in object.name):
            shadowLamp = object
    if ((text == None) or (shadow == None) or (shadowLamp == None)):
        print('Selected Title Scene Is Incomplete')
        self.report({'WARNING'}, 'Selected Title Scene Is Incomplete')
        return
    
    name = "QuickTitle: "+quicktitle.text
    
    #Scene update
    scene.frame_end = quicktitle.length
    index = bpy.data.materials.find(quicktitle.material)
    if (index >= 0):
        text.data.materials.clear()
        text.data.materials.append(bpy.data.materials[index])
    else:
        material = bpy.data.materials.new('QuickTitler Material')
        quicktitle.material = material.name
    text.location = (quicktitle.x, quicktitle.y, 0)
    text.scale = (quicktitle.size, quicktitle.size, quicktitle.size)
    text.data.extrude = quicktitle.extrude
    text.data.bevel_depth = quicktitle.bevel
    text.data.bevel_resolution = quicktitle.bevelres
    text.data.body = quicktitle.text
    text.data.font = bpy.data.fonts[quicktitle.font]
    shadow.material_slots[0].material.alpha = quicktitle.shadowamount
    shadowLamp.data.shadow_buffer_soft = quicktitle.shadowsoft * 10
    shadow.location = (0, 0, -(quicktitle.shadowsize / 8))
    scene.name = name
    sequence.name = name
    scene.quicktitles[0].name = name
    bpy.ops.sequencer.reload(adjust_length=True)
    bpy.ops.sequencer.refresh_all()
    
#Function to create QuickTitle scenes and sequences
def quicktitle_create(quicktitle):
    scene = bpy.context.scene
    name = "QuickTitle: "+quicktitle.text
    
    #Basic scene setup
    bpy.ops.scene.new(type='EMPTY')
    title_scene = bpy.context.scene
    title_scene.name = name
    title_scene.frame_end = quicktitle.length
    title_scene.layers = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    title_scene.render.engine = 'BLENDER_RENDER'
    title_scene.render.alpha_mode = 'TRANSPARENT'
    title_scene.render.image_settings.file_format = 'PNG'
    title_scene.render.image_settings.color_mode = 'RGBA'
    title_scene.quicktitles.clear()
    title_scene.quicktitles.add()
    copy_title_preset(quicktitle, title_scene.quicktitles[0])
    title_scene.quicktitles[0].name = name

    #Camera setup
    bpy.ops.object.camera_add()
    camera = bpy.context.scene.objects.active
    title_scene.camera = camera
    camera.location = ((0, 0, 15))
    camera.name = "QuickTitlerCamera"
    
    #Basic lamps setup
    lampEnergy = 0.5
    bpy.ops.object.lamp_add(location=(-4, -2.5, 2))
    lamp1 = bpy.context.scene.objects.active
    lamp1.data.energy = lampEnergy
    lamp1.data.shadow_method = 'NOSHADOW'
    bpy.ops.object.lamp_add(location=(4, -2.5, 2))
    lamp2 = bpy.context.scene.objects.active
    lamp2.data.energy = lampEnergy
    lamp2.data.shadow_method = 'NOSHADOW'
    bpy.ops.object.lamp_add(location=(-4, 2.5, 2))
    lamp3 = bpy.context.scene.objects.active
    lamp3.data.energy = lampEnergy
    lamp3.data.shadow_method = 'NOSHADOW'
    bpy.ops.object.lamp_add(location=(4, 2.5, 2))
    lamp4 = bpy.context.scene.objects.active
    lamp4.data.energy = lampEnergy
    lamp4.data.shadow_method = 'NOSHADOW'
    
    #Shadow lamp setup
    bpy.ops.object.lamp_add(type= 'SPOT', location=(0, 0, 4))
    shadowLamp = bpy.context.scene.objects.active
    shadowLamp.name = 'QuickTitlerLamp'
    shadowLamp.data.use_only_shadow = True
    shadowLamp.data.shadow_method = 'BUFFER_SHADOW'
    shadowLamp.data.shadow_buffer_type = 'REGULAR'
    shadowLamp.data.shadow_buffer_soft = 10
    shadowLamp.data.shadow_buffer_bias = 0.1
    shadowLamp.data.shadow_buffer_size = 512
    shadowLamp.data.shadow_buffer_samples = 8
    shadowLamp.data.spot_size = 2.182
    
    #Shadow setup
    bpy.ops.mesh.primitive_plane_add(radius=10)
    shadow = bpy.context.scene.objects.active
    shadow.name = "QuickTitlerShadow"
    shadow.draw_type = 'WIRE'
    shadowMaterial = bpy.data.materials.new('QuickTitlerShadow')
    shadowMaterial.diffuse_color = (0, 0, 0)
    shadowMaterial.diffuse_intensity = 1
    shadowMaterial.specular_intensity = 0
    shadowMaterial.use_transparency = True
    shadowMaterial.use_cast_buffer_shadows = False
    shadowMaterial.shadow_only_type = 'SHADOW_ONLY'
    shadowMaterial.use_only_shadow = True
    shadow.data.materials.append(shadowMaterial)
    
    #Text setup
    bpy.ops.object.text_add()
    text = bpy.context.scene.objects.active
    text.data.align = 'CENTER'
    text.name = "QuickTitlerText"
    
    #Add scene to sequencer
    bpy.context.screen.scene = scene
    bpy.ops.sequencer.scene_strip_add(frame_start=scene.frame_current, scene=title_scene.name)
    sequence = bpy.context.scene.sequence_editor.active_strip
    sequence.name = name
    sequence.blend_type = 'ALPHA_OVER'
    scene = title_scene



#Functions related to QuickSpeed

#Function for frame skipping with the speed step handler
@persistent
def frame_step(scene):
    scene = bpy.context.scene
    step = scene.step
    if (step == 1):
        #if the step is 1, only one frame in every 3 will be skipped
        if (scene.frame_current % 3 == 0):
            scene.frame_current = scene.frame_current + 1
    if (step == 2):
        #if the step is 2, every other frame is skipped
        if (scene.frame_current % 2 == 0):
            scene.frame_current = scene.frame_current + 1
    if (step > 2):
        #if the step is greater than 2, (step-2) frames will be skipped per frame
        scene.frame_current = scene.frame_current + (step - 2)

#Draws the speed selector in the sequencer header
def draw_quickspeed_header(self, context):
    layout = self.layout
    scene = context.scene
    self.layout_width = 30
    layout.prop(scene, 'step', text="Speed Step")



#Functions related to QuickZoom

#Draws the menu for the QuickZoom shortcuts
def draw_quickzoom_menu(self, context):
    layout = self.layout
    layout.menu('vseqf.quickzooms_menu', text="Quick Zoom")

#Function to zoom to an area on the sequencer timeline
def zoom_custom(begin, end):
    scene = bpy.context.scene
    selected = []
    
    #Find sequence editor, or create if not found
    try:
        sequences = bpy.context.sequences
    except:
        scene.sequence_editor_create()
        sequences = bpy.context.sequences
    
    #Save selected sequences and active strip because they will be overwritten
    for sequence in sequences:
        if (sequence.select):
            selected.append(sequence)
            sequence.select = False
    active = bpy.context.scene.sequence_editor.active_strip
    
    #Determine preroll for the zoom
    zoomlength = end - begin
    if zoomlength > 60:
        preroll = (zoomlength-60) / 10
    else:
        preroll = 0
    
    #Create a temporary sequence, zoom in on it, then delete it
    zoomClip = scene.sequence_editor.sequences.new_effect(name='temp', type='ADJUSTMENT', channel=1, frame_start=begin-preroll, frame_end=end)
    scene.sequence_editor.active_strip = zoomClip
    for region in bpy.context.area.regions:
        if (region.type == 'WINDOW'):
            override = {'region': region, 'window': bpy.context.window, 'screen': bpy.context.screen, 'area': bpy.context.area, 'scene': bpy.context.scene}
            bpy.ops.sequencer.view_selected(override)
    bpy.ops.sequencer.delete()
    
    #Reset selected sequences and active strip
    for sequence in selected:
        sequence.select = True
    bpy.context.scene.sequence_editor.active_strip = active

#Function to zoom near the cursor based on the 'zoomsize' scene variable
def zoom_cursor(self=None, context=None):
    cursor = bpy.context.scene.frame_current
    zoom_custom(cursor, (cursor + bpy.context.scene.zoomsize))



#Functions related to QuickFades

#Function to add a crossfade between two sequences, the transition type is determined by the scene variable 'transition'
def crossfade(first_sequence, second_sequence):
    type = bpy.context.scene.transition
    sequences = bpy.context.sequences
    
    bpy.ops.sequencer.select_all(action='DESELECT')
    first_sequence.select = True
    second_sequence.select = True
    bpy.context.scene.sequence_editor.active_strip = second_sequence
    bpy.ops.sequencer.effect_strip_add(type=type)

#Function to detect, create and edit fadein and fadeout for sequences
def fades(sequence, fade_length, type, mode, fade_low_point_frame=False):
    #sequence = vse sequence
    #fade_length = positive value of fade in frames
    #type = 'in' or 'out'
    #mode = 'detect' or 'set' or 'clear'
    
    scene = bpy.context.scene
    
    #These functions check for the needed variables and create them if in set mode.  Otherwise, ends the function.
    if scene.animation_data == None:
        #No animation data in scene, create it
        if (mode == 'set'):
            scene.animation_data_create()
        else:
            return 0
    if scene.animation_data.action == None:
        #No action in scene, create it
        if mode == 'set':
            action = bpy.data.actions.new(scene.name+"Action")
            scene.animation_data.action = action
        else:
            return 0
    
    all_curves = scene.animation_data.action.fcurves
    fade_curve = False #curve for the fades
    fade_low_point = False #keyframe that the fade reaches minimum value at
    fade_high_point = False #keyframe that the fade starts maximum value at
    if (type == 'in'):
        if not fade_low_point_frame:
            fade_low_point_frame = sequence.frame_final_start
    else:
        if not fade_low_point_frame:
            fade_low_point_frame = sequence.frame_final_end
        fade_length = -fade_length
    fade_high_point_frame = fade_low_point_frame + fade_length
    
    fade_max_value = 1 #set default fade max value, this may change
    
    #set up the data value to fade
    if sequence.type == 'SOUND':
        fade_variable = 'volume'
    else:
        fade_variable = 'blend_alpha'

    #attempts to find the fade keyframes by iterating through all curves in scene
    for curve in all_curves:
        if (curve.data_path == 'sequence_editor.sequences_all["'+sequence.name+'"].'+fade_variable):
            #keyframes found
            fade_curve = curve
            
            #delete keyframes and end function
            if mode == 'clear':
                all_curves.remove(fade_curve)
                return 0
            
    if not fade_curve:
        #no fade animation curve found, create and continue if instructed to, otherwise end function
        if (mode == 'set'):
            fade_curve = all_curves.new(data_path=sequence.path_from_id(fade_variable))
            keyframes = fade_curve.keyframe_points
        else:
            return 0
    
    #Detect fades or add if set mode
    fade_keyframes = fade_curve.keyframe_points
    if len(fade_keyframes) == 0:
        #no keyframes found, create them if instructed to do so
        if (mode == 'set'):
            fade_max_value = getattr(sequence, fade_variable)
            set_fade(fade_keyframes, type, fade_low_point_frame, fade_high_point_frame, fade_max_value)
        else:
            return 0
            
    elif len(fade_keyframes) == 1:
        #only one keyframe, use y value of keyframe as the max value for a new fade
        if (mode == 'set'):
            #determine fade_max_value from value at one keyframe
            fade_max_value = fade_keyframes[0].co[1]
            if fade_max_value == 0:
                fade_max_value = 1
            
            #remove lone keyframe, then add new fade
            fade_keyframes.remove(fade_keyframes[0])
            set_fade(fade_keyframes, type, fade_low_point_frame, fade_high_point_frame, fade_max_value)
        else:
            return 0
    
    elif len(fade_keyframes) > 1:
        #at least 2 keyframes, there may be a fade already
        if type == 'in':
            fade_low_point = fade_keyframes[0]
            fade_high_point = fade_keyframes[1]
        elif type == 'out':
            fade_low_point = fade_keyframes[-1]
            fade_high_point = fade_keyframes[-2]
        
        #check to see if the fade points are valid
        if fade_low_point.co[1] == 0:
            #opacity is 0, assume there is a fade
            if fade_low_point.co[0] == fade_low_point_frame:
                #fade low point is in the correct location
                if fade_high_point.co[1] > fade_low_point.co[1]:
                    #both fade points are valid
                    if mode == 'set':
                        fade_max_value = fade_high_point.co[1]
                        set_fade(fade_keyframes, type, fade_low_point_frame, fade_high_point_frame, fade_max_value, fade_low_point=fade_low_point, fade_high_point=fade_high_point)
                        return fade_length
                    else:
                        #fade detected!
                        return abs(fade_high_point.co[0] - fade_low_point.co[0])
                else:
                    #fade high point is not valid, low point is tho
                    if mode == 'set':
                        fade_max_value = fade_curve.evaluate(fade_high_point_frame)
                        set_fade(fade_keyframes, type, fade_low_point_frame, fade_high_point_frame, fade_max_value, fade_low_point=fade_low_point)
                        return fade_length
                    else:
                        return 0
            else:
                #fade low point is not in the correct location
                if mode == 'set':
                    #check fade high point
                    if fade_high_point.co[1] > fade_low_point.co[1]:
                        #fade exists, but is not set up properly
                        fade_max_value = fade_high_point.co[1]
                        set_fade(fade_keyframes, type, fade_low_point_frame, fade_high_point_frame, fade_max_value, fade_low_point=fade_low_point, fade_high_point=fade_high_point)
                        return fade_length
                    else:
                        #no valid fade high point
                        fade_max_value = fade_curve.evaluate(fade_high_point_frame)
                        set_fade(fade_keyframes, type, fade_low_point_frame, fade_high_point_frame, fade_max_value, fade_low_point=fade_low_point)
                        return fade_length
                else:
                    return 0
            
        else:
            #no valid fade detected, other keyframes are on the curve tho
            if mode == 'set':
                fade_max_value = fade_curve.evaluate(fade_high_point_frame)
                set_fade(fade_keyframes, type, fade_low_point_frame, fade_high_point_frame, fade_max_value)
                return fade_length
            else:
                return 0

#creates a fade in or out on a set of keyframes, can be passed keyframes to adjust
def set_fade(fade_keyframes, direction, fade_low_point_frame, fade_high_point_frame, fade_max_value, fade_low_point = None, fade_high_point = None):
    #check if any keyframe points other than the fade high and low points are in the fade area, delete them if needed
    for keyframe in fade_keyframes:
        if direction == 'in':
            if (keyframe.co[0] < fade_high_point_frame) and (keyframe.co[0] > fade_low_point_frame):
                if (keyframe != fade_low_point) and (keyframe != fade_high_point):
                    fade_keyframes.remove(keyframe)
        if direction == 'out':
            if (keyframe.co[0] > fade_high_point_frame) and (keyframe.co[0] < fade_low_point_frame):
                if (keyframe != fade_low_point) and (keyframe != fade_high_point):
                    fade_keyframes.remove(keyframe)

    fade_length = abs(fade_high_point_frame - fade_low_point_frame)
    handle_offset = fade_length * .38
    if fade_low_point:
        if fade_length != 0:
            #move fade low point to where it should be
            fade_low_point.co = ((fade_low_point_frame, 0))
            fade_low_point.handle_left = ((fade_low_point_frame - handle_offset, 0))
            fade_low_point.handle_right = ((fade_low_point_frame + handle_offset, 0))
        else:
            #remove fade low point
            fade_keyframes.remove(fade_low_point)
    else:
        if fade_high_point_frame != fade_low_point_frame:
            #create new fade low point
            fade_keyframes.insert(frame=fade_low_point_frame, value=0)
        
    if fade_high_point:
        #move fade high point to where it should be
        fade_high_point.co = ((fade_high_point_frame, fade_max_value))
        fade_high_point.handle_left = ((fade_high_point_frame - handle_offset, fade_max_value))
        fade_high_point.handle_right = ((fade_high_point_frame + handle_offset, fade_max_value))
    else:
        #create new fade high point
        fade_keyframes.insert(frame=fade_high_point_frame, value=fade_max_value)



#Functions related to QuickParents

#Function to look for a sound sequence that is tied to a video sequence
def find_sound_child(parent_sequence, sequences):
    for sequence in sequences:
        if ((os.path.splitext(sequence.name)[0] == os.path.splitext(parent_sequence.name)[0]) & (sequence.type == 'SOUND')):
            return sequence
    return False

#Function to add QuickParents relationships between a parent sequence and one or more child sequences
def add_children(parent_sequence, child_sequences):
    clean_relationships()
    for child_sequence in child_sequences:
        if (child_sequence.name != parent_sequence.name):
            children = find_children(parent_sequence)
            if (child_sequence not in children):
                relationship = bpy.context.scene.parenting.add()
                relationship.parent = parent_sequence.name
                relationship.child = child_sequence.name

#Function to return a list of sequences that are QuickParents children of an inputted sequence
def find_children(parent_sequence):
    scene = bpy.context.scene
    sequences = scene.sequence_editor.sequences_all
    child_sequences = []
    for relationship in scene.parenting:
        if (relationship.parent == parent_sequence.name):
            child_name = relationship.child
            if child_name in sequences:
                child_sequences.append(sequences[child_name])
    return child_sequences

#Function to return the QuickParents parent sequence to a child sequence
def find_parent(child_sequence):
    scene = bpy.context.scene
    sequences = scene.sequence_editor.sequences_all
    for relationship in scene.parenting:
        if (relationship.child == child_sequence.name):
            parent_name = relationship.parent
            if parent_name in sequences:
                return sequences[parent_name]
    return False

#Function to remove QuickParents children from a parent sequence
def clear_children(parent_sequence):
    scene = bpy.context.scene
    for index in reversed(range(len(scene.parenting))):
        if (scene.parenting[index].parent == parent_sequence.name):
            scene.parenting.remove(index)
    clean_relationships()

#Function to remove a QuickParents parent relationship from a child sequence
def clear_parent(child_sequence):
    scene = bpy.context.scene
    for index in reversed(range(len(scene.parenting))):
        if (scene.parenting[index].child == child_sequence.name):
            scene.parenting.remove(index)
    clean_relationships()

#Function that finds QuickParents child sequences, then selects them
def select_children(parent_sequence):
    children = find_children(parent_sequence)
    for child in children:
        child.select = True

#Function that finds a QuickParents parent sequence and selects it
def select_parent(child_sequence):
    parent = find_parent(child_sequence)
    if parent:
        parent.select = True

#Function that checks the QuickParents relationships property for any stale relationships
def clean_relationships():
    scene = bpy.context.scene
    sequences = scene.sequence_editor.sequences_all
    for index, relationship in enumerate(scene.parenting):
        if ( (sequences.find(relationship.parent) == -1) | (sequences.find(relationship.child) == -1) ):
            scene.parenting.remove(index)



#Functions related to QuickSnaps

#Draws the QuickSnaps menu
def draw_quicksnap_menu(self, context):
    layout = self.layout
    layout.menu('vseqf.quicksnaps_menu', text="Quick Snaps")



#Classes related to QuickList

#QuickList panel
class VSEQFQuickListPanel(bpy.types.Panel):
    bl_label = "Quick List"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
    @classmethod
    def poll(self, context):
        #Check if panel is disabled
        if 'list' not in context.scene.quickenabledpanels:
            return False
        
        #Check for sequences
        if not bpy.context.sequences:
            return False
        if len(bpy.context.sequences) > 0:
            return True
        else:
            return False
    
    def draw(self, contex):
        scene = bpy.context.scene
        sequencer = scene.sequence_editor
        sequences = bpy.context.sequences
        
        #Sort the sequences
        sorted = list(sequences)
        if (scene.quicklistsort == 'Title'):
            sorted.sort(key=lambda sequence: sequence.name)
        elif (scene.quicklistsort =='Length'):
            sorted.sort(key=lambda sequence: sequence.frame_final_duration)
        else:
            sorted.sort(key=lambda sequence: sequence.frame_final_start)

        #Check for effect sequences and move them next to their parent sequence
        for sequence in sorted:
            if hasattr(sequence, 'input_1'):
                resort = sorted.pop(sorted.index(sequence))
                parentindex = sorted.index(sequence.input_1)
                sorted.insert(parentindex + 1, resort)
        
        layout = self.layout
        
        #Display Mode
        row = layout.row()
        row.prop(scene, 'quicklistdisplay')
        
        #Select all and sort buttons
        if scene.quicklistdisplay == 'STANDARD':
            row = layout.row()
            row.operator('vseqf.quicklist_select', text='Select/Deselect All Sequences').sequence = ''

            row = layout.row(align=True)
            row.alignment = 'EXPAND'
            row.label('Sort By:')
        else:
            row = layout.row(align=True)
            row.alignment = 'EXPAND'
            row.operator('vseqf.quicklist_select', text='Select All').sequence = ''
            row.label('Sort:')
        sub = row.column(align=True)
        sub.operator('vseqf.quicklist_sortby', text='Position').method = 'Position'
        if scene.quicklistsort == 'Position':
            sub.active = True
        else:
            sub.active = False
        sub = row.column(align=True)
        sub.operator('vseqf.quicklist_sortby', text='Title').method = 'Title'
        if scene.quicklistsort == 'Title':
            sub.active = True
        else:
            sub.active = False
        sub = row.column(align=True)
        sub.operator('vseqf.quicklist_sortby', text='Length').method = 'Length'
        if scene.quicklistsort == 'Length':
            sub.active = True
        else:
            sub.active = False

        #Display all sequences
        for index, sequence in enumerate(sorted):
            if (hasattr(sequence, 'input_1')):
                #Effect sequence, add an indent
                row = box.row()
                row.separator()
                row.separator()
                outline = row.split()
            else:
                if scene.quicklistdisplay == 'STANDARD' or scene.quicklistdisplay == 'ONELINE':
                    outline = layout.box()
                else:
                    row.separator()
                    row = layout.row()
                    outline = layout.row()
            box = outline.column()
            
            if scene.quicklistdisplay == 'ONELINE' or scene.quicklistdisplay == 'ONELINECOMPACT':
                row = box.row(align=True)
                split = row.split(align=True)
                split.prop(sequence, 'mute', text='')
                split.prop(sequence, 'lock', text='')
                split = row.split(align=True, percentage=0.2)
                col = split.column(align=True)
                col.operator('vseqf.quicklist_select', text="("+sequence.type+")").sequence = sequence.name
                col.active = sequence.select
                col = split.column(align=True)
                col.prop(sequence, 'name', text='')
                
                split = row.split(percentage=0.8)
                col = split.row(align=True)
                col.prop(sequence, 'frame_final_duration', text="Len:"+timecode_from_frames(sequence.frame_final_duration, scene.render.fps)+", ")
                col.prop(sequence, 'frame_start', text="Pos:"+timecode_from_frames(sequence.frame_start, scene.render.fps)+", ")
                col = split.row()
                if (sequence.type != 'SOUND') and (not hasattr(sequence, 'input_1')):
                    col.prop(sequence, 'use_proxy', text='Proxy')
                    if (sequence.use_proxy):
                        #Proxy is enabled, add row for proxy settings
                        row = box.row()
                        split = row.split(percentage=0.33)
                        col = split.row(align=True)
                        col.prop(sequence.proxy, 'quality')
                        col = split.row(align=True)
                        col.prop(sequence.proxy, 'build_25')
                        col.prop(sequence.proxy, 'build_50')
                        col.prop(sequence.proxy, 'build_75')
                        col.prop(sequence.proxy, 'build_100')
                else:
                    col.label('')

            else:
                #First row - mute, lock, type and title
                row = box.row(align=True)
                split = row.split(align=True)
                split.prop(sequence, 'mute', text='')
                split.prop(sequence, 'lock', text='')
                split = row.split(align=True, percentage=0.2)
                col = split.column(align=True)
                col.operator('vseqf.quicklist_select', text="("+sequence.type+")").sequence = sequence.name
                col.active = sequence.select
                col = split.column(align=True)
                col.prop(sequence, 'name', text='')
                
                #Second row - length, position and proxy toggle
                row = box.row()
                split = row.split(percentage=0.8)
                col = split.row(align=True)
                col.prop(sequence, 'frame_final_duration', text="Len:"+timecode_from_frames(sequence.frame_final_duration, scene.render.fps)+", ")
                col.prop(sequence, 'frame_start', text="Pos:"+timecode_from_frames(sequence.frame_start, scene.render.fps)+", ")
                col = split.row()
                if (sequence.type != 'SOUND') and (not hasattr(sequence, 'input_1')):
                    col.prop(sequence, 'use_proxy', text='Proxy')
                    if (sequence.use_proxy):
                        #Proxy is enabled, add row for proxy settings
                        row = box.row()
                        split = row.split(percentage=0.33)
                        col = split.row(align=True)
                        col.prop(sequence.proxy, 'quality')
                        col = split.row(align=True)
                        col.prop(sequence.proxy, 'build_25')
                        col.prop(sequence.proxy, 'build_50')
                        col.prop(sequence.proxy, 'build_75')
                        col.prop(sequence.proxy, 'build_100')
            
            #List children sequences if found
            children = find_children(sequence)
            if len(children) > 0 and (scene.quicklistdisplay != 'COMPACT' and scene.quicklistdisplay != 'ONELINECOMPACT'):
                row = box.row()
                split = row.split(percentage=0.25)
                col = split.column()
                col.label('Children:')
                col = split.column()
                for child in children:
                    col.label(child.name)
            
            #List sub-sequences in a meta sequence
            if sequence.type == 'META' and (scene.quicklistdisplay != 'COMPACT' and scene.quicklistdisplay != 'ONELINECOMPACT'):
                row = box.row()
                split = row.split(percentage=0.25)
                col = split.column()
                col.label('Sub-sequences:')
                col = split.column()
                for index, subsequence in enumerate(sequence.sequences):
                    if index > 10:
                        #Stops listing sub-sequences if list is too long
                        col.label('...')
                        break
                    col.label(subsequence.name)

#Operator to change scene.quicklistsort method
class VSEQFQuickListSortBy(bpy.types.Operator):
    bl_idname = "vseqf.quicklist_sortby"
    bl_label = "VSEQF Quick List Sort By"
    method = bpy.props.StringProperty()
    def execute(self, context):
        scene = context.scene
        scene.quicklistsort = self.method
        return {'FINISHED'}

#Operator to select a sequence, or multiple sequences
class VSEQFQuickListSelect(bpy.types.Operator):
    bl_idname = "vseqf.quicklist_select"
    bl_label = "VSEQF Quick List Select Sequence"
    sequence = bpy.props.StringProperty()
    def execute(self, context):
        sequences = context.sequences
        if (self.sequence == ''):
            bpy.ops.sequencer.select_all(action='TOGGLE')
        else:
            for sequence in sequences:
                if (sequence.name == self.sequence):
                    sequence.select = not sequence.select
        return {'FINISHED'}



#Classes related to continuous update

#Continous modal operator class that handles detecting real-time events
class VSEQFContinuous(bpy.types.Operator):
    bl_idname = "vseqf.continuous"
    bl_label = "VSEQF Continuous Modal Operator"
    
    #Last settings variables for detecting when settings change
    last_scene = bpy.props.StringProperty()
    last_active_sequence = bpy.props.StringProperty()
    last_active_sequence_start = bpy.props.IntProperty()
    last_active_sequence_length = bpy.props.IntProperty()
    last_active_sequence_channel = bpy.props.IntProperty()
    last_cursor_position = bpy.props.IntProperty()
    last_selected_sequences = {}
    last_sequence_names = []
    
    def set_old_variables(self):
        self.last_selected_sequences = {}
        scene = bpy.context.scene
        if bpy.context.selected_sequences != None:
            for selected_sequence in bpy.context.selected_sequences:
                self.last_selected_sequences[selected_sequence.name] = {
                    'start':selected_sequence.frame_final_start,
                    'duration':selected_sequence.frame_final_duration}
        self.last_scene = scene.name
        self.last_cursor_position = scene.frame_current
    
    def modal(self, context, event):
        if not context.scene.quickcontinuousenable:
            return {'CANCELLED'}
        
        scene = context.scene
        
        #do nothing if modal settings are not enabled
        if not scene.quickcontinuousenable:
            return {'FINISHED'}
    
        #Sequence related modal checks
        sequencer = scene.sequence_editor
        if hasattr(sequencer, 'sequences_all'):
            sequences = sequencer.sequences_all
        else:
            sequences = []
        if bpy.context.selected_sequences != None:
            selected_sequences = bpy.context.selected_sequences
        else:
            selected_sequences = []
        
        cut_sequences = []
        resized_sequences = []
        moved_sequences = []
        added_sequences = []
        current_sequences = []
        
        #iterate through selected sequences and select child sequences
        if scene.quickcontinuousselectchildren:
            for sequence in selected_sequences:
                children = find_children(sequence)
                for child in children:
                    if not child.select:
                        child.select = True
        
        current_sequence_names = []
        
        #iterate through sequences and look for changes
        for sequence in sequences:
            current_sequence_names.append(sequence.name)
            if sequence.name in self.last_selected_sequences:
                #sequence was selected, it may have been modified somehow
                old_sequence_info = self.last_selected_sequences[sequence.name]
                if (sequence.frame_final_start != old_sequence_info['start']) and (sequence.frame_final_duration == old_sequence_info['duration']):
                    #Sequence has been moved
                    moved_sequences.append(sequence)
                elif sequence.frame_final_duration != old_sequence_info['duration']:
                    #Sequence has been cut or resized
                    if len(sequences) > len(self.last_sequence_names):
                        #More sequences have been added, so the selected sequences must have been cut
                        cut_sequences.append(sequence)
                    else:
                        #Sequence was resized
                        resized_sequences.append(sequence)
            else:
                #sequence is newly cut or added or renamed
                added_sequences.append(sequence)
        
        #if scene has not changed, check for modal stuff
        if self.last_scene == scene.name:
            
            #Iterate through cut sequences and cut child sequences too, and copy parenting relationships
            for sequence in cut_sequences:
                original_children = find_children(sequence)
                children_to_cut = []
                if len(original_children) == 0:
                    #no child sequences, dont need to do anything
                    continue

                new_sequence_name = renamed(sequence.name)
                new_sequence = False
                for added_sequence in added_sequences:
                    if added_sequence.name == new_sequence_name:
                        new_sequence = added_sequence
                        
                        #remove this sequence from added_sequences
                        added_sequences.remove(added_sequence)
                        break
                
                if not new_sequence:
                    #cut sequence guessed name must already exist, so blender used the lowest number available...
                    #unfortunately, things could get ambiguous here, but lets check a couple things first
                    
                    possible_new_sequences = []
                    sequence_base_name = base_name(sequence.name)
                    for added_sequence in added_sequences:
                        #find added sequences that match the sequence's base name
                        if base_name(added_sequence.name) == sequence_base_name:
                            possible_new_sequences.append(added_sequence)
                    
                    if len(possible_new_sequences) == 1:
                        #only one renamed possibility found, this must be it!
                        new_sequence = possible_new_sequences[0]
                        
                    else:
                        #more than one possible match
                        #still too ambiguous, give up - couldnt determine cut sequence
                        print('Could not find cut sequence for: '+sequence.name)
                        self.report({'WARNING'}, "Could not find cut sequence for: "+sequence.name)
                    
                #iterate through child sequences to cut and copy relationships
                for child in original_children:
                    if child.frame_final_start < scene.frame_current and child.frame_final_end > scene.frame_current:
                        #child sequence needs to be cut and new child sequence parented to new sequence
                        if scene.quickcontinuouschildren:
                            original_selected = bpy.context.selected_sequences
                            original_active = scene.sequence_editor.active_strip
                            
                            bpy.ops.sequencer.select_all(action='DESELECT')
                            child.select = True
                            bpy.ops.sequencer.cut(frame=scene.frame_current)
                            cut_sequences = bpy.context.selected_sequences
                            if new_sequence:
                                #the new cut sequence was found, so copy the new child sequences to it
                                for cut_sequence in cut_sequences:
                                    if cut_sequence != child:
                                        #cut sequence is not the child of the original sequence
                                        add_children(new_sequence, [cut_sequence])

                            bpy.ops.sequencer.select_all(action='DESELECT')
                            for select in original_selected:
                                select.select = True
                            scene.sequence_editor.active_strip = original_active
                        
                    else:
                        if child in cut_sequences:
                            #child was cut already, deal with parenting info
                            if new_sequence:
                                new_child_name = renamed(child.name)
                                for added_sequence in added_sequences:
                                    if new_child_name == added_sequence.name:
                                        add_children(new_sequence, [added_sequence])
                                        
                                        #remove this sequence from added_sequences
                                        added_sequences.remove(added_sequence)
                                        break
                        
                        else:
                            #dont worry about cutting sequence, just copy parent info over
                            if new_sequence:
                                add_children(new_sequence, [child])

            #Iterate through moved sequences and move child sequences too
            if scene.quickcontinuouschildren:
                for sequence in moved_sequences:
                    #move any child sequences along with the parent, if they are not selected as well
                    children = find_children(sequence)
                    offset = sequence.frame_final_start - self.last_selected_sequences[sequence.name]['start']
                    for child in children:
                        if child not in moved_sequences:
                            #only move child sequences if they were not moved
                            child.frame_start = child.frame_start + offset
            
            #iterate through new sequences and auto parent sound sequences to their movie sequence
            for sequence in added_sequences:
                if sequence in selected_sequences:
                    if (sequence.type == 'MOVIE'):
                        soundclip = find_sound_child(sequence, selected_sequences)
                        if (soundclip):
                            print("Parenting "+soundclip.name+" to "+sequence.name)
                            self.report({'INFO'}, "Parenting "+soundclip.name+" to "+sequence.name)
                            add_children(sequence, [soundclip])

            #Iterate through resized sequences resize children, and fix fades if they are on the sequence
            for sequence in resized_sequences:
                old_sequence_info = self.last_selected_sequences[sequence.name]
                start_frame = old_sequence_info['start']
                fade_in = fades(sequence, fade_length=0, type='in', mode='detect', fade_low_point_frame=start_frame)
                end_frame = start_frame + old_sequence_info['duration']
                fade_out = fades(sequence, fade_length=0, type='out', mode='detect', fade_low_point_frame=end_frame)
                if fade_in > 0:
                    fades(sequence, fade_length=fade_in, type='in', mode='set')
                if fade_out > 0:
                    fades(sequence, fade_length=fade_out, type='out', mode='set')
                if scene.quickcontinuouschildren:
                    children = find_children(sequence)
                    for child in children:
                        if child.frame_final_start == start_frame:
                            child.frame_final_start = sequence.frame_final_start
                            child_fade_in = fades(child, fade_length=0, type='in', mode='detect', fade_low_point_frame=start_frame)
                            if child_fade_in > 0:
                                fades(child, fade_length=child_fade_in, type='in', mode='set')

                        if child.frame_final_end == end_frame:
                            child.frame_final_end = sequence.frame_final_end
                            child_fade_out = fades(child, fade_length=0, type='out', mode='detect', fade_low_point_frame=end_frame)
                            if child_fade_out > 0:
                                fades(child, fade_length=child_fade_out, type='out', mode='set')
           
            #Cursor related modal settings
            if (scene.frame_current != self.last_cursor_position) and scene.quickcontinuousfollow:
                #Attempt to move timeline to follow cursor
                #Find the right area
                for area in context.screen.areas:
                    if (area.type == 'SEQUENCE_EDITOR'):
                        for region in area.regions:
                            if (region.type == 'WINDOW') and (area.spaces[0].view_type == 'SEQUENCER'):
                                #Found sequencer area, override context and move viewport view
                                override = {'area': area, 'window': context.window, 'region': region, 'screen': context.screen}
                                offset = scene.frame_current - self.last_cursor_position
                                scale = 1
                                bpy.ops.view2d.pan(override, deltax=offset*scale)
    
        #Save variables for next iteration
        self.last_sequence_names = current_sequence_names
        self.set_old_variables()
        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        if context.scene.quickcontinuousenable:
            self.set_old_variables()
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            return {'CANCELLED'}



#Classes related to QuickTitling

#Property for a QuickTitling preset
class QuickTitle(bpy.types.PropertyGroup):
    name=bpy.props.StringProperty(
        name = "Preset Name",
        default = "Default")
    font=bpy.props.StringProperty(
        name = "Font",
        default = "Bfont",
        description = "QuickTitler Selected Font")
    x=bpy.props.FloatProperty(
        name = "Text X Location",
        default = 0)
    y=bpy.props.FloatProperty(
        name = "Text Y Location",
        default = -3)
    size=bpy.props.FloatProperty(
        name = "Text Size",
        default = 1,
        min = 0)
    extrude=bpy.props.FloatProperty(
        name = "Extrude Amount",
        default = 0,
        min = 0)
    bevel=bpy.props.FloatProperty(
        name = "Bevel Size",
        default = 0,
        min = 0)
    bevelres=bpy.props.IntProperty(
        name = "Bevel Resolution",
        default = 0,
        min = 0)
    shadowsize=bpy.props.FloatProperty(
        name = "Shadow Distance",
        default = 1,
        min = 0)
    shadowamount=bpy.props.FloatProperty(
        name = "Shadow Amount",
        default = 0,
        max = 1,
        min = 0)
    shadowsoft=bpy.props.FloatProperty(
        name = "Shadow Softness",
        default = 1,
        min = 0)
    material=bpy.props.StringProperty(
        name = "Material",
        default = "None")
    text=bpy.props.StringProperty(
        name = "Text",
        default = "None")
    length=bpy.props.IntProperty(
        name = "Scene Length",
        default = 300)

#Panel for QuickTitling settings and operators
class VSEQFQuickTitlingPanel(bpy.types.Panel):
    bl_label = "Quick Titling"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
        
    @classmethod
    def poll(self, context):
        #Check if panel is disabled
        if 'titling' in context.scene.quickenabledpanels:
            return True
        else:
            return False
    
    def draw(self, contex):
        scene = bpy.context.scene
        layout = self.layout

        quicktitle = current_quicktitle()
        
        if not quicktitle:
            #No presets found, must create one before doing anything
            #bpy.ops.vseqf.quicktitler_preset_manipulate(operation="Add") #Doesnt work, have to do it manually...
            row = layout.row()
            row.operator('vseqf.quicktitler_preset_manipulate', text="New Title Preset").operation = "Add"
        else:
            #Load preset
            
            #Preset info and modification
            selected_title = titling_scene_selected()
            outline = layout.box()
            row = outline.row()
            split = row.split(percentage=0.6, align=True)
            split.menu('vseqf.quicktitler_preset_menu', text=quicktitle.name)
            split.operator('vseqf.quicktitler_preset_manipulate', text='Copy').operation = 'Copy'
            split.operator('vseqf.quicktitler_preset_manipulate', text='New').operation = 'Add'
            if not selected_title:
                split.operator('vseqf.quicktitler_preset_manipulate', text='Delete').operation = 'Delete'
            row = outline.row()
            row.prop(quicktitle, 'name')
            
            row = layout.row()
            row.label('')
            row = layout.row()
            #Determine if a titler sequence is selected, if so display an update scene button instead of create button
            try:
                sequence = bpy.context.scene.sequence_editor.active_strip
                if (('QuickTitle: ' in sequence.name) & (sequence.type == 'SCENE')):
                    row.operator('vseqf.quicktitling', text='Update Title Scene').action = 'update'
                    scene = sequence.scene
                else:
                    row.operator('vseqf.quicktitling', text='Create Title Scene').action = 'create'
                    scene = bpy.context.scene
            except:
                row.operator('vseqf.quicktitling', text='Create Title Scene').action = 'create'
                scene = bpy.context.scene
            
            row = layout.row()
            row.prop(quicktitle, 'length')
            row = layout.row()
            row.prop(quicktitle, 'text')
            
            row = layout.row()
            row.label('')
            row = layout.row
            
            #Font section
            outline = layout.box()
            row = outline.row(align=True)
            split = row.split()
            split.label('Text Font:')
            split = row.split(percentage=0.66, align=True)
            split.menu('vseqf.quicktitler_fonts_menu', text=quicktitle.font)
            split.operator('vseqf.quicktitler_load_font', text='+')
            row = outline.row(align=True)
            split = row.split()
            split.label('Material:')
            split = row.split(percentage=0.66, align=True)
            split.menu('vseqf.quicktitler_materials_menu', text=quicktitle.material)
            split.operator('vseqf.quicktitler_new_material', text='+')
            index = bpy.data.materials.find(quicktitle.material)
            if (index >= 0):
                material = bpy.data.materials[index]
                split.prop(material, 'diffuse_color', text='')
            
            #Position and size section
            outline = layout.box()
            row = outline.row()
            split = row.split(align=True)
            split.prop(quicktitle, 'x', text='X Loc:')
            split.prop(quicktitle, 'y', text='Y Loc:')
            row = outline.row()
            row.prop(quicktitle, 'size', text='Size')
            
            #Extrude and bevel section
            outline = layout.box()
            row = outline.row()
            row.prop(quicktitle, 'extrude')
            row = outline.row()
            split = row.split(align=True)
            split.prop(quicktitle, 'bevel')
            split.prop(quicktitle, 'bevelres')
            
            #Shadow section
            outline = layout.box()
            row = outline.row()
            row.prop(quicktitle, 'shadowamount')
            row = outline.row()
            row.prop(quicktitle, 'shadowsize', text='Distance')
            row.prop(quicktitle, 'shadowsoft', text='Soft')

#Operator to manipulate QuickTitler presets - create, copy, or delete
class VSEQFQuickTitlingPresetManipulate(bpy.types.Operator):
    bl_idname = 'vseqf.quicktitler_preset_manipulate'
    bl_label = 'Manipulate Presets'
    bl_description = 'Add, Copy or Delete The First QuickTitling Preset'
    
    #What to do - should be set to 'Delete', 'Copy', or 'Add'
    operation = bpy.props.StringProperty()
    
    def execute(self, context):
        scene = context.scene
        if self.operation == 'Delete':
            if len(scene.quicktitles) > 0:
                scene.quicktitles.remove(0)
        else:
            title = scene.quicktitles.add()
            if self.operation == 'Copy' and len(scene.quicktitles) > 1:
                #copy current title info to new title
                old_title = current_quicktitle()
                copy_title_preset(old_title, title)
                
            scene.quicktitles.move((len(scene.quicktitles) - 1),0)
            
        return {'FINISHED'}

#Menu to list in alphabetical order the QuickTitler Presets
class VSEQFQuickTitlingPresetMenu(bpy.types.Menu):
    bl_idname = 'vseqf.quicktitler_preset_menu'
    bl_label = 'List of saved presets'
    def draw(self, context):
        presets = context.scene.quicktitles
        layout = self.layout
        title_preset_names = []
        
        #iterate through presets and dump the names into a list
        for preset in presets:
            title_preset_names.append(preset.name)
            
        #sort and display preset names list
        title_preset_names.sort()
        selected_title = titling_scene_selected()
        if selected_title:
            layout.operator('vseqf.quicktitler_preset', text="Scene Preset: "+selected_title.quicktitles[0].name)
        for name in title_preset_names:
            layout.operator('vseqf.quicktitler_preset', text=name).preset = name

#Operator to select a QuickTitling preset
class VSEQFQuickTitlingPreset(bpy.types.Operator):
    bl_idname = 'vseqf.quicktitler_preset'
    bl_label = 'Set Preset'
    bl_description = 'Select A QuickTitling Preset'
    
    #Preset name
    preset = bpy.props.StringProperty()
    
    def execute(self,context):
        if not self.preset:
            return {'FINISHED'}
        scene = context.scene
        istitle = False
        
        #Iterate through titler presets to try and find the inputted one
        for index, preset in enumerate(scene.quicktitles):
            if preset.name == self.preset:
                title = index
                istitle = True
                break
        
        if istitle:
            #found title
            scene.quicktitles.move(title, 0)
            titling_scene = titling_scene_selected()
            
            #if a title sequence is selected, copy new selected preset to that scene
            if titling_scene:
                if len(titling_scene.quicktitles) == 0:
                    titling_scene.quicktitles.add()
                copy_title_preset(scene.quicktitles[0], titling_scene.quicktitles[0])
        return {'FINISHED'}

#Operator to load a new font into Blender
class VSEQFQuickTitlingLoadFont(bpy.types.Operator):
    bl_idname = 'vseqf.quicktitler_load_font'
    bl_label = 'Load Font'
    bl_description = 'Load A New Font'
    
    #font file to be loaded
    filepath = bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self,context):
        #When the file browser finishes, this is called
        scene = context.scene
        fonts = bpy.data.fonts
        quicktitle = current_quicktitle()
        
        #Try to load font file
        try:
            font = bpy.data.fonts.load(self.filepath)
            quicktitle.font = font.name
        except:
            print("Not a valid font file: "+self.filepath)
            self.report({'WARNING'}, "Not a valid font file: "+self.filepath)
            
        return {'FINISHED'}
    
    def invoke(self, context, event):
        #Open a file browser
        context.window_manager.fileselect_add(self)
        
        return{'RUNNING_MODAL'}

#Menu for listing and changing QuickTitler fonts
class VSEQFQuickTitlingFontMenu(bpy.types.Menu):
    bl_idname = 'vseqf.quicktitler_fonts_menu'
    bl_label = 'List of loaded fonts'
    def draw(self, context):
        fonts = bpy.data.fonts
        layout = self.layout
        for font in fonts:
            layout.operator('vseqf.quicktitler_change_font', text=font.name).font = font.name

#Operator for changing the QuickTitler font on the current preset
class VSEQFQuickTitlingChangeFont(bpy.types.Operator):
    bl_idname = 'vseqf.quicktitler_change_font'
    bl_label = 'Change Font'
    font = bpy.props.StringProperty()
    def execute(self, context):
        quicktitle = current_quicktitle()
        if quicktitle:
            quicktitle.font = self.font
        return {'FINISHED'}

#Operator for copying or creating a new material to be used in QuickTitler
class VSEQFQuickTitlingNewMaterial(bpy.types.Operator):
    bl_idname = 'vseqf.quicktitler_new_material'
    bl_label = 'New Material'
    bl_description = 'Creates A New Material, Duplicates Current If Available'
    def execute(self, context):
        quicktitle = current_quicktitle()
        if quicktitle:
            index = bpy.data.materials.find(quicktitle.material)
            if (index >= 0):
                material = bpy.data.materials[index].copy()
            else:
                material = bpy.data.materials.new('QuickTitler Material')
            quicktitle.material = material.name
        return {'FINISHED'}

#Menu to list all Materials in blend file, and assign them to QuickTitler presets
class VSEQFQuickTitlingMaterialMenu(bpy.types.Menu):
    bl_idname = 'vseqf.quicktitler_materials_menu'
    bl_label = 'List of loaded materials'
    def draw(self, context):
        materials = bpy.data.materials
        layout = self.layout
        for material in materials:
            layout.operator('vseqf.quicktitler_change_material', text=material.name).material = material.name

#Operator to assign a material name to the material of a QuickTitler preset
class VSEQFQuickTitlingChangeMaterial(bpy.types.Operator):
    bl_idname = 'vseqf.quicktitler_change_material'
    bl_label = 'Change Material'
    material = bpy.props.StringProperty()
    def execute(self, context):
        quicktitle = current_quicktitle()
        if quicktitle:
            quicktitle.material = self.material
        return {'FINISHED'}

#Operator to create QuickTitle scenes
class VSEQFQuickTitling(bpy.types.Operator):
    bl_idname = 'vseqf.quicktitling'
    bl_label = 'VSEQF Quick Titling'
    bl_description = 'Creates or updates a titler scene'
    
    #Should be set to 'create' or 'update'
    action = bpy.props.StringProperty()
    
    def execute(self, context):
        quicktitle = current_quicktitle()
        if not quicktitle:
            print('No QuickTitle Preset Found')
            self.report({'WARNING'}, 'No QuickTitle Preset Found')
            return {'CANCELLED'}
        
        title_scene_length = quicktitle.length
        title_scene_name = "QuickTitle: "+quicktitle.text
        if (self.action == 'create'):
            quicktitle_create(quicktitle)
            
        sequence = bpy.context.scene.sequence_editor.active_strip
        
        quicktitle_update(sequence, quicktitle)

        return {'FINISHED'}



#Classes related to QuickParents

#Defines a parent/child relationship, these are stored in the scene
class ParentRelationship(bpy.types.PropertyGroup):
    parent=bpy.props.StringProperty(name="Parent", default="None")
    child=bpy.props.StringProperty(name="Children", default="None")

#Panel for operators and properties related to QuickParents
class VSEQFQuickParentsPanel(bpy.types.Panel):
    bl_label = "Quick Parents"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
    
    @classmethod
    def poll(self, context):
        #Check if panel is disabled
        if 'parents' not in context.scene.quickenabledpanels:
            return False
        try:
            #attempt to find the active sequence
            sequence = context.scene.sequence_editor.active_strip
            if (sequence):
                return True
            else:
                return False
        except:
            return False
            
    def draw(self, context):
        #Set up variables needed by panel
        scene = bpy.context.scene
        sequence = scene.sequence_editor.active_strip
        selected = bpy.context.selected_sequences
        children = find_children(sequence)
        parent = find_parent(sequence)
        
        layout = self.layout
        
        #First row: selections
        row = layout.row()
        row.operator('vseqf.quickparents', text='Select Children').action = 'selectchildren'
        row.operator('vseqf.quickparents', text='Select Parent').action = 'selectparent'
        
        #Second row: setting
        row = layout.row()
        if (len(selected) <= 1):
            row.enabled = False
        row.operator('vseqf.quickparents', text='Set Active As Parent').action = 'add'
        
        #Third row: clearing
        row = layout.row()
        row.operator('vseqf.quickparents', text='Clear Children').action = 'clearchildren'
        row.operator('vseqf.quickparents', text='Clear Parent').action = 'clearparent'
        
        #List relationships for active sequence
        if parent:
            row = layout.row()
            row.label("Parent: "+parent.name)
        if (len(children) > 0):
            row = layout.row()
            row.label("Children: "+children[0].name)
            index = 1
            while index < len(children):
                row = layout.row()
                row.label(children[index].name)
                index = index + 1

#Pop-up menu for QuickParents
class VSEQFQuickParentsMenu(bpy.types.Menu):
    bl_idname = "vseqf.quickparents_menu"
    bl_label = "Quick Parents"
    
    def draw(self, context):
        scene = bpy.context.scene
        sequence = scene.sequence_editor.active_strip
        layout = self.layout
        
        if sequence:
            #Active sequence set
            
            selected = bpy.context.selected_sequences
            children = find_children(sequence)
            parent = find_parent(sequence)
            
            layout.operator('vseqf.quickparents', text='Select Children').action = 'selectchildren'
            layout.operator('vseqf.quickparents', text='Select Parent').action = 'selectparent'
            if len(selected) > 1:
                #more than one sequence is selected, so children can be set
                layout.operator('vseqf.quickparents', text='Set Active As Parent').action = 'add'
                
            layout.operator('vseqf.quickparents', text='Clear Children').action = 'clearchildren'
            layout.operator('vseqf.quickparents', text='Clear Parent').action = 'clearparent'
            
            if parent:
                #Parent sequence is found, display it
                layout.separator()
                layout.label("     Parent: ")
                layout.label(parent.name)
                layout.separator()
                
            if len(children) > 0:
                #At least one child sequence is found, display them
                layout.separator()
                layout.label("     Children:")
                index = 0
                while index < len(children):
                    layout.label(children[index].name)
                    index = index + 1
                layout.separator()
                
        else:
            layout.label('No Sequence Selected')

#Operator for changing parenting relationships
class VSEQFQuickParents(bpy.types.Operator):
    bl_idname = 'vseqf.quickparents'
    bl_label = 'VSEQF Quick Parents'
    bl_description = 'Sets Or Removes Strip Parents'
    
    #Defines what the operator will attempt to do
    #Can be set to: 'add', 'selectchildren', 'selectparent', 'clearparent', 'clearchildren'
    action = bpy.props.StringProperty()
    
    def execute(self, context):
        clean_relationships()
        selected = bpy.context.selected_sequences
        active = bpy.context.scene.sequence_editor.active_strip
        
        if (self.action == 'add') and (len(selected) > 1):
            add_children(active, selected)
        else:
            for sequence in selected:
                if self.action == 'selectchildren':
                    select_children(sequence)
                if self.action == 'selectparent':
                    select_parent(sequence)
                if self.action == 'clearparent':
                    clear_parent(sequence)
                if self.action == 'clearchildren':
                    clear_children(sequence)
        return {'FINISHED'}



#Classes related to QuickSnaps

#Pop-up menu for QuickSnaps
class VSEQFQuickSnapsMenu(bpy.types.Menu):
    bl_idname = "vseqf.quicksnaps_menu"
    bl_label = "Quick Snaps"
    
    def draw(self, context):
        layout = self.layout
        layout.operator('vseqf.quicksnaps', text='Cursor To Nearest Second').type = 'cursor_to_seconds'
        scene = bpy.context.scene
        
        try:
            #Display only if active sequence is set
            sequence = scene.sequence_editor.active_strip
            if (sequence):
                layout.operator('vseqf.quicksnaps', text='Cursor To Beginning Of Sequence').type = 'cursor_to_beginning'
                layout.operator('vseqf.quicksnaps', text='Cursor To End Of Sequence').type = 'cursor_to_end'
                layout.separator()
                layout.operator('vseqf.quicksnaps', text='Selected To Cursor').type = 'selected_to_cursor'
                layout.operator('vseqf.quicksnaps', text='Sequence Beginning To Cursor').type = 'begin_to_cursor'
                layout.operator('vseqf.quicksnaps', text='Sequence End To Cursor').type = 'end_to_cursor'
                layout.operator('vseqf.quicksnaps', text='Sequence To Previous Sequence').type = 'sequence_to_previous'
                layout.operator('vseqf.quicksnaps', text='Sequence To Next Sequence').type = 'sequence_to_next'
        
        except:
            pass

#Operator for snapping cursor and sequences
class VSEQFQuickSnaps(bpy.types.Operator):
    bl_idname = 'vseqf.quicksnaps'
    bl_label = 'VSEQF Quick Snaps'
    bl_description = 'Snaps selected sequences'
    
    #Snapping operation to perform
    type = bpy.props.StringProperty()
    
    def execute(self, context):
        #Set up variables needed for operator
        selected = bpy.context.selected_sequences
        scene = bpy.context.scene
        active = bpy.context.scene.sequence_editor.active_strip
        frame = scene.frame_current
        
        #Cursor snaps
        if self.type == 'cursor_to_seconds':
            fps = scene.render.fps / scene.render.fps_base
            scene.frame_current = round(round(scene.frame_current / fps) * fps)
        
        if self.type == 'cursor_to_beginning':
            scene.frame_current = active.frame_final_start
        
        if self.type == 'cursor_to_end':
            scene.frame_current = active.frame_final_end
        
        if self.type == 'selected_to_cursor':
            bpy.ops.sequencer.snap(frame=frame)
        
        #Sequence snaps
        if self.type == 'begin_to_cursor':
            for sequence in selected:
                offset = sequence.frame_final_start - sequence.frame_start
                sequence.frame_start = (frame - offset)
        
        if self.type == 'end_to_cursor':
            for sequence in selected:
                offset = sequence.frame_final_start - sequence.frame_start
                sequence.frame_start = (frame - offset - sequence.frame_final_duration)
        
        if self.type == 'sequence_to_previous':
            previous = find_close_sequence(scene.sequence_editor.sequences, active, 'previous', 'any')
            
            if previous:
                for sequence in selected:
                    offset = sequence.frame_final_start - sequence.frame_start
                    sequence.frame_start = (previous.frame_final_end - offset)
            
            else:
                self.report({'WARNING'}, 'No Previous Sequence Found')
        
        if self.type == 'sequence_to_next':
            next = find_close_sequence(scene.sequence_editor.sequences, active, 'next', 'any')
            
            if (next):
                for sequence in selected:
                    offset = sequence.frame_final_start - sequence.frame_start
                    sequence.frame_start = (next.frame_final_start - offset - sequence.frame_final_duration)
            
            else:
                self.report({'WARNING'}, 'No Next Sequence Found')
        
        return{'FINISHED'}



#Classes related to QuickFades

#Panel for QuickFades operators and properties
class VSEQFQuickFadesPanel(bpy.types.Panel):
    bl_label = "Quick Fades"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
    
    @classmethod
    def poll(self, context):
        #Check if panel is disabled
        if 'fades' not in context.scene.quickenabledpanels:
            return False
        
        try:
            #Check for an active sequence to operate on
            sequence = context.scene.sequence_editor.active_strip
            if (sequence):
                return True
            else:
                return False
                
        except:
            return False
    
    def draw(self, context):
        #Set up basic variables needed by panel
        scene = bpy.context.scene
        active_sequence = scene.sequence_editor.active_strip
        frame = scene.frame_current
        fadein = fades(sequence=active_sequence, fade_length=0, type='in', mode='detect')
        fadeout = fades(sequence=active_sequence, fade_length=0, type='out', mode='detect')
        
        layout = self.layout
        
        #First row, detected fades
        row = layout.row()
        if fadein > 0:
            row.label("Fadein: "+str(round(fadein))+" Frames")
        else:
            row.label("No Fadein Detected")
        if fadeout > 0:
            row.label("Fadeout: "+str(round(fadeout))+" Frames")
        else:
            row.label("No Fadeout Detected")
        
        #Setting fades section
        row = layout.row()
        row.prop(scene, 'fade')
        row = layout.row()
        row.operator('vseqf.quickfades', text='Set Fadein').type = 'in'
        row.operator('vseqf.quickfades', text='Set Fadeout').type = 'out'
        row = layout.row()
        row.operator('vseqf.quickfades_clear', text='Clear Fades')
        row = layout.row()
        row.separator()
        
        #Crossfades section
        row = layout.row()
        row.menu('vseqf.quickfades_transition_menu', text="Transition Type: "+scene.transition)
        row = layout.row()
        row.operator('vseqf.quickfades_cross', text='Crossfade Prev Clip').type = 'previous'
        row.operator('vseqf.quickfades_cross', text='Crossfade Next Clip').type = 'next'
        row = layout.row()
        row.operator('vseqf.quickfades_cross', text='Smart Cross to Prev').type = 'previoussmart'
        row.operator('vseqf.quickfades_cross', text='Smart Cross to Next').type = 'nextsmart'

#Pop-up menu for QuickFade operators
class VSEQFQuickFadesMenu(bpy.types.Menu):
    bl_idname = "vseqf.quickfades_menu"
    bl_label = "Quick Fades"
    
    def draw(self, context):
        scene = bpy.context.scene
        sequence = scene.sequence_editor.active_strip
        
        layout = self.layout
        if sequence:
            #If a sequence is active
            frame = scene.frame_current
            fadein = fades(sequence=sequence, fade_length=0, type='in', mode='detect')
            fadeout = fades(sequence=sequence, fade_length=0, type='out', mode='detect')
            
            #Detected fades section
            if (fadein > 0):
                fadeinlabel = "Fadein: "+str(round(fadein))+" Frames"
            else:
                fadeinlabel = "No Fadein Detected"
            if (fadeout > 0):
                fadeoutlabel = "Fadeout: "+str(round(fadeout))+" Frames"
            else:
                fadeoutlabel = "No Fadeout Detected"
            layout.label(fadeinlabel)
            layout.label(fadeoutlabel)
            
            #Fade length
            layout.prop(scene, 'fade')
            
            #Add fades
            layout.operator('vseqf.quickfades_fade', text='Set Fadein').type = 'in'
            layout.operator('vseqf.quickfades_fade', text='Set Fadeout').type = 'out'
            layout.operator('vseqf.quickfades_clear', text='Clear Fades')
            
            #Add crossfades
            layout.separator()
            layout.menu('vseqf.quickfades_transition_menu', text="Transition Type: "+scene.transition)
            layout.operator('vseqf.quickfades_cross', text='Crossfade Prev Sequence').type = 'previous'
            layout.operator('vseqf.quickfades_cross', text='Crossfade Next Sequence').type = 'next'
            layout.operator('vseqf.quickfades_cross', text='Smart Cross to Prev').type = 'previoussmart'
            layout.operator('vseqf.quickfades_cross', text='Smart Cross to Next').type = 'nextsmart'
        
        else:
            layout.label("No Sequence Selected")

#Operator to add fades to selected sequences
class VSEQFQuickFades(bpy.types.Operator):
    bl_idname = 'vseqf.quickfades'
    bl_label = 'VSEQF Quick Fades Set Fade'
    bl_description = 'Adds or changes fade for selected sequences'
    
    #Should be set to 'in' or 'out'
    type = bpy.props.StringProperty()
    
    def execute(self, context):
        for sequence in bpy.context.selected_sequences:
            #iterate through selected sequences and apply fades to them
            fades(sequence=sequence, fade_length=bpy.context.scene.fade, type=self.type, mode='set')
            
        return{'FINISHED'}

#Operator to clear fades on selected sequences
class VSEQFQuickFadesClear(bpy.types.Operator):
    bl_idname = 'vseqf.quickfades_clear'
    bl_label = 'VSEQF Quick Fades Clear Fades'
    bl_description = 'Clears fade in and out for selected sequences'
    
    def execute(self, context):
        for sequence in bpy.context.selected_sequences:
            #iterate through selected sequences, remove fades, and set opacity to full
            fades(sequence=sequence, fade_length=bpy.context.scene.fade, type='both', mode='clear')
            sequence.blend_alpha = 1
            
        return{'FINISHED'}

#Operator to add crossfades between sequences
class VSEQFQuickFadesCross(bpy.types.Operator):
    bl_idname = 'vseqf.quickfades_cross'
    bl_label = 'VSEQF Quick Fades Add Crossfade'
    bl_description = 'Adds a crossfade between selected sequence and next or previous sequence in timeline'
    
    #Should be set to 'nextsmart', 'previoussmart', 'next', 'previous'
    type = bpy.props.StringProperty()
    
    def execute(self, context):
        sequences = bpy.context.sequences
        
        #store a list of selected sequences since adding a crossfade destroys the selection
        selected_sequences = bpy.context.selected_sequences
        
        for sequence in selected_sequences:
            if sequence.type != 'SOUND' and not hasattr(sequence, 'input_1'):
                #iterate through selected sequences and add crossfades to previous or next sequence
                
                if self.type == 'nextsmart':
                    #Need to find next sequence
                    first_sequence = sequence
                    second_sequence = find_close_sequence(sequences, first_sequence, 'next', mode='all')
                    
                elif self.type == 'previoussmart':
                    #Need to find previous sequence
                    second_sequence = sequence
                    first_sequence = find_close_sequence(sequences, second_sequence, 'prev', mode='all')
                    
                elif self.type == 'next':
                    #Need to find next sequence
                    first_sequence = sequence
                    second_sequence = find_close_sequence(sequences, first_sequence, 'next')
                    
                elif self.type == 'previous':
                    #Need to find previous sequence
                    second_sequence = sequence
                    first_sequence = find_close_sequence(sequences, second_sequence, 'prev')
                    
                if (second_sequence != False) & (first_sequence != False):
                    if 'smart' in self.type:
                        #adjust start and end frames of sequences based on frame_offset_end/start to overlap by amount of crossfade
                        target_fade = bpy.context.scene.fade
                        current_fade = first_sequence.frame_final_end - second_sequence.frame_final_start
                        fade_offset = abs(current_fade - target_fade)
                        first_sequence_offset = round((fade_offset/2)+.1)
                        second_sequence_offset = round((fade_offset/2)-.1)
                        
                        if current_fade < target_fade:
                            #detected overlap is not enough, extend the ends of the sequences to match the target overlap
                            
                            if ((first_sequence.frame_offset_end > first_sequence_offset) & (second_sequence.frame_offset_start > second_sequence_offset)) | ((first_sequence.frame_offset_end == 0) & (first_sequence.frame_offset_start == 0)):
                                #both sequence offsets are larger than both target offsets or neither sequence has offsets
                                first_sequence.frame_final_end = first_sequence.frame_final_end + first_sequence_offset
                                second_sequence.frame_final_start = second_sequence.frame_final_start - second_sequence_offset
                                
                            else:
                                #sequence offsets need to be adjusted individually
                                currentOffset = first_sequence.frame_offset_end + second_sequence.frame_offset_start
                                first_sequence_offset_percent = first_sequence.frame_offset_end / currentOffset
                                second_sequence_offset_percent = second_sequence.frame_offset_start / currentOffset
                                first_sequence.frame_final_end = first_sequence.frame_final_end + (round(first_sequence_offset_percent * fade_offset))
                                second_sequence.frame_final_start = second_sequence.frame_final_start - (round(second_sequence_offset_percent * fade_offset))
                        
                        elif current_fade > target_fade:
                            #detected overlap is larger than target fade, subtract equal amounts from each sequence
                            first_sequence.frame_final_end = first_sequence.frame_final_end - first_sequence_offset
                            second_sequence.frame_final_start = second_sequence.frame_final_start + second_sequence_offset
                            
                    crossfade(first_sequence, second_sequence)
                    
                else:
                    self.report({'WARNING'}, 'No Second Sequence Found')
                
        return{'FINISHED'}

#Menu for transition types
class VSEQFQuickFadesTransitionMenu(bpy.types.Menu):
    bl_idname = 'vseqf.quickfades_transition_menu'
    bl_label = 'List Available Transitions'
    
    def draw(self, context):
        layout = self.layout
        
        layout.operator("vseqf.quickfades_change_transition", text="Crossfade").transition = "CROSS"
        layout.operator("vseqf.quickfades_change_transition", text="Wipe").transition = "WIPE"
        layout.operator("vseqf.quickfades_change_transition", text="Gamma Cross").transition = "GAMMA_CROSS"

#Applies a transition type to the scene transition variable
class VSEQFQuickFadesChangeTransition(bpy.types.Operator):
    bl_idname = 'vseqf.quickfades_change_transition'
    bl_label = 'VSEQF Quick Fades Change Transition'
    
    #Transition type to be applied
    transition = bpy.props.StringProperty()
    
    def execute(self, context):
        bpy.context.scene.transition = self.transition
        return{'FINISHED'}



#Classes related to QuickZooms

#Pop-up menu for sequencer zoom shortcuts
class VSEQFQuickZoomsMenu(bpy.types.Menu):
    bl_idname = "vseqf.quickzooms_menu"
    bl_label = "Quick Zooms"
    
    def draw(self, context):
        scene = bpy.context.scene
        layout = self.layout
        
        layout.operator('vseqf.quickzooms', text='Zoom All').area = 'all'
        if (len(bpy.context.selected_sequences) > 0):
            #Only show if a sequence is selected
            layout.operator('vseqf.quickzooms', text='Zoom Selected').area = 'selected'
            
        layout.operator('vseqf.quickzooms', text='Zoom Cursor').area = 'cursor'
        layout.prop(scene, 'zoomsize', text="Size")
        
        layout.separator()
        layout.operator('vseqf.quickzooms', text='Zoom 2 Seconds').area = '2'
        layout.operator('vseqf.quickzooms', text='Zoom 10 Seconds').area = '10'
        layout.operator('vseqf.quickzooms', text='Zoom 30 Seconds').area = '30'
        layout.operator('vseqf.quickzooms', text='Zoom 1 Minute').area = '60'
        layout.operator('vseqf.quickzooms', text='Zoom 2 Minutes').area = '120'
        layout.operator('vseqf.quickzooms', text='Zoom 5 Minutes').area = '300'
        layout.operator('vseqf.quickzooms', text='Zoom 10 Minutes').area = '600'


class VSEQFQuickZooms(bpy.types.Operator):
    bl_idname = 'vseqf.quickzooms'
    bl_label = 'VSEQF Quick Zooms'
    bl_description = 'Changes zoom level of the sequencer timeline'
    
    #Should be set to 'all', 'selected', cursor', or a positive number of seconds
    area = bpy.props.StringProperty()
    
    def execute(self, context):
        if self.area.isdigit():
            #Zoom value is a number of seconds
            scene = bpy.context.scene
            cursor = scene.frame_current
            
            zoom_custom(cursor, (cursor + (scene.render.fps * int(self.area))))
            
        elif self.area == 'all':
            bpy.ops.sequencer.view_all()
            
        elif self.area == 'selected':
            bpy.ops.sequencer.view_selected()
            
        elif self.area == 'cursor':
            zoom_cursor()
            
        return{'FINISHED'}



#Miscellaneous Classes

#Pop-up menu for Quick Function settings
class VSEQFSettingsMenu(bpy.types.Menu):
    bl_idname = "vseqf.settings_menu"
    bl_label = "Quick Settings"
    
    def draw(self, context):
        layout = self.layout
        scene = bpy.context.scene
        
        layout.prop(scene, 'quickcontinuousenable')
        if scene.quickcontinuousenable:
            layout.separator()
            layout.prop(scene, 'quickcontinuousfollow')
            layout.prop(scene, 'quickcontinuouschildren')
            layout.prop(scene, 'quickcontinuousselectchildren')

        #Enable and disable panels
        layout.separator()
        
        if 'list' in scene.quickenabledpanels:
            enabled = 'Off'
        else:
            enabled = 'On'
        layout.operator('vseqf.settings', text='Toggle QuickList Panel '+enabled).setting = 'list'
        
        if 'titling' in scene.quickenabledpanels:
            enabled = 'Off'
        else:
            enabled = 'On'
        layout.operator('vseqf.settings', text='Toggle QuickTitling Panel '+enabled).setting = 'titling'
        
        if 'parents' in scene.quickenabledpanels:
            enabled = 'Off'
        else:
            enabled = 'On'
        layout.operator('vseqf.settings', text='Toggle QuickParents Panel '+enabled).setting = 'parents'
        
        if 'fades' in scene.quickenabledpanels:
            enabled = 'Off'
        else:
            enabled = 'On'
        layout.operator('vseqf.settings', text='Toggle QuickFades Panel '+enabled).setting = 'fades'

#Operator for toggling VSEQF settings
class VSEQFSettings(bpy.types.Operator):
    bl_idname = 'vseqf.settings'
    bl_label = 'VSEQF Settings'
    bl_description = 'Toggles various settings'
    
    #name of setting to toggle
    setting = bpy.props.StringProperty()
    
    def execute(self, context):
        if self.setting == 'list' or self.setting == 'titling' or self.setting == 'parents' or self.setting == 'fades':
            #Panel was toggled
            panels_toggle(self.setting)
        
        return{'FINISHED'}



#Register properties, operators, menus and shortcuts
def register():
    #Register operators
    bpy.utils.register_module(__name__)
    
    #Add menus
    bpy.types.SEQUENCER_HT_header.append(draw_quickspeed_header)
    bpy.types.SEQUENCER_MT_view.append(draw_quickzoom_menu)
    bpy.types.SEQUENCER_MT_view.prepend(draw_quicksettings_menu)
    bpy.types.SEQUENCER_MT_strip.prepend(draw_quicksnap_menu)
    
    #Enable and disable features properties
    bpy.types.Scene.quickenabledpanels = bpy.props.StringProperty(
        name = "Enabled Quick Panels",
        default = 'list,titling,parents,fades')
                
    bpy.types.Scene.quickcontinuousenable = bpy.props.BoolProperty(
        name = "Enable Continuous Options",
        default = False,
        update = toggle_continuous)
        
    bpy.types.Scene.quickcontinuousfollow = bpy.props.BoolProperty(
        name = "Cursor Following",
        default = False)
        
    bpy.types.Scene.quickcontinuouschildren = bpy.props.BoolProperty(
        name = "Cut/Move Sequence Children",
        default = True)
        
    bpy.types.Scene.quickcontinuousselectchildren = bpy.props.BoolProperty(
        name = "Auto-Select Sequence Children",
        default = False)

    #Group properties
    bpy.types.Scene.parenting = bpy.props.CollectionProperty(type=ParentRelationship)

    bpy.types.Scene.quicktitles = bpy.props.CollectionProperty(type=QuickTitle)

    #Operator properties
    bpy.types.Scene.transition = bpy.props.StringProperty(
        name = "Transition Type",
        default = "CROSS")
        
    bpy.types.Scene.fade = bpy.props.IntProperty(
        name = "Fade Length",
        default = 0,
        min = 0,
        description = "Fade Length In Frames")
        
    bpy.types.Scene.zoomsize = bpy.props.IntProperty(
        name = 'Zoom Amount',
        default = 200,
        min = 1,
        description = "Zoom size in frames",
        update = zoom_cursor)
        
    bpy.types.Scene.quicklistdisplay = bpy.props.EnumProperty(
        name = 'Display Mode',
        default = 'STANDARD',
        items = [('STANDARD', 'Standard', '', 1),('COMPACT', 'Standard Compact', '', 2),('ONELINE', 'One Line', '', 3),('ONELINECOMPACT', 'One Line Compact', '', 4)])

    #Temporary properties
    bpy.types.Scene.step = bpy.props.IntProperty(
        name = "Frame Step",
        default = 0,
        min = 0,
        max = 6)

    bpy.types.Scene.quicklistsort = bpy.props.StringProperty(
        name = "Sort Method",
        default = 'Position')
    
    
    #Register shortcuts
    keymap = bpy.context.window_manager.keyconfigs.addon.keymaps.new(name='Sequencer', space_type='SEQUENCE_EDITOR', region_type='WINDOW')
    keymapitems = keymap.keymap_items
    
    for keymapitem in keymapitems:
        #Iterate through keymaps and delete old shortcuts
        if ((keymapitem.type == 'Z') | (keymapitem.type == 'P') | (keymapitem.type == 'F') | (keymapitem.type == 'S')):
            keymapitems.remove(keymapitem)
    keymapzoom = keymapitems.new('wm.call_menu', 'Z', 'PRESS')
    keymapzoom.properties.name = 'vseqf.quickzooms_menu'
    keymapfade = keymapitems.new('wm.call_menu', 'F', 'PRESS')
    keymapfade.properties.name = 'vseqf.quickfades_menu'
    keymapsnap = keymapitems.new('wm.call_menu', 'S', 'PRESS')
    keymapsnap.properties.name = 'vseqf.quicksnaps_menu'
    keymapparent = keymapitems.new('wm.call_menu', 'P', 'PRESS', ctrl=True)
    keymapparent.properties.name = 'vseqf.quickparents_menu'
    keymapparentselect = keymapitems.new('vseqf.quickparents', 'P', 'PRESS', shift=True)
    keymapparentselect.properties.action = 'selectchildren'

    
    #Register handler and modal operator
    handlers = bpy.app.handlers.frame_change_post
    for handler in handlers:
        if (" frame_step " in str(handler)):
            handlers.remove(handler)
    handlers.append(frame_step)
    handlers = bpy.app.handlers.load_post
    for handler in handlers:
        if (" toggle_continuous " in str(handler)):
            handlers.remove(handler)
    handlers.append(toggle_continuous)


def unregister():
    #Unregister menus
    bpy.types.SEQUENCER_HT_header.remove(draw_quickspeed_header)
    bpy.types.SEQUENCER_MT_view.remove(draw_quickzoom_menu)
    bpy.types.SEQUENCER_MT_view.remove(draw_quicksettings_menu)
    bpy.types.SEQUENCER_MT_strip.remove(draw_quicksnap_menu)
    
    #Unregister temporary properties
    del bpy.types.Scene.step
    del bpy.types.Scene.quicklistsort
    
    #Remove shortcuts
    keymapitems = bpy.context.window_manager.keyconfigs.addon.keymaps['Sequencer'].keymap_items
    for keymapitem in keymapitems:
        if ((keymapitem.type == 'Z') | (keymapitem.type == 'F') | (keymapitem.type == 'S')):
            keymapitems.remove(keymapitem)
            
    #Remove handlers for modal operators
    handlers = bpy.app.handlers.frame_change_post
    for handler in handlers:
        if (" frame_step " in str(handler)):
            handlers.remove(handler)
    handlers = bpy.app.handlers.load_post
    for handler in handlers:
        if (" toggle_continuous " in str(handler)):
            handlers.remove(handler)
            
    #Unregister operators
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
