# PSL SNAPSHOT v1.0 - 3Dview Addon - Blender 2.5x
#
# THIS SCRIPT IS LICENSED UNDER GPL, 
# please read the license block.
#
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

#bl_info = {
#    "name": "PSL_SnapShot",
#    "author": "Daniel M. Lara & Jose Molina   http://josemolinagarcia.blogspot.com",
#    "link": "http://josemolinagarcia.blogspot.com",
#    "version": (1, 0),
#    "blender": (2, 6, 0),
#    "api": 35853,
#    "location": "View3D > Nkey Panel > PSL SnapShot",
#    "description": "Make SnapShots from Animated Meshes",
#    "warning": "",
#    "category": "Animation"}

# import the basic library
import bpy
import os

prefixpsl = 'PSL_'

snapshotSource = prefixpsl +'snapshotSource'
snapshotInstances = prefixpsl +'snapshotInstances'

nameMaterialSlot   = prefixpsl + 'SNAPSHOT_SLOT'
nameMaterialGray   = prefixpsl + 'SNAPSHOT_GRAY'
nameMaterialBlack  = prefixpsl + 'SNAPSHOT_BLACK'
nameMaterialCustom = prefixpsl + 'SNAPSHOT_CUSTOM'

nameObjectPrefix = prefixpsl + "SNAPSHOT_"
nameEmptyDad = prefixpsl + "SNAPSHOT_DAD"

def initializeMaterials():
    #check if exists
    try:
        materialgray = bpy.data.materials[nameMaterialGray]
    except:
        #create it
        materialgray = bpy.data.materials.new(nameMaterialGray)
        materialgray.diffuse_color=[.5,.5,.5]
        materialgray.diffuse_intensity = 1.0
        materialgray.specular_intensity = .0
        materialgray.use_fake_user = True
    #check if exists
    try:    
        materialblack = bpy.data.materials[nameMaterialBlack]
    except:  
        #create it      
        materialblack = materialgray.copy()
        materialblack.name = nameMaterialBlack
        materialblack.diffuse_color=[0.0,0.0,0.0]
        materialblack.use_fake_user = True
    
    try:
        materialcustom = bpy.data.materials[nameMaterialCustom]
    except:
        materialcustom = materialgray.copy()
        materialcustom.name = nameMaterialCustom
        materialcustom.diffuse_color=[1.0,0.0,0.0]
        materialcustom.use_fake_user = True
        

def initializeSnpashotGroups():
    try:
        group = bpy.data.groups[snapshotSource]                
    except:
        bpy.data.groups.new(snapshotSource)
    
    try:
        group = bpy.data.groups[snapshotInstances]                
    except:
        bpy.data.groups.new(snapshotInstances)


def initializePSLsnapshot():

    actual_object = ""        
    actual_mode = bpy.context.mode 
    scn = bpy.context.scene
    
    try:
        actual_object =  context.active_object.name            
    except:
        pass    
    if bpy.context.mode != 'OBJECT':
         bpy.ops.object.mode_set(mode='OBJECT')         
    bpy.ops.object.select_pattern(pattern="",extend=False)
    
    createEmptyGroup()
    initializeSnpashotGroups()  
    initializeMaterials() 

    
    bpy.ops.object.select_pattern(pattern=actual_object,extend=False)            
    try:    
        scn.objects.active = scn.objects[actual_object]    
        bpy.ops.object.mode_set(mode=actual_mode)       
    except:
        pass
     
        
def addObjectsToSource(context):
    objects_to_add = [obj.name for obj in bpy.context.selected_objects if obj.type == 'MESH']  
    scn = bpy.context.scene  
    for name in objects_to_add:  
        scn.objects.active = scn.objects[name]  
        bpy.ops.object.group_link(group=snapshotSource)

def createEmptyGroup():
    #check if exists
    actual_selected = bpy.context.selected_objects[:]
    try:
        dad = bpy.data.objects[nameEmptyDad]
    except:            
        #create
        scn = bpy.context.scene
        bpy.ops.object.add(type='EMPTY', view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0))
        new_empty = scn.objects.active
        new_empty.name = nameEmptyDad
    for object in bpy.data.objects:
        if object in actual_selected:
            object.select = True
        else:
            object.select = False
            
class PSL_AddToSourceGroup(bpy.types.Operator):
    bl_idname = "object.addtosourcegroup"
    bl_label = "Add To Source Group"
    bl_description = "Add element to source group"

    @classmethod
    def poll(cls, context):
        sel_objects = bpy.context.selected_objects
        if len(sel_objects) == 0 :
            return False
        all_mesh = True
        for object in sel_objects:
            if  object.type != 'MESH':
                all_mesh = False
                return all_mesh
        return all_mesh

    def execute(self, context): 
        try:
            #initializePSLsnapshot()    
            addObjectsToSource(context)                     
        except:
            self.report(type={'ERROR'}, message="Error adding to the source" ) 
        return {'FINISHED'}
    
class PSL_DeleteFromSourceGroup(bpy.types.Operator):
    bl_idname = "object.deletefromsourcegroup"
    bl_label = "Delete from Source Group"
    bl_description = "Delete element from source group"

    @classmethod
    def poll(cls, context):
        try:
            objects = bpy.data.groups[snapshotSource].objects
            sel_objects = context.selected_objects            
            for each_object in objects:
                is_there = False
                for each_selobject in sel_objects:
                    if each_selobject == each_object:
                        is_there = True
                        return is_there
                    
            return is_there
        except:
            return False
        return False
        return True#context.active_object is not None

    def execute(self, context): 
        try:
            sel_objects = context.selected_objects
            source_Group = bpy.data.groups[snapshotSource]
            for selobject in sel_objects:
                try:
                   source_Group.objects.unlink(selobject)
                except:
                    raise
            
        except:
            self.report(type={'ERROR'}, message="Error removing from source" ) 
        return {'FINISHED'}

def changeGroup (context,object):     
    scn = context.scene  
    scn.objects.active = scn.objects[object.name]  
    try:
        bpy.ops.group.objects_remove_active()
    except:
        pass
    bpy.ops.object.group_link(group=snapshotInstances)


def applyMaterial (context, object,materialname):
    scn = context.scene
    scn.objects.active = scn.objects[object.name]
    bpy.ops.object.material_slot_add()
    slot = object.material_slots['']
    #slot.name = nameMaterialSlot
    slot.material = bpy.data.materials[materialname]

def exportImportObj(object):
    newObject = None
    print("************************** " + object.name)
    filename = bpy.data.filepath.split(os.sep)[ len(bpy.data.filepath.split(os.sep))-1:][0]
    
    
    filepathbas= bpy.data.filepath.replace(filename,"")#'/tmp/'
    filepathobj=filepathbas+'psl_snapshot_temp.obj'
    filepathmtl=filepathbas+'psl_snapshot_temp.mtl'
    
    #bpy.ops.object.select_pattern(pattern="",extend=False)
    bpy.ops.object.select_pattern(pattern=object.name,extend=False)
    #scene.objects.active = scene.objects[object.name]

    bpy.ops.export_scene.obj(filepath=filepathobj,use_selection=True, use_materials=False)
    bpy.ops.import_scene.obj(filepath=filepathobj)
    
    try:
        os.remove(filepathobj)
    except:
        pass
    try:
        os.remove(filepathmtl)
    except:
        pass
    return newObject


    

#NEW diplicateObjects in obj
def duplicateObjects(context,material):
    objects = bpy.data.groups[snapshotSource].objects
    scn = bpy.context.scene  
    for eachobject in objects:
        if eachobject in context.visible_objects:
            exportImportObj(eachobject)
            newobject = context.selected_objects[0]
            newobject.name = eachobject.name
            newobject.name = nameObjectPrefix + newobject.name.split(".")[0] + "__"+ str(scn.frame_current)
            
            changeGroup(context,newobject)
            #applyMaterial
            if material == "GRAY":
                applyMaterial (context, newobject,nameMaterialGray)
            if material == "BLACK":
                applyMaterial (context, newobject,nameMaterialBlack)
            if material == "CUSTOM":
                applyMaterial (context, newobject,nameMaterialCustom)    
    
            #set parent
            newobject.parent = bpy.data.objects[nameEmptyDad]
            
            #decimate
            decimate = newobject.modifiers.new(name="decimate", type='DECIMATE')
            decimate.ratio = scn.psl_decimate_ratio


def generateSnapshot ( self, context):
    selected_objects = bpy.context.selected_objects[:]
    original_layers = bpy.context.scene.layers[:]
    actual_object = ""        
    actual_mode = context.mode 
    scn = context.scene  
    try:
        actual_object =  context.active_object.name            
    except:
        pass
    
    if context.mode != 'OBJECT':
         bpy.ops.object.mode_set(mode='OBJECT')
        
    for i in range(len(bpy.context.scene.layers)):
        bpy.context.scene.layers[i] = True
    
    bpy.ops.object.select_pattern(pattern="",extend=False) 
    bpy.context.scene.objects.active = None
    bpy.context.scene.layers = original_layers
    
    material = scn.psl_snapshot_material
    duplicateObjects(context,material)

        
    for object in context.scene.objects:
        if object in selected_objects:
            object.select = True
        else:
            object.select = False
    
       
    try:   
        scn.objects.active = scn.objects[actual_object]   
        bpy.ops.object.mode_set(mode=actual_mode)       
    except:
        pass
     
 

         
class PSL_MakeSnapshot(bpy.types.Operator):
    '''Tooltip'''
    bl_idname = "object.make_snapshot"
    bl_label = "Make Snapshot"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Make Snapshot!"
        
    material = bpy.props.StringProperty(name="material", description="Material", default="GRAY")

    @classmethod
    def poll(cls, context):
        try:
            objects = bpy.data.groups[snapshotSource].objects
            if len(objects) > 0 :
                return True
            else:
                return False
        except:
            return False
        return False

    def execute(self, context): 
        
        try:
            scn = context.scene
            if not scn.psl_generate_all:            
                CleanExistingSnapshot (context)
                generateSnapshot ( self, context)
            else:        
                last_frame = False    
                CleanAllSnapshots ( context )
                scn.frame_set(scn.psl_snapshot_start)
                generateSnapshot ( self, context)
                
                while (not last_frame) and (scn.frame_current < scn.psl_snapshot_end):
                    actual_frame = scn.frame_current
                    
                    bpy.ops.screen.keyframe_jump(next=True)
                    if actual_frame != scn.frame_current:
                        generateSnapshot ( self, context)
                    else:
                        last_frame = True
    
            
            if not scn.psl_generate_all and scn.psl_jump_next_frame:
                bpy.ops.screen.keyframe_jump(next=True)   
        except:
            self.report(type={'ERROR'}, message="Error making snapshot" ) 
        return {'FINISHED'}



def CleanExistingSnapshot (context):
    
    scn = context.scene 
    '''
    bpy.ops.object.select_pattern(pattern='',extend=False)
    bpy.ops.object.select_pattern(pattern='*'+ nameObjectPrefix + '*'+ str(scn.frame_current) +'*',extend=False)
    objects = context.selected_objects
    '''
    objects = []
    for object in scn.objects:
        if nameObjectPrefix in object.name:
            end = object.name.split("__")[len(object.name.split("__"))-1]
            if  str(scn.frame_current) == end:
                objects.append(object)
    CleanSnapshots(context, objects)

def CleanAllSnapshots ( context ):
    objects = bpy.data.groups[snapshotInstances].objects
    CleanSnapshots(context,objects)    

def CleanSnapshot (context, object):
    bpy.ops.object.select_pattern(pattern="",extend=False)
    
    scn = context.scene  
    object.hide_select = False
    object.select = True
    
    bpy.ops.object.delete()
    
    '''
    bpy.ops.object.select_pattern(pattern=object.name,extend=False)
    bpy.ops.object.delete()
    bpy.ops.object.select_pattern(pattern=object.name,extend=False)
    bpy.ops.object.delete()
    '''

def CleanSnapshots ( context, objects ): 
    something_selected = len(bpy.context.selected_objects) > 0
    
    actual_object = ""        
    actual_mode =  context.mode 
    
    try:
        actual_object =  context.active_object.name            
    except:
        pass
    
    if context.mode != 'OBJECT':
         bpy.ops.object.mode_set(mode='OBJECT')
         
    bpy.ops.object.select_pattern(pattern="",extend=False)
    scn = context.scene  
    #objects = bpy.data.groups[snapshotInstances].objects
    for object in objects:
        CleanSnapshot(context, object)

    
    bpy.ops.object.select_pattern(pattern=actual_object,extend=False)
    
    scn = context.scene    
    try:    
        scn.objects.active = scn.objects[actual_object]    
        bpy.ops.object.mode_set(mode=actual_mode)       
    except:
        pass
        
        
class PSL_CleanSnapshots(bpy.types.Operator):
    '''Tooltip'''
    bl_idname = "object.clean_snapshots"
    bl_label = "Clean Spanshots"
    bl_description = "Delete Current Frame Snapshot"
    
    all = bpy.props.BoolProperty(name="All", description="Delete all snapshots", default=False)
    
    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context): 
        try:
            if (self.all):        
                objects = bpy.data.groups[snapshotInstances].objects
                CleanSnapshots(context,objects)
            else:
                CleanExistingSnapshot(context)
                if context.scene.psl_jump_next_frame:
                    bpy.ops.screen.keyframe_jump(next=True) 
        
        except:
            self.report(type={'ERROR'}, message="Error deleting snapshot" )          
        return {'FINISHED'}
    

class PSL_SnapshotVisible(bpy.types.Operator):
    bl_idname = "object.snapshot_visible"
    bl_label = "Enable / Disable Visibility Snapshot"
    bl_description = "Show / Hide snapshots"
        
    visible = bpy.props.BoolProperty(name="Visible", description="make visible", default=False)
    
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context): 
        try:
            objects = bpy.data.groups[snapshotInstances].objects
            for object in objects:            
                object.hide = not self.visible      
            bpy.types.PSL_SnapshotUI.visible = self.visible
        except:
            self.report(type={'ERROR'}, message="Error while enabling / disabling visibility of the snapshots" )  
        return {'FINISHED'}
 
class PSL_SnapshotRendereable(bpy.types.Operator):
    bl_idname = "object.snapshot_renderable"
    bl_label = "Enable / Disable Render Snapshot"
    bl_description = "Enable / Disable render snapshots"
    
    rendeable = bpy.props.BoolProperty(name="Rendeable", description="make rendeable", default=False)
    
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context): 
        try:
            objects = bpy.data.groups[snapshotInstances].objects
            for object in objects:
                object.hide_render = not self.rendeable
            bpy.types.PSL_SnapshotUI.rendeable = self.rendeable   
        except:
            self.report(type={'ERROR'}, message="Error while enabling / disabling render of the snapshots" )                
        return {'FINISHED'}

class PSL_SnapshotSelectable(bpy.types.Operator):
    bl_idname = "object.snapshot_selectable"
    bl_label = "Select / Deselect snapshot"
    bl_description = "Enable / Disable select snapshots"
    
    selectable = bpy.props.BoolProperty(name="Selectable", description="make selectable", default=False)
    
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context): 
        try:
            objects = bpy.data.groups[snapshotInstances].objects
            for object in objects:            
                object.hide_select = not self.selectable      
            bpy.types.PSL_SnapshotUI.selectable = self.selectable
        except:
            self.report(type={'ERROR'}, message="Error while enabling / disabling select of the snapshots" )   
        return {'FINISHED'}    

class PSL_DecimateVisible(bpy.types.Operator):
    bl_idname = "object.decimate_visible"
    bl_label = "Enable / Disable visibility decimate"
    bl_description = "Enable / Disable visibility decimate modifier"
        
    visible = bpy.props.BoolProperty(name="Visible", description="make visible", default=False)
    
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context): 
        try:
            objects = bpy.data.groups[snapshotInstances].objects
            for object in objects:            
                object.modifiers['decimate'].show_viewport = not self.visible
            bpy.types.PSL_SnapshotUI.visible_decimate = self.visible
        except:
            self.report(type={'ERROR'}, message="Error while enabling / disabling visibility of the decimate" )   
        return {'FINISHED'}
 
class PSL_DecimateRendereable(bpy.types.Operator):
    bl_idname = "object.decimate_renderable"
    bl_label = "Enable / Disable render of decimate"
    bl_description = "Enable / Disable render decimate modifier"
        
    rendeable = bpy.props.BoolProperty(name="Rendeable", description="make rendeable", default=False)
    
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context): 
        try:
            objects = bpy.data.groups[snapshotInstances].objects
            for object in objects:
                object.modifiers['decimate'].show_render = not self.rendeable
            bpy.types.PSL_SnapshotUI.rendeable_decimate = self.rendeable    
        except:
            self.report(type={'ERROR'}, message="Error while enabling / disabling render of the decimate" )                 
        return {'FINISHED'}

class PSL_DecimateUpdate(bpy.types.Operator):
    bl_idname = "object.decimate_update"
    bl_label = "Update decimate ratio"    
    bl_description = "Update decimate modifier"   
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context): 
        try:
            objects = bpy.data.groups[snapshotInstances].objects
            for object in objects:
                object.modifiers['decimate'].ratio = context.scene.psl_decimate_ratio
        except:
            self.report(type={'ERROR'}, message="Error while updating the decimate" ) 
        return {'FINISHED'}

class PSL_RadioButtonMaterial(bpy.types.Operator):
    bl_idname = "object.pls_rdbmaterial"
    bl_label = "Update radio button material"    
    bl_description = "Select Material"    
    material   = bpy.props.StringProperty(name="material", description="material", default="BLACK")
    
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context):  
        try:       
            scn = context.scene
            scn.psl_snapshot_material = self.material
        except:
            self.report(type={'ERROR'}, message="Error updating material" ) 
        return {'FINISHED'}

class PSL_Snapshot_Initialize(bpy.types.Operator):
    bl_idname = "object.psl_snp_initialize"
    bl_label = "Initialize"    
    bl_description = "Re/Generate all necesary for the addon "
    
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context):  
        try:       
            initializePSLsnapshot()
        except:
            self.report(type={'ERROR'}, message="Error while initializing the addon" ) 
        return {'FINISHED'}



############--------------------############
############--------------------############

# Sub Location        
class SubLoc_Snapshot():
    """PSL Snapshot"""
    bl_category="VFX"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D' 
 

    @classmethod
    def poll(cls, context):
        return context.scene.osc_snapshot and context.mode == ('OBJECT')

## Sub Panel
class PSL_SnapshotUI(SubLoc_Snapshot, bpy.types.Panel):
    """PSL Snapshot"""
    bl_idname = """psl_snapshot"""
    bl_label = """[PSL SNAPSHOT]"""

    material   = bpy.props.BoolProperty(name="gray_material", description="gray_material", default=False)
    selectable = bpy.props.BoolProperty(name="Selectable", description="make selectable", default=False) 
    rendeable  = bpy.props.BoolProperty(name="Rendeable", description="make rendeable", default=False)
    visible    = bpy.props.BoolProperty(name="Visible", description="make visible", default=False)

    rendeable_decimate  = bpy.props.BoolProperty(name="Rendeable Decimate", description="make rendeable", default=False)
    visible_decimate    = bpy.props.BoolProperty(name="Visible Decimate", description="make visible", default=False)

    def draw(self, context):
        layout = self.layout        
        scn = bpy.context.scene  
        regenerar = False
        try: 
            m1 =  bpy.data.materials[nameMaterialBlack]
            m2 =  bpy.data.materials[nameMaterialGray]
            m3 =  bpy.data.materials[nameMaterialCustom]
        except:
            regenerar = True
        
        if not regenerar:
            #OBJ operators
            colobjs = layout.column()
            colobjs.label(text="Objs to Snapshot:")
            operator = colobjs.operator("object.addtosourcegroup",text="Add to List",icon='EXPORT')      
            operator = colobjs.operator("object.deletefromsourcegroup",text="Delete from List",icon='X')  
            colobjs.label(text="")
                
            
            #snapshot Operator
            
            colsnapshot = layout.row(align=True)
            colsnapshot.label(text="Snapshots") #, icon='GROUP')

            if self.visible :
                operator = colsnapshot.operator("object.snapshot_visible",text="",icon='RESTRICT_VIEW_OFF') 
                operator.visible=False
            else:
                operator = colsnapshot.operator("object.snapshot_visible",text="",icon='RESTRICT_VIEW_ON') 
                operator.visible=True

            if self.selectable:
                operator = colsnapshot.operator("object.snapshot_selectable",text="",icon='RESTRICT_SELECT_OFF') 
                operator.selectable=False
            else:
                operator = colsnapshot.operator("object.snapshot_selectable",text="",icon='RESTRICT_SELECT_ON') 
                operator.selectable=True
                 
            if self.rendeable :
                operator = colsnapshot.operator("object.snapshot_renderable",text="",icon='RESTRICT_RENDER_OFF') 
                operator.rendeable=False
            else:
                operator = colsnapshot.operator("object.snapshot_renderable",text="",icon='RESTRICT_RENDER_ON') 
                operator.rendeable=True
                
            colbuttonsnpshot = layout.row(align=True)  
            colbuttonsnpshot.scale_y = 2
            colbuttonsnpshot.prop ( scn,"psl_jump_next_frame", icon='FF',text="") 
            operator = colbuttonsnpshot.operator("object.make_snapshot",text="Make snapshot",icon='NONE')
            operator = colbuttonsnpshot.operator("object.clean_snapshots",text="",icon='X')  
            operator.all = False
            
            
            layout.separator()
            
            colgekeyscheck = layout.column()
            colgekeyscheck.prop ( scn, "psl_generate_all")#, icon ='SCRIPTPLUGINS')
            colgekeys = layout.row(align=True)
            colgekeys.enabled = scn.psl_generate_all
            colgekeys.prop ( scn,"psl_snapshot_start") 
            colgekeys.prop ( scn,"psl_snapshot_end") 
            
     

            col = layout.row()     
          
            boxcolors = col.box()
            

            if scn.psl_snapshot_material == 'BLACK':
                row = boxcolors.row()
                col1 = row.column()
                operator = col1.operator("object.pls_rdbmaterial",text="Color1",icon='RADIOBUT_ON',emboss=False)
                operator.material = "BLACK"  
                col1.active = True
                col2 = row.column()
                col2.prop ( bpy.data.materials[nameMaterialBlack],"diffuse_color",text ="", icon_only=True)   
                col2.enabled = True

                row = boxcolors.row()
                col1 = row.column()
                operator = col1.operator("object.pls_rdbmaterial",text="Color2",icon='RADIOBUT_OFF',emboss=False)
                operator.material = "GRAY"  
                col1.active = False
                col2 = row.column()
                col2.prop ( bpy.data.materials[nameMaterialGray],"diffuse_color",text ="", icon_only=True)   
                col2.enabled = True 
                
                row = boxcolors.row()
                col1 = row.column()
                operator = col1.operator("object.pls_rdbmaterial",text="Color3",icon='RADIOBUT_OFF',emboss=False)
                operator.material = "CUSTOM"  
                col1.active = False
                col2 = row.column()
                col2.prop ( bpy.data.materials[nameMaterialCustom],"diffuse_color",text ="", icon_only=True)   
                col2.enabled = True
                      
            if scn.psl_snapshot_material == 'GRAY':
                row = boxcolors.row()
                col1 = row.column()
                operator = col1.operator("object.pls_rdbmaterial",text="Color1",icon='RADIOBUT_OFF',emboss=False)
                operator.material = "BLACK"  
                col1.active = False
                col2 = row.column()
                col2.prop ( bpy.data.materials[nameMaterialBlack],"diffuse_color",text ="", icon_only=True)   
                col2.enabled = True
                
                row = boxcolors.row()
                col1 = row.column()
                operator = col1.operator("object.pls_rdbmaterial",text="Color2",icon='RADIOBUT_ON',emboss=False)
                operator.material = "GRAY"  
                col1.active = True
                col2 = row.column()
                col2.prop ( bpy.data.materials[nameMaterialGray],"diffuse_color",text ="", icon_only=True)   
                col2.enabled = True 
                
                row = boxcolors.row()
                col1 = row.column()
                operator = col1.operator("object.pls_rdbmaterial",text="Color3",icon='RADIOBUT_OFF',emboss=False)
                operator.material = "CUSTOM"  
                col1.active = False
                col2 = row.column()
                col2.prop ( bpy.data.materials[nameMaterialCustom],"diffuse_color",text ="", icon_only=True)   
                col2.enabled = True          
            if scn.psl_snapshot_material == 'CUSTOM':
                row = boxcolors.row()
                col1 = row.column()
                operator = col1.operator("object.pls_rdbmaterial",text="Color1",icon='RADIOBUT_OFF',emboss=False)
                operator.material = "BLACK"  
                col1.active = False
                col2 = row.column()
                col2.prop ( bpy.data.materials[nameMaterialBlack],"diffuse_color",text ="", icon_only=True)   
                col2.enabled = True
                
                row = boxcolors.row()
                col1 = row.column()
                operator = col1.operator("object.pls_rdbmaterial",text="Color2",icon='RADIOBUT_OFF',emboss=False)
                operator.material = "GRAY"  
                col1.active = False
                col2 = row.column()
                col2.prop ( bpy.data.materials[nameMaterialGray],"diffuse_color",text ="", icon_only=True)   
                col2.enabled = True 
                
                row = boxcolors.row()
                col1 = row.column()
                operator = col1.operator("object.pls_rdbmaterial",text="Color3",icon='RADIOBUT_ON',emboss=False)
                operator.material = "CUSTOM"  
                col1.active = True
                col2 = row.column()
                col2.prop ( bpy.data.materials[nameMaterialCustom],"diffuse_color",text ="", icon_only=True)   
                col2.enabled = True
                
           
            
            
          
            layout.separator()
           
            rowcleansnapshot = layout.row(align=False)
            rowcleansnapshot.label(text="Optimize Snapshot Meshes:") #, icon='GROUP')

            type_vis = True
            coldecimate = layout.row(align=True)
            coldecimate.prop(scn,"psl_decimate_ratio")
            operator =coldecimate.operator("object.decimate_update",text="",icon='FILE_REFRESH',emboss=type_vis)   
            
            coldecimate.separator()
            
            if self.visible_decimate :
                operator = coldecimate.operator("object.decimate_visible",text="",icon='RESTRICT_VIEW_ON',emboss=type_vis) 
                operator.visible=False
            else:            
                operator = coldecimate.operator("object.decimate_visible",text="",icon='RESTRICT_VIEW_OFF',emboss=type_vis) 
                operator.visible=True           
            
                 
            if self.rendeable_decimate :
                operator = coldecimate.operator("object.decimate_renderable",text="",icon='RESTRICT_RENDER_OFF',emboss=type_vis) 
                operator.rendeable=False
            else:
                #col = col.box()
                operator = coldecimate.operator("object.decimate_renderable",text="",icon='RESTRICT_RENDER_ON',emboss=type_vis) 
                operator.rendeable=True
            
            layout.separator()
            
            rowcleanall = layout.row(align=True)
            
            rowcleanall.scale_y = 1
            operator = rowcleanall.operator("object.clean_snapshots",text="Clean All Snapshots",icon='CANCEL')  
            operator.all = True
            
            # if there aren't elements in source
            num_objects = len(bpy.data.groups[snapshotSource].objects)
            if num_objects == 0 :
                #col.enabled = False
                colsnapshot.enabled = False
                boxcolors.enabled = False
                colbuttonsnpshot.enabled = False
                colgekeyscheck.enabled = False
                colgekeys.enabled = False
                coldecimate.enabled = False
                rowcleanall.enabled = False
                rowcleansnapshot.enabled = False
                
                
        else:
            colobjs = layout.column()
            #colobjs.label(text="Objs to Snapshot:")
            operator = colobjs.operator("object.psl_snp_initialize",text="Initialize",icon='EXPORT') 

        
def register():
    # Define properties for the draw setting.
    
    bpy.types.Scene.psl_generate_all = bpy.props.BoolProperty(
        name="Do it in all keyframes",
        description="Generate Snapshots in all Keyframes from start to end",
        default=0)
    bpy.types.Scene.psl_snapshot_start = bpy.props.IntProperty(
        name="Start",
        description="From frame snapshot",
        default=0)    
    bpy.types.Scene.psl_snapshot_end = bpy.props.IntProperty(
        name="End",
        description="To end snapshot",
        default=150)
            
    bpy.types.Scene.psl_jump_next_frame = bpy.props.BoolProperty(
        name="Jump next key-frame",
        description="When on jump to next key-frame after make snapshot",
        default=0)

    bpy.types.Scene.psl_decimate_ratio = bpy.props.FloatProperty(
        name="Decimate Ratio",
        description="Value of the decimate modifier",
        max=1,
        min=0,
        default=1.0)   
    
    bpy.types.Scene.psl_decimate_renderable = bpy.props.BoolProperty(
        name="Render decimate",
        description="Enable / disable renderable decimate",
        default=1)      
    bpy.types.Scene.psl_decimate_visibility = bpy.props.BoolProperty(
        name="Render visualize",
        description="Enable / disable visibility decimate",
        default=1) 
    
    bpy.types.Scene.psl_snapshot_material = bpy.props.StringProperty(
        name="Snapshot Material",
        description="Enable / disable visibility decimate",
        default="BLACK") 
        
    bpy.utils.register_class(PSL_AddToSourceGroup)
    bpy.utils.register_class(PSL_DeleteFromSourceGroup)
    bpy.utils.register_class(PSL_MakeSnapshot)
    bpy.utils.register_class(PSL_CleanSnapshots)
    bpy.utils.register_class(PSL_SnapshotRendereable)
    bpy.utils.register_class(PSL_SnapshotSelectable)    
    bpy.utils.register_class(PSL_SnapshotUI)
    bpy.utils.register_class(PSL_SnapshotVisible)
    
    bpy.utils.register_class(PSL_RadioButtonMaterial)

    bpy.utils.register_class(PSL_DecimateVisible)
    bpy.utils.register_class(PSL_DecimateRendereable)  
    bpy.utils.register_class(PSL_DecimateUpdate)
    
    bpy.utils.register_class(PSL_Snapshot_Initialize)
    
    #,initializePSLsnapshot()


def unregister():
    bpy.utils.unregister_class(PSL_AddToSourceGroup)
    bpy.utils.unregister_class(PSL_DeleteFromSourceGroup)
    bpy.utils.unregister_class(PSL_MakeSnapshot)
    bpy.utils.unregister_class(PSL_CleanSnapshots)
    bpy.utils.unregister_class(PSL_SnapshotRendereable)
    bpy.utils.unregister_class(PSL_SnapshotSelectable)  
    bpy.utils.unregister_class(PSL_SnapshotUI)
    bpy.utils.unregister_class(PSL_SnapshotVisible)
    
    bpy.utils.unregister_class(PSL_RadioButtonMaterial)

    bpy.utils.unregister_class(PSL_DecimateVisible)
    bpy.utils.unregister_class(PSL_DecimateRendereable)        
    bpy.utils.unregister_class(PSL_DecimateUpdate)  
    
    bpy.utils.unregister_class(PSL_Snapshot_Initialize)
    
    del bpy.types.Scene.psl_generate_all
    del bpy.types.Scene.psl_snapshot_start
    del bpy.types.Scene.psl_snapshot_end
    del bpy.types.Scene.psl_jump_next_frame
    del bpy.types.Scene.psl_decimate_ratio
    del bpy.types.Scene.psl_decimate_renderable
    del bpy.types.Scene.psl_decimate_visibility    
    del bpy.types.Scene.psl_snapshot_material
    

if __name__ == "__main__":    
    register()




