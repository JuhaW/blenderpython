import bpy


class Particle_NONE(bpy.types.Operator):
    """none brush"""
    bl_idname = "particle.none_select"
    bl_label = "select none particle brush"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.particle_edit.tool = 'NONE'
        return {'FINISHED'}

bpy.utils.register_class(Particle_NONE)


class Particle_COMB(bpy.types.Operator):
    """comb brush"""
    bl_idname = "particle.comb_select"
    bl_label = "select comb particle brush"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.particle_edit.tool = 'COMB'
        return {'FINISHED'}

bpy.utils.register_class(Particle_COMB)


class Particle_SMOOTH(bpy.types.Operator):
    """smooth brush"""
    bl_idname = "particle.smooth_select"
    bl_label = "select smooth particle brush"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.particle_edit.tool = 'SMOOTH'
        return {'FINISHED'}

bpy.utils.register_class(Particle_SMOOTH)


class Particle_ADD(bpy.types.Operator):
    """add brush"""
    bl_idname = "particle.add_select"
    bl_label = "select add particle brush"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.particle_edit.tool = 'ADD'
        return {'FINISHED'}

bpy.utils.register_class(Particle_ADD)


class Particle_LENGTH(bpy.types.Operator):
    """length brush"""
    bl_idname = "particle.length_select"
    bl_label = "select length particle brush"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.particle_edit.tool = 'LENGTH'
        return {'FINISHED'}

bpy.utils.register_class(Particle_LENGTH)


class Particle_PUFF(bpy.types.Operator):
    """puff brush"""
    bl_idname = "particle.puff_select"
    bl_label = "select puff particle brush"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.particle_edit.tool = 'PUFF'
        return {'FINISHED'}

bpy.utils.register_class(Particle_PUFF)


class Particle_CUT(bpy.types.Operator):
    """cut brush"""
    bl_idname = "particle.cut_select"
    bl_label = "select cut particle brush"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.particle_edit.tool = 'CUT'
        return {'FINISHED'}

bpy.utils.register_class(Particle_CUT)


class Particle_WEIGHT(bpy.types.Operator):
    """weight brush"""
    bl_idname = "particle.weight_select"
    bl_label = "select weight particle brush"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.particle_edit.tool = 'WEIGHT'
        return {'FINISHED'}

bpy.utils.register_class(Particle_WEIGHT)







### Selectmode

class Particle_PATH(bpy.types.Operator):
    """selectmode path"""
    bl_idname = "particle.path_select"
    bl_label = "select the path"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.particle_edit.select_mode = 'PATH'
        return {'FINISHED'}

bpy.utils.register_class(Particle_PATH)


class Particle_TIP(bpy.types.Operator):
    """selectmode tip"""
    bl_idname = "particle.tip_select"
    bl_label = "select the tip"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.particle_edit.select_mode = 'TIP'
        return {'FINISHED'}

bpy.utils.register_class(Particle_TIP)


class Particle_POINT(bpy.types.Operator):
    """selectmode point"""
    bl_idname = "particle.point_select"
    bl_label = "select the POINT"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.scene.tool_settings.particle_edit.select_mode = 'POINT'
        return {'FINISHED'}

#bpy.utils.register_class(Particle_POINT)



def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()