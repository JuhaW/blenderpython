# bl_info = {
#    "name": "Extension Add",
#    "author": "marvin.k.breuer",
#    "version": (0, 1, 0),
#    "blender": (2, 72, 0),
#    "location": "View3D > Toolbar",
#    "warning": "",
#    "description": "Toolkit Extension",
#    "wiki_url": "",
#    "category": "User Panel",
#}


import bpy
from bpy import *
# property group containing all properties for the gui in the panel
# Dropdown Arrow ### general display properties = arrow tooltips


class DropdownMetaTool_UV_Props(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.metawindowtool_uv
    """
    # UV Unwrap Tools
    display_tab_unwrap = bpy.props.BoolProperty(name="UV Tools", description="Display UV Tools", default=True)
    display_tab_uvut = bpy.props.BoolProperty(name="UV Utility", description="Display UV Utility Tools", default=False)
    display_tab_uvsure = bpy.props.BoolProperty(name="SureUVW", description="Display SureUVW Tools", default=False)
    display_tab_unwrapset = bpy.props.BoolProperty(name="UV Unwrap", description="Display UV Unwrap Tools", default=False)
    display_tab_uvnext = bpy.props.BoolProperty(name="TextureSpace / Freestyle", description="Display TextureSpace / Freestyle Tools", default=False)


#############################################################
###----------------  UV Mapping  -------------------------###
###----------------  UV Mapping  -------------------------###
#############################################################

# Sub Location
class SubLoc_UVS():
    """UV Tools"""
    bl_category = "META"
    #bl_region_type = 'TOOLS'
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(cls, context):
        return context.scene.osc_uvs

# Sub Panel


class META_TAB_UVS(SubLoc_UVS, bpy.types.Panel):
    """UV Tool"""
    bl_idname = "meta.uvtools"
    bl_label = "[UV UNWRAP]"

    def draw(self, context):
        lt = context.window_manager.metawindowtool_uv
        wm = context.window_manager
        scn = context.scene
        obj = context.object
        scene = context.scene
        layout = self.layout


# -------------------------------------------------------
# UV Mapping  #######-------------------------------------------------------
# UV Mapping  #######-------------------------------------------------------
# -------------------------------------------------------

### Objectmode ###

        col = layout.column(align=True)

        obj = context
        if obj and obj.mode == 'OBJECT':

            if lt.display_tab_unwrap:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_tab_unwrap", text="", icon='TRIA_DOWN')
            else:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_tab_unwrap", text="", icon='TRIA_RIGHT')

            row.label("UvTools...")

            if lt.display_tab_unwrap:

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("transform.translate", text="Move Texture Space").texture_space = True

                row = col_top.row(align=True)
                row.operator("uv.uv_equalize", text="UV Equalize")


# UV Utility  ######-------------------------------------------------
# UV Utility  ######-------------------------------------------------

                if lt.display_tab_uvut:
                    box = layout.box()
                    row = box.row()
                    row.prop(lt, "display_tab_uvut", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    box = layout.box()
                    row = box.row()
                    row.prop(lt, "display_tab_uvut", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

                row.label("UV Utility...")

                if lt.display_tab_uvut:

                    col = layout.column(align=True)
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("uvutil.change_index", text="Drop Active UV Back")

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.prop(scene, "UVTexRenderActive")

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("uvutil.select_index", text="Select UVTexCoord")
                    row = col_top.row(align=True)
                    row.prop(scene, "UVTexIndex", text="UVTexCoord")

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("uvutil.select_name", text="Select UV Name")
                    row = col_top.row(align=True)
                    row.prop(scene, "UVTexGetName", text="")

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("uvutil.remove_active", text="Remove Active UV")


# SureUVW  ######-------------------------------------------------
# SureUVW  ######-------------------------------------------------

                if lt.display_tab_uvsure:
                    box = layout.box()
                    row = box.row()
                    row.prop(lt, "display_tab_uvsure", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    box = layout.box()
                    row = box.row()
                    row.prop(lt, "display_tab_uvsure", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

                row.label("SureUVW...")

                if lt.display_tab_uvsure:

                    col = layout.column(align=True)
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)

                    row.label("Press this button first:")
                    row = col_top.row(align=True)
                    row.operator("object.sureuvw_operator", text="Show active texture on object").action = 'showtex'
                    row = col_top.row(align=True)
                    row.label("UVW Mapping:")
                    row = col_top.row(align=True)
                    row.operator("object.sureuvw_operator", text="UVW Box Map").action = 'box'
                    row = col_top.row(align=True)
                    row.operator("object.sureuvw_operator", text="Best Planar Map").action = 'bestplanar'
                    row = col_top.row(align=True)
                    row.label("1. Make Material With Raster Texture!")
                    row = col_top.row(align=True)
                    row.label("2. Set Texture Mapping Coords: UV!")
                    row = col_top.row(align=True)
                    row.label("3. Use Addon buttons")


# -------------------------------------------------------
# UV Mapping Edit  #######-------------------------------------------------------
# UV Mapping Edit  #######-------------------------------------------------------
# -------------------------------------------------------

### Editmode ###

        obj = context
        if obj and obj.mode == 'EDIT_MESH':

            if lt.display_tab_unwrap:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_tab_unwrap", text="", icon='TRIA_DOWN')
            else:
                box = layout.box()
                row = box.row()
                row.prop(lt, "display_tab_unwrap", text="", icon='TRIA_RIGHT')

            row.label("UVTools...")

            if lt.display_tab_unwrap:

                col = layout.column(align=True)
                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)

                row.operator("mesh.mark_seam").clear = False
                row.operator("mesh.mark_seam", text="Clear Seam").clear = True

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.operator("uv.copy_uv")
                row.operator("uv.paste_uv")

                row = col_top.row(align=True)
                row.operator("uv.copy_uv_sel_seq", "Copy UV Sel. Seq.")
                row.operator("uv.paste_uv_sel_seq", "Paste UV Sel. Seq.")

                row = col_top.row(align=True)
                row.menu("uv.copy_uv_map", "Copy UV Map")
                row.menu("uv.paste_uv_map", "Paste UV Map")

                box = col.column(align=True).box().column()
                col_top = box.column(align=True)

                row = col_top.row(align=True)
                row.alignment = 'CENTER'
                row.operator("uv.reproject_image", text="Reproject Image")


# Unwrap  ######-------------------------------------------------
# Unwrap  ######-------------------------------------------------

                if lt.display_tab_unwrapset:
                    box = layout.box()
                    row = box.row()
                    row.prop(lt, "display_tab_unwrapset", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    box = layout.box()
                    row = box.row()
                    row.prop(lt, "display_tab_unwrapset", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

                row.label("Unwrap...")

                if lt.display_tab_unwrapset:

                    col = layout.column(align=True)
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("uv.unwrap", text="Unwrap")
                    row.operator("uv.reset", text="Reset")

                    row = col_top.row(align=True)
                    row.operator("uv.smart_project", text="Smart UV Project")

                    row = col_top.row(align=True)
                    row.operator("uv.lightmap_pack", text="Lightmap Pack")

                    row = col_top.row(align=True)
                    row.operator("uv.follow_active_quads", text="Follow Active Quads")

                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("uv.cube_project", text="Cube Project")

                    row = col_top.row(align=True)
                    row.operator("uv.cylinder_project", text="Cylinder Project")

                    row = col_top.row(align=True)
                    row.operator("uv.sphere_project", text="Sphere Project")

                    row = col_top.row(align=True)
                    row.operator("uv.tube_uv_unwrap", text="Tube Project")

                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.operator("uv.project_from_view", text="Project from View").scale_to_bounds = False

                    row = col_top.row(align=True)
                    row.operator("uv.project_from_view", text="Project from View > Bounds").scale_to_bounds = True


# TexSpace / Freestyle  ######-------------------------------------------------
# TexSpace / Freestyle  ######-------------------------------------------------

                if lt.display_tab_uvnext:
                    box = layout.box()
                    row = box.row()
                    row.prop(lt, "display_tab_uvnext", text="", icon='DISCLOSURE_TRI_DOWN_VEC')
                else:
                    box = layout.box()
                    row = box.row()
                    row.prop(lt, "display_tab_uvnext", text="", icon='DISCLOSURE_TRI_RIGHT_VEC')

                row.label("TexSpace... / Freestyle")

                if lt.display_tab_uvnext:

                    col = layout.column(align=True)
                    box = col.column(align=True).box().column()
                    col_top = box.column(align=True)

                    row = col_top.row(align=True)
                    row.label(text="Texture Space:")

                    row = col_top.row(align=True)
                    row.operator("transform.translate", text="Move").texture_space = True
                    row.operator("mesh.mark_seam", text="Scale").clear = True

                    col_top = box.column(align=True)
                    row = col_top.row(align=True)
                    row.label(text="Freestyle:")

                    row = col_top.row(align=True)
                    row.operator("mesh.mark_freestyle_face", text="Mark Face").clear = False
                    row.operator("mesh.mark_freestyle_face", text="Clear Face").clear = True


############------------############
############  REGISTER  ############
############------------############


def register():
    bpy.utils.register_class(META_TAB_UVS)
    bpy.utils.register_class(DropdownMetaTool_UV_Props)
    bpy.types.WindowManager.metawindowtool_uv = bpy.props.PointerProperty(type=DropdownMetaTool_UV_Props)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
