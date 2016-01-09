# convert_materials_to_lux.py
# 
# Copyright (C) 5-mar-2012, Cycles version by Silvio Falcinelli. Fixes by others. Lux version by Marshall Flynn
#
# special thanks to user blenderartists.org cmomoney
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

bl_info = {
    "name": "Convert Materials to Cycles2",
    "author": "Marshall Flynn, adapted from Cycles version by Silvio Falcinelli & others",
    "version": (1, 2, 0),
    "blender": (2, 73, 0),
    "location": "Properties > Material > Convert to Cycles",
    "description": "Convert non-nodes Blender materials to Cycles",
    "warning": "beta",
    "wiki_url": "http://www.tinkeringconnection.com/wp-content/storage/cycles_converter_doc.pdf",
    "category": "Material"}


import bpy
import math
from math import log
from math import pow
from math import exp
import os, sys
from datetime import datetime
import time
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )


#from luxrender import LuxRenderAddon
import _cycles
print ("Importing modules complete!")
#realpath = os.path.expanduser('c:/temp/blender/sample.jpg')




def FixBadMaps():
    if bpy.ops.object.mode_set.poll():
       bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.uv.select_all(action='SELECT')
   
    #bpy.ops.transform.mirror(constraint_axis=(True, False, False), constraint_orientation='GLOBAL', proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)



def AutoNode(active=False):
    print ("This is the Cycles Material Converter")
    print ("Starting convert here.....")
    bpy.ops.object.mode_set(mode='OBJECT')
    sc = bpy.context.scene
    sc.render.engine = 'BLENDER_RENDER'
    # Clear out BI nodes
    BImats = bpy.data.materials
    for clearmat in BImats:
        clearmat.use_nodes = False
 
 
    map_glass = ''
    if (sc.my_prop == True):
      print ("** Image Map on Glass Disabled")
      map_glass = 'no'
    else:
      print ("** Image Map on Glass Enabled")
      map_glass = 'yes'
 
  
    # unselect all objects
    for item in bpy.context.selectable_objects:   
           item.select = False   
  
    outpath = bpy.data.scenes[0].render.filepath
    if active:
        # this is redundant in new code
        mats = bpy.context.active_object.data.materials
    else:
        #this is what will happen
        things = bpy.data.objects
      
    bi_gloss = 'no'
    bi_emitt = 'no'
    bi_matt = 'yes'
    bi_image = 'no'
    bi_diffuse = 'no'
    bi_trans = 'no'
    bi_glass = 'no'
    bi_alpha = 'no'
    bi_reflect = 'no'
    bi_bump = 'no'
    bi_normal = 'no'
    bi_specular = 'no'
    bi_lucent = 'no'
    bi_mlucent = 'no'
    lux_output = 'no'
    bi_metal = 'no'
    bi_mirror = 'no'
    matSlot = 0
    teximage = ''
    imgalready = 'no'
    use_shader = 0
    shaderX = 900
    shaderY = 300
    object_name = ''
    material_name = ''
    nowmat_is_transp = False
    use_glass_image = 'no'
    mat_depth = 0.0
    roughval = 0
    material_idx = 0
    mirror_added = 0
    metal_type = ''
    light_color = (0.9,0.9,0.9,1)
    diff_color = (0.7,0.7,0.7,1)
    j = 0
    L = 0
    timestring = ''
    cstep = 0
    slotNum = 0
    bumpSlot = 0
    specslot = 0
    normslot = 0
    texalpha = 0
    power = 0
    shadernode = ''
    matspecinty = 0.0
    # End of startup variables
    
    
    tcurr = datetime.today()
    timestring = str(tcurr)
    timestring = timestring[-4:]
    wr = open(outpath + 'CyclesConvert' + timestring + '.log', 'a')
    wr.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    wr.write("New Run....\n")
    wr.write("Blender to Cycles Converter\n")
    wr.write("  Marshall Flynn, 2015\n")
    wr.write("------------------------------------------------\n")
    wr.write("Toggle Map Glass: " + str(map_glass) + "\n")
    # Start iterating objects
    # If object normals are messed up, so will the image maps.  This will not correct normals.
    for nowthing in things:
        if nowthing.type not in {'CAMERA', 'LAMP'}:
            print ("Object Loop -----------------------------------------------")
            
            wr.write(">>>New Object --------------------------------\n")
            #bpy.context.scene.objects.active = bpy.data.objects[str(nowthing.name)]
            # Active object
            actob = bpy.context.active_object
            print ("Object Loop Technical Active Object: " + str(actob))
            print ("Object Loop Current Object: " + str(nowthing.name))
            print ("Object Loop Context Object: " + str(bpy.context.object.name)) # Not right
            wr.write("Current Object is: " + str(nowthing.name)+ "\n")
            #mats = bpy.context.active_object.data.materials
            #for nowmat in nowthing:  #  Material Loop      
            for mats in nowthing.material_slots:
                nowmat = mats.material
                bpy.context.object.active_material_index = material_idx
                print (" ")
                print ("Material Loop Current Object: " + str(nowthing.name))
                print ("New Material ------------------------------------------------")
                print ("Raw Loop material: " + str(nowmat) )
                print ("Active Material Index: " + str(things[nowthing.name].active_material_index))
                sys.stdout.flush()  #Flush annoying retained text
                
                #This maybe where material slots gets screwed up
                #bpy.context.active_object.active_material = bpy.data.materials[str(nowmat.name)]
                wr.write("New Material ----------------------------------------\n")
                wr.write(" Current Material: " + nowmat.name + "\n")
                print ("Next 3 may not match match.......OK")
                print ("  Loop nowmat is " + nowmat.name)
                if bpy.context.object.active_material:
                   print ("  Technical Active Material is: " + str(bpy.context.active_object.active_material))
                   # print ("Technical Active Node Material is: " + str(nowmat.active_node_material))
                   wr.write(" Active Material: " + nowmat.name + "\n")
                   wr.write(" Active Node Material: " + str(nowmat.active_node_material) + "\n")
                   wr.write(" Material Slot: " + str(bpy.context.object.material_slots) + "\n")
                   wr.write(" Active Material Index: " + str(things[nowthing.name].active_material_index) + "\n")
                idtype = 'Material'
                # context_data = bpy.context.active_object.active_material
                context_data = nowmat
                
                # nowmat.use_transparency = False        
                # print ("FEEDBACK: Active Material BI is: " + context_data.name)
                
                
                object_name = nowthing.name
                material_name = nowmat.name
                # Grab the existing material from Blender Internal
                matambient = nowmat.ambient
                matalpha = nowmat.alpha
                matdcolor = nowmat.diffuse_color
                for primary in matdcolor:
                    cstep = cstep + 1
                    if cstep == 1:
                      dcolor_r = primary
                    if cstep == 2:
                      dcolor_g = primary
                    if cstep == 3:
                      dcolor_b = primary
                    if cstep == 4:
                      dcolor_a = primary
                matdiffuseinty = nowmat.diffuse_intensity
                matemitt = nowmat.emit
                matmirrorcol = nowmat.mirror_color
                matRTmirror = nowmat.raytrace_mirror.reflect_factor
                matuseRTmirror = nowmat.raytrace_mirror.use
                matRTtrans = nowmat.raytrace_transparency
                matspeccol = nowmat.specular_color
                matspecinty = nowmat.specular_intensity
                matusetrans = nowmat.use_transparency
                mattranstype = nowmat.transparency_method
                mattransIOR = nowmat.raytrace_transparency.ior
                
                
                
                # Texture Properties
                teximgpath = ''
                texglasspath = ''
                texspecpath = ''
                texbumppath = ''
                texnormpath = ''
                texalphapath = ''
                for tex in nowmat.texture_slots:
                    if tex:
                        print ("Tex Type: " + tex.texture.type)
                        print ("Original texture coordinates: " + str(tex.texture_coords))
                        wr.write(" New Texture Slot ................................. " + "\n")
                        wr.write(" Texture Type: " + str(tex.texture.type) + "\n")
                        wr.write(" Original texture coordinates: " + str(tex.texture_coords) + "\n")
                        #Iterate through textures
                        
                        if tex.texture.type == 'IMAGE':
                            
                            teximage = tex.texture.name
                            print("FEEDBACK:  Found IMAGE shader node " + teximage)
                            print ("FEEDBACK:  Current image slot: " + str(j))
                            wr.write(" Texture Image: " + teximage + "\n")
                            bi_image = 'yes'
                            print ("Check-bi_glass: " + bi_glass)
                            slotNum = j    #we only want to count image slots
                            texreflectfact = tex.reflection_factor
                            texreflectuse = tex.use_map_reflect
                            texmap = tex.mapping
                            texemittuse = tex.use_map_emit
                            texdisplaceuse = tex.use_map_displacement
                            texnormaluse = tex.use_map_normal
                            texnormalfact = tex.normal_factor
                            texdisplaceuse = tex.use_map_displacement
                            texdiffuseuse = tex.use_map_diffuse
                            texdiffusemapcol = tex.use_map_color_diffuse
                            texambientuse = tex.use_map_ambient
                            texambientfact = tex.ambient_factor
                            texalphause = tex.use_map_alpha
                            texspecularuse = tex.use_map_specular
                            texalphafact = tex.alpha_factor
                            texspecularfact = tex.specular_factor
                            texcoords = tex.texture_coords
                            Bsub = teximage[0:4]
                            print ("FEEDBACK:  Credible Texture Image Info: " + str(tex.texture.image))
                            wr.write(" What is this Image Texture Slot: " + str(tex.texture.image) + "\n")
                            
                            teximgrealname = tex.texture.image.name
                            #  There may not be an image in slot - now we check:
                            if tex.texture.image:
                                
                                texpath = tex.texture.image.filepath
                                if texdiffuseuse == True or texdiffusemapcol == True:
                                    bi_diffuse = 'yes'
                                    teximgrealname = tex.texture.image.name
                                    teximgpath = tex.texture.image.filepath
                                
                                if 'D' in teximage and not 'Diffuse' in teximage:
                                    # The 'D' is from an OBJ file import
                                    print ("Here is where we search: " + str(teximage))
                                    print ("we found  a D in here...")
                                    texglasspath = tex.texture.image.filepath
                                    texglassrealname = tex.texture.image.name
                                    bi_glass = 'yes'
                                    nowmat.use_transparency = True
                                    use_glass_image = 'yes'
                                    print ("also Glass Image location: " + texglasspath)
                                    print ("Check-bi_glass: " + bi_glass)
                                    wr.write(" Uses Glass Image Mapping: " + use_glass_image + "\n")
                                    wr.write("   based on this image name: " + teximage + "\n")
                                if texnormaluse == True or texdisplaceuse == True:
                                    # A bump type of image
                                    texbumppath = tex.texture.image.filepath
                                    texbumprealname = tex.texture.image.name
                                    bi_bump = 'yes'
                                    print ("Changed to bump due to slot normaluse: " + bi_bump)
                                    bumpSlot = slotNum
                                if texnormaluse == True:
                                    if texdisplaceuse == False:
                                        # A normal type of image
                                        texnormpath = tex.texture.image.filepath
                                        texnormrealname = tex.texture.image.name
                                        bi_normal = 'yes'
                                        bi_bump = 'no'
                                        normSlot = slotNum
                                        if texnormalfact == 0.0 or texnormalfact == 1.0:
                                            texnormalfact = 0.32
                                        print ("Changed to Normal only due to Displacement = " + str(texdisplaceuse))
                                if Bsub == 'Bump' or Bsub == 'bump':
                                    # If the name is 'Bump', it was an imported OBJ file
                                    texbumppath = tex.texture.image.filepath
                                    texbumprealname = tex.texture.image.name
                                    bi_bump = 'yes'
                                    bi_normal = 'no'
                                    
                                    #overrides normal
                                    print ("Changed to bump due to word Bump: " + bi_bump)
                                    bumpSlot = slotNum
                                
                                if texspecularuse == True:
                                    # A specular type of image
                                    texspecpath = tex.texture.image.filepath
                                    texspecrealname = tex.texture.image.name
                                    bi_specular = 'yes'
                                    specslot = slotNum
                                if texalphause == True:
                                    if texdiffuseuse == False and tex.blend_type == 'MIX':
                                        # A glass type of image
                                        print ("Check-bi_glass [use_alpha]: " + bi_glass)
                                        texglasspath = tex.texture.image.filepath
                                        texglassrealname = tex.texture.image.name
                                        bi_glass = 'yes'
                                        nowmat.use_transparency = True
                                        use_glass_image = 'yes'
                                        print ("also Glass Image location: " + texglasspath)
                                        wr.write(" Uses Glass Image Mapping: " + use_glass_image + "\n")
                                    else:
                                        # A plain alpha type of image
                                        print ("Check-bi_glass [use_alpha]: " + bi_glass)
                                        print ("Most likely a Light Map " )
                                        texalphapath = tex.texture.image.filepath
                                        texalpharealname = tex.texture.image.name
                                        bi_alpha = 'yes'
                                    
                                
                                   
                                wr.write(" TEXTURE SLOT [" + str(j) + "] DETAILS: " + "\n")
                                print ("This material has color image: " + teximage)
                                print ("  The image file name: " + teximgrealname)
                                wr.write(" Image Filename: " + teximgrealname + "\n")
                                print ("  Current File location: " + texpath)
                                wr.write(" Current Image Location: " + texpath + "\n")
                                print ("  Used for diffuse: " + str(texdiffuseuse))
                                wr.write(" For Diffuse: " + str(texdiffuseuse) + "\n")
                                wr.write(" For Diffuse Map: " + str(texdiffusemapcol) + "\n")
                                print ("  Used for normal: " + str(texnormaluse))
                                wr.write(" For Normal: " + str(texnormaluse) + "\n")
                                print ("  Used for displacement: " + str(texdisplaceuse))
                                print ("  Used for specular: " + str(texspecularuse))
                                print ("  Used for alpha: " + str(texalphause))
                                wr.write(" For Displacement: " + str(texdisplaceuse) + "\n")
                                wr.write(" For Alpha: " + str(texalphause) + "\n")
                                wr.write(" For Ambient: " + str(texambientuse) + "\n")
                                wr.write(" For Specular: " + str(texspecularuse) + "\n")
                                print ("  Image mapping: " + str(texmap))
                                wr.write(" Image Mapping: " + str(texmap) + "\n")
                                wr.write(" Image Mirror Value: " + str(texreflectfact) + "\n")
                                wr.write(" Image Ambient Value: " + str(texambientfact) + "\n")
                                wr.write(" Image Normal Value: " + str(texnormalfact) + "\n")
                                wr.write(" Image Alpha Value: " + str(texalphafact) + "\n")
                                print ("  Texture Blend Type: " + str(tex.blend_type))
                                wr.write(" End this Texture ________________________________ " + "\n")
                                j = j + 1
                            else:
                                # No image or pathname
                                print ("Image slot has no actual image")
                                bi_image = 'no'
                                wr.write(" texture Slot has no actual image or path!: " + "\n")
                  
                # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++           
                print ("Material Information -------------------------------")
                wr.write(" Material Data ---------------------------------------- " + "\n")
                print ("Material name: " + nowmat.name)
                print ("Original Material Alpha setting: " + str(nowmat.alpha))
                wr.write("  Original Material Alpha: " + str(matalpha) + "\n")
                print ("Original Diffuse Red setting: " + str(dcolor_r))
                print ("Original Diffuse Green setting: " + str(dcolor_g))
                print ("Original Diffuse Blue setting: " + str(dcolor_b))
                #print ("Original Diffuse Alpha setting: " + str(dcolor_a))
                print ("Original Specular Color: " + str(nowmat.specular_color))
                wr.write("  Original Specular Color: " + str(nowmat.specular_color) + "\n")
                print ("Original Ambient setting: " + str(nowmat.ambient))
                wr.write("  Original Ambient: " + str(nowmat.ambient) + "\n")
                print ("Originally Transparent: " + str(nowmat.use_transparency))
                wr.write("  Originally set as transparent: " + str(matusetrans) + "\n")
                wr.write("  Originally set as Mirror: " + str(matuseRTmirror) + "\n")
                wr.write("  Original Mirror data: " + str(matRTmirror) + "\n")
                print ("Originally Transparent Type: " + str(mattranstype))
                wr.write("  Original transparent type: " + str(mattranstype) + "\n")
                print ("Originally Reflection: " + str(matuseRTmirror))
                print ("Original IOR setting: " + str(mattransIOR))
                wr.write("  Original Trans IOR: " + str(mattransIOR) + "\n")
                wr.write("  Original Specular Intensity: " + str(matspecinty) + "\n")
                print ("Diffuse Image Path: " + str(teximgpath))
                print ("Glass Image Path: " + str(texglasspath))
                print ("Specular Image Path: " + str(texspecpath))
                print ("Bump Image Path: " + str(texbumppath))
                print ("Normal Image Path: " + str(texnormpath))
                print ("Alpha Image Path: " + str(texalphapath))
                wr.write("  Material String Variable is " + str(material_name) + "\n")
                bi_matt = 'yes'
                
                
                if bi_glass == 'yes':
                    print ("Check-bi_glass: " + bi_glass)
                    bi_matt = 'no'
                    if matspecinty == 0.0:
                        nowmat.specular_intensity = 1.0
                    print ("Glass change using OBJ texture slot!")
                    wr.write("  Glass change using OBJ texture slot" + "\n")
                if nowmat.use_transparency:
                    nowmat_is_transp = True
                    if matspecinty > 0.8 and matalpha < 0.4:
                        bi_glass = 'yes'
                        bi_matt = 'no'
                        bi_lucent = 'no'
                        print ("Glass change using original Transparency!")
                        wr.write("  Glass change due to original Transparency - be careful!" + "\n")
                    if matalpha > 0.0 and matalpha < 0.9:
                        bi_glass = 'no'
                        bi_matt = 'no'
                        bi_lucent = 'yes'
                        wr.write("  Original Use_Transparency, but Alpha low - so now Translucent" + "\n")
                    if matalpha >= 0.9 and use_glass_image == 'no':
                        bi_glass = 'no'
                        bi_matt = 'yes'
                        bi_lucent = 'no'
                        bi_mlucent = 'no'
                        wr.write("  Original Use_Transparency, but Alpha high - so now Matte" + "\n")
                    
                    # not always true. OBJ importer has all material transparent
                if nowmat.alpha > 0.0 and nowmat.alpha < 0.4:
                    nowmat_is_transp = True
                    bi_glass = 'yes'
                    bi_gloss = 'no'
                    bi_matt = 'no'
                    print ("Glass change using Alpha!")
                    wr.write("  Glass change due to Alpha low value" + "\n")
                if matuseRTmirror == True and matRTmirror > 0.9:
                    bi_mirror = 'yes'
                    bi_gloss = 'no'
                    bi_matt = 'no'
                    bi_lucent = 'no'
                    bi_mlucent = 'no'
                    print ("Mirror change!")
                    wr.write("  Mirror change due to Raytrace Mirror and reflection" + "\n")
                if matuseRTmirror == True and matRTmirror > 0.1:
                    if matalpha >= 0.4:
                        bi_mirror = 'no'
                        bi_gloss = 'yes'
                        bi_matt = 'no'
                        bi_lucent = 'no'
                        bi_mlucent = 'no'
                        bi_glass = 'no'
                        print ("Gloss change!")
                        wr.write("  Gloss change due to Raytrace Mirror and reflection" + "\n")
                if matRTmirror >= 0.1 and matRTmirror < 0.9:
                    if matalpha > 0.0 and matalpha < 0.4:
                        bi_mirror = 'no'
                        bi_gloss = 'no'
                        bi_matt = 'no'
                        bi_lucent = 'no'
                        bi_mlucent = 'no'
                        bi_glass = 'yes'
                        
                        print ("Glass change!")
                        wr.write("  Glass change due to Raytrace Mirror and Alpha" + "\n")
                if nowmat.specular_color == (1.0,1.0,1.0):
                    #this could definitely be glass
                    bi_glass = 'yes'
                    wr.write("  Possible Glass due to Specular all 1.0" + "\n")
                if nowmat.transparency_method == 'Z_TRANSPARENCY':
                    if nowmat.alpha > 0.0 and nowmat.alpha < 0.4:
                        nowmat_is_transp = True
                        bi_glass = 'yes'
                        bi_lucent = 'no'
                        bi_mlucent = 'no'
                        bi_matt = 'no'
                        print ("Glass change due to Z & Alpha!")
                        wr.write("  Glass change due to Z Transparency & Alpha" + "\n")
                    if nowmat.alpha >= 0.6 and nowmat.alpha < 0.9:
                        if bi_gloss == 'yes':
                            bi_lucent = 'yes'
                            bi_gloss = 'no'
                        else:
                            bi_mlucent = 'yes'
                if nowmat.transparency_method == 'RAYTRACE':
                    if nowmat.alpha > 0.0 and nowmat.alpha < 0.4:
                        nowmat_is_transp = True
                        bi_glass = 'yes'
                        bi_matt = 'no'
                        print ("Glass change due to Z & Alpha!")
                        wr.write("  Glass change due to Z Transparency & Alpha" + "\n")
                    if nowmat.alpha >= 0.6 and nowmat.alpha < 0.9:
                        if bi_gloss == 'yes':
                            bi_lucent = 'yes'
                            bi_gloss = 'no'
                        else:
                            bi_mlucent = 'yes'
                if nowmat.use_transparency == True and nowmat.alpha > 0.99:
                    # Corrects OBJ import anomaly
                    if use_glass_image == 'no':
                       bi_glass = 'no'
                       bi_gloss = 'no'
                       bi_matt = 'yes'
                       print ("Glass remove as OBJ anomaly!")
                       wr.write("  Remove OBJ opaque alpha anomaly " + "\n")
                    
                    
        
        
                
                # Following are Material Overrides
                wr.write("  * GUI Checkbox status [map_glass]: " + map_glass + "\n")
                # Check if glass will contain image map
                if map_glass == 'no':
                    use_glass_image = 'no'
                    wr.write("  Removed Glass Image due to GUI checkbox" + "\n")
                if "Glass" in nowmat.name or "glass" in nowmat.name:
                    if "wood" in nowmat.name or "Wood" in nowmat.name:
                        #do nothing
                        print ("Wood in name")
                    else:
                        bi_glass = 'yes'
                        bi_matt = 'no'
                        bi_gloss = 'no'
                        roughval = 0
                        wr.write("  Converted to Glass due to Material Name Glass" + "\n")
                if "Flame" in nowmat.name or "flame" in nowmat.name:
                    bi_emitt = 'yes'
                    bi_mlucent = 'yes'
                    bi_lucent = 'no'
                    bi_matt = 'no'
                    bi_glass = 'no'
                    mat_depth = 0.9
                    light_color = (0.8,0.8,0.5,1)
                    power = 50
                    wr.write("  Converted to Emitt due to Material Name Flame" + "\n")
                
                if "Bulb" in nowmat.name or "bulb" in nowmat.name:
                    bi_emitt = 'yes'
                    bi_mlucent = 'no'
                    bi_lucent = 'no'
                    bi_matt = 'no'
                    bi_glass = 'yes'
                    mat_depth = 0.9
                    roughval = 0.01
                    light_color = (0.9,0.9,0.8,1)
                    power = 70
                    wr.write("  Converted to Emitt due to Material Name Lightbulb" + "\n")
                
                if "Lightbulb" in nowmat.name or "lightbulb" in nowmat.name:
                    bi_emitt = 'yes'
                    bi_mlucent = 'no'
                    bi_matt = 'no'
                    bi_glass = 'yes'
                    mat_depth = 0.9
                    roughval = 0.01
                    light_color = (0.9,0.9,0.8,1)
                    power = 70
                    wr.write("  Converted to Emitt due to Material Name Lightbulb" + "\n")
                                
                
                if bi_glass == 'no':
                    if "windows" in nowmat.name:
                       bi_glass = 'yes'
                       wr.write("  Converted to Glass due to Material Name Windows" + "\n")
                    if "Windows" in nowmat.name:
                       bi_glass = 'yes'
                       wr.write("  Converted to Glass due to Material Name Windows" + "\n")
                    if "window" in nowmat.name:
                       bi_glass = 'yes'
                       wr.write("  Converted to Glass due to Material Name Window" + "\n")
                    if "Window" in nowmat.name:
                       bi_glass = 'yes'
                       wr.write("  Converted to Glass due to Material Name Window" + "\n")
                if "tear" in nowmat.name or "Tear" in nowmat.name:
                    bi_glass = 'yes'
                    wr.write("  Converted to Glass due to Material Name Tear" + "\n")
                if "cornea" in nowmat.name or "Cornea" in nowmat.name:
                    bi_glass = 'yes'
                    wr.write("  Converted to Glass due to Material Name Cornea" + "\n")
                if "clear" in nowmat.name or "Clear" in nowmat.name:
                    bi_glass = 'yes'
                    wr.write("  Converted to Glass due to Material Name Clear" + "\n")
                if "Mirror" in nowmat.name or "mirror" in nowmat.name:
                    if "wood" in nowmat.name or "Wood" in nowmat.name:
                        #do nothing
                        print ("Wood in name")
                    else:
                        bi_glass = 'no'
                        bi_gloss = 'no'
                        bi_mirror = 'yes'
                        bi_matt = 'no'
                        roughval = 0.0001
                        mirror_added = 1
                        wr.write("  Converted to Mirror due to Material Name Mirror" + "\n")
                
                if "leather" in nowmat.name or "Leather" in nowmat.name:
                    bi_lucent = 'yes'
                    bi_matt = 'no'
                    bi_gloss = 'no'
                    diff_color = (0.4,0.3,0.1,1)
                    texnormalfact = 0.06
                    wr.write("  Converted to Translucent due to Material Name Leather" + "\n")
                if "skin" in nowmat.name or "Skin" in nowmat.name:
                    bi_lucent = 'yes'
                    mat_depth = 0.12
                    texnormalfact = 0.044
                    wr.write("  Converted to Translucent due to Material Name Skin" + "\n")
                
                if "head" in material_name or "Head" in nowmat.name:
                    bi_lucent = 'yes'
                    mat_depth = 0.12
                    texnormalfact = 0.044
                    wr.write("  Converted to Translucent due to Material Name Head" + "\n")
                
                if "torso" in nowmat.name or "Torso" in nowmat.name:
                    bi_lucent = 'yes'
                    mat_depth = 0.12
                    texnormalfact = 0.044
                    wr.write("  Converted to Translucent due to Material Name Torso" + "\n")
                if "Limbs" in nowmat.name or "limbs" in nowmat.name:
                    bi_lucent = 'yes'
                    mat_depth = 0.12
                    texnormalfact = 0.044
                    wr.write("  Converted to Translucent due to Material Name Torso" + "\n")
                if "Arms" in nowmat.name or "arms" in nowmat.name:
                    bi_lucent = 'yes'
                    mat_depth = 0.12
                    texnormalfact = 0.044
                    wr.write("  Converted to Translucent due to Material Name Arms" + "\n")
                if "Legs" in nowmat.name or "legs" in nowmat.name:
                    bi_lucent = 'yes'
                    mat_depth = 0.12
                    texnormalfact = 0.044
                    wr.write("  Converted to Translucent due to Material Name Arms" + "\n")
                if "Face" in nowmat.name or "face" in nowmat.name:
                    bi_lucent = 'yes'
                    mat_depth = 0.12
                    texnormalfact = 0.044
                    wr.write("  Converted to Translucent due to Material Name Face" + "\n")
                
                if "Neck" in nowmat.name or "neck" in nowmat.name:
                    bi_lucent = 'yes'
                    mat_depth = 0.12
                    texnormalfact = 0.044
                    wr.write("  Converted to Translucent due to Material Name Neck" + "\n")
                
                if "Blade" in nowmat.name or "blade" in nowmat.name:
                    bi_metal = 'yes'
                    roughval = 0.033
                    wr.write("  Converted to Metal due to Material Name Blade" + "\n")
                
                if "Gold" in material_name or "gold" in material_name:
                    roughval = 0.07
                    metal_type = 'gold' # has to be small letters
                if "Silver" in material_name or "silver" in material_name:
                    roughval = 0.07
                    metal_type = 'silver' # has to be small letters
                if "Copper" in material_name or "copper" in material_name:
                    roughval = 0.07
                    metal_type = 'copper' # has to be small letters
                if "pewter" in material_name or "Pewter" in material_name:
                    roughval = 0.17
                    metal_type = 'pewter' # has to be small letters
                if "Sword" in nowmat.name or "sword" in nowmat.name:
                    bi_metal = 'yes'
                    roughval = 0.033
                    wr.write("  Converted to Metal due to Material Name Sword" + "\n")
                
                if "metal" in material_name or "Metal" in material_name:
                    bi_metal = 'yes'
                    bi_matt = 'no'
                    roughval = 0.11
                    dcolor_r = 0.43
                    dcolor_g = 0.43
                    dcolor_b = 0.43
                    if "pewter" in material_name or "Pewter" in material_name:
                        roughval = 0.14
                    if "iron" in material_name or "Iron" in material_name:
                        roughval = 0.19
                    if "Gold" in material_name or "gold" in material_name:
                        roughval = 0.07
                        metal_type = 'gold' # has to be small letters
                    if "Silver" in material_name or "silver" in material_name:
                        roughval = 0.07
                        metal_type = 'silver' # has to be small letters
                    if "Copper" in material_name or "copper" in material_name:
                        roughval = 0.07
                        metal_type = 'copper' # has to be small letters
                    wr.write("  This is Material Name used for change: " + str(material_name) + "\n")
                    wr.write("  Converted to Metal due to Material Name Metal" + "\n")
        
                #======================================================================================   
                print ("Material Takeaways ----------------------------")
                wr.write("  Material From Original Scene -----------------" + "\n")
                print ("bi_glass: " + bi_glass)
                wr.write("  bi_glass:" + bi_glass + "\n")
                print ("bi_matt: " + bi_matt)
                wr.write("  bi_matt:" + bi_matt + "\n")
                print ("bi_gloss: " + bi_gloss)
                wr.write("  bi_gloss:" + bi_gloss + "\n")
                print ("bi_reflect: " + bi_reflect)
                wr.write("  bi_reflect:" + bi_reflect + "\n")
                print ("bi_mirror: " + bi_mirror)
                wr.write("  bi_mirror:" + bi_mirror + "\n")
                print ("bi_lucent: " + bi_lucent)
                wr.write("  bi_lucent:" + bi_lucent + "\n")
                wr.write("  bi_mlucent:" + bi_mlucent + "\n")
                print ("bi_metal: " + bi_metal)
                wr.write("  bi_metal:" + bi_metal + "\n")
                if bi_metal == 'yes':
                    wr.write("  Metal Type: " + metal_type + "\n")
                print ("   Metal type: " + metal_type)
                wr.write("  bi_emitt:" + bi_emitt + "\n")
                print ("bi_emitt: " + bi_emitt)
                print ("bi_image: " + bi_image)
                wr.write("  bi_image:" + bi_image + "\n")
                print ("bi_bump: " + bi_bump)
                wr.write("  bi_bump:" + bi_bump + "\n")
                print ("bi_specular: " + bi_specular)
                wr.write("  bi_specular:" + bi_specular + "\n")
                print ("bi_normal: " + bi_normal)
                wr.write("  bi_normal:" + bi_normal + "\n")
                print ("bi_alpha: " + bi_alpha)
                wr.write("  bi_alpha:" + bi_alpha + "\n")
                wr.write("  " + "\n")
                
                #Material component checks
                if bi_matt == 'yes':
                    roughval = 0.30
                    dcolor_a = 1.0
                if metal_type == 'gold':
                    bi_metal = 'yes'
                    bi_matt = 'no'
                    dcolor_r = 0.5
                    dcolor_g = 0.469
                    dcolor_b = 0.112
                if metal_type == 'silver':
                    bi_metal = 'yes'
                    bi_matt = 'no'
                    dcolor_r = 0.7
                    dcolor_g = 0.7
                    dcolor_b = 0.7
                if metal_type == 'copper':
                    bi_metal = 'yes'
                    bi_matt = 'no'
                    dcolor_r = 0.5
                    dcolor_g = 0.4
                    dcolor_b = 0.2
                if metal_type == 'pewter':
                    bi_metal = 'yes'
                    bi_matt = 'no'
                    dcolor_r = 0.3
                    dcolor_g = 0.3
                    dcolor_b = 0.3
                if bi_gloss == 'yes' and roughval == 0.0:
                    roughval = 0.22
                if bi_glass == 'yes':
                    roughval = 0.0
                    dcolor_a = 0.8
                if bi_metal == 'yes':
                    roughval = 0.11
                    dcolor_a = 1.0
                if bi_emitt == 'yes':
                    if power == 0:
                        power = 55
                    
        
                
                # Cycles nodes
                # --------------------------------------------------------------
                shaderX = 550
                shaderY = 325
                L = L + 1
                cycles_output = 'yes'
                sc.render.engine = 'CYCLES'
                nowmat.use_nodes = True
                #all new code for Cycles
                tnodes = nowmat.node_tree
                cnodes = nowmat.node_tree.nodes
                nlinks = tnodes.links
                #start from scratch
                for n in tnodes.nodes:
                    tnodes.nodes.remove(n)
                #create the output node (apparently automatically there)
                outputnode = cnodes.new('ShaderNodeOutputMaterial')
                outputnode.location = (800, 250)
                outputX = 800
                outputY = 250
                #material nodes
                if bi_matt == 'yes' or bi_gloss == 'yes':
                    wr.write("--Making Matt or Glossy shader node  " + "\n")
                    mixnodegloss = cnodes.new('ShaderNodeMixShader')
                    #imagenode.inputs[0].default_value = [dcolor_r, dcolor_g, dcolor_b, dcolor_a]
                    shaderX = outputX - 400
                    shaderY = outputY - 5
                    mixnodegloss.location = (shaderX,shaderY)
                    mixnodegloss.select = True
                    mixnodegloss.inputs[0].default_value = 1  # default to full gloss
                    wr.write("--Making Translucent shader node  " + "\n")
                    lucentnode = cnodes.new('ShaderNodeBsdfTranslucent')
                    if bi_image == 'no' or bi_diffuse == 'no':
                        lucentnode.inputs[0].default_value = diff_color
                    else:
                        # wait for image input
                        print ("Waiting for image node input to translucent....")
                    shaderX -= 180
                    shaderY += 170
                    lucentnode.location = (shaderX,shaderY)
                    nlinks.new(lucentnode.outputs[0],mixnodegloss.inputs[1])
                    glossynode = cnodes.new('ShaderNodeBsdfGlossy')
                    glossynode.inputs[1].default_value = roughval
                    glossynode.distribution = 'GGX'
                    glossynode.inputs[0].default_value = [dcolor_r, dcolor_g, dcolor_b, dcolor_a]
                    # no need for shader X calc
                    shaderY -= 250
                    glossynode.location = (shaderX,shaderY)
                    nlinks.new(glossynode.outputs[0],mixnodegloss.inputs[2])
                    # Check if specular is used
                    if bi_specular == 'yes':
                        # do nothing - wait for spec image
                        print ("Waiting for specular image...")
                    else:
                        nlinks.new(mixnodegloss.outputs[0],outputnode.inputs[0])
                    bi_matt = 'no'
                    # change to gloss, as there is no separate matte or diffuse
                    bi_gloss = 'yes'
                    mainNodeX = shaderX
                    mainNodeY = shaderY
                    shadernode = glossynode
                if bi_lucent == 'yes':
                    mixnodegloss.inputs[0].default_value = 0.42  # move to a translucent increase
                    
                    
                    
                if bi_metal == 'yes':
                    wr.write("--Making Metal shader node  " + "\n")
                    metalnode = cnodes.new('ShaderNodeBsdfAnisotropic')
                    metalnode.inputs[1].default_value = roughval
                    metalnode.inputs[0].default_value = [dcolor_r, dcolor_g, dcolor_b, dcolor_a]
                    shaderX = outputX - 400
                    shaderY = outputY - 5
                    metalnode.location = (shaderX,shaderY)
                    nlinks.new(metalnode.outputs[0],outputnode.inputs[0])
                    shadernode = metalnode
                    mainNodeX = shaderX
                    mainNodeY = shaderY
                    bi_image = 'no'
                if bi_mirror == 'yes':
                    wr.write("--Making Mirror shader node  " + "\n")
                    mirrornode = cnodes.new('ShaderNodeBsdfGlossy')
                    mirrornode.inputs[1].default_value = roughval
                    mirrornode.inputs[0].default_value = [dcolor_r, dcolor_g, dcolor_b, dcolor_a]
                    mirrornode.location = (shaderX,shaderY)
                    nlinks.new(mirrornode.outputs[0],outputnode.inputs[0])
                    shadernode = mirrornode
                    bi_image = 'no'
                if bi_glass == 'yes':
                    wr.write("--Making Glass shader node  " + "\n")
                    glassnode = cnodes.new('ShaderNodeBsdfGlass')
                    glassnode.inputs[1].default_value = roughval
                    glassnode.inputs[0].default_value = [dcolor_r, dcolor_g, dcolor_b, dcolor_a]
                    glassnode.location = (shaderX,shaderY)
                    nlinks.new(glassnode.outputs[0],outputnode.inputs[0])
                    shadernode = glassnode

                # Image Map Node below shader nodes (further left)
                if bi_image == 'yes':
                    wr.write("--Inserting Image texture node  " + "\n")
                    imagenode = cnodes.new('ShaderNodeTexImage')
                    #imagenode.inputs[0].default_value = [dcolor_r, dcolor_g, dcolor_b, dcolor_a]
                    shaderX -= 210
                    shaderY += 200
                    imagenode.location = (shaderX,shaderY)
                    imagenode.select = True
                    # Just load diffuse image
                    print ('Check image: ' + teximgpath)
                    wr.write("Check image: " + teximgpath + "\n")
                    print ('Check glass image: ' + texglasspath)
                    wr.write("Check glass image: " + texglasspath + "\n")
                    if teximgpath != '':
                        print ("Image path formed:" + str(teximgpath))
                        if bi_gloss == 'yes' or bi_matt == 'yes':
                            getimg = bpy.data.images.load(teximgpath)
                            imagenode.image = getimg
                        if bi_lucent == 'yes':
                            getimg = bpy.data.images.load(teximgpath)
                            imagenode.image = getimg
                        if bi_mlucent == 'yes':
                            getimg = bpy.data.images.load(teximgpath)
                            imagenode.image = getimg
                        
                    if texglasspath != '':
                        print ("Image path formed:" + str(texglasspath))
                        if bi_glass == 'yes':
                            getimg = bpy.data.images.load(texglasspath)
                            imagenode.image = getimg
                    else:
                        if bi_glass == 'yes':
                            print ("There is no real glass image......")
                            cnodes.remove(imagenode)
                        if bi_bump != 'yes':
                            getimg = bpy.data.images.load(teximgpath)
                            imagenode.image = getimg
                    
                    if bi_gloss == 'yes':  # This also could be translucent depending on mixer slider
                        # plug into translucent and glossy
                        nlinks.new(imagenode.outputs[0],lucentnode.inputs[0])
                        nlinks.new(imagenode.outputs[0],glossynode.inputs[0])
                    else:
                        if bi_glass != 'yes':
                            nlinks.new(imagenode.outputs[0],shadernode.inputs[0])
                
                    
                if bi_specular == 'yes':
                    wr.write("--Inserting Specular texture node  " + "\n")
                    mixnodespec = cnodes.new('ShaderNodeMixShader')
                    #imagenode.inputs[0].default_value = [dcolor_r, dcolor_g, dcolor_b, dcolor_a]
                    shaderX = outputX - 170
                    shaderY = outputY + 25
                    mixnodespec.location = (shaderX,shaderY)
                    mixnodespec.select = True
                    nlinks.new(mixnodespec.outputs[0],outputnode.inputs[0])
                    bi_image = 'no'
                    specimgnode = cnodes.new('ShaderNodeTexImage')
                    shaderX -= 160
                    shaderY += 260
                    specimgnode.location = (shaderX,shaderY)
                    getimg = bpy.data.images.load(texspecpath)
                    specimgnode.image = getimg
                    nlinks.new(specimgnode.outputs[0],mixnodespec.inputs[0])
                    speccolnode = cnodes.new('ShaderNodeBsdfGlossy')
                    shaderX -= 5
                    shaderY -= 510
                    speccolnode.location = (shaderX,shaderY)
                    speccolnode.inputs[1].default_value = 0.25
                    nlinks.new(speccolnode.outputs[0],mixnodespec.inputs[2])
                    #assumes glossynode exists
                    print ("we assume glossynode mixer exists...")
                    nlinks.new(mixnodegloss.outputs[0],mixnodespec.inputs[1])
                    texspecpath = ''
                if bi_bump == 'yes':
                    wr.write("--Inserting Bump texture node  " + "\n")
                    mathnode = cnodes.new('ShaderNodeMath')
                    mathnode.location = (650,110)
                    mathnode.operation = 'MULTIPLY'
                    mathnode.inputs[1].default_value = 0.15  # tame original bump map
                    nlinks.new(mathnode.outputs[0],outputnode.inputs[2])
                    bwnode = cnodes.new('ShaderNodeRGBToBW')
                    bwnode.location = (520,100)
                    nlinks.new(bwnode.outputs[0],mathnode.inputs[0])
                    bumpnode = cnodes.new('ShaderNodeTexImage')
                    #imagenode.inputs[0].default_value = [dcolor_r, dcolor_g, dcolor_b, dcolor_a]
                    shaderX = 400
                    shaderY = 95
                    bumpnode.location = (shaderX,shaderY)
                    bumpnode.select = True
                    getimg = bpy.data.images.load(texbumppath)
                    bumpnode.image = getimg
                    nlinks.new(bumpnode.outputs[0],bwnode.inputs[0])
                    #bumpval = mathnode.outputs[0].value
                    #wr.write("    Final Bump value:  " + str(bumpval) + "\n")
                    texbumppath = ''
                if bi_normal == 'yes':
                    # This is true normal and not bump (mainly for Cycles)
                    print ("Running Normal node placement....")
                    normalnode = cnodes.new('ShaderNodeNormalMap')
                    shaderX = mainNodeX - 170
                    shaderY = mainNodeY - 120
                    normalnode.location = (shaderX,shaderY)
                    normalnode.inputs[0].default_value = texnormalfact
                    nlinks.new(normalnode.outputs[0],shadernode.inputs[2])
                    normalimgnode = cnodes.new('ShaderNodeTexImage')
                    #imagenode.inputs[0].default_value = [dcolor_r, dcolor_g, dcolor_b, dcolor_a]
                    shaderX -= 200
                    shaderY -= 30
                    normalimgnode.location = (shaderX,shaderY)
                    normalimgnode.select = True
                    getimg = bpy.data.images.load(texnormpath)
                    normalimgnode.image = getimg
                    nlinks.new(normalimgnode.outputs[0],normalnode.inputs[1])
                # If area light from material, we convert here
                if bi_emitt == 'yes':
                    wr.write("--Inserting Area Light emission node  " + "\n")
                    lightnode = cnodes.new('ShaderNodeEmission')
                    #imagenode.inputs[0].default_value = [dcolor_r, dcolor_g, dcolor_b, dcolor_a]
                    shaderX = 600
                    shaderY = 120
                    lightnode.location = (shaderX,shaderY)
                    lightnode.select = True
                    lightnode.inputs[0].default_value = light_color
                    lightnode.inputs[1].default_value = power  #light power
                    nlinks.new(lightnode.outputs[0],outputnode.inputs[0])
                if bi_alpha == 'yes':
                    # do all the alpha work here.....
                    mixnodealpha = cnodes.new('ShaderNodeMixShader')
                    outputnode.select = True
                    outputX += 300
                    shaderX = outputX - 185
                    shaderY = outputY + 5
                    outputnode.location = (outputX, outputY)
                    for ln in outputnode.inputs[0].links:
                        nlinks.remove(ln)
                    mixnodealpha.location = (shaderX, shaderY)
                    nlinks.new(mixnodealpha.outputs[0],outputnode.inputs[0])  # To output
                    if bi_specular == 'yes':
                        nlinks.new(mixnodespec.outputs[0],mixnodealpha.inputs[2])  # specular mix to alpha mix input
                    else:
                        nlinks.new(mixnodegloss.outputs[0],mixnodealpha.inputs[2])  # glossy mix to alpha mix input
                    
                    transpnode = cnodes.new('ShaderNodeBsdfTransparent')
                    shaderX -= 0
                    shaderY -= 290
                    transpnode.location = (shaderX, shaderY)
                    nlinks.new(transpnode.outputs[0],mixnodealpha.inputs[1])
                    nlinks.new(imagenode.outputs[1],mixnodealpha.inputs[0])
                    
                
                
            
                print ('FEEDBACK: End converting this material ' + str(nowmat) )
                wr.write("Finished converting this Material: " + str(nowmat) + "\n")
                print ("=========================================================")
                j = 0
                material_idx = material_idx + 1
                bi_bump = 'no'
                bi_normal = 'no'
                bi_image = 'no'
                bi_glass = 'no'
                bi_gloss = 'no'
                bi_metal = 'no'
                bi_mlucent = 'no'
                bi_lucent = 'no'
                bi_matt = 'no'
                bi_emitt = 'no'
                bi_mirror = 'no'
                bi_specular = 'no'
                metal_type = ''
                cstep = 0
                bumpslot = 0
                slotnum = 0
                imgalready = 'no'
                use_glass_image = 'no'
                light_color = (0,0,0)
                roughval = 0.0
                getimg = ''
                nowmat.use_transparency = False
                
    material_idx = 0
    mirror_added = 0
    bi_emitt = 'no'
    wr.write("=========================================================" + "\n")
# ----------------------------------------------------------------------------
 

class cvrtCycles(bpy.types.Operator):
    bl_idname = "cycles.convert"
    bl_label = "Convert All Materials"
    bl_description = "Convert all materials in the scene from non-nodes to Lux"
    bl_register = True
    bl_undo = True

    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        AutoNode(False)
        return {'FINISHED'}

class mlrefresh_active(bpy.types.Operator):
    bl_idname = "mll.refresh_active"
    bl_label = "Convert All Materials From Active Object"
    bl_description = "Convert all materials from active object from non-nodes to Lux"
    bl_register = True
    bl_undo = True

    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        AutoNode(True)
        return {'FINISHED'}

class mlrestore(bpy.types.Operator):
    bl_idname = "mll.restore"
    bl_label = "Restore"
    bl_description = "Switch Back to non nodes & Blender Internal"
    bl_register = True
    bl_undo = True
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context):
        AutoNodeOff()
        return {'FINISHED'}

from bpy.props import *
sc = bpy.types.Scene
sc.EXTRACT_ALPHA = BoolProperty(attr="EXTRACT_ALPHA", default=False)
sc.EXTRACT_PTEX = BoolProperty(attr="EXTRACT_PTEX", default=False)
sc.EXTRACT_OW = BoolProperty(attr="Overwrite", default=False, description="Extract textures again instead of re-using previous textures")
#my_bool = BoolProperty( name="Enable or Disable", description="A simple bool property",default = True)
sc.my_prop = BoolProperty( name="Prop name", description="Some tooltip", default = False)

class OBJECT_PT_totalscene(bpy.types.Panel):
    bl_label = "Convert Materials to Cycles"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"
    
    def draw(self, context):
        sc = context.scene
        layout = self.layout
        
        row = layout.row()
        #box = row.box()
        row.operator("cycles.convert", text='Convert All Materials to Cycles', icon='MATERIAL')
        #box.operator("mll.refresh_active", text='Convert Active to Lux', icon='MATERIAL')
        row = layout.row()
        # Allow user to skip original model author use of image mapping on glass
        row.prop(sc, "my_prop", text="Disable Maps on Glass")

        
        
        



def register():
    bpy.utils.register_module(__name__)
    pass

def unregister():
    bpy.utils.unregister_module(__name__)
    pass

if __name__ == "__main__":
    register()
