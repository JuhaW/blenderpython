import bpy
l0 = bpy.context.user_preferences.system.solid_lights[0]
l1 = bpy.context.user_preferences.system.solid_lights[1]
l2 = bpy.context.user_preferences.system.solid_lights[2]

l0.use = True
l0.diffuse_color = (1.0, 1.0, 1.0)
l0.specular_color = (0.45796120166778564, 0.45796120166778564, 0.45796120166778564)
l0.direction = (-0.327, -0.422, -0.846)
l1.use = True
l1.diffuse_color = (1.0, 1.0, 1.0)
l1.specular_color = (0.0, 0.0, 0.0)
l1.direction = (0.284, 0.352, 0.892)
l2.use = True
l2.diffuse_color = (0.0, 0.0, 0.0)
l2.specular_color = (0.581, 0.581, 0.581)
l2.direction = (0.386, 0.068, 0.92)
