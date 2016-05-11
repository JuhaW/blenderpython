bl_info = {
    "name": "Mask Tools",
    "author": "Yigit Savtur",
    "version": (0, 1),
    "blender": (2, 7, 4),
    "location": "3d View > Tool shelf > Sculpt",
    "description": "Tools for Converting Sculpt Masks to Vertex groups",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Sculpting"}

import bpy
import maskToVGroup
import vgroupToMask

maskToVGroup.register()
vgroupToMask.register()

class MaskToolsPanel(bpy.types.Panel):
    """Creates a Mask Tool Box in the Viewport Tool Panel"""
    bl_category = "Sculpt"
    bl_label = "Mask Tools"
    bl_idname = "MESH_OT_masktools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'


    def draw(self, context):
        layout = self.layout

        vgroupHeader = layout.row(align = True)
        vgroupHeader.label(text = "Vertex Group :", icon = 'GROUP_VERTEX')
        
        vGroupButtons = layout.row()
        vGroupButtons.operator("mesh.masktovgroup", text = "Create VGroup", icon = 'GROUP_VERTEX')
        vGroupButtons.operator("mesh.masktovgroup_append", text = "Add", icon = 'DISCLOSURE_TRI_RIGHT')
        vGroupButtons.operator("mesh.masktovgroup_remove", text = "Remove", icon = 'DISCLOSURE_TRI_DOWN')
        
        space = layout.row()
        
        maskHeader = layout.row(align = True)
        maskHeader.label(text = "Mask :", icon = 'MOD_MASK')
        
        maskButtons = layout.row()
        maskButtons.operator("mesh.vgrouptomask", text = "Create Mask", icon='MOD_MASK')
        maskButtons.operator("mesh.vgrouptomask_append", text = "Add", icon = 'DISCLOSURE_TRI_RIGHT')
        maskButtons.operator("mesh.vgrouptomask_remove", text = "Remove", icon = 'DISCLOSURE_TRI_DOWN')


def register():
    bpy.utils.register_module(__name__)

	
def unregister():
    bpy.utils.unregister_module(__name__)
	
	
if __name__ == "__main__" :
	register()
