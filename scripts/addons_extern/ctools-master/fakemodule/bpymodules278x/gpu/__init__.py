GPU_DATA_1I = 1
"""one integer

:type: int
"""

GPU_DATA_1F = 2
"""one float

:type: int
"""

GPU_DATA_2F = 3
"""two floats

:type: int
"""

GPU_DATA_3F = 4
"""three floats

:type: int
"""

GPU_DATA_4F = 5
"""four floats

:type: int
"""

GPU_DATA_9F = 6
"""matrix 3x3 in column-major order

:type: int
"""

GPU_DATA_16F = 7
"""matrix 4x4 in column-major order

:type: int
"""

GPU_DATA_4UB = 8
"""four unsigned byte

:type: int
"""

GPU_DYNAMIC_OBJECT_VIEWMAT = 196609
"""A matrix that converts world coordinates to camera coordinates (see mat4_world_to_cam).
:type: matrix4x4

:type: int
"""

GPU_DYNAMIC_OBJECT_MAT = 196610
"""A matrix that converts object coordinates to world coordinates (see mat4_object_to_world).
:type: matrix4x4

:type: int
"""

GPU_DYNAMIC_OBJECT_VIEWIMAT = 196611
"""The uniform is a 4x4 GL matrix that converts coordinates
                                in camera space to world coordinates (see mat4_cam_to_world).
:type: matrix4x4

:type: int
"""

GPU_DYNAMIC_OBJECT_IMAT = 196612
"""The uniform is a 4x4 GL matrix that converts world coodinates
                                to object coordinates (see mat4_world_to_object).
:type: matrix4x4

:type: int
"""

GPU_DYNAMIC_OBJECT_COLOR = 196613
"""An RGB color + alpha defined at object level.
                                Each values between 0.0 and 1.0.
See bpy.types.Object.color.
:type: float4

:type: int
"""

GPU_DYNAMIC_OBJECT_AUTOBUMPSCALE = 196614
"""Multiplier for bump-map scaling.
:type: float

:type: int
"""

GPU_DYNAMIC_LAMP_DYNVEC = 131073
"""Represents the direction of light in camera space.
:type: float3

:type: int
"""

GPU_DYNAMIC_LAMP_DYNCO = 131074
"""Represents the position of the light in camera space.
:type: float3

:type: int
"""

GPU_DYNAMIC_LAMP_DYNIMAT = 131075
"""Matrix that converts vector in camera space to lamp space.
:type: matrix4x4

:type: int
"""

GPU_DYNAMIC_LAMP_DYNPERSMAT = 131076
"""Matrix that converts a vector in camera space to shadow buffer depth space.
mat4_perspective_to_depth is a fixed matrix defined as follow:
:type: matrix4x4

:type: int
"""

GPU_DYNAMIC_LAMP_DYNENERGY = 131077
"""See bpy.types.Lamp.energy.
:type: float

:type: int
"""

GPU_DYNAMIC_LAMP_DYNCOL = 131078
"""See bpy.types.Lamp.color.
:type: float3

:type: int
"""

GPU_DYNAMIC_LAMP_DISTANCE = 131079
"""See bpy.types.Lamp.distance.
:type: float

:type: int
"""

GPU_DYNAMIC_LAMP_ATT1 = 131080
"""See
                                bpy.types.PointLamp.linear_attenuation,
                                bpy.types.SpotLamp.linear_attenuation.
:type: float

:type: int
"""

GPU_DYNAMIC_LAMP_ATT2 = 131081
"""See
                                bpy.types.PointLamp.quadratic_attenuation,
                                bpy.types.SpotLamp.quadratic_attenuation.
:type: float

:type: int
"""

GPU_DYNAMIC_LAMP_SPOTSIZE = 131082
"""See bpy.types.SpotLamp.spot_size.
:type: float

:type: int
"""

GPU_DYNAMIC_LAMP_SPOTBLEND = 131083
"""See bpy.types.SpotLamp.spot_blend.
:type: float

:type: int
"""

GPU_DYNAMIC_LAMP_SPOTSCALE = 131084
"""Represents the SpotLamp local scale.
:type: float2

:type: int
"""

GPU_DYNAMIC_SAMPLER_2DBUFFER = 262145
"""Represents an internal texture used for certain effect
                                (color band, etc).
:type: int

:type: int
"""

GPU_DYNAMIC_SAMPLER_2DIMAGE = 262146
"""Represents a texture loaded from an image file.
:type: int

:type: int
"""

GPU_DYNAMIC_SAMPLER_2DSHADOW = 262147
"""Represents a texture loaded from a shadow buffer file.
:type: int

:type: int
"""

GPU_DYNAMIC_MIST_ENABLE = 327681
"""See bpy.types.WorldMistSettings.use_mist.
:type: float (0 or 1)

:type: int
"""

GPU_DYNAMIC_MIST_START = 327682
"""See bpy.types.WorldMistSettings.start.
See bpy.types.WorldMistSettings.depth.
:type: float

:type: int
"""

GPU_DYNAMIC_MIST_DISTANCE = 327683
"""See bpy.types.WorldMistSettings.intensity.
:type: float

:type: int
"""

GPU_DYNAMIC_MIST_INTENSITY = 327684
"""
:type: float

:type: int
"""

GPU_DYNAMIC_MIST_TYPE = 327685
"""See bpy.types.WorldMistSettings.falloff.
:type: float (used as an index into the type)

:type: int
"""

GPU_DYNAMIC_MIST_COLOR = 327686
""":type: int"""

GPU_DYNAMIC_HORIZON_COLOR = 393217
"""See bpy.types.World.horizon_color.
:type: float3

:type: int
"""

GPU_DYNAMIC_AMBIENT_COLOR = 393218
"""See bpy.types.World.ambient_color.
:type: float3

:type: int
"""

GPU_DYNAMIC_MAT_DIFFRGB = 458753
"""See bpy.types.Material.diffuse_color.
:type: float3

:type: int
"""

GPU_DYNAMIC_MAT_REF = 458754
"""See bpy.types.Material.diffuse_intensity.
:type: float

:type: int
"""

GPU_DYNAMIC_MAT_SPECRGB = 458755
"""See bpy.types.Material.specular_color.
:type: float3

:type: int
"""

GPU_DYNAMIC_MAT_SPEC = 458756
"""See bpy.types.Material.specular_intensity.
:type: float

:type: int
"""

GPU_DYNAMIC_MAT_HARD = 458757
"""See bpy.types.Material.specular_hardness.
:type: float

:type: int
"""

GPU_DYNAMIC_MAT_EMIT = 458758
"""See bpy.types.Material.emit.
:type: float

:type: int
"""

GPU_DYNAMIC_MAT_AMB = 458759
"""See bpy.types.Material.ambient.
:type: float

:type: int
"""

GPU_DYNAMIC_MAT_ALPHA = 458760
"""See bpy.types.Material.alpha.
:type: float

:type: int
"""

CD_MTFACE = 5
"""Vertex attribute is a UV Map. Data type is vector of 2 float.
There can be more than one attribute of that type, they are differenciated by name.
                            In blender, you can retrieve the attribute data with:

:type: int
"""

CD_MCOL = 6
"""Vertex attribute is color layer. Data type is vector 4 unsigned byte (RGBA).
There can be more than one attribute of that type, they are differenciated by name.
                            In blender you can retrieve the attribute data with:

:type: int
"""

CD_ORCO = 14
"""Vertex attribute is original coordinates. Data type is vector 3 float.
There can be only 1 attribute of that type per shader.
                            In blender you can retrieve the attribute data with:

:type: int
"""

CD_TANGENT = 18
"""Vertex attribute is the tangent vector. Data type is vector 4 float.
There can be only 1 attribute of that type per shader.
                            There is currently no way to retrieve this attribute data via the RNA API but a standalone
                            C function to compute the tangent layer from the other layers can be obtained from
                            blender.org.

:type: int
"""


def export_shader(scene, material):
    """Extracts the GLSL shader producing the visual effect of material in scene for the purpose of
                            reusing the shader in an external engine.
    This function is meant to be used in material exporter
                            so that the GLSL shader can be exported entirely.
    The return value is a dictionary containing the
                            shader source code and all associated data.
    The dictionary contains the following elements:
    ["fragment"]: string
    - fragment shader source code.["vertex"]: string
    - vertex shader source code.["uniforms"]: sequence
    - list of uniforms used in fragment shader, can be empty list. Each element of the
                                                sequence is a dictionary with the following elements:["varname"]: string
    - name of the uniform in the fragment shader. Always of the form 'unf<number>'.["datatype"]: integer
    - data type of the uniform variable. Can be one of the following:
    gpu.GPU_DATA_1I : use glUniform1i
    gpu.GPU_DATA_1F : use glUniform1fv
    gpu.GPU_DATA_2F : use glUniform2fv
    gpu.GPU_DATA_3F : use glUniform3fv
    gpu.GPU_DATA_4F : use glUniform4fv
    gpu.GPU_DATA_9F : use glUniformMatrix3fv
    gpu.GPU_DATA_16F : use glUniformMatrix4fv["type"]: integer
    - type of uniform, determines the origin and method of calculation. See uniform-type.
                                                                    Depending on the type, more elements will be be present.["lamp"]: bpy.types.Object
    - Reference to the lamp object from which the uniforms value are extracted.
                                                                    Set for the following uniforms types:
    gpu.GPU_DYNAMIC_LAMP_DYNVEC
    gpu.GPU_DYNAMIC_LAMP_DYNCO
    gpu.GPU_DYNAMIC_LAMP_DYNIMAT
    gpu.GPU_DYNAMIC_LAMP_DYNPERSMAT
    gpu.GPU_DYNAMIC_LAMP_DYNENERGY
    gpu.GPU_DYNAMIC_LAMP_DYNCOL
    gpu.GPU_DYNAMIC_SAMPLER_2DSHADOW
    - Notes:
    - The uniforms
                                                                            gpu.GPU_DYNAMIC_LAMP_DYNVEC,
                                                                            gpu.GPU_DYNAMIC_LAMP_DYNCO,
                                                                            gpu.GPU_DYNAMIC_LAMP_DYNIMAT and
                                                                            gpu.GPU_DYNAMIC_LAMP_DYNPERSMAT
                                                                            refer to the lamp object position and orientation,
                                                                            both of can be derived from the object world matrix:obmat = uniform["lamp"].matrix_world
    - where obmat is the mat4_lamp_to_world matrix of the lamp as a 2 dimensional array,
                                                                                the lamp world location location is in obmat[3].
    - The uniform types
                                                                            gpu.GPU_DYNAMIC_LAMP_DYNENERGY and
                                                                            gpu.GPU_DYNAMIC_LAMP_DYNCOL
                                                                            refer to the lamp data bloc that you get from:la = uniform["lamp"].data
    - from which you get lamp.energy and lamp.colorLamp duplication is not supported: if you have duplicated lamps in your scene
    - (i.e. lamp that are instantiated by dupligroup, etc), this element will only
                                                                                        give you a reference to the orignal lamp and you will not know which instance
                                                                                        of the lamp it is refering too. You can still handle that case in the exporter
                                                                                        by distributing the uniforms amongst the duplicated lamps.["image"]: bpy.types.Image
    - Reference to the image databloc.
                                                                    Set for uniform type
                                                                    gpu.GPU_DYNAMIC_SAMPLER_2DIMAGE.
                                                                    You can get the image data from:# full path to image file
    uniform["image"].filepath
    # image size as a 2-dimensional array of int
    uniform["image"].size["texnumber"]: integer
    - Channel number to which the texture is bound when drawing the object.
                                                                    Set for uniform types
                                                                    gpu.GPU_DYNAMIC_SAMPLER_2DBUFFER,
                                                                    gpu.GPU_DYNAMIC_SAMPLER_2DIMAGE and
                                                                    gpu.GPU_DYNAMIC_SAMPLER_2DSHADOW.
    - This is provided for information only: when reusing the shader outside blencer,
                                                                    you are free to assign the textures to the channel of your choice and to pass
                                                                    that number channel to the GPU in the uniform.["texpixels"]: byte array
    - texture data for uniform type gpu.GPU_DYNAMIC_SAMPLER_2DBUFFER.
                                                                    Although the corresponding uniform is a 2D sampler,
                                                                    the texture is always a 1D texture of n x 1 pixel.
                                                                    The texture size n is provided in ["texsize"] element.
                                                                    These texture are only used for computer generated texture (colorband, etc).
                                                                    The texture data is provided so that you can make a real image out of it in the exporter.["texsize"]: integer
    - horizontal size of texture for uniform type gpu.GPU_DYNAMIC_SAMPLER_2DBUFFER.
                                                                    The texture data is in ["texpixels"].["attributes"]: sequence
    - list of attributes used in vertex shader, can be empty. Blender doesn't use
                                                standard attributes except for vertex position and normal. All other vertex
                                                attributes must be passed using the generic glVertexAttrib functions.
                                                The attribute data can be found in the derived mesh custom data using RNA.
                                                Each element of the sequence is a dictionary containing the following elements:["varname"]: string
    - name of the uniform in the vertex shader. Always of the form 'att<number>'.["datatype"]: integer
    - data type of vertex attribute, can be one of the following:
    - gpu.GPU_DATA_2F: use glVertexAttrib2fv
    - gpu.GPU_DATA_3F: use glVertexAttrib3fv
    - gpu.GPU_DATA_4F: use glVertexAttrib4fv
    - gpu.GPU_DATA_4UB: use glVertexAttrib4ubv["number"]: integer
    - Generic attribute number. This is provided for information only.
                                                                    Blender doesn't use glBindAttribLocation to place generic attributes at specific location,
                                                                    it lets the shader compiler place the attributes automatically and query the
                                                                    placement with glGetAttribLocation.
                                                                    The result of this placement is returned in this element.
    - When using this shader in a render engine, you should either use
                                                                    glBindAttribLocation to force the attribute at this location or use
                                                                    glGetAttribLocation to get the placement chosen by the compiler of your GPU.["type"]: integer
    - type of the mesh custom data from which the vertex attribute is loaded.
                                                                    See attribute-type.["name"]: string or integer
    - custom data layer name, used for attribute type gpu.CD_MTFACE and gpu.CD_MCOL.
    Example:
    
    :param scene: the scene in which the material in rendered.
    :type scene: bpy.types.Scene
    :param material: the material that you want to export the GLSL shader
    :type material: bpy.types.Material
    :return: the shader source code and all associated data in a dictionary
    :rtype: dictionary
    """
