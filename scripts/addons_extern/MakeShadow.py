bl_info = {
    "name": "Make Shadow",
    "author": "Andreas Esau",
    "version": (0, 1),
    "blender": (2, 6, 3),
    "api": 50000,
    "location": "Properties > Render",
    "description": "A simple Shadow Baker for static Shadows.",
    "warning": "This is just a testversion and may contain several bugs!",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Game Engine"}

import bpy
from bpy.props import StringProperty, BoolProperty, EnumProperty, IntProperty, FloatProperty
import mathutils

class MakeShadow(bpy.types.Panel):
    bl_label = "MakeShadow - Lightbaker"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    COMPAT_ENGINES = {'BLENDER_RENDER'}
    
    def draw(self, context):
        col = self.layout.column()
        row = self.layout.row()
        split = self.layout.split()
        ob = context.object
        scene = context.scene
        row.template_list(scene, "ms_lightmap_groups", scene, "ms_lightmap_groups_index",prop_list="template_list_controls", rows=2)
        col = row.column(align=True)
        col.operator("scene.ms_add_lightmap_group", icon='ZOOMIN', text="")
        col.operator("scene.ms_del_lightmap_group", icon='ZOOMOUT', text="")
        
        row = self.layout.row(align=True)
        
        try:
            row.prop(context.scene.ms_lightmap_groups[context.scene.ms_lightmap_groups_index], 'bake_type', text='Shadow',expand=True)
            row = self.layout.row()
            row.prop(context.scene.ms_lightmap_groups[context.scene.ms_lightmap_groups_index], 'resolution', text='Resolution',expand=True)
            row = self.layout.row()
            row.prop(context.scene.ms_lightmap_groups[context.scene.ms_lightmap_groups_index], 'sh_intens', text='Shadow Intensity', slider = True)  
            row = self.layout.row()
            row.prop(context.scene.ms_lightmap_groups[context.scene.ms_lightmap_groups_index], 'spec_intens', text='Specular Intensity', slider = True)        
        except:
            pass    
        
        row = self.layout.row()
        row = self.layout.row()
        row = self.layout.row()
        row = self.layout.row()
        row = self.layout.row()
        row = self.layout.row()
        row = self.layout.row()
        row = self.layout.row()
        row.operator("scene.ms_add_selected_to_group", text="Add Selection To Current Group",icon="GROUP")
        
        row = self.layout.row()
        row.operator("object.ms_run",text="Create Shadow Map",icon="LAMP_SPOT")

class runMakeShadow(bpy.types.Operator):
    bl_idname = "object.ms_run"
    bl_label = "MakeShadow - Run"
    bl_description = "Creates a Shadowmap from selected Objects"
    
    
    
    def execute(self, context):
        old_context = bpy.context.area.type
        
        try:
            OBJECTLIST = []
            active_object = bpy.context.scene.objects.active.name
            for object in bpy.context.selected_objects:
                OBJECTLIST.append(object.name)
            
            
            
            bpy.context.area.type = 'VIEW_3D'
            i = 0    
            for group in bpy.context.scene.ms_lightmap_groups:
    
                if group.bake == True:
                    if i == 0:
                        bpy.ops.object.ms_merge_objects(group_name=group.name)
                        bpy.ops.object.ms_create_lightmap(group_name=group.name)
                    
                    res = int(bpy.context.scene.ms_lightmap_groups[group.name].resolution)
                    bpy.ops.object.ms_bake_lightmap(group_name=group.name,resolution=res)
                    
                    
                    i += 1  
                    if i >= len(bpy.context.scene.ms_lightmap_groups):
                        bpy.ops.object.ms_separate_objects(group_name=group.name) 
                      
            bpy.context.area.type = old_context
            
            bpy.ops.object.select_all(action='DESELECT')
            for object in OBJECTLIST:
                bpy.context.scene.objects[object].select = True
                bpy.context.scene.objects.active = bpy.context.scene.objects[active_object]
        except:
             self.report({'INFO'}, "Something went wrong!") 
             bpy.context.area.type = old_context  
        return{'FINISHED'}
    
class uv_layers(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(default="")

class materials(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(default="")

class children(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(default="") 
    
class vertex_groups(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(default="") 
    
class groups(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(default="") 

class ms_lightmap_groups(bpy.types.PropertyGroup):
    
    def update_color(self, context):
        for object in bpy.data.groups[self.name].objects:
            for material in object.data.materials:
                material.texture_slots[self.name].diffuse_color_factor = self.sh_intens
                
    def update_spec(self, context):
        for object in bpy.data.groups[self.name].objects:
            for material in object.data.materials:
                material.texture_slots[self.name].specular_factor = self.spec_intens
                
    def update(self,context):
        for object in bpy.data.groups[self.name].objects:
            for material in object.data.materials:
                material.texture_slots[self.name].use = self.show
    
    name = bpy.props.StringProperty(default="")
    bake = bpy.props.BoolProperty(default=True)
    show = bpy.props.BoolProperty(default=True,update=update)
    sh_intens = FloatProperty(default=1.0,min=0.0,max=1.0,update=update_color)
    spec_intens = FloatProperty(default=5.0,min=0.0,max=10.0,update=update_spec)
    bake_type = EnumProperty(name="bake_type",items=(('0','Shadow','SHADOW'),('1','Ambient Occlusion','AMBIENT_OCCLUSION')))
    resolution = EnumProperty(name="resolution",items=(('256','256','256'),('512','512','512'),('1024','1024','1024'),('2048','2048','2048'),('4096','4096','4096')))
    template_list_controls = StringProperty(default="show", options={"HIDDEN"})
    
    

class mergedObjects(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(default="")
    position = bpy.props.FloatVectorProperty(default=(0.0,0.0,0.0))
    scale = bpy.props.FloatVectorProperty(default=(0.0,0.0,0.0))
    rotation = bpy.props.FloatVectorProperty(default=(0.0,0.0,0.0))
    material = bpy.props.CollectionProperty(type=materials)
    parent = bpy.props.StringProperty(default="")
    children = bpy.props.CollectionProperty(type=children)
    vertex_groups = bpy.props.CollectionProperty(type=vertex_groups)
    groups = bpy.props.CollectionProperty(type=groups)
    uv_layers = bpy.props.CollectionProperty(type=uv_layers)
    

class addSelectedToGroup(bpy.types.Operator):
    bl_idname = "scene.ms_add_selected_to_group" 
    bl_label = ""
    bl_description = "Adds selected Objects to current Group"
    
    
    def execute(self, context):
        try:
            group_name = bpy.context.scene.ms_lightmap_groups[bpy.context.scene.ms_lightmap_groups_index].name
        except:
            self.report({'INFO'}, "No Groups Exists!")
        for object in bpy.context.selected_objects:
            if object.type == 'MESH':
                try:
                    bpy.data.groups[group_name].objects.link(object)
                except:
                    pass
                    
        return {'FINISHED'}


class addLightmapGroup(bpy.types.Operator):
    bl_idname = "scene.ms_add_lightmap_group" 
    bl_label = ""
    bl_description = "Adds a new Lightmap Group"
    
    name = StringProperty(name="Group Name",default='lightmap') 

    def execute(self, context):
        group = bpy.data.groups.new(self.name)
        
        item = bpy.context.scene.ms_lightmap_groups.add() 
        item.name = group.name
        item.resolution = '1024'
        bpy.context.scene.ms_lightmap_groups_index = len(bpy.context.scene.ms_lightmap_groups)-1
        
        
        for object in bpy.context.selected_objects:
            bpy.context.scene.objects.active = object
            if bpy.context.active_object.type == 'MESH':
                bpy.data.groups[group.name].objects.link(object)

        
        return {'FINISHED'}
    
    def invoke(self, context, event): 
        wm = context.window_manager 
        return wm.invoke_props_dialog(self) 
    
class delLightmapGroup(bpy.types.Operator):
    bl_idname = "scene.ms_del_lightmap_group" 
    bl_label = ""
    bl_description = "Deletes active Lightmap Group"
    

    def execute(self, context):
        idx = bpy.context.scene.ms_lightmap_groups_index
        group_name = bpy.context.scene.ms_lightmap_groups[idx].name
        for object in bpy.data.groups[group_name].objects:
            for material in object.data.materials:
                for i in range(len(material.texture_slots)):
                    if material.texture_slots[i] != None:
                        if material.texture_slots[i].name == group_name:
                            print (material.texture_slots[i].name)
                            material.texture_slots[i].use = False
                            material.texture_slots.clear(i)
        
        
        bpy.data.groups.remove(bpy.data.groups[bpy.context.scene.ms_lightmap_groups[idx].name])
        bpy.context.scene.ms_lightmap_groups.remove(bpy.context.scene.ms_lightmap_groups_index)
        bpy.context.scene.ms_lightmap_groups_index -= 1
        if bpy.context.scene.ms_lightmap_groups_index < 0:
            bpy.context.scene.ms_lightmap_groups_index = 0
            
        
        return {'FINISHED'}

class mergeObjects(bpy.types.Operator):
    bl_idname = "object.ms_merge_objects" 
    bl_label = "MakeShadow - MergeObjects"
    bl_description = "Merges Objects and stores Origins"
    
    group_name = StringProperty(default='lightmap')

    def execute(self, context):
        active_object = bpy.data.groups[self.group_name].objects[0]
        
        bpy.ops.object.select_all(action='DESELECT')
        OBJECTLIST = []
        for object in bpy.data.groups[self.group_name].objects:
            OBJECTLIST.append(object)   
            object.select = True   
        bpy.context.scene.objects.active = active_object      

        #for object in OBJECTLIST:
        #    object.select = True
        
        ### Make Object Single User
        bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=True, obdata=True, material=False, texture=False, animation=False)
            
        for object in bpy.context.selected_objects:
            ### delete lightmap uv if existant
            for uv in object.data.uv_textures:
                if uv.name == 'lightmap':
                    uv.active = True
                    bpy.context.scene.objects.active = object
                    bpy.ops.mesh.uv_texture_remove()
                    
            
            
            ### create Material if none exists
            if len(object.material_slots) == 0:
                mat = bpy.data.materials.new(object.name)
                object.data.materials.append(bpy.data.materials[object.name])
            elif object.material_slots[0].name == '':
                mat = bpy.data.materials.new(object.name)
                object.data.materials.append(bpy.data.materials[object.name])
                
            ### create vertex groups for each selected object
            bpy.context.scene.objects.active = bpy.data.objects[object.name]
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.object.vertex_group_add()
            bpy.ops.object.vertex_group_assign()
            id = len(bpy.context.object.vertex_groups)-1
            bpy.context.object.vertex_groups[id].name = object.name
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.mode_set(mode = 'OBJECT')
            
            
            ### save object name and object location in merged object
            item = active_object.ms_merged_objects.add()
            item.name = object.name
            item.scale = mathutils.Vector(object.scale)
            item.rotation = mathutils.Vector(object.rotation_euler)
            
            ### save vertex group name in merged object
            for vertex_group in object.vertex_groups:
                item4 = active_object.ms_merged_objects[item.name].vertex_groups.add()
                item4.name = vertex_group.name 
            
            ### save uv layer name
            for layer in object.data.uv_layers:
                item6 = active_object.ms_merged_objects[item.name].uv_layers.add()
                item6.name = layer.name
                
            ### save vertex group name in merged object
            for group in bpy.data.groups:
                if object.name in group.objects:
                    item5 = active_object.ms_merged_objects[item.name].groups.add()
                    item5.name = group.name     
            
            ### save material name in merged object
            for material in object.material_slots:
                item2 = active_object.ms_merged_objects[item.name].material.add()
                item2.name = material.name
            
            for child in object.children:
                if child not in bpy.context.selected_objects:
                    item3 = active_object.ms_merged_objects[item.name].children.add()
                    item3.name = child.name
                    
            if object.parent != None:
                item.parent = object.parent.name
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.scene.objects[object.name].select = True
                bpy.context.scene.objects.active = bpy.context.scene.objects[object.name]
                bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
            else:
                item.parent = ''
            
            ### generate temp Duplicate Objects with copied modifier,properties and logic bricks
            bpy.ops.object.select_all(action='DESELECT')
            
            bpy.context.scene.objects.active = object
            me = bpy.data.meshes.new(object.name+'_t')
            ob = bpy.data.objects.new(object.name+'_t',me)
            bpy.context.scene.objects.link(ob)
            ob.select = True
            ob.location = object.location
            
            bpy.ops.object.make_links_data(type='MODIFIERS')
            bpy.ops.object.game_property_copy(operation='MERGE')
            bpy.ops.object.logic_bricks_copy()
            
            bpy.ops.object.select_all(action='DESELECT')
            for object in OBJECTLIST:
                object.select = True
            ##### 
                
            item.position = mathutils.Vector(object.location)
            
            
                

        ### merge objects together
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        bpy.context.scene.objects.active = active_object
        bpy.ops.object.join()
        bpy.context.object.name = 'mergedObject'
        
        return{'FINISHED'}

class createLightmap(bpy.types.Operator):
    bl_idname = "object.ms_create_lightmap" 
    bl_label = "MakeShadow - Generate Lightmap"
    bl_description = "Generates a Lightmap"
    
    group_name = StringProperty(default='')

    def execute(self, context):  
        
        ### create lightmap uv layout
        bpy.ops.object.mode_set(mode = 'EDIT')
        
        if bpy.context.object.data.uv_textures.active == None:
            bpy.ops.mesh.uv_texture_add()
            bpy.context.object.data.uv_textures.active.name = 'lightmap'
        else:    
            if 'lightmap' not in bpy.context.object.data.uv_textures:
                bpy.ops.mesh.uv_texture_add()
                bpy.context.object.data.uv_textures.active.name = 'lightmap'
                bpy.context.object.data.uv_textures['lightmap'].active = True
                bpy.context.object.data.uv_textures['lightmap'].active_render = True
            else:
                bpy.context.object.data.uv_textures['lightmap'].active = True
                bpy.context.object.data.uv_textures['lightmap'].active_render = True
                
        bpy.ops.uv.lightmap_pack(PREF_CONTEXT='ALL_FACES', PREF_PACK_IN_ONE=True, PREF_NEW_UVLAYER=False, PREF_APPLY_IMAGE=False, PREF_IMG_PX_SIZE=512, PREF_BOX_DIV=48, PREF_MARGIN_DIV=0.3)
        bpy.ops.object.mode_set(mode = 'OBJECT')
        return{'FINISHED'}


class bakeLightmap(bpy.types.Operator):
    bl_idname = "object.ms_bake_lightmap" 
    bl_label = "MakeShadow - Bake Lightmap"
    bl_description = "Bakes a Lightmap"
    
    group_name = StringProperty(default='')
    resolution = IntProperty(default=1024)

    def execute(self, context):
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        if self.group_name not in bpy.data.images:
            bpy.ops.image.new(name=self.group_name,width=self.resolution,height=self.resolution)
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.data.screens['UV Editing'].areas[1].spaces[0].image = bpy.data.images[self.group_name]
        else:
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.data.screens['UV Editing'].areas[1].spaces[0].image = bpy.data.images[self.group_name]
            bpy.data.images[self.group_name].generated_type = 'BLANK'
            bpy.data.images[self.group_name].generated_width = self.resolution
            bpy.data.images[self.group_name].generated_height = self.resolution
            
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        current_bake_type = bpy.context.scene.render.bake_type
        bake_margin = bpy.context.scene.render.bake_margin
        bpy.context.scene.render.bake_margin = 4
        
        if bpy.context.scene.ms_lightmap_groups[self.group_name].bake_type == '0':
            bpy.context.scene.render.bake_type = 'SHADOW'
        elif bpy.context.scene.ms_lightmap_groups[self.group_name].bake_type == '1':
            bpy.context.scene.render.bake_type = 'AO'
            normalized = bpy.context.scene.render.use_bake_normalize
            bpy.context.scene.render.use_bake_normalize = True
            
            
        bpy.ops.object.bake_image()
        
        try:
            bpy.context.scene.render.use_bake_normalize = normalized
        except:
            pass
        bpy.context.scene.render.bake_type = current_bake_type
        bpy.context.scene.render.bake_margin = bake_margin
        
        return{'FINISHED'}
    
class separateObjects(bpy.types.Operator):
    bl_idname = "object.ms_separate_objects" 
    bl_label = "MakeShadow - Separate Objects"
    bl_description = "Separates Objects and restores Origin"
    
    group_name = StringProperty(default='')

    def execute(self, context):
        active_object = bpy.context.active_object.name
        for object in bpy.context.scene.objects:
            if object.mode != 'OBJECT':
                bpy.context.scene.objects.active = object
                bpy.ops.object.mode_set(mode = 'OBJECT')
            
        bpy.context.scene.objects.active = bpy.context.scene.objects[active_object]
        
        OBJECTLIST = []
        for object in bpy.context.active_object.ms_merged_objects:
            OBJECTLIST.append(object.name)
            ### select vertex groups and separate group from merged object
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.context.active_object.vertex_groups.active_index = bpy.context.active_object.vertex_groups[object.name].index            
            bpy.ops.object.vertex_group_select()
            bpy.ops.mesh.separate(type='SELECTED')
            
            ### rename separated object to old name
            bpy.ops.object.mode_set(mode = 'OBJECT')
            bpy.context.scene.objects.active = bpy.context.scene.objects[active_object+'.001']
            bpy.ops.object.select_all(action='TOGGLE')
            bpy.context.scene.objects.active.select = True
            bpy.context.active_object.name = object.name
            bpy.context.active_object.data.name = object.name
            
            ### restore objects origin
            bpy.context.scene.cursor_location = bpy.context.scene.objects[object.name+'_t'].location#object.position
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            
            ### restore objects rotation
            bpy.context.active_object.rotation_euler = mathutils.Vector(object.rotation)
            for vertex in bpy.context.active_object.data.vertices:
                vertex.co = vertex.co * bpy.context.active_object.rotation_euler.to_matrix()
            
            ### restore objects scale
            old_pivot_point = bpy.context.space_data.pivot_point
            bpy.context.active_object.scale = object.scale
            bpy.context.space_data.pivot_point = 'CURSOR'
            for vertex in bpy.context.active_object.data.vertices:
                vertex.co[0] = vertex.co[0] * (1/bpy.context.active_object.scale[0])
                vertex.co[1] = vertex.co[1] * (1/bpy.context.active_object.scale[1])
                vertex.co[2] = vertex.co[2] * (1/bpy.context.active_object.scale[2])            
            bpy.context.space_data.pivot_point = old_pivot_point
            
                    
            ### restore parent
            if object.parent != '':
                bpy.context.scene.objects[object.parent].select=True
                bpy.context.scene.objects.active = bpy.context.scene.objects[object.parent]  
                bpy.ops.object.parent_set(type='OBJECT', xmirror=False)
                bpy.ops.object.select_all(action='TOGGLE')
                bpy.context.scene.objects.active = bpy.context.scene.objects[object.name]  
                
            
                
            ### delete not used materials from separeted objects
            slot_length = len(bpy.context.scene.objects[object.name].material_slots)
            for i in range(0,len(bpy.context.scene.objects[object.name].material_slots)):
                idx = slot_length-1-i
                bpy.context.active_object.active_material_index = idx
                try:
                    if bpy.context.scene.objects[object.name].active_material.name not in object.material:
                        bpy.ops.object.material_slot_remove()
                except:
                    bpy.ops.object.material_slot_remove()
                    
            bpy.context.active_object.active_material_index = 0
            
            ### delete vertex groups and object properties
            for group in bpy.context.active_object.ms_merged_objects:
                id = bpy.context.active_object.vertex_groups[group.name]
                bpy.context.active_object.vertex_groups.remove(id)
            #bpy.ops.wm.properties_remove(data_path="object",property="ms_merged_objects")
            
            ### delete not used vertex groups from separeted objects
            for vertex_group in bpy.context.scene.objects[object.name].vertex_groups:
                if vertex_group.name not in object.vertex_groups:
                    bpy.context.scene.objects[object.name].vertex_groups.remove(vertex_group)
                
            ### delete not used groups from separeted objects
            for group in bpy.data.groups:
                if group.name not in object.groups:
                    try:
                        group.objects.unlink(bpy.context.scene.objects[object.name])
                    except:
                        pass
                if group.name in object.groups:
                    try:
                        group.objects.link(bpy.context.scene.objects[object.name])
                    except:
                        pass
                        
            
            ### generate overlay Texture
            for material in bpy.context.active_object.material_slots:  
                for image in bpy.data.images:
                    
                    if image.name in bpy.context.scene.ms_lightmap_groups:
                        print(image.name)
                        if image.name not in bpy.data.textures:
                            texture = bpy.data.textures.new(image.name, type = 'IMAGE')
                            texture.image = bpy.data.images[image.name]
                        else:
                            texture = bpy.data.textures[image.name]
                            texture.image = bpy.data.images[image.name]

                        print(texture.name)
                        if image.name not in material.material.texture_slots:
                            mtex = material.material.texture_slots.add()
                        else:
                            mtex = material.material.texture_slots[image.name]
                        mtex.texture = texture
                        mtex.texture_coords = 'UV'
                        mtex.uv_layer = 'lightmap'
                        mtex.blend_type = 'MULTIPLY'
                        mtex.use_map_specular = True
                        mtex.use = True
                        
                        bpy.data.textures[image.name].use_alpha = False
                        mtex.specular_factor = 5.0
            
            
#            for material in bpy.context.active_object.material_slots:  
#                if self.group_name not in bpy.data.textures:
#                    image = bpy.data.textures.new(self.group_name, type = 'IMAGE')
#                    image.image = bpy.data.images[self.group_name]
#                else:
#                    image = bpy.data.textures[self.group_name]
#                    image.image = bpy.data.images[self.group_name]
#                
#                if self.group_name not in material.material.texture_slots:
#                    mtex = material.material.texture_slots.add()
#                else:
#                    mtex = material.material.texture_slots[self.group_name]
#                mtex.texture = image
#                mtex.texture_coords = 'UV'
#                mtex.uv_layer = 'lightmap'
#                mtex.blend_type = 'MULTIPLY'
#                mtex.use_map_specular = True
#                mtex.use = True
#                
#                bpy.data.textures[self.group_name].use_alpha = False
#                mtex.specular_factor = 5.0
                
                
                
            bpy.context.scene.objects.active = bpy.context.scene.objects[active_object]
            bpy.context.scene.objects.active.select = True
            bpy.context.active_object.name = active_object 
            
        

        ### restore children of object
        for object in bpy.context.active_object.ms_merged_objects:            
            if 'children' in object:
                for child in object.children:
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.context.scene.objects[child.name].select = True
                    bpy.context.scene.objects[object.name].select = True
                    bpy.context.scene.objects.active = bpy.context.scene.objects[object.name]
                    
                    bpy.ops.object.parent_set(type='OBJECT', xmirror=False)
                
        
        ### restore UV Name
            
        for name in OBJECTLIST:
            bpy.ops.object.select_all(action='DESELECT')
            
            bpy.context.scene.objects[name].select = True
            bpy.context.scene.objects.active = bpy.context.scene.objects[name]
            
            for i in range(len(bpy.context.scene.objects[name].ms_merged_objects[name].uv_layers)):
                uv = bpy.context.scene.objects[name].data.uv_textures[i]
                uv.name = bpy.context.scene.objects[name].ms_merged_objects[name].uv_layers[i].name
         
            object = bpy.context.active_object
            
            uv = object.data.uv_textures
            uv_len = len(uv)
            for i in range(uv_len):
                idx = uv_len - i-1
                if uv[idx].name not in object.ms_merged_objects[object.name].uv_layers and uv[idx].name != 'lightmap':
                    uv[idx].active = True
                    bpy.ops.mesh.uv_texture_remove()
                    
            ### delete ms_merged_objects property
            bpy.ops.wm.properties_remove(data_path="object",property="ms_merged_objects")
            
        
            
        ### restore Logic Bricks, Properties, Modifier
        for name in OBJECTLIST:
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.scene.objects[name].select = True
            bpy.context.scene.objects[name+'_t'].select = True
            bpy.context.scene.objects.active = bpy.context.scene.objects[name+'_t']
            
            bpy.ops.object.make_links_data(type='MODIFIERS')
            bpy.ops.object.game_property_copy(operation='MERGE')
            bpy.ops.object.logic_bricks_copy()
        
        ### delete empty merged object
        
        bpy.ops.object.select_all(action='DESELECT')
        for name in OBJECTLIST:
            bpy.context.scene.objects[name+'_t'].select = True
        bpy.context.scene.objects[active_object].select = True
        bpy.ops.object.delete(use_global=False)
            
        return{'FINISHED'}



def register():
    bpy.utils.register_class(MakeShadow)
    
    bpy.utils.register_class(addLightmapGroup)
    bpy.utils.register_class(delLightmapGroup)
    bpy.utils.register_class(addSelectedToGroup)
    
    bpy.utils.register_class(runMakeShadow)
    bpy.utils.register_class(mergeObjects)
    bpy.utils.register_class(separateObjects)
    bpy.utils.register_class(createLightmap)
    bpy.utils.register_class(bakeLightmap)
    
    bpy.utils.register_class(materials)
    bpy.utils.register_class(uv_layers)
    bpy.utils.register_class(children)
    bpy.utils.register_class(vertex_groups)
    bpy.utils.register_class(groups)
    
    bpy.utils.register_class(mergedObjects)
    bpy.types.Object.ms_merged_objects = bpy.props.CollectionProperty(type=mergedObjects)
    
    bpy.utils.register_class(ms_lightmap_groups)
    bpy.types.Scene.ms_lightmap_groups = bpy.props.CollectionProperty(type=ms_lightmap_groups)
    bpy.types.Scene.ms_lightmap_groups_index = bpy.props.IntProperty()
    


def unregister():
    bpy.utils.unregister_class(MakeShadow)
    
    bpy.utils.unregister_class(addLightmapGroup)
    bpy.utils.unregister_class(delLightmapGroup)
    bpy.utils.unregister_class(addSelectedToGroup)
    
    bpy.utils.unregister_class(runMakeShadow)
    bpy.utils.unregister_class(mergeObjects)
    bpy.utils.unregister_class(separateObjects)
    bpy.utils.unregister_class(createLightmap)
    bpy.utils.unregister_class(bakeLightmap)
    
    bpy.utils.unregister_class(materials)
    bpy.utils.unregister_class(uv_layers)
    bpy.utils.unregister_class(children)
    bpy.utils.unregister_class(vertex_groups)
    bpy.utils.unregister_class(groups)
    
    bpy.utils.unregister_class(mergedObjects)
    
    bpy.utils.unregister_class(ms_lightmap_groups)
    
    
if __name__ == "__main__":
    register()