
bl_info = {
        "name": "Areatype Split (3D View/UV Editor)",
        "description":"This example adds a button which toggles a split of an area with another.",
        "author":"dustractor@gmail.com",
        "version":(0,1),
        "blender":(2,65,0),
        "location":"Prepended to the header of the viewport.",
        "warning":"",
        "wiki_url":"",
        "category": "System"
        }

import bpy
from .utils import AddonPreferences, SpaceProperty

class AREATYPE_OT_split(bpy.types.Operator):
    bl_idname = "areatype.splitview"
    bl_label = "areatype.splitview"
    def execute(self,context):
        thisarea = context.area
        otherarea = None
        tgxvalue = thisarea.x + thisarea.width + 1
        thistype = context.area.type
        arealist = list(context.screen.areas)
        for area in context.screen.areas:
            if area == thisarea:
                continue
            elif area.x == tgxvalue and area.y == thisarea.y:
                otherarea = area
                break
        if otherarea:
            bpy.ops.screen.area_join(min_x=thisarea.x,min_y=thisarea.y,max_x=otherarea.x,max_y=otherarea.y)
            bpy.ops.screen.screen_full_area()
            bpy.ops.screen.screen_full_area()
            return {"FINISHED"}
        else:
            context.area.type = "IMAGE_EDITOR"
            areax = None
            bpy.ops.screen.area_split(direction="VERTICAL")
            for area in context.screen.areas:
                if area not in arealist:
                    areax = area
                    break
            if areax:
                areax.type = thistype
                return {"FINISHED"}
        return {"CANCELLED"}


def viewdraw(self,context):
    layout = self.layout
    layout.operator("areatype.splitview",text="",icon="COLOR_BLUE")

import bpy

class AREATYPE_OT_switch(bpy.types.Operator):
    bl_idname = "areatype.switch"
    bl_label = "areatype.switch"
    switchto = bpy.props.StringProperty()
    def execute(self,context):
        context.area.type = self.switchto
        return {"FINISHED"}

def timedraw(self,context):
    layout = self.layout
    layout.operator("areatype.switch",text="",icon="NODETREE").switchto = "NODE_EDITOR"

def nodedraw(self,context):
    layout = self.layout
    layout.operator("areatype.switch",text="",icon="TIME").switchto = "TIMELINE"

classes = [
    AREATYPE_OT_split,
    AREATYPE_OT_switch,
    ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_HT_header.prepend(viewdraw)
    bpy.types.TIME_HT_header.prepend(timedraw)
    bpy.types.NODE_HT_header.prepend(nodedraw)



def unregister():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_HT_header.remove(viewdraw)
    bpy.types.TIME_HT_header.remove(timedraw)
    bpy.types.NODE_HT_header.remove(nodedraw)

if __name__ == "__main__":
    register()	

