'''
BEGIN GPL LICENSE BLOCK

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

END GPL LICENCE BLOCK
'''

bl_info = {  
 "name": "calculate length and angles",  
 "author": "Diego Quevedo ( http://doshape.com/ )",  
 "version": (1, 0),  
 "blender": (2, 7 , 3),  
 "location": "View3D > EditMode > ToolShelf",  
 "description": "calculate length and angles",  
 "warning": "",  
 "wiki_url": "",  
 "tracker_url": "",  
 "category": "Mesh"} 

import bpy
import bmesh
import mathutils
import math
from bpy.props import *  

class MessageOperator(bpy.types.Operator):
    bl_idname = "error.message"
    bl_label = "Message"
    type = StringProperty()
    message = StringProperty()
 
    def execute(self, context):
        self.report({'INFO'}, self.message)
        print(self.message)
        return {'FINISHED'}
 
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_popup(self, width=400, height=200)
 
    def draw(self, context):
        self.layout.label("A message has arrived")
        row = self.layout.split(0.25)
        row.prop(self, "type")
        row.prop(self, "message")
        row = self.layout.split(0.80)
        row.label("") 
        row.operator("error.ok")
 
#
#   The OK button in the error dialog

bpy.utils.register_class(MessageOperator)


def calcularangulos(lado1,lado2,lado3):
    print("calculando angulos")
    l1 = lado1
    l2 = lado2
    l3 = lado3
    #formula para calcular :     
    #angulo1 =  arccos((x2 + y2 - z2)/2xy)
    a1= (l1*l1)+(l2*l2)-(l3*l3)
    b1= (2*l1*l2)
    
    #print(a)
    #print(b)
    angulo1_radianes = math.acos(a1/b1)
    print("angulo1 en radianes: " + str(angulo1_radianes))
    pi = math.pi # constante de pi
    
    # convertimos los radianes a angulos
    angulo1_grados = (180 * angulo1_radianes) / pi
    print("angulo1 en grados: " + str(angulo1_grados))
    
    ###########################################################
    #angulo2 =  arccos((y2 + z2 - x2)/2yz)
    a2= (l2*l2)+(l3*l3)-(l1*l1)
    b2= (2*l2*l3)
    
    #print(a)
    #print(b)
    angulo2_radianes = math.acos(a2/b2)
    print("angulo2 en radianes: " + str(angulo2_radianes))

        # convertimos los radianes a angulos
    angulo2_grados = (180 * angulo2_radianes) / pi
    print("angulo2 en grados: " + str(angulo2_grados))
    
            
    ###########################################################
    #angulo3 =  arccos((x2 + z2 - y2)/2xz)
    a3= (l1*l1)+(l3*l3)-(l2*l2)
    b3= (2*l1*l3)
    
    #print(a)
    #print(b)
    angulo3_radianes = math.acos(a3/b3)
    print("angulo3 en radianes: " + str(angulo3_radianes))

        # convertimos los radianes a angulos
    angulo3_grados = (180 * angulo3_radianes) / pi
    print("angulo3 en grados: " + str(angulo3_grados))
    
    bpy.ops.error.message('INVOKE_DEFAULT', 
        type = "Angles",
        message = 'angle 1 : ' + str(angulo1_grados) + "   " + 'angle 2 : ' + str(angulo2_grados ) + "   " +'angle 3 : ' + str(angulo3_grados) )
     

           
class angle_length_calcOperator(bpy.types.Operator):
    "calcula el largo y angulo"
    bl_idname = 'mesh.angle_length_calc'
    bl_label = 'show length and angle'
    bl_description  = "Calcula el angulo y largo de 3 caras seleccionadas"
    bl_options = {'REGISTER', 'UNDO'}
    
    def main(self, context):   



         ##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################   
        obj = bpy.context.object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        vertices = [v for v in bm.verts if (v.select and not v.hide)]

        if len(vertices)!= 3:
            bpy.ops.error.message('INVOKE_DEFAULT', 
                type = "Error",
                message = 'Select 3 Vertices')
                        
        else:
                
            v1,v2,v3 = [v for v in vertices]
            print("cordenada vertice  " + str(v1))
            print("cordenada vertice  " + str(v2))
            print("cordenada vertice  " + str(v3))
            #distancia v1v2 

            l1 = math.sqrt(math.fabs((((((v2.co.x)-(v1.co.x))**2))+((((v2.co.y)-(v1.co.y))**2))+((((v2.co.z)-(v1.co.z))**2)))))
                        
            print("distancia entre vertices v1_v2 : " + str(l1))
            
            #distancia v1v3 
                
            l2 = math.sqrt(math.fabs((((((v3.co.x)-(v1.co.x))**2))+((((v3.co.y)-(v1.co.y))**2))+((((v3.co.z)-(v1.co.z))**2)))))
                        
            print("distancia entre vertices v1_v3 : " + str(l2))
            
            
            #distancia v2v3  # este es el lado opuesto
                
            l3 = math.sqrt(math.fabs((((((v3.co.x)-(v2.co.x))**2))+((((v3.co.y)-(v2.co.y))**2))+((((v3.co.z)-(v2.co.z))**2)))))
                        
            print("distancia entre vertices v2_v3 : " + str(l3))
            
            

            l2 = math.sqrt(math.fabs((((((v3.co.x)-(v1.co.x))**2))+((((v3.co.y)-(v1.co.y))**2))+((((v3.co.z)-(v1.co.z))**2)))))

            print("distancia entre vertices v1_v3 : " + str(l2))



            l3 = math.sqrt(math.fabs((((((v3.co.x)-(v2.co.x))**2))+((((v3.co.y)-(v2.co.y))**2))+((((v3.co.z)-(v2.co.z))**2)))))

            print("distancia entre vertices v2_v3 : " + str(l3))

            bpy.ops.error.message('INVOKE_DEFAULT', 
                type = "Lengh",
                message = 'length 1 : ' + str(l1) + "   " + 'length 2 : ' + str(l2) + "   " +'length 3 : ' + str(l3) )
             

               #####################################   
            #llamo a la funcion que calcula los angulos:
            calcularangulos(l1,l2,l3)  #funcionando

        ## actualizar toda la malla
            bmesh.update_edit_mesh(me, True)
            
            
        bpy.ops.mesh.remove_doubles()

    @classmethod
    def poll(self, context):
        obj = context.active_object
        return all([obj is not None, obj.type == 'MESH', obj.mode == 'EDIT'])

    def execute(self, context):
        
        self.main(context)
        return {'FINISHED'}  
    
    
class angle_length_calcOperatorPanel(bpy.types.Panel):
	#bl_category = "Bisector"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    #bl_context = "editmode"
    bl_label = "calculate length and angles"
    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')
    
    def draw(self, context):
        
        layout = self.layout 
        row = layout.row(align=True)
        row.label(text="calculate length and angles")
        row.operator(angle_length_calcOperator.bl_idname) 


    

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()