bl_info = {
    "name": "Vertex Paint | Generate Face Size & Paint Tools",
    "author": "Luca Scheller",
    "version": (1, 1),
    "blender": (2, 7, 3),
    "location": "3d View > Vertex Paint > Paint > Generate Face Size",
    "description": "Generate A Face Size Vertex Color Layer",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Paint"}

import bpy

# Operators


class VP_Generate_FaceSize(bpy.types.Operator):
    bl_idname = "vp.generate_facesize"
    bl_label = "Generate Face Size"
    bl_options = {"REGISTER", "UNDO"}

    Interpolated = bpy.props.BoolProperty(name='Interpolate', default=True, description='Interpolate Face Size')
    Invert = bpy.props.BoolProperty(name='Invert', default=False, description='Invert Result')
    Generate_Vertex_Group = bpy.props.BoolProperty(name='Generate Vertex Group', default=False, description='Generate Vertex Group')

    def draw(self, context):

        layout = self.layout

        layout.prop(self, 'Interpolated')
        layout.prop(self, 'Invert')
        if self.Interpolated == True:
            layout.prop(self, 'Generate_Vertex_Group')

    def execute(self, context):

        # Variables
        Area_Max = 0
        Area_Min = 1000000
        Face_Area = 0
        Face_LoopIndicesRange = 0
        Loop_Indices_KVI = {}  # Loop Indices , Key is Vertex Index
        Loop_Indices_Area_KLI = {}  # Loop Indices Area , Key is Loop Index
        Loop_Indices_AreaList_KVI = {}  # Loop Indices Area List , Key is Vertex Index
        active_obj = bpy.context.active_object
        if active_obj.data.vertex_colors.active != None:
            Vertex_Col_Layer = active_obj.data.vertex_colors.active
        else:
            Vertex_Col_Layer = active_obj.data.vertex_colors.new(name="Face_Size")
        # Get Data
        for x in active_obj.data.vertices:
            Loop_Indices_KVI[x.index] = []
            Loop_Indices_AreaList_KVI[x.index] = []

        for x in active_obj.data.polygons:
            # Get Area_Max
            if x.area > Area_Max:
                Area_Max = x.area
            if x.area < Area_Min:
                Area_Min = x.area
            # Get Raw Face_Area
            Face_Area = x.area
            # Get Raw Face Area per Loop Index
            Face_LoopIndicesRange = active_obj.data.polygons[x.index].loop_indices
            for y in Face_LoopIndicesRange:
                Loop_Indices_Area_KLI[y] = Face_Area
                VertexIndex = active_obj.data.loops[y].vertex_index
                Loop_Indices_KVI[VertexIndex].append(y)
                Loop_Indices_AreaList_KVI[VertexIndex].append(Face_Area)

        # Calc Interpolated
        if self.Interpolated == True:
            Area_Max = 0
            Area_Min = 1000000
            # Average Values
            for x in active_obj.data.loops:
                Average_Area = sum(Loop_Indices_AreaList_KVI[x.vertex_index]) / len(Loop_Indices_AreaList_KVI[x.vertex_index])
                Loop_Indices_Area_KLI[x.index] = Average_Area
                # Get Area_Max
                if Average_Area > Area_Max:
                    Area_Max = Average_Area
                if Average_Area < Area_Min:
                    Area_Min = Average_Area

        # Calc 0-1 Range + Invert
        Area_Max = Area_Max - Area_Min
        for x in Loop_Indices_Area_KLI:
            if self.Invert == True:
                Area = ((Loop_Indices_Area_KLI[x] - Area_Min) / Area_Max)
            else:
                Area = 1 - ((Loop_Indices_Area_KLI[x] - Area_Min) / Area_Max)
            Loop_Indices_Area_KLI[x] = Area

        # Set Vertex Color
        for x in active_obj.data.loops:

            # Set Vertex Col
            Face_Color = (Loop_Indices_Area_KLI[x.index], Loop_Indices_Area_KLI[x.index], Loop_Indices_Area_KLI[x.index])
            # print(Face_Color)
            Vertex_Col_Layer.data[x.index].color = Face_Color

        if self.Generate_Vertex_Group == True and self.Interpolated == True:
            # Create new Vertex Group / Reuse Existing
            if Vertex_Col_Layer.name in active_obj.vertex_groups.keys():
                Vertex_Group = active_obj.vertex_groups[Vertex_Col_Layer.name]
            else:
                Vertex_Group = active_obj.vertex_groups.new(name=Vertex_Col_Layer.name)
            active_obj.vertex_groups.active = Vertex_Group
            # Assign Values
            for x in active_obj.data.vertices:
                list = [x.index]  # add needs list
                Vertex_Group.add(list, Loop_Indices_Area_KLI[Loop_Indices_KVI[x.index][0]], "REPLACE")  # Get "First" Loop Index of Vertex Index

        return {"FINISHED"}


class VP_Convert_Vertex_Paint_To_Vertex_Group(bpy.types.Operator):
    bl_idname = "vp.convert_vertex_paint_to_vertex_group"
    bl_label = "Convert Vertex Paint Layer To Vertex Group Layer"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        # Variables
        Loop_Indices_KVI = {}  # Loop Indices , Key is Vertex Index
        Loop_Indices_ColVal_KLI = {}  # Loop Indices Color Value , Key is Loop Index
        Loop_Indices_ColValList_KVI = {}  # Loop Indices Color Value List , Key is Vertex Index
        active_obj = bpy.context.active_object
        if active_obj.data.vertex_colors.active != None:
            Vertex_Col_Layer = active_obj.data.vertex_colors.active
        else:
            self.report({'WARNING'}, "No Active Vertex Paint Layer!")
            return {"CANCELLED"}

        # Get Data
        for x in active_obj.data.vertices:
            Loop_Indices_KVI[x.index] = []
            Loop_Indices_ColValList_KVI[x.index] = []

        for x in active_obj.data.loops:
            VertexIndex = x.vertex_index
            Loop_Indices_KVI[VertexIndex].append(x.index)
            Loop_Indices_ColValList_KVI[VertexIndex].append(Vertex_Col_Layer.data[x.index].color.v)

        # Average Values
        for x in active_obj.data.loops:
            Average_ColVal = sum(Loop_Indices_ColValList_KVI[x.vertex_index]) / len(Loop_Indices_ColValList_KVI[x.vertex_index])
            Loop_Indices_ColVal_KLI[x.index] = Average_ColVal

        # Create new Vertex Group / Reuse Existing
        if Vertex_Col_Layer.name in active_obj.vertex_groups.keys():
            Vertex_Group = active_obj.vertex_groups[Vertex_Col_Layer.name]
        else:
            Vertex_Group = active_obj.vertex_groups.new(name=Vertex_Col_Layer.name)
        active_obj.vertex_groups.active = Vertex_Group
        # Assign Values
        for x in active_obj.data.vertices:
            list = [x.index]  # add needs list
            Vertex_Group.add(list, Loop_Indices_ColVal_KLI[Loop_Indices_KVI[x.index][0]], "REPLACE")  # Get "First" Loop Index of Vertex Index

        return {"FINISHED"}


class VP_Convert_Vertex_Group_To_Vertex_Paint(bpy.types.Operator):
    bl_idname = "vp.convert_vertex_group_to_vertex_paint"
    bl_label = "Convert Vertex Group To Vertex Paint Layer"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        # Variables
        Weight_ColValList_KVI = {}  # Loop Indices , Key is Vertex Index
        active_obj = bpy.context.active_object
        if active_obj.vertex_groups.active != None:
            Vertex_Group_Layer = active_obj.vertex_groups.active
        else:
            self.report({'WARNING'}, "No Active Vertex Group!")
            return {"CANCELLED"}

        # Get Data
        for x in active_obj.data.vertices:
            try:
                x.index  # Try this
                Weight_ColValList_KVI[x.index] = Vertex_Group_Layer.weight(x.index)
            except RuntimeError:
                Weight_ColValList_KVI[x.index] = 0

        # Create new Vertex Paint Layer / Reuse Existing
        if Vertex_Group_Layer.name in active_obj.data.vertex_colors.keys():
            Vertex_Paint_Layer = active_obj.data.vertex_colors[Vertex_Group_Layer.name]
        else:
            Vertex_Paint_Layer = active_obj.data.vertex_colors.new(name=Vertex_Group_Layer.name)
        active_obj.data.vertex_colors.active = Vertex_Paint_Layer
        # Assign Values
        for x in active_obj.data.loops:
            Vertex_Paint_Layer.data[x.index].color.v = Weight_ColValList_KVI[x.vertex_index]

        return {"FINISHED"}


class VP_Level(bpy.types.Operator):
    bl_idname = "vp.level"
    bl_label = "Level Vertex Colors"
    bl_options = {"REGISTER", "UNDO"}

    Offset = bpy.props.FloatProperty(name='Offset', default=0, soft_min=-10, soft_max=10, description='Offset Color Values')
    Gain = bpy.props.FloatProperty(name='Gain', default=1, min=0, soft_max=10, description='Multiply Color Values')

    def execute(self, context):

        # Variables
        active_obj = bpy.context.active_object
        if active_obj.data.vertex_colors.active != None:
            Vertex_Paint_Layer = active_obj.data.vertex_colors.active
        else:
            self.report({'WARNING'}, "No Active Vertex Group!")
            return {"CANCELLED"}

        # Assign Values
        for x in active_obj.data.loops:
            Vertex_Paint_Layer.data[x.index].color.v = Vertex_Paint_Layer.data[x.index].color.v + self.Offset
            Vertex_Paint_Layer.data[x.index].color.v = Vertex_Paint_Layer.data[x.index].color.v * self.Gain

        return {"FINISHED"}

# Operators

# Panels


def VP_GFaceSize_Convert_VP_To_VG_Panel(self, context):
    layout = self.layout
    layout.operator("vp.level", text="Level Vertex Colors")
    layout.operator("vp.generate_facesize")
    layout.operator("vp.convert_vertex_paint_to_vertex_group")


def VP_Convert_VG_To_VP_Panel(self, context):
    layout = self.layout
    layout.operator("vp.convert_vertex_group_to_vertex_paint")
"""
class VP_Paint_Tools_Panel(bpy.types.Panel):
    bl_label = "Paint Tools"
    bl_idname = "vp_paint_tools"
    #bl_space_type = 'VIEW_3D'
    #bl_region_type = 'TOOLS'
    bl_category = "Tools"
    bl_context = "vertexpaint"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator("paint.vertex_color_set", text="Set Vertex Colors")
        col.operator("paint.vertex_color_smooth", text="Smooth Vertex Colors")
        col.operator("paint.vertex_color_dirt", text="Dirty Vertex Colors")
        col.operator("vp.level", text="Level Vertex Colors")
        col.operator("vp.generate_facesize", text="Generate Face Size")
        col.operator("vp.convert_vertex_paint_to_vertex_group", text="Convert Vertex Paint Layer To Vertex Group")
"""
# Panels


def register():

    bpy.utils.register_class(VP_Level)
    bpy.utils.register_class(VP_Generate_FaceSize)
    bpy.utils.register_class(VP_Convert_Vertex_Paint_To_Vertex_Group)
    bpy.utils.register_class(VP_Convert_Vertex_Group_To_Vertex_Paint)
    # bpy.utils.register_class(VP_Paint_Tools_Panel)
    bpy.types.VIEW3D_MT_paint_vertex.append(VP_GFaceSize_Convert_VP_To_VG_Panel)
    bpy.types.VIEW3D_PT_tools_weightpaint.append(VP_Convert_VG_To_VP_Panel)


def unregister():

    # bpy.utils.unregister_class(VP_Paint_Tools_Panel)
    bpy.types.VIEW3D_PT_tools_weightpaint.remove(VP_Convert_VG_To_VP_Panel)
    bpy.types.VIEW3D_MT_paint_vertex.remove(VP_GFaceSize_Convert_VP_To_VG_Panel)
    bpy.utils.unregister_class(VP_Convert_Vertex_Paint_To_Vertex_Group)
    bpy.utils.unregister_class(VP_Convert_Vertex_Group_To_Vertex_Paint)
    bpy.utils.unregister_class(VP_Generate_FaceSize)
    bpy.utils.unregister_class(VP_Level)

if __name__ == "__main__":
    register()
