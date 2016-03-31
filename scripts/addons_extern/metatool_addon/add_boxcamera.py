####################################
# SetTemplateCamera
#       v.2.1
#  (c)Ishidourou 2013
####################################
#name = SetTemplateCamera, exec_from_panel = set.tmpcamera

#!BPY
import bpy
from bpy.props import *

#bl_info = {
#    "name": "SetTemplateCamera",
#    "author": "ishidourou",
#    "version": (2, 1),
#    "blender": (2, 65, 0),
#    "location": "View3D > Toolbar and View3D",
#    "description": "SetTemplateCamera",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": '3D View'}

def objselect(objct,selection):
    if (selection == 'ONLY'):
        bpy.ops.object.select_all(action='DESELECT')
    bpy.context.scene.objects.active = objct
    objct.select = True

def makecamera(loc,rot):
    bpy.ops.object.camera_add(view_align=True, enter_editmode=False, 
                            location= loc,
                            rotation= rot,
                            layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True)
                            )

    camera = bpy.context.object
    camera.data.type = 'ORTHO'
    camera.data.ortho_scale = 10
    camera.name = 'Template Camera'
    #camera.hide_select = True
    #camera.hide = True
    return camera

def makeempty(loc,rot):
    bpy.ops.object.empty_add(type='PLAIN_AXES',
                        view_align=False,
                        location= loc,
                        rotation= rot,
                        layers=(False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False)
                        )
    empty = bpy.context.object
    empty.empty_draw_type = 'IMAGE'
    empty.empty_draw_size = 10
    empty.name = 'Template Empty'
    empty.color[3] = 0.3   #Transparency
    empty.show_x_ray = True
    return empty
 
    
#    Menu in tools region
#class SetTemplateCameraPanel(bpy.types.Panel):
#    bl_label = "SetTemplateCamera"
#    bl_space_type = "VIEW_3D"
#    bl_region_type = "TOOLS"
# 
#    def draw(self, context):
#        self.layout.operator("set.tmpcamera")

#---- main ------
class SetTemplateCamera(bpy.types.Operator):
    """Boxmodelling > add a Camera & Box to the center > change view over the timeline keyframe 1-2-3"""
    bl_idname = "set.tmpcamera"
    bl_label = "SetTemplateCamera"
    bl_options = {'REGISTER'}

    my_mode = EnumProperty(name="Template Mode:",
        items = [('SINGLE','Single','0'),
                 ('SEPARATE','3D Separate','1'),
                 ('CONTACT','3D Contact','2')],
                 default = 'SEPARATE')

    def execute(self, context):
        pi = 3.141595
        pq = pi/2
        #mq = -1*pi/2
        rtype = 'BUILTIN_KSI_LocRot'
        sn = bpy.context.scene
        mode = self.my_mode
         
        cloc = [(0, -10, 0),(10, 0, 0),(0, 0, 10)]
        crot = [(pq, 0, 0),(pq, 0, pq),(0, 0, 2*pq)]
        eloc = [(-5, 5, -5),(-5, -5, -5),(-5, -5, -5)]
        erot = [(pq, 0, 0),(pq, 0, pq),(0, 0, 0)]
        cname = ['Front','Side','Top']

        if mode != 'SEPARATE':
            eloc = [(-5, 0, -5),(0, -5, -5),(-5, -5, 0)]

        bpy.context.space_data.show_axis_z = True
        sn.layers[19] = True
        sn.layers[5] = True
        #sn.layers[0] = True

        sn.render.resolution_x = 1000
        sn.render.resolution_y = 1000
 
        camera = makecamera(cloc[0],crot[0])
        for i in range(3):
            sn.frame_set(i+1)
            objselect(camera,'ONLY')
            #cname[i] = camera.name
            camera.location = cloc[i]
            camera.rotation_euler = crot[i]
            bpy.ops.anim.keyframe_insert_menu(type=rtype) 

            empty = makeempty(eloc[i],erot[i])
            if i == 0:
                firstcamera = camera
                firstempty = empty
            objselect(empty,'ONLY')
            objselect(camera,'ADD')
            #bpy.ops.object.parent_set(type='OBJECT')
            if mode == 'SINGLE':
                break
        objselect(firstcamera,'ONLY')
        bpy.ops.view3d.object_as_camera()
        sn.frame_set(1)
        objselect(firstempty,'ONLY')
        
        #for i in range(3):
            #bpy.data.objects[cname[i]].hide = True

        sn.layers[19] = False
            
        print('Finished')
        return{'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

#	Registration

def register():
    #bpy.utils.register_class(SetTemplateCameraPanel)
    bpy.utils.register_class(SetTemplateCamera)

def unregister():
    #bpy.utils.unregister_class(SetTemplateCameraPanel)
    bpy.utils.unregister_class(SetTemplateCamera)

if __name__ == "__main__":
    register()
