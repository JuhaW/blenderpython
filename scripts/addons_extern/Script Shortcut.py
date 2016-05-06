import bpy
import os
import sys
from bpy_extras.io_utils import ImportHelper


bl_info = {
    "name": "Script Shortcut",
    "description": "Allows easily running of python scripts by adding a configurable shortcut panel to the Properties shelf of most areas.  Pressing a script button will execute commands directly in the script, and will run the 'register()' function if it exists.",
    "author": "Hudson Barkley (Snu)",
    "version": (0, 3, 0),
    "blender": (2, 76, 0),
    "location": "Properties shelf in most areas, View menu in same areas.",
    "wiki_url": "none",
    "category": "Development"
}


def draw_scriptshortcut_menu(self, context):
    # This function draws the menu to enable/disable shortcut panels
    layout = self.layout
    layout.menu("scriptshortcut.menu", text="Script Shortcut Panels")


def panel_settings_item(context, layout, setting):
    # This function will draw a single panel toggle element in the popup menu
    name = setting.replace('_', ' ').title()
    if setting in context.scene.scriptshortcutpanels:
        enabled = "Off"
    else:
        enabled = "On"

    layout.operator("scriptshortcut.settings", text="Toggle " + name + " Panel " + enabled).setting = setting


def return_panel(scene, panel):
    # This function will return the panel data for the given panel name
    if panel == 'VIEW_3D':
        return [scene.scriptshortcuts.VIEW_3Dedit, scene.scriptshortcuts.VIEW_3D]
    if panel == 'GRAPH_EDITOR':
        return [scene.scriptshortcuts.GRAPH_EDITORedit, scene.scriptshortcuts.GRAPH_EDITOR]
    if panel == 'NLA_EDITOR':
        return [scene.scriptshortcuts.NLA_EDITORedit, scene.scriptshortcuts.NLA_EDITOR]
    if panel == 'IMAGE_EDITOR':
        return [scene.scriptshortcuts.IMAGE_EDITORedit, scene.scriptshortcuts.IMAGE_EDITOR]
    if panel == 'SEQUENCE_EDITOR':
        return [scene.scriptshortcuts.SEQUENCE_EDITORedit, scene.scriptshortcuts.SEQUENCE_EDITOR]
    if panel == 'CLIP_EDITOR':
        return [scene.scriptshortcuts.CLIP_EDITORedit, scene.scriptshortcuts.CLIP_EDITOR]
    if panel == 'TEXT_EDITOR':
        return [scene.scriptshortcuts.TEXT_EDITORedit, scene.scriptshortcuts.TEXT_EDITOR]
    if panel == 'NODE_EDITOR':
        return [scene.scriptshortcuts.NODE_EDITORedit, scene.scriptshortcuts.NODE_EDITOR]
    if panel == 'LOGIC_EDITOR':
        return [scene.scriptshortcuts.LOGIC_EDITORedit, scene.scriptshortcuts.LOGIC_EDITOR]


class ScriptShortcutPanelButton(bpy.types.PropertyGroup):
    # This class stores the data for a panel element

    # The button name
    title = bpy.props.StringProperty(
        name="Button Title",
        default="Button")
    # The script that will be run when the button is activated
    script = bpy.props.StringProperty(
        name="Script File",
        default="")
    # Determine if this button is conditional or not
    conditional = bpy.props.BoolProperty(
        name="Conditional Enabled",
        description="Make This Button A Conditional Button",
        default=False)
    # A string that contains the conditional check statement for this button
    requirement = bpy.props.StringProperty(
        name="Conditional Requirement",
        default="")


class ScriptShortcutPanels(bpy.types.PropertyGroup):
    # Class that stores the data for all the panel elements
    VIEW_3D = bpy.props.CollectionProperty(type=ScriptShortcutPanelButton)
    VIEW_3Dedit = bpy.props.BoolProperty(default=False)
    GRAPH_EDITOR = bpy.props.CollectionProperty(type=ScriptShortcutPanelButton)
    GRAPH_EDITORedit = bpy.props.BoolProperty(default=False)
    NLA_EDITOR = bpy.props.CollectionProperty(type=ScriptShortcutPanelButton)
    NLA_EDITORedit = bpy.props.BoolProperty(default=False)
    IMAGE_EDITOR = bpy.props.CollectionProperty(type=ScriptShortcutPanelButton)
    IMAGE_EDITORedit = bpy.props.BoolProperty(default=False)
    SEQUENCE_EDITOR = bpy.props.CollectionProperty(type=ScriptShortcutPanelButton)
    SEQUENCE_EDITORedit = bpy.props.BoolProperty(default=False)
    CLIP_EDITOR = bpy.props.CollectionProperty(type=ScriptShortcutPanelButton)
    CLIP_EDITORedit = bpy.props.BoolProperty(default=False)
    TEXT_EDITOR = bpy.props.CollectionProperty(type=ScriptShortcutPanelButton)
    TEXT_EDITORedit = bpy.props.BoolProperty(default=False)
    NODE_EDITOR = bpy.props.CollectionProperty(type=ScriptShortcutPanelButton)
    NODE_EDITORedit = bpy.props.BoolProperty(default=False)
    LOGIC_EDITOR = bpy.props.CollectionProperty(type=ScriptShortcutPanelButton)
    LOGIC_EDITORedit = bpy.props.BoolProperty(default=False)


class ScriptShortcutSave(bpy.types.Operator, ImportHelper):
    # This is an operator to save a current panel layout to an external file
    # The panel variable must be set

    bl_idname = "scriptshortcut.save"
    bl_label = "Save Layout"
    bl_description = "Save this layout"

    panel = bpy.props.StringProperty()
    title = bpy.props.StringProperty(name='Title')
    filepath = bpy.props.StringProperty()

    def execute(self, context):
        # Get the panel data
        self.data = return_panel(context.scene, self.panel)[1]
        try:
            file = open(self.filepath, 'w')
            for button in self.data:
                file.write(button.title + '\n')
                file.write(str(button.conditional) + '\n')
                file.write(button.script + '\n')
            file.close()
            self.report({'INFO'}, "Saved file to: " + self.filepath)
        except:
            self.report({'WARNING'}, "Unable to save file: " + self.filepath)
        return {'FINISHED'}


class ScriptShortcutLoad(bpy.types.Operator, ImportHelper):
    # This is an operator to load a layout file
    bl_idname = "scriptshortcut.load"
    bl_label = "Load Layout"
    bl_description = "Load this layout"

    panel = bpy.props.StringProperty()
    title = bpy.props.StringProperty(name='Title')
    filepath = bpy.props.StringProperty()

    def execute(self, context):
        try:
            file = open(self.filepath, "r")
            data = file.readlines()
            file.close()
            if len(data) > 1:
                oldpanel = return_panel(context.scene, self.panel)[1]
                oldpanel.clear()
                element = 'title'
                title = ""
                conditional = False
                for line in data:
                    if len(line.replace('\n', '')) > 0:
                        if element == 'title':
                            title = line.replace('\n', '')
                            element = 'conditional'
                        elif element == 'conditional':
                            if line.replace('\n', '') == 'True':
                                conditional = True
                            element = 'script'
                        elif element == 'script':
                            button = oldpanel.add()
                            button.title = title
                            button.conditional = conditional
                            button.script = line.replace('\n', '')
                            try:
                                file = open(button.script, 'r')
                                requirement = file.readline().strip("\n\r")
                                file.close()
                                if requirement[0] == "#":
                                    button.requirement = requirement[1:]
                            except:
                                pass
                            element = 'title'

                self.report({'INFO'}, "Loaded layout from file: " + self.filepath)
            else:
                raise Exception("")
        except:
            self.report({'WARNING'}, "Unable to open file: " + self.filepath)
        return {'FINISHED'}


class ScriptShortcutClear(bpy.types.Operator):
    # This operator will remove all elements from a panel
    bl_idname = "scriptshortcut.clear"
    bl_label = "Clear Layout"
    bl_description = "Clear this layout"

    panel = bpy.props.StringProperty()

    def execute(self, context):
        self.data = return_panel(context.scene, self.panel)[1]
        self.data.clear()
        return {'FINISHED'}


class ScriptShortcutMove(bpy.types.Operator):
    # This operator will move an element up or down in the list
    bl_idname = "scriptshortcut.move"
    bl_label = "Move Shortcut"
    bl_description = "Move this item"

    argument = bpy.props.StringProperty()

    def execute(self, context):
        panel = self.argument.split(',')[0]
        buttonindex = int(self.argument.split(',')[1])
        direction = self.argument.split(',')[2]
        buttons = return_panel(context.scene, panel)[1]
        if direction == 'up':
            move = -1
        else:
            move = 1
        buttons.move(buttonindex, buttonindex + move)
        return {'FINISHED'}


class ScriptShortcutRun(bpy.types.Operator):
    # This operator will run an external python script
    bl_idname = "scriptshortcut.run"
    bl_label = "Run Script"
    bl_description = "Run a python script"

    path = bpy.props.StringProperty()

    def execute(self, context):
        try:
            folder = os.path.split(self.path)[0]
            file = os.path.splitext(os.path.split(self.path)[1])[0]
            sys.path.insert(0, folder)
            script = __import__(file)

            try:
                script.register()

            except:
                pass

            sys.path.remove(folder)
            del sys.modules[file]
            del script

        except:
            pass

        return {'FINISHED'}


class ScriptShortcutRename(bpy.types.Operator):
    # This operator will rename an element in a shortcut panel
    bl_idname = "scriptshortcut.rename"
    bl_label = "Rename Button Or Label"
    bl_description = "Rename this item"

    argument = bpy.props.StringProperty()
    title = bpy.props.StringProperty(name='Title')
    script = bpy.props.StringProperty()

    def invoke(self, context, event):
        button_index = int(self.argument.split(',')[1])
        buttons = return_panel(context.scene, self.argument.split(',')[0])[1]
        self.button = buttons[button_index]
        self.title = self.button.title
        return context.window_manager.invoke_props_dialog(self, width=600, height=200)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(self, 'title')

    def execute(self, context):
        self.button.title = self.title
        return {'FINISHED'}


class ScriptShortcutAdd(bpy.types.Operator):
    # This operator will add a new element to a shortcut panel
    bl_idname = "scriptshortcut.new"
    bl_label = "Add New Script Shortcut"
    bl_description = "Add a new item"

    argument = bpy.props.StringProperty()
    title = bpy.props.StringProperty(name='Title')
    type = bpy.props.StringProperty()
    panel = bpy.props.StringProperty()

    def invoke(self, context, event):
        self.type = self.argument.split(',')[1]
        self.panel = self.argument.split(',')[0]
        buttons = return_panel(context.scene, self.panel)[1]
        if self.type == "button":
            self.title = "Button " + str(len(buttons) + 1)
            return context.window_manager.invoke_props_dialog(self, width=600, height=200)
        elif self.type == "label":
            self.title = "Label " + str(len(buttons) + 1)
            return context.window_manager.invoke_props_dialog(self, width=600, height=200)
        else:
            button = buttons.add()
            button.title = '_'
            button.script = '_'
            return {'FINISHED'}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(self, 'title')

    def execute(self, context):
        if self.type == "button":
            bpy.ops.scriptshortcut.selectscript('INVOKE_DEFAULT', title=self.title, panel=self.argument.split(',')[0])
        else:
            buttons = return_panel(context.scene, self.panel)[1]
            button = buttons.add()
            button.title = self.title
            button.script = '_'
        return {'FINISHED'}


class ScriptShortcutSelectScript(bpy.types.Operator, ImportHelper):
    # This operator will open a file select dialog to select an external script for a panel element
    bl_idname = "scriptshortcut.selectscript"
    bl_label = "Select A Script For Script Shortcut"

    title = bpy.props.StringProperty(name='Title')
    panel = bpy.props.StringProperty(name='Panel')
    filename_ext = ".py"

    filter_glob = bpy.props.StringProperty(
        default="*.py",
        options={'HIDDEN'})
    directory = bpy.props.StringProperty(subtype='DIR_PATH')

    def execute(self, context):
        buttons = return_panel(context.scene, self.panel)[1]
        button = buttons.add()
        button.title = self.title
        button.script = self.filepath
        file = open(self.filepath, 'r')
        requirement = file.readline().strip("\n\r")
        file.close()
        if requirement[0] == "#":
            button.requirement = requirement[1:]
        return {'FINISHED'}


class ScriptShortcutRemove(bpy.types.Operator):
    # This operator will remove an item from the shortcut list
    bl_idname = "scriptshortcut.remove"
    bl_label = "Remove A Script Shortcut"
    bl_description = "Remove this item"

    argument = bpy.props.StringProperty()

    def execute(self, context):
        buttons = return_panel(context.scene, self.argument.split(',')[0])[1]
        button = int(self.argument.split(',')[1])
        buttons.remove(button)
        return {'FINISHED'}


class ScriptShortcutMenu(bpy.types.Menu):
    # This is the menu for toggling shortcut panels on and off
    bl_idname = "scriptshortcut.menu"
    bl_label = "Script Shortcut"

    def draw(self, context):
        layout = self.layout

        panel_settings_item(context, layout, "VIEW_3D")
        panel_settings_item(context, layout, "GRAPH_EDITOR")
        panel_settings_item(context, layout, "NLA_EDITOR")
        panel_settings_item(context, layout, "IMAGE_EDITOR")
        panel_settings_item(context, layout, "SEQUENCE_EDITOR")
        panel_settings_item(context, layout, "CLIP_EDITOR")
        panel_settings_item(context, layout, "TEXT_EDITOR")
        panel_settings_item(context, layout, "NODE_EDITOR")
        panel_settings_item(context, layout, "LOGIC_EDITOR")


class ScriptShortcutSettings(bpy.types.Operator):
    # This operator will toggle a specific panel on or off
    bl_idname = "scriptshortcut.settings"
    bl_label = "Script Shortcut Settings"
    bl_description = "Toggles Panels On And Off"

    setting = bpy.props.StringProperty()

    def execute(self, context):
        panel_settings = context.scene.scriptshortcutpanels.split(',')
        if self.setting in panel_settings:
            panel_settings.pop(panel_settings.index(self.setting))
        else:
            panel_settings.append(self.setting)
        context.scene.scriptshortcutpanels = ','.join(panel_settings)

        return{'FINISHED'}


class ScriptShortcutPanelTemplate(bpy.types.Panel):
    # This class is the template for all panels
    bl_label = "Script Shortcuts"
    bl_space_type = "EMPTY"
    bl_region_type = "UI"

    @classmethod
    def poll(self, context):
        if self.bl_space_type not in context.scene.scriptshortcutpanels:
            return False
        else:
            return True

    def draw(self, context):
        panel = self.bl_space_type
        layout = self.layout

        # Get the panel data thats stored in the scene properties
        paneldata = return_panel(context.scene, panel)
        buttons = paneldata[1]
        editmode = paneldata[0]

        if editmode:
            # Draw the panel in edit mode
            for index, button in enumerate(buttons):
                # Iterate through the elements and draw each one
                if button.title == '_' and button.script == '_':
                    # This element is a spacer
                    row = layout.row()
                    split = row.split(percentage=.6, align=True)
                    # Spacer label
                    split.label("<Spacer>")
                    # Move up button
                    split.operator("scriptshortcut.move", text="", icon="TRIA_UP").argument = panel + ',' + str(index) + ',' + 'up'
                    # Move down button
                    split.operator("scriptshortcut.move", text="", icon="TRIA_DOWN").argument = panel + ',' + str(index) + ',' + 'down'
                    # Remove the label button
                    split.operator("scriptshortcut.remove", text="", icon="X").argument = panel + ',' + str(index)
                    # Spacer area to keep layout over the conditional property
                    split.label(text="")

                else:
                    # This element is a button or a label
                    row = layout.row()
                    split = row.split(percentage=.6, align=True)
                    # Button to rename this button
                    split.operator("scriptshortcut.rename", text=button.title).argument = panel + ',' + str(index)
                    # Move up button
                    split.operator("scriptshortcut.move", text="", icon="TRIA_UP").argument = panel + ',' + str(index) + ',' + 'up'
                    # Move down button
                    split.operator("scriptshortcut.move", text="", icon="TRIA_DOWN").argument = panel + ',' + str(index) + ',' + 'down'
                    # Remove the label button
                    split.operator("scriptshortcut.remove", text="", icon="X").argument = panel + ',' + str(index)

                    if button.script == '_':
                        # Spacer area to keep layout over the conditional property
                        split.label(text="")
                    else:
                        # Conditional mode checkbox property
                        split.prop(button, 'conditional')

            row = layout.row()
            split = row.split(align=True)
            # Create a new button
            split.operator("scriptshortcut.new", text="Button", icon="PLUS").argument = panel + ',' + "button"
            # Create a new spacer
            split.operator("scriptshortcut.new", text="Spacer", icon="PLUS").argument = panel + ',' + "spacer"
            # Create a new label
            split.operator("scriptshortcut.new", text="Label", icon="PLUS").argument = panel + ',' + "label"
            row = layout.row()
            split = row.split()
            # Save layout button
            split.operator("scriptshortcut.save", text="Save", icon="DISK_DRIVE").panel = panel
            # Load layout button
            split.operator("scriptshortcut.load", text="Load", icon="FILESEL").panel = panel
            # Clear layout button
            split.operator("scriptshortcut.clear", text="Clear").panel = panel

        else:
            # Draw the panel in normal display mode
            for index, button in enumerate(buttons):
                # Iterate through the elements and draw each one
                row = layout.row()
                if button.script == '_':
                    # This element is a label or spacer
                    if button.title == '_':
                        # This element is a spacer
                        row.label("")
                    else:
                        # This element is a label
                        row.label(button.title)

                else:
                    # This element is a button
                    row.operator("scriptshortcut.run", text=button.title).path = button.script

                    # Check if this button is conditional and should be disabled
                    if button.conditional and len(button.requirement) > 0:
                        # This button is in conditional mode
                        try:
                            condition = eval(button.requirement)
                            if condition == False:
                                row.enabled = False
                        except:
                            row.enabled = False

        row = layout.row()
        # Edit mode toggle button
        row.prop(context.scene.scriptshortcuts, panel + 'edit', text='Edit')


# The following classes are definitions for each panel
class ScriptShortcutPanelView3d(ScriptShortcutPanelTemplate):
    bl_space_type = "VIEW_3D"


class ScriptShortcutPanelGraphEditor(ScriptShortcutPanelTemplate):
    bl_space_type = "GRAPH_EDITOR"


class ScriptShortcutPanelNLAEditor(ScriptShortcutPanelTemplate):
    bl_space_type = "NLA_EDITOR"


class ScriptShortcutPanelImageEditor(ScriptShortcutPanelTemplate):
    bl_space_type = "IMAGE_EDITOR"


class ScriptShortcutPanelSequenceEditor(ScriptShortcutPanelTemplate):
    bl_space_type = "SEQUENCE_EDITOR"


class ScriptShortcutPanelClipEditor(ScriptShortcutPanelTemplate):
    bl_space_type = "CLIP_EDITOR"


class ScriptShortcutPanelTextEditor(ScriptShortcutPanelTemplate):
    bl_space_type = "TEXT_EDITOR"


class ScriptShortcutPanelNodeEditor(ScriptShortcutPanelTemplate):
    bl_space_type = "NODE_EDITOR"


class ScriptShortcutPanelLogicEditor(ScriptShortcutPanelTemplate):
    bl_space_type = "LOGIC_EDITOR"


def register():
    bpy.utils.register_module(__name__)

    bpy.types.VIEW3D_MT_view.prepend(draw_scriptshortcut_menu)
    bpy.types.GRAPH_MT_view.prepend(draw_scriptshortcut_menu)
    bpy.types.NLA_MT_view.prepend(draw_scriptshortcut_menu)
    bpy.types.IMAGE_MT_view.prepend(draw_scriptshortcut_menu)
    bpy.types.SEQUENCER_MT_view.prepend(draw_scriptshortcut_menu)
    bpy.types.CLIP_MT_view.prepend(draw_scriptshortcut_menu)
    bpy.types.TEXT_MT_view.prepend(draw_scriptshortcut_menu)
    bpy.types.NODE_MT_view.prepend(draw_scriptshortcut_menu)
    bpy.types.LOGIC_MT_view.prepend(draw_scriptshortcut_menu)

    bpy.types.Scene.scriptshortcuts = bpy.props.PointerProperty(type=ScriptShortcutPanels)

    bpy.types.Scene.scriptshortcutpanels = bpy.props.StringProperty(
        name="Enabled Script Shortcut Panels",
        default="VIEW_3D,GRAPH_EDITOR,NLA_EDITOR,IMAGE_EDITOR,SEQUENCE_EDITOR,CLIP_EDITOR,TEXT_EDITOR,NODE_EDITOR,LOGIC_EDITOR")


def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.VIEW3D_MT_view.remove(draw_scriptshortcut_menu)
    bpy.types.GRAPH_MT_view.remove(draw_scriptshortcut_menu)
    bpy.types.NLA_MT_view.remove(draw_scriptshortcut_menu)
    bpy.types.IMAGE_MT_view.remove(draw_scriptshortcut_menu)
    bpy.types.SEQUENCER_MT_view.remove(draw_scriptshortcut_menu)
    bpy.types.CLIP_MT_view.remove(draw_scriptshortcut_menu)
    bpy.types.TEXT_MT_view.remove(draw_scriptshortcut_menu)
    bpy.types.NODE_MT_view.remove(draw_scriptshortcut_menu)
    bpy.types.LOGIC_MT_view.remove(draw_scriptshortcut_menu)


if __name__ == "__main__":
    register()
