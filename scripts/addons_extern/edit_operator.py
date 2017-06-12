bl_info = {
    "name": "Edit Operator Source",
    "author": "scorpion81",
    "version": (1, 0),
    "blender": (2, 78, 0),
    "location": "Text Editor > Edit > Edit Operator",
    "description": "Opens source file of chosen operator, if it is an addon operator",
    "warning": "",
    "wiki_url": "",
    "category": "Development"}

import bpy, sys, inspect

def getclazz(opname):
    opid = opname.split(".")
    opmod = getattr(bpy.ops, opid[0])
    op = getattr(opmod, opid[1])
    id = op.get_rna().bl_rna.identifier
    clazz = getattr(bpy.types, id)
    return clazz 

def getmodule(opname):
    addon = True
    clazz = getclazz(opname)
    modn = clazz.__module__
    
    try: 
        line = inspect.getsourcelines(clazz)[1]
    except IOError: 
        line = -1
    except TypeError:
        line = -1
    
    if modn == 'bpy.types':
        mod = 'C operator'
        addon = False
    elif modn != '__main__':
        mod = sys.modules[modn].__file__
    else:
        addon = False
        mod = modn
        
    return mod, line, addon

def get_ops(scene, context):
    allops = []
    for opmodname in dir(bpy.ops):
        opmod = getattr(bpy.ops, opmodname)
        for o in dir(opmod):
            name = opmodname+"."+o
            clazz = getclazz(name)
            if (clazz.__module__ != 'bpy.types'):
                allops.append(name)
                
    l = sorted(allops)
    #print(l)       
    return [(y, y, "", x) for x, y in enumerate(l)]

class EditOperator(bpy.types.Operator):
    """Opens the source file of operators chosen from menu"""
    bl_idname = "text.edit_operator"
    bl_label = "Edit Operator"
    bl_property = "op"
    
    
    op = bpy.props.EnumProperty(
        name="Op",
        description="",
        items=get_ops
        )
    
    def invoke(self, context, event):
        context.window_manager.invoke_search_popup(self)
        return {'PASS_THROUGH'}

    def execute(self, context):
        path, line, addon = getmodule(self.op)
        if addon:
            self.report({'INFO'}, "Opened: "+ path)
            bpy.ops.text.open(filepath=path)
            bpy.ops.text.jump(line=line)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "Found no source for "+self.op)
            return {'CANCELLED'}
            

class EditOperatorPanel(bpy.types.Panel):
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    bl_label = "Edit"
    
    def draw(self, context):
        layout = self.layout
        layout.operator("text.edit_operator")
        #layout.operator("text.jump").line = 10
        

def register():
    bpy.utils.register_class(EditOperator)
    bpy.utils.register_class(EditOperatorPanel)

def unregister():
    bpy.utils.unregister_class(EditOperatorPanel)
    bpy.utils.unregister_class(EditOperator)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.text.edit_operator('INVOKE_DEFAULT')
