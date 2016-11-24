import bpy
l0 = bpy.context.user_preferences.system.solid_lights[0]
l1 = bpy.context.user_preferences.system.solid_lights[1]
l2 = bpy.context.user_preferences.system.solid_lights[2]

l0.use = True
l0.diffuse_color = (0.6, 0.6, 0.6)
l0.specular_color = (0.05, 0.05, 0.05)
l0.direction = (-0.46, -0.658, -0.596)
l1.use = True
l1.diffuse_color = (1.0, 1.0, 1.0)
l1.specular_color = (0.45, 0.45, 0.45)
l1.direction = (0.543, 0.067, 0.837)
l2.use = True
l2.diffuse_color = (0.55, 0.55, 0.55)
l2.specular_color = (0.016, 0.016, 0.016)
l2.direction = (-0.762, 0.295, 0.576)
