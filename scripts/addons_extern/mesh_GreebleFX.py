#
#####################################################################################
# Copyright (C) 2015-2015 GreebleFX
#  http://www.youtube.com/jesus650rwc
#  http://albertofx.wix.com/afxlab
#  animationsvfx@gmail.com
# Based on code by AlbertoFX copyright (C) 2015-2015 GreebleFX
# License: http://www.gnu.org/licenses/gpl.html GPL version 2 or higher
#####################################################################################
#
bl_info = {"name": "GreebleFX",
           "author": "Albertofx",
           "version": (1, 0),
           "blender": (2, 7, 1),
           "location": "View3D > ToolShelf",
           "description": "Add-on that adds greeble to your objects.(Face or Custom Greeble)",
           "warning": "",
           "wiki_url": "",
           "category": "Mesh"}


import bpy
import os


def GreebleFaces(self):
    actob = bpy.context.active_object
    actname = bpy.context.object.name
    # bpy.context.object.name = "GREEBLE_" + actname
    bpy.ops.object.duplicate()
    bpy.ops.object.modifier_remove(modifier="Greeble Height")
    bpy.ops.object.modifier_remove(modifier="Island Greeble")
    bpy.ops.object.modifier_remove(modifier="GREEBLE")
    bpy.ops.object.particle_system_remove()

    actob.select = True
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)

    ob = bpy.context.active_object
    ob.select = True
    bpy.context.scene.objects.active = actob
    # bpy.ops.object.select_all(action='DESELECT')
    for ob in actob.children:
        ob.select = True

        bpy.context.scene.objects.active = actob.children
        ob.select = False
    ob.select = True
    bpy.context.scene.objects.active = actob

    ob = bpy.context.active_object
    bpy.ops.object.particle_system_add()
    # make particle system settings here....

    ob.particle_systems[0].name = "FaceGreeble_System"
    partsys = ob.particle_systems[0].settings

    partsys.frame_start = 1
    partsys.frame_end = 1
    partsys.lifetime = 1000

    # check if number of polygons is less than 5

    facecount = len(ob.data.polygons)
    partsys.count = facecount
    partsys.effector_weights.gravity = 0.0
    partsys.draw_method = 'RENDER'
    partsys.use_render_emitter = True
    partsys.physics_type = 'KEYED'
    partsys.render_type = 'NONE'

    # partsys.use_modifier_stack = True

    partsys.emit_from = 'FACE'
    bpy.context.active_object.modifiers.new(name='GREEBLE', type='EXPLODE')

    bpy.context.active_object.modifiers.new(name='Island Greeble', type='SMOOTH')
    bpy.context.active_object.modifiers.new(name='Greeble Height', type='SOLIDIFY')

    bpy.context.object.modifiers["Greeble Height"].thickness = -0.05
    actname = bpy.context.object.name

    bpy.context.object.name = "GREEBLE_" + actname

    for obj in bpy.context.selected_objects:

        actob = bpy.context.active_object

        bpy.context.object.hide_select = False
        bpy.context.object.lock_location[0] = True
        bpy.context.object.lock_location[1] = True
        bpy.context.object.lock_location[2] = True
        bpy.context.object.lock_rotation[0] = True
        bpy.context.object.lock_rotation[1] = True
        bpy.context.object.lock_rotation[2] = True
        bpy.context.object.lock_scale[0] = True
        bpy.context.object.lock_scale[1] = True
        bpy.context.object.lock_scale[2] = True

        # ob.select = True

    ob.select = False

    bpy.context.scene.objects.active = ob.parent


class greeblefaces(bpy.types.Operator):
    """Creates greeble based on face count"""
    afxlab = "mesh"

    bl_idname = "afxlab.greeblefaces"
    bl_label = "Tear Cloth"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        GreebleFaces(self)
        return {'FINISHED'}


class GreebleSystemPanel(bpy.types.Panel):
    bl_category = "GreebleFX"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_context = "editmode"
    bl_label = "Greeble System Tools"


def RemoveGreebleFaces(self):
    ob = bpy.context.active_object

    for ob in ob.children:
        if ob.name.startswith("GREEBLE"):
            ob.hide_select = False
            # bpy.ops.object.delete(use_global=False)

            bpy.ops.object.select_all(action='DESELECT')

            ob.select = True
            bpy.ops.object.delete(use_global=False)
            ob.select = True
    ob.select = True
    ob = bpy.context.active_object
    ob.select = True


class removegreeblefaces(bpy.types.Operator):
    """Remove Greeble from active"""
    afxlab = "mesh"
    bl_idname = "afxlab.removegreeblefaces"
    bl_label = "Remove Greeble"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        RemoveGreebleFaces(self)
        return {'FINISHED'}


class GreebleSystemPanel(bpy.types.Panel):
    bl_category = "GreebleFX"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_context = "editmode"
    bl_label = "GreebleFX Tools"


def CustomGreeble(self):
    ob = bpy.context.active_object
    bpy.ops.object.particle_system_add()
    # make particle system settings here....

    ob.particle_systems[0].name = "Greeble_System"
    partsys = ob.particle_systems[0].settings

    partsys.frame_start = 1
    partsys.frame_end = 1
    partsys.lifetime = 1000

    # check if number of polygons is less than 5
    facecount = len(ob.data.polygons)
    partsys.count = facecount

    partsys.effector_weights.gravity = 0.0
    partsys.draw_method = 'RENDER'
    partsys.use_render_emitter = True
    partsys.physics_type = 'KEYED'
    partsys.render_type = 'OBJECT'

    # partsys.use_modifier_stack = True
    partsys.emit_from = 'FACE'
    actname = bpy.context.object.name
    bpy.context.object.name = actname + "_CGREEBLE"
    actob = bpy.context.active_object


class customgreeble(bpy.types.Operator):
    """Creates greeble from Object or Group"""
    afxlab = "mesh"

    bl_idname = "afxlab.customgreeble"
    bl_label = "Add Custom Greeble"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        CustomGreeble(self)
        return {'FINISHED'}


class GreebleSystemPanel(bpy.types.Panel):
    bl_category = "GreebleFX"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_context = "editmode"
    bl_label = "GreebleFX Tools"


def RemoveGreeble(self):
    actname = bpy.context.object.name[:-9]
    bpy.context.object.name = actname

    bpy.ops.object.particle_system_remove()


class removegreeble(bpy.types.Operator):
    """Remove Greeble from active"""
    afxlab = "mesh"
    bl_idname = "afxlab.removegreeble"
    bl_label = "Remove Greeble"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        RemoveGreeble(self)
        return {'FINISHED'}


class GreebleSystemPanel(bpy.types.Panel):
    bl_category = "GreebleFX"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_context = "editmode"
    bl_label = "GreebleFX Tools"


def greeble_OBJECT(self, context):

    if context.scene.greeble_OBJECT:
        bpy.context.scene.greeble_GROUP = False
        ob = bpy.context.active_object
        partsys = ob.particle_systems[0].settings

        partsys.render_type = 'OBJECT'
    else:
        bpy.context.scene.greeble_GROUP = True
bpy.types.Scene.greeble_OBJECT = bpy.props.BoolProperty(update=greeble_OBJECT)


class GreebleSystemPanel(bpy.types.Panel):
    bl_category = "GreebleFX"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_context = "editmode"
    bl_label = "GreebleFX Tools"

    @classmethod
    def greeble_OBJECT(self, context):

        return True


def greeble_GROUP(self, context):

    if context.scene.greeble_GROUP:
        bpy.context.scene.greeble_OBJECT = False

        ob = bpy.context.active_object
        partsys = ob.particle_systems[0].settings

        partsys.render_type = 'GROUP'
    else:
        bpy.context.scene.greeble_OBJECT = True
        partsys.render_type = 'OBJECT'
bpy.types.Scene.greeble_GROUP = bpy.props.BoolProperty(update=greeble_GROUP)


class GreebleSystemPanel(bpy.types.Panel):
    bl_category = "GreebleFX"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_context = "editmode"
    bl_label = "GreebleFX Tools"

    @classmethod
    def greeble_GROUP(self, context):

        return True


def applyselectedgreeble(self):
    bpy.context.object.lock_location[0] = False
    bpy.context.object.lock_location[1] = False
    bpy.context.object.lock_location[2] = False
    bpy.context.object.lock_rotation[0] = False
    bpy.context.object.lock_rotation[1] = False
    bpy.context.object.lock_rotation[2] = False
    bpy.context.object.lock_scale[0] = False
    bpy.context.object.lock_scale[1] = False
    bpy.context.object.lock_scale[2] = False
    bpy.ops.object.convert(target='MESH')

    actname = bpy.context.object.name[-11:]
    bpy.context.object.name = actname


class applyactivegreeble(bpy.types.Operator):
    """Apply active greeble"""
    afxlab = "mesh"
    bl_idname = "afxlab.applyactivegreeble"
    bl_label = "Apply Greeble"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        applyselectedgreeble(self)
        return {'FINISHED'}


class GreebleSystemPanel(bpy.types.Panel):
    bl_category = "GreebleFX"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_context = "editmode"
    bl_label = "GreebleFX Tools"


def applyfacegreeble(self):
    ob = bpy.context.active_object
    bpy.ops.object.select_all(action='DESELECT')
    for ob in ob.children:
        if ob.name.startswith("GREEBLE"):
            bpy.context.scene.objects.active = ob
            ob.hide_select = False
            ob.select = True
            # bpy.ops.object.delete(use_global=False)

            # bpy.ops.object.select_all(action='DESELECT')

            # ob.select = True
            bpy.context.object.lock_location[0] = False
            bpy.context.object.lock_location[1] = False
            bpy.context.object.lock_location[2] = False
            bpy.context.object.lock_rotation[0] = False
            bpy.context.object.lock_rotation[1] = False
            bpy.context.object.lock_rotation[2] = False
            bpy.context.object.lock_scale[0] = False
            bpy.context.object.lock_scale[1] = False
            bpy.context.object.lock_scale[2] = False
            bpy.ops.object.convert(target='MESH')

            actname = bpy.context.object.name[+8:]
            bpy.context.object.name = actname

            # acname = bpy.context.object.name[:-4]
            # bpy.context.object.name = acname
            obname = bpy.context.object.name

            bpy.context.object.name = obname + "(GREEBLE)"
            # ob.select = True


class applygreeble(bpy.types.Operator):
    """Apply greeble faces"""
    afxlab = "mesh"
    bl_idname = "afxlab.applygreeble"
    bl_label = "Apply Greeble"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        applyfacegreeble(self)
        return {'FINISHED'}


class GreebleSystemPanel(bpy.types.Panel):
    bl_category = "GreebleFX"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_context = "editmode"
    bl_label = "GreebleFX Tools"


class afxlab(bpy.types.Operator):
    bl_idname = "visit.afxlab"
    bl_label = "See other tools"
    bl_description = "Sends you to my site where you can find many other add-ons by me(AlbertoFX)"

    def execute(self, context):
        bpy.ops.wm.url_open(url="http://albertofx.wix.com/afxlab")
        return{"FINISHED"}


class GreebleSystemPanel(bpy.types.Panel):
    bl_category = "GreebleFX"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    # bl_context = "editmode"
    bl_label = "GreebleFX Tools"

    def draw(self, context):
        ob = context.object
        sce = context.scene
        layout = self.layout
        # row = layout.row(align=True)
        if ob is not None:
            if not ob.name.startswith("GREEBLE"):

                if ob is not None:

                    # if ob.name.startswith("GREEBLE"):
                    # layout.operator(customgreeble.bl_idname,text= "Add Adaptive Greeble", icon= 'ZOOMIN')
                    # layout.operator(greeblefaces.bl_idname,text= "Greeble Faces", icon ='SPLITSCREEN')

                    # pass
                    # else:
                    if ob.particle_systems and ob.particle_systems["Greeble_System"].name == "Greeble_System":

                        # row.label(text="",icon='BLANK1' )
                        # layout.prop(context.scene, "select_type", expand=True)

                        # layout.operator(customgreeble.bl_idname,text= "Add Adaptive Greeble", icon= 'ZOOMIN')
                        row = layout.row(align=True)
                        row.prop(sce, "greeble_OBJECT", text="OBJECT", icon='OBJECT_DATAMODE')
                        row.prop(sce, "greeble_GROUP", text="GROUP", icon='GROUP')
                    else:

                        layout.operator(customgreeble.bl_idname, text="Custom Greeble", icon='UGLYPACKAGE')
                        layout.operator(greeblefaces.bl_idname, text="Greeble Faces", icon='SPLITSCREEN')
                        row = layout.row()
                        box = row.box()
                        box.operator("visit.afxlab", text="*AFXLAB*", icon='WORLD')

                    if bpy.context.scene.greeble_OBJECT == True:

                        layout = self.layout
                        row = layout.row(align=True)
                        sce = context.scene
                        ob = bpy.context.active_object

                        if ob is not None:

                            # if ob.name.startswith("GREEBLE"):
                            #     pass
                            #     row.label(text="",icon='BLANK1' )
                            # else:
                            if ob.particle_systems and ob.particle_systems["Greeble_System"].name == "Greeble_System":

                                if ob is not None:
                                    for ps in ob.particle_systems:

                                        # layout.prop(sce, "greeble_OBJECT",text="OBJECT", icon='OBJECT_DATAMODE')

                                        # layout.prop(context.scene, "select_type", expand=True)
                                        layout.prop(ps.settings, "dupli_object", text="")

                                        row = layout.row(align=True)
                                        # row.label(text="",icon='BLANK1' )

                                        row.prop(ps.settings, "count", text="Amount")
                                        layout.prop(ps.settings, "particle_size", text="Size")
                                        layout.prop(ps.settings, "size_random", text="Size offset")

                                        row = layout.row(align=True)
                                        row.label(text="Track to axis:", icon='MANIPUL')
                                        row = layout.row(align=True)
                                        row.prop(ps.settings, "object_align_factor", text="X", index=0)
                                        row.prop(ps.settings, "object_align_factor", text="Y", index=1)
                                        row.prop(ps.settings, "object_align_factor", text="Z", index=2)
                                        layout.operator(removegreeble.bl_idname, text="Remove Greeble", icon='CANCEL')
                                        row = layout.row()
                                        box = row.box()
                                        box.operator("visit.afxlab", text="*AFXLAB*", icon='WORLD')
                                    # if bpy.context.scene.select_type == '0':

                    if bpy.context.scene.greeble_GROUP == True:

                        layout = self.layout
                        row = layout.row(align=True)
                        sce = context.scene
                        ob = context.object

                        if ob.particle_systems and ob.particle_systems["Greeble_System"].name == "Greeble_System":

                            if ob is not None:
                                for ps in ob.particle_systems:

                                    # layout.prop(context.scene, "select_type", expand=True)
                                    layout.prop(ps.settings, "dupli_group", text="")

                                    row = layout.row(align=True)
                                    # row.label(text="",icon='BLANK1' )

                                    row.prop(ps.settings, "count", text="Amount")
                                    layout.prop(ps.settings, "particle_size", text="Size")

                                    layout.prop(ps.settings, "size_random", text="Size offset")
                                    row = layout.row(align=True)
                                    row.label(text="Track to axis:", icon='MANIPUL')
                                    row = layout.row(align=True)
                                    row.prop(ps.settings, "object_align_factor", text="X", index=0)
                                    row.prop(ps.settings, "object_align_factor", text="Y", index=1)
                                    row.prop(ps.settings, "object_align_factor", text="Z", index=2)
                                    layout.operator(removegreeble.bl_idname, text="Remove Greeble", icon='CANCEL')
                                    # layout = self.layout
                                    row = layout.row()
                                    box = row.box()
                                    box.operator("visit.afxlab", text="*AFXLAB*", icon='WORLD')

                    ob = bpy.context.active_object
                    layout = self.layout

                    ob = bpy.context.active_object
                    for ob in ob.children:
                        if ob.type == 'MESH' and ob.name.startswith("GREEBLE"):
                            row = layout.row()
                            box = row.box()
                            if ob.particle_systems["FaceGreeble_System"].name == "FaceGreeble_System":
                                # if ob.particle_systems:
                                # layout = self.layout
                                box.label(text="FACE GREEBLE STTINGS:", icon='SETTINGS')

                                box.operator(removegreeblefaces.bl_idname, text="Remove Greeble", icon='CANCEL')

                                for mod in ob.modifiers:

                                    if mod.type == 'EXPLODE':

                                        box.prop(mod, "use_edge_cut", text="Offset Edges")

                                    if mod.type == 'SOLIDIFY':
                                            # match enum type to our functions, avoids a lookup table.

                                        row = layout.row(align=True)
                                        if ob.particle_systems:
                                            for ps in ob.particle_systems:

                                                # layout.prop(context.scene, "select_type", expand=True)

                                                # row = layout.row(align=True)
                                                # row.label(text="",icon='BLANK1' )

                                                box.prop(ps.settings, "count", text="Amount")
                                        box.prop(mod, "thickness", text="Height")
                                        box.prop(mod, "thickness_clamp", text="Height offset")

                                box.operator(applygreeble.bl_idname, text="Apply Greeble", icon='FILE_TICK')
                else:
                    layout.label(text="Select Object First", icon='VIEW3D')
            else:
                layout = self.layout
                layout.label(text="Select main object for Greeble", icon='ERROR')
                layout.label(text="     settings.")
                layout.operator(applyactivegreeble.bl_idname, text="Apply Greeble", icon='FILE_TICK')
        else:
            layout = self.layout
            layout.label(text="Select Object First", icon='VIEW3D')
            row = layout.row()
            box = row.box()
            box.operator("visit.afxlab", text="*AFXLAB*", icon='WORLD')


def register():
    bpy.utils.register_module(__name__)

    bpy.types.Scene.select_type = bpy.props.EnumProperty(
        name="Type",
        description="Select object or group",
        items=[("0", "OBJECT", "make duplicates of a specific object"),
               ("1", "GROUP", "make duplicates of the objects in a group"),
               ],
        default='0')


def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.select_type

if __name__ == "__main__":
    register()
