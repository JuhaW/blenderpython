bl_info = {
    "name": "Edit Addon Source",
    "author": "scorpion81",
    "version": (0, 2),
    "blender": (2, 69, 0),
    "location": "User Preferences > Addons > Addon > Edit Source",
    "description": "Allows to open addon sources with one click in internal or external editor",
    "warning": "",
    "wiki_url": "",
    "category": "Development"}


import bpy
from bpy.types import Operator, USERPREF_PT_addons, AddonPreferences
from bpy.props import StringProperty

class EditAddonSourcePreferences(AddonPreferences):
    # this must match the addon name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __name__

    external_editor = StringProperty(
            name="External Editor",
            subtype='FILE_PATH',
            )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "external_editor")                     

def draw(self, context):
        import os
        import addon_utils

        layout = self.layout

        userpref = context.user_preferences
        used_ext = {ext.module for ext in userpref.addons}

        userpref_addons_folder = os.path.join(userpref.filepaths.script_directory, "addons")
        scripts_addons_folder = bpy.utils.user_resource('SCRIPTS', "addons")

        # collect the categories that can be filtered on
        addons = [(mod, addon_utils.module_bl_info(mod)) for mod in addon_utils.modules(refresh=False)]

        split = layout.split(percentage=0.2)
        col = split.column()
        col.prop(context.window_manager, "addon_search", text="", icon='VIEWZOOM')

        col.label(text="Supported Level")
        col.prop(context.window_manager, "addon_support", expand=True)

        col.label(text="Categories")
        col.prop(context.window_manager, "addon_filter", expand=True)

        col = split.column()

        # set in addon_utils.modules_refresh()
        if addon_utils.error_duplicates:
            self.draw_error(col,
                            "Multiple addons using the same name found!\n"
                            "likely a problem with the script search path.\n"
                            "(see console for details)",
                            )

        if addon_utils.error_encoding:
            self.draw_error(col,
                            "One or more addons do not have UTF-8 encoding\n"
                            "(see console for details)",
                            )

        filter = context.window_manager.addon_filter
        search = context.window_manager.addon_search.lower()
        support = context.window_manager.addon_support

        # initialized on demand
        user_addon_paths = []

        for mod, info in addons:
            module_name = mod.__name__

            is_enabled = module_name in used_ext

            if info["support"] not in support:
                continue

            # check if addon should be visible with current filters
            if ((filter == "All") or
                (filter == info["category"]) or
                (filter == "Enabled" and is_enabled) or
                (filter == "Disabled" and not is_enabled) or
                (filter == "User" and (mod.__file__.startswith((scripts_addons_folder, userpref_addons_folder))))
                ):

                if search and search not in info["name"].lower():
                    if info["author"]:
                        if search not in info["author"].lower():
                            continue
                    else:
                        continue

                # Addon UI Code
                col_box = col.column()
                box = col_box.box()
                colsub = box.column()
                row = colsub.row()

                row.operator("wm.addon_expand", icon='TRIA_DOWN' if info["show_expanded"] else 'TRIA_RIGHT', emboss=False).module = module_name

                sub = row.row()
                sub.active = is_enabled
                sub.label(text='%s: %s' % (info["category"], info["name"]))
                if info["warning"]:
                    sub.label(icon='ERROR')

                # icon showing support level.
                sub.label(icon=self._support_icon_mapping.get(info["support"], 'QUESTION'))

                if is_enabled:
                    row.operator("wm.addon_disable", icon='CHECKBOX_HLT', text="", emboss=False).module = module_name
                else:
                    row.operator("wm.addon_enable", icon='CHECKBOX_DEHLT', text="", emboss=False).module = module_name

                # Expanded UI (only if additional info is available)
                if info["show_expanded"]:
                    if info["description"]:
                        split = colsub.row().split(percentage=0.15)
                        split.label(text="Description:")
                        split.label(text=info["description"])
                    if info["location"]:
                        split = colsub.row().split(percentage=0.15)
                        split.label(text="Location:")
                        split.label(text=info["location"])
                    if mod:
                        split = colsub.row().split(percentage=0.15)
                        split.label(text="File:")
                        split.label(text=mod.__file__, translate=False)
                    if info["author"]:
                        split = colsub.row().split(percentage=0.15)
                        split.label(text="Author:")
                        split.label(text=info["author"], translate=False)
                    if info["version"]:
                        split = colsub.row().split(percentage=0.15)
                        split.label(text="Version:")
                        split.label(text='.'.join(str(x) for x in info["version"]), translate=False)
                    if info["warning"]:
                        split = colsub.row().split(percentage=0.15)
                        split.label(text="Warning:")
                        split.label(text='  ' + info["warning"], icon='ERROR')

                    user_addon = USERPREF_PT_addons.is_user_addon(mod, user_addon_paths)
                    tot_row = bool(info["wiki_url"]) + bool(user_addon)

                    if tot_row:
                        split = colsub.row().split(percentage=0.15)
                        split.label(text="Internet:")
                        if info["wiki_url"]:
                            split.operator("wm.url_open", text="Documentation", icon='HELP').url = info["wiki_url"]
                        tracker_url = "http://developer.blender.org/maniphest/task/create/?project=3&type=Bug"
                        split.operator("wm.url_open", text="Report a Bug", icon='URL').url = tracker_url
                        if user_addon:
                            split.operator("wm.addon_remove", text="Remove", icon='CANCEL').module = mod.__name__
                            
                        #THE NEW OPERATOR....
                        split.operator("wm.addon_edit", text="Edit Source", icon='TEXT').module = mod.__name__

                        for i in range(4 - tot_row):
                            split.separator()

                    # Show addon user preferences
                    if is_enabled:
                        addon_preferences = userpref.addons[module_name].preferences
                        if addon_preferences is not None:
                            draw = getattr(addon_preferences, "draw", None)
                            if draw is not None:
                                addon_preferences_class = type(addon_preferences)
                                box_prefs = col_box.box()
                                box_prefs.label("Preferences:")
                                addon_preferences_class.layout = box_prefs
                                try:
                                    draw(context)
                                except:
                                    import traceback
                                    traceback.print_exc()
                                    box_prefs.label(text="Error (see console)", icon='ERROR')
                                del addon_preferences_class.layout

        # Append missing scripts
        # First collect scripts that are used but have no script file.
        module_names = {mod.__name__ for mod, info in addons}
        missing_modules = {ext for ext in used_ext if ext not in module_names}

        if missing_modules and filter in {"All", "Enabled"}:
            col.column().separator()
            col.column().label(text="Missing script files")

            module_names = {mod.__name__ for mod, info in addons}
            for module_name in sorted(missing_modules):
                is_enabled = module_name in used_ext
                # Addon UI Code
                box = col.column().box()
                colsub = box.column()
                row = colsub.row()

                row.label(text=module_name, translate=False, icon='ERROR')

                if is_enabled:
                    row.operator("wm.addon_disable", icon='CHECKBOX_HLT', text="", emboss=False).module = module_name

class WM_OT_addon_edit(Operator):
    "Edit the addon source files"
    bl_idname = "wm.addon_edit"
    bl_label = "Edit Addon Files"

    module = StringProperty(
            name="Module",
            description="Module name of the addon to edit",
            )

    def load_sources(self, context, filepaths):
        import subprocess

        user_preferences = context.user_preferences
        addon_prefs = user_preferences.addons[__name__].preferences
        text_editor = addon_prefs.external_editor #context.user_preferences.filepaths.text_editor

        if not text_editor:
            for path in filepaths:
                bpy.data.texts.load(path)
                self.report({'INFO'}, "Loaded source file: %r" % path)
             
            return {'FINISHED'}

        else:
            cmd = [text_editor] + filepaths
    
            try:
                subprocess.Popen(cmd)
            except:
                import traceback
                traceback.print_exc()
                self.report({'ERROR'},
                            "Text editor not found, "
                            "please specify in Addon Preferences > External Editor")
                return {'CANCELLED'}

            return {'FINISHED'}
    
    @staticmethod
    def path_from_addon(module):
        import os
        import addon_utils

        for mod in addon_utils.modules():
            if mod.__name__ == module:
                filepath = mod.__file__
                if os.path.exists(filepath):
                    if os.path.splitext(os.path.basename(filepath))[0] == "__init__":
                        return os.path.dirname(filepath), True
                    else:
                        return filepath, False
        return None, False

    def execute(self, context):
        import addon_utils
        import os

        path, isdir = WM_OT_addon_edit.path_from_addon(self.module)
        if path is None:
            self.report({'WARNING'}, "Addon path %r could not be found" % path)
            return {'CANCELLED'}

        filepaths = []
        # walk through dir recursively to find all py files and load them
        if isdir:
             for root, dirs, files in os.walk(path):
                 for file in files:
                     if file.endswith(".py"):
                        filepath = os.path.join(root, file);
                        filepaths.append(filepath)
        else:
             filepaths = [path]

        return self.load_sources(context, filepaths)


def register():
    bpy.utils.register_class(EditAddonSourcePreferences)
    bpy.utils.register_class(WM_OT_addon_edit)
    
    #re-assign method
    global olddraw   
    olddraw = bpy.types.USERPREF_PT_addons.draw    
    bpy.types.USERPREF_PT_addons.draw = draw
   
    
def unregister():
    global olddraw
    bpy.types.USERPREF_PT_addons.draw = olddraw 
    bpy.utils.unregister_class(WM_OT_addon_edit)
    bpy.utils.unregister_class(EditAddonSourcePreferences)


if __name__ == "__main__":
    register()
