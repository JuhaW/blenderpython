import bpy
from bpy import*

######################################################################################################################################################
#######-------------#################
#######  Operators  #################
#######-------------#################
######################################################################################################################################################


#####  Edit  ############################################################################################
#####  Edit  ############################################################################################

class ShrinkApply(bpy.types.Operator):
    bl_idname = "retopo.shrinkapply"
    bl_label = "Apply Shrinkwrap"
    
    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Shrinkwrap")
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class MirrorApply(bpy.types.Operator):
    bl_idname = "retopo.mirrorapply"
    bl_label = "Apply Mirror"
    
    def execute(self, context):
       
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}

class LatticeApply(bpy.types.Operator):
    """apply & delete easy-lattice it from deformed object"""
    bl_idname = "retopo.latticeapply"
    bl_label = "Apply E-Lattice and delete it"
    
    def execute(self, context):       

        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="latticeeasytemp")
        bpy.ops.object.select_pattern(pattern="LatticeEasytTemp", extend=False)
        bpy.ops.object.delete(use_global=False)

        return {'FINISHED'}
    
    
class Wire_All(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.wire_all"
    bl_label = "Wire on All Objects"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        
        for obj in bpy.data.objects:
            if obj.show_wire:
                obj.show_all_edges = False
                obj.show_wire = False            
            else:
                obj.show_all_edges = True
                obj.show_wire = True
                             
        return {'FINISHED'} 


class RetopoBevel(bpy.types.Operator):
    bl_idname = "retopo.bevel"
    bl_label = "ShadeBevel"
    
    def execute(self, context):
       
        bpy.ops.mesh.bevel(offset=0.1, segments=2, profile=1, vertex_only=False)

        return {'FINISHED'}





#####  Material  ###############################################################################################
#####  Material  ###############################################################################################

class deleteMat(bpy.types.Operator):
    """delete material slots"""
    bl_idname = "material.remove"
    bl_label = "Delete all Material"
    bl_options = {'REGISTER', 'UNDO'}

    deleteMat = bpy.props.IntProperty(name="Delete all Material", description="How many times?", default=100, min=1, soft_max=1000, step=1)
    
    def execute(self, context):
        
        for i in range(self.deleteMat):
          
            bpy.ops.object.material_slot_remove()

        return {'FINISHED'}


class MetaObjMaterial(bpy.types.Operator):
    """add a new material and enable color object in options"""
    bl_idname = "meta.newmaterial"
    bl_label = "Add Material"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.view3d.assign_material()
        bpy.context.object.active_material.use_object_color = True
        return {'FINISHED'}

bpy.utils.register_class(MetaObjMaterial) 




# ------------------------------------------------------------------------
#    freeze selection button
# ------------------------------------------------------------------------   

class FreezeObjectsButton(bpy.types.Operator):
    bl_idname = "vfxtoolbox.freeze_selected_objects"
    bl_label = "Freeze Selection"
    bl_description = "Disables the viewport selection of current objects."
   
    def execute(self, context):
        selection = get_AllObjectsInSelection()
        n = len(selection)
        if n > 0:
            get_hideSelectObjects(selection)
            self.report({'INFO'}, "%d Object%s frozen." % (n, "s"[n==1:]))
        else:
            self.report({'INFO'}, 'Nothing selected.')
        return{'FINISHED'} 


# ------------------------------------------------------------------------
#    unfreeze all button
# ------------------------------------------------------------------------ 

class UnfreezeButton(bpy.types.Operator):
    bl_idname = "vfxtoolbox.defreeze_all_objects"
    bl_label = "Unfreeze All"
    bl_description = "Enables viewport selection of all objects in scene."
   
    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        selection = get_AllObjectsInScene()
        n = len(selection)

        if n > 0:
            freezed_array = get_dehideSelectObjects(selection)
            get_highlightObjects(freezed_array)
            self.report({'INFO'}, "%d Object%s released." % (n, "s"[n==1:]))
        else:
            self.report({'INFO'}, 'Nothing selected.')
        
        return{'FINISHED'} 



#Double Threshold 0.001
class DoubleThreshold0001(bpy.types.Operator):
    bl_idname = "double.threshold0001"
    bl_label = "Double Threshold 0001"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    def execute(self, context):
        bpy.context.scene.tool_settings.double_threshold = 0.001
        return {'FINISHED'}

#Double Threshold 0.1
class DoubleThreshold01(bpy.types.Operator):
    bl_idname = "double.threshold01"
    bl_label = "Double Threshold 01"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    def execute(self, context):
        bpy.context.scene.tool_settings.double_threshold = 0.1
        return {'FINISHED'}


            


#######  Mirror Full activ  #######-------------------------------------------------------                  
#######  Mirror Full activ  #######-------------------------------------------------------                  

class FullMIRROR(bpy.types.Operator):
    """Add a x mirror modifier with cage and clipping"""
    bl_idname = "view3d.fullmirror"
    bl_label = "Mirror X"

    def execute(self, context):
    
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.ops.view3d.display_modifiers_cage_on()
        bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}
    
bpy.utils.register_class(FullMIRROR) 

class FullMIRRORY(bpy.types.Operator):
    """Add a y mirror modifier with cage and clipping"""
    bl_idname = "view3d.fullmirrory"
    bl_label = "Mirror Y"

    def execute(self, context):
    
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_x = False
        bpy.context.object.modifiers["Mirror"].use_y = True
        bpy.ops.view3d.display_modifiers_cage_on()
        bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}
    
bpy.utils.register_class(FullMIRRORY) 


class FullMIRRORZ(bpy.types.Operator):
    """Add a z mirror modifier with cage and clipping"""
    bl_idname = "view3d.fullmirrorz"
    bl_label = "Mirror Z"

    def execute(self, context):
    
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_x = False
        bpy.context.object.modifiers["Mirror"].use_z = True        
        bpy.ops.view3d.display_modifiers_cage_on()
        bpy.context.object.modifiers["Mirror"].use_clip = True

        return {'FINISHED'}   


#vismaya 
class Freeze_Selected(bpy.types.Operator):
    """freeze selection"""
    bl_idname = "view3d.freeze_selected"
    bl_label = "Freeze Selected"
    bl_options = {'REGISTER', 'UNDO'}    

    def execute(self, context):
        
        for obj in bpy.context.selected_objects:
    
            bpy.context.scene.objects.active = obj
    
            bpy.context.object.hide_select = True                

        return{'FINISHED'}


class UnFreeze_Selected(bpy.types.Operator):
    """unfreeze selection"""    
    bl_idname = "view3d.unfreeze_selected"
    bl_label = "UnFreeze Selected"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        for obj in bpy.context.selected_objects:
    
             bpy.context.object.hide_select = False
             bpy.context.scene.objects.active = obj        

        return{'FINISHED'} 

    
#######  Origin  #######-------------------------------------------------------                  
#######  Origin  #######------------------------------------------------------- 

class loop7(bpy.types.Operator):
    """set origin to selected / objectmode"""                 
    bl_idname = "object.loops7"          
    bl_label = "origin to selected / in objectmode"                 
    bl_options = {'REGISTER', 'UNDO'}   

    def execute(self, context):

        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}
     

class loop9(bpy.types.Operator):
    """set origin to selected / editmode / tip: change for local rotation"""                 
    bl_idname = "object.loops9"          
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


class OriginBottom_Obm(bpy.types.Operator):
    """only for an object without instance"""        
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


class OriginBottom_Edm(bpy.types.Operator):
    """only for an object without instance"""        
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




#####  Pivot Point  ############################################################################################
#####  Pivot Point  ############################################################################################

class pivotBox(bpy.types.Operator):
   """Set pivot point to Bounding Box"""
   bl_label = "Set pivot point to Bounding Box"
   bl_idname = "view3d.pivot_bounding_box"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'BOUNDING_BOX_CENTER'
       return {"FINISHED"} 

 
class pivotCursor(bpy.types.Operator):
   """Set pivot point to 3D Cursor"""
   bl_label = "Set pivot point to 3D Cursor"
   bl_idname = "view3d.pivot_3d_cursor"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'CURSOR'
       return {"FINISHED"} 


class pivotMedian(bpy.types.Operator):
    """Set pivot point to Median Point"""
    bl_label = "Set pivot point to Median Point"
    bl_idname = "view3d.pivot_median"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'
        return {"FINISHED"}


class pivotActive(bpy.types.Operator):
   """Set pivot point to Active"""
   bl_label = "Set pivot point to Active"
   bl_idname = "view3d.pivot_active"
   bl_options = {'REGISTER', 'UNDO'}
    
   def execute(self, context):
       bpy.context.space_data.pivot_point = 'ACTIVE_ELEMENT'
       return {"FINISHED"} 


class pivotIndividual(bpy.types.Operator):
    """Set pivot point to Individual"""
    bl_label = "Set pivot point to Individual Point"
    bl_idname = "view3d.pivot_individual"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.space_data.pivot_point = 'INDIVIDUAL_ORIGINS'
        return {"FINISHED"}   


class pivotCursor3d(bpy.types.Operator):
    """place the origin between all selected with 3d cursor"""
    bl_label = "Set origin between selected with 3d cursor"
    bl_idname = "view3d.origin_3dcursor"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.space_data.pivot_point = 'CURSOR'
  
        return {"FINISHED"}
    

class pivotCursor3d2(bpy.types.Operator):
    """place the origin of the active to cursor with 3d cursor"""
    bl_label = "place the origin to cursor with 3d cursor"
    bl_idname = "view3d.origin_3dcursor2"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.space_data.pivot_point = 'CURSOR'
          
        return {"FINISHED"}


class pivotCursor3d3(bpy.types.Operator):
    """origin to geometry with median pivot"""
    bl_label = "origin to geometry"
    bl_idname = "view3d.origin_3dcursor3"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        bpy.context.space_data.pivot_point = 'MEDIAN_POINT'
  
        return {"FINISHED"}



#####  Mirror XYZ Local  #########################################################################################        
#####  Mirror XYZ Local  #########################################################################################

class loop4(bpy.types.Operator):
    """mirror over X axis / local"""                 
    bl_idname = "object.loops4"          
    bl_label = "mirror selected on X axis > local"                  
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(True, False, False), constraint_orientation='LOCAL')
       
        return {'FINISHED'}
        

class loop5(bpy.types.Operator):
    """mirror over Y axis / local"""                
    bl_idname = "object.loops5"         
    bl_label = "mirror selected on Y axis > local"                 
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(False, True, False), constraint_orientation='LOCAL')
        
        return {'FINISHED'}        


class loop6(bpy.types.Operator):
    """mirror over Z axis / local"""                 
    bl_idname = "object.loops6"        
    bl_label = "mirror selected on Z axis > local"                  
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):

        bpy.ops.transform.mirror(constraint_axis=(False, False, True), constraint_orientation='LOCAL')
        
        return {'FINISHED'}


#####  Mirror XYZ Global  ############################################################################################
#####  Mirror XYZ Global  ############################################################################################

class loop1(bpy.types.Operator):
    """mirror over X axis / global"""                 
    bl_idname = "object.loops1"          
    bl_label = "mirror selected on X axis"                  
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):
        bpy.ops.transform.mirror(constraint_axis=(True, False, False))
       
        return {'FINISHED'}


class loop2(bpy.types.Operator):
    """mirror over Y axis / global"""                
    bl_idname = "object.loops2"         
    bl_label = "mirror selected on Y axis"                 
    bl_options = {'REGISTER', 'UNDO'}   
        
    def execute(self, context):
        bpy.ops.transform.mirror(constraint_axis=(False, True, False))
        
        return {'FINISHED'}
       

class loop3(bpy.types.Operator):
    """mirror over Z axis / global"""                 
    bl_idname = "object.loops3"        
    bl_label = "mirror selected on Z axis"                  
    bl_options = {'REGISTER', 'UNDO'}  
        
    def execute(self, context):
        bpy.ops.transform.mirror(constraint_axis=(False, False, True))
        
        return {'FINISHED'}
    

        
#####  Pivot Align XYZ  ###############################################################################################
#####  Pivot Align XYZ  ###############################################################################################

class alignxy(bpy.types.Operator):
    """align selected to XY-axis / depend by pivot"""
    bl_label = "align selected face to XY axis"
    bl_idname = "mesh.face_align_xy"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(0, 0, 1), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"} 

class alignxz(bpy.types.Operator):
    """align selected to XZ-axis / depend by pivot"""
    bl_label = "align xz"
    bl_idname = "mesh.face_align_xz"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(0, 1, 0), constraint_axis=(True, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}

class alignyz(bpy.types.Operator):
    """align selected to yz-axis / depend by pivot"""
    bl_label = "align yz"
    bl_idname = "mesh.face_align_yz"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(1, 0, 0), constraint_axis=(False, True, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"} 
    
    
#####  Flat Align XYZ  ###############################################################################################
#####  Flat Align XYZ  ###############################################################################################

class alignx(bpy.types.Operator):
    """align selected to X-axis / depend by pivot"""
    bl_label = "align selected face to X axis"
    bl_idname = "mesh.face_align_x"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"} 

class aligny(bpy.types.Operator):
    """align selected to Y-axis / depend by pivot"""
    bl_label = "align y"
    bl_idname = "mesh.face_align_y"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}

class alignz(bpy.types.Operator):
    """align selected to Z-axis / depend by pivot"""
    bl_label = "align z"
    bl_idname = "mesh.face_align_z"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        return {"FINISHED"}    
    

    
#
class CreateHole(bpy.types.Operator):                  
    """This Operator create a hole on a selection"""                   
    bl_idname = "object.createhole"                     
    bl_label = "Create Hole"   
    bl_options = {'REGISTER', 'UNDO'}     

    @classmethod                                     
    def poll(cls, context):                         
        return context.active_object is not None 

    def execute(self, context):                     
        
        bpy.ops.mesh.extrude_region_move()
        bpy.ops.transform.resize(value=(0.6, 0.6, 0.6))
        bpy.ops.mesh.looptools_circle()
        bpy.ops.mesh.extrude_region_move()
        bpy.ops.transform.resize(value=(0.8, 0.8, 0.8))
        bpy.ops.mesh.delete(type='FACE')
        return {'FINISHED'} 
    

class CurvesTo3D (bpy.types.Operator):
    """Put curves to ground and turn to 3d mode (wiring them) for farthere spread to layout sheet"""
    bl_idname = "object.curv_to_3d"
    bl_label = "Curves to 3d"
    bl_options = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        obj = bpy.context.selected_objects
        if obj[0].type == 'CURVE':
            for o in obj:
                o.data.extrude = 0.0
                o.data.dimensions = '3D'
                #o.matrix_world.translation[2] = 0
        return {'FINISHED'}

class CurvesTo2D (bpy.types.Operator):
    """Curves turn to 2d mode (and thicken 0.03 mm)"""
    bl_idname = "object.curv_to_2d"
    bl_label = "Curves to 2d"
    bl_options = {'REGISTER', 'UNDO'} 
    
    def execute(self, context):
        obj = bpy.context.selected_objects
        if obj[0].type == 'CURVE':
            for o in obj:
                o.data.extrude = 0.0016
                o.data.dimensions = '2D'
                nam = o.data.name
                # Я фанат группы "Сплин", ребята.
                for splin in bpy.data.curves[nam].splines:
                    splin.use_smooth = False
                    for point in splin.bezier_points:
                        point.radius = 1.0
        return {'FINISHED'}
    
    



#Radial Clone from Mifth Tools
import bmesh
import time
import math

from bpy.types import Menu
from bpy.props import *
from bpy.app.handlers import persistent
from bpy.types import Operator, AddonPreferences
from bl_ui.properties_paint_common import (
				UnifiedPaintPanel,
				brush_texture_settings,
				brush_texpaint_common,
				brush_mask_texture_settings,
		)




bpy.mifthTools = dict()

class MFTProperties(bpy.types.PropertyGroup):

	radialClonesAxis = EnumProperty(
		items = (('X', 'X', ''),
			('Y', 'Y', ''),
			('Z', 'Z', '')
			),
		default = 'Z'
	)

	radialClonesAxisType = EnumProperty(
		items = (('Global', 'Global', ''),
			   ('Local', 'Local', '')
			   ),
		default = 'Global'
	)


class MFTRadialClone(bpy.types.Operator):
	bl_idname = "mft.radialclone"
	bl_label = "Radial Clone"
	bl_description = "Radial Clone"
	bl_options = {'REGISTER', 'UNDO'}

	radialClonesAngle = FloatProperty(
		name = "Angle",
		default = 360.0,
		min = -360.0,
		max = 360.0
	)
	clonez = IntProperty(
		name = "Count",
		default = 8,
		min = 2,
		max = 300
	)
	

	def execute(self, context):

		if len(bpy.context.selected_objects) > 0:
			activeObj = bpy.context.scene.objects.active
			selObjects = bpy.context.selected_objects
			mifthTools = bpy.context.scene.mifthTools
			#self.clonez = mifthTools.radialClonesNumber

			activeObjMatrix = activeObj.matrix_world

			for i in range(self.clonez - 1):
				bpy.ops.object.duplicate(linked=True, mode='DUMMY')
				#newObj = bpy.context.selected_objects[0]
				#print(newObj)
				#for obj in bpy.context.selected_objects:
				theAxis = None

				if mifthTools.radialClonesAxis == 'X':
					if mifthTools.radialClonesAxisType == 'Local':
						theAxis = (activeObjMatrix[0][0], activeObjMatrix[1][0], activeObjMatrix[2][0])
					else:
						theAxis = (1, 0, 0)

				elif mifthTools.radialClonesAxis == 'Y':
					if mifthTools.radialClonesAxisType == 'Local':
						theAxis = (activeObjMatrix[0][1], activeObjMatrix[1][1], activeObjMatrix[2][1])
					else:
						theAxis = (0, 1, 0)

				elif mifthTools.radialClonesAxis == 'Z':
					if mifthTools.radialClonesAxisType == 'Local':
						theAxis = (activeObjMatrix[0][2], activeObjMatrix[1][2], activeObjMatrix[2][2])
					else:
						theAxis = (0, 0, 1)
				
				rotateValue = (math.radians(self.radialClonesAngle)/float(self.clonez))
				bpy.ops.transform.rotate(value=rotateValue, axis=theAxis)


			bpy.ops.object.select_all(action='DESELECT')

			for obj in selObjects:
				obj.select = True
			selObjects = None
			bpy.context.scene.objects.active = activeObj
		else:
			self.report({'INFO'}, "Select Objects!")

		return {'FINISHED'}



#####  Brushes  ###############################################################################################
#####  Brushes  ###############################################################################################


class SculptPolish(bpy.types.Operator):
    bl_idname = "sculpt.polish"
    bl_label = "Sculpt-Polish"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        layout = self.layout
        bpy.context.tool_settings.sculpt.brush=bpy.data.brushes['Polish']    
        return {'FINISHED'} 

bpy.utils.register_class(SculptPolish)

class SculptSculptDraw(bpy.types.Operator):
    bl_idname = "sculpt.sculptraw"
    bl_label = "Sculpt-SculptDraw"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        layout = self.layout
        bpy.context.tool_settings.sculpt.brush=bpy.data.brushes['SculptDraw']
        return {'FINISHED'}

bpy.utils.register_class(SculptSculptDraw)


class VertexDraw(bpy.types.Operator):
    bl_idname = "vertex.draw"
    bl_label = "Vertex Draw"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        layout = self.layout
        bpy.context.tool_settings.vertex_paint.brush=bpy.data.brushes['Draw']    
        return {'FINISHED'} 

bpy.utils.register_class(VertexDraw)

class VertexBrush(bpy.types.Operator):
    bl_idname = "vertex.brush"
    bl_label = "Vertex Brush"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        layout = self.layout
        bpy.context.tool_settings.vertex_paint.brush=bpy.data.brushes['Brush']    
        return {'FINISHED'} 

bpy.utils.register_class(VertexBrush)
           
######################################################################################################################################################
############------------############
############  REGISTER  ############
############------------############
######################################################################################################################################################
   
def register():
    bpy.utils.register_module(__name__)
 
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()













