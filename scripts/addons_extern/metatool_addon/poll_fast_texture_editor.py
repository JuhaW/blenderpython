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

# <pep8 compliant>
#

##########################################################################################################################################
##########################################################################################################################################
##############  Fast Textures Editor  ####################################################################################################
##############  Fast Textures Editor  ####################################################################################################


# bl_info = {
#    "name": "Fast Textures Editor",
#    "author": "Alfonso Annarumma",
#    "version": (0, 1),
#    "blender": (2, 70),
#    "location": "Proprieties > Scene > Fast Textures Editor",
#    "warning": "",
#    "description": "Fast Edit Texture",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "User Changed"}

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

import bpy

from bpy.props import StringProperty, BoolProperty, CollectionProperty, EnumProperty

#EDIT = {"EDIT_MESH", "EDIT_CURVE", "EDIT_SURFACE", "EDIT_METABALL", "EDIT_TEXT", "EDIT_ARMATURE"}


# Sub Location
class SubLoc_PathTEX():
    """Fast Textures Editor"""
    bl_category = "TEX"
    bl_region_type = 'TOOLS'
    #bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    COMPAT_ENGINES = {'BLENDER_RENDER', 'BLENDER_GAME'}

    @classmethod
    def poll(cls, context):
        return context.scene.osc_pathtex and context.mode == ('OBJECT')


# Sub Panel
class FastTexturesEditorPanel(SubLoc_PathTEX, bpy.types.Panel):
    """Rename directory path of multiply file"""
    bl_label = "[TEXTURE]"
    bl_idname = "fast_textures_layout"

    #bpy.types.Scene.ImageThree= BoolProperty(name="Show images link", default=False)
    #@classmethod
    # def poll(cls, context):
    # An exception, don't call the parent poll func because
    # this manages materials for all engine types

    #engine = context.scene.render.engine
    # return (context.material or context.object) and (engine in cls.COMPAT_ENGINES)

    def draw(self, context):

        scene = context.scene
        object = context.active_object

        # variabili
        material = object.active_material
        textures = bpy.data.textures
        layout = self.layout

        row1 = layout.row()
        row1.operator("view3d.assign_material", text="Use Material & Image Texture")

        row1 = layout.row()
        row1.label(text="> " + material.name + " of " + object.name)

        # prima riga, pulsante per il refresh

    ########################################
        i = 0
      # per ogni cartella che si trova nella lista elenco le opzioni per il rename
        for texture_slot in material.texture_slots:

            # variabili
            #texture = textures[texture_slot.name]

            if texture_slot and texture_slot.name == "":
                material.texture_slots.clear(i)

            # bpy.data.textures.remove(texture)

            if texture_slot and texture_slot.name != "":

                row = layout.row(align=True)
                col = row.column(align=True)

                col.label(text="slot" + str(i))
                row = layout.row(align=True)

                row.template_ID(texture_slot, "texture", new="texture.new")

                row = layout.row(align=True)
                row.prop(texture_slot, "texture_coords", text="")
                row = layout.row(align=True)
                if texture_slot.name != "":
                    if texture_slot.texture_coords == 'UV':

                        row.prop_search(texture_slot, "uv_layer", object.data, "uv_textures", text="")
                        row = layout.row(align=True)

            col = row.column(align=True)

            col.scale_x = 2

            col.prop(texture_slot, "use_map_color_diffuse", text="Color")
            col.prop(texture_slot, "use_map_specular", text="Specular")

            col = row.column(align=True)

            col.scale_x = 2

            col.prop(texture_slot, "use_map_normal", text="Bump")
            col.prop(texture_slot, "use_map_alpha", text="Alpha")

            col = row.column(align=True)
            row = layout.row(align=True)

            if texture_slot.use_map_normal:

                col = row.column(align=True)
                col.scale_x = 2
                col.prop(texture_slot.texture, "use_normal_map", text="Normal Map")
                col.prop(texture_slot, "normal_map_space", text="")

            col = row.column(align=True)
            row = layout.row(align=True)

            if texture_slot.use_map_specular:

                col.scale_x = 3
                col.prop(texture_slot, "use_rgb_to_intensity", text="RGB to intensy")
                col.prop(texture_slot, "color", text="")

            i = i + 1
        #row = layout.row(align=True)
        # row.label(text="fine")


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.register_module(__name__)


if __name__ == "__main__":
    register()
