bl_info = {
    "name": "ArranjaremCurva",
    "author": "Mano-Wii",
    "version": (1, 4),
    "blender": (2, 73, 4),
    "location": "View3D > TOOLS > Mano-Wii > Dist_Mano",
    "description": "Arrange objects along a curve",
    "warning": "Select curve",
    "wiki_url" : "http://blenderartists.org/forum/showthread.php?361029-Specify-an-object-from-a-list-with-all-selectable-objects",
    "category": "Add Curve"}

import bpy
import winsound
import ctypes
import mathutils
from mathutils import Vector

def Glpoints(curve):
    Lpoints = []
    Gpoints = []
    id = 0
    for spline in (curve.data.splines):
        Lpoints.append(id)
        Lpoints[id] = []
        Gpoints.append(id)
        Gpoints[id] = []
        if len(spline.bezier_points) >= 2:
            r = spline.resolution_u + 1
            segments = len(spline.bezier_points)
            if not spline.use_cyclic_u:
                segments -= 1        
            for i in range(segments):
                inext = (i + 1) % len(spline.bezier_points)
                knot1 = spline.bezier_points[i].co
                handle1 = spline.bezier_points[i].handle_right
                handle2 = spline.bezier_points[inext].handle_left
                knot2 = spline.bezier_points[inext].co
                _points = mathutils.geometry.interpolate_bezier(knot1, handle1, handle2, knot2, r)
                Lpoints[id].extend(_points)            
        Gpoints[id] = [curve.matrix_world*vert for vert in Lpoints[id]]
        id += 1
    return Gpoints

class PaneldeArranjarObjetosNumaCurva(bpy.types.Panel) :
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_category = "Mano-Addons"
    bl_label = "Arrange Objects"
    
    @classmethod
    def poll(cls, context): 
        return (context.object is not None and
                context.object.type == 'CURVE')

    def draw(self, context) :
        layout = self.layout
        ob = context.object
        layout.prop(context.scene, "select_type", expand=True)                             
        if context.scene.select_type == '0':
            layout.column(align = True).prop_search(context.object, "objeto_arranjar", bpy.data, "objects")
        elif context.scene.select_type == '1':
            layout.column(align = True).prop_search(context.object, "objeto_arranjar", bpy.data, "groups")
        TheCol = self.layout.column(align = True)
        TheCol.prop(context.scene, "distancia_entre_objetos")            
        TheCol.operator("mesh.arranjar_numa_curva", text = "Arrange Objects")

class ArranjarObjetosNumaCurva(bpy.types.Operator):
    bl_idname = "mesh.arranjar_numa_curva"
    bl_label = "Arrange Objects"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        if bpy.context.object.objeto_arranjar == '':
            return {"FINISHED"}        
        else:
            dist  = bpy.context.scene.distancia_entre_objetos # Distance between duplicate objects
            wm = context.window_manager            
            curve = bpy.context.active_object            
            dt = 0.0
            ArranjarObjetosNumaCurva.Gpoints = Glpoints(curve)                        
            for po in self.Gpoints:
                for e in range(1,len(po)):
                    vetorx  = po[e]-po[e-1] # Vector spline section
                    dt += vetorx.length # Defined length calculation equal total length of the spline section
            self.report({'INFO'}, "TOTAL %d Objects!!!" % (dt/dist))
            ArranjarObjetosNumaCurva.qtobj = dt/dist                  
            if dt/dist > 1000: ###***PRECAUTION***###                      
                return wm.invoke_popup(self, width=220)
            return ContinueOperator.execute(self, context)

    def draw(self, context):
        if self.qtobj > 1000:
            layout = self.layout
            layout.label(text='!!!ARE YOU SURE ABOUT THAT?!!!', icon='ERROR')
            layout.label('   !!!Will have in total %d Objects!!!' % self.qtobj)        
            row = layout.row()
            row.operator("continue.op")
            row.operator("cancel.op")
            winsound.PlaySound("*", winsound.SND_ASYNC)
       
    def execute(self, context):
        return {"FINISHED"}
        
class ContinueOperator(bpy.types.Operator):
    bl_idname = "continue.op"
    bl_label = "CONTINUE"
    def execute(self, context):
        VK_ESCAPE = 0x1B
        ctypes.windll.user32.keybd_event(VK_ESCAPE)
        wm = context.window_manager
        wm.progress_begin(0, ArranjarObjetosNumaCurva.qtobj)
        if context.scene.select_type == '0':
            G_Objeto = [bpy.data.objects[bpy.context.object.objeto_arranjar]]
        elif context.scene.select_type == '1':
            G_Objeto = bpy.data.groups[bpy.context.object.objeto_arranjar].objects        
        dx = 0.0 # Length of initial calculation of section
        qt = 0 #(To see in System Console)
        dist  = bpy.context.scene.distancia_entre_objetos # Distance between duplicate objects
        for po in ArranjarObjetosNumaCurva.Gpoints:            
            for e in range(1,len(po)):
                vetorx  = po[e]-po[e-1]# Vector spline section
                dx     += vetorx.length # Defined length calculation equal total length of the spline section                
                while dx > dist: # While calculating the total length of the section is larger than the set distance proceed:       
                    for object in G_Objeto:
                        x = dx - dist # Calculating the remaining length of the section
                        obj = object.copy()            
                        bpy.context.scene.objects.link(obj)
                        obj.location = po[e] - (vetorx/vetorx.length)*x # Putting in the correct position
                        obj.rotation_mode = 'QUATERNION'
                        obj.rotation_quaternion = mathutils.Vector.to_track_quat(vetorx, 'X', 'Z') # Tracking the selected objects            
                        dx = x # Defining the new length calculation remainder of the section
                        qt+=1
                        #print('duplicate', qt)                    
                        wm.progress_update(qt)
        wm.progress_end()
        return {"FINISHED"}
    
class CancelOperator(bpy.types.Operator):
    bl_idname = "cancel.op"
    bl_label = "CANCEL"
    def execute(self, context):
        VK_ESCAPE = 0x1B
        ctypes.windll.user32.keybd_event(VK_ESCAPE)
        return {"FINISHED"}

def register():
    bpy.utils.register_module(__name__)

    bpy.types.Object.objeto_arranjar = bpy.props.StringProperty(name="")
    #bpy.types.Object.group_arranjar = bpy.props.StringProperty(name="Group", update=name_up)
    bpy.types.Scene.distancia_entre_objetos = bpy.props.FloatProperty \
      (
        name = "Dist",
        description = "Distancia entre objetos",
        default = 35.0,
        min = 0.002
      )
    bpy.types.Scene.select_type = bpy.props.EnumProperty(
        name="Type",
        description="Select object or group",
        items=[("0","OBJECT","make duplicates of a specific object"),
               ("1","GROUP","make duplicates of the objects in a group"),
              ],
              default='0')
def unregister() :

    del bpy.types.Object.objeto_arranjar
    #del bpy.types.Object.group_arranjar
    del bpy.types.Scene.distancia_entre_objetos
    del bpy.types.Scene.select_type
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__" :
    register()

                                                  