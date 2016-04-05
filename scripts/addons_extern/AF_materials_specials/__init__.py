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
#  (c) 2015 meta-androcto, parts based on work by Saidenka, Materials Utils by MichaleW Materials Conversion: Silvio Falcinelli#

bl_info = {
    "name": "AF: Materials Specials",
    "author": "Meta Androcto",
    "version": (0, 2),
    "blender": (2, 75, 0),
    "location": "Materials Specilas Menu/Shift Q",
    "description": "Extended Specials: Materials Properties",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6"\
        "/Py/Scripts",
    "tracker_url": "",
    "category": "Addon Factory"}

if "bpy" in locals():
    import importlib
    importlib.reload(materials_cycles_converter)
    importlib.reload(material_converter)
else:
    from . import materials_cycles_converter
    from . import material_converter

import bpy
from bpy.props import StringProperty, BoolProperty, EnumProperty

def fake_user_set(fake_user='ON', materials='UNUSED'):
    if materials == 'ALL':
        mats = (mat for mat in bpy.data.materials if mat.library is None)
    elif materials == 'UNUSED':
        mats = (mat for mat in bpy.data.materials if mat.library is None and mat.users == 0)
    else:
        mats = []
        if materials == 'ACTIVE':
            objs = [bpy.context.active_object]
        elif materials == 'SELECTED':
            objs = bpy.context.selected_objects
        elif materials == 'SCENE':
            objs = bpy.context.scene.objects
        else: # materials == 'USED'
            objs = bpy.data.objects
            # Maybe check for users > 0 instead?

        """ more reable than the following generator:
        for ob in objs:
            if hasattr(ob.data, "materials"):
                for mat in ob.data.materials:
                    if mat.library is None: #and not in mats:
                        mats.append(mat)
        """
        mats = (mat for ob in objs if hasattr(ob.data, "materials") for mat in ob.data.materials if mat.library is None)

    for mat in mats:
        mat.use_fake_user = fake_user == 'ON'

    for area in bpy.context.screen.areas:
        if area.type in ('PROPERTIES', 'NODE_EDITOR'):
            area.tag_redraw()


def replace_material(m1, m2, all_objects=False, update_selection=False):
    # replace material named m1 with material named m2
    # m1 is the name of original material
    # m2 is the name of the material to replace it with
    # 'all' will replace throughout the blend file

    matorg = bpy.data.materials.get(m1)
    matrep = bpy.data.materials.get(m2)

    if matorg != matrep and None not in (matorg, matrep):
        #store active object
        scn = bpy.context.scene

        if all_objects:
            objs = bpy.data.objects

        else:
            objs = bpy.context.selected_editable_objects

        for ob in objs:
            if ob.type == 'MESH':

                match = False

                for m in ob.material_slots:
                    if m.material == matorg:
                        m.material = matrep
                        # don't break the loop as the material can be
                        # ref'd more than once

                        # Indicate which objects were affected
                        if update_selection:
                            ob.select = True
                            match = True

                if update_selection and not match:
                    ob.select = False

    #else:
    #    print('Replace material: nothing to replace')


def select_material_by_name(find_mat_name):
    #in object mode selects all objects with material find_mat_name
    #in edit mode selects all polygons with material find_mat_name

    find_mat = bpy.data.materials.get(find_mat_name)

    if find_mat is None:
        return

    #check for editmode
    editmode = False

    scn = bpy.context.scene

    #set selection mode to polygons
    scn.tool_settings.mesh_select_mode = False, False, True

    actob = bpy.context.active_object
    if actob.mode == 'EDIT':
        editmode = True
        bpy.ops.object.mode_set()

    if not editmode:
        objs = bpy.data.objects
        for ob in objs:
            if ob.type in {'MESH', 'CURVE', 'SURFACE', 'FONT', 'META'}:
                ms = ob.material_slots
                for m in ms:
                    if m.material == find_mat:
                        ob.select = True
                        # the active object may not have the mat!
                        # set it to one that does!
                        scn.objects.active = ob
                        break
                    else:
                        ob.select = False

            #deselect non-meshes
            else:
                ob.select = False

    else:
        #it's editmode, so select the polygons
        ob = actob
        ms = ob.material_slots

        #same material can be on multiple slots
        slot_indeces = []
        i = 0
        # found = False  # UNUSED
        for m in ms:
            if m.material == find_mat:
                slot_indeces.append(i)
                # found = True  # UNUSED
            i += 1
        me = ob.data
        for f in me.polygons:
            if f.material_index in slot_indeces:
                f.select = True
            else:
                f.select = False
        me.update()
    if editmode:
        bpy.ops.object.mode_set(mode='EDIT')


def mat_to_texface():
    # assigns the first image in each material to the polygons in the active
    # uvlayer for all selected objects

    #check for editmode
    editmode = False

    actob = bpy.context.active_object
    if actob.mode == 'EDIT':
        editmode = True
        bpy.ops.object.mode_set()

    for ob in bpy.context.selected_editable_objects:
        if ob.type == 'MESH':
            #get the materials from slots
            ms = ob.material_slots

            #build a list of images, one per material
            images = []
            #get the textures from the mats
            for m in ms:
                if m.material is None:
                    continue
                gotimage = False
                textures = zip(m.material.texture_slots, m.material.use_textures)
                for t, enabled in textures:
                    if enabled and t is not None:
                        tex = t.texture
                        if tex.type == 'IMAGE':
                            img = tex.image
                            images.append(img)
                            gotimage = True
                            break

                if not gotimage:
#                    print('noimage on', m.name)
                    images.append(None)

            # now we have the images applythem to the uvlayer

            me = ob.data
            #got uvs?
            if not me.uv_textures:
                scn = bpy.context.scene
                scn.objects.active = ob
                bpy.ops.mesh.uv_texture_add()
                scn.objects.active = actob

            #get active uvlayer
            for t in  me.uv_textures:
                if t.active:
                    uvtex = t.data
                    for f in me.polygons:
                        #check that material had an image!
                        if images[f.material_index] is not None:
                            uvtex[f.index].image = images[f.material_index]
                        else:
                            uvtex[f.index].image = None

            me.update()

    if editmode:
        bpy.ops.object.mode_set(mode='EDIT')


def assignmatslots(ob, matlist):
    #given an object and a list of material names
    #removes all material slots form the object
    #adds new ones for each material in matlist
    #adds the materials to the slots as well.

    scn = bpy.context.scene
    ob_active = bpy.context.active_object
    scn.objects.active = ob

    for s in ob.material_slots:
        bpy.ops.object.material_slot_remove()

    # re-add them and assign material
    i = 0
    for m in matlist:
        mat = bpy.data.materials[m]
        ob.data.materials.append(mat)
        i += 1

    # restore active object:
    scn.objects.active = ob_active


def cleanmatslots():
    #check for edit mode
    editmode = False
    actob = bpy.context.active_object
    if actob.mode == 'EDIT':
        editmode = True
        bpy.ops.object.mode_set()

    objs = bpy.context.selected_editable_objects

    for ob in objs:
        if ob.type == 'MESH':
            mats = ob.material_slots.keys()

            #check the polygons on the mesh to build a list of used materials
            usedMatIndex = []  # we'll store used materials indices here
            faceMats = []
            me = ob.data
            for f in me.polygons:
                #get the material index for this face...
                faceindex = f.material_index

                #indices will be lost: Store face mat use by name
                currentfacemat = mats[faceindex]
                faceMats.append(currentfacemat)

                # check if index is already listed as used or not
                found = 0
                for m in usedMatIndex:
                    if m == faceindex:
                        found = 1
                        #break

                if found == 0:
                #add this index to the list
                    usedMatIndex.append(faceindex)

            #re-assign the used mats to the mesh and leave out the unused
            ml = []
            mnames = []
            for u in usedMatIndex:
                ml.append(mats[u])
                #we'll need a list of names to get the face indices...
                mnames.append(mats[u])

            assignmatslots(ob, ml)

            # restore face indices:
            i = 0
            for f in me.polygons:
                matindex = mnames.index(faceMats[i])
                f.material_index = matindex
                i += 1

    if editmode:
        bpy.ops.object.mode_set(mode='EDIT')


def assign_mat(matname="Default"):
    # get active object so we can restore it later
    actob = bpy.context.active_object

    # check if material exists, if it doesn't then create it
    found = False
    for m in bpy.data.materials:
        if m.name == matname:
            target = m
            found = True
            break
    if not found:
        target = bpy.data.materials.new(matname)

    # if objectmode then set all polygons
    editmode = False
    allpolygons = True
    if actob.mode == 'EDIT':
        editmode = True
        allpolygons = False
        bpy.ops.object.mode_set()

    objs = bpy.context.selected_editable_objects

    for ob in objs:
        # set the active object to our object
        scn = bpy.context.scene
        scn.objects.active = ob

        if ob.type in {'CURVE', 'SURFACE', 'FONT', 'META'}:
            found = False
            i = 0
            for m in bpy.data.materials:
                if m.name == matname:
                    found = True
                    index = i
                    break
                i += 1
                if not found:
                    index = i - 1
            targetlist = [index]
            assignmatslots(ob, targetlist)

        elif ob.type == 'MESH':
            # check material slots for matname material
            found = False
            i = 0
            mats = ob.material_slots
            for m in mats:
                if m.name == matname:
                    found = True
                    index = i
                    #make slot active
                    ob.active_material_index = i
                    break
                i += 1

            if not found:
                index = i
                #the material is not attached to the object
                ob.data.materials.append(target)

            #now assign the material:
            me = ob.data
            if allpolygons:
                for f in me.polygons:
                    f.material_index = index
            elif allpolygons == False:
                for f in me.polygons:
                    if f.select:
                        f.material_index = index
            me.update()

    #restore the active object
    bpy.context.scene.objects.active = actob
    if editmode:
        bpy.ops.object.mode_set(mode='EDIT')


def check_texture(img, mat):
    #finds a texture from an image
    #makes a texture if needed
    #adds it to the material if it isn't there already

    tex = bpy.data.textures.get(img.name)

    if tex is None:
        tex = bpy.data.textures.new(name=img.name, type='IMAGE')

    tex.image = img

    #see if the material already uses this tex
    #add it if needed
    found = False
    for m in mat.texture_slots:
        if m and m.texture == tex:
            found = True
            break
    if not found and mat:
        mtex = mat.texture_slots.add()
        mtex.texture = tex
        mtex.texture_coords = 'UV'
        mtex.use_map_color_diffuse = True


def texface_to_mat():
    # editmode check here!
    editmode = False
    ob = bpy.context.object
    if ob.mode == 'EDIT':
        editmode = True
        bpy.ops.object.mode_set()

    for ob in bpy.context.selected_editable_objects:

        faceindex = []
        unique_images = []

        # get the texface images and store indices
        if (ob.data.uv_textures):
            for f in ob.data.uv_textures.active.data:
                if f.image:
                    img = f.image
                    #build list of unique images
                    if img not in unique_images:
                        unique_images.append(img)
                    faceindex.append(unique_images.index(img))

                else:
                    img = None
                    faceindex.append(None)

        # check materials for images exist; create if needed
        matlist = []
        for i in unique_images:
            if i:
                try:
                    m = bpy.data.materials[i.name]
                except:
                    m = bpy.data.materials.new(name=i.name)
                    continue

                finally:
                    matlist.append(m.name)
                    # add textures if needed
                    check_texture(i, m)

        # set up the object material slots
        assignmatslots(ob, matlist)

        #set texface indices to material slot indices..
        me = ob.data

        i = 0
        for f in faceindex:
            if f is not None:
                me.polygons[i].material_index = f
            i += 1
    if editmode:
        bpy.ops.object.mode_set(mode='EDIT')

def remove_materials():

	for ob in bpy.data.objects:
		print (ob.name)
		try:
			bpy.ops.object.material_slot_remove()
			print ("removed material from " + ob.name)
		except:
			print (ob.name + " does not have materials.")

def CyclesNodeOn():
    mats = bpy.data.materials
    for cmat in mats:
        cmat.use_nodes = True
    bpy.context.scene.render.engine = 'CYCLES'

## Operator Classes ##

class mlrestore(bpy.types.Operator):
    bl_idname = "cycles.restore"
    bl_label = "Restore Cycles"
    bl_description = "Switch Back to Cycles Nodes"
    bl_register = True
    bl_undo = True
    @classmethod
    def poll(cls, context):
        return True
    def execute(self, context):
        CyclesNodeOn()
        return {'FINISHED'}

class SetTransparentBackSide(bpy.types.Operator):
	bl_idname = "material.set_transparent_back_side"
	bl_label = "Transparent back (BI)."
	bl_description = "Creates BI nodes transparently mesh background"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		obj = context.active_object
		if (not obj):
			return False
		mat = context.material
		if (not mat):
			return False
		if (mat.node_tree):
			if (len(mat.node_tree.nodes) == 0):
				return True
		if (not mat.use_nodes):
			return True
		return False

	def execute(self, context):
		mat = context.material
		mat.use_nodes = True
		if (mat.node_tree):
			for node in mat.node_tree.nodes:
				if (node):
					mat.node_tree.nodes.remove(node)
		mat.use_transparency = True
		node_mat = mat.node_tree.nodes.new('ShaderNodeMaterial')
		node_out = mat.node_tree.nodes.new('ShaderNodeOutput')
		node_geo = mat.node_tree.nodes.new('ShaderNodeGeometry')
		node_mat.material = mat
		node_out.location = [node_out.location[0]+500, node_out.location[1]]
		node_geo.location = [node_geo.location[0]+150, node_geo.location[1]-150]
		mat.node_tree.links.new(node_mat.outputs[0], node_out.inputs[0])
		mat.node_tree.links.new(node_geo.outputs[8], node_out.inputs[1])
		return {'FINISHED'}

class MoveMaterialSlotTop(bpy.types.Operator):
	bl_idname = "material.move_material_slot_top"
	bl_label = "Slot to the top"
	bl_description = "Move the active material slots on top"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		obj = context.active_object
		if (not obj):
			return False
		if (len(obj.material_slots) <= 2):
			return False
		if (obj.active_material_index <= 0):
			return False
		return True
	def execute(self, context):
		activeObj = context.active_object
		for i in range(activeObj.active_material_index):
			bpy.ops.object.material_slot_move(direction='UP')
		return {'FINISHED'}

class MoveMaterialSlotBottom(bpy.types.Operator):
	bl_idname = "material.move_material_slot_bottom"
	bl_label = "Slots to the bottom"
	bl_description = "Move the active material slot at the bottom"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		obj = context.active_object
		if (not obj):
			return False
		if (len(obj.material_slots) <= 2):
			return False
		if (len(obj.material_slots)-1 <= obj.active_material_index):
			return False
		return True
	def execute(self, context):
		activeObj = context.active_object
		lastSlotIndex = len(activeObj.material_slots) - 1
		for i in range(lastSlotIndex - activeObj.active_material_index):
			bpy.ops.object.material_slot_move(direction='DOWN')
		return {'FINISHED'}

class MATERIAL_OT_link_to_base_names(bpy.types.Operator):
    bl_idname = "material.link_to_base_names"
    bl_label = "Merge .001, .002 All Objects"
    bl_description = " Replace .001, .002 slots with Original Material/Name on All Materials/Objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for ob in context.scene.objects:
            for slot in ob.material_slots:
                self.fixup_slot(slot)

        return {'FINISHED'}

    def split_name(self, material):
        name = material.name

        if not '.' in name:
            return name, None

        base, suffix = name.rsplit('.', 1)
        try:
            num = int(suffix, 10)
        except ValueError:
            # Not a numeric suffix
            return name, None

        return base, suffix

    def fixup_slot(self, slot):
        if not slot.material:
            return

        base, suffix = self.split_name(slot.material)
        if suffix is None:
            return

        try:
            base_mat = bpy.data.materials[base]
        except KeyError:
            print('Base material %r not found' % base)
            return

        slot.material = base_mat

class VIEW3D_OT_texface_to_material(bpy.types.Operator):
    """Create texture materials for images assigned in UV editor"""
    bl_idname = "view3d.texface_to_material"
    bl_label = "Texface Images to Material/Texture (Material Utils)"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if context.selected_editable_objects:
            texface_to_mat()
            return {'FINISHED'}
        else:
            self.report({'WARNING'},
                        "No editable selected objects, could not finish")
            return {'CANCELLED'}


class VIEW3D_OT_assign_material(bpy.types.Operator):
    """Assign a material to the selection"""
    bl_idname = "view3d.assign_material"
    bl_label = "Assign Material (Material Utils)"
    bl_options = {'REGISTER', 'UNDO'}

    matname = StringProperty(
            name='Material Name',
            description='Name of Material to Assign',
            default="",
            maxlen=63,
            )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        mn = self.matname
        print(mn)
        assign_mat(mn)
        cleanmatslots()
        mat_to_texface()
        return {'FINISHED'}


class VIEW3D_OT_clean_material_slots(bpy.types.Operator):
    """Removes any material slots from selected objects """ \
    """that are not used by the mesh"""
    bl_idname = "view3d.clean_material_slots"
    bl_label = "Clean Material Slots (Material Utils)"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        cleanmatslots()
        return {'FINISHED'}


class VIEW3D_OT_material_to_texface(bpy.types.Operator):
    """Transfer material assignments to UV editor"""
    bl_idname = "view3d.material_to_texface"
    bl_label = "Material Images to Texface (Material Utils)"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        mat_to_texface()
        return {'FINISHED'}

class VIEW3D_OT_material_remove(bpy.types.Operator):
    """Remove all material slots from active objects"""
    bl_idname = "view3d.material_remove"
    bl_label = "Remove All Material Slots (Material Utils)"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        remove_materials()
        return {'FINISHED'}


class VIEW3D_OT_select_material_by_name(bpy.types.Operator):
    """Select geometry with this material assigned to it"""
    bl_idname = "view3d.select_material_by_name"
    bl_label = "Select Material By Name (Material Utils)"
    bl_options = {'REGISTER', 'UNDO'}
    matname = StringProperty(
            name='Material Name',
            description='Name of Material to Select',
            maxlen=63,
            )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        mn = self.matname
        select_material_by_name(mn)
        return {'FINISHED'}


class VIEW3D_OT_replace_material(bpy.types.Operator):
    """Replace a material by name"""
    bl_idname = "view3d.replace_material"
    bl_label = "Replace Material (Material Utils)"
    bl_options = {'REGISTER', 'UNDO'}

    matorg = StringProperty(
            name="Original",
            description="Material to replace",
            maxlen=63,
            )
    matrep = StringProperty(name="Replacement",
            description="Replacement material",
            maxlen=63,
            )
    all_objects = BoolProperty(
            name="All objects",
            description="Replace for all objects in this blend file",
            default=True,
            )
    update_selection = BoolProperty(
            name="Update Selection",
            description="Select affected objects and deselect unaffected",
            default=True,
            )

    # Allow to replace all objects even without a selection / active object
    #@classmethod
    #def poll(cls, context):
    #    return context.active_object is not None

    def draw(self, context):
        layout = self.layout
        layout.prop_search(self, "matorg", bpy.data, "materials")
        layout.prop_search(self, "matrep", bpy.data, "materials")
        layout.prop(self, "all_objects")
        layout.prop(self, "update_selection")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        replace_material(self.matorg, self.matrep, self.all_objects, self.update_selection)
        return {'FINISHED'}


class VIEW3D_OT_fake_user_set(bpy.types.Operator):
    """Enable/disable fake user for materials"""
    bl_idname = "view3d.fake_user_set"
    bl_label = "Set Fake User (Material Utils)"
    bl_options = {'REGISTER', 'UNDO'}

    fake_user = EnumProperty(
            name="Fake User",
            description="Turn fake user on or off",
            items=(('ON', "On", "Enable fake user"),('OFF', "Off", "Disable fake user")),
            default='ON'
            )

    materials = EnumProperty(
            name="Materials",
            description="Which materials of objects to affect",
            items=(('ACTIVE', "Active object", "Materials of active object only"),
                   ('SELECTED', "Selected objects", "Materials of selected objects"),
                   ('SCENE', "Scene objects", "Materials of objects in current scene"),
                   ('USED', "Used", "All materials used by objects"),
                   ('UNUSED', "Unused", "Currently unused materials"),
                   ('ALL', "All", "All materials in this blend file")),
            default='UNUSED'
            )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "fake_user", expand=True)
        layout.prop(self, "materials")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        fake_user_set(self.fake_user, self.materials)
        return {'FINISHED'}


# -----------------------------------------------------------------------------
# menu classes #

class VIEW3D_MT_assign_material(bpy.types.Menu):
    bl_label = "Assign Material"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        for material_name in bpy.data.materials.keys():
            layout.operator("view3d.assign_material",
                text=material_name,
                icon='MATERIAL_DATA').matname = material_name

        layout.operator("view3d.assign_material",
                        text="Add New",
                        icon='ZOOMIN')


class VIEW3D_MT_select_material(bpy.types.Menu):
    bl_label = "Select by Material"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        ob = context.object
        layout.label
        if ob.mode == 'OBJECT':
            #show all used materials in entire blend file
            for material_name, material in bpy.data.materials.items():
                if material.users > 0:
                    layout.operator("view3d.select_material_by_name",
                                    text=material_name,
                                    icon='MATERIAL_DATA',
                                    ).matname = material_name

        elif ob.mode == 'EDIT':
            #show only the materials on this object
            mats = ob.material_slots.keys()
            for m in mats:
                layout.operator("view3d.select_material_by_name",
                    text=m,
                    icon='MATERIAL_DATA').matname = m

class VIEW3D_MT_delete_material(bpy.types.Menu):
    bl_label = "Clean Slots"
    bl_idname = "VIEW3D_MT_delete_material"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.separator()
        layout.label(text = "Selected Object Only")
        layout.operator("view3d.clean_material_slots",
                        text="Clean Material Slots",
                        icon='CANCEL')
        layout.operator("view3d.material_remove",
                        text="Remove Material Slots",
                        icon='CANCEL')
        self.layout.operator("material.link_to_base_names", icon='CANCEL', text="Merge Base Names")

class VIEW3D_MT_master_material(bpy.types.Menu):
	bl_label = "Material Utils Menu"

	def draw(self, context):
	# Cycles
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'
		if context.scene.render.engine == "CYCLES":

			layout.menu("VIEW3D_MT_assign_material", icon='ZOOMIN')
			layout.menu("VIEW3D_MT_select_material", icon='HAND')
			layout.operator("view3d.replace_material",
							text='Replace Material',
							icon='ARROW_LEFTRIGHT')

			layout.separator()
			layout.menu("VIEW3D_MT_delete_material", icon="COLOR_RED")

			layout.separator()
			layout.operator("view3d.fake_user_set",
							text='Set Fake User',
							icon='UNPINNED')

			layout.separator()
			layout.label(text="Switch To Blender Render")
			layout.operator("ml.restore", text='BI Nodes Off', icon='APPEND_BLEND')
			layout.operator("xps_tools.restore_bi_materials_all", text='BI Nodes On', icon='APPEND_BLEND')

	#Blender Internal

		elif context.scene.render.engine == "BLENDER_RENDER":

			layout.menu("VIEW3D_MT_assign_material", icon='ZOOMIN')
			layout.menu("VIEW3D_MT_select_material", icon='HAND')
			layout.operator("view3d.replace_material",
							text='Replace Material',
							icon='ARROW_LEFTRIGHT')

			layout.separator()
			layout.menu("VIEW3D_MT_delete_material", icon="COLOR_RED")

			layout.separator()
			layout.operator("view3d.fake_user_set",
							text='Set Fake User',
							icon='UNPINNED')

			self.layout.separator()
			layout.operator("view3d.material_to_texface",
							text="Material to Texface",
							icon='MATERIAL_DATA')
			layout.operator("view3d.texface_to_material",
							text="Texface to Material",
							icon='TEXTURE_SHADED')
			layout.separator()
			layout.label(text="Switch To Cycles Render")
			layout.operator("ml.refresh_active", text='Convert Active to Cycles', icon='NODE_INSERT_OFF')
			layout.operator("ml.refresh", text='Convert All to Cycles', icon='NODE_INSERT_ON')
			layout.operator("cycles.restore", text='Back to Cycles Nodes', icon='NODETREE')
### Specials Menu's ###

def menu_func(self, context):
# Cycles
    layout = self.layout
    layout.operator_context = 'INVOKE_REGION_WIN'
    if context.scene.render.engine == "CYCLES":
        layout.separator()
        layout.menu("VIEW3D_MT_assign_material", icon='ZOOMIN')
        layout.menu("VIEW3D_MT_select_material", icon='HAND')
        layout.operator("view3d.replace_material",
                        text='Replace Material',
                        icon='ARROW_LEFTRIGHT')

        layout.separator()
        layout.menu("VIEW3D_MT_delete_material", icon="COLOR_RED")

        layout.separator()
        layout.operator("view3d.fake_user_set",
                        text='Set Fake User',
                        icon='UNPINNED')

        layout.separator()
        layout.label(text="Switch To Blender Render")
        layout.operator("ml.restore", text='BI Nodes Off', icon='APPEND_BLEND')
        layout.operator("xps_tools.restore_bi_materials_all", text='BI Nodes On', icon='APPEND_BLEND')
#Blender Internal

    elif context.scene.render.engine == "BLENDER_RENDER":
        layout.separator()
        layout.menu("VIEW3D_MT_assign_material", icon='ZOOMIN')
        layout.menu("VIEW3D_MT_select_material", icon='HAND')
        layout.operator("view3d.replace_material",
                        text='Replace Material',
                        icon='ARROW_LEFTRIGHT')

        layout.separator()
        layout.menu("VIEW3D_MT_delete_material", icon="COLOR_RED")

        layout.separator()
        layout.operator("view3d.fake_user_set",
                        text='Set Fake User',
                        icon='UNPINNED')

        self.layout.separator()
        layout.operator("view3d.material_to_texface",
                        text="Material to Texface",
                        icon='MATERIAL_DATA')
        layout.operator("view3d.texface_to_material",
                        text="Texface to Material",
                        icon='TEXTURE_SHADED')

        self.layout.separator()
        self.layout.operator("material.set_transparent_back_side", icon='TEXTURE_DATA', text="Transparent back (BI)")

        layout.separator()
        layout.label(text="Switch To Cycles Render")
        layout.operator("ml.refresh_active", text='Convert Active to Cycles', icon='NODE_INSERT_OFF')
        layout.operator("ml.refresh", text='Convert All to Cycles', icon='NODE_INSERT_ON')
        layout.operator("cycles.restore", text='Back to Cycles Nodes', icon='NODETREE')

def menu_move(self, context):
# Cycles
    layout = self.layout
    layout.operator_context = 'INVOKE_REGION_WIN'
    if context.scene.render.engine == "CYCLES":

        self.layout.separator()
        self.layout.operator("material.move_material_slot_top", icon='TRIA_UP', text="Slot to top")
        self.layout.operator("material.move_material_slot_bottom", icon='TRIA_DOWN', text="Slot to bottom")

#Blender Internal

    elif context.scene.render.engine == "BLENDER_RENDER":

        self.layout.separator()
        self.layout.operator("material.move_material_slot_top", icon='TRIA_UP', text="Slot to top")
        self.layout.operator("material.move_material_slot_bottom", icon='TRIA_DOWN', text="Slot to bottom")
# -----------------------------------------------------------------------------

# Addons Preferences
class AddonPreferences(bpy.types.AddonPreferences):
	bl_idname = __name__
	
	def draw(self, context):
		layout = self.layout
		layout.label(text="----Materials Specials----")
		layout.label(text="proto type for materials specials")
		layout.label(text="Materials Conversion does not include BI Textures execpt single Image type.")

def register():
    bpy.utils.register_module(__name__)

    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new('wm.call_menu', 'Q', 'PRESS', shift=True)
        kmi.properties.name = "VIEW3D_MT_master_material"
		
    bpy.types.MATERIAL_MT_specials.prepend(menu_move)
    bpy.types.MATERIAL_MT_specials.append(menu_func)

def unregister():

    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps["3D View"]
        for kmi in km.keymap_items:
            if kmi.idname == 'wm.call_menu':
                if kmi.properties.name == "VIEW3D_MT_master_material":
                    km.keymap_items.remove(kmi)
                    break

    bpy.types.MATERIAL_MT_specials.remove(menu_move)
    bpy.types.MATERIAL_MT_specials.remove(menu_func)
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()

