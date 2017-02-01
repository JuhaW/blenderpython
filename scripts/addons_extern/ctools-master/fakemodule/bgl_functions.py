# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


functions = {}


###############################################################################
# glColor
###############################################################################
def glColor3b(red, green, blue): pass
def glColor3s(red, green, blue): pass
def glColor3i(red, green, blue): pass
def glColor3f(red, green, blue): pass
def glColor3d(red, green, blue): pass
def glColor3ub(red, green, blue): pass
def glColor3us(red, green, blue): pass
def glColor3ui(red, green, blue): pass
def glColor4b(red, green, blue, alpha): pass
def glColor4s(red, green, blue, alpha): pass
def glColor4i(red, green, blue, alpha): pass
def glColor4f(red, green, blue, alpha): pass
def glColor4d(red, green, blue, alpha): pass
def glColor4ub(red, green, blue, alpha): pass
def glColor4us(red, green, blue, alpha): pass
def glColor4ui(red, green, blue, alpha): pass
def glColor3bv(v): pass
def glColor3sv(v): pass
def glColor3iv(v): pass
def glColor3fv(v): pass
def glColor3dv(v): pass
def glColor3ubv(v): pass
def glColor3usv(v): pass
def glColor3uiv(v): pass
def glColor4bv(v): pass
def glColor4sv(v): pass
def glColor4iv(v): pass
def glColor4fv(v): pass
def glColor4dv(v): pass
def glColor4ubv(v): pass
def glColor4usv(v): pass
def glColor4uiv(v): pass

doc_glColor3i = \
    """Set a new color.

    :param red: Specify new red value for the current color.
    :type red: int
    :param green: Specify new green value for the current color.
    :type green: int
    :param blue: Specify new blue value for the current color.
    :type blue: int
    """

doc_glColor4i = \
    """Set a new color.

    :param red: Specify new red value for the current color.
    :type red: int
    :param green: Specify new green value for the current color.
    :type green: int
    :param blue: Specify new blue value for the current color.
    :type blue: int
    :param alpha: Specify new alpha value for the current color.
    :type alpha: int
    """

doc_glColor3iv = \
    """Set a new color.

    :param v: Specifies a pointer to an array that contains red, green,
        and blue values.
    :type v: bgl.Buffer[GL_INT]
    """

doc_glColor4iv = \
    """Set a new color.

    :param v: Specifies a pointer to an array that contains red, green,
        blue, and alpha values.
    :type v: bgl.Buffer[GL_INT]
    """

glColor3b.__doc__ = doc_glColor3i
glColor3s.__doc__ = doc_glColor3i
glColor3i.__doc__ = doc_glColor3i
glColor3f.__doc__ = doc_glColor3i.replace('int', 'float')
glColor3d.__doc__ = doc_glColor3i.replace('int', 'float')
glColor3ub.__doc__ = doc_glColor3i
glColor3us.__doc__ = doc_glColor3i
glColor3ui.__doc__ = doc_glColor3i

glColor4b.__doc__ = doc_glColor4i
glColor4s.__doc__ = doc_glColor4i
glColor4i.__doc__ = doc_glColor4i
glColor4f.__doc__ = doc_glColor4i.replace('int', 'float')
glColor4d.__doc__ = doc_glColor4i.replace('int', 'float')
glColor4ub.__doc__ = doc_glColor4i
glColor4us.__doc__ = doc_glColor4i
glColor4ui.__doc__ = doc_glColor4i

glColor3bv.__doc__ = doc_glColor3iv.replace('GL_INT', 'GL_BYTE')
glColor3sv.__doc__ = doc_glColor3iv.replace('GL_INT', 'GL_SHORT')
glColor3iv.__doc__ = doc_glColor3iv
glColor3fv.__doc__ = doc_glColor3iv.replace('GL_INT', 'GL_FLOAT')
glColor3dv.__doc__ = doc_glColor3iv.replace('GL_INT', 'GL_DOUBLE')
glColor3ubv.__doc__ = doc_glColor3iv.replace('GL_INT', 'GL_BYTE')
glColor3usv.__doc__ = doc_glColor3iv.replace('GL_INT', 'GL_SHORT')
glColor3uiv.__doc__ = doc_glColor3iv

glColor4bv.__doc__ = doc_glColor4iv.replace('GL_INT', 'GL_BYTE')
glColor4sv.__doc__ = doc_glColor4iv.replace('GL_INT', 'GL_SHORT')
glColor4iv.__doc__ = doc_glColor4iv
glColor4fv.__doc__ = doc_glColor4iv.replace('GL_INT', 'GL_FLOAT')
glColor4dv.__doc__ = doc_glColor4iv.replace('GL_INT', 'GL_DOUBLE')
glColor4ubv.__doc__ = doc_glColor4iv.replace('GL_INT', 'GL_BYTE')
glColor4usv.__doc__ = doc_glColor4iv.replace('GL_INT', 'GL_SHORT')
glColor4uiv.__doc__ = doc_glColor4iv

functions['glColor'] = [
    glColor3b,
    glColor3s,
    glColor3i,
    glColor3f,
    glColor3d,
    glColor3ub,
    glColor3us,
    glColor3ui,
    glColor4b,
    glColor4s,
    glColor4i,
    glColor4f,
    glColor4d,
    glColor4ub,
    glColor4us,
    glColor4ui,
    glColor3bv,
    glColor3sv,
    glColor3iv,
    glColor3fv,
    glColor3dv,
    glColor3ubv,
    glColor3usv,
    glColor3uiv,
    glColor4bv,
    glColor4sv,
    glColor4iv,
    glColor4fv,
    glColor4dv,
    glColor4ubv,
    glColor4usv,
    glColor4uiv,
]

###############################################################################
# glEdgeFlag
###############################################################################
def glEdgeFlag(flag):
    """flag edges as either boundary or nonboundary

    :param flag: Specifies the current edge flag value, either GL_TRUE or
        GL_FALSE. The initial value is GL_TRUE.
    :type flag: bool | int
    """


def glEdgeFlagv(flag):
    """flag edges as either boundary or nonboundary

    :param flag: Specifies a pointer to an array that contains a single
        boolean element, which replaces the current edge flag value.
    :type flag: bgl.Buffer[GL_BYTE | GL_SHORT | GL_INT]
    """


functions['glEdgiFlag'] = [
    glEdgeFlag,
    glEdgeFlagv,
]

###############################################################################
# glEvalCoord
###############################################################################
def glEvalCoord1f(u): pass
def glEvalCoord1d(u): pass
def glEvalCoord2f(u, v): pass
def glEvalCoord2d(u, v): pass
def glEvalCoord1fv(u): pass
def glEvalCoord1dv(u): pass
def glEvalCoord2fv(u): pass
def glEvalCoord2dv(u): pass

doc_glEvalCoord1f = \
    """evaluate enabled one- and two-dimensional maps
    :param u: Specifies a value that is the domain coordinate  u to the basis
        function defined in a previous glMap1 or glMap2 command.
    :type u: float
    """

doc_glEvalCoord2f = \
    """evaluate enabled one- and two-dimensional maps
    :param u: Specifies a value that is the domain coordinate  u to the basis
        function defined in a previous glMap1 or glMap2 command.
    :type u: float
    :param v: Specifies a value that is the domain coordinate v to the basis
        function defined in a previous glMap2 command. This argument is not
        present in a glEvalCoord1 command.
    :type v: float
    """

doc_glEvalCoord1fv = \
    """evaluate enabled one- and two-dimensional maps
    :param u: Specifies a pointer to an array containing either one or two
        domain coordinates. The first coordinate is u. The second coordinate
        is v, which is present only in glEvalCoord2 versions.
    :type u: bgl.Buffer[GL_FLOAT]
    """

glEvalCoord1f.__doc__ = doc_glEvalCoord1f
glEvalCoord1d.__doc__ = doc_glEvalCoord1f
glEvalCoord2f.__doc__ = doc_glEvalCoord2f
glEvalCoord2d.__doc__ = doc_glEvalCoord2f
glEvalCoord1fv.__doc__ = doc_glEvalCoord1fv
glEvalCoord1dv.__doc__ = doc_glEvalCoord1fv.replace('GL_FLOAT', 'GL_DOUBLE')
glEvalCoord2fv.__doc__ = doc_glEvalCoord1fv
glEvalCoord2dv.__doc__ = doc_glEvalCoord1fv.replace('GL_FLOAT', 'GL_DOUBLE')

functions['glEvalCoord'] = [
    glEvalCoord1f,
    glEvalCoord1d,
    glEvalCoord2f,
    glEvalCoord2d,
    glEvalCoord1fv,
    glEvalCoord1dv,
    glEvalCoord2fv,
    glEvalCoord2dv,
]

###############################################################################
# glEvalMesh
###############################################################################
def glEvalMesh1(mode, i1, i2):
    """compute a one- or two-dimensional grid of points or lines

    :param mode: In glEvalMesh1, specifies whether to compute a
        one-dimensional mesh of points or lines.
    :type mode: int
    :    enum in [GL_POINT, GL_LINE]
    :param i1: Specify the first integer value for grid domain variable i.
    :type i1: int
    :param i2: Specify the last integer value for grid domain variable i.
    :type i2: int
    """


def glEvalMesh2(mode, i1, i2, j1, j2):
    """compute a one- or two-dimensional grid of points or lines

    :param mode: In glEvalMesh2, specifies whether to compute a
        two-dimensional mesh of points, lines, or polygons.
    :type mode: int
    :    enum in [GL_POINT, GL_LINE, GL_FILL]
    :param i1: Specify the first integer value for grid domain variable i.
    :type i1: int
    :param i2: Specify the last integer value for grid domain variable i.
    :type i2: int
    :param j1: Specify the first integer value for grid domain variable j.
    :type j1: int
    :param j2: Specify the last integer value for grid domain variable j.
    :type j2: int
    """

functions['glEvalMesh'] = [
    glEvalMesh1,
    glEvalMesh2,
]

###############################################################################
# glEvalPoint
###############################################################################
def glEvalPoint1(i):
    """generate and evaluate a single point in a mesh

    :param i: Specifies the integer value for grid domain variable i.
    :type i: int
    """


def glEvalPoint2(i, j):
    """generate and evaluate a single point in a mesh

    :param i: Specifies the integer value for grid domain variable i.
    :type i: int
    :param j: Specifies the integer value for grid domain variable j.

    :type j: int
    """

functions['glEvalPoint'] = [
    glEvalPoint1,
    glEvalPoint2,
]

###############################################################################
# glFog
###############################################################################
def glFogi(pname, param): pass
def glFogf(pname, param): pass
def glFogiv(pname, params): pass
def glFogfv(pname, params): pass

doc_glFog = \
    """specify fog parameters

    :param pname: Specifies a single-valued fog parameter.
        enum in [GL_FOG_MODE, GL_FOG_DENSITY, GL_FOG_START, GL_FOG_END,
        GL_FOG_INDEX, GL_FOG_COORD]
    :type pname: int
    :param param: Specifies the value that pname will be set to.
    :type param: int
    """

doc_glFogv = \
    """specify fog parameters

    :param pname: Specifies a fog parameter.
        enum in [GL_FOG_MODE, GL_FOG_DENSITY, GL_FOG_START, GL_FOG_END,
        GL_FOG_INDEX, GL_FOG_COLOR, GL_FOG_COORD_SRC]
    :type pname: int
    :param params: Specifies the value or values to be assigned to pname.
        GL_FOG_COLOR requires an array of four values. All other parameters
        accept an array containing only a single value.
    :type params: bgl.Buffer[GL_INT]
    """

glFogi.__doc__ = doc_glFog
glFogf.__doc__ = doc_glFog.replace(':type param: int', ':type param: float')
glFogiv.__doc__ = doc_glFogv
glFogfv.__doc__ = doc_glFogv.replace('GL_INT', 'GL_FLOAT')

functions['glFog'] = [
    glFogi,
    glFogf,
    glFogiv,
    glFogfv
]

###############################################################################
# glGet
###############################################################################
def glGetBooleanv(pname, params): pass
def glGetIntegerv(pname, params): pass
def glGetFloatv(pname, params): pass
def glGetDoublev(pname, params): pass

doc_glGet = \
    """return the value or values of a selected parameter

    :param pname: Specifies the parameter value to be returned.
        The symbolic constants in the list below are accepted.
    :type pname: int
    :param params: Returns the value or values of the specified parameter.
    :type params: bgl.Buffer[GL_BYTE]
    """

glGetBooleanv.__doc__ = doc_glGet
glGetIntegerv.__doc__ = doc_glGet.replace('GL_BYTE', 'GL_INT')
glGetFloatv.__doc__ = doc_glGet.replace('GL_BYTE', 'GL_FLOAT')
glGetDoublev.__doc__ = doc_glGet.replace('GL_BYTE', 'GL_DOUBLE')


functions['glGet'] = [
    glGetBooleanv,
    glGetIntegerv,
    glGetFloatv,
    glGetDoublev,
]

###############################################################################
# glGetLight
###############################################################################
def glGetLightiv(light, pname, params): pass
def glGetLightfv(light, pname, params): pass

doc_glGetLight = \
    """return light source parameter values

    :param light: Specifies a light source.
        The number of possible lights depends on the implementation,
        but at least eight lights are supported.
        They are identified by symbolic names of the form GL_LIGHT i where i
        ranges from 0 to the value of GL_MAX_LIGHTS - 1.
    :type light: int
    :param pname: Specifies a light source parameter for light.
        enum in [ GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_POSITION,
        GL_SPOT_DIRECTION, GL_SPOT_EXPONENT, GL_SPOT_CUTOFF,
        GL_CONSTANT_ATTENUATION, GL_LINEAR_ATTENUATION,
        GL_QUADRATIC_ATTENUATION]
    :type pname: int
    :param params: Returns the requested data.
    :type params: bgl.Buffer[GL_INT]
    """

glGetLightiv.__doc__ = doc_glGetLight
glGetLightfv.__doc__ = doc_glGetLight.replace('GL_INT', 'GL_FLOAT')

functions['glGetLight'] = [
    glGetLightiv,
    glGetLightfv,
]

###############################################################################
# glGetMap
###############################################################################
def glGetMapiv(target, query, v): pass
def glGetMapfv(target, query, v): pass
def glGetMapdv(target, query, v): pass

doc_glGetMap = \
    """return evaluator parameters

    :param target: Specifies the symbolic name of a map.
        enum in [GL_MAP1_COLOR_4, GL_MAP1_INDEX, GL_MAP1_NORMAL,
        GL_MAP1_TEXTURE_COORD_1, GL_MAP1_TEXTURE_COORD_2,
        GL_MAP1_TEXTURE_COORD_3, GL_MAP1_TEXTURE_COORD_4, GL_MAP1_VERTEX_3,
        GL_MAP1_VERTEX_4, GL_MAP2_COLOR_4, GL_MAP2_INDEX, GL_MAP2_NORMAL,
        GL_MAP2_TEXTURE_COORD_1, GL_MAP2_TEXTURE_COORD_2,
        GL_MAP2_TEXTURE_COORD_3, GL_MAP2_TEXTURE_COORD_4, GL_MAP2_VERTEX_3,
        GL_MAP2_VERTEX_4]
    :type target: int
    :param query: Specifies which parameter to return.
        enum in [GL_COEFF, GL_ORDER, GL_DOMAIN]
    :type query: int
    :param v: Returns the requested data.
    :type v: bgl.Buffer[GL_INT]
    """

glGetMapiv.__doc__ = doc_glGetMap
glGetMapfv.__doc__ = doc_glGetMap.replace('GL_INT', 'GL_FLOAT')
glGetMapdv.__doc__ = doc_glGetMap.replace('GL_INT', 'GL_DOUBLE')

functions['glGetMap'] = [
    glGetMapiv,
    glGetMapfv,
    glGetMapdv,
]

###############################################################################
# glGetMaterial
###############################################################################
def glGetMaterialiv(face, pname, params): pass
def glGetMaterialfv(face, pname, params): pass

doc_glGetMaterial = \
    """return material parameters

    :param face: Specifies which of the two materials is being queried.
        GL_FRONT or GL_BACK are accepted, representing the front and back
        materials, respectively.
        enum in [GL_FRONT, GL_BACK]
    :type face: int
    :param pname: Specifies the material parameter to return.
        enum in [GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_EMISSION,
        GL_SHININESS, GL_COLOR_INDEXES]
    :type pname: int
    :param params: Returns the requested data.
    :type params: bgl.Buffer[GL_INT]
    """

glGetMaterialiv.__doc__ = doc_glGetMaterial
glGetMaterialfv.__doc__ = doc_glGetMaterial.replace('GL_INT', 'GL_FLOAT')

functions['glGetMaterial'] = [
    glGetMaterialiv,
    glGetMaterialfv,
]

###############################################################################
# glGetPixelMap
###############################################################################
def glGetPixelMapusv(map, data): pass
def glGetPixelMapuiv(map, data): pass
def glGetPixelMapfv(map, data): pass

doc_glGetPixelMap = \
    """return the specified pixel map

    :param map: Specifies the name of the pixel map to return.
        enum in [GL_PIXEL_MAP_I_TO_I, GL_PIXEL_MAP_S_TO_S,
        GL_PIXEL_MAP_I_TO_R, GL_PIXEL_MAP_I_TO_G, GL_PIXEL_MAP_I_TO_B,
        GL_PIXEL_MAP_I_TO_A, GL_PIXEL_MAP_R_TO_R, GL_PIXEL_MAP_G_TO_G,
        GL_PIXEL_MAP_B_TO_B, GL_PIXEL_MAP_A_TO_A]
    :type map: int
    :param data: Returns the pixel map contents.
    :type data: bgl.Buffer[GL_SHORT]
    """

glGetPixelMapusv.__doc__ = doc_glGetPixelMap
glGetPixelMapuiv.__doc__ = doc_glGetPixelMap.replace('GL_SHORT', 'GL_INT')
glGetPixelMapfv.__doc__ = doc_glGetPixelMap.replace('GL_SHORT', 'GL_FLOAT')

functions['glGetPixelMap'] = [
    glGetPixelMapusv,
    glGetPixelMapuiv,
    glGetPixelMapfv,
]

###############################################################################
# glGetTexEnv
###############################################################################
def glGetTexEnviv(target, pname, params): pass
def glGetTexEnvfv(target, pname, params): pass

doc_glGetTexEnv = \
    """return texture environment parameters

    :param target: Specifies a texture environment.
        enum in [GL_TEXTURE_ENV, GL_TEXTURE_FILTER_CONTROL, GL_POINT_SPRITE]
    :type target: int
    :param pname: Specifies the symbolic name of a texture environment parameter.
        enum in [GL_TEXTURE_ENV_MODE, GL_TEXTURE_ENV_COLOR,
        GL_TEXTURE_LOD_BIAS, GL_COMBINE_RGB, GL_COMBINE_ALPHA, GL_SRC0_RGB,
        GL_SRC1_RGB, GL_SRC2_RGB, GL_SRC0_ALPHA, GL_SRC1_ALPHA, GL_SRC2_ALPHA,
        GL_OPERAND0_RGB, GL_OPERAND1_RGB, GL_OPERAND2_RGB, GL_OPERAND0_ALPHA,
        GL_OPERAND1_ALPHA, GL_OPERAND2_ALPHA, GL_RGB_SCALE, GL_ALPHA_SCALE,
        GL_COORD_REPLACE]
    :type pname: int
    :param params: Returns the requested data.
    :type params: bgl.Buffer[GL_INT]
    """

glGetTexEnviv.__doc__ = doc_glGetTexEnv
glGetTexEnvfv.__doc__ = doc_glGetTexEnv.replace('GL_INT', 'GL_FLOAT')

functions['glGetTexEnv'] = [
    glGetTexEnviv,
    glGetTexEnvfv,
]

###############################################################################
# glGetTexGen
###############################################################################
def glGetTexGeniv(target, pname, params): pass
def glGetTexGenfv(target, pname, params): pass
def glGetTexGendv(target, pname, params): pass

doc_glGetTexGen = \
    """return texture coordinate generation parameters

    :param target: Specifies a texture coordinate.
        enum in [GL_S, GL_T, GL_R, GL_Q]
    :type target: int
    :param pname: Specifies the symbolic name of the value(s) to be returned.
        Must be either GL_TEXTURE_GEN_MODE or the name of one of the
        texture generation plane equations: GL_OBJECT_PLANE or GL_EYE_PLANE.
    :type pname: int
    :param params: Returns the requested data.
    :type params: bgl.Buffer[GL_INT]
    """

glGetTexGeniv.__doc__ = doc_glGetTexGen
glGetTexGenfv.__doc__ = doc_glGetTexGen.replace('GL_INT', 'GL_FLOAT')
glGetTexGendv.__doc__ = doc_glGetTexGen.replace('GL_INT', 'GL_DOUBLE')

functions['glGetTexGen'] = [
    glGetTexGeniv,
    glGetTexGenfv,
    glGetTexGendv,
]

###############################################################################
#  glGetTexLevelParameter
###############################################################################
def glGetTexLevelParameteriv(target, level, pname, params): pass
def glGetTexLevelParameterfv(target, level, pname, params): pass

doc_glGetTexLevelParameter = \
    """return texture parameter values for a specific level of detail

    :param target: Specifies the symbolic name of the target texture.
        enum in [GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D,
        GL_PROXY_TEXTURE_1D, GL_PROXY_TEXTURE_2D, GL_PROXY_TEXTURE_3D,
        GL_TEXTURE_CUBE_MAP_POSITIVE_X, GL_TEXTURE_CUBE_MAP_NEGATIVE_X,
        GL_TEXTURE_CUBE_MAP_POSITIVE_Y, GL_TEXTURE_CUBE_MAP_NEGATIVE_Y,
        GL_TEXTURE_CUBE_MAP_POSITIVE_Z, GL_TEXTURE_CUBE_MAP_NEGATIVE_Z,
        GL_PROXY_TEXTURE_CUBE_MAP]
    :type target: int
    :param level: Specifies the level-of-detail number of the desired image.
        Level 0 is the base image level. Level n is the nth mipmap reduction
        image.
    :type level: int
    :param pname: Specifies the symbolic name of a texture parameter.
        enum in [GL_TEXTURE_WIDTH, GL_TEXTURE_HEIGHT, GL_TEXTURE_DEPTH,
        GL_TEXTURE_INTERNAL_FORMAT, GL_TEXTURE_BORDER, GL_TEXTURE_RED_SIZE,
        GL_TEXTURE_GREEN_SIZE, GL_TEXTURE_BLUE_SIZE, GL_TEXTURE_ALPHA_SIZE,
        GL_TEXTURE_LUMINANCE_SIZE, GL_TEXTURE_INTENSITY_SIZE,
        GL_TEXTURE_DEPTH_SIZE, GL_TEXTURE_COMPRESSED,
        GL_TEXTURE_COMPRESSED_IMAGE_SIZE]
    :type pname: int
    :param params: Returns the requested data.
    :type params: bgl.Buffer[GL_INT]
    """

glGetTexLevelParameteriv.__doc__ = doc_glGetTexLevelParameter
glGetTexLevelParameterfv.__doc__ = doc_glGetTexLevelParameter.replace(
    'GL_INT', 'GL_FLOAT')

functions['glGetTexLevelParameter'] = [
    glGetTexLevelParameteriv,
    glGetTexLevelParameterfv,
]

###############################################################################
# glGetTexParameter
###############################################################################
def glGetTexParameteriv(target, pname, params): pass
def glGetTexParameterfv(target, pname, params): pass

doc_glGetTexParameter = \
    """return texture parameter values

    :param target: Specifies the symbolic name of the target texture.
        enum in [GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D,
        GL_TEXTURE_CUBE_MAP]
    :type target: int
    :param pname: Specifies the symbolic name of a texture parameter.
        enum in [GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MIN_FILTER,
        GL_TEXTURE_MIN_LOD, GL_TEXTURE_MAX_LOD, GL_TEXTURE_BASE_LEVEL,
        GL_TEXTURE_MAX_LEVEL, GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T,
        GL_TEXTURE_WRAP_R, GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_PRIORITY,
        GL_TEXTURE_RESIDENT, GL_TEXTURE_COMPARE_MODE,
        GL_TEXTURE_COMPARE_FUNC, GL_DEPTH_TEXTURE_MODE, GL_GENERATE_MIPMAP]
    :type pname: int
    :param params: Returns the texture parameters.
    :type params: bgl.Buffer[GL_INT]
    """

glGetTexParameteriv.__doc__ = doc_glGetTexParameter
glGetTexParameterfv.__doc__ = doc_glGetTexParameter.replace(
    'GL_INT', 'GL_FLOAT')

functions['glGetTexParameter'] = [
    glGetTexParameteriv,
    glGetTexParameterfv,
]

###############################################################################
# glIndex
###############################################################################
def glIndexs(c): pass
def glIndexi(c): pass
def glIndexf(c): pass
def glIndexd(c): pass
def glIndexub(c): pass
def glIndexsv(c): pass
def glIndexiv(c): pass
def glIndexfv(c): pass
def glIndexdv(c): pass
def glIndexubv(c): pass

doc_glIndex = \
    """set the current color index

    :param c: Specifies the new value for the current color index.
    :type c: int
    """

doc_glIndexv = \
    """set the current color index

    :param c: Specifies a pointer to a one-element array that contains
        the new value for the current color index.
    :type c: bgl.Buffer[GL_SHORT]
    """

glIndexs.__doc__ = doc_glIndex
glIndexi.__doc__ = doc_glIndex
glIndexf.__doc__ = doc_glIndex.replace('int', 'float')
glIndexd.__doc__ = doc_glIndex.replace('int', 'float')
glIndexub.__doc__ = doc_glIndex

glIndexsv.__doc__ = doc_glIndexv
glIndexiv.__doc__ = doc_glIndexv.replace('GL_SHORT', 'GL_INT')
glIndexfv.__doc__ = doc_glIndexv.replace('GL_SHORT', 'GL_FLOAT')
glIndexdv.__doc__ = doc_glIndexv.replace('GL_SHORT', 'GL_DOUBLE')
glIndexubv.__doc__ = doc_glIndexv.replace('GL_SHORT', 'GL_BYTE')

functions['glIndex'] = [
    glIndexs,
    glIndexi,
    glIndexf,
    glIndexd,
    glIndexub,
    glIndexsv,
    glIndexiv,
    glIndexfv,
    glIndexdv,
    glIndexubv,
]

###############################################################################
# glLight
###############################################################################
def glLighti(light, pname, params): pass
def glLightf(light, pname, params): pass

doc_glLight = \
    """set light source parameters

    :param light: Specifies a light. The number of lights depends on the
        implementation, but at least eight lights are supported. They are
        identified by symbolic names of the form GL_LIGHT i, where i ranges
        from 0 to the value of GL_MAX_LIGHTS - 1.
    :type light: int
    :param pname: Specifies a single-valued light source parameter for light.
        enum in [ GL_SPOT_EXPONENT, GL_SPOT_CUTOFF, GL_CONSTANT_ATTENUATION,
        GL_LINEAR_ATTENUATION, GL_QUADRATIC_ATTENUATION]
    :type pname: int
    :param params: Specifies the value that parameter pname of light source
        light will be set to.
    :type params: int
    """

glLighti.__doc__ = doc_glLight
glLightf.__doc__ = doc_glLight.replace(
    ':type params: int', ':type params: float')

functions['glLight'] = [
    glLighti,
    glLightf,
]

###############################################################################
# glLightModel
###############################################################################
def glLightModeli(pname, param): pass
def glLightModelf(pname, param): pass
def glLightModeliv(pname, params): pass
def glLightModelfv(pname, params): pass

doc_glLightModel = \
    """set the lighting model parameters

    :param pname: Specifies a single-valued lighting model parameter.
        enum in [ GL_LIGHT_MODEL_LOCAL_VIEWER, GL_LIGHT_MODEL_COLOR_CONTROL,
        GL_LIGHT_MODEL_TWO_SIDE]
    :type pname: int
    :param param: Specifies the value that param will be set to.
    :type param: int
    """

doc_glLightModelv = \
    """set the lighting model parameters

    :param pname: Specifies a single-valued lighting model parameter.
        enum in [ GL_LIGHT_MODEL_LOCAL_VIEWER, GL_LIGHT_MODEL_COLOR_CONTROL,
        GL_LIGHT_MODEL_TWO_SIDE]
    :type pname: int
    :param param: Specifies a pointer to the value or values that params
        will be set to.
    :type param: bgl.Buffer[GL_INT]
    """

glLightModeli.__doc__ = doc_glLightModel
glLightModelf.__doc__ = doc_glLightModel.replace(
    ':type param: int', ':type param: float')
glLightModeliv.__doc__ = doc_glLightModelv
glLightModelfv.__doc__ = doc_glLightModelv.replace('GL_INT', 'GL_FLOAT')

functions['glLightModel'] = [
    glLightModeli,
    glLightModelf,
    glLightModeliv,
    glLightModelfv,
]

###############################################################################
# glLoadMatrix
###############################################################################
def glLoadMatrixf(m): pass
def glLoadMatrixd(m): pass

doc_glLoadMatrix = \
    """replace the current matrix with the specified matrix

    :param m: Specifies a pointer to 16 consecutive values, which are used
        as the elements of a 4 × 4 column-major matrix.
    :type m: bgl.Buffer[GL_FLOAT]
    """

glLoadMatrixf.__doc__ = doc_glLoadMatrix
glLoadMatrixd.__doc__ = doc_glLoadMatrix.replace('GL_FLOAT', 'GL_DOUBLE')

functions['glLoadMatrix'] = [
    glLoadMatrixf,
    glLoadMatrixd,
]

###############################################################################
# glMap1
###############################################################################
def glMap1f(target,  u1,  u2, stride, order, points): pass
def glMap1d(target,  u1,  u2, stride, order, points): pass

doc_glMap1 = \
    """define a one-dimensional evaluator

    :param target: Specifies the kind of values that are generated by the evaluator.
        enum in [GL_MAP1_VERTEX_3, GL_MAP1_VERTEX_4, GL_MAP1_INDEX,
        GL_MAP1_COLOR_4, GL_MAP1_NORMAL, GL_MAP1_TEXTURE_COORD_1,
        GL_MAP1_TEXTURE_COORD_2, GL_MAP1_TEXTURE_COORD_3,
        GL_MAP1_TEXTURE_COORD_4]
    :type target: int
    :param u1: Specify a linear mapping of u, as presented to glEvalCoord1,
        to û , the variable that is evaluated by the equations specified by
        this command.
    :type u1: float
    :param u2: Specify a linear mapping of u, as presented to glEvalCoord1,
        to û , the variable that is evaluated by the equations specified by
        this command.
    :type u2: float
    :param stride: Specifies the number of floats or doubles between
        the beginning of one control point and the beginning of the next one
        in the data structure referenced in points.
        This allows control points to be embedded in arbitrary data structures.
        The only constraint is that the values for a particular control point
        must occupy contiguous memory locations.
    :type stride: int
    :param order: Specifies the number of control points. Must be positive.
    :type order: int
    :param points: Specifies a pointer to the array of control points.
    :type points: bgl.Buffer[GL_FLOAT]
    """

glMap1f.__doc__ = doc_glMap1
glMap1d.__doc__ = doc_glMap1.replace('GL_FLOAT', 'GL_DOUBLE')

functions['glMap1'] = [
    glMap1f,
    glMap1d,
]

###############################################################################
# glMap2
###############################################################################
doc_glMap2 = \
    """define a two-dimensional evaluator

    :param target: Specifies the kind of values that are generated by the
        evaluator.
        enum in [GL_MAP2_VERTEX_3, GL_MAP2_VERTEX_4, GL_MAP2_INDEX,
        GL_MAP2_COLOR_4, GL_MAP2_NORMAL, GL_MAP2_TEXTURE_COORD_1,
        GL_MAP2_TEXTURE_COORD_2, GL_MAP2_TEXTURE_COORD_3,
        GL_MAP2_TEXTURE_COORD_4]
    :type target: int
    :param u1: Specify a linear mapping of u, as presented to glEvalCoord2,
        to û , one of the two variables that are evaluated by the equations
        specified by this command. Initially, u1 is 0 and u2 is 1.
    :type u1: float
    :param u2: Specify a linear mapping of u, as presented to glEvalCoord2,
        to û , one of the two variables that are evaluated by the equations
        specified by this command. Initially, u1 is 0 and u2 is 1.
    :type u2: float
    :param ustride: Specifies the number of floats or doubles between the
        beginning of control point R ij and the beginning of control
        point R i + 1 ⁢ j , where i and j are the u and v control point
        indices, respectively. This allows control points to be embedded in
        arbitrary data structures. The only constraint is that the values for
        a particular control point must occupy contiguous memory locations.
        The initial value of ustride is 0.
    :type ustride: int
    :param uorder: Specifies the dimension of the control point array in the u
        axis. Must be positive. The initial value is 1.
    :type uorder: int
    :param v1: Specify a linear mapping of v, as presented to glEvalCoord2,
        to v̂ , one of the two variables that are evaluated by the equations
        specified by this command. Initially, v1 is 0 and v2 is 1.
    :type v1: float
    :param v2:  Specify a linear mapping of v, as presented to glEvalCoord2,
        to v̂ , one of the two variables that are evaluated by the equations
        specified by this command. Initially, v1 is 0 and v2 is 1.
    :type v2: float
    :param vstride: Specifies the number of floats or doubles between the
        beginning of control point R ij and the beginning of control
        point R i ⁡ j + 1 , where i and j are the u and v control point
        indices, respectively. This allows control points to be embedded in
        arbitrary data structures. The only constraint is that the values for
        a particular control point must occupy contiguous memory locations.
        The initial value of vstride is 0.
    :type vstride: int
    :param vorder: Specifies the dimension of the control point array in the
        v axis. Must be positive. The initial value is 1.
    :type vorder: int
    :param points: Specifies a pointer to the array of control points.
    :type points: bgl.Buffer[GL_FLOAT]
    """


def glMap2f(target,  u1,  u2,  ustride,  uorder,  v1,  v2,  vstride,  vorder,
            points):
    pass


def glMap2d(target,  u1,  u2,  ustride,  uorder,  v1,  v2,  vstride,  vorder,
            points):
    pass

glMap2f.__doc__ = doc_glMap2
glMap2d.__doc__ = doc_glMap2.replace('GL_FLOAT', 'GL_DOUBLE')

functions['glMap2'] = [
    glMap2f,
    glMap2d,
]

###############################################################################
# glMapGrid
###############################################################################
def glMapGrid1f(un, u1, n2): pass
def glMapGrid1d(un, u1, n2): pass
def glMapGrid2f(un, u1, n2, vn, v1, v2): pass
def glMapGrid2d(un, u1, n2, vn, v1, v2): pass

doc_glMapGrid1 = \
    """define a one- or two-dimensional mesh

    :param un: Specifies the number of partitions in the grid range interval
        [u1, u2]. Must be positive.
    :type un: int
    :param u1: Specify the mapping for integer grid domain value i = 0.
    :type u1: float
    :param n2: Specify the mapping for integer grid domain value i = un.
    :type n2: float
    """

doc_glMapGrid2 = \
    """define a one- or two-dimensional mesh

    :param un: Specifies the number of partitions in the grid range interval
        [u1, u2]. Must be positive.
    :type un: int
    :param u1: Specify the mapping for integer grid domain value i = 0.
    :type u1: float
    :param n2: Specify the mapping for integer grid domain value i = un.
    :type n2: float
    :param vn: Specifies the number of partitions in the grid range interval
        [v1, v2]
    :type vn: int
    :param v1: Specify the mapping for integer grid domain value j = 0.
    :type v1: float
    :param v2: Specify the mapping for integer grid domain value j = vn.
    :type v2: float
    """

glMapGrid1f.__doc__ = doc_glMapGrid1
glMapGrid1d.__doc__ = doc_glMapGrid1
glMapGrid2f.__doc__ = doc_glMapGrid2
glMapGrid2d.__doc__ = doc_glMapGrid2

functions['glMapGrid'] = [
    glMapGrid1f,
    glMapGrid1d,
    glMapGrid2f,
    glMapGrid2d,
]

###############################################################################
# glMultMatrix
###############################################################################
def glMultMatrixf(m): pass
def glMultMatrixd(m): pass

doc_glMultMatrix = \
    """multiply the current matrix with the specified matrix

    :param m: Points to 16 consecutive values that are used as the elements
        of a 4 × 4 column-major matrix.
    :type m: bgl.Buffer[GL_FLOAT]
    """

glMultMatrixf.__doc__ = doc_glMultMatrix
glMultMatrixd.__doc__ = doc_glMultMatrix.replace('GL_FLOAT', 'GL_DOUBL')

functions['glMultMatrix'] = [
    glMultMatrixf,
    glMultMatrixd,
]

###############################################################################
# glNormal3
###############################################################################
def glNormal3b(nx, ny, nz): pass
def glNormal3s(nx, ny, nz): pass
def glNormal3i(nx, ny, nz): pass
def glNormal3f(nx, ny, nz): pass
def glNormal3d(nx, ny, nz): pass
def glNormal3bv(v): pass
def glNormal3sv(v): pass
def glNormal3iv(v): pass
def glNormal3fv(v): pass
def glNormal3dv(v): pass

doc_glNormal = \
    """set the current normal vector

    :param nx: Specify the x coordinate of the new current normal.
        The initial value of the current normal is the unit vector, (0, 0, 1).
    :type nx: int
    :param ny: Specify the y coordinate of the new current normal.
        The initial value of the current normal is the unit vector, (0, 0, 1).
    :type ny: int
    :param nz: Specify the z coordinate of the new current normal.
        The initial value of the current normal is the unit vector, (0, 0, 1).
    :type nz: int
    """

doc_glNormalv = \
    """set the current normal vector

    :param v: Specifies a pointer to an array of three elements: the x, y,
        and z coordinates of the new current normal.
    :type v: bgl.Buffer[GL_BYTE]
    """

glNormal3b.__doc__ = doc_glNormal
glNormal3s.__doc__ = doc_glNormal
glNormal3i.__doc__ = doc_glNormal
glNormal3f.__doc__ = doc_glNormal.replace('int', 'float')
glNormal3d.__doc__ = doc_glNormal.replace('int', 'float')
glNormal3bv.__doc__ = doc_glNormalv
glNormal3sv.__doc__ = doc_glNormalv.replace('GL_BYTE', 'GL_SHORT')
glNormal3iv.__doc__ = doc_glNormalv.replace('GL_BYTE', 'GL_INT')
glNormal3fv.__doc__ = doc_glNormalv.replace('GL_BYTE', 'GL_FLOAT')
glNormal3dv.__doc__ = doc_glNormalv.replace('GL_BYTE', 'GL_DOUBLE')

functions['glNormal3'] = [
    glNormal3b,
    glNormal3s,
    glNormal3i,
    glNormal3f,
    glNormal3d,
    glNormal3bv,
    glNormal3sv,
    glNormal3iv,
    glNormal3fv,
    glNormal3dv,
]

###############################################################################
# glPixelMap
###############################################################################
def glPixelMapusv(map, mapsize, values): pass
def glPixelMapuiv(map, mapsize, values): pass
def glPixelMapfv(map, mapsize, values): pass

doc_glPixelMap = \
    """set up pixel transfer maps

    :param map: Specifies a symbolic map name.
        enum in [GL_PIXEL_MAP_I_TO_I, GL_PIXEL_MAP_S_TO_S,
        GL_PIXEL_MAP_I_TO_R, GL_PIXEL_MAP_I_TO_G, GL_PIXEL_MAP_I_TO_B,
        GL_PIXEL_MAP_I_TO_A, GL_PIXEL_MAP_R_TO_R, GL_PIXEL_MAP_G_TO_G,
        GL_PIXEL_MAP_B_TO_B, GL_PIXEL_MAP_A_TO_A]
    :type map: int
    :param mapsize: Specifies the size of the map being defined.
    :type mapsize: int
    :param values: Specifies an array of mapsize values.
    :type values: bgl.Buffer[GL_SHORT]
    """

glPixelMapusv.__doc__ = doc_glPixelMap
glPixelMapuiv.__doc__ = doc_glPixelMap.replace('GL_SHORT', 'GL_INT')
glPixelMapfv.__doc__ = doc_glPixelMap.replace('GL_SHORT', 'GL_FLOAT')

functions['glPixelMap'] = [
    glPixelMapusv,
    glPixelMapuiv,
    glPixelMapfv,
]

###############################################################################
# glPixelStore
###############################################################################
def glPixelStorei(pname, param): pass
def glPixelStoref(pname, param): pass

doc_glPixelStore = \
    """set pixel storage modes

    :param pname: Specifies the symbolic name of the parameter to be set.
        Six values affect the packing of pixel data into memory:
        enum in [GL_PACK_SWAP_BYTES, GL_PACK_LSB_FIRST, GL_PACK_ROW_LENGTH,
        GL_PACK_IMAGE_HEIGHT, GL_PACK_SKIP_PIXELS, GL_PACK_SKIP_ROWS,
        GL_PACK_SKIP_IMAGES, GL_PACK_ALIGNMENT]
        Six more affect the unpacking of pixel data from memory:
        enum in [GL_UNPACK_SWAP_BYTES, GL_UNPACK_LSB_FIRST,
        GL_UNPACK_ROW_LENGTH, GL_UNPACK_IMAGE_HEIGHT, GL_UNPACK_SKIP_PIXELS,
        GL_UNPACK_SKIP_ROWS, GL_UNPACK_SKIP_IMAGES, GL_UNPACK_ALIGNMENT]
    :type pname: int
    :param param: Specifies the value that pname is set to.
    :type param: int
    """

glPixelStorei.__doc__ = doc_glPixelStore
glPixelStoref.__doc__ = doc_glPixelStore.replace(
    ':type param: int', ':type param: float')

functions['glPixelStore'] = [
    glPixelStorei,
    glPixelStoref,
]

###############################################################################
# glPixelTransfer
###############################################################################
def glPixelTransferi(pname, param): pass
def glPixelTransferf(pname, param): pass

# この辺からenumはそのまま
doc_glPixelTransfer = \
    """set pixel transfer modes

    :param pname: Specifies the symbolic name of the pixel transfer parameter
        to be set.
        Must be one of the following:
        GL_MAP_COLOR,
        GL_MAP_STENCIL,
        GL_INDEX_SHIFT,
        GL_INDEX_OFFSET,
        GL_RED_SCALE,
        GL_RED_BIAS,
        GL_GREEN_SCALE,
        GL_GREEN_BIAS,
        GL_BLUE_SCALE,
        GL_BLUE_BIAS,
        GL_ALPHA_SCALE,
        GL_ALPHA_BIAS,
        GL_DEPTH_SCALE, or
        GL_DEPTH_BIAS.

        Additionally, if the ARB_imaging extension is supported, the
        following symbolic names are accepted:
        GL_POST_COLOR_MATRIX_RED_SCALE,
        GL_POST_COLOR_MATRIX_GREEN_SCALE,
        GL_POST_COLOR_MATRIX_BLUE_SCALE,
        GL_POST_COLOR_MATRIX_ALPHA_SCALE,
        GL_POST_COLOR_MATRIX_RED_BIAS,
        GL_POST_COLOR_MATRIX_GREEN_BIAS,
        GL_POST_COLOR_MATRIX_BLUE_BIAS,
        GL_POST_COLOR_MATRIX_ALPHA_BIAS,
        GL_POST_CONVOLUTION_RED_SCALE,
        GL_POST_CONVOLUTION_GREEN_SCALE,
        GL_POST_CONVOLUTION_BLUE_SCALE,
        GL_POST_CONVOLUTION_ALPHA_SCALE,
        GL_POST_CONVOLUTION_RED_BIAS,
        GL_POST_CONVOLUTION_GREEN_BIAS,
        GL_POST_CONVOLUTION_BLUE_BIAS, and
        GL_POST_CONVOLUTION_ALPHA_BIAS.
    :type pname: int
    :param param: Specifies the value that pname is set to.
    :type param: int
    """

glPixelTransferi.__doc__ = doc_glPixelTransfer
glPixelTransferf.__doc__ = doc_glPixelTransfer.replace(
    ':type param: int', ':type param: float')

functions['glPixelTransfer'] = [
    glPixelTransferi,
    glPixelTransferf,
]

###############################################################################
# glRasterPos
###############################################################################
def glRasterPos2s(x, y):pass
def glRasterPos2i(x, y): pass
def glRasterPos2f(x, y): pass
def glRasterPos2d(x, y): pass
def glRasterPos3s(x, y, z): pass
def glRasterPos3i(x, y, z): pass
def glRasterPos3f(x, y, z): pass
def glRasterPos3d(x, y, z): pass
def glRasterPos4s(x, y, z, w): pass
def glRasterPos4i(x, y, z, w): pass
def glRasterPos4f(x, y, z, w): pass
def glRasterPos4d(x, y, z, w): pass
def glRasterPos2sv(v): pass
def glRasterPos2iv(v): pass
def glRasterPos2fv(v): pass
def glRasterPos2dv(v): pass
def glRasterPos3sv(v): pass
def glRasterPos3iv(v): pass
def glRasterPos3fv(v): pass
def glRasterPos3dv(v): pass
def glRasterPos4sv(v): pass
def glRasterPos4iv(v): pass
def glRasterPos4fv(v): pass
def glRasterPos4dv(v): pass

doc_glRasterPos2 = \
    """specify the raster position for pixel operations

    :param x: Specify the x object coordinate for the raster position.
    :type x: int
    :param y: Specify the y object coordinate for the raster position.
    :type y: int
    """

doc_glRasterPos3 = \
    """specify the raster position for pixel operations

    :param x: Specify the x object coordinate for the raster position.
    :type x: int
    :param y: Specify the y object coordinate for the raster position.
    :type y: int
    :param z: Specify the z object coordinate for the raster position.
    :type z: int
    """

doc_glRasterPos4 = \
    """specify the raster position for pixel operations

    :param x: Specify the x object coordinate for the raster position.
    :type x: int
    :param y: Specify the y object coordinate for the raster position.
    :type y: int
    :param z: Specify the z object coordinate for the raster position.
    :type z: int
    :param w: Specify the w object coordinate for the raster position.
    :type w: int
    """

doc_glRasterPos2v = \
    """specify the raster position for pixel operations

    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x and y coordinates, respectively.
    :type v: bgl.Buffer[GL_SHORT]
    """

doc_glRasterPos3v = \
    """specify the raster position for pixel operations

    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x, y, and w coordinates, respectively.
    :type v: bgl.Buffer[GL_SHORT]
    """

doc_glRasterPos4v = \
    """specify the raster position for pixel operations

    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x, y, z, and w coordinates, respectively.
    :type v: bgl.Buffer[GL_SHORT]
    """

glRasterPos2s.__doc__ = doc_glRasterPos2
glRasterPos2i.__doc__ = doc_glRasterPos2
glRasterPos2f.__doc__ = doc_glRasterPos2.replace('int', 'float')
glRasterPos2d.__doc__ = doc_glRasterPos2.replace('int', 'float')
glRasterPos3s.__doc__ = doc_glRasterPos3
glRasterPos3i.__doc__ = doc_glRasterPos3
glRasterPos3f.__doc__ = doc_glRasterPos3.replace('int', 'float')
glRasterPos3d.__doc__ = doc_glRasterPos3.replace('int', 'float')
glRasterPos4s.__doc__ = doc_glRasterPos4
glRasterPos4i.__doc__ = doc_glRasterPos4
glRasterPos4f.__doc__ = doc_glRasterPos4.replace('int', 'float')
glRasterPos4d.__doc__ = doc_glRasterPos4.replace('int', 'float')

glRasterPos2sv.__doc__ = doc_glRasterPos2v
glRasterPos2iv.__doc__ = doc_glRasterPos2v.replace('GL_SHORT', 'GL_INT')
glRasterPos2fv.__doc__ = doc_glRasterPos2v.replace('GL_SHORT', 'GL_FLOAT')
glRasterPos2dv.__doc__ = doc_glRasterPos2v.replace('GL_SHORT', 'GL_DOUBLE')
glRasterPos3sv.__doc__ = doc_glRasterPos3v
glRasterPos3iv.__doc__ = doc_glRasterPos3v.replace('GL_SHORT', 'GL_INT')
glRasterPos3fv.__doc__ = doc_glRasterPos3v.replace('GL_SHORT', 'GL_FLOAT')
glRasterPos3dv.__doc__ = doc_glRasterPos3v.replace('GL_SHORT', 'GL_DOUBLE')
glRasterPos4sv.__doc__ = doc_glRasterPos4v
glRasterPos4iv.__doc__ = doc_glRasterPos4v.replace('GL_SHORT', 'GL_INT')
glRasterPos4fv.__doc__ = doc_glRasterPos4v.replace('GL_SHORT', 'GL_FLOAT')
glRasterPos4dv.__doc__ = doc_glRasterPos4v.replace('GL_SHORT', 'GL_DOUBLE')

functions['glRasterPos'] = [
    glRasterPos2s,
    glRasterPos2i,
    glRasterPos2f,
    glRasterPos2d,
    glRasterPos3s,
    glRasterPos3i,
    glRasterPos3f,
    glRasterPos3d,
    glRasterPos4s,
    glRasterPos4i,
    glRasterPos4f,
    glRasterPos4d,
    glRasterPos2sv,
    glRasterPos2iv,
    glRasterPos2fv,
    glRasterPos2dv,
    glRasterPos3sv,
    glRasterPos3iv,
    glRasterPos3fv,
    glRasterPos3dv,
    glRasterPos4sv,
    glRasterPos4iv,
    glRasterPos4fv,
    glRasterPos4dv,
]

###############################################################################
# glRect
###############################################################################
def glRects(x1, y1, x2, y2): pass
def glRecti(x1, y1, x2, y2): pass
def glRectf(x1, y1, x2, y2): pass
def glRectd(x1, y1, x2, y2): pass
def glRectsv(v1, v2): pass
def glRectiv(v1, v2): pass
def glRectfv(v1, v2): pass
def glRectdv(v1, v2): pass

doc_glRect = \
    """draw a rectangle

    :param x1: Specify one vertex of a rectangle.
    :type x1: int
    :param y1: Specify one vertex of a rectangle.
    :type y1: int
    :param x2: Specify the opposite vertex of the rectangle.
    :type x2: int
    :param y2: Specify the opposite vertex of the rectangle.
    :type y2: int
    """

doc_glRectv = \
    """draw a rectangle

    :param v1: Specifies a pointer to one vertex of a rectangle.
    :type v1: Bugger[GL_SHORT]
    :param v2: Specifies a pointer to the opposite vertex of the rectangle.
    :type v2: Bugger[GL_SHORT]
    """

glRects.__doc__ = doc_glRect
glRecti.__doc__ = doc_glRect
glRectf.__doc__ = doc_glRect.replace('int', 'float')
glRectd.__doc__ = doc_glRect.replace('int', 'float')
glRectsv.__doc__ = doc_glRectv
glRectiv.__doc__ = doc_glRectv.replace('GL_SHORT', 'GL_INT')
glRectfv.__doc__ = doc_glRectv.replace('GL_SHORT', 'GL_FLOAT')
glRectdv.__doc__ = doc_glRectv.replace('GL_SHORT', 'GL_DOUBLE')

functions['glRect'] = [
    glRects,
    glRecti,
    glRectf,
    glRectd,
    glRectsv,
    glRectiv,
    glRectfv,
    glRectdv,
]

###############################################################################
# glRotate
###############################################################################
def glRotatef(angle, x, y, z): pass
def glRotated(angle, x, y, z): pass

doc_glRotate = \
    """multiply the current matrix by a rotation matrix

    :param angle: Specifies the angle of rotation, in degrees.
    :type angle: float
    :param x: Specify the x coordinate of a vector.
    :type x: float
    :param y: Specify the y coordinate of a vector.
    :type y: float
    :param z: Specify the z coordinate of a vector.
    :type z: float
    """

glRotatef.__doc__ = doc_glRotate
glRotated.__doc__ = doc_glRotate

functions['glRotate'] = [
    glRotatef,
    glRotated,
]

###############################################################################
# glScale
###############################################################################
def glScalef(x, y, z): pass
def glScaled(x, y, z): pass

doc_glScale = \
    """multiply the current matrix by a general scaling matrix

    :param x: Specify scale factors along the x axis.
    :type x: float
    :param y: Specify scale factors along the y axis.
    :type y: float
    :param z: Specify scale factors along the z axis.
    :type z: float
    """

glScalef.__doc__ = doc_glScale
glScaled.__doc__ = doc_glScale

functions['glScale'] = [
    glScalef,
    glScaled,
]

###############################################################################
# glTexCoord
###############################################################################
def glTexCoord1s(s): pass
def glTexCoord1i(s): pass
def glTexCoord1f(s): pass
def glTexCoord1d(s): pass
def glTexCoord2s(s, t): pass
def glTexCoord2i(s, t): pass
def glTexCoord2f(s, t): pass
def glTexCoord2d(s, t): pass
def glTexCoord3s(s, t, r): pass
def glTexCoord3i(s, t, r): pass
def glTexCoord3f(s, t, r): pass
def glTexCoord3d(s, t, r): pass
def glTexCoord4s(s, t, r, q): pass
def glTexCoord4i(s, t, r, q): pass
def glTexCoord4f(s, t, r, q): pass
def glTexCoord4d(s, t, r, q): pass
def glTexCoord1sv(v): pass
def glTexCoord1iv(v): pass
def glTexCoord1fv(v): pass
def glTexCoord1dv(v): pass
def glTexCoord2sv(v): pass
def glTexCoord2iv(v): pass
def glTexCoord2fv(v): pass
def glTexCoord2dv(v): pass
def glTexCoord3sv(v): pass
def glTexCoord3iv(v): pass
def glTexCoord3fv(v): pass
def glTexCoord3dv(v): pass
def glTexCoord4sv(v): pass
def glTexCoord4iv(v): pass
def glTexCoord4fv(v): pass
def glTexCoord4dv(v): pass


doc_glTexCoord1 = \
    """set the current texture coordinates

    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: int
    """

doc_glTexCoord2 = \
    """set the current texture coordinates

    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: int
    :param t: Specify t texture coordinate.
        Not all parameters are present in all forms of the command.
    :type t: int
    """

doc_glTexCoord3 = \
    """set the current texture coordinates

    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: int
    :param t: Specify t texture coordinate.
        Not all parameters are present in all forms of the command.
    :type t: int
    :param r: Specify r texture coordinate.
        Not all parameters are present in all forms of the command.
    :type r: int
    """

doc_glTexCoord4 = \
    """set the current texture coordinates

    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: int
    :param t: Specify t texture coordinate.
        Not all parameters are present in all forms of the command.
    :type t: int
    :param r: Specify r texture coordinate.
        Not all parameters are present in all forms of the command.
    :type r: int
    :param q: Specify q texture coordinate.
        Not all parameters are present in all forms of the command.
    :type q: int
    """

doc_glTexCoord1v = \
    """set the current texture coordinates

    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s texture coordinate.
    :type v: bgl.Buffer[GL_SHORT]
    """

doc_glTexCoord2v = \
    """set the current texture coordinates

    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s and t texture coordinates.
    :type v: bgl.Buffer[GL_SHORT]
    """

doc_glTexCoord3v = \
    """set the current texture coordinates

    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s, t, and r texture coordinates.
    :type v: bgl.Buffer[GL_SHORT]
    """

doc_glTexCoord4v = \
    """set the current texture coordinates

    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s, t, r, and q texture coordinates.
    :type v: bgl.Buffer[GL_SHORT]
    """

glTexCoord1s.__doc__ = doc_glTexCoord1
glTexCoord1i.__doc__ = doc_glTexCoord1
glTexCoord1f.__doc__ = doc_glTexCoord1.replace('int', 'float')
glTexCoord1d.__doc__ = doc_glTexCoord1.replace('int', 'float')
glTexCoord2s.__doc__ = doc_glTexCoord2
glTexCoord2i.__doc__ = doc_glTexCoord2
glTexCoord2f.__doc__ = doc_glTexCoord2.replace('int', 'float')
glTexCoord2d.__doc__ = doc_glTexCoord2.replace('int', 'float')
glTexCoord3s.__doc__ = doc_glTexCoord3
glTexCoord3i.__doc__ = doc_glTexCoord3
glTexCoord3f.__doc__ = doc_glTexCoord3.replace('int', 'float')
glTexCoord3d.__doc__ = doc_glTexCoord3.replace('int', 'float')
glTexCoord4s.__doc__ = doc_glTexCoord4
glTexCoord4i.__doc__ = doc_glTexCoord4
glTexCoord4f.__doc__ = doc_glTexCoord4.replace('int', 'float')
glTexCoord4d.__doc__ = doc_glTexCoord4.replace('int', 'float')

glTexCoord1sv.__doc__ = doc_glTexCoord1v
glTexCoord1iv.__doc__ = doc_glTexCoord1v.replace('GL_SHORT', 'GL_INT')
glTexCoord1fv.__doc__ = doc_glTexCoord1v.replace('GL_SHORT', 'GL_SHORT')
glTexCoord1dv.__doc__ = doc_glTexCoord1v.replace('GL_SHORT', 'GL_DOUBLE')
glTexCoord2sv.__doc__ = doc_glTexCoord2v
glTexCoord2iv.__doc__ = doc_glTexCoord2v.replace('GL_SHORT', 'GL_INT')
glTexCoord2fv.__doc__ = doc_glTexCoord2v.replace('GL_SHORT', 'GL_SHORT')
glTexCoord2dv.__doc__ = doc_glTexCoord2v.replace('GL_SHORT', 'GL_DOUBLE')
glTexCoord3sv.__doc__ = doc_glTexCoord3v
glTexCoord3iv.__doc__ = doc_glTexCoord3v.replace('GL_SHORT', 'GL_INT')
glTexCoord3fv.__doc__ = doc_glTexCoord3v.replace('GL_SHORT', 'GL_SHORT')
glTexCoord3dv.__doc__ = doc_glTexCoord3v.replace('GL_SHORT', 'GL_DOUBLE')
glTexCoord4sv.__doc__ = doc_glTexCoord4v
glTexCoord4iv.__doc__ = doc_glTexCoord4v.replace('GL_SHORT', 'GL_INT')
glTexCoord4fv.__doc__ = doc_glTexCoord4v.replace('GL_SHORT', 'GL_SHORT')
glTexCoord4dv.__doc__ = doc_glTexCoord4v.replace('GL_SHORT', 'GL_DOUBLE')

functions['glTexCoord'] = [
    glTexCoord1s,
    glTexCoord1i,
    glTexCoord1f,
    glTexCoord1d,
    glTexCoord2s,
    glTexCoord2i,
    glTexCoord2f,
    glTexCoord2d,
    glTexCoord3s,
    glTexCoord3i,
    glTexCoord3f,
    glTexCoord3d,
    glTexCoord4s,
    glTexCoord4i,
    glTexCoord4f,
    glTexCoord4d,
    glTexCoord1sv,
    glTexCoord1iv,
    glTexCoord1fv,
    glTexCoord1dv,
    glTexCoord2sv,
    glTexCoord2iv,
    glTexCoord2fv,
    glTexCoord2dv,
    glTexCoord3sv,
    glTexCoord3iv,
    glTexCoord3fv,
    glTexCoord3dv,
    glTexCoord4sv,
    glTexCoord4iv,
    glTexCoord4fv,
    glTexCoord4dv,
]

###############################################################################
# glTexEnv
###############################################################################
def glTexEnvi(target, pname, param): pass
def glTexEnvf(target, pname, param): pass
def glTexEnviv(target, pname, params): pass
def glTexEnvfv(target, pname, params): pass

doc_glTexEnv = \
    """set texture environment parameters

    :param target: Specifies a texture environment.
        May be GL_TEXTURE_ENV, GL_TEXTURE_FILTER_CONTROL or GL_POINT_SPRITE.
    :type target: int
    :param pname: Specifies the symbolic name of a single-valued texture
        environment parameter.
        May be either GL_TEXTURE_ENV_MODE, GL_TEXTURE_LOD_BIAS,
        GL_COMBINE_RGB,
        GL_COMBINE_ALPHA,
        GL_SRC0_RGB,
        GL_SRC1_RGB,
        GL_SRC2_RGB,
        GL_SRC0_ALPHA,
        GL_SRC1_ALPHA,
        GL_SRC2_ALPHA,
        GL_OPERAND0_RGB,
        GL_OPERAND1_RGB,
        GL_OPERAND2_RGB,
        GL_OPERAND0_ALPHA,
        GL_OPERAND1_ALPHA,
        GL_OPERAND2_ALPHA,
        GL_RGB_SCALE,
        GL_ALPHA_SCALE, or
        GL_COORD_REPLACE.
    :type pname: int
    :param param: Specifies a single symbolic constant, one of GL_ADD,
        GL_ADD_SIGNED, GL_INTERPOLATE, GL_MODULATE, GL_DECAL,
        GL_BLEND, GL_REPLACE, GL_SUBTRACT, GL_COMBINE,
        GL_TEXTURE, GL_CONSTANT, GL_PRIMARY_COLOR, GL_PREVIOUS,
        GL_SRC_COLOR, GL_ONE_MINUS_SRC_COLOR, GL_SRC_ALPHA,
        GL_ONE_MINUS_SRC_ALPHA,
        a single boolean value for the point sprite texture coordinate replacement,
        a single floating-point value for the texture level-of-detail bias,
        or 1.0, 2.0, or 4.0 when specifying the GL_RGB_SCALE or GL_ALPHA_SCALE.
    :type param: int
    """

doc_glTexEnvv = \
    """set texture environment parameters

    :param target: Specifies a texture environment.
        May be either GL_TEXTURE_ENV, or GL_TEXTURE_FILTER_CONTROL.
    :type target: int
    :param pname: Specifies the symbolic name of a texture environment parameter.
        Accepted values are GL_TEXTURE_ENV_MODE, GL_TEXTURE_ENV_COLOR, or
        GL_TEXTURE_LOD_BIAS.
    :type pname: int
    :param params: Specifies a pointer to a parameter array that contains
        either a single symbolic constant, single floating-point number, or
        an RGBA color.
    :type params: bgl.Buffer[GL_INT]
    """

glTexEnvi.__doc__ = doc_glTexEnv
glTexEnvf.__doc__ = doc_glTexEnv.replace(
    ':type param: int', ':type param: float')
glTexEnviv.__doc__ = doc_glTexEnvv
glTexEnvfv.__doc__ = doc_glTexEnvv.replace('GL_INT', 'GL_FLOAT')

functions['glTexEnv'] = [
    glTexEnvi,
    glTexEnvf,
    glTexEnviv,
    glTexEnvfv,
]

###############################################################################
# glTexGen
###############################################################################
def glTexGeni(coord, pname, param): pass
def glTexGenf(coord, pname, param): pass
def glTexGend(coord, pname, param): pass
def glTexGeniv(coord, pname, params): pass
def glTexGenfv(coord, pname, params): pass
def glTexGendv(coord, pname, params): pass

doc_glTexGen = \
    """control the generation of texture coordinates

    :param coord: Specifies a texture coordinate.
        Must be one of GL_S, GL_T, GL_R, or GL_Q.
    :type coord: int
    :param pname: Specifies the symbolic name of the texture-coordinate
        generation function. Must be GL_TEXTURE_GEN_MODE.
    :type pname: int
    :param param: Specifies a single-valued texture generation parameter,
        one of GL_OBJECT_LINEAR, GL_EYE_LINEAR, GL_SPHERE_MAP,
        GL_NORMAL_MAP, or GL_REFLECTION_MAP.
    :type param: int
    """

doc_glTexGenv = \
    """control the generation of texture coordinates

    :param coord: Specifies a texture coordinate.
        Must be one of GL_S, GL_T, GL_R, or GL_Q.
    :type coord: int
    :param pname: Specifies the symbolic name of the texture-coordinate
        generation function or function parameters. Must be
        GL_TEXTURE_GEN_MODE, GL_OBJECT_PLANE, or GL_EYE_PLANE.
    :type pname: int
    :param params: Specifies a pointer to an array of texture generation
        parameters. If pname is GL_TEXTURE_GEN_MODE, then the array must
        contain a single symbolic constant, one of GL_OBJECT_LINEAR,
        GL_EYE_LINEAR, GL_SPHERE_MAP, GL_NORMAL_MAP, or GL_REFLECTION_MAP.
        Otherwise, params holds the coefficients for the texture-coordinate
        generation function specified by pname.
    :type params: bgl.Buffer[GL_INT]
    """

glTexGeni.__doc__ = doc_glTexGen
glTexGenf.__doc__ = doc_glTexGen.replace(
    ':type param: int', ':type param: float')
glTexGend.__doc__ = doc_glTexGen.replace(
    ':type param: int', ':type param: float')
glTexGeniv.__doc__ = doc_glTexGenv
glTexGenfv.__doc__ = doc_glTexGenv.replace('GL_INT', 'GL_FLOAT')
glTexGendv.__doc__ = doc_glTexGenv.replace('GL_INT', 'GL_DOUBLE')

functions['glTexGen'] = [
    glTexGeni,
    glTexGenf,
    glTexGend,
    glTexGeniv,
    glTexGenfv,
    glTexGendv,
]

###############################################################################
# glTexParameter
###############################################################################
doc_glTexParameter = \
    """set texture parameters

    :param target: Specifies the target texture,
        which must be either GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D,
        or GL_TEXTURE_CUBE_MAP.
    :type target: int
    :param pname: Specifies the symbolic name of a single-valued texture
    parameter. pname can be one of the following:
        GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MIN_LOD,
        GL_TEXTURE_MAX_LOD, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_MAX_LEVEL,
        GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, GL_TEXTURE_WRAP_R,
        GL_TEXTURE_PRIORITY, GL_TEXTURE_COMPARE_MODE,
        GL_TEXTURE_COMPARE_FUNC, GL_DEPTH_TEXTURE_MODE, or GL_GENERATE_MIPMAP.
    :type pname: int
    :param param: Specifies the value of pname.
    :type param: int
    """

doc_glTexParameterv = \
    """set texture parameters

    :param target: Specifies the target texture,
        which must be either GL_TEXTURE_1D, GL_TEXTURE_2D, GL_TEXTURE_3D,
        or GL_TEXTURE_CUBE_MAP.
    :type target: int
    :param pname: Specifies the symbolic name of a texture parameter.
        pname can be one of the following:
        GL_TEXTURE_MIN_FILTER, GL_TEXTURE_MAG_FILTER, GL_TEXTURE_MIN_LOD,
        GL_TEXTURE_MAX_LOD, GL_TEXTURE_BASE_LEVEL, GL_TEXTURE_MAX_LEVEL,
        GL_TEXTURE_WRAP_S, GL_TEXTURE_WRAP_T, GL_TEXTURE_WRAP_R,
        GL_TEXTURE_BORDER_COLOR, GL_TEXTURE_PRIORITY, GL_TEXTURE_COMPARE_MODE,
        GL_TEXTURE_COMPARE_FUNC, GL_DEPTH_TEXTURE_MODE, or GL_GENERATE_MIPMAP.
    :type pnames: int
    :param param: Specifies a pointer to an array where the value or values
        of pname are stored.
    :type params: bgl.Buffer[GL_INT]
    """

def glTexParameteri(target, pname, param): pass
def glTexParameterf(target, pname, param): pass
def glTexParameteriv(target, pname, params): pass
def glTexParameterfv(target, pname, params): pass

glTexParameteri.__doc__ = doc_glTexParameter
glTexParameterf.__doc__ = doc_glTexParameter.replace(
    ':type param: int', ':type param: float')
glTexParameteriv.__doc__ = doc_glTexParameterv
glTexParameterfv.__doc__ = doc_glTexParameterv.replace('GL_INT', 'GL_FLOAT')

functions['glTexParameter'] = [
    glTexParameteri,
    glTexParameterf,
    glTexParameteriv,
    glTexParameterfv,
]

###############################################################################
# glTranslate
###############################################################################
def glTranslatef(x, y, z): pass
def glTranslated(x, y, z): pass

doc_glTranslate = \
    """multiply the current matrix by a translation matrix

    :param x: Specify the x coordinate of a translation vector.
    :type x: float
    :param y: Specify the y coordinate of a translation vector.
    :type y: float
    :param z: Specify the z coordinate of a translation vector.
    :type z: float
    """

glTranslatef.__doc__ = doc_glTranslate
glTranslated.__doc__ = doc_glTranslate

functions['glTranslate'] = [
    glTranslatef,
    glTranslated,
]

###############################################################################
# glVertex
###############################################################################
def glVertex2s(x, y): pass
def glVertex2i(x, y): pass
def glVertex2f(x, y): pass
def glVertex2d(x, y): pass
def glVertex3s(x, y, z): pass
def glVertex3i(x, y, z): pass
def glVertex3f(x, y, z): pass
def glVertex3d(x, y, z): pass
def glVertex4s(x, y, z, w): pass
def glVertex4i(x, y, z, w): pass
def glVertex4f(x, y, z, w): pass
def glVertex4d(x, y, z, w): pass

def glVertex2sv(v): pass
def glVertex2iv(v): pass
def glVertex2fv(v): pass
def glVertex2dv(v): pass
def glVertex3sv(v): pass
def glVertex3iv(v): pass
def glVertex3fv(v): pass
def glVertex3dv(v): pass
def glVertex4sv(v): pass
def glVertex4iv(v): pass
def glVertex4fv(v): pass
def glVertex4dv(v): pass

doc_glVertex2 = \
    """specify a vertex

    :param x: Specify x coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type x: int
    :param y: Specify y coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type y: int
    """

doc_glVertex3 = \
    """specify a vertex

    :param x: Specify x coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type x: int
    :param y: Specify y coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type y: int
    :param z: Specify z coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type z: int
    """

doc_glVertex4 = \
    """specify a vertex

    :param x: Specify x coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type x: int
    :param y: Specify y coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type y: int
    :param z: Specify z coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type z: int
    :param w: Specify w coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type w: int
    """

doc_glVertexv = \
    """specify a vertex

    :param v: Specifies a pointer to an array of two, three, or four elements.
        The elements of a two-element array are x and y; of a three-element
        array, x, y, and z; and of a four-element array, x, y, z, and w.
    :type x: bgl.Buffer[GL_SHORT]
    """

glVertex2s.__doc__ = doc_glVertex2
glVertex2i.__doc__ = doc_glVertex2
glVertex2f.__doc__ = doc_glVertex2.replace('int', 'float')
glVertex2d.__doc__ = doc_glVertex2.replace('int', 'float')
glVertex3s.__doc__ = doc_glVertex3
glVertex3i.__doc__ = doc_glVertex3
glVertex3f.__doc__ = doc_glVertex3.replace('int', 'float')
glVertex3d.__doc__ = doc_glVertex3.replace('int', 'float')
glVertex4s.__doc__ = doc_glVertex4
glVertex4i.__doc__ = doc_glVertex4
glVertex4f.__doc__ = doc_glVertex4.replace('int', 'float')
glVertex4d.__doc__ = doc_glVertex4.replace('int', 'float')

glVertex2sv.__doc__ = doc_glVertexv
glVertex2iv.__doc__ = doc_glVertexv.replace('GL_SHORT', 'GL_INT')
glVertex2fv.__doc__ = doc_glVertexv.replace('GL_SHORT', 'GL_FLOAT')
glVertex2dv.__doc__ = doc_glVertexv.replace('GL_SHORT', 'GL_DOUBLE')
glVertex3sv.__doc__ = doc_glVertexv
glVertex3iv.__doc__ = doc_glVertexv.replace('GL_SHORT', 'GL_INT')
glVertex3fv.__doc__ = doc_glVertexv.replace('GL_SHORT', 'GL_FLOAT')
glVertex3dv.__doc__ = doc_glVertexv.replace('GL_SHORT', 'GL_DOUBLE')
glVertex4sv.__doc__ = doc_glVertexv
glVertex4iv.__doc__ = doc_glVertexv.replace('GL_SHORT', 'GL_INT')
glVertex4fv.__doc__ = doc_glVertexv.replace('GL_SHORT', 'GL_FLOAT')
glVertex4dv.__doc__ = doc_glVertexv.replace('GL_SHORT', 'GL_DOUBLE')

functions['glVertex'] = [
    glVertex2s,
    glVertex2i,
    glVertex2f,
    glVertex2d,
    glVertex3s,
    glVertex3i,
    glVertex3f,
    glVertex3d,
    glVertex4s,
    glVertex4i,
    glVertex4f,
    glVertex4d,
    glVertex2sv,
    glVertex2iv,
    glVertex2fv,
    glVertex2dv,
    glVertex3sv,
    glVertex3iv,
    glVertex3fv,
    glVertex3dv,
    glVertex4sv,
    glVertex4iv,
    glVertex4fv,
    glVertex4dv,
]
