bl_info = {
    "name": "export mesh data to TXT",
    "author": "pATRICK bOELEN",
    "version": (1, 0),
    "blender": (2, 7, 0),
    "location": "View3D > Tool Shelf",
    "description": "EXPORT MESH DATA TO TXT",
    "warning": "",
    "wiki_url": "",
    "category": "Import-Export"}


import bpy


class exportToTXT(bpy.types.Operator):
    bl_idname = "export.export_to_txt"
    bl_label = "Export To TXT"

    filepath = bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        obverts = bpy.context.active_object.data.vertices
        obfaces = bpy.context.active_object.data.polygons

        verts = []
        faces = []
        numFaces = 0
        numVerts = 0

        for vertex in obverts:
            verts.append("(" + str(vertex.co.x) + "* scale_x," + str(vertex.co.y) + "* scale_y," + str(vertex.co.z) + "* scale_z)")
            numVerts += 1

        for face in obfaces:
            faces.append(tuple(face.vertices))
            numFaces += 1

        file = open(self.filepath, 'w')
        file.write("verts = " + str(verts))
        file.write(str("\n"))
        file.write("faces = " + str(faces))
        file.write(str("\n"))
        '''
        file.write(str("numero de Vertices:   "))
        file.write(str(numVerts))
        file.write(str("\n\n\n"))
        file.write("verts = " + str(verts))
        file.write(str("\n\n\n\n\n\n\n\n\n\n\n\n"))
        file.write(str("numero de Caras:   "))
        file.write(str(numFaces))
        file.write(str("\n\n\n"))
        file.write("faces = " + str(faces))
        
        count = 0
        for t in verts:
            for i in t:
                if count == 6:
                    file.write('\n')
                    count = 0
                count += 1
                file.write(str(i)+' ')
        
      
        # write faces
        file.write('\n')
    
        for t in faces:
            fv = len(t)
            file.write(str(fv) + '  ')
            for i in t:
                file.write(str(i)+' ')
            file.write('\n')

        '''

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


class exportToTXTPanel(bpy.types.Panel):
    bl_idname = "Export_To_TXT"
    bl_label = "Export To TXT"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_category = "ORIGAMI SYMBOLS"

    def draw(self, context):
        layout = self.layout
        layout.operator("export.export_to_txt", text="Export to TXT")


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
