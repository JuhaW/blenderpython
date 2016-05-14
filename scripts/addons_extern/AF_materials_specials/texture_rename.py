bl_info = {"name": "Texture Renamer", "category": "Material"}

import bpy


class SimpleOp (bpy.types.Operator):
    bl_idname = "object.rename"
    bl_label = "Renamer"

    def execute(self, context):
        for texture in bpy.data.textures:
            if "Texture" in texture.name and texture.type == "IMAGE":
                textname = ""
                for word in bpy.data.textures[texture.name].image.name:
                    if word != ".":
                        textname = textname + word
                    else:
                        break
                texture.name = textname
            if texture.type != "IMAGE":  # rename specific textures as clouds, environnement map,...
                texture.name = texture.type.lower()

        return {'FINISHED'}


class HWPl(bpy.types.Panel):
    #"""Creates a Panel in the scene context of the properties editor"""
    bl_label = "Texture Rename"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "texture"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.rename")


def register():
    bpy.utils.register_class(HWPl)
    bpy.utils.register_class(SimpleOp)


def unregister():
    bpy.utils.unregister_class(HWPl)
    bpy.utils.unregister_class(SimpleOp)

if __name__ == "__main__":
    register()
