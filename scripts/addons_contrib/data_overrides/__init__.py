### BEGIN GPL LICENSE BLOCK #####
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

# <pep8 compliant>

bl_info = {
    "name": "Data Overrides",
    "author": "Lukas Toenne",
    "version": (0, 1),
    "blender": (2, 7, 3),
    "location": "Scene Properties",
    "description": "Override settings and caching for linked objects",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
    }
# Utils
import bpy, time, sys, hashlib
from bpy.types import UILayout
from math import *

def ifloor(x):
    return int(x) if x >= 0.0 else int(x) - 1

def iceil(x):
    return int(x) + 1 if x >= 0.0 else int(x)

# based on http://code.activestate.com/recipes/578114-round-number-to-specified-number-of-significant-di/
def round_sigfigs(num, sig_figs):
    if num != 0:
        return round(num, -int(floor(log10(abs(num))) - (sig_figs - 1)))
    else:
        return 0  # Can't take the log of 0


def data_uuid(id_data, path=""):
    identifier = id_data.name.encode(encoding="utf-8")
    if id_data.library:
        identifier += b'\0' + id_data.library.filepath.encode(encoding="utf-8")
    if path:
        identifier += b'\0' + path.encode(encoding="utf-8")

    m = hashlib.md5()
    m.update(identifier)
    return m.hexdigest(), int.from_bytes(m.digest(), byteorder='big') % 0xFFFFFFFF

_id_collections = [ c.identifier for c in bpy.types.BlendData.bl_rna.properties if isinstance(c, bpy.types.CollectionProperty) and isinstance(c.fixed_type, bpy.types.ID) ]
def _id_data_blocks(blend_data):
    for name in _id_collections:
        coll = getattr(blend_data, name)
        for id_data in coll:
            yield id_data

def find_id_data(blend_data, name, library):
    if library:
        for id_data in _id_data_blocks(blend_data):
            if id_data.library and id_data.library.filepath == library and id_data.name == name:
                return id_data
    else:
        for id_data in _id_data_blocks(blend_data):
            if not id_data.library and id_data.name == name:
                return id_data

def id_data_from_enum(identifier):
    for id_data in _id_data_blocks(bpy.data):
        if str(id_data.as_pointer()) == identifier:
            return id_data

def id_data_enum_item(id_data):
    #identifier, number = id_data_uuid(id_data)
    number = id_data.as_pointer() % 0xFFFFFFFF
    identifier = str(id_data.as_pointer())
    return (identifier, id_data.name, "", UILayout.icon(id_data), number)


class OperatorCallContext():
    def __enter__(self):
        scene = bpy.context.scene
        prefs = bpy.context.user_preferences

        # store active/selected state to restore it after operator execution
        self.curact = scene.objects.active
        self.cursel = { ob : ob.select for ob in scene.objects }
        
        # undo can store files a lot when running operators internally,
        # disable since we only need one undo step after main operators anyway
        self.use_global_undo = prefs.edit.use_global_undo
        prefs.edit.use_global_undo = False

        return (self.curact, self.cursel)
    
    def __exit__(self, exc_type, exc_value, traceback):
        scene = bpy.context.scene
        prefs = bpy.context.user_preferences

        # restore active/selected state
        scene.objects.active = self.curact
        for ob in scene.objects:
            ob.select = self.cursel.get(ob, False)

        prefs.edit.use_global_undo = self.use_global_undo

def select_single_object(ob):
    scene = bpy.context.scene
    
    scene.objects.active = ob
    for tob in scene.objects:
        tob.select = (tob == ob)
# Override
import bpy, os
from bpy.types import Operator, PropertyGroup
from bpy.props import *
from bpy.utils import escape_identifier

# ======================================================================================

class OverrideCustomProperty(PropertyGroup):
    def _value_get(self):
        return self['value']
    def _value_set(self, v):
        self['value'] = v
    def _value_del(self):
        del self['value']
    value = property(_value_get, _value_set, _value_del)

    def reset(self, target):
        try:
            val = eval("target.{}".format(self.name))
        except:
            # TODO define exceptions that should be handled gracefully
            raise
            return
        self['value'] = val

    def apply(self, target):
        val = self['value']
        try:
            eval("target.{} = val".format(self.name))
        except:
            # TODO define exceptions that should be handled gracefully
            raise
            return

class Override(PropertyGroup):
    id_name = StringProperty(name="ID Name", description="Name of the overridden ID datablock")
    id_library = StringProperty(name="ID Library", description="Library file path of the overridden ID datablock")

    show_expanded = BoolProperty(name="Show Expanded", description="Expand override details in the interface", default=True)

    def add_custom_property(self, name):
        prop = self.custom_properties.get(name, None)
        if not prop:
            target = self.find_target(bpy.data)
            if target:
                prop = self.custom_properties.add()
                prop.name = name
                prop.reset(target) # initialize with target value

    def find_target(self, blend_data):
        return find_id_data(blend_data, self.id_name, self.id_library)

    @property
    def label(self):
        return "{}".format(self.id_name)

    def draw_custom_props(self, context, layout):
        for prop in self.custom_properties:
            row = layout.row(align=True)
            row.label(prop.name, icon='DOT')
            row.prop(prop, '["{}"]'.format(escape_identifier("value")), text="")
        
        row = layout.row()
        row.operator_context = 'INVOKE_SCREEN'
        row.context_pointer_set("id_data_override", self)
        row.operator("scene.override_add_custom_property", text="", icon='ZOOMIN')

    def draw(self, context, layout):
        target = self.find_target(context.blend_data)
        if not target:
            return

        split = layout.split(0.05)

        col = split.column()
        col.prop(self, "show_expanded", emboss=False, icon_only=True, icon='TRIA_DOWN' if self.show_expanded else 'TRIA_RIGHT')

        col = split.column()
        icon = bpy.types.UILayout.icon(target)
        col.label(text=self.label, icon_value=icon)

        self.draw_custom_props(context, layout)


def target_library(target):
    id_data = target.id_data
    return id_data.library.filepath if id_data.library else ""

# This name is not human-readable, but is unique and avoids issues with escaping
# when combining file paths and ID names and RNA paths
# For lookup and display in the UI other name/path properties of the override should be used
def target_identifier(target):
    id_data = target.id_data
    try:
        path = target.path_from_id()
    # ValueError is raise when the target type does not support path_from_id
    except ValueError:
        path = ""
    identifier, number = data_uuid(id_data, path)
    return identifier

def find_override(scene, target):
    return scene.overrides.get(target_identifier(target), None)

def add_override(scene, target):
    id_data = target.id_data

    override = scene.overrides.add()
    override.name = target_identifier(target)
    override.id_name = id_data.name
    override.id_library = id_data.library.filepath if id_data.library else ""
    #override.init(target) # TODO

def remove_override(scene, target):
    override = scene.overrides.find(target)
    if override:
        scene.overrides.remove(override)

# ======================================================================================

def register_property_groups():


    Override.custom_properties = CollectionProperty(type=OverrideCustomProperty)


    bpy.types.Scene.overrides = CollectionProperty(type=Override)

def unregister_property_groups():
    del bpy.types.Scene.overrides


# ======================================================================================

def register():
    register_property_groups()

def unregister():
    unregister_property_groups()

import bpy, os
from bpy.types import Operator, Panel, UIList
from bpy.props import *



'''
def id_data_children(id_data):
    if isinstance(id_data, bpy.types.Object):
        if id_data.dupli_type == 'GROUP' and id_data.dupli_group:
            yield id_data.dupli_group
    elif isinstance(id_data, bpy.types.Group):
        for ob in id_data.objects:
            yield ob


def template_id_overrides(layout, context, overrides, id_data, max_level):
    split = layout.split(0.05)

    col = split.column()
    icon = 'DISCLOSURE_TRI_DOWN' if overrides.show_expanded else 'DISCLOSURE_TRI_RIGHT'
    col.prop(overrides, "show_expanded", text="", icon=icon, icon_only=True, emboss=False)

    col = split.column()

    for data, override_type in id_override_targets(id_data):
        col.label(data.path_from_id())

    if max_level <= 0 or max_level > 1:
        for id_child in id_data_children(id_data):
            template_id_overrides(col, context, overrides, id_child, max_level-1)


def template_overrides(layout, context, localroot, max_level=0):
    overrides = localroot.overrides
    for id_child in id_data_children(localroot):
        template_id_overrides(layout, context, overrides, id_child, max_level)

class OBJECT_PT_SimulationOverrides(Panel):
    """Simulation Overrides"""
    bl_label = "Simulation Overrides"
    bl_idname = "OBJECT_PT_SimulationOverrides"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        ob = context.object

        box = layout.box()
        template_overrides(box, context, ob)
'''


class SCENE_OT_Override_Add(Operator):
    """Add Datablock Override"""
    bl_idname = "scene.override_add"
    bl_label = "Add Override"
    bl_property = "id_block"

    def id_block_items(self, context):
        return [id_data_enum_item(id_data) for id_data in bpy.data.objects]

    id_block = EnumProperty(name="ID", description="ID datablock for which to add overrides", items=id_block_items)

    def invoke(self, context, evemt):
        context.window_manager.invoke_search_popup(self)
        return {'CANCELLED'}

    def execute(self, context):
        scene = context.scene

        id_data = id_data_from_enum(self.id_block)
        add_override(scene, id_data)
        
        return {'FINISHED'}


class SCENE_OT_Override_AddCustomProperty(Operator):
    """Add Custom Property Override"""
    bl_idname = "scene.override_add_custom_property"
    bl_label = "Add Custom Property Override"
    bl_options = {'REGISTER', 'UNDO'}

    propname = StringProperty(name="Property", description="Path to the custom property to override")

    @classmethod
    def poll(cls, context):
        if not context.scene:
            return False
        if not hasattr(context, "id_data_override"):
            return False
        return True

    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)

    def execute(self, context):
        print("AAAAAA")
        scene = context.scene
        override = context.id_data_override

        if not self.propname:
            print("no propname?")
            return {'CANCELLED'}

        print("adding %s" % self.propname)
        override.add_custom_property(self.propname)
        return {'FINISHED'}

def template_overrides(layout, context, scene):
    for override in scene.overrides:
        override.draw(context, layout)


class SCENE_PT_Overrides(Panel):
    """Scene Overrides"""
    bl_label = "Scene Overrides"
    bl_idname = "SCENE_PT_Overrides"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.operator("scene.override_add")

        box = layout.box()
        template_overrides(box, context, scene)


# ======================================================================================


def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
