#
# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#
# ***** END GPL LICENCE BLOCK *****
#

"""
bl_info = {
    "name": "Display Align Menu",
    "author": "Multiple Authors, mkbreuer",
    "version": (0, 1, 0),
    "blender": (2, 7, 2),
    "location": "3D View",
    "description": "[BACKSLASH] Different Align Tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "User Display"}
"""

import bpy
from bpy import *



###### -----------#####################################################################################################################
######  Operator  #####################################################################################################################
######  Operator  #####################################################################################################################
###### -----------#####################################################################################################################

#####  Mirror XYZ Global  ############################################################################################
#####  Mirror XYZ Global  ############################################################################################

class MirrorGlobalX(bpy.types.Operator):
    """Mirror over X axis / global"""                 
    bl_idname = "object.mirrorglobalx"          
    bl_label = "mirror selected on X axis"                  
    bl_options = {'REGISTER', 'UNDO'}   
       
    def execute(self, context):
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        bpy.ops.transform.mirror(constraint_axis=(True, False, False), constraint_orientation='GLOBAL', proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
       
        return {'FINISHED'}

bpy.utils.register_class(MirrorGlobalX)    


class MirrorGlobalY(bpy.types.Operator):
    """Mirror over Y axis / global"""                
    bl_idname = "object.mirrorglobaly"         
    bl_label = "mirror selected on Y axis"                 
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        bpy.ops.transform.mirror(constraint_axis=(False, True, False), constraint_orientation='GLOBAL', proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {'FINISHED'}

bpy.utils.register_class(MirrorGlobalY)
    

class MirrorGlobalZ(bpy.types.Operator):
    """Mirror over Z axis / global"""                 
    bl_idname = "object.mirrorglobalz"        
    bl_label = "mirror selected on Z axis"                  
    bl_options = {'REGISTER', 'UNDO'}   
      
    def execute(self, context):
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        bpy.ops.transform.mirror(constraint_axis=(False, False, True), constraint_orientation='GLOBAL', proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        
        return {'FINISHED'}

bpy.utils.register_class(MirrorGlobalZ)         


#####  Mirror XYZ Local  #########################################################################################        
#####  Mirror XYZ Local  #########################################################################################

class MirrorLocalX(bpy.types.Operator):
    """Mirror over X axis / local"""                 
    bl_idname = "object.mirrorlocalx"          
    bl_label = "mirror selected on X axis > local"                  
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(True, False, False), constraint_orientation='LOCAL', proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}
        
bpy.utils.register_class(MirrorLocalX) 


class MirrorLocalY(bpy.types.Operator):
    """Mirror over Y axis / local"""                
    bl_idname = "object.mirrorlocaly"         
    bl_label = "mirror selected on Y axis > local"                 
    bl_options = {'REGISTER', 'UNDO'}   
      
    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(False, True, False), constraint_orientation='LOCAL', proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}
    
bpy.utils.register_class(MirrorLocalY)         


class MirrorLocalZ(bpy.types.Operator):
    """Mirror over Z axis / local"""                 
    bl_idname = "object.mirrorlocalz"        
    bl_label = "mirror selected on Z axis > local"                  
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(False, False, True), constraint_orientation='LOCAL', proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)        
        return {'FINISHED'}
    
bpy.utils.register_class(MirrorLocalZ)     
 
        
######  set Origin  ##################################################################################
######  set Origin  ##################################################################################

class OriginObm(bpy.types.Operator):
    """set origin to selected / stay in objectmode"""                 
    bl_idname = "object.originobm"          
    bl_label = "origin to selected / in objectmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}
    
bpy.utils.register_class(OriginObm) 


class OriginEdm(bpy.types.Operator):
    """set origin to selected / stay in editmode"""                 
    bl_idname = "object.originedm"          
    bl_label = "origin to selected in editmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}

bpy.utils.register_class(OriginEdm) 


class OriginBottom_Obm(bpy.types.Operator):  
    bl_idname = "object.pivotobottom_obm"  
    bl_label = "Origin To Bottom / Obm"  
  
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        o=bpy.context.active_object
        init=0
        for x in o.data.vertices:
             if init==0:
                 a=x.co.z
                 init=1
             elif x.co.z<a:
                 a=x.co.z
                 
        for x in o.data.vertices:
             x.co.z-=a

        o.location.z+=a 
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

bpy.utils.register_class(OriginBottom_Obm)


class OriginBottom_Edm(bpy.types.Operator):  
    bl_idname = "object.pivotobottom_edm"  
    bl_label = "Origin To Bottom / Edm"  
  
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        o=bpy.context.active_object
        init=0
        for x in o.data.vertices:
             if init==0:
                 a=x.co.z
                 init=1
             elif x.co.z<a:
                 a=x.co.z
                 
        for x in o.data.vertices:
             x.co.z-=a

        o.location.z+=a 
        bpy.ops.object.mode_set(mode = 'EDIT')
        return {'FINISHED'}

bpy.utils.register_class(OriginBottom_Edm) 



######  Pivot  ##################################################################################
######  Pivot  ##################################################################################

class pivotBox(bpy.types.Operator):
   """Set pivot point to Bounding Box"""
   bl_label = "Set pivot point to Bounding Box"
   bl_idname = "view3d.pivot_bounding_box"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'
       return {"FINISHED"} 

bpy.utils.register_class(pivotBox) 

 
class pivotCursor(bpy.types.Operator):
   """Set pivot point to 3D Cursor"""
   bl_label = "Set pivot point to 3D Cursor"
   bl_idname = "view3d.pivot_3d_cursor"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'CURSOR'
       return {"FINISHED"} 

bpy.utils.register_class(pivotCursor) 


class pivotMedian(bpy.types.Operator):
    """Set pivot point to Median Point"""
    bl_label = "Set pivot point to Median Point"
    bl_idname = "view3d.pivot_median"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'
        return {"FINISHED"}

bpy.utils.register_class(pivotMedian) 


class pivotActive(bpy.types.Operator):
   """Set pivot point to Active"""
   bl_label = "Set pivot point to Active"
   bl_idname = "view3d.pivot_active"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
       return {"FINISHED"} 

bpy.utils.register_class(pivotActive) 


class pivotIndividual(bpy.types.Operator):
    """Set pivot point to Individual"""
    bl_label = "Set pivot point to Individual Point"
    bl_idname = "view3d.pivot_individual"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'INDIVIDUAL_ORIGINS'
        return {"FINISHED"}
        
bpy.utils.register_class(pivotIndividual) 


######  Transform Orientation  ##################################################################
######  Transform Orientation  ##################################################################

class spaceGlobal(bpy.types.Operator):
    """Transform Orientation Global"""
    bl_idname = "space.global"
    bl_label = "Transform Orientation Global"
    bl_options = {'REGISTER'}

    def execute(self, context):

        bpy.context.space_data.transform_orientation = 'GLOBAL'
        return {'FINISHED'}
    
bpy.utils.register_class(spaceGlobal) 
    

class spaceLOCAL(bpy.types.Operator):
    """Transform Orientation LOCAL"""
    bl_idname = "space.local"
    bl_label = "Transform Orientation LOCAL"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        bpy.context.space_data.transform_orientation = 'LOCAL'
        return {'FINISHED'}

bpy.utils.register_class(spaceLOCAL) 


class spaceNORMAL(bpy.types.Operator):
    """Transform Orientation NORMAL"""
    bl_idname = "space.normal"
    bl_label = "Transform Orientation NORMAL"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        bpy.context.space_data.transform_orientation = 'NORMAL'
        return {'FINISHED'}
    
bpy.utils.register_class(spaceNORMAL) 


class spaceGIMBAL(bpy.types.Operator):
    """Transform Orientation GIMBAL"""
    bl_idname = "space.gimbal"
    bl_label = "Transform Orientation GIMBAL"
    bl_options = {'REGISTER'}

    def execute(self, context):
        bpy.context.space_data.transform_orientation = 'GIMBAL'
        return {'FINISHED'}

bpy.utils.register_class(spaceGIMBAL)   


class spaceVIEW(bpy.types.Operator):
    """Transform Orientation VIEW"""
    bl_idname = "space.view"
    bl_label = "Transform Orientation VIEW"
    bl_options = {'REGISTER'}

    def execute(self, context):
        bpy.context.space_data.transform_orientation = 'VIEW'
        return {'FINISHED'}

bpy.utils.register_class(spaceVIEW)     
  


######  Snap Target  ##################################################################
######  Snap Target  ##################################################################

class snapACTIVE(bpy.types.Operator):
    """Snap Target ACTIVE"""
    bl_idname = "snap.active"
    bl_label = "Snap Target ACTIVE"
    bl_options = {'REGISTER'}

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_target = 'ACTIVE'
        return {'FINISHED'}

bpy.utils.register_class(snapACTIVE) 


class snapMEDIAN(bpy.types.Operator):
    """Snap Target MEDIAN"""
    bl_idname = "snap.median"
    bl_label = "Snap Target MEDIAN"
    bl_options = {'REGISTER'}

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_target = 'MEDIAN'
        return {'FINISHED'}

bpy.utils.register_class(snapMEDIAN) 


class snapCENTER(bpy.types.Operator):
    """Snap Target CENTER"""
    bl_idname = "snap.center"
    bl_label = "Snap Target CENTER"
    bl_options = {'REGISTER'}

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_target = 'CENTER'
        return {'FINISHED'}

bpy.utils.register_class(snapCENTER) 


class snapCLOSEST(bpy.types.Operator):
    """Snap Target CLOSEST"""
    bl_idname = "snap.closest"
    bl_label = "Snap Target CLOSEST"
    bl_options = {'REGISTER'}

    def execute(self, context):
        bpy.context.scene.tool_settings.snap_target = 'CLOSEST'
        return {'FINISHED'}

bpy.utils.register_class(snapCLOSEST) 



######  Snap Element  ##################################################################
######  Snap Element  ##################################################################

class snaepVOLUME(bpy.types.Operator):
    """Snap Element VOLUME"""
    bl_idname = "snape.volume"
    bl_label = "Snap Element VOLUME"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        bpy.context.scene.tool_settings.snap_element = 'VOLUME'
        return {'FINISHED'}

bpy.utils.register_class(snaepVOLUME)  


class snaepFACE(bpy.types.Operator):
    """Snap Element FACE"""
    bl_idname = "snape.face"
    bl_label = "Snap Element FACE"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        bpy.context.scene.tool_settings.snap_element = 'FACE'
        return {'FINISHED'}

bpy.utils.register_class(snaepFACE)  


class snaepEDGE(bpy.types.Operator):
    """Snap Element EDGE"""
    bl_idname = "snape.edge"
    bl_label = "Snap Element EDGE"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        bpy.context.scene.tool_settings.snap_element = 'EDGE'
        return {'FINISHED'}

bpy.utils.register_class(snaepEDGE)    


class snaepVERTEX(bpy.types.Operator):
    """Snap Element VERTEX"""
    bl_idname = "snape.vertex"
    bl_label = "Snap Element VERTEX"
    bl_options = {'REGISTER'}
    
    def execute(self, context):
        bpy.context.scene.tool_settings.snap_element = 'VERTEX'
        return {'FINISHED'} 
    
bpy.utils.register_class(snaepVERTEX)


class snaepINCREMENT(bpy.types.Operator):
    """Snap Element INCREMENT"""
    bl_idname = "snape.increment"
    bl_label = "Snap Element INCREMENT"
    bl_options = {'REGISTER'}

    
    def execute(self, context):
        bpy.context.scene.tool_settings.snap_element = 'INCREMENT'
        return {'FINISHED'}

bpy.utils.register_class(snaepINCREMENT)



#####  Flat Align XYZ  ###############################################################################################
#####  Flat Align XYZ  ###############################################################################################

class alignx(bpy.types.Operator):
    """align selected face > x"""
    bl_label = "align selected face to X axis"
    bl_idname = "mesh.face_align_x"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"} 

bpy.utils.register_class(alignx)


class aligny(bpy.types.Operator):
    """align selected face to Y axis"""
    bl_label = "align y"
    bl_idname = "mesh.face_align_y"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}

bpy.utils.register_class(aligny)


class alignz(bpy.types.Operator):
    """align selected face to Z axis"""
    bl_label = "align z"
    bl_idname = "mesh.face_align_z"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"} 
                      
bpy.utils.register_class(alignz)



#####  Align Direction  ###############################################################################################
#####  Align Direction  ###############################################################################################
#Wazou  

#Align X
class AlignX(bpy.types.Operator):  
    bl_idname = "align.x"  
    bl_label = "Align  X"  
  
    def execute(self, context):

        for vert in bpy.context.object.data.vertices:
            bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'} 
    
#Align Y
class AlignY(bpy.types.Operator):  
    bl_idname = "align.y"  
    bl_label = "Align  Y"  
  
    def execute(self, context):

        for vert in bpy.context.object.data.vertices:
            bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}    

#Align Z
class AlignZ(bpy.types.Operator):  
    bl_idname = "align.z"  
    bl_label = "Align  Z"  
  
    def execute(self, context):

        for vert in bpy.context.object.data.vertices:
            bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
        return {'FINISHED'}

#Align to X - 0
class AlignToX0(bpy.types.Operator):  
    bl_idname = "align.2x0"  
    bl_label = "Align To X-0"  
  
    def execute(self, context):
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        for vert in bpy.context.object.data.vertices:
            if vert.select: 
                vert.co[0] = 0
        bpy.ops.object.editmode_toggle() 
        return {'FINISHED'}     

#Align to Z - 0
class AlignToY0(bpy.types.Operator):  
    bl_idname = "align.2y0"  
    bl_label = "Align To Y-0"  
  
    def execute(self, context):
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        for vert in bpy.context.object.data.vertices:
            if vert.select: 
                vert.co[1] = 0
        bpy.ops.object.editmode_toggle() 
        return {'FINISHED'}      

#Align to Z - 0
class AlignToZ0(bpy.types.Operator):  
    bl_idname = "align.2z0"  
    bl_label = "Align To Z-0"  
  
    def execute(self, context):
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        for vert in bpy.context.object.data.vertices:
            if vert.select: 
                vert.co[2] = 0
        bpy.ops.object.editmode_toggle() 
        return {'FINISHED'}

#Align X Left
class AlignXLeft(bpy.types.Operator):  
    bl_idname = "alignx.left"  
    bl_label = "Align X Left"  
  
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 0
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] < max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')  
        return {'FINISHED'}

#Align X Right
class AlignXRight(bpy.types.Operator):  
    bl_idname = "alignx.right"  
    bl_label = "Align X Right"  
  
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 0
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] > max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')  
        return {'FINISHED'}

#Align Y Back
class AlignYBack(bpy.types.Operator):  
    bl_idname = "aligny.back"  
    bl_label = "Align Y back"  
  
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 1
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] > max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')  
        return {'FINISHED'}

#Align Y Front
class AlignYFront(bpy.types.Operator):  
    bl_idname = "aligny.front"  
    bl_label = "Align Y Front"  
  
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 1
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] < max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')  
        return {'FINISHED'}
#Align Z Top
class AlignZTop(bpy.types.Operator):  
    bl_idname = "alignz.top"  
    bl_label = "Align Z Top"  
  
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 2
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] > max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')  
        return {'FINISHED'}  
    
#Align Z Bottom
class AlignZBottom(bpy.types.Operator):  
    bl_idname = "alignz.bottom"  
    bl_label = "Align Z Bottom"  
  
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode='OBJECT')
        count = 0
        axe = 2
        for vert in bpy.context.object.data.vertices:
            if vert.select:
                if count == 0:
                    max = vert.co[axe]
                    count += 1
                    continue
                count += 1
                if vert.co[axe] < max:
                    max = vert.co[axe]

        bpy.ops.object.mode_set(mode='OBJECT')

        for vert in bpy.context.object.data.vertices:
            if vert.select:
                vert.co[axe] = max
        bpy.ops.object.mode_set(mode='EDIT')  
        return {'FINISHED'}  

  
######------------#####################################################################################################################
######  Sub Menu  #####################################################################################################################
######  Sub Menu  #####################################################################################################################
######------------#####################################################################################################################


#######  Align Direction Setup  #######-------------------------------------------------------  
#######  Align Direction Setup  #######------------------------------------------------------- 
    
class AlignXYZ(bpy.types.Menu):
    bl_idname = "align.xyz_new"
    bl_label = "Align Direction Setup"

    def draw(self, context):
        layout = self.layout
     
        layout.label("Align Direction", icon = "ROTATE")

        layout.operator("alignx.left", text="X Left")
        layout.operator("alignx.right", text="X Right")
        layout.operator("aligny.front", text="Y Front")
        layout.operator("aligny.back", text="Y Back")
        layout.operator("alignz.top", text="Z Top")
        layout.operator("alignz.bottom", text="Z Bottom")   

bpy.utils.register_class(AlignXYZ) 



#######  Menus Proportional  #######-------------------------------------------------------  
#######  Menus Proportional  #######-------------------------------------------------------  

class ProportionalMenu(bpy.types.Menu):
    bl_label = "Proportional Menu"
    bl_idname = "proportionalmenu"
  
    def draw(self, context):
        layout = self.layout
        view = context.space_data
        obj = context.active_object
        toolsettings = context.tool_settings

        layout.prop(toolsettings, "use_proportional_edit_objects", text = "on/off", icon_only=True)
       
        if toolsettings.use_proportional_edit_objects:
            layout.prop(toolsettings, "proportional_edit_falloff", icon_only=True)

        layout.prop(toolsettings, "proportional_edit", icon_only=True)

bpy.utils.register_class(ProportionalMenu) 



#######  Menus Align Transform  #######-------------------------------------------------------  
#######  Menus Align Transform  #######------------------------------------------------------- 

class AlignLocMenu(bpy.types.Menu):
    bl_label = "Location XYZ-Axis"
    bl_idname = "alignlocmenu"
   
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        mesh = context.active_object.data

        layout.operator("object.align_location_x",text="Loc X-Axis")
        layout.operator("object.align_location_y",text="Loc Y-Axis")
        layout.operator("object.align_location_z",text="Loc Z-Axis")

bpy.utils.register_class(AlignLocMenu)  


class AlignRotMenu(bpy.types.Menu):
    bl_label = "Rotation XYZ-Axis"
    bl_idname = "alignrotmenu"
    

    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        mesh = context.active_object.data

        layout.operator("object.align_location_x",text="Loc X-Axis")
        layout.operator("object.align_location_y",text="Loc Y-Axis")
        layout.operator("object.align_location_z",text="Loc Z-Axis")

bpy.utils.register_class(AlignRotMenu)  


class AlignScaleMenu(bpy.types.Menu):
    bl_label = "Scale XYZ-Axis"
    bl_idname = "alignscalemenu"
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        mesh = context.active_object.data

        layout.operator("object.align_location_x",text="Loc X-Axis")
        layout.operator("object.align_location_y",text="Loc Y-Axis")
        layout.operator("object.align_location_z",text="Loc Z-Axis")

bpy.utils.register_class(AlignScaleMenu)   


#######  Menus Multi Select  #######-------------------------------------------------------                  
#######  Menus Multi Select  #######-------------------------------------------------------                  

class VIEW3D_MT_edit_multi(bpy.types.Menu):
    bl_label = "Multi Selection"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        prop = layout.operator("wm.context_set_value", text="Vertex Select", icon='VERTEXSEL')
        prop.value = "(True, False, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Edge Select", icon='EDGESEL')
        prop.value = "(False, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Face Select", icon='FACESEL')
        prop.value = "(False, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"
        
        layout.separator()

        prop = layout.operator("wm.context_set_value", text="Vertex & Edge Select", icon='EDITMODE_HLT')
        prop.value = "(True, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Vertex & Face Select", icon='ORTHO')
        prop.value = "(True, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value", text="Edge & Face Select", icon='SNAP_FACE')
        prop.value = "(False, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"
        layout.separator()

        prop = layout.operator("wm.context_set_value", text="Vertex & Edge & Face Select", icon='SNAP_VOLUME')
        prop.value = "(True, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

bpy.utils.register_class(VIEW3D_MT_edit_multi)  


#######  Menus Origin  #######-------------------------------------------------------                  
#######  Menus Origin  #######-------------------------------------------------------                   

class OriginSetupMenu_obm(bpy.types.Menu):
    bl_label = "Origin Setup Menu"
    bl_idname = "originsetupmenu_obm"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.label("Boundbox Bottom", icon = "LAYER_ACTIVE") 
               
        layout.operator("object.pivotobottom_edm", "to Editmode")
        layout.operator("object.pivotobottom_obm", "to Objectmode")              

        layout.separator()   
                 
        layout.operator("object.origin_set", text="Geometry to Origin").type = 'GEOMETRY_ORIGIN'

        layout.separator()   
        
        layout.label("Origin to...",icon = "LAYER_ACTIVE" )
        
        layout.operator("object.origin_set", text="to Geometry").type = 'ORIGIN_GEOMETRY'
        layout.operator("object.origin_set", text="to 3D Cursor").type = 'ORIGIN_CURSOR'
        layout.operator("object.origin_set", text="to Center of Mass").type = 'ORIGIN_CENTER_OF_MASS'

bpy.utils.register_class(OriginSetupMenu_obm) 


class OriginSetupMenu_edm(bpy.types.Menu):
    bl_label = "Origin Setup Menu"
    bl_idname = "originsetupmenu_edm"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.label("Origin to Selected", icon = "RESTRICT_SELECT_OFF")
            
        layout.operator("object.originedm","to Editmode")
        layout.operator("object.originobm","to Objectmode")
            
        layout.separator() 
                       
        layout.label("Boundbox Bottom", icon = "LAYER_ACTIVE") 
            
        layout.operator("object.pivotobottom_edm", "to Editmode")
        layout.operator("object.pivotobottom_obm", "to Objectmode")               

bpy.utils.register_class(OriginSetupMenu_edm) 


class OriginSetupMenu_all_edm(bpy.types.Menu):
    bl_label = "Origin Setup Menu"
    bl_idname = "originsetupmenu_alledm"

    def draw(self, context):
        layout = self.layout

        layout.label("Set Origin to Selected", icon = "LAYER_ACTIVE")
         
        layout.operator("object.originedm","to Editmode")
        layout.operator("object.originobm","to Objectmode")
            
bpy.utils.register_class(OriginSetupMenu_all_edm) 



#######  Menus Apply / Clear  #######-------------------------------------------------------                  
#######  Menus Apply / Clear  #######-------------------------------------------------------                   

class VIEW3D_ApplyandClear(bpy.types.Menu):
    bl_label = "Apply & Clear Setup"
    bl_idname = "htk_applyclear_transform"

    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        mesh = context.active_object.data        

        layout.label("Apply Transform", icon = "FILE_TICK")

        props = layout.operator("object.transform_apply", text=" Move",icon="RIGHTARROW_THIN")
        props.location= True
        props.rotation= False
        props.scale= False
        
        props = layout.operator("object.transform_apply", text=" Rotation",icon="RIGHTARROW_THIN")
        props.location= False
        props.rotation= True
        props.scale= False
        
        props = layout.operator("object.transform_apply", text=" Scale",icon="RIGHTARROW_THIN")
        props.location= False
        props.rotation= False
        props.scale= True

        layout.separator()

        layout.operator("object.visual_transform_apply", text="Visual Transform")
        layout.operator("object.duplicates_make_real", text="Real Duplicate")
               
        layout.separator()  
        
        layout.label("Clear Transform", icon = "X")
        
        layout.operator("object.location_clear", text=" Move")
        layout.operator("object.rotation_clear", text=" Rotation")
        layout.operator("object.scale_clear", text=" Scale")
        
        layout.separator()
        
        layout.operator("object.location_clear", text="Origin", icon="LAYER_ACTIVE")

bpy.utils.register_class(VIEW3D_ApplyandClear)



class VIEW3D_PoseApplyClear(bpy.types.Menu):
    bl_label = "Apply & Clear:"
    bl_idname = "htk_applyclearpose"

    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Apply Pose", icon="PMARKER")

        layout.operator("pose.armature_apply", text="Pose as Rest Pose")

        layout.operator("pose.visual_transform_apply", text="Visual as Pose")

        layout.separator()

        layout.label(text="Clear Pose", icon="PANEL_CLOSE")

        layout.operator("pose.loc_clear", text="Location")
        layout.operator("pose.rot_clear", text="Rotation")
        layout.operator("pose.scale_clear", text="Scale")
        layout.operator("pose.transforms_clear", text="Clear All Pose")
        
        layout.separator()

        layout.operator("pose.user_transforms_clear", text="Reset unkeyed")
                
bpy.utils.register_class(VIEW3D_PoseApplyClear)



#######  Menus Snap  #######-------------------------------------------------------  
#######  Menus Snap  #######-------------------------------------------------------  

class SnapType(bpy.types.Menu):
    bl_label = "Snap Type"
    bl_idname = "htk_snaptype"
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        mesh = context.active_object.data

        settings = context.tool_settings
        view = context.space_data
        toolsettings = context.tool_settings

        snap_meta = toolsettings.use_snap          
       
        layout.operator("snape.increment", "Increment", icon = "SNAP_INCREMENT")        
        layout.operator("snape.vertex", "Vertex", icon = "SNAP_VERTEX")        
        layout.operator("snape.edge", "Edge", icon = "SNAP_EDGE")        
        layout.operator("snape.face", "Face", icon = "SNAP_FACE")
        layout.operator("snape.volume", "Volume", icon = "SNAP_VOLUME")    


bpy.utils.register_class(SnapType) 



class SnapTarget(bpy.types.Menu):
    bl_label = "Snap Target"
    bl_idname = "htk_snaptarget"
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        mesh = context.active_object.data

        settings = context.tool_settings
        view = context.space_data
        toolsettings = context.tool_settings

        snap_meta = toolsettings.use_snap          
                    
        layout.operator("snap.closest", "Closest")        
        layout.operator("snap.center", "Center")
        layout.operator("snap.median", "Median")
        layout.operator("snap.active", "Active")  

bpy.utils.register_class(SnapTarget) 



class SnapOption(bpy.types.Menu):
    bl_label = "Snap Option"
    bl_idname = "htk_snapoption"
    
    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        mesh = context.active_object.data

        settings = context.tool_settings
        view = context.space_data
        toolsettings = context.tool_settings

        snap_meta = toolsettings.use_snap

        if snap_meta == False:
            layout.operator("wm.context_toggle", text="Snap on/off", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
        else:
            layout.operator("wm.context_toggle", text="Snap on/off", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"      
        
        if obj and obj.mode == 'EDIT':
            layout.prop(toolsettings, "use_mesh_automerge", text="Auto-Merge", icon='AUTOMERGE_ON')

        if obj and obj.mode == 'OBJECT':
            layout.prop(toolsettings, "use_snap_align_rotation", text="Snap Normal", icon="SNAP_NORMAL")

        if obj and obj.mode == 'EDIT':
            layout.prop(toolsettings, "use_snap_self", text="Snap Self", icon="ORTHO")
            layout.prop(toolsettings, "use_snap_project", text="Snap Projection", icon="RETOPO")


bpy.utils.register_class(SnapOption) 



#######  Menus Snap to  #######-------------------------------------------------------                  
#######  Menus Snap to  #######-------------------------------------------------------                  

class SelectiontoMenu(bpy.types.Menu):
    bl_label = "Selection to..."
    bl_idname = "htk_selectionto"
    
    def draw(self, context):

        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

         
        layout.operator("view3d.snap_selected_to_grid", text="Grid")       
        layout.operator("view3d.snap_selected_to_cursor", text="Cursor").use_offset = False
        layout.operator("view3d.snap_selected_to_cursor","Cursor (offset)").use_offset = True

        if obj and obj.mode == 'EDIT':   
            layout.separator()
            
            layout.operator("transform.snap_type", text="Snap Tools")    
            layout.operator("view3d.snap_cursor_to_edge_intersection", text="Cursor to Edge Intersection")
            
bpy.utils.register_class(SelectiontoMenu)


class CursortoMenu(bpy.types.Menu):
    bl_label = "Cursor to..."
    bl_idname = "htk_cursorto"
    
    def draw(self, context):

        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("view3d.snap_cursor_to_grid", text="Grid")
        layout.operator("view3d.snap_cursor_to_center", text="Center")
        layout.operator("view3d.snap_cursor_to_active", text="Active")    
        layout.operator("view3d.snap_cursor_to_selected", text="Selected")
        
        layout.separator()

        if obj and obj.mode == 'EDIT':   
            layout.separator()
            
            layout.operator("transform.snap_type", text="Snap Tools", icon='SNAP_ON')    
            layout.operator("view3d.snap_cursor_to_edge_intersection", text="Cursor to Edge Intersection")
            
bpy.utils.register_class (CursortoMenu)





#######  Menus Pivot  #######-------------------------------------------------------  
#######  Menus Pivot  #######------------------------------------------------------- 

class PivotType(bpy.types.Menu):
    bl_label = "Pivot Type"
    bl_idname = "htk_pivottype"
    
    def draw(self, context):
        layout = self.layout

        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'
         
        layout.operator("view3d.pivot_bounding_box", "Bounding Box", icon="ROTATE")
        layout.operator("view3d.pivot_median", "Median", icon="ROTATECENTER")
        layout.operator("view3d.pivot_3d_cursor", "3D Cursor", icon="CURSOR")
        layout.operator("view3d.pivot_active", "Active", icon="ROTACTIVE")
        layout.operator("view3d.pivot_individual", "Individual", icon="ROTATECOLLECTION")


bpy.utils.register_class(PivotType) 



class PivotOrient(bpy.types.Menu):
    bl_label = "Pivot Orientation"
    bl_idname = "htk_pivotorient"
    
    def draw(self, context):
        layout = self.layout

        settings = context.tool_settings
        layout.operator_context = 'INVOKE_REGION_WIN'      

        layout.operator("space.global", "Global")
        layout.operator("space.local", "Local")        
        layout.operator("space.normal", "Normal")
        layout.operator("space.gimbal", "Gimbal")
        layout.operator("space.view", "View")

bpy.utils.register_class(PivotOrient) 




######------------------################################################################################################################
######  Repeat History  ################################################################################################################
######  Repeat History  ################################################################################################################
######------------------################################################################################################################


######  Align History  ######-------------------------------------------------------                          
######  Align History  ######-------------------------------------------------------                          
 
def draw_align_history_tools(context, layout):
    view = context.space_data 
    settings = context.tool_settings
    obj = context.active_object    
    layout.operator_context = 'INVOKE_REGION_WIN'
            
    layout.menu("htk_pivottype", "Pivot Type", icon = "ROTATE")
    layout.menu("htk_pivotorient", "Pivot Orientation", icon = "MANIPUL")

    layout.separator()

    #layout.menu("htk_snapoption", "Snap", icon = "")  
    layout.menu("htk_snaptype", "Snap Type", icon = "SNAP_INCREMENT")    
    layout.menu("htk_snaptarget", "Snap Target", icon = "SNAP_ON")

    layout.separator()
    
    mesh = context.active_object.data
    toolsettings = context.tool_settings

    snap_meta = toolsettings.use_snap

    if snap_meta == False:
        layout.operator("wm.context_toggle", text="Snap on/off", icon="CHECKBOX_DEHLT").data_path = "tool_settings.use_snap"
    else:
        layout.operator("wm.context_toggle", text="Snap on/off", icon="CHECKBOX_HLT").data_path = "tool_settings.use_snap"      
    
    if obj and obj.mode == 'EDIT':
        layout.prop(toolsettings, "use_mesh_automerge", text="Auto-Merge", icon='AUTOMERGE_ON')

    if obj and obj.mode == 'OBJECT':
        layout.prop(toolsettings, "use_snap_align_rotation", text="Snap Normal", icon="SNAP_NORMAL")

    if obj and obj.mode == 'EDIT':
        layout.prop(toolsettings, "use_snap_self", text="Snap Self", icon="ORTHO")
        layout.prop(toolsettings, "use_snap_project", text="Snap Projection", icon="RETOPO")


      
    layout.separator()
    
    layout.menu("htk_cursorto", icon = "FORCE_FORCE")    
    layout.menu("htk_selectionto", icon = "RESTRICT_SELECT_OFF")    
    
    layout.menu("htk_proportionalmenu", "Proportional Menu", icon = "PROP_ON")
            

def draw_align_history2_tools(context, layout):
    view = context.space_data 
    settings = context.tool_settings
    obj = context.active_object    
    layout.operator_context = 'INVOKE_REGION_WIN'

    layout.label("Align to Pivot", icon="ALIGN")

    layout.operator("mesh.face_align_x", "X-Axis")
    layout.operator("mesh.face_align_y", "Y-Axis")           
    layout.operator("mesh.face_align_z", "Z-Axis")        


def draw_align_history3_tools(context, layout):
    view = context.space_data 
    settings = context.tool_settings
    obj = context.active_object    
    layout.operator_context = 'INVOKE_REGION_WIN'
              
    layout.label("Mirror", icon="ARROW_LEFTRIGHT")
            
    layout.operator("object.mirrorglobalx",text="X-Axis")
    layout.operator("object.mirrorglobaly",text="Y-Axis")
    layout.operator("object.mirrorglobalz",text="Z-Axis") 

    layout.separator()                                  
            
    layout.menu("VIEW3D_MT_mirror", text = "Mirror Interactive")          

    layout.separator() 

    if obj and obj.mode == 'OBJECT':
        layout.operator("object.editmode_toggle", text="Fast Toggle", icon = "EDITMODE_HLT") 

    if obj and obj.mode == 'EDIT':                 
        layout.operator("object.editmode_toggle", text="Fast Toggle", icon = "OBJECT_DATAMODE") 
      
     
######--------------################################################################################################################
######  Align Menu  ################################################################################################################
######  Align Menu  ################################################################################################################
######--------------################################################################################################################
    
class VIEW3D_HTK_Align(bpy.types.Menu):
    bl_label = "Align Menu [BACKSLASH]"
    bl_idname = "htk_align"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        obj = context.active_object
        mesh = context.active_object.data
    
        
####### Object menu ------------------------------------------------        
####### Object menu ------------------------------------------------

        obj = context
        if obj and obj.mode == 'OBJECT':

            #########################################
            draw_align_history_tools(context, layout)
            #########################################
            
            layout.separator() 
                       
            layout.menu("originsetupmenu_obm", icon = "LAYER_ACTIVE")
            
            layout.separator()  
            
            layout.operator("object.distribute_osc",text="Distribute", icon='ALIGN')             
            layout.operator("object.align_tools", text="Advance Align Tool") 
                        
            layout.separator()
        
            layout.operator("object.align_location_all",text="All Location", icon='MAN_TRANS') 
        
            layout.operator("object.align_rotation_all",text="All Rotation", icon='MAN_ROT')
           
            layout.operator("object.align_objects_scale_all",text="All Scale", icon='MAN_SCALE')    

            
            layout.separator()                                  
            
            ##########################################
            draw_align_history3_tools(context, layout)
            ##########################################
            

                        
####### Edit menu ------------------------------------------------        
####### Edit menu ------------------------------------------------

        if obj and obj.mode == 'EDIT_MESH':            
            
            #########################################
            draw_align_history_tools(context, layout)
            #########################################
            
            layout.separator()            
            
            layout.menu("originsetupmenu_edm", icon = "LAYER_ACTIVE")         
            layout.menu("VIEW3D_MT_edit_multi")          
                                    
            layout.separator()                                  
                        
            ##########################################
            draw_align_history2_tools(context, layout)
            ##########################################

            layout.separator()
            
            layout.operator("mesh.vertex_align",text="First to Last", icon="ZOOMOUT")
            layout.operator("mesh.vertex_distribute",text="Distribute Vertices", icon="PARTICLE_POINT")  
                       
            #layout.menu("align.xyz_new", text = "Align Boundbox")            

            layout.separator()                                  
            
            ##########################################
            draw_align_history3_tools(context, layout)
            ##########################################



####### Curve menu ------------------------------------------------        
####### Curve menu ------------------------------------------------
        
        if obj and obj.mode == 'EDIT_CURVE':            
            
            #########################################
            draw_align_history_tools(context, layout)
            #########################################
            
            layout.separator()            
            
            layout.menu("originsetupmenu_edm", icon = "LAYER_ACTIVE") 
                        
            layout.separator()                                  
                        
            ##########################################
            draw_align_history2_tools(context, layout)
            ##########################################
            
            layout.separator()                                  
            
            ##########################################
            draw_align_history3_tools(context, layout)
            ##########################################
 


####### Surface menu ----------------------------------------------
####### Surface menu ----------------------------------------------
        
        if obj and obj.mode == 'EDIT_SURFACE':            
            
            #########################################
            draw_align_history_tools(context, layout)
            #########################################
            
            layout.separator()            
            
            layout.menu("originsetupmenu_edm", icon = "LAYER_ACTIVE") 
                                     
            layout.separator()                                  
                        
            ##########################################
            draw_align_history2_tools(context, layout)
            ##########################################

            layout.separator()                                  
            
            ##########################################
            draw_align_history3_tools(context, layout)
            ##########################################



####### Metaball menu ---------------------------------------------
####### Metaball menu ---------------------------------------------
      
        if obj and obj.mode == 'EDIT_METABALL':            
            
            #########################################
            draw_align_history_tools(context, layout)
            #########################################
            
            layout.separator()            
            
            layout.menu("originsetupmenu_edm", icon = "LAYER_ACTIVE") 
                                   
            layout.separator()                                  
                        
            ##########################################
            draw_align_history2_tools(context, layout)
            ##########################################

            layout.separator()
            
            ##########################################
            draw_align_history3_tools(context, layout)
            ##########################################   



####### Lattice menu ----------------------------------------------
####### Lattice menu ----------------------------------------------
        
        if obj and obj.mode == 'EDIT_LATTICE':
            
            #########################################
            draw_align_history_tools(context, layout)
            #########################################
            
            layout.separator()            
            
            layout.menu("originsetupmenu_edm", icon = "LAYER_ACTIVE")

            layout.separator()             
            
            layout.operator("lattice.flip", text="Flip X-Axis (U)").axis = "U"
            layout.operator("lattice.flip", text="Flip Y-Axis (V)").axis = "V"
            layout.operator("lattice.flip", text="Flip Z-Axis (W)").axis = "W"

            layout.separator()
            
            layout.operator("lattice.make_regular", text="Make Regular (Distribute)")             
                                   
            layout.separator()                                  
                        
            ##########################################
            draw_align_history2_tools(context, layout)
            ##########################################

            layout.separator()
            
            ##########################################
            draw_align_history3_tools(context, layout)
            ##########################################                        



####### Particle ---------------------------------------------          
####### Particle ---------------------------------------------          

        if  context.mode == 'PARTICLE':

            # Brush Menu
            layout.menu("VIEW3D_ParticleBrush", text = "Brushes", icon='BRUSH_DATA') 



####### Weightpaint ---------------------------------------------          
####### Weightpaint ---------------------------------------------          

        ob = context
        if ob.mode == 'PAINT_WEIGHT':

            # Brush Menu
            layout.menu("VIEW3D_VertexBrush", text = "Brush", icon='BRUSH_DATA')



####### Vertexpaint ---------------------------------------------          
####### Vertexpaint ---------------------------------------------          

        elif ob.mode == 'PAINT_VERTEX':

            # Brush Menu
            layout.menu("VIEW3D_VertexBrush", text = "Brush", icon='BRUSH_DATA')
            

            
####### Texturepaint --------------------------------------------- 
####### Texturepaint --------------------------------------------- 

        elif ob.mode == 'PAINT_TEXTURE':

            # Brush Menu
            layout.menu("VIEW3D_TextureBrush", text = "Brush", icon='BRUSH_DATA')            



####### Sculptmode --------------------------------------------- 
####### Sculptmode --------------------------------------------- 

        elif ob.mode == 'SCULPT':

            # Brush Menu
            layout.menu("VIEW3D_SculptBrush", text = "Brushes", icon='BRUSH_DATA')  
                        

####### Armature menu ---------------------------------------------
####### Armature menu ---------------------------------------------                                   
        
        if obj and obj.mode == 'EDIT_ARMATURE': 
            
            #########################################
            draw_align_history_tools(context, layout)
            #########################################
                       
            layout.separator()                         
            
            layout.menu("originsetupmenu_edm", icon = "LAYER_ACTIVE")
            
            layout.separator()                                  
                        
            ##########################################
            draw_align_history2_tools(context, layout)
            ##########################################

            layout.separator()
            
            ##########################################
            draw_align_history3_tools(context, layout)
            ########################################## 



####### Pose mode menu --------------------------------------------
####### Pose mode menu --------------------------------------------
            
        if obj and obj.mode == 'POSE': 
            
            arm = context.active_object.data
                       
            layout.menu("htk_pivotmenu", "Pivot Menu", icon = "ROTATE")
            layout.menu("htk_snapmenu", "Snap Menu", icon = "SNAP_ON")
            layout.menu("htk_snaptomenu", "Snap To Menu", icon = "SNAP_SURFACE")
            
            layout.separator()
                          
            layout.menu("originsetupmenu_edm", icon = "LAYER_ACTIVE")
                        
            layout.separator()                                  
                        
            ##########################################
            draw_align_history2_tools(context, layout)
            ##########################################

            layout.separator()
            
            ##########################################
            draw_align_history3_tools(context, layout)
            ########################################## 
                                    
            

######------------################################################################################################################
######  Registry  ################################################################################################################
######  Registry  ################################################################################################################
######------------################################################################################################################

def abs(val):
    if val > 0:
        return val
    return -val

def register():

    bpy.utils.register_class(VIEW3D_HTK_Align) 
    
    bpy.utils.register_module(__name__)        
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Window')
        kmi = km.keymap_items.new('wm.call_menu', 'BACK_SLASH', 'PRESS')
        kmi.properties.name = "htk_align"


def unregister():
    
    bpy.utils.unregister_module(__name__)
    
    bpy.utils.unregister_class(VIEW3D_HTK_Align)   
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps['Window']
        for kmi in km.keymap_items:
            if kmi.idname == 'wm.call_menu':
                if kmi.properties.name == "":
                    km.keymap_items.remove(kmi)
                    break 


if __name__ == "__main__":
    register() 	

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=VIEW3D_HTK_Align.bl_idname)
         


        



































