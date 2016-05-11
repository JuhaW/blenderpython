import bpy
from bpy.props import BoolProperty, IntVectorProperty
from . common import isFamily, findLightGrp, family, refreshMaterials

class SelectionOperator(bpy.types.Operator):
    """ Custom selection """
    bl_idname = "view3d.select_custom" 
    bl_label = "Custom selection"

    extend = BoolProperty(default = False)
    deselect = BoolProperty(default = False)
    toggle = BoolProperty(default = False)
    center = BoolProperty(default = False)
    enumerate = BoolProperty(default = False)
    object = BoolProperty(default = False)
    location = IntVectorProperty(default = (0,0),subtype ='XYZ', size = 2)

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D' and context.mode == 'OBJECT'
    
    def execute(self, context):
        deactivate=''
        if context.active_object:
            obname = context.active_object.name
            deactivate = obname.startswith('BLS_CONTROLLER.') or obname.startswith('BLS_LIGHT_MESH.')
            
        bpy.ops.view3d.select(extend=self.extend, deselect=self.deselect, toggle=self.toggle, center=self.center, enumerate=self.enumerate, object=self.object, location=(self.location[0] , self.location[1] ))
        if context.active_object:
            obname = context.active_object.name
            if obname.startswith('BLS_CONTROLLER.'):
                lno = obname.split('.')[1]
                lno = context.scene.objects.find('BLS_LIGHT_MESH.'+lno)
                if lno is not -1:
                    context.scene.objects[lno].select = True
                
            if deactivate or obname.startswith('BLS_CONTROLLER.') or obname.startswith('BLS_LIGHT_MESH.'):
                refreshMaterials()
                    
            context.scene.frame_current = context.scene.frame_current
            refreshMaterials()
            
        return {'FINISHED'}

    def invoke(self, context, event):
        self.location[0] = event.mouse_region_x
        self.location[1]  = event.mouse_region_y
        return self.execute(context)

def replace_shortkey( old_op_name, new_op_name) :
        wm = bpy.context.window_manager
        keyconfig = wm.keyconfigs.active
        keymap = keyconfig.keymaps['3D View']
        items = keymap.keymap_items

        item = items.get(old_op_name, None)
        while item :

                props = item.properties

                extend    = props.extend.real
                deselect  = props.deselect.real
                toggle    = props.toggle.real
                center    = props.center.real
                enumerate = props.enumerate.real
                object    = props.object.real

                item.idname = new_op_name

                props.extend    = extend 
                props.deselect  = deselect
                props.toggle    = toggle
                props.center    = center
                props.enumerate = enumerate
                props.object    = object

                item = items.get( old_op_name, None)
