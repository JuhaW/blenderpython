#Needed information for the addon

bl_info = {
    "name": "Mikel007 Addons",
    "author": "Mikel007",
    "version": (1, 0),
    "blender": (2, 73, 0),
    "location": "View3D > Misc",
    "description": "Mikel007 addons",
    "warning": "",
    "wiki_url": "",
    "category": "User Interface"}

#Blender phyton import

import bpy

# Initalisation for the Mikel007 Panel

class MikelsPanel(bpy.types.Panel):

    bl_label = "Mikel007 Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Mikel007"
    
# Draw the buttons

    def draw(self, context):
        
        self.layout.operator("mirror.on")
        self.layout.operator("mirror.off")
        self.layout.operator("subs.on")
        self.layout.operator("subs.off")

# Defintion of the behaviour for the button Mirror on

class OBJECT_OT_Mirroron(bpy.types.Operator):
    bl_label = "Mirror on"
    bl_idname = "mirror.on" # This is the ID Text, very important
    bl_description = "Switch on the Mirror-Modifier of all objects in the viewport" # The description you can see if you move the mouse over the button
    
    def execute(self, context):
        
        for ob in bpy.context.scene.objects:
            for mod in ob.modifiers:
                if mod.type=="MIRROR":
                    mod.show_viewport=True
                    
        return{"FINISHED"}
                
# Defintion of the behaviour for the button Mirror off

class OBJECT_OT_Mirroroff(bpy.types.Operator):
    bl_label = "Mirror off"
    bl_idname = "mirror.off"
    bl_description = "Switch of the Mirror-Modifier of all objects in the viewport"
    
    def execute(self, context):
        
        for ob in bpy.context.scene.objects:
            for mod in ob.modifiers:
                if mod.type=="MIRROR":
                    mod.show_viewport=False
                    
        return{"FINISHED"}

# Defintion of the behaviour for the button Subs on

class OBJECT_OT_Subson(bpy.types.Operator):
    bl_label = "Subs on"
    bl_idname = "subs.on"
    bl_description = "Switch on the Subdivision-Modifier for all objects in the viewport"

    def execute(self, context):
        
        for ob in bpy.context.scene.objects:
            for mod in ob.modifiers:
                if mod.type=="SUBSURF":
                    mod.show_viewport=True
                    
        return{"FINISHED"}


# Defintion of the behaviour for the button Subs off

class OBJECT_OT_Subsoff(bpy.types.Operator):
    bl_label = "Subs off"
    bl_idname = "subs.off"
    bl_description = "Switch off the Subdivision-Modifier of all objects in the viewport"

    def execute(self, context):
        
        for ob in bpy.context.scene.objects:
            for mod in ob.modifiers:
                if mod.type=="SUBSURF":
                    mod.show_viewport=False
                    
        return{"FINISHED"}

        
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
    
    