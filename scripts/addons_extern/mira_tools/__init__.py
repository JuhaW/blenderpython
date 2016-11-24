# BEGIN GPL LICENSE BLOCK #####
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
# END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Mira Tools",
    "author": "Paul Geraskin, Marvin K. Breuer",
    "version": (0, 4, 0),
    "blender": (2, 78, 0),
    "location": "3D Viewport",
    "description": "Mira Tools",
    "warning": "",
    "wiki_url": "https://github.com/mifth/mifthtools/wiki/Mira-Tools",
    "tracker_url": "https://github.com/mifth/mifthtools/issues",
    "category": "ToolPlus"}


#ui compact
from mira_tools.mi_gui_compact import (VIEW3D_MIRA_Panel_TOOLS)
from mira_tools.mi_gui_compact import (VIEW3D_MIRA_Panel_UI)

#ui main
from mira_tools.mi_gui_main import (MI_ModifyPanel_TOOLS)
from mira_tools.mi_gui_main import (MI_ModifyPanel_UI)

from mira_tools.mi_gui_main import (MI_DeformPanel_TOOLS)
from mira_tools.mi_gui_main import (MI_DeformPanel_UI)

from mira_tools.mi_gui_main import (MI_SettingsPanel_TOOLS)
from mira_tools.mi_gui_main import (MI_SettingsPanel_UI)

from mira_tools.mi_gui_main import register_icons, unregister_icons


if "bpy" in locals():
    import imp
    imp.reload(mi_curve_test)
    imp.reload(mi_curve_stretch)
    imp.reload(mi_curve_surfaces)
    imp.reload(mi_settings)
    imp.reload(mi_noise)
    imp.reload(mi_deform)
    imp.reload(mi_linear_deformer)
    imp.reload(mi_curve_guide)
    imp.reload(mi_draw_extrude)
    imp.reload(mi_poly_loop)
    imp.reload(mi_batch)

else:
    from . import mi_curve_test
    from . import mi_curve_stretch
    from . import mi_curve_surfaces
    from . import mi_settings
    from . import mi_linear_deformer
    from . import mi_curve_guide
    from . import mi_deform
    from . import mi_noise
    from . import mi_draw_extrude
    from . import mi_poly_loop
    from . import mi_batch


import bpy, os
from bpy.props import *

import rna_keymap_ui

from bpy import*
from bpy.types import AddonPreferences, PropertyGroup


def update_panel_position_cmp(self, context):
    try:
        bpy.utils.unregister_class(VIEW3D_MIRA_Panel_UI)        
        bpy.utils.unregister_class(VIEW3D_MIRA_Panel_TOOLS)        
    except:
        pass    
    try:
        bpy.utils.unregister_class(VIEW3D_MIRA_Panel_UI)
    except:
        pass
        
    if context.user_preferences.addons[__name__].preferences.tab_location_cmp == 'tools':        

        VIEW3D_MIRA_Panel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_cmp       
        bpy.utils.register_class(VIEW3D_MIRA_Panel_TOOLS)

    if context.user_preferences.addons[__name__].preferences.tab_location_cmp == 'ui':        
        bpy.utils.register_class(VIEW3D_MIRA_Panel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location_cmp == 'off':
        pass      



def update_panel_position_main(self, context):
    try:
        bpy.utils.unregister_class(MI_ModifyPanel_UI)
        bpy.utils.unregister_class(MI_DeformPanel_UI)
        bpy.utils.unregister_class(MI_SettingsPanel_UI)
        
        bpy.utils.unregister_class(MI_ModifyPanel_TOOLS)
        bpy.utils.unregister_class(MI_DeformPanel_TOOLS)
        bpy.utils.unregister_class(MI_SettingsPanel_TOOLS)
        
    except:
        pass
    
    try:
        bpy.utils.unregister_class(MI_ModifyPanel_UI)
        bpy.utils.unregister_class(MI_DeformPanel_UI)
        bpy.utils.unregister_class(MI_SettingsPanel_UI)

    except:
        pass
    
    if context.user_preferences.addons[__name__].preferences.tab_location_main == 'tools':
        
        MI_ModifyPanel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_main
        MI_DeformPanel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_main
        MI_SettingsPanel_TOOLS.bl_category = context.user_preferences.addons[__name__].preferences.tools_category_main
       
        bpy.utils.register_class(MI_ModifyPanel_TOOLS)
        bpy.utils.register_class(MI_DeformPanel_TOOLS)
        bpy.utils.register_class(MI_SettingsPanel_TOOLS)

    if context.user_preferences.addons[__name__].preferences.tab_location_main == 'ui':
        bpy.utils.register_class(MI_ModifyPanel_UI)
        bpy.utils.register_class(MI_DeformPanel_UI)
        bpy.utils.register_class(MI_SettingsPanel_UI)

    if context.user_preferences.addons[__name__].preferences.tab_location_main == 'off':
        pass



#Panel preferences
class TP_Panels_Preferences(AddonPreferences):
    bl_idname = __name__
    
    key_inputs = EnumProperty(
        name = "Key Inputs Style",
        items = (('Blender', 'Blender', ''),
                ('Maya', 'Maya', '')
                ),
        default = 'Blender')


    prefs_tabs = EnumProperty(
        items=(('info',       "Info",       "Info"),
               ('location',   "Location",   "Location"),
               ('keymap',     "Keymap",     "Keymap"),
               ('url',        "URLs",       "URLs")),
               default='info')

    #Tab Location           
    tab_location_cmp = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off Shelf', 'disable panel')),
               default='off', update = update_panel_position_cmp)

    tab_location_main = EnumProperty(
        name = 'Panel Location',
        description = 'save user settings and restart blender after switching the panel location',
        items=(('tools', 'Tool Shelf', 'place panel in the tool shelf [T]'),
               ('ui', 'Property Shelf', 'place panel in the property shelf [N]'),
               ('off', 'Off Shelf', 'disable panel')),
               default='tools', update = update_panel_position_main)


    tools_category_cmp = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Mira', update = update_panel_position_cmp)
    tools_category_main = StringProperty(name = "TAB Category", description = "add name for a new category tab", default = 'Mira', update = update_panel_position_main)


    def draw(self, context):
        layout = self.layout
        
        #Info
        row= layout.row(align=True)
        row.prop(self, "prefs_tabs", expand=True)
       
        if self.prefs_tabs == 'info':
            box = layout.box()
          
            row = box.row(1)            
            row.label(text="Welcome to MiraTools!")

            row = box.column(1)
            row.label(text="This addon includes modern modeling and retopology tools.")
            row.label(text="They allows you to create, deform and drawing mesh")
            row.label(text="Have Fun! :) ")

        #Location
        if self.prefs_tabs == 'location':
            box = layout.box()
          
            row = box.row(1)  
            row.label("Location Main: ")
            
            row = box.row(1)  
            row.prop(self, 'tab_location_main', expand=True)

            if self.tab_location_main == 'tools':

                row = box.row(1)                  
                row.prop(self, "tools_category_main")

            box.separator()
            
            row = box.row(1)  
            row.label("Location Compact: ")
            
            row = box.row(1)  
            row.prop(self, 'tab_location_cmp', expand=True)

            if self.tab_location_cmp == 'tools':

                row = box.row(1)                  
                row.prop(self, "tools_category_cmp")
            

            box.separator()
            
            row = box.row(1) 
            row.label(text="please restart blender after changing the panel location", icon ="INFO")       
         

        #Keymap
        if self.prefs_tabs == 'keymap':
            box = layout.box()
                    
            col = box.column()
            kc = bpy.context.window_manager.keyconfigs.addon
            for km, kmi in addon_keymaps:
                km = km.active()
                col.context_pointer_set("keymap", km)
                rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)
            
            col.separator()
           
            row = box.column(1)  
            row.label("Keys can not be changed here permanently", icon ="TRIA_RIGHT")
            row.label("Therefore go to TAB Input", icon ="TRIA_RIGHT")
            row.label("Search by Name: Mira", icon ="TRIA_RIGHT")
            row.label("Set new Key > Save User Settings", icon ="TRIA_RIGHT")
            
            row = box.row(1)  
            row.operator('wm.url_open', text = 'Key Type', icon = 'FILE_TEXT').url = "https://lh3.googleusercontent.com/2QbM8LeV-F6vie4q1q6wIMFXkzq1s8cB6EkyzLBbBNPHy8v7LtcqnGz4ad7DncopwBijbXlELnEp8UB27jbjXwanVey-KnC-HWfcOA6lq-wOSvBIruHBno-AH-tqOFESrl7xqzQKspkynMC8Tcvoo0QVHPhMesaFqnKKZwyohW1UJPurQmTnjgk6CbWRhJMeUlAgL3-lhKPSgXmDi3lkEFmYlmvcqD4ImoHexcUZ8WsbV8EBCnSyrFe9sxZP2y6GtYkCmiBqP8dTAhIJU27wI0iu7tiVIyGlagPP-UwjeXfPFaYVTu6Worts4jII5W_8st6xIEDdk6fVo6f8pN5GQsIvbEWsOiVKcT_yarWXsfU3jRm2IzAm48eac5_-qOWaSZRM5dW6sxHDfQOcreL7wzw2HQ96NKULyDlXplZ8NYZM3n1LnJmT24zN0od3nCgk88IB07FIsfgsLFrrzS1PftlqQqhBFhNOwbrfhpLou-LFGv79A_w4Ulk8FMjCQ3E2gLGTZhvcOLBAcheW4yqqeRjeSAslg19RKsiT5CDCVfL7HLQrbgpz3u1vdi9GY43gEf397s1QFAvYOk_ecYMKoGsP3uslEXhfWdk_gn0VvwGIyubU=w521-h955-no"
            row.operator('wm.url_open', text = 'recommend: is key free addon', icon = 'PLUGIN').url = "https://github.com/Antonioya/blender/tree/master/iskeyfree"
            
        #Weblinks
        if self.prefs_tabs == 'url':
            box = layout.box()
          
            row = box.row(1)
            row.operator('wm.url_open', text = 'Wiki', icon = 'HELP').url = "https://github.com/mifth/mifthtools/wiki/Mira-Tools"
            row.operator('wm.url_open', text = 'Issues', icon = 'ERROR').url = "https://github.com/mifth/mifthtools/issues"
            row.operator('wm.url_open', text = 'Thread', icon = 'BLENDER').url = "http://blenderartists.org/forum/showthread.php?366107-MiraTools"



class DropdownMiraToolProps(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.mirawindow
    """

    display_mirastretch = bpy.props.BoolProperty(name="Curve Stretch", description="UI Curve Stretch Tools", default=False)
    display_mirasface = bpy.props.BoolProperty(name="Curve Surface", description="UI Curve Surface Tools", default=False)
    display_miraguide = bpy.props.BoolProperty(name="Curve Guide", description="UI Curve Guide Tools", default=False)
    display_miramodify = bpy.props.BoolProperty(name="Modify Tools", description="UI Modify Tools", default=False)
    display_miradeform = bpy.props.BoolProperty(name="Deform Tools", description="UI Deform Tools", default=False)
    display_miraextrude = bpy.props.BoolProperty(name="Draw Extrude", description="UI Draw Extrude", default=False)
    display_mirasettings = bpy.props.BoolProperty(name="Settings", description="UI Settings", default=False)
    display_help = bpy.props.BoolProperty(name="Help", description="Open/Close Help", default=False)




# This allows you to right click on a button and link to the manual / see templates
def miratool_manual_map():
    url_manual_prefix = "https://blenderartists.org/forum/showthread.php?366107-MiraTools"
    url_manual_mapping = (
        ("bpy.ops.mira.curve_stretch", "MiraTool-Wiki"),               
        ("bpy.ops.mira.curve_guide", "MiraTool-Wiki"),               
        ("bpy.ops.mira.poly_loop", "MiraTool-Wiki"),               
        ("bpy.ops.mira.curve_surfaces", "MiraTool-Wiki"),               
        ("bpy.ops.mira.draw_extrude", "MiraTool-Wiki"),               
        ("bpy.ops.mira.noise", "MiraTool-Wiki"),               
        ("bpy.ops.mira.deformer", "MiraTool-Wiki"),               
        ("bpy.ops.mira.linear_deformer", "MiraTool-Wiki"),               
        )
    return url_manual_prefix, url_manual_mapping



# register

addon_keymaps = []

def register():  
    register_icons()
    
    bpy.utils.register_module(__name__)

    bpy.types.Scene.mi_settings = PointerProperty(
        name="Global Settings",
        type=mi_settings.MI_Settings,
        description="Global Settings."
    )

    bpy.types.Scene.mi_cur_stretch_settings = PointerProperty(
        name="Curve Stretch Settings",
        type=mi_curve_stretch.MI_CurveStretchSettings,
        description="Curve Stretch Settings."
    )

    bpy.types.Scene.mi_cur_surfs_settings = PointerProperty(
        name="Curve Surfaces Settings",
        type=mi_curve_surfaces.MI_CurveSurfacesSettings,
        description="Curve Surfaces Settings."
    )

    bpy.types.Scene.mi_extrude_settings = PointerProperty(
        name="Extrude Variables",
        type=mi_draw_extrude.MI_ExtrudeSettings,
        description="Extrude Settings"
    )

    bpy.types.Scene.mi_ldeformer_settings = PointerProperty(
        name="Linear Deformer Variables",
        type=mi_linear_deformer.MI_LDeformer_Settings,
        description="Linear Deformer Settings"
    )

    bpy.types.Scene.mi_curguide_settings = PointerProperty(
        name="Curve Guide Variables",
        type=mi_curve_guide.MI_CurGuide_Settings,
        description="Curve Guide Settings"
    )

    # alternative gui
    bpy.types.WindowManager.mirawindow = bpy.props.PointerProperty(type = DropdownMiraToolProps)
    #bpy.types.WindowManager.mirawindow = bpy.props.PointerProperty(type = mi_gui.DropdownMiraToolProps)


    #kEYMAP#
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        
#KEY Change                                      # -vvv-  add a new type of event here...    
    kmi = km.keymap_items.new('tp_ops.miratools', 'BACK_SLASH', 'PRESS') #, ctrl=True, shift=True, alt=True)  

    kmi.active = True
    addon_keymaps.append((km, kmi))

    bpy.utils.register_manual_map(miratool_manual_map)
        
    update_panel_position_cmp(None, bpy.context)
    update_panel_position_main(None, bpy.context)



def unregister():
    import bpy

    #del bpy.types.Scene.miraTool
    #del bpy.types.Object.mi_curves  # need to investigate if i need to delete it
    del bpy.types.Scene.mi_settings
    del bpy.types.Scene.mi_cur_stretch_settings
    del bpy.types.Scene.mi_cur_surfs_settings
    del bpy.types.Scene.mi_extrude_settings
    del bpy.types.Scene.mi_ldeformer_settings
    del bpy.types.Scene.mi_curguide_settings

    del bpy.types.WindowManager.mirawindow

    bpy.utils.unregister_module(__name__)

    unregister_icons()

    bpy.utils.unregister_manual_map(miratool_manual_map)

    #kEYMAP#
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)        
    addon_keymaps.clear()  


if __name__ == "__main__":
    register()




