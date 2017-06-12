def glAccum(op, value):
    """Operate on the accumulation buffer.
    
    :param op: The accumulation buffer operation.
    :type op: Enumerated constant
    :param value: a value used in the accumulation buffer operation.
    :type value: float
    """


def glAlphaFunc(func, ref):
    """Specify the alpha test function.
    
    :param func: Specifies the alpha comparison function.
    :type func: Enumerated constant
    :param ref: The reference value that incoming alpha values are compared to.
                                                Clamped between 0 and 1.
    :type ref: float
    """


def glAreTexturesResident(n, textures, residences):
    """Determine if textures are loaded in texture memory
    
    :param n: Specifies the number of textures to be queried.
    :type n: int
    :param textures: Specifies an array containing the names of the textures to be queried
    :type textures: bgl.Buffer object I{type GL_INT}
    :param residences: An array in which the texture residence status in returned.
                                                The residence status of a texture named by an element of textures is
                                                returned in the corresponding element of residences.
    :type residences: bgl.Buffer object I{type GL_INT}(boolean)
    """


def glBegin(mode):
    """Delimit the vertices of a primitive or a group of like primatives
    
    :param mode: Specifies the primitive that will be create from vertices between
                                        glBegin and glEnd.
    :type mode: Enumerated constant
    """


def glBindTexture(target, texture):
    """Bind a named texture to a texturing target
    
    :param target: Specifies the target to which the texture is bound.
    :type target: Enumerated constant
    :param texture: Specifies the name of a texture.
    :type texture: unsigned int
    """


def glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap):
    """Draw a bitmap
    
    :param height: Specify the pixel width and height of the bitmap image.
    :type height: bge.render.RASOffScreen.width,
    :param yorig: Specify the location of the origin in the bitmap image. The origin is measured
                                                from the lower left corner of the bitmap, with right and up being the positive axes.
    :type yorig: xorig,
    :param ymove: Specify the x and y offsets to be added to the current raster position after
                                                the bitmap is drawn.
    :type ymove: xmove,
    :param bitmap: Specifies the address of the bitmap image.
    :type bitmap: bgl.Buffer object I{type GL_BYTE}
    """


def glBlendFunc(sfactor, dfactor):
    """Specify pixel arithmetic
    
    :param sfactor: Specifies how the red, green, blue, and alpha source blending factors are
                                                computed.
    :type sfactor: Enumerated constant
    :param dfactor: Specifies how the red, green, blue, and alpha destination
                                                blending factors are computed.
    :type dfactor: Enumerated constant
    """


def glCallList(list):
    """Execute a display list
    
    :param list: Specifies the integer name of the display list to be executed.
    :type list: unsigned int
    """


def glCallLists(n, type, lists):
    """Execute a list of display lists
    
    :param n: Specifies the number of display lists to be executed.
    :type n: int
    :param type: Specifies the type of values in lists.
    :type type: Enumerated constant
    :param lists: Specifies the address of an array of name offsets in the display list.
                                                The pointer type is void because the offsets can be bytes, shorts, ints, or floats,
                                                depending on the value of type.
    :type lists: bgl.Buffer object
    """


def glClear(mask):
    """Clear buffers to preset values
    
    :param mask: Bitwise OR of masks that indicate the buffers to be cleared.
    :type mask: Enumerated constant(mathutils.Color.s)
    """


def glClearAccum(red, green, blue, alpha):
    """Specify clear values for the accumulation buffer
    
    :param green, blue, alpha (bpy.types.CompositorNodeColorCorrection.red,): Specify the red, green, blue, and alpha values used when the
                                        accumulation buffer is cleared. The initial values are all 0.
    """


def glClearColor(red, green, blue, alpha):
    """Specify clear values for the color buffers
    
    :param green, blue, alpha (bpy.types.CompositorNodeColorCorrection.red,): Specify the red, green, blue, and alpha values used when the
                                        color buffers are cleared. The initial values are all 0.
    """


def glClearDepth(depth):
    """Specify the clear value for the depth buffer
    
    :param depth: Specifies the depth value used when the depth buffer is cleared.
                                        The initial value is 1.
    :type depth: int
    """


def glClearIndex(c):
    """Specify the clear value for the color index buffers
    
    :param c: Specifies the index used when the color index buffers are cleared.
                                        The initial value is 0.
    :type c: float
    """


def glClearStencil(s):
    """Specify the clear value for the stencil buffer
    
    :param s: Specifies the index used when the stencil buffer is cleared. The initial value is 0.
    :type s: int
    """


def glClipPlane(plane, equation):
    """Specify a plane against which all geometry is clipped
    
    :param plane: Specifies which clipping plane is being positioned.
    :type plane: Enumerated constant
    :param equation: Specifies the address of an array of four double- precision
                                                floating-point values. These values are interpreted as a plane equation.
    :type equation: bgl.Buffer object I{type GL_FLOAT}(double)
    """


def glColor3b(red, green, blue):
    """Set a new color.
    
    :param red: Specify new red value for the current color.
    :type red: int
    :param green: Specify new green value for the current color.
    :type green: int
    :param blue: Specify new blue value for the current color.
    :type blue: int
    """


def glColor3s(red, green, blue):
    """Set a new color.
    
    :param red: Specify new red value for the current color.
    :type red: int
    :param green: Specify new green value for the current color.
    :type green: int
    :param blue: Specify new blue value for the current color.
    :type blue: int
    """


def glColor3i(red, green, blue):
    """Set a new color.
    
    :param red: Specify new red value for the current color.
    :type red: int
    :param green: Specify new green value for the current color.
    :type green: int
    :param blue: Specify new blue value for the current color.
    :type blue: int
    """


def glColor3f(red, green, blue):
    """Set a new color.
    
    :param red: Specify new red value for the current color.
    :type red: float
    :param green: Specify new green value for the current color.
    :type green: float
    :param blue: Specify new blue value for the current color.
    :type blue: float
    """


def glColor3d(red, green, blue):
    """Set a new color.
    
    :param red: Specify new red value for the current color.
    :type red: float
    :param green: Specify new green value for the current color.
    :type green: float
    :param blue: Specify new blue value for the current color.
    :type blue: float
    """


def glColor3ub(red, green, blue):
    """Set a new color.
    
    :param red: Specify new red value for the current color.
    :type red: int
    :param green: Specify new green value for the current color.
    :type green: int
    :param blue: Specify new blue value for the current color.
    :type blue: int
    """


def glColor3us(red, green, blue):
    """Set a new color.
    
    :param red: Specify new red value for the current color.
    :type red: int
    :param green: Specify new green value for the current color.
    :type green: int
    :param blue: Specify new blue value for the current color.
    :type blue: int
    """


def glColor3ui(red, green, blue):
    """Set a new color.
    
    :param red: Specify new red value for the current color.
    :type red: int
    :param green: Specify new green value for the current color.
    :type green: int
    :param blue: Specify new blue value for the current color.
    :type blue: int
    """


def glColor4b(red, green, blue, alpha):
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


def glColor4s(red, green, blue, alpha):
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


def glColor4i(red, green, blue, alpha):
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


def glColor4f(red, green, blue, alpha):
    """Set a new color.
    
    :param red: Specify new red value for the current color.
    :type red: float
    :param green: Specify new green value for the current color.
    :type green: float
    :param blue: Specify new blue value for the current color.
    :type blue: float
    :param alpha: Specify new alpha value for the current color.
    :type alpha: float
    """


def glColor4d(red, green, blue, alpha):
    """Set a new color.
    
    :param red: Specify new red value for the current color.
    :type red: float
    :param green: Specify new green value for the current color.
    :type green: float
    :param blue: Specify new blue value for the current color.
    :type blue: float
    :param alpha: Specify new alpha value for the current color.
    :type alpha: float
    """


def glColor4ub(red, green, blue, alpha):
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


def glColor4us(red, green, blue, alpha):
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


def glColor4ui(red, green, blue, alpha):
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


def glColor3bv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        and blue values.
    :type v: bgl.Buffer[GL_BYTE]
    """


def glColor3sv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        and blue values.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glColor3iv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        and blue values.
    :type v: bgl.Buffer[GL_INT]
    """


def glColor3fv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        and blue values.
    :type v: bgl.Buffer[GL_FLOAT]
    """


def glColor3dv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        and blue values.
    :type v: bgl.Buffer[GL_DOUBLE]
    """


def glColor3ubv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        and blue values.
    :type v: bgl.Buffer[GL_BYTE]
    """


def glColor3usv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        and blue values.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glColor3uiv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        and blue values.
    :type v: bgl.Buffer[GL_INT]
    """


def glColor4bv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        blue, and alpha values.
    :type v: bgl.Buffer[GL_BYTE]
    """


def glColor4sv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        blue, and alpha values.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glColor4iv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        blue, and alpha values.
    :type v: bgl.Buffer[GL_INT]
    """


def glColor4fv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        blue, and alpha values.
    :type v: bgl.Buffer[GL_FLOAT]
    """


def glColor4dv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        blue, and alpha values.
    :type v: bgl.Buffer[GL_DOUBLE]
    """


def glColor4ubv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        blue, and alpha values.
    :type v: bgl.Buffer[GL_BYTE]
    """


def glColor4usv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        blue, and alpha values.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glColor4uiv(v):
    """Set a new color.
    
    :param v: Specifies a pointer to an array that contains red, green,
        blue, and alpha values.
    :type v: bgl.Buffer[GL_INT]
    """


def glColorMask(red, green, blue, alpha):
    """Enable and disable writing of frame buffer color components
    
    :param green, blue, alpha (bpy.types.CompositorNodeColorCorrection.red,): Specify whether red, green, blue, and alpha can or cannot be
                                        written into the frame buffer. The initial values are all GL_TRUE, indicating that the
                                        color components can be written.
    """


def glColorMaterial(face, mode):
    """Cause a material color to track the current color
    
    :param face: Specifies whether front, back, or both front and back material parameters should
                                                track the current color.
    :type face: Enumerated constant
    :param mode: Specifies which of several material parameters track the current color.
    :type mode: Enumerated constant
    """


def glCopyPixels(x, y, width, height, type):
    """Copy pixels in the frame buffer
    def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):
    Copy pixels into a 2D texture image
    
    :param y: Specify the window coordinates of the lower left corner of the rectangular
                                                region of pixels to be copied.
    :type y: bge.types.KX_VertexProxy.x,
    :param width,height: Specify the dimensions of the rectangular region of pixels to be copied.
                                                Both must be non-negative.
    :param type: Specifies whether color values, depth values, or stencil values are to be copied.
    :type type: Enumerated constant
    :param target: Specifies the target texture.
    :type target: Enumerated constant
    :param level: Specifies the level-of-detail number. Level 0 is the base image level.
                                                Level n is the nth mipmap reduction image.
    :type level: int
    :param internalformat: Specifies the number of color components in the texture.
    :type internalformat: int
    :param y: Specify the window coordinates of the first pixel that is copied
                                                from the frame buffer. This location is the lower left corner of a rectangular
                                                block of pixels.
    :type y: bge.types.KX_VertexProxy.x,
    :param width: Specifies the width of the texture image. Must be 2n+2(border) for
                                                some integer n. All implementations support texture images that are at least 64
                                                texels wide.
    :type width: int
    :param height: Specifies the height of the texture image. Must be 2m+2(border) for
                                                some integer m. All implementations support texture images that are at least 64
                                                texels high.
    :type height: int
    :param border: Specifies the width of the border. Must be either 0 or 1.
    :type border: int
    """


def glCullFace(mode):
    """Specify whether front- or back-facing facets can be culled
    
    :param mode: Specifies whether front- or back-facing facets are candidates for culling.
    :type mode: Enumerated constant
    """


def glDeleteLists(list, range):
    """Delete a contiguous group of display lists
    
    :param list: Specifies the integer name of the first display list to delete
    :type list: unsigned int
    :param range: Specifies the number of display lists to delete
    :type range: int
    """


def glDeleteTextures(n, textures):
    """Delete named textures
    
    :param n: Specifies the number of textures to be deleted
    :type n: int
    :param textures: Specifies an array of textures to be deleted
    :type textures: bgl.Buffer I{GL_INT}
    """


def glDepthFunc(func):
    """Specify the value used for depth buffer comparisons
    
    :param func: Specifies the depth comparison function.
    :type func: Enumerated constant
    """


def glDepthMask(flag):
    """Enable or disable writing into the depth buffer
    
    :param flag: Specifies whether the depth buffer is enabled for writing. If flag is GL_FALSE,
                                        depth buffer writing is disabled. Otherwise, it is enabled. Initially, depth buffer
                                        writing is enabled.
    :type flag: int (boolean)
    """


def glDepthRange(zNear, zFar):
    """Specify mapping of depth values from normalized device coordinates to window coordinates
    
    :param zNear: Specifies the mapping of the near clipping plane to window coordinates.
                                                The initial value is 0.
    :type zNear: int
    :param zFar: Specifies the mapping of the far clipping plane to window coordinates.
                                                The initial value is 1.
    :type zFar: int
    """


def glDisable(cap):
    """Disable server-side GL capabilities
    
    :param cap: Specifies a symbolic constant indicating a GL capability.
    :type cap: Enumerated constant
    """


def glDrawBuffer(mode):
    """Specify which color buffers are to be drawn into
    
    :param mode: Specifies up to four color buffers to be drawn into.
    :type mode: Enumerated constant
    """


def glDrawPixels(width, height, format, type, pixels):
    """Write a block of pixels to the frame buffer
    
    :param height: Specify the dimensions of the pixel rectangle to be
                                                written into the frame buffer.
    :type height: bge.render.RASOffScreen.width,
    :param format: Specifies the format of the pixel data.
    :type format: Enumerated constant
    :param type: Specifies the data type for pixels.
    :type type: Enumerated constant
    :param pixels: Specifies a pointer to the pixel data.
    :type pixels: bgl.Buffer object
    """


def glEdgeFlag(flag):
    """B{glEdgeFlag, glEdgeFlagv}
    Flag edges as either boundary or non-boundary
    
    :param flag: Specifies the current edge flag value.The initial value is GL_TRUE.
        (type: Depends of function prototype)
    :type flag: Depends
    """


def glEnable(cap):
    """Enable server-side GL capabilities
    
    :param cap: Specifies a symbolic constant indicating a GL capability.
    :type cap: Enumerated constant
    """


def glEnd():
    """Delimit the vertices of a primitive or group of like primitives"""


def glEndList():
    """Create or replace a display list"""


def glEvalCoord1f(u):
    """evaluate enabled one- and two-dimensional maps
    :param u: Specifies a value that is the domain coordinate  u to the basis
        function defined in a previous glMap1 or glMap2 command.
    :type u: float
    """


def glEvalCoord1d(u):
    """evaluate enabled one- and two-dimensional maps
    :param u: Specifies a value that is the domain coordinate  u to the basis
        function defined in a previous glMap1 or glMap2 command.
    :type u: float
    """


def glEvalCoord2f(u, v):
    """evaluate enabled one- and two-dimensional maps
    :param u: Specifies a value that is the domain coordinate  u to the basis
        function defined in a previous glMap1 or glMap2 command.
    :type u: float
    :param v: Specifies a value that is the domain coordinate v to the basis
        function defined in a previous glMap2 command. This argument is not
        present in a glEvalCoord1 command.
    :type v: float
    """


def glEvalCoord2d(u, v):
    """evaluate enabled one- and two-dimensional maps
    :param u: Specifies a value that is the domain coordinate  u to the basis
        function defined in a previous glMap1 or glMap2 command.
    :type u: float
    :param v: Specifies a value that is the domain coordinate v to the basis
        function defined in a previous glMap2 command. This argument is not
        present in a glEvalCoord1 command.
    :type v: float
    """


def glEvalCoord1fv(u):
    """evaluate enabled one- and two-dimensional maps
    :param u: Specifies a pointer to an array containing either one or two
        domain coordinates. The first coordinate is u. The second coordinate
        is v, which is present only in glEvalCoord2 versions.
    :type u: bgl.Buffer[GL_FLOAT]
    """


def glEvalCoord1dv(u):
    """evaluate enabled one- and two-dimensional maps
    :param u: Specifies a pointer to an array containing either one or two
        domain coordinates. The first coordinate is u. The second coordinate
        is v, which is present only in glEvalCoord2 versions.
    :type u: bgl.Buffer[GL_DOUBLE]
    """


def glEvalCoord2fv(u):
    """evaluate enabled one- and two-dimensional maps
    :param u: Specifies a pointer to an array containing either one or two
        domain coordinates. The first coordinate is u. The second coordinate
        is v, which is present only in glEvalCoord2 versions.
    :type u: bgl.Buffer[GL_FLOAT]
    """


def glEvalCoord2dv(u):
    """evaluate enabled one- and two-dimensional maps
    :param u: Specifies a pointer to an array containing either one or two
        domain coordinates. The first coordinate is u. The second coordinate
        is v, which is present only in glEvalCoord2 versions.
    :type u: bgl.Buffer[GL_DOUBLE]
    """


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


def glFeedbackBuffer(size, type, buffer):
    """Controls feedback mode
    
    :param size: Specifies the maximum number of values that can be written into buffer.
    :type size: int
    :param type: Specifies a symbolic constant that describes the information that
                                                will be returned for each vertex.
    :type type: Enumerated constant
    :param buffer: Returns the feedback data.
    :type buffer: bgl.Buffer object I{GL_FLOAT}
    """


def glFinish():
    """Block until all GL execution is complete"""


def glFlush():
    """Force Execution of GL commands in finite time"""


def glFogi(pname, param):
    """specify fog parameters
    
    :param pname: Specifies a single-valued fog parameter.
        enum in [GL_FOG_MODE, GL_FOG_DENSITY, GL_FOG_START, GL_FOG_END,
        GL_FOG_INDEX, GL_FOG_COORD]
    :type pname: int
    :param param: Specifies the value that pname will be set to.
    :type param: int
    """


def glFogf(pname, param):
    """specify fog parameters
    
    :param pname: Specifies a single-valued fog parameter.
        enum in [GL_FOG_MODE, GL_FOG_DENSITY, GL_FOG_START, GL_FOG_END,
        GL_FOG_INDEX, GL_FOG_COORD]
    :type pname: int
    :param param: Specifies the value that pname will be set to.
    :type param: float
    """


def glFogiv(pname, params):
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


def glFogfv(pname, params):
    """specify fog parameters
    
    :param pname: Specifies a fog parameter.
        enum in [GL_FOG_MODE, GL_FOG_DENSITY, GL_FOG_START, GL_FOG_END,
        GL_FOG_INDEX, GL_FOG_COLOR, GL_FOG_COORD_SRC]
    :type pname: int
    :param params: Specifies the value or values to be assigned to pname.
        GL_FOG_COLOR requires an array of four values. All other parameters
        accept an array containing only a single value.
    :type params: bgl.Buffer[GL_FLOAT]
    """


def glFrontFace(mode):
    """Define front- and back-facing polygons
    
    :param mode: Specifies the orientation of front-facing polygons.
    :type mode: Enumerated constant
    """


def glFrustum(left, right, bottom, top, zNear, zFar):
    """Multiply the current matrix by a perspective matrix
    
    :param right: Specify the coordinates for the left and right vertical
                                                clipping planes.
    :type right: left,
    :param bottom: Specify the coordinates for the bottom and top horizontal
                                                clipping planes.
    :type bottom: bpy.types.SpaceTextEditor.top,
    :param zFar: Specify the distances to the near and far depth clipping planes.
                                                Both distances must be positive.
    :type zFar: zNear,
    """


def glGenLists(range):
    """Generate a contiguous set of empty display lists
    
    :param range: Specifies the number of contiguous empty display lists to be generated.
    :type range: int
    """


def glGenTextures(n, textures):
    """Generate texture names
    
    :param n: Specifies the number of textures name to be generated.
    :type n: int
    :param textures: Specifies an array in which the generated textures names are stored.
    :type textures: bgl.Buffer object I{type GL_INT}
    """


def glGetBooleanv(pname, params):
    """return the value or values of a selected parameter
    
    :param pname: Specifies the parameter value to be returned.
        The symbolic constants in the list below are accepted.
    :type pname: int
    :param params: Returns the value or values of the specified parameter.
    :type params: bgl.Buffer[GL_BYTE]
    """


def glGetIntegerv(pname, params):
    """return the value or values of a selected parameter
    
    :param pname: Specifies the parameter value to be returned.
        The symbolic constants in the list below are accepted.
    :type pname: int
    :param params: Returns the value or values of the specified parameter.
    :type params: bgl.Buffer[GL_INT]
    """


def glGetFloatv(pname, params):
    """return the value or values of a selected parameter
    
    :param pname: Specifies the parameter value to be returned.
        The symbolic constants in the list below are accepted.
    :type pname: int
    :param params: Returns the value or values of the specified parameter.
    :type params: bgl.Buffer[GL_FLOAT]
    """


def glGetDoublev(pname, params):
    """return the value or values of a selected parameter
    
    :param pname: Specifies the parameter value to be returned.
        The symbolic constants in the list below are accepted.
    :type pname: int
    :param params: Returns the value or values of the specified parameter.
    :type params: bgl.Buffer[GL_DOUBLE]
    """


def glGetClipPlane(plane, equation):
    """Return the coefficients of the specified clipping plane
    
    :param plane: Specifies a clipping plane. The number of clipping planes depends on the
                                                implementation, but at least six clipping planes are supported. They are identified by
                                                symbolic names of the form GL_CLIP_PLANEi where 0 < i < GL_MAX_CLIP_PLANES.
    :type plane: Enumerated constant
    :param equation: Returns four float (double)-precision values that are the coefficients of the
                                                plane equation of plane in eye coordinates. The initial value is (0, 0, 0, 0).
    :type equation: bgl.Buffer object I{type GL_FLOAT}
    """


def glGetError():
    """Return error information"""


def glGetLightiv(light, pname, params):
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


def glGetLightfv(light, pname, params):
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
    :type params: bgl.Buffer[GL_FLOAT]
    """


def glGetMapiv(target, query, v):
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


def glGetMapfv(target, query, v):
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
    :type v: bgl.Buffer[GL_FLOAT]
    """


def glGetMapdv(target, query, v):
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
    :type v: bgl.Buffer[GL_DOUBLE]
    """


def glGetMaterialiv(face, pname, params):
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


def glGetMaterialfv(face, pname, params):
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
    :type params: bgl.Buffer[GL_FLOAT]
    """


def glGetPixelMapusv(map, data):
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


def glGetPixelMapuiv(map, data):
    """return the specified pixel map
    
    :param map: Specifies the name of the pixel map to return.
        enum in [GL_PIXEL_MAP_I_TO_I, GL_PIXEL_MAP_S_TO_S,
        GL_PIXEL_MAP_I_TO_R, GL_PIXEL_MAP_I_TO_G, GL_PIXEL_MAP_I_TO_B,
        GL_PIXEL_MAP_I_TO_A, GL_PIXEL_MAP_R_TO_R, GL_PIXEL_MAP_G_TO_G,
        GL_PIXEL_MAP_B_TO_B, GL_PIXEL_MAP_A_TO_A]
    :type map: int
    :param data: Returns the pixel map contents.
    :type data: bgl.Buffer[GL_INT]
    """


def glGetPixelMapfv(map, data):
    """return the specified pixel map
    
    :param map: Specifies the name of the pixel map to return.
        enum in [GL_PIXEL_MAP_I_TO_I, GL_PIXEL_MAP_S_TO_S,
        GL_PIXEL_MAP_I_TO_R, GL_PIXEL_MAP_I_TO_G, GL_PIXEL_MAP_I_TO_B,
        GL_PIXEL_MAP_I_TO_A, GL_PIXEL_MAP_R_TO_R, GL_PIXEL_MAP_G_TO_G,
        GL_PIXEL_MAP_B_TO_B, GL_PIXEL_MAP_A_TO_A]
    :type map: int
    :param data: Returns the pixel map contents.
    :type data: bgl.Buffer[GL_FLOAT]
    """


def glGetPolygonStipple(mask):
    """Return the polygon stipple pattern
    
    :param mask: Returns the stipple pattern. The initial value is all 1's.
    :type mask: bgl.Buffer object I{type GL_BYTE}
    """


def glGetString(name):
    """Return a string describing the current GL connection
    
    :param name: Specifies a symbolic constant.
    :type name: Enumerated constant
    """


def glGetTexEnviv(target, pname, params):
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


def glGetTexEnvfv(target, pname, params):
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
    :type params: bgl.Buffer[GL_FLOAT]
    """


def glGetTexGeniv(target, pname, params):
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


def glGetTexGenfv(target, pname, params):
    """return texture coordinate generation parameters
    
    :param target: Specifies a texture coordinate.
        enum in [GL_S, GL_T, GL_R, GL_Q]
    :type target: int
    :param pname: Specifies the symbolic name of the value(s) to be returned.
        Must be either GL_TEXTURE_GEN_MODE or the name of one of the
        texture generation plane equations: GL_OBJECT_PLANE or GL_EYE_PLANE.
    :type pname: int
    :param params: Returns the requested data.
    :type params: bgl.Buffer[GL_FLOAT]
    """


def glGetTexGendv(target, pname, params):
    """return texture coordinate generation parameters
    
    :param target: Specifies a texture coordinate.
        enum in [GL_S, GL_T, GL_R, GL_Q]
    :type target: int
    :param pname: Specifies the symbolic name of the value(s) to be returned.
        Must be either GL_TEXTURE_GEN_MODE or the name of one of the
        texture generation plane equations: GL_OBJECT_PLANE or GL_EYE_PLANE.
    :type pname: int
    :param params: Returns the requested data.
    :type params: bgl.Buffer[GL_DOUBLE]
    """


def glGetTexImage(target, level, format, type, pixels):
    """Return a texture image
    
    :param target: Specifies which texture is to be obtained.
    :type target: Enumerated constant
    :param level: Specifies the level-of-detail number of the desired image.
                                                Level 0 is the base image level. Level n is the nth mipmap reduction image.
    :type level: int
    :param format: Specifies a pixel format for the returned data.
    :type format: Enumerated constant
    :param type: Specifies a pixel type for the returned data.
    :type type: Enumerated constant
    :param pixels: Returns the texture image. Should be a pointer to an array of the
                                                type specified by type
    :type pixels: bgl.Buffer object.
    """


def glGetTexLevelParameteriv(target, level, pname, params):
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


def glGetTexLevelParameterfv(target, level, pname, params):
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
    :type params: bgl.Buffer[GL_FLOAT]
    """


def glGetTexParameteriv(target, pname, params):
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


def glGetTexParameterfv(target, pname, params):
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
    :type params: bgl.Buffer[GL_FLOAT]
    """


def glHint(target, mode):
    """Specify implementation-specific hints
    
    :param target: Specifies a symbolic constant indicating the behavior to be
                                                controlled.
    :type target: Enumerated constant
    :param mode: Specifies a symbolic constant indicating the desired behavior.
    :type mode: Enumerated constant
    """


def glIndexs(c):
    """set the current color index
    
    :param c: Specifies the new value for the current color index.
    :type c: int
    """


def glIndexi(c):
    """set the current color index
    
    :param c: Specifies the new value for the current color index.
    :type c: int
    """


def glIndexf(c):
    """set the current color index
    
    :param c: Specifies the new value for the current color index.
    :type c: float
    """


def glIndexd(c):
    """set the current color index
    
    :param c: Specifies the new value for the current color index.
    :type c: float
    """


def glIndexub(c):
    """set the current color index
    
    :param c: Specifies the new value for the current color index.
    :type c: int
    """


def glIndexsv(c):
    """set the current color index
    
    :param c: Specifies a pointer to a one-element array that contains
        the new value for the current color index.
    :type c: bgl.Buffer[GL_SHORT]
    """


def glIndexiv(c):
    """set the current color index
    
    :param c: Specifies a pointer to a one-element array that contains
        the new value for the current color index.
    :type c: bgl.Buffer[GL_INT]
    """


def glIndexfv(c):
    """set the current color index
    
    :param c: Specifies a pointer to a one-element array that contains
        the new value for the current color index.
    :type c: bgl.Buffer[GL_FLOAT]
    """


def glIndexdv(c):
    """set the current color index
    
    :param c: Specifies a pointer to a one-element array that contains
        the new value for the current color index.
    :type c: bgl.Buffer[GL_DOUBLE]
    """


def glIndexubv(c):
    """set the current color index
    
    :param c: Specifies a pointer to a one-element array that contains
        the new value for the current color index.
    :type c: bgl.Buffer[GL_BYTE]
    """


def glIndexMask(mask):
    """Control the writing of individual bits in the color index buffers
    
    :param mask: Specifies a bit mask to enable and disable the writing of individual bits
                                        in the color index buffers.
                                        Initially, the mask is all 1's.
    :type mask: int
    """


def glInitNames():
    """Initialize the name stack"""


def glIsEnabled(cap):
    """Test whether a capability is enabled
    
    :param cap: Specifies a constant representing a GL capability.
    :type cap: Enumerated constant
    """


def glIsList(list):
    """Determine if a name corresponds to a display-list
    
    :param list: Specifies a potential display-list name.
    :type list: unsigned int
    """


def glIsTexture(texture):
    """Determine if a name corresponds to a texture
    
    :param texture: Specifies a value that may be the name of a texture.
    :type texture: unsigned int
    """


def glLighti(light, pname, params):
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


def glLightf(light, pname, params):
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
    :type params: float
    """


def glLightModeli(pname, param):
    """set the lighting model parameters
    
    :param pname: Specifies a single-valued lighting model parameter.
        enum in [ GL_LIGHT_MODEL_LOCAL_VIEWER, GL_LIGHT_MODEL_COLOR_CONTROL,
        GL_LIGHT_MODEL_TWO_SIDE]
    :type pname: int
    :param param: Specifies the value that param will be set to.
    :type param: int
    """


def glLightModelf(pname, param):
    """set the lighting model parameters
    
    :param pname: Specifies a single-valued lighting model parameter.
        enum in [ GL_LIGHT_MODEL_LOCAL_VIEWER, GL_LIGHT_MODEL_COLOR_CONTROL,
        GL_LIGHT_MODEL_TWO_SIDE]
    :type pname: int
    :param param: Specifies the value that param will be set to.
    :type param: float
    """


def glLightModeliv(pname, params):
    """set the lighting model parameters
    
    :param pname: Specifies a single-valued lighting model parameter.
        enum in [ GL_LIGHT_MODEL_LOCAL_VIEWER, GL_LIGHT_MODEL_COLOR_CONTROL,
        GL_LIGHT_MODEL_TWO_SIDE]
    :type pname: int
    :param param: Specifies a pointer to the value or values that params
        will be set to.
    :type param: bgl.Buffer[GL_INT]
    """


def glLightModelfv(pname, params):
    """set the lighting model parameters
    
    :param pname: Specifies a single-valued lighting model parameter.
        enum in [ GL_LIGHT_MODEL_LOCAL_VIEWER, GL_LIGHT_MODEL_COLOR_CONTROL,
        GL_LIGHT_MODEL_TWO_SIDE]
    :type pname: int
    :param param: Specifies a pointer to the value or values that params
        will be set to.
    :type param: bgl.Buffer[GL_FLOAT]
    """


def glLineStipple(factor, pattern):
    """Specify the line stipple pattern
    
    :param factor: Specifies a multiplier for each bit in the line stipple pattern.
                                                If factor is 3, for example, each bit in the pattern is used three times before
                                                the next bit in the pattern is used. factor is clamped to the range [1, 256] and
                                                defaults to 1.
    :type factor: int
    :param pattern: Specifies a 16-bit integer whose bit pattern determines which fragments
                                                of a line will be drawn when the line is rasterized. Bit zero is used first; the default
                                                pattern is all 1's.
    :type pattern: unsigned short int
    """


def glLineWidth(width):
    """Specify the width of rasterized lines.
    
    :param width: Specifies the width of rasterized lines. The initial value is 1.
    :type width: float
    """


def glListBase(base):
    """Set the display-list base for glCallLists
    
    :param base: Specifies an integer offset that will be added to glCallLists
                                        offsets to generate display-list names. The initial value is 0.
    :type base: unsigned int
    """


def glLoadIdentity():
    """Replace the current matrix with the identity matrix"""


def glLoadMatrixf(m):
    """replace the current matrix with the specified matrix
    
    :param m: Specifies a pointer to 16 consecutive values, which are used
        as the elements of a 4 × 4 column-major matrix.
    :type m: bgl.Buffer[GL_FLOAT]
    """


def glLoadMatrixd(m):
    """replace the current matrix with the specified matrix
    
    :param m: Specifies a pointer to 16 consecutive values, which are used
        as the elements of a 4 × 4 column-major matrix.
    :type m: bgl.Buffer[GL_DOUBLE]
    """


def glLoadName(name):
    """Load a name onto the name stack.
    
    :param name: Specifies a name that will replace the top value on the name stack.
    :type name: unsigned int
    """


def glLogicOp(opcode):
    """Specify a logical pixel operation for color index rendering
    
    :param opcode: Specifies a symbolic constant that selects a logical operation.
    :type opcode: Enumerated constant
    """


def glMap1f(target, u1, u2, stride, order, points):
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


def glMap1d(target, u1, u2, stride, order, points):
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
    :type points: bgl.Buffer[GL_DOUBLE]
    """


def glMap2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
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


def glMap2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
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
    :type points: bgl.Buffer[GL_DOUBLE]
    """


def glMapGrid1f(un, u1, n2):
    """define a one- or two-dimensional mesh
    
    :param un: Specifies the number of partitions in the grid range interval
        [u1, u2]. Must be positive.
    :type un: int
    :param u1: Specify the mapping for integer grid domain value i = 0.
    :type u1: float
    :param n2: Specify the mapping for integer grid domain value i = un.
    :type n2: float
    """


def glMapGrid1d(un, u1, n2):
    """define a one- or two-dimensional mesh
    
    :param un: Specifies the number of partitions in the grid range interval
        [u1, u2]. Must be positive.
    :type un: int
    :param u1: Specify the mapping for integer grid domain value i = 0.
    :type u1: float
    :param n2: Specify the mapping for integer grid domain value i = un.
    :type n2: float
    """


def glMapGrid2f(un, u1, n2, vn, v1, v2):
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


def glMapGrid2d(un, u1, n2, vn, v1, v2):
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


def glMaterial(face, pname, params):
    """Specify material parameters for the lighting model.
    
    :param face: Specifies which face or faces are being updated. Must be one of:
    :type face: Enumerated constant
    :param pname: Specifies the single-valued material parameter of the face
                                                or faces that is being updated. Must be GL_SHININESS.
    :type pname: Enumerated constant
    :param params: Specifies the value that parameter GL_SHININESS will be set to.
                                                If function prototype ends in 'v' specifies a pointer to the value or values that
                                                pname will be set to.
    :type params: int
    """


def glMatrixMode(mode):
    """Specify which matrix is the current matrix.
    
    :param mode: Specifies which matrix stack is the target for subsequent matrix operations.
    :type mode: Enumerated constant
    """


def glMultMatrixf(m):
    """multiply the current matrix with the specified matrix
    
    :param m: Points to 16 consecutive values that are used as the elements
        of a 4 × 4 column-major matrix.
    :type m: bgl.Buffer[GL_FLOAT]
    """


def glMultMatrixd(m):
    """multiply the current matrix with the specified matrix
    
    :param m: Points to 16 consecutive values that are used as the elements
        of a 4 × 4 column-major matrix.
    :type m: bgl.Buffer[GL_DOUBL]
    """


def glNewList(list, mode):
    """Create or replace a display list
    
    :param list: Specifies the display list name
    :type list: unsigned int
    :param mode: Specifies the compilation mode.
    :type mode: Enumerated constant
    """


def glNormal3b(nx, ny, nz):
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


def glNormal3s(nx, ny, nz):
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


def glNormal3i(nx, ny, nz):
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


def glNormal3f(nx, ny, nz):
    """set the current normal vector
    
    :param nx: Specify the x coordinate of the new current normal.
        The initial value of the current normal is the unit vector, (0, 0, 1).
    :type nx: float
    :param ny: Specify the y coordinate of the new current normal.
        The initial value of the current normal is the unit vector, (0, 0, 1).
    :type ny: float
    :param nz: Specify the z coordinate of the new current normal.
        The initial value of the current normal is the unit vector, (0, 0, 1).
    :type nz: float
    """


def glNormal3d(nx, ny, nz):
    """set the current normal vector
    
    :param nx: Specify the x coordinate of the new current normal.
        The initial value of the current normal is the unit vector, (0, 0, 1).
    :type nx: float
    :param ny: Specify the y coordinate of the new current normal.
        The initial value of the current normal is the unit vector, (0, 0, 1).
    :type ny: float
    :param nz: Specify the z coordinate of the new current normal.
        The initial value of the current normal is the unit vector, (0, 0, 1).
    :type nz: float
    """


def glNormal3bv(v):
    """set the current normal vector
    
    :param v: Specifies a pointer to an array of three elements: the x, y,
        and z coordinates of the new current normal.
    :type v: bgl.Buffer[GL_BYTE]
    """


def glNormal3sv(v):
    """set the current normal vector
    
    :param v: Specifies a pointer to an array of three elements: the x, y,
        and z coordinates of the new current normal.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glNormal3iv(v):
    """set the current normal vector
    
    :param v: Specifies a pointer to an array of three elements: the x, y,
        and z coordinates of the new current normal.
    :type v: bgl.Buffer[GL_INT]
    """


def glNormal3fv(v):
    """set the current normal vector
    
    :param v: Specifies a pointer to an array of three elements: the x, y,
        and z coordinates of the new current normal.
    :type v: bgl.Buffer[GL_FLOAT]
    """


def glNormal3dv(v):
    """set the current normal vector
    
    :param v: Specifies a pointer to an array of three elements: the x, y,
        and z coordinates of the new current normal.
    :type v: bgl.Buffer[GL_DOUBLE]
    """


def glOrtho(left, right, bottom, top, zNear, zFar):
    """Multiply the current matrix with an orthographic matrix
    
    :param right: Specify the coordinates for the left and
                                                right vertical clipping planes.
    :type right: left,
    :param top: Specify the coordinates for the bottom and top
                                                horizontal clipping planes.
    :type top: bottom,
    :param zFar: Specify the distances to the nearer and farther
                                                depth clipping planes. These values are negative if the plane is to be behind the viewer.
    :type zFar: zNear,
    """


def glPassThrough(token):
    """Place a marker in the feedback buffer
    
    :param token: Specifies a marker value to be placed in the feedback
                                        buffer following a GL_PASS_THROUGH_TOKEN.
    :type token: float
    """


def glPixelMapusv(map, mapsize, values):
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


def glPixelMapuiv(map, mapsize, values):
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
    :type values: bgl.Buffer[GL_INT]
    """


def glPixelMapfv(map, mapsize, values):
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
    :type values: bgl.Buffer[GL_FLOAT]
    """


def glPixelStorei(pname, param):
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


def glPixelStoref(pname, param):
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
    :type param: float
    """


def glPixelTransferi(pname, param):
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


def glPixelTransferf(pname, param):
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
    :type param: float
    """


def glPixelZoom(xfactor, yfactor):
    """Specify the pixel zoom factors
    
    :param yfactor: Specify the x and y zoom factors for pixel write operations.
    :type yfactor: xfactor,
    """


def glPointSize(size):
    """Specify the diameter of rasterized points
    
    :param size: Specifies the diameter of rasterized points. The initial value is 1.
    :type size: float
    """


def glPolygonMode(face, mode):
    """Select a polygon rasterization mode
    
    :param face: Specifies the polygons that mode applies to.
                                                Must be GL_FRONT for front-facing polygons, GL_BACK for back- facing
                                                polygons, or GL_FRONT_AND_BACK for front- and back-facing polygons.
    :type face: Enumerated constant
    :param mode: Specifies how polygons will be rasterized.
                                                The initial value is GL_FILL for both front- and back- facing polygons.
    :type mode: Enumerated constant
    """


def glPolygonOffset(factor, units):
    """Set the scale and units used to calculate depth values
    
    :param factor: Specifies a scale factor that is used to create a variable depth
                                                offset for each polygon. The initial value is 0.
    :type factor: float
    :param units: Is multiplied by an implementation-specific value to create a
                                                constant depth offset. The initial value is 0.
    :type units: float
    """


def glPolygonStipple(mask):
    """Set the polygon stippling pattern
    
    :param mask: Specifies a pointer to a 32x32 stipple pattern that will be unpacked
                                        from memory in the same way that glDrawPixels unpacks pixels.
    :type mask: bgl.Buffer object I{type GL_BYTE}
    """


def glPopAttrib():
    """Pop the server attribute stack"""


def glPopClientAttrib():
    """Pop the client attribute stack"""


def glPopMatrix():
    """Pop the current matrix stack"""


def glPopName():
    """Pop the name stack"""


def glPrioritizeTextures(n, textures, priorities):
    """Set texture residence priority
    
    :param n: Specifies the number of textures to be prioritized.
    :type n: int
    :param textures: Specifies an array containing the names of the textures to be prioritized.
    :type textures: bgl.Buffer I{type GL_INT}
    :param priorities: Specifies an array containing the texture priorities.
                                                A priority given in an element of priorities applies to the texture named
                                                by the corresponding element of textures.
    :type priorities: bgl.Buffer I{type GL_FLOAT}
    """


def glPushAttrib(mask):
    """Push the server attribute stack
    
    :param mask: Specifies a mask that indicates which attributes to save.
    :type mask: Enumerated constant(mathutils.Color.s)
    """


def glPushClientAttrib(mask):
    """Push the client attribute stack
    
    :param mask: Specifies a mask that indicates which attributes to save.
    :type mask: Enumerated constant(mathutils.Color.s)
    """


def glPushMatrix():
    """Push the current matrix stack"""


def glPushName(name):
    """Push the name stack
    
    :param name: Specifies a name that will be pushed onto the name stack.
    :type name: unsigned int
    """


def glRasterPos2s(x, y):
    """specify the raster position for pixel operations
    
    :param x: Specify the x object coordinate for the raster position.
    :type x: int
    :param y: Specify the y object coordinate for the raster position.
    :type y: int
    """


def glRasterPos2i(x, y):
    """specify the raster position for pixel operations
    
    :param x: Specify the x object coordinate for the raster position.
    :type x: int
    :param y: Specify the y object coordinate for the raster position.
    :type y: int
    """


def glRasterPos2f(x, y):
    """specify the raster position for pixel operations
    
    :param x: Specify the x object coordinate for the raster position.
    :type x: float
    :param y: Specify the y object coordinate for the raster position.
    :type y: float
    """


def glRasterPos2d(x, y):
    """specify the raster position for pixel operations
    
    :param x: Specify the x object coordinate for the raster position.
    :type x: float
    :param y: Specify the y object coordinate for the raster position.
    :type y: float
    """


def glRasterPos3s(x, y, z):
    """specify the raster position for pixel operations
    
    :param x: Specify the x object coordinate for the raster position.
    :type x: int
    :param y: Specify the y object coordinate for the raster position.
    :type y: int
    :param z: Specify the z object coordinate for the raster position.
    :type z: int
    """


def glRasterPos3i(x, y, z):
    """specify the raster position for pixel operations
    
    :param x: Specify the x object coordinate for the raster position.
    :type x: int
    :param y: Specify the y object coordinate for the raster position.
    :type y: int
    :param z: Specify the z object coordinate for the raster position.
    :type z: int
    """


def glRasterPos3f(x, y, z):
    """specify the raster position for pixel operations
    
    :param x: Specify the x object coordinate for the raster position.
    :type x: float
    :param y: Specify the y object coordinate for the raster position.
    :type y: float
    :param z: Specify the z object coordinate for the raster position.
    :type z: float
    """


def glRasterPos3d(x, y, z):
    """specify the raster position for pixel operations
    
    :param x: Specify the x object coordinate for the raster position.
    :type x: float
    :param y: Specify the y object coordinate for the raster position.
    :type y: float
    :param z: Specify the z object coordinate for the raster position.
    :type z: float
    """


def glRasterPos4s(x, y, z, w):
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


def glRasterPos4i(x, y, z, w):
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


def glRasterPos4f(x, y, z, w):
    """specify the raster position for pixel operations
    
    :param x: Specify the x object coordinate for the raster position.
    :type x: float
    :param y: Specify the y object coordinate for the raster position.
    :type y: float
    :param z: Specify the z object coordinate for the raster position.
    :type z: float
    :param w: Specify the w object coordinate for the raster position.
    :type w: float
    """


def glRasterPos4d(x, y, z, w):
    """specify the raster position for pixel operations
    
    :param x: Specify the x object coordinate for the raster position.
    :type x: float
    :param y: Specify the y object coordinate for the raster position.
    :type y: float
    :param z: Specify the z object coordinate for the raster position.
    :type z: float
    :param w: Specify the w object coordinate for the raster position.
    :type w: float
    """


def glRasterPos2sv(v):
    """specify the raster position for pixel operations
    
    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x and y coordinates, respectively.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glRasterPos2iv(v):
    """specify the raster position for pixel operations
    
    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x and y coordinates, respectively.
    :type v: bgl.Buffer[GL_INT]
    """


def glRasterPos2fv(v):
    """specify the raster position for pixel operations
    
    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x and y coordinates, respectively.
    :type v: bgl.Buffer[GL_FLOAT]
    """


def glRasterPos2dv(v):
    """specify the raster position for pixel operations
    
    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x and y coordinates, respectively.
    :type v: bgl.Buffer[GL_DOUBLE]
    """


def glRasterPos3sv(v):
    """specify the raster position for pixel operations
    
    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x, y, and w coordinates, respectively.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glRasterPos3iv(v):
    """specify the raster position for pixel operations
    
    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x, y, and w coordinates, respectively.
    :type v: bgl.Buffer[GL_INT]
    """


def glRasterPos3fv(v):
    """specify the raster position for pixel operations
    
    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x, y, and w coordinates, respectively.
    :type v: bgl.Buffer[GL_FLOAT]
    """


def glRasterPos3dv(v):
    """specify the raster position for pixel operations
    
    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x, y, and w coordinates, respectively.
    :type v: bgl.Buffer[GL_DOUBLE]
    """


def glRasterPos4sv(v):
    """specify the raster position for pixel operations
    
    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x, y, z, and w coordinates, respectively.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glRasterPos4iv(v):
    """specify the raster position for pixel operations
    
    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x, y, z, and w coordinates, respectively.
    :type v: bgl.Buffer[GL_INT]
    """


def glRasterPos4fv(v):
    """specify the raster position for pixel operations
    
    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x, y, z, and w coordinates, respectively.
    :type v: bgl.Buffer[GL_FLOAT]
    """


def glRasterPos4dv(v):
    """specify the raster position for pixel operations
    
    :param v: Specifies a pointer to an array of two, three, or four elements,
        specifying x, y, z, and w coordinates, respectively.
    :type v: bgl.Buffer[GL_DOUBLE]
    """


def glReadBuffer(mode):
    """Select a color buffer source for pixels.
    
    :param mode: Specifies a color buffer.
    :type mode: Enumerated constant
    """


def glReadPixels(x, y, width, height, format, type, pixels):
    """Read a block of pixels from the frame buffer
    
    :param y: Specify the window coordinates of the first pixel that is read
                                                from the frame buffer. This location is the lower left corner of a rectangular
                                                block of pixels.
    :type y: bge.types.KX_VertexProxy.x,
    :param height: Specify the dimensions of the pixel rectangle. width and
                                                height of one correspond to a single pixel.
    :type height: bge.render.RASOffScreen.width,
    :param format: Specifies the format of the pixel data.
    :type format: Enumerated constant
    :param type: Specifies the data type of the pixel data.
    :type type: Enumerated constant
    :param pixels: Returns the pixel data.
    :type pixels: bgl.Buffer object
    """


def glRects(x1, y1, x2, y2):
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


def glRecti(x1, y1, x2, y2):
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


def glRectf(x1, y1, x2, y2):
    """draw a rectangle
    
    :param x1: Specify one vertex of a rectangle.
    :type x1: float
    :param y1: Specify one vertex of a rectangle.
    :type y1: float
    :param x2: Specify the opposite vertex of the rectangle.
    :type x2: float
    :param y2: Specify the opposite vertex of the rectangle.
    :type y2: float
    """


def glRectd(x1, y1, x2, y2):
    """draw a rectangle
    
    :param x1: Specify one vertex of a rectangle.
    :type x1: float
    :param y1: Specify one vertex of a rectangle.
    :type y1: float
    :param x2: Specify the opposite vertex of the rectangle.
    :type x2: float
    :param y2: Specify the opposite vertex of the rectangle.
    :type y2: float
    """


def glRectsv(v1, v2):
    """draw a rectangle
    
    :param v1: Specifies a pointer to one vertex of a rectangle.
    :type v1: Bugger[GL_SHORT]
    :param v2: Specifies a pointer to the opposite vertex of the rectangle.
    :type v2: Bugger[GL_SHORT]
    """


def glRectiv(v1, v2):
    """draw a rectangle
    
    :param v1: Specifies a pointer to one vertex of a rectangle.
    :type v1: Bugger[GL_INT]
    :param v2: Specifies a pointer to the opposite vertex of the rectangle.
    :type v2: Bugger[GL_INT]
    """


def glRectfv(v1, v2):
    """draw a rectangle
    
    :param v1: Specifies a pointer to one vertex of a rectangle.
    :type v1: Bugger[GL_FLOAT]
    :param v2: Specifies a pointer to the opposite vertex of the rectangle.
    :type v2: Bugger[GL_FLOAT]
    """


def glRectdv(v1, v2):
    """draw a rectangle
    
    :param v1: Specifies a pointer to one vertex of a rectangle.
    :type v1: Bugger[GL_DOUBLE]
    :param v2: Specifies a pointer to the opposite vertex of the rectangle.
    :type v2: Bugger[GL_DOUBLE]
    """


def glRenderMode(mode):
    """Set rasterization mode
    
    :param mode: Specifies the rasterization mode.
    :type mode: Enumerated constant
    """


def glRotatef(angle, x, y, z):
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


def glRotated(angle, x, y, z):
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


def glScalef(x, y, z):
    """multiply the current matrix by a general scaling matrix
    
    :param x: Specify scale factors along the x axis.
    :type x: float
    :param y: Specify scale factors along the y axis.
    :type y: float
    :param z: Specify scale factors along the z axis.
    :type z: float
    """


def glScaled(x, y, z):
    """multiply the current matrix by a general scaling matrix
    
    :param x: Specify scale factors along the x axis.
    :type x: float
    :param y: Specify scale factors along the y axis.
    :type y: float
    :param z: Specify scale factors along the z axis.
    :type z: float
    """


def glScissor(x,y,width,height):
    """Define the scissor box
    
    :param y: Specify the lower left corner of the scissor box. Initially (0, 0).
    :type y: bge.types.KX_VertexProxy.x,
    :param height: Specify the width and height of the scissor box. When a
                                                GL context is first attached to a window, width and height are set to the
                                                dimensions of that window.
    :type height: bge.render.RASOffScreen.width
    """


def glSelectBuffer(size, buffer):
    """Establish a buffer for selection mode values
    
    :param size: Specifies the size of buffer
    :type size: int
    :param buffer: Returns the selection data
    :type buffer: bgl.Buffer I{type GL_INT}
    """


def glShadeModel(mode):
    """Select flat or smooth shading
    
    :param mode: Specifies a symbolic value representing a shading technique.
    :type mode: Enumerated constant
    """


def glStencilFunc(func, ref, mask):
    """Set function and reference value for stencil testing
    
    :param func: Specifies the test function.
    :type func: Enumerated constant
    :param ref: Specifies the reference value for the stencil test. ref is clamped
                                                to the range [0,2n-1], where n is the number of bitplanes in the stencil
                                                buffer. The initial value is 0.
    :type ref: int
    :param mask: Specifies a mask that is ANDed with both the reference value and
                                                the stored stencil value when the test is done. The initial value is all 1's.
    :type mask: unsigned int
    """


def glStencilMask(mask):
    """Control the writing of individual bits in the stencil planes
    
    :param mask: Specifies a bit mask to enable and disable writing of individual bits
                                        in the stencil planes. Initially, the mask is all 1's.
    :type mask: unsigned int
    """


def glStencilOp(fail, zfail, zpass):
    """Set stencil test actions
    
    :param fail: Specifies the action to take when the stencil test fails.
                                                The initial value is GL_KEEP.
    :type fail: Enumerated constant
    :param zfail: Specifies the stencil action when the stencil test passes, but the
                                                depth test fails. zfail accepts the same symbolic constants as fail.
                                                The initial value is GL_KEEP.
    :type zfail: Enumerated constant
    :param zpass: Specifies the stencil action when both the stencil test and the
                                                depth test pass, or when the stencil test passes and either there is no
                                                depth buffer or depth testing is not enabled. zpass accepts the same
                                                symbolic constants
                                                as fail. The initial value is GL_KEEP.
    :type zpass: Enumerated constant
    """


def glTexCoord1s(s):
    """set the current texture coordinates
    
    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: int
    """


def glTexCoord1i(s):
    """set the current texture coordinates
    
    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: int
    """


def glTexCoord1f(s):
    """set the current texture coordinates
    
    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: float
    """


def glTexCoord1d(s):
    """set the current texture coordinates
    
    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: float
    """


def glTexCoord2s(s, t):
    """set the current texture coordinates
    
    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: int
    :param t: Specify t texture coordinate.
        Not all parameters are present in all forms of the command.
    :type t: int
    """


def glTexCoord2i(s, t):
    """set the current texture coordinates
    
    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: int
    :param t: Specify t texture coordinate.
        Not all parameters are present in all forms of the command.
    :type t: int
    """


def glTexCoord2f(s, t):
    """set the current texture coordinates
    
    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: float
    :param t: Specify t texture coordinate.
        Not all parameters are present in all forms of the command.
    :type t: float
    """


def glTexCoord2d(s, t):
    """set the current texture coordinates
    
    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: float
    :param t: Specify t texture coordinate.
        Not all parameters are present in all forms of the command.
    :type t: float
    """


def glTexCoord3s(s, t, r):
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


def glTexCoord3i(s, t, r):
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


def glTexCoord3f(s, t, r):
    """set the current texture coordinates
    
    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: float
    :param t: Specify t texture coordinate.
        Not all parameters are present in all forms of the command.
    :type t: float
    :param r: Specify r texture coordinate.
        Not all parameters are present in all forms of the command.
    :type r: float
    """


def glTexCoord3d(s, t, r):
    """set the current texture coordinates
    
    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: float
    :param t: Specify t texture coordinate.
        Not all parameters are present in all forms of the command.
    :type t: float
    :param r: Specify r texture coordinate.
        Not all parameters are present in all forms of the command.
    :type r: float
    """


def glTexCoord4s(s, t, r, q):
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


def glTexCoord4i(s, t, r, q):
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


def glTexCoord4f(s, t, r, q):
    """set the current texture coordinates
    
    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: float
    :param t: Specify t texture coordinate.
        Not all parameters are present in all forms of the command.
    :type t: float
    :param r: Specify r texture coordinate.
        Not all parameters are present in all forms of the command.
    :type r: float
    :param q: Specify q texture coordinate.
        Not all parameters are present in all forms of the command.
    :type q: float
    """


def glTexCoord4d(s, t, r, q):
    """set the current texture coordinates
    
    :param s: Specify s texture coordinate.
        Not all parameters are present in all forms of the command.
    :type s: float
    :param t: Specify t texture coordinate.
        Not all parameters are present in all forms of the command.
    :type t: float
    :param r: Specify r texture coordinate.
        Not all parameters are present in all forms of the command.
    :type r: float
    :param q: Specify q texture coordinate.
        Not all parameters are present in all forms of the command.
    :type q: float
    """


def glTexCoord1sv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s texture coordinate.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glTexCoord1iv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s texture coordinate.
    :type v: bgl.Buffer[GL_INT]
    """


def glTexCoord1fv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s texture coordinate.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glTexCoord1dv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s texture coordinate.
    :type v: bgl.Buffer[GL_DOUBLE]
    """


def glTexCoord2sv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s and t texture coordinates.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glTexCoord2iv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s and t texture coordinates.
    :type v: bgl.Buffer[GL_INT]
    """


def glTexCoord2fv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s and t texture coordinates.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glTexCoord2dv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s and t texture coordinates.
    :type v: bgl.Buffer[GL_DOUBLE]
    """


def glTexCoord3sv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s, t, and r texture coordinates.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glTexCoord3iv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s, t, and r texture coordinates.
    :type v: bgl.Buffer[GL_INT]
    """


def glTexCoord3fv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s, t, and r texture coordinates.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glTexCoord3dv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s, t, and r texture coordinates.
    :type v: bgl.Buffer[GL_DOUBLE]
    """


def glTexCoord4sv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s, t, r, and q texture coordinates.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glTexCoord4iv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s, t, r, and q texture coordinates.
    :type v: bgl.Buffer[GL_INT]
    """


def glTexCoord4fv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s, t, r, and q texture coordinates.
    :type v: bgl.Buffer[GL_SHORT]
    """


def glTexCoord4dv(v):
    """set the current texture coordinates
    
    :param v: Specifies a pointer to an array of one, two, three, or four
        elements, which in turn specify the s, t, r, and q texture coordinates.
    :type v: bgl.Buffer[GL_DOUBLE]
    """


def glTexEnvi(target, pname, param):
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


def glTexEnvf(target, pname, param):
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
    :type param: float
    """


def glTexEnviv(target, pname, params):
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


def glTexEnvfv(target, pname, params):
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
    :type params: bgl.Buffer[GL_FLOAT]
    """


def glTexGeni(coord, pname, param):
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


def glTexGenf(coord, pname, param):
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
    :type param: float
    """


def glTexGend(coord, pname, param):
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
    :type param: float
    """


def glTexGeniv(coord, pname, params):
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


def glTexGenfv(coord, pname, params):
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
    :type params: bgl.Buffer[GL_FLOAT]
    """


def glTexGendv(coord, pname, params):
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
    :type params: bgl.Buffer[GL_DOUBLE]
    """


def glTexImage1D(target, level, internalformat, width, border, format, type, pixels):
    """Specify a one-dimensional texture image
    
    :param target: Specifies the target texture.
    :type target: Enumerated constant
    :param level: Specifies the level-of-detail number. Level 0 is the base image level.
                                                Level n is the nth mipmap reduction image.
    :type level: int
    :param internalformat: Specifies the number of color components in the texture.
    :type internalformat: int
    :param width: Specifies the width of the texture image. Must be 2n+2(border)
                                                for some integer n. All implementations support texture images that are
                                                at least 64 texels wide. The height of the 1D texture image is 1.
    :type width: int
    :param border: Specifies the width of the border. Must be either 0 or 1.
    :type border: int
    :param format: Specifies the format of the pixel data.
    :type format: Enumerated constant
    :param type: Specifies the data type of the pixel data.
    :type type: Enumerated constant
    :param pixels: Specifies a pointer to the image data in memory.
    :type pixels: bgl.Buffer object.
    """


def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels):
    """Specify a two-dimensional texture image
    
    :param target: Specifies the target texture.
    :type target: Enumerated constant
    :param level: Specifies the level-of-detail number. Level 0 is the base image level.
                                                Level n is the nth mipmap reduction image.
    :type level: int
    :param internalformat: Specifies the number of color components in the texture.
    :type internalformat: int
    :param width: Specifies the width of the texture image. Must be 2n+2(border)
                                                for some integer n. All implementations support texture images that are at
                                                least 64 texels wide.
    :type width: int
    :param height: Specifies the height of the texture image. Must be 2m+2(border) for
                                                some integer m. All implementations support texture images that are at
                                                least 64 texels high.
    :type height: int
    :param border: Specifies the width of the border. Must be either 0 or 1.
    :type border: int
    :param format: Specifies the format of the pixel data.
    :type format: Enumerated constant
    :param type: Specifies the data type of the pixel data.
    :type type: Enumerated constant
    :param pixels: Specifies a pointer to the image data in memory.
    :type pixels: bgl.Buffer object.
    """


def glTexParameteri(target, pname, param):
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


def glTexParameterf(target, pname, param):
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
    :type param: float
    """


def glTexParameteriv(target, pname, params):
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


def glTexParameterfv(target, pname, params):
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
    :type params: bgl.Buffer[GL_FLOAT]
    """


def glTranslatef(x, y, z):
    """multiply the current matrix by a translation matrix
    
    :param x: Specify the x coordinate of a translation vector.
    :type x: float
    :param y: Specify the y coordinate of a translation vector.
    :type y: float
    :param z: Specify the z coordinate of a translation vector.
    :type z: float
    """


def glTranslated(x, y, z):
    """multiply the current matrix by a translation matrix
    
    :param x: Specify the x coordinate of a translation vector.
    :type x: float
    :param y: Specify the y coordinate of a translation vector.
    :type y: float
    :param z: Specify the z coordinate of a translation vector.
    :type z: float
    """


def glVertex2s(x, y):
    """specify a vertex
    
    :param x: Specify x coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type x: int
    :param y: Specify y coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type y: int
    """


def glVertex2i(x, y):
    """specify a vertex
    
    :param x: Specify x coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type x: int
    :param y: Specify y coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type y: int
    """


def glVertex2f(x, y):
    """specify a vertex
    
    :param x: Specify x coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type x: float
    :param y: Specify y coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type y: float
    """


def glVertex2d(x, y):
    """specify a vertex
    
    :param x: Specify x coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type x: float
    :param y: Specify y coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type y: float
    """


def glVertex3s(x, y, z):
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


def glVertex3i(x, y, z):
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


def glVertex3f(x, y, z):
    """specify a vertex
    
    :param x: Specify x coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type x: float
    :param y: Specify y coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type y: float
    :param z: Specify z coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type z: float
    """


def glVertex3d(x, y, z):
    """specify a vertex
    
    :param x: Specify x coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type x: float
    :param y: Specify y coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type y: float
    :param z: Specify z coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type z: float
    """


def glVertex4s(x, y, z, w):
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


def glVertex4i(x, y, z, w):
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


def glVertex4f(x, y, z, w):
    """specify a vertex
    
    :param x: Specify x coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type x: float
    :param y: Specify y coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type y: float
    :param z: Specify z coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type z: float
    :param w: Specify w coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type w: float
    """


def glVertex4d(x, y, z, w):
    """specify a vertex
    
    :param x: Specify x coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type x: float
    :param y: Specify y coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type y: float
    :param z: Specify z coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type z: float
    :param w: Specify w coordinate of a vertex.
        Not all parameters are present in all forms of the command.
    :type w: float
    """


def glVertex2sv(v):
    """specify a vertex
    
    :param v: Specifies a pointer to an array of two, three, or four elements.
        The elements of a two-element array are x and y; of a three-element
        array, x, y, and z; and of a four-element array, x, y, z, and w.
    :type x: bgl.Buffer[GL_SHORT]
    """


def glVertex2iv(v):
    """specify a vertex
    
    :param v: Specifies a pointer to an array of two, three, or four elements.
        The elements of a two-element array are x and y; of a three-element
        array, x, y, and z; and of a four-element array, x, y, z, and w.
    :type x: bgl.Buffer[GL_INT]
    """


def glVertex2fv(v):
    """specify a vertex
    
    :param v: Specifies a pointer to an array of two, three, or four elements.
        The elements of a two-element array are x and y; of a three-element
        array, x, y, and z; and of a four-element array, x, y, z, and w.
    :type x: bgl.Buffer[GL_FLOAT]
    """


def glVertex2dv(v):
    """specify a vertex
    
    :param v: Specifies a pointer to an array of two, three, or four elements.
        The elements of a two-element array are x and y; of a three-element
        array, x, y, and z; and of a four-element array, x, y, z, and w.
    :type x: bgl.Buffer[GL_DOUBLE]
    """


def glVertex3sv(v):
    """specify a vertex
    
    :param v: Specifies a pointer to an array of two, three, or four elements.
        The elements of a two-element array are x and y; of a three-element
        array, x, y, and z; and of a four-element array, x, y, z, and w.
    :type x: bgl.Buffer[GL_SHORT]
    """


def glVertex3iv(v):
    """specify a vertex
    
    :param v: Specifies a pointer to an array of two, three, or four elements.
        The elements of a two-element array are x and y; of a three-element
        array, x, y, and z; and of a four-element array, x, y, z, and w.
    :type x: bgl.Buffer[GL_INT]
    """


def glVertex3fv(v):
    """specify a vertex
    
    :param v: Specifies a pointer to an array of two, three, or four elements.
        The elements of a two-element array are x and y; of a three-element
        array, x, y, and z; and of a four-element array, x, y, z, and w.
    :type x: bgl.Buffer[GL_FLOAT]
    """


def glVertex3dv(v):
    """specify a vertex
    
    :param v: Specifies a pointer to an array of two, three, or four elements.
        The elements of a two-element array are x and y; of a three-element
        array, x, y, and z; and of a four-element array, x, y, z, and w.
    :type x: bgl.Buffer[GL_DOUBLE]
    """


def glVertex4sv(v):
    """specify a vertex
    
    :param v: Specifies a pointer to an array of two, three, or four elements.
        The elements of a two-element array are x and y; of a three-element
        array, x, y, and z; and of a four-element array, x, y, z, and w.
    :type x: bgl.Buffer[GL_SHORT]
    """


def glVertex4iv(v):
    """specify a vertex
    
    :param v: Specifies a pointer to an array of two, three, or four elements.
        The elements of a two-element array are x and y; of a three-element
        array, x, y, and z; and of a four-element array, x, y, z, and w.
    :type x: bgl.Buffer[GL_INT]
    """


def glVertex4fv(v):
    """specify a vertex
    
    :param v: Specifies a pointer to an array of two, three, or four elements.
        The elements of a two-element array are x and y; of a three-element
        array, x, y, and z; and of a four-element array, x, y, z, and w.
    :type x: bgl.Buffer[GL_FLOAT]
    """


def glVertex4dv(v):
    """specify a vertex
    
    :param v: Specifies a pointer to an array of two, three, or four elements.
        The elements of a two-element array are x and y; of a three-element
        array, x, y, and z; and of a four-element array, x, y, z, and w.
    :type x: bgl.Buffer[GL_DOUBLE]
    """


def glViewport(x,y,width,height):
    """Set the viewport
    
    :param y: Specify the lower left corner of the viewport rectangle,
                                                in pixels. The initial value is (0,0).
    :type y: bge.types.KX_VertexProxy.x,
    :param height: Specify the width and height of the viewport. When a GL
                                                context is first attached to a window, width and height are set to the
                                                dimensions of that window.
    :type height: bge.render.RASOffScreen.width,
    """


def gluPerspective(fovY, aspect, zNear, zFar):
    """Set up a perspective projection matrix.
    
    :param fovY: Specifies the field of view angle, in degrees, in the y direction.
    :type fovY: bpy.types.PropertyGroupItem.double
    :param aspect: Specifies the aspect ratio that determines the field of view in the x direction.
                                                The aspect ratio is the ratio of x (width) to y (height).
    :type aspect: bpy.types.PropertyGroupItem.double
    :param zNear: Specifies the distance from the viewer to the near clipping plane (always positive).
    :type zNear: bpy.types.PropertyGroupItem.double
    :param zFar: Specifies the distance from the viewer to the far clipping plane (always positive).
    :type zFar: bpy.types.PropertyGroupItem.double
    """


def gluLookAt(eyex, eyey, eyez, centerx, centery, centerz, upx, upy, upz):
    """Define a viewing transformation.
    
    :param eyey, eyez (eyex,): Specifies the position of the eye point.
    :param centery, centerz (centerx,): Specifies the position of the reference point.
    :param upy, upz (upx,): Specifies the direction of the up vector.
    """


def gluOrtho2D(left, right, bottom, top):
    """Define a 2-D orthographic projection matrix.
    
    :param right: Specify the coordinates for the left and right vertical clipping planes.
    :type right: left,
    :param top: Specify the coordinates for the bottom and top horizontal clipping planes.
    :type top: bottom,
    """


def gluPickMatrix(x, y, width, height, viewport):
    """Define a picking region.
    
    :param y: Specify the center of a picking region in window coordinates.
    :type y: bge.types.KX_VertexProxy.x,
    :param height: Specify the width and height, respectively, of the picking region in window coordinates.
    :type height: bge.render.RASOffScreen.width,
    :param viewport: Specifies the current viewport.
    :type viewport: bgl.Buffer object. [int]
    """


def gluProject(objx, objy, objz, modelMatrix, projMatrix, viewport, winx, winy, winz):
    """Map object coordinates to window coordinates.
    
    :param objy, objz (objx,): Specify the object coordinates.
    :param modelMatrix: Specifies the current modelview matrix (as from a glGetDoublev call).
    :type modelMatrix: bgl.Buffer object. [double]
    :param projMatrix: Specifies the current projection matrix (as from a glGetDoublev call).
    :type projMatrix: bgl.Buffer object. [double]
    :param viewport: Specifies the current viewport (as from a glGetIntegerv call).
    :type viewport: bgl.Buffer object. [int]
    :param winy, winz (winx,): Return the computed window coordinates.
    """


def gluUnProject(winx, winy, winz, modelMatrix, projMatrix, viewport, objx, objy, objz):
    """Map object coordinates to window coordinates.
    
    :param winy, winz (winx,): Specify the window coordinates to be mapped.
    :param modelMatrix: Specifies the current modelview matrix (as from a glGetDoublev call).
    :type modelMatrix: bgl.Buffer object. [double]
    :param projMatrix: Specifies the current projection matrix (as from a glGetDoublev call).
    :type projMatrix: bgl.Buffer object. [double]
    :param viewport: Specifies the current viewport (as from a glGetIntegerv call).
    :type viewport: bgl.Buffer object. [int]
    :param objy, objz (objx,): Return the computed object coordinates.
    """


def glUseProgram(program):
    """Installs a program object as part of current rendering state
    
    :param program: Specifies the handle of the program object whose executables are to be used as part of current rendering state.
    :type program: int
    """


def glValidateProgram(program):
    """Validates a program object
    
    :param program: Specifies the handle of the program object to be validated.
    :type program: int
    """


def glLinkProgram(program):
    """Links a program object.
    
    :param program: Specifies the handle of the program object to be linked.
    :type program: int
    """


def glActiveTexture(texture):
    """Select active texture unit.
    
    :param texture: Constant in GL_TEXTURE0 0 - 8
    :type texture: int
    """


def glAttachShader(program, shader):
    """Attaches a shader object to a program object.
    
    :param program: Specifies the program object to which a shader object will be attached.
    :type program: int
    :param shader: Specifies the shader object that is to be attached.
    :type shader: int
    """


def glCompileShader(shader):
    """Compiles a shader object.
    
    :param shader: Specifies the shader object to be compiled.
    :type shader: int
    """


def glCreateProgram():
    """Creates a program object
    
    :rtype: int
    :return: The new program or zero if an error occurs.
    """


def glCreateShader(shaderType):
    """Creates a shader object.
    
    :type shaderType: Specifies the type of shader to be created.
                                        Must be one of GL_VERTEX_SHADER,
                                        GL_TESS_CONTROL_SHADER,
                                        GL_TESS_EVALUATION_SHADER,
                                        GL_GEOMETRY_SHADER,
                                        or GL_FRAGMENT_SHADER.
    :rtype: int
    :return: 0 if an error occurs.
    """


def glDeleteProgram(program):
    """Deletes a program object.
    
    :param program: Specifies the program object to be deleted.
    :type program: int
    """


def glDeleteShader(shader):
    """Deletes a shader object.
    
    :param shader: Specifies the shader object to be deleted.
    :type shader: int
    """


def glDetachShader(program, shader):
    """Detaches a shader object from a program object to which it is attached.
    
    :param program: Specifies the program object from which to detach the shader object.
    :type program: int
    :param shader: pecifies the program object from which to detach the shader object.
    :type shader: int
    """


def glGetAttachedShaders(program, maxCount, count, shaders):
    """Returns the handles of the shader objects attached to a program object.
    
    :param program: Specifies the program object to be queried.
    :type program: int
    :param maxCount: Specifies the size of the array for storing the returned object names.
    :type maxCount: int
    :param count: Returns the number of names actually returned in objects.
    :type count: bgl.Buffer int buffer.
    :param shaders: Specifies an array that is used to return the names of attached shader objects.
    :type shaders: bgl.Buffer int buffer.
    """


def glGetProgramInfoLog(program, maxLength, length, infoLog):
    """Returns the information log for a program object.
    
    :param program: Specifies the program object whose information log is to be queried.
    :type program: int
    :param maxLength: Specifies the size of the character buffer for storing the returned information log.
    :type maxLength: int
    :param length: Returns the length of the string returned in infoLog (excluding the null terminator).
    :type length: bgl.Buffer int buffer.
    :param infoLog: Specifies an array of characters that is used to return the information log.
    :type infoLog: bgl.Buffer char buffer.
    """


def glGetShaderInfoLog(program, maxLength, length, infoLog):
    """Returns the information log for a shader object.
    
    :param shader: Specifies the shader object whose information log is to be queried.
    :type shader: int
    :param maxLength: Specifies the size of the character buffer for storing the returned information log.
    :type maxLength: int
    :param length: Returns the length of the string returned in infoLog (excluding the null terminator).
    :type length: bgl.Buffer int buffer.
    :param infoLog: Specifies an array of characters that is used to return the information log.
    :type infoLog: bgl.Buffer char buffer.
    """


def glGetProgramiv(program, pname, params):
    """Returns a parameter from a program object.
    
    :param program: Specifies the program object to be queried.
    :type program: int
    :param pname: Specifies the object parameter.
    :type pname: int
    :param params: Returns the requested object parameter.
    :type params: bgl.Buffer int buffer.
    """


def glIsShader(shader):
    """Determines if a name corresponds to a shader object.
    
    :param shader: Specifies a potential shader object.
    :type shader: int
    """


def glIsProgram(program):
    """Determines if a name corresponds to a program object
    
    :param program: Specifies a potential program object.
    :type program: int
    """


def glGetShaderSource(shader, bufSize, length, source):
    """Returns the source code string from a shader object
    
    :param shader: Specifies the shader object to be queried.
    :type shader: int
    :param bufSize: Specifies the size of the character buffer for storing the returned source code string.
    :type bufSize: int
    :param length: Returns the length of the string returned in source (excluding the null terminator).
    :type length: bgl.Buffer int buffer.
    :param source: Specifies an array of characters that is used to return the source code string.
    :type source: bgl.Buffer char.
    """


def glShaderSource(shader, shader_string):
    """Replaces the source code in a shader object.
    
    :param shader: Specifies the handle of the shader object whose source code is to be replaced.
    :type shader: int
    :param shader_string: The shader string.
    :type shader_string: str
    """


class Buffer:
    """The Buffer object is simply a block of memory that is delineated and initialized by the
                        user. Many OpenGL functions return data to a C-style pointer, however, because this
                        is not possible in python the Buffer object can be used to this end. Wherever pointer
                        notation is used in the OpenGL functions the Buffer object can be used in it's bgl
                        wrapper. In some instances the Buffer object will need to be initialized with the template
                        parameter, while in other instances the user will want to create just a blank buffer
                        which will be zeroed by default.
    """

    dimensions = None
    """The number of dimensions of the Buffer."""

    def to_list(self):
        """The contents of the Buffer as a python list."""

    def __init__(self, type, dimensions, template = None):
        """This will create a new Buffer object for use with other bgl OpenGL commands.
                                    Only the type of argument to store in the buffer and the dimensions of the buffer
                                    are necessary. Buffers are zeroed by default unless a template is supplied, in
                                    which case the buffer is initialized to the template.
        
        :param type: The format to store data in. The type should be one of
                                                            GL_BYTE, GL_SHORT, GL_INT, or GL_FLOAT.
        :type type: int
        :param dimensions: If the dimensions are specified as an int a linear array will
                                                            be created for the buffer. If a sequence is passed for the dimensions, the buffer
                                                            becomes n-Dimensional, where n is equal to the number of parameters passed in the
                                                            sequence. Example: [256,2] is a two- dimensional buffer while [256,256,4] creates
                                                            a three- dimensional buffer. You can think of each additional dimension as a sub-item
                                                            of the dimension to the left. i.e. [10,2] is a 10 element array each with 2 sub-items.
                                                            [(0,0), (0,1), (1,0), (1,1), (2,0), ...] etc.
        :type dimensions: An int or sequence object specifying the dimensions of the buffer.
        :param template: A sequence of matching dimensions which will be used to initialize
                                                            the Buffer. If a template is not passed in all fields will be initialized to 0.
        :type template: A python sequence object (optional)
        :rtype: Buffer object
        :return: The newly created buffer as a PyObject.
        """


GL_2D = 1536
""":type: int"""

GL_2_BYTES = 5127
""":type: int"""

GL_3D = 1537
""":type: int"""

GL_3D_COLOR = 1538
""":type: int"""

GL_3D_COLOR_TEXTURE = 1539
""":type: int"""

GL_3_BYTES = 5128
""":type: int"""

GL_4D_COLOR_TEXTURE = 1540
""":type: int"""

GL_4_BYTES = 5129
""":type: int"""

GL_ACCUM = 256
""":type: int"""

GL_ACCUM_ALPHA_BITS = 3419
""":type: int"""

GL_ACCUM_BLUE_BITS = 3418
""":type: int"""

GL_ACCUM_BUFFER_BIT = 512
""":type: int"""

GL_ACCUM_CLEAR_VALUE = 2944
""":type: int"""

GL_ACCUM_GREEN_BITS = 3417
""":type: int"""

GL_ACCUM_RED_BITS = 3416
""":type: int"""

GL_ACTIVE_ATTRIBUTES = 35721
""":type: int"""

GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 35722
""":type: int"""

GL_ACTIVE_TEXTURE = 34016
""":type: int"""

GL_ACTIVE_UNIFORMS = 35718
""":type: int"""

GL_ACTIVE_UNIFORM_BLOCKS = 35382
""":type: int"""

GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH = 35381
""":type: int"""

GL_ACTIVE_UNIFORM_MAX_LENGTH = 35719
""":type: int"""

GL_ADD = 260
""":type: int"""

GL_ADD_SIGNED = 34164
""":type: int"""

GL_ALIASED_LINE_WIDTH_RANGE = 33902
""":type: int"""

GL_ALIASED_POINT_SIZE_RANGE = 33901
""":type: int"""

GL_ALL_ATTRIB_BITS = 1048575
""":type: int"""

GL_ALPHA = 6406
""":type: int"""

GL_ALPHA12 = 32829
""":type: int"""

GL_ALPHA16 = 32830
""":type: int"""

GL_ALPHA4 = 32827
""":type: int"""

GL_ALPHA8 = 32828
""":type: int"""

GL_ALPHA_BIAS = 3357
""":type: int"""

GL_ALPHA_BITS = 3413
""":type: int"""

GL_ALPHA_INTEGER = 36247
""":type: int"""

GL_ALPHA_SCALE = 3356
""":type: int"""

GL_ALPHA_TEST = 3008
""":type: int"""

GL_ALPHA_TEST_FUNC = 3009
""":type: int"""

GL_ALPHA_TEST_REF = 3010
""":type: int"""

GL_ALREADY_SIGNALED = 37146
""":type: int"""

GL_ALWAYS = 519
""":type: int"""

GL_AMBIENT = 4608
""":type: int"""

GL_AMBIENT_AND_DIFFUSE = 5634
""":type: int"""

GL_AND = 5377
""":type: int"""

GL_AND_INVERTED = 5380
""":type: int"""

GL_AND_REVERSE = 5378
""":type: int"""

GL_ANY_SAMPLES_PASSED = 35887
""":type: int"""

GL_ARRAY_BUFFER = 34962
""":type: int"""

GL_ARRAY_BUFFER_BINDING = 34964
""":type: int"""

GL_ATTACHED_SHADERS = 35717
""":type: int"""

GL_ATTRIB_STACK_DEPTH = 2992
""":type: int"""

GL_AUTO_NORMAL = 3456
""":type: int"""

GL_AUX0 = 1033
""":type: int"""

GL_AUX1 = 1034
""":type: int"""

GL_AUX2 = 1035
""":type: int"""

GL_AUX3 = 1036
""":type: int"""

GL_AUX_BUFFERS = 3072
""":type: int"""

GL_BACK = 1029
""":type: int"""

GL_BACK_LEFT = 1026
""":type: int"""

GL_BACK_RIGHT = 1027
""":type: int"""

GL_BGR = 32992
""":type: int"""

GL_BGRA = 32993
""":type: int"""

GL_BGRA_INTEGER = 36251
""":type: int"""

GL_BGR_INTEGER = 36250
""":type: int"""

GL_BITMAP = 6656
""":type: int"""

GL_BITMAP_TOKEN = 1796
""":type: int"""

GL_BLEND = 3042
""":type: int"""

GL_BLEND_DST = 3040
""":type: int"""

GL_BLEND_DST_ALPHA = 32970
""":type: int"""

GL_BLEND_DST_RGB = 32968
""":type: int"""

GL_BLEND_EQUATION_ALPHA = 34877
""":type: int"""

GL_BLEND_EQUATION_RGB = 32777
""":type: int"""

GL_BLEND_SRC = 3041
""":type: int"""

GL_BLEND_SRC_ALPHA = 32971
""":type: int"""

GL_BLEND_SRC_RGB = 32969
""":type: int"""

GL_BLUE = 6405
""":type: int"""

GL_BLUE_BIAS = 3355
""":type: int"""

GL_BLUE_BITS = 3412
""":type: int"""

GL_BLUE_INTEGER = 36246
""":type: int"""

GL_BLUE_SCALE = 3354
""":type: int"""

GL_BOOL = 35670
""":type: int"""

GL_BOOL_VEC2 = 35671
""":type: int"""

GL_BOOL_VEC3 = 35672
""":type: int"""

GL_BOOL_VEC4 = 35673
""":type: int"""

GL_BUFFER_ACCESS = 35003
""":type: int"""

GL_BUFFER_ACCESS_FLAGS = 37151
""":type: int"""

GL_BUFFER_MAPPED = 35004
""":type: int"""

GL_BUFFER_MAP_LENGTH = 37152
""":type: int"""

GL_BUFFER_MAP_OFFSET = 37153
""":type: int"""

GL_BUFFER_MAP_POINTER = 35005
""":type: int"""

GL_BUFFER_SIZE = 34660
""":type: int"""

GL_BUFFER_USAGE = 34661
""":type: int"""

GL_BYTE = 5120
""":type: int"""

GL_C3F_V3F = 10788
""":type: int"""

GL_C4F_N3F_V3F = 10790
""":type: int"""

GL_C4UB_V2F = 10786
""":type: int"""

GL_C4UB_V3F = 10787
""":type: int"""

GL_CCW = 2305
""":type: int"""

GL_CLAMP = 10496
""":type: int"""

GL_CLAMP_FRAGMENT_COLOR = 35099
""":type: int"""

GL_CLAMP_READ_COLOR = 35100
""":type: int"""

GL_CLAMP_TO_BORDER = 33069
""":type: int"""

GL_CLAMP_TO_EDGE = 33071
""":type: int"""

GL_CLAMP_VERTEX_COLOR = 35098
""":type: int"""

GL_CLEAR = 5376
""":type: int"""

GL_CLIENT_ACTIVE_TEXTURE = 34017
""":type: int"""

GL_CLIENT_ALL_ATTRIB_BITS = -1
""":type: int"""

GL_CLIENT_ATTRIB_STACK_DEPTH = 2993
""":type: int"""

GL_CLIENT_PIXEL_STORE_BIT = 1
""":type: int"""

GL_CLIENT_VERTEX_ARRAY_BIT = 2
""":type: int"""

GL_CLIP_DISTANCE0 = 12288
""":type: int"""

GL_CLIP_DISTANCE1 = 12289
""":type: int"""

GL_CLIP_DISTANCE2 = 12290
""":type: int"""

GL_CLIP_DISTANCE3 = 12291
""":type: int"""

GL_CLIP_DISTANCE4 = 12292
""":type: int"""

GL_CLIP_DISTANCE5 = 12293
""":type: int"""

GL_CLIP_PLANE0 = 12288
""":type: int"""

GL_CLIP_PLANE1 = 12289
""":type: int"""

GL_CLIP_PLANE2 = 12290
""":type: int"""

GL_CLIP_PLANE3 = 12291
""":type: int"""

GL_CLIP_PLANE4 = 12292
""":type: int"""

GL_CLIP_PLANE5 = 12293
""":type: int"""

GL_COEFF = 2560
""":type: int"""

GL_COLOR = 6144
""":type: int"""

GL_COLOR_ARRAY = 32886
""":type: int"""

GL_COLOR_ARRAY_BUFFER_BINDING = 34968
""":type: int"""

GL_COLOR_ARRAY_POINTER = 32912
""":type: int"""

GL_COLOR_ARRAY_SIZE = 32897
""":type: int"""

GL_COLOR_ARRAY_STRIDE = 32899
""":type: int"""

GL_COLOR_ARRAY_TYPE = 32898
""":type: int"""

GL_COLOR_ATTACHMENT0 = 36064
""":type: int"""

GL_COLOR_ATTACHMENT1 = 36065
""":type: int"""

GL_COLOR_ATTACHMENT10 = 36074
""":type: int"""

GL_COLOR_ATTACHMENT11 = 36075
""":type: int"""

GL_COLOR_ATTACHMENT12 = 36076
""":type: int"""

GL_COLOR_ATTACHMENT13 = 36077
""":type: int"""

GL_COLOR_ATTACHMENT14 = 36078
""":type: int"""

GL_COLOR_ATTACHMENT15 = 36079
""":type: int"""

GL_COLOR_ATTACHMENT2 = 36066
""":type: int"""

GL_COLOR_ATTACHMENT3 = 36067
""":type: int"""

GL_COLOR_ATTACHMENT4 = 36068
""":type: int"""

GL_COLOR_ATTACHMENT5 = 36069
""":type: int"""

GL_COLOR_ATTACHMENT6 = 36070
""":type: int"""

GL_COLOR_ATTACHMENT7 = 36071
""":type: int"""

GL_COLOR_ATTACHMENT8 = 36072
""":type: int"""

GL_COLOR_ATTACHMENT9 = 36073
""":type: int"""

GL_COLOR_BUFFER_BIT = 16384
""":type: int"""

GL_COLOR_CLEAR_VALUE = 3106
""":type: int"""

GL_COLOR_INDEX = 6400
""":type: int"""

GL_COLOR_INDEXES = 5635
""":type: int"""

GL_COLOR_LOGIC_OP = 3058
""":type: int"""

GL_COLOR_MATERIAL = 2903
""":type: int"""

GL_COLOR_MATERIAL_FACE = 2901
""":type: int"""

GL_COLOR_MATERIAL_PARAMETER = 2902
""":type: int"""

GL_COLOR_SUM = 33880
""":type: int"""

GL_COLOR_WRITEMASK = 3107
""":type: int"""

GL_COMBINE = 34160
""":type: int"""

GL_COMBINE_ALPHA = 34162
""":type: int"""

GL_COMBINE_RGB = 34161
""":type: int"""

GL_COMPARE_REF_TO_TEXTURE = 34894
""":type: int"""

GL_COMPARE_R_TO_TEXTURE = 34894
""":type: int"""

GL_COMPILE = 4864
""":type: int"""

GL_COMPILE_AND_EXECUTE = 4865
""":type: int"""

GL_COMPILE_STATUS = 35713
""":type: int"""

GL_COMPRESSED_ALPHA = 34025
""":type: int"""

GL_COMPRESSED_INTENSITY = 34028
""":type: int"""

GL_COMPRESSED_LUMINANCE = 34026
""":type: int"""

GL_COMPRESSED_LUMINANCE_ALPHA = 34027
""":type: int"""

GL_COMPRESSED_RED = 33317
""":type: int"""

GL_COMPRESSED_RED_RGTC1 = 36283
""":type: int"""

GL_COMPRESSED_RG = 33318
""":type: int"""

GL_COMPRESSED_RGB = 34029
""":type: int"""

GL_COMPRESSED_RGBA = 34030
""":type: int"""

GL_COMPRESSED_RG_RGTC2 = 36285
""":type: int"""

GL_COMPRESSED_SIGNED_RED_RGTC1 = 36284
""":type: int"""

GL_COMPRESSED_SIGNED_RG_RGTC2 = 36286
""":type: int"""

GL_COMPRESSED_SLUMINANCE = 35914
""":type: int"""

GL_COMPRESSED_SLUMINANCE_ALPHA = 35915
""":type: int"""

GL_COMPRESSED_SRGB = 35912
""":type: int"""

GL_COMPRESSED_SRGB_ALPHA = 35913
""":type: int"""

GL_COMPRESSED_TEXTURE_FORMATS = 34467
""":type: int"""

GL_CONDITION_SATISFIED = 37148
""":type: int"""

GL_CONSTANT = 34166
""":type: int"""

GL_CONSTANT_ALPHA = 32771
""":type: int"""

GL_CONSTANT_ATTENUATION = 4615
""":type: int"""

GL_CONSTANT_COLOR = 32769
""":type: int"""

GL_CONTEXT_COMPATIBILITY_PROFILE_BIT = 2
""":type: int"""

GL_CONTEXT_CORE_PROFILE_BIT = 1
""":type: int"""

GL_CONTEXT_FLAGS = 33310
""":type: int"""

GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT = 1
""":type: int"""

GL_CONTEXT_PROFILE_MASK = 37158
""":type: int"""

GL_COORD_REPLACE = 34914
""":type: int"""

GL_COPY = 5379
""":type: int"""

GL_COPY_INVERTED = 5388
""":type: int"""

GL_COPY_PIXEL_TOKEN = 1798
""":type: int"""

GL_COPY_READ_BUFFER = 36662
""":type: int"""

GL_COPY_WRITE_BUFFER = 36663
""":type: int"""

GL_CULL_FACE = 2884
""":type: int"""

GL_CULL_FACE_MODE = 2885
""":type: int"""

GL_CURRENT_BIT = 1
""":type: int"""

GL_CURRENT_COLOR = 2816
""":type: int"""

GL_CURRENT_FOG_COORD = 33875
""":type: int"""

GL_CURRENT_FOG_COORDINATE = 33875
""":type: int"""

GL_CURRENT_INDEX = 2817
""":type: int"""

GL_CURRENT_NORMAL = 2818
""":type: int"""

GL_CURRENT_PROGRAM = 35725
""":type: int"""

GL_CURRENT_QUERY = 34917
""":type: int"""

GL_CURRENT_RASTER_COLOR = 2820
""":type: int"""

GL_CURRENT_RASTER_DISTANCE = 2825
""":type: int"""

GL_CURRENT_RASTER_INDEX = 2821
""":type: int"""

GL_CURRENT_RASTER_POSITION = 2823
""":type: int"""

GL_CURRENT_RASTER_POSITION_VALID = 2824
""":type: int"""

GL_CURRENT_RASTER_SECONDARY_COLOR = 33887
""":type: int"""

GL_CURRENT_RASTER_TEXTURE_COORDS = 2822
""":type: int"""

GL_CURRENT_SECONDARY_COLOR = 33881
""":type: int"""

GL_CURRENT_TEXTURE_COORDS = 2819
""":type: int"""

GL_CURRENT_VERTEX_ATTRIB = 34342
""":type: int"""

GL_CW = 2304
""":type: int"""

GL_DECAL = 8449
""":type: int"""

GL_DECR = 7683
""":type: int"""

GL_DECR_WRAP = 34056
""":type: int"""

GL_DELETE_STATUS = 35712
""":type: int"""

GL_DEPTH = 6145
""":type: int"""

GL_DEPTH24_STENCIL8 = 35056
""":type: int"""

GL_DEPTH32F_STENCIL8 = 36013
""":type: int"""

GL_DEPTH_ATTACHMENT = 36096
""":type: int"""

GL_DEPTH_BIAS = 3359
""":type: int"""

GL_DEPTH_BITS = 3414
""":type: int"""

GL_DEPTH_BUFFER_BIT = 256
""":type: int"""

GL_DEPTH_CLAMP = 34383
""":type: int"""

GL_DEPTH_CLEAR_VALUE = 2931
""":type: int"""

GL_DEPTH_COMPONENT = 6402
""":type: int"""

GL_DEPTH_COMPONENT16 = 33189
""":type: int"""

GL_DEPTH_COMPONENT24 = 33190
""":type: int"""

GL_DEPTH_COMPONENT32 = 33191
""":type: int"""

GL_DEPTH_COMPONENT32F = 36012
""":type: int"""

GL_DEPTH_FUNC = 2932
""":type: int"""

GL_DEPTH_RANGE = 2928
""":type: int"""

GL_DEPTH_SCALE = 3358
""":type: int"""

GL_DEPTH_STENCIL = 34041
""":type: int"""

GL_DEPTH_STENCIL_ATTACHMENT = 33306
""":type: int"""

GL_DEPTH_TEST = 2929
""":type: int"""

GL_DEPTH_TEXTURE_MODE = 34891
""":type: int"""

GL_DEPTH_WRITEMASK = 2930
""":type: int"""

GL_DIFFUSE = 4609
""":type: int"""

GL_DITHER = 3024
""":type: int"""

GL_DOMAIN = 2562
""":type: int"""

GL_DONT_CARE = 4352
""":type: int"""

GL_DOT3_RGB = 34478
""":type: int"""

GL_DOT3_RGBA = 34479
""":type: int"""

GL_DOUBLE = 5130
""":type: int"""

GL_DOUBLEBUFFER = 3122
""":type: int"""

GL_DRAW_BUFFER = 3073
""":type: int"""

GL_DRAW_BUFFER0 = 34853
""":type: int"""

GL_DRAW_BUFFER1 = 34854
""":type: int"""

GL_DRAW_BUFFER10 = 34863
""":type: int"""

GL_DRAW_BUFFER11 = 34864
""":type: int"""

GL_DRAW_BUFFER12 = 34865
""":type: int"""

GL_DRAW_BUFFER13 = 34866
""":type: int"""

GL_DRAW_BUFFER14 = 34867
""":type: int"""

GL_DRAW_BUFFER15 = 34868
""":type: int"""

GL_DRAW_BUFFER2 = 34855
""":type: int"""

GL_DRAW_BUFFER3 = 34856
""":type: int"""

GL_DRAW_BUFFER4 = 34857
""":type: int"""

GL_DRAW_BUFFER5 = 34858
""":type: int"""

GL_DRAW_BUFFER6 = 34859
""":type: int"""

GL_DRAW_BUFFER7 = 34860
""":type: int"""

GL_DRAW_BUFFER8 = 34861
""":type: int"""

GL_DRAW_BUFFER9 = 34862
""":type: int"""

GL_DRAW_FRAMEBUFFER = 36009
""":type: int"""

GL_DRAW_FRAMEBUFFER_BINDING = 36006
""":type: int"""

GL_DRAW_PIXEL_TOKEN = 1797
""":type: int"""

GL_DST_ALPHA = 772
""":type: int"""

GL_DST_COLOR = 774
""":type: int"""

GL_DYNAMIC_COPY = 35050
""":type: int"""

GL_DYNAMIC_DRAW = 35048
""":type: int"""

GL_DYNAMIC_READ = 35049
""":type: int"""

GL_EDGE_FLAG = 2883
""":type: int"""

GL_EDGE_FLAG_ARRAY = 32889
""":type: int"""

GL_EDGE_FLAG_ARRAY_BUFFER_BINDING = 34971
""":type: int"""

GL_EDGE_FLAG_ARRAY_POINTER = 32915
""":type: int"""

GL_EDGE_FLAG_ARRAY_STRIDE = 32908
""":type: int"""

GL_ELEMENT_ARRAY_BUFFER = 34963
""":type: int"""

GL_ELEMENT_ARRAY_BUFFER_BINDING = 34965
""":type: int"""

GL_EMISSION = 5632
""":type: int"""

GL_ENABLE_BIT = 8192
""":type: int"""

GL_EQUAL = 514
""":type: int"""

GL_EQUIV = 5385
""":type: int"""

GL_EVAL_BIT = 65536
""":type: int"""

GL_EXP = 2048
""":type: int"""

GL_EXP2 = 2049
""":type: int"""

GL_EXTENSIONS = 7939
""":type: int"""

GL_EYE_LINEAR = 9216
""":type: int"""

GL_EYE_PLANE = 9474
""":type: int"""

GL_FALSE = 0
""":type: int"""

GL_FASTEST = 4353
""":type: int"""

GL_FEEDBACK = 7169
""":type: int"""

GL_FEEDBACK_BUFFER_POINTER = 3568
""":type: int"""

GL_FEEDBACK_BUFFER_SIZE = 3569
""":type: int"""

GL_FEEDBACK_BUFFER_TYPE = 3570
""":type: int"""

GL_FILL = 6914
""":type: int"""

GL_FIRST_VERTEX_CONVENTION = 36429
""":type: int"""

GL_FIXED_ONLY = 35101
""":type: int"""

GL_FLAT = 7424
""":type: int"""

GL_FLOAT = 5126
""":type: int"""

GL_FLOAT_32_UNSIGNED_INT_24_8_REV = 36269
""":type: int"""

GL_FLOAT_MAT2 = 35674
""":type: int"""

GL_FLOAT_MAT2x3 = 35685
""":type: int"""

GL_FLOAT_MAT2x4 = 35686
""":type: int"""

GL_FLOAT_MAT3 = 35675
""":type: int"""

GL_FLOAT_MAT3x2 = 35687
""":type: int"""

GL_FLOAT_MAT3x4 = 35688
""":type: int"""

GL_FLOAT_MAT4 = 35676
""":type: int"""

GL_FLOAT_MAT4x2 = 35689
""":type: int"""

GL_FLOAT_MAT4x3 = 35690
""":type: int"""

GL_FLOAT_VEC2 = 35664
""":type: int"""

GL_FLOAT_VEC3 = 35665
""":type: int"""

GL_FLOAT_VEC4 = 35666
""":type: int"""

GL_FOG = 2912
""":type: int"""

GL_FOG_BIT = 128
""":type: int"""

GL_FOG_COLOR = 2918
""":type: int"""

GL_FOG_COORD = 33873
""":type: int"""

GL_FOG_COORDINATE = 33873
""":type: int"""

GL_FOG_COORDINATE_ARRAY = 33879
""":type: int"""

GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING = 34973
""":type: int"""

GL_FOG_COORDINATE_ARRAY_POINTER = 33878
""":type: int"""

GL_FOG_COORDINATE_ARRAY_STRIDE = 33877
""":type: int"""

GL_FOG_COORDINATE_ARRAY_TYPE = 33876
""":type: int"""

GL_FOG_COORDINATE_SOURCE = 33872
""":type: int"""

GL_FOG_COORD_ARRAY = 33879
""":type: int"""

GL_FOG_COORD_ARRAY_BUFFER_BINDING = 34973
""":type: int"""

GL_FOG_COORD_ARRAY_POINTER = 33878
""":type: int"""

GL_FOG_COORD_ARRAY_STRIDE = 33877
""":type: int"""

GL_FOG_COORD_ARRAY_TYPE = 33876
""":type: int"""

GL_FOG_COORD_SRC = 33872
""":type: int"""

GL_FOG_DENSITY = 2914
""":type: int"""

GL_FOG_END = 2916
""":type: int"""

GL_FOG_HINT = 3156
""":type: int"""

GL_FOG_INDEX = 2913
""":type: int"""

GL_FOG_MODE = 2917
""":type: int"""

GL_FOG_START = 2915
""":type: int"""

GL_FRAGMENT_DEPTH = 33874
""":type: int"""

GL_FRAGMENT_SHADER = 35632
""":type: int"""

GL_FRAGMENT_SHADER_DERIVATIVE_HINT = 35723
""":type: int"""

GL_FRAMEBUFFER = 36160
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = 33301
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = 33300
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = 33296
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = 33297
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = 33302
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = 33299
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_LAYERED = 36263
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 36049
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 36048
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE = 33298
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = 33303
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 36051
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = 36052
""":type: int"""

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 36050
""":type: int"""

GL_FRAMEBUFFER_BINDING = 36006
""":type: int"""

GL_FRAMEBUFFER_COMPLETE = 36053
""":type: int"""

GL_FRAMEBUFFER_DEFAULT = 33304
""":type: int"""

GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 36054
""":type: int"""

GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER = 36059
""":type: int"""

GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS = 36264
""":type: int"""

GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 36055
""":type: int"""

GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = 36182
""":type: int"""

GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER = 36060
""":type: int"""

GL_FRAMEBUFFER_SRGB = 36281
""":type: int"""

GL_FRAMEBUFFER_UNDEFINED = 33305
""":type: int"""

GL_FRAMEBUFFER_UNSUPPORTED = 36061
""":type: int"""

GL_FRONT = 1028
""":type: int"""

GL_FRONT_AND_BACK = 1032
""":type: int"""

GL_FRONT_FACE = 2886
""":type: int"""

GL_FRONT_LEFT = 1024
""":type: int"""

GL_FRONT_RIGHT = 1025
""":type: int"""

GL_FUNC_ADD = 32774
""":type: int"""

GL_FUNC_REVERSE_SUBTRACT = 32779
""":type: int"""

GL_FUNC_SUBTRACT = 32778
""":type: int"""

GL_GENERATE_MIPMAP = 33169
""":type: int"""

GL_GENERATE_MIPMAP_HINT = 33170
""":type: int"""

GL_GEOMETRY_INPUT_TYPE = 35095
""":type: int"""

GL_GEOMETRY_OUTPUT_TYPE = 35096
""":type: int"""

GL_GEOMETRY_SHADER = 36313
""":type: int"""

GL_GEOMETRY_VERTICES_OUT = 35094
""":type: int"""

GL_GEQUAL = 518
""":type: int"""

GL_GREATER = 516
""":type: int"""

GL_GREEN = 6404
""":type: int"""

GL_GREEN_BIAS = 3353
""":type: int"""

GL_GREEN_BITS = 3411
""":type: int"""

GL_GREEN_INTEGER = 36245
""":type: int"""

GL_GREEN_SCALE = 3352
""":type: int"""

GL_HALF_FLOAT = 5131
""":type: int"""

GL_HINT_BIT = 32768
""":type: int"""

GL_INCR = 7682
""":type: int"""

GL_INCR_WRAP = 34055
""":type: int"""

GL_INDEX = 33314
""":type: int"""

GL_INDEX_ARRAY = 32887
""":type: int"""

GL_INDEX_ARRAY_BUFFER_BINDING = 34969
""":type: int"""

GL_INDEX_ARRAY_POINTER = 32913
""":type: int"""

GL_INDEX_ARRAY_STRIDE = 32902
""":type: int"""

GL_INDEX_ARRAY_TYPE = 32901
""":type: int"""

GL_INDEX_BITS = 3409
""":type: int"""

GL_INDEX_CLEAR_VALUE = 3104
""":type: int"""

GL_INDEX_LOGIC_OP = 3057
""":type: int"""

GL_INDEX_MODE = 3120
""":type: int"""

GL_INDEX_OFFSET = 3347
""":type: int"""

GL_INDEX_SHIFT = 3346
""":type: int"""

GL_INDEX_WRITEMASK = 3105
""":type: int"""

GL_INFO_LOG_LENGTH = 35716
""":type: int"""

GL_INT = 5124
""":type: int"""

GL_INTENSITY = 32841
""":type: int"""

GL_INTENSITY12 = 32844
""":type: int"""

GL_INTENSITY16 = 32845
""":type: int"""

GL_INTENSITY4 = 32842
""":type: int"""

GL_INTENSITY8 = 32843
""":type: int"""

GL_INTERLEAVED_ATTRIBS = 35980
""":type: int"""

GL_INTERPOLATE = 34165
""":type: int"""

GL_INT_2_10_10_10_REV = 36255
""":type: int"""

GL_INT_SAMPLER_1D = 36297
""":type: int"""

GL_INT_SAMPLER_1D_ARRAY = 36302
""":type: int"""

GL_INT_SAMPLER_2D = 36298
""":type: int"""

GL_INT_SAMPLER_2D_ARRAY = 36303
""":type: int"""

GL_INT_SAMPLER_2D_MULTISAMPLE = 37129
""":type: int"""

GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 37132
""":type: int"""

GL_INT_SAMPLER_2D_RECT = 36301
""":type: int"""

GL_INT_SAMPLER_3D = 36299
""":type: int"""

GL_INT_SAMPLER_BUFFER = 36304
""":type: int"""

GL_INT_SAMPLER_CUBE = 36300
""":type: int"""

GL_INT_VEC2 = 35667
""":type: int"""

GL_INT_VEC3 = 35668
""":type: int"""

GL_INT_VEC4 = 35669
""":type: int"""

GL_INVALID_ENUM = 1280
""":type: int"""

GL_INVALID_FRAMEBUFFER_OPERATION = 1286
""":type: int"""

GL_INVALID_INDEX = -1
""":type: int"""

GL_INVALID_OPERATION = 1282
""":type: int"""

GL_INVALID_VALUE = 1281
""":type: int"""

GL_INVERT = 5386
""":type: int"""

GL_KEEP = 7680
""":type: int"""

GL_LAST_VERTEX_CONVENTION = 36430
""":type: int"""

GL_LEFT = 1030
""":type: int"""

GL_LEQUAL = 515
""":type: int"""

GL_LESS = 513
""":type: int"""

GL_LIGHT0 = 16384
""":type: int"""

GL_LIGHT1 = 16385
""":type: int"""

GL_LIGHT2 = 16386
""":type: int"""

GL_LIGHT3 = 16387
""":type: int"""

GL_LIGHT4 = 16388
""":type: int"""

GL_LIGHT5 = 16389
""":type: int"""

GL_LIGHT6 = 16390
""":type: int"""

GL_LIGHT7 = 16391
""":type: int"""

GL_LIGHTING = 2896
""":type: int"""

GL_LIGHTING_BIT = 64
""":type: int"""

GL_LIGHT_MODEL_AMBIENT = 2899
""":type: int"""

GL_LIGHT_MODEL_COLOR_CONTROL = 33272
""":type: int"""

GL_LIGHT_MODEL_LOCAL_VIEWER = 2897
""":type: int"""

GL_LIGHT_MODEL_TWO_SIDE = 2898
""":type: int"""

GL_LINE = 6913
""":type: int"""

GL_LINEAR = 9729
""":type: int"""

GL_LINEAR_ATTENUATION = 4616
""":type: int"""

GL_LINEAR_MIPMAP_LINEAR = 9987
""":type: int"""

GL_LINEAR_MIPMAP_NEAREST = 9985
""":type: int"""

GL_LINES = 1
""":type: int"""

GL_LINES_ADJACENCY = 10
""":type: int"""

GL_LINE_BIT = 4
""":type: int"""

GL_LINE_LOOP = 2
""":type: int"""

GL_LINE_RESET_TOKEN = 1799
""":type: int"""

GL_LINE_SMOOTH = 2848
""":type: int"""

GL_LINE_SMOOTH_HINT = 3154
""":type: int"""

GL_LINE_STIPPLE = 2852
""":type: int"""

GL_LINE_STIPPLE_PATTERN = 2853
""":type: int"""

GL_LINE_STIPPLE_REPEAT = 2854
""":type: int"""

GL_LINE_STRIP = 3
""":type: int"""

GL_LINE_STRIP_ADJACENCY = 11
""":type: int"""

GL_LINE_TOKEN = 1794
""":type: int"""

GL_LINE_WIDTH = 2849
""":type: int"""

GL_LINE_WIDTH_GRANULARITY = 2851
""":type: int"""

GL_LINE_WIDTH_RANGE = 2850
""":type: int"""

GL_LINK_STATUS = 35714
""":type: int"""

GL_LIST_BASE = 2866
""":type: int"""

GL_LIST_BIT = 131072
""":type: int"""

GL_LIST_INDEX = 2867
""":type: int"""

GL_LIST_MODE = 2864
""":type: int"""

GL_LOAD = 257
""":type: int"""

GL_LOGIC_OP = 3057
""":type: int"""

GL_LOGIC_OP_MODE = 3056
""":type: int"""

GL_LOWER_LEFT = 36001
""":type: int"""

GL_LUMINANCE = 6409
""":type: int"""

GL_LUMINANCE12 = 32833
""":type: int"""

GL_LUMINANCE12_ALPHA12 = 32839
""":type: int"""

GL_LUMINANCE12_ALPHA4 = 32838
""":type: int"""

GL_LUMINANCE16 = 32834
""":type: int"""

GL_LUMINANCE16_ALPHA16 = 32840
""":type: int"""

GL_LUMINANCE4 = 32831
""":type: int"""

GL_LUMINANCE4_ALPHA4 = 32835
""":type: int"""

GL_LUMINANCE6_ALPHA2 = 32836
""":type: int"""

GL_LUMINANCE8 = 32832
""":type: int"""

GL_LUMINANCE8_ALPHA8 = 32837
""":type: int"""

GL_LUMINANCE_ALPHA = 6410
""":type: int"""

GL_MAJOR_VERSION = 33307
""":type: int"""

GL_MAP1_COLOR_4 = 3472
""":type: int"""

GL_MAP1_GRID_DOMAIN = 3536
""":type: int"""

GL_MAP1_GRID_SEGMENTS = 3537
""":type: int"""

GL_MAP1_INDEX = 3473
""":type: int"""

GL_MAP1_NORMAL = 3474
""":type: int"""

GL_MAP1_TEXTURE_COORD_1 = 3475
""":type: int"""

GL_MAP1_TEXTURE_COORD_2 = 3476
""":type: int"""

GL_MAP1_TEXTURE_COORD_3 = 3477
""":type: int"""

GL_MAP1_TEXTURE_COORD_4 = 3478
""":type: int"""

GL_MAP1_VERTEX_3 = 3479
""":type: int"""

GL_MAP1_VERTEX_4 = 3480
""":type: int"""

GL_MAP2_COLOR_4 = 3504
""":type: int"""

GL_MAP2_GRID_DOMAIN = 3538
""":type: int"""

GL_MAP2_GRID_SEGMENTS = 3539
""":type: int"""

GL_MAP2_INDEX = 3505
""":type: int"""

GL_MAP2_NORMAL = 3506
""":type: int"""

GL_MAP2_TEXTURE_COORD_1 = 3507
""":type: int"""

GL_MAP2_TEXTURE_COORD_2 = 3508
""":type: int"""

GL_MAP2_TEXTURE_COORD_3 = 3509
""":type: int"""

GL_MAP2_TEXTURE_COORD_4 = 3510
""":type: int"""

GL_MAP2_VERTEX_3 = 3511
""":type: int"""

GL_MAP2_VERTEX_4 = 3512
""":type: int"""

GL_MAP_COLOR = 3344
""":type: int"""

GL_MAP_FLUSH_EXPLICIT_BIT = 16
""":type: int"""

GL_MAP_INVALIDATE_BUFFER_BIT = 8
""":type: int"""

GL_MAP_INVALIDATE_RANGE_BIT = 4
""":type: int"""

GL_MAP_READ_BIT = 1
""":type: int"""

GL_MAP_STENCIL = 3345
""":type: int"""

GL_MAP_UNSYNCHRONIZED_BIT = 32
""":type: int"""

GL_MAP_WRITE_BIT = 2
""":type: int"""

GL_MATRIX_MODE = 2976
""":type: int"""

GL_MAX = 32776
""":type: int"""

GL_MAX_3D_TEXTURE_SIZE = 32883
""":type: int"""

GL_MAX_ARRAY_TEXTURE_LAYERS = 35071
""":type: int"""

GL_MAX_ATTRIB_STACK_DEPTH = 3381
""":type: int"""

GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = 3387
""":type: int"""

GL_MAX_CLIP_DISTANCES = 3378
""":type: int"""

GL_MAX_CLIP_PLANES = 3378
""":type: int"""

GL_MAX_COLOR_ATTACHMENTS = 36063
""":type: int"""

GL_MAX_COLOR_TEXTURE_SAMPLES = 37134
""":type: int"""

GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = 35379
""":type: int"""

GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS = 35378
""":type: int"""

GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 35661
""":type: int"""

GL_MAX_COMBINED_UNIFORM_BLOCKS = 35374
""":type: int"""

GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = 35377
""":type: int"""

GL_MAX_CUBE_MAP_TEXTURE_SIZE = 34076
""":type: int"""

GL_MAX_DEPTH_TEXTURE_SAMPLES = 37135
""":type: int"""

GL_MAX_DRAW_BUFFERS = 34852
""":type: int"""

GL_MAX_DUAL_SOURCE_DRAW_BUFFERS = 35068
""":type: int"""

GL_MAX_ELEMENTS_INDICES = 33001
""":type: int"""

GL_MAX_ELEMENTS_VERTICES = 33000
""":type: int"""

GL_MAX_EVAL_ORDER = 3376
""":type: int"""

GL_MAX_FRAGMENT_INPUT_COMPONENTS = 37157
""":type: int"""

GL_MAX_FRAGMENT_UNIFORM_BLOCKS = 35373
""":type: int"""

GL_MAX_FRAGMENT_UNIFORM_COMPONENTS = 35657
""":type: int"""

GL_MAX_GEOMETRY_INPUT_COMPONENTS = 37155
""":type: int"""

GL_MAX_GEOMETRY_OUTPUT_COMPONENTS = 37156
""":type: int"""

GL_MAX_GEOMETRY_OUTPUT_VERTICES = 36320
""":type: int"""

GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS = 35881
""":type: int"""

GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS = 36321
""":type: int"""

GL_MAX_GEOMETRY_UNIFORM_BLOCKS = 35372
""":type: int"""

GL_MAX_GEOMETRY_UNIFORM_COMPONENTS = 36319
""":type: int"""

GL_MAX_INTEGER_SAMPLES = 37136
""":type: int"""

GL_MAX_LIGHTS = 3377
""":type: int"""

GL_MAX_LIST_NESTING = 2865
""":type: int"""

GL_MAX_MODELVIEW_STACK_DEPTH = 3382
""":type: int"""

GL_MAX_NAME_STACK_DEPTH = 3383
""":type: int"""

GL_MAX_PIXEL_MAP_TABLE = 3380
""":type: int"""

GL_MAX_PROGRAM_TEXEL_OFFSET = 35077
""":type: int"""

GL_MAX_PROJECTION_STACK_DEPTH = 3384
""":type: int"""

GL_MAX_RECTANGLE_TEXTURE_SIZE = 34040
""":type: int"""

GL_MAX_RENDERBUFFER_SIZE = 34024
""":type: int"""

GL_MAX_SAMPLES = 36183
""":type: int"""

GL_MAX_SAMPLE_MASK_WORDS = 36441
""":type: int"""

GL_MAX_SERVER_WAIT_TIMEOUT = 37137
""":type: int"""

GL_MAX_TEXTURE_BUFFER_SIZE = 35883
""":type: int"""

GL_MAX_TEXTURE_COORDS = 34929
""":type: int"""

GL_MAX_TEXTURE_IMAGE_UNITS = 34930
""":type: int"""

GL_MAX_TEXTURE_LOD_BIAS = 34045
""":type: int"""

GL_MAX_TEXTURE_SIZE = 3379
""":type: int"""

GL_MAX_TEXTURE_STACK_DEPTH = 3385
""":type: int"""

GL_MAX_TEXTURE_UNITS = 34018
""":type: int"""

GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = 35978
""":type: int"""

GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = 35979
""":type: int"""

GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = 35968
""":type: int"""

GL_MAX_UNIFORM_BLOCK_SIZE = 35376
""":type: int"""

GL_MAX_UNIFORM_BUFFER_BINDINGS = 35375
""":type: int"""

GL_MAX_VARYING_COMPONENTS = 35659
""":type: int"""

GL_MAX_VARYING_FLOATS = 35659
""":type: int"""

GL_MAX_VERTEX_ATTRIBS = 34921
""":type: int"""

GL_MAX_VERTEX_OUTPUT_COMPONENTS = 37154
""":type: int"""

GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 35660
""":type: int"""

GL_MAX_VERTEX_UNIFORM_BLOCKS = 35371
""":type: int"""

GL_MAX_VERTEX_UNIFORM_COMPONENTS = 35658
""":type: int"""

GL_MAX_VIEWPORT_DIMS = 3386
""":type: int"""

GL_MIN = 32775
""":type: int"""

GL_MINOR_VERSION = 33308
""":type: int"""

GL_MIN_PROGRAM_TEXEL_OFFSET = 35076
""":type: int"""

GL_MIRRORED_REPEAT = 33648
""":type: int"""

GL_MODELVIEW = 5888
""":type: int"""

GL_MODELVIEW_MATRIX = 2982
""":type: int"""

GL_MODELVIEW_STACK_DEPTH = 2979
""":type: int"""

GL_MODULATE = 8448
""":type: int"""

GL_MULT = 259
""":type: int"""

GL_MULTISAMPLE = 32925
""":type: int"""

GL_MULTISAMPLE_BIT = 536870912
""":type: int"""

GL_N3F_V3F = 10789
""":type: int"""

GL_NAME_STACK_DEPTH = 3440
""":type: int"""

GL_NAND = 5390
""":type: int"""

GL_NEAREST = 9728
""":type: int"""

GL_NEAREST_MIPMAP_LINEAR = 9986
""":type: int"""

GL_NEAREST_MIPMAP_NEAREST = 9984
""":type: int"""

GL_NEVER = 512
""":type: int"""

GL_NICEST = 4354
""":type: int"""

GL_NONE = 0
""":type: int"""

GL_NOOP = 5381
""":type: int"""

GL_NOR = 5384
""":type: int"""

GL_NORMALIZE = 2977
""":type: int"""

GL_NORMAL_ARRAY = 32885
""":type: int"""

GL_NORMAL_ARRAY_BUFFER_BINDING = 34967
""":type: int"""

GL_NORMAL_ARRAY_POINTER = 32911
""":type: int"""

GL_NORMAL_ARRAY_STRIDE = 32895
""":type: int"""

GL_NORMAL_ARRAY_TYPE = 32894
""":type: int"""

GL_NORMAL_MAP = 34065
""":type: int"""

GL_NOTEQUAL = 517
""":type: int"""

GL_NO_ERROR = 0
""":type: int"""

GL_NUM_COMPRESSED_TEXTURE_FORMATS = 34466
""":type: int"""

GL_NUM_EXTENSIONS = 33309
""":type: int"""

GL_OBJECT_LINEAR = 9217
""":type: int"""

GL_OBJECT_PLANE = 9473
""":type: int"""

GL_OBJECT_TYPE = 37138
""":type: int"""

GL_ONE = 1
""":type: int"""

GL_ONE_MINUS_CONSTANT_ALPHA = 32772
""":type: int"""

GL_ONE_MINUS_CONSTANT_COLOR = 32770
""":type: int"""

GL_ONE_MINUS_DST_ALPHA = 773
""":type: int"""

GL_ONE_MINUS_DST_COLOR = 775
""":type: int"""

GL_ONE_MINUS_SRC1_ALPHA = 35067
""":type: int"""

GL_ONE_MINUS_SRC1_COLOR = 35066
""":type: int"""

GL_ONE_MINUS_SRC_ALPHA = 771
""":type: int"""

GL_ONE_MINUS_SRC_COLOR = 769
""":type: int"""

GL_OPERAND0_ALPHA = 34200
""":type: int"""

GL_OPERAND0_RGB = 34192
""":type: int"""

GL_OPERAND1_ALPHA = 34201
""":type: int"""

GL_OPERAND1_RGB = 34193
""":type: int"""

GL_OPERAND2_ALPHA = 34202
""":type: int"""

GL_OPERAND2_RGB = 34194
""":type: int"""

GL_OR = 5383
""":type: int"""

GL_ORDER = 2561
""":type: int"""

GL_OR_INVERTED = 5389
""":type: int"""

GL_OR_REVERSE = 5387
""":type: int"""

GL_OUT_OF_MEMORY = 1285
""":type: int"""

GL_PACK_ALIGNMENT = 3333
""":type: int"""

GL_PACK_IMAGE_HEIGHT = 32876
""":type: int"""

GL_PACK_LSB_FIRST = 3329
""":type: int"""

GL_PACK_ROW_LENGTH = 3330
""":type: int"""

GL_PACK_SKIP_IMAGES = 32875
""":type: int"""

GL_PACK_SKIP_PIXELS = 3332
""":type: int"""

GL_PACK_SKIP_ROWS = 3331
""":type: int"""

GL_PACK_SWAP_BYTES = 3328
""":type: int"""

GL_PASS_THROUGH_TOKEN = 1792
""":type: int"""

GL_PERSPECTIVE_CORRECTION_HINT = 3152
""":type: int"""

GL_PIXEL_MAP_A_TO_A = 3193
""":type: int"""

GL_PIXEL_MAP_A_TO_A_SIZE = 3257
""":type: int"""

GL_PIXEL_MAP_B_TO_B = 3192
""":type: int"""

GL_PIXEL_MAP_B_TO_B_SIZE = 3256
""":type: int"""

GL_PIXEL_MAP_G_TO_G = 3191
""":type: int"""

GL_PIXEL_MAP_G_TO_G_SIZE = 3255
""":type: int"""

GL_PIXEL_MAP_I_TO_A = 3189
""":type: int"""

GL_PIXEL_MAP_I_TO_A_SIZE = 3253
""":type: int"""

GL_PIXEL_MAP_I_TO_B = 3188
""":type: int"""

GL_PIXEL_MAP_I_TO_B_SIZE = 3252
""":type: int"""

GL_PIXEL_MAP_I_TO_G = 3187
""":type: int"""

GL_PIXEL_MAP_I_TO_G_SIZE = 3251
""":type: int"""

GL_PIXEL_MAP_I_TO_I = 3184
""":type: int"""

GL_PIXEL_MAP_I_TO_I_SIZE = 3248
""":type: int"""

GL_PIXEL_MAP_I_TO_R = 3186
""":type: int"""

GL_PIXEL_MAP_I_TO_R_SIZE = 3250
""":type: int"""

GL_PIXEL_MAP_R_TO_R = 3190
""":type: int"""

GL_PIXEL_MAP_R_TO_R_SIZE = 3254
""":type: int"""

GL_PIXEL_MAP_S_TO_S = 3185
""":type: int"""

GL_PIXEL_MAP_S_TO_S_SIZE = 3249
""":type: int"""

GL_PIXEL_MODE_BIT = 32
""":type: int"""

GL_PIXEL_PACK_BUFFER = 35051
""":type: int"""

GL_PIXEL_PACK_BUFFER_BINDING = 35053
""":type: int"""

GL_PIXEL_UNPACK_BUFFER = 35052
""":type: int"""

GL_PIXEL_UNPACK_BUFFER_BINDING = 35055
""":type: int"""

GL_POINT = 6912
""":type: int"""

GL_POINTS = 0
""":type: int"""

GL_POINT_BIT = 2
""":type: int"""

GL_POINT_DISTANCE_ATTENUATION = 33065
""":type: int"""

GL_POINT_FADE_THRESHOLD_SIZE = 33064
""":type: int"""

GL_POINT_SIZE = 2833
""":type: int"""

GL_POINT_SIZE_GRANULARITY = 2835
""":type: int"""

GL_POINT_SIZE_MAX = 33063
""":type: int"""

GL_POINT_SIZE_MIN = 33062
""":type: int"""

GL_POINT_SIZE_RANGE = 2834
""":type: int"""

GL_POINT_SMOOTH = 2832
""":type: int"""

GL_POINT_SMOOTH_HINT = 3153
""":type: int"""

GL_POINT_SPRITE = 34913
""":type: int"""

GL_POINT_SPRITE_COORD_ORIGIN = 36000
""":type: int"""

GL_POINT_TOKEN = 1793
""":type: int"""

GL_POLYGON = 9
""":type: int"""

GL_POLYGON_BIT = 8
""":type: int"""

GL_POLYGON_MODE = 2880
""":type: int"""

GL_POLYGON_OFFSET_FACTOR = 32824
""":type: int"""

GL_POLYGON_OFFSET_FILL = 32823
""":type: int"""

GL_POLYGON_OFFSET_LINE = 10754
""":type: int"""

GL_POLYGON_OFFSET_POINT = 10753
""":type: int"""

GL_POLYGON_OFFSET_UNITS = 10752
""":type: int"""

GL_POLYGON_SMOOTH = 2881
""":type: int"""

GL_POLYGON_SMOOTH_HINT = 3155
""":type: int"""

GL_POLYGON_STIPPLE = 2882
""":type: int"""

GL_POLYGON_STIPPLE_BIT = 16
""":type: int"""

GL_POLYGON_TOKEN = 1795
""":type: int"""

GL_POSITION = 4611
""":type: int"""

GL_PREVIOUS = 34168
""":type: int"""

GL_PRIMARY_COLOR = 34167
""":type: int"""

GL_PRIMITIVES_GENERATED = 35975
""":type: int"""

GL_PRIMITIVE_RESTART = 36765
""":type: int"""

GL_PRIMITIVE_RESTART_INDEX = 36766
""":type: int"""

GL_PROGRAM_POINT_SIZE = 34370
""":type: int"""

GL_PROJECTION = 5889
""":type: int"""

GL_PROJECTION_MATRIX = 2983
""":type: int"""

GL_PROJECTION_STACK_DEPTH = 2980
""":type: int"""

GL_PROVOKING_VERTEX = 36431
""":type: int"""

GL_PROXY_TEXTURE_1D = 32867
""":type: int"""

GL_PROXY_TEXTURE_1D_ARRAY = 35865
""":type: int"""

GL_PROXY_TEXTURE_2D = 32868
""":type: int"""

GL_PROXY_TEXTURE_2D_ARRAY = 35867
""":type: int"""

GL_PROXY_TEXTURE_2D_MULTISAMPLE = 37121
""":type: int"""

GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY = 37123
""":type: int"""

GL_PROXY_TEXTURE_3D = 32880
""":type: int"""

GL_PROXY_TEXTURE_CUBE_MAP = 34075
""":type: int"""

GL_PROXY_TEXTURE_RECTANGLE = 34039
""":type: int"""

GL_Q = 8195
""":type: int"""

GL_QUADRATIC_ATTENUATION = 4617
""":type: int"""

GL_QUADS = 7
""":type: int"""

GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION = 36428
""":type: int"""

GL_QUAD_STRIP = 8
""":type: int"""

GL_QUERY_BY_REGION_NO_WAIT = 36374
""":type: int"""

GL_QUERY_BY_REGION_WAIT = 36373
""":type: int"""

GL_QUERY_COUNTER_BITS = 34916
""":type: int"""

GL_QUERY_NO_WAIT = 36372
""":type: int"""

GL_QUERY_RESULT = 34918
""":type: int"""

GL_QUERY_RESULT_AVAILABLE = 34919
""":type: int"""

GL_QUERY_WAIT = 36371
""":type: int"""

GL_R = 8194
""":type: int"""

GL_R11F_G11F_B10F = 35898
""":type: int"""

GL_R16 = 33322
""":type: int"""

GL_R16F = 33325
""":type: int"""

GL_R16I = 33331
""":type: int"""

GL_R16UI = 33332
""":type: int"""

GL_R16_SNORM = 36760
""":type: int"""

GL_R32F = 33326
""":type: int"""

GL_R32I = 33333
""":type: int"""

GL_R32UI = 33334
""":type: int"""

GL_R3_G3_B2 = 10768
""":type: int"""

GL_R8 = 33321
""":type: int"""

GL_R8I = 33329
""":type: int"""

GL_R8UI = 33330
""":type: int"""

GL_R8_SNORM = 36756
""":type: int"""

GL_RASTERIZER_DISCARD = 35977
""":type: int"""

GL_READ_BUFFER = 3074
""":type: int"""

GL_READ_FRAMEBUFFER = 36008
""":type: int"""

GL_READ_FRAMEBUFFER_BINDING = 36010
""":type: int"""

GL_READ_ONLY = 35000
""":type: int"""

GL_READ_WRITE = 35002
""":type: int"""

GL_RED = 6403
""":type: int"""

GL_RED_BIAS = 3349
""":type: int"""

GL_RED_BITS = 3410
""":type: int"""

GL_RED_INTEGER = 36244
""":type: int"""

GL_RED_SCALE = 3348
""":type: int"""

GL_REFLECTION_MAP = 34066
""":type: int"""

GL_RENDER = 7168
""":type: int"""

GL_RENDERBUFFER = 36161
""":type: int"""

GL_RENDERBUFFER_ALPHA_SIZE = 36179
""":type: int"""

GL_RENDERBUFFER_BINDING = 36007
""":type: int"""

GL_RENDERBUFFER_BLUE_SIZE = 36178
""":type: int"""

GL_RENDERBUFFER_DEPTH_SIZE = 36180
""":type: int"""

GL_RENDERBUFFER_GREEN_SIZE = 36177
""":type: int"""

GL_RENDERBUFFER_HEIGHT = 36163
""":type: int"""

GL_RENDERBUFFER_INTERNAL_FORMAT = 36164
""":type: int"""

GL_RENDERBUFFER_RED_SIZE = 36176
""":type: int"""

GL_RENDERBUFFER_SAMPLES = 36011
""":type: int"""

GL_RENDERBUFFER_STENCIL_SIZE = 36181
""":type: int"""

GL_RENDERBUFFER_WIDTH = 36162
""":type: int"""

GL_RENDERER = 7937
""":type: int"""

GL_RENDER_MODE = 3136
""":type: int"""

GL_REPEAT = 10497
""":type: int"""

GL_REPLACE = 7681
""":type: int"""

GL_RESCALE_NORMAL = 32826
""":type: int"""

GL_RETURN = 258
""":type: int"""

GL_RG = 33319
""":type: int"""

GL_RG16 = 33324
""":type: int"""

GL_RG16F = 33327
""":type: int"""

GL_RG16I = 33337
""":type: int"""

GL_RG16UI = 33338
""":type: int"""

GL_RG16_SNORM = 36761
""":type: int"""

GL_RG32F = 33328
""":type: int"""

GL_RG32I = 33339
""":type: int"""

GL_RG32UI = 33340
""":type: int"""

GL_RG8 = 33323
""":type: int"""

GL_RG8I = 33335
""":type: int"""

GL_RG8UI = 33336
""":type: int"""

GL_RG8_SNORM = 36757
""":type: int"""

GL_RGB = 6407
""":type: int"""

GL_RGB10 = 32850
""":type: int"""

GL_RGB10_A2 = 32857
""":type: int"""

GL_RGB10_A2UI = 36975
""":type: int"""

GL_RGB12 = 32851
""":type: int"""

GL_RGB16 = 32852
""":type: int"""

GL_RGB16F = 34843
""":type: int"""

GL_RGB16I = 36233
""":type: int"""

GL_RGB16UI = 36215
""":type: int"""

GL_RGB16_SNORM = 36762
""":type: int"""

GL_RGB32F = 34837
""":type: int"""

GL_RGB32I = 36227
""":type: int"""

GL_RGB32UI = 36209
""":type: int"""

GL_RGB4 = 32847
""":type: int"""

GL_RGB5 = 32848
""":type: int"""

GL_RGB5_A1 = 32855
""":type: int"""

GL_RGB8 = 32849
""":type: int"""

GL_RGB8I = 36239
""":type: int"""

GL_RGB8UI = 36221
""":type: int"""

GL_RGB8_SNORM = 36758
""":type: int"""

GL_RGB9_E5 = 35901
""":type: int"""

GL_RGBA = 6408
""":type: int"""

GL_RGBA12 = 32858
""":type: int"""

GL_RGBA16 = 32859
""":type: int"""

GL_RGBA16F = 34842
""":type: int"""

GL_RGBA16I = 36232
""":type: int"""

GL_RGBA16UI = 36214
""":type: int"""

GL_RGBA16_SNORM = 36763
""":type: int"""

GL_RGBA2 = 32853
""":type: int"""

GL_RGBA32F = 34836
""":type: int"""

GL_RGBA32I = 36226
""":type: int"""

GL_RGBA32UI = 36208
""":type: int"""

GL_RGBA4 = 32854
""":type: int"""

GL_RGBA8 = 32856
""":type: int"""

GL_RGBA8I = 36238
""":type: int"""

GL_RGBA8UI = 36220
""":type: int"""

GL_RGBA8_SNORM = 36759
""":type: int"""

GL_RGBA_INTEGER = 36249
""":type: int"""

GL_RGBA_MODE = 3121
""":type: int"""

GL_RGB_INTEGER = 36248
""":type: int"""

GL_RGB_SCALE = 34163
""":type: int"""

GL_RG_INTEGER = 33320
""":type: int"""

GL_RIGHT = 1031
""":type: int"""

GL_S = 8192
""":type: int"""

GL_SAMPLER_1D = 35677
""":type: int"""

GL_SAMPLER_1D_ARRAY = 36288
""":type: int"""

GL_SAMPLER_1D_ARRAY_SHADOW = 36291
""":type: int"""

GL_SAMPLER_1D_SHADOW = 35681
""":type: int"""

GL_SAMPLER_2D = 35678
""":type: int"""

GL_SAMPLER_2D_ARRAY = 36289
""":type: int"""

GL_SAMPLER_2D_ARRAY_SHADOW = 36292
""":type: int"""

GL_SAMPLER_2D_MULTISAMPLE = 37128
""":type: int"""

GL_SAMPLER_2D_MULTISAMPLE_ARRAY = 37131
""":type: int"""

GL_SAMPLER_2D_RECT = 35683
""":type: int"""

GL_SAMPLER_2D_RECT_SHADOW = 35684
""":type: int"""

GL_SAMPLER_2D_SHADOW = 35682
""":type: int"""

GL_SAMPLER_3D = 35679
""":type: int"""

GL_SAMPLER_BINDING = 35097
""":type: int"""

GL_SAMPLER_BUFFER = 36290
""":type: int"""

GL_SAMPLER_CUBE = 35680
""":type: int"""

GL_SAMPLER_CUBE_SHADOW = 36293
""":type: int"""

GL_SAMPLES = 32937
""":type: int"""

GL_SAMPLES_PASSED = 35092
""":type: int"""

GL_SAMPLE_ALPHA_TO_COVERAGE = 32926
""":type: int"""

GL_SAMPLE_ALPHA_TO_ONE = 32927
""":type: int"""

GL_SAMPLE_BUFFERS = 32936
""":type: int"""

GL_SAMPLE_COVERAGE = 32928
""":type: int"""

GL_SAMPLE_COVERAGE_INVERT = 32939
""":type: int"""

GL_SAMPLE_COVERAGE_VALUE = 32938
""":type: int"""

GL_SAMPLE_MASK = 36433
""":type: int"""

GL_SAMPLE_MASK_VALUE = 36434
""":type: int"""

GL_SAMPLE_POSITION = 36432
""":type: int"""

GL_SCISSOR_BIT = 524288
""":type: int"""

GL_SCISSOR_BOX = 3088
""":type: int"""

GL_SCISSOR_TEST = 3089
""":type: int"""

GL_SECONDARY_COLOR_ARRAY = 33886
""":type: int"""

GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING = 34972
""":type: int"""

GL_SECONDARY_COLOR_ARRAY_POINTER = 33885
""":type: int"""

GL_SECONDARY_COLOR_ARRAY_SIZE = 33882
""":type: int"""

GL_SECONDARY_COLOR_ARRAY_STRIDE = 33884
""":type: int"""

GL_SECONDARY_COLOR_ARRAY_TYPE = 33883
""":type: int"""

GL_SELECT = 7170
""":type: int"""

GL_SELECTION_BUFFER_POINTER = 3571
""":type: int"""

GL_SELECTION_BUFFER_SIZE = 3572
""":type: int"""

GL_SEPARATE_ATTRIBS = 35981
""":type: int"""

GL_SEPARATE_SPECULAR_COLOR = 33274
""":type: int"""

GL_SET = 5391
""":type: int"""

GL_SHADER_SOURCE_LENGTH = 35720
""":type: int"""

GL_SHADER_TYPE = 35663
""":type: int"""

GL_SHADE_MODEL = 2900
""":type: int"""

GL_SHADING_LANGUAGE_VERSION = 35724
""":type: int"""

GL_SHININESS = 5633
""":type: int"""

GL_SHORT = 5122
""":type: int"""

GL_SIGNALED = 37145
""":type: int"""

GL_SIGNED_NORMALIZED = 36764
""":type: int"""

GL_SINGLE_COLOR = 33273
""":type: int"""

GL_SLUMINANCE = 35910
""":type: int"""

GL_SLUMINANCE8 = 35911
""":type: int"""

GL_SLUMINANCE8_ALPHA8 = 35909
""":type: int"""

GL_SLUMINANCE_ALPHA = 35908
""":type: int"""

GL_SMOOTH = 7425
""":type: int"""

GL_SMOOTH_LINE_WIDTH_GRANULARITY = 2851
""":type: int"""

GL_SMOOTH_LINE_WIDTH_RANGE = 2850
""":type: int"""

GL_SMOOTH_POINT_SIZE_GRANULARITY = 2835
""":type: int"""

GL_SMOOTH_POINT_SIZE_RANGE = 2834
""":type: int"""

GL_SOURCE0_ALPHA = 34184
""":type: int"""

GL_SOURCE0_RGB = 34176
""":type: int"""

GL_SOURCE1_ALPHA = 34185
""":type: int"""

GL_SOURCE1_RGB = 34177
""":type: int"""

GL_SOURCE2_ALPHA = 34186
""":type: int"""

GL_SOURCE2_RGB = 34178
""":type: int"""

GL_SPECULAR = 4610
""":type: int"""

GL_SPHERE_MAP = 9218
""":type: int"""

GL_SPOT_CUTOFF = 4614
""":type: int"""

GL_SPOT_DIRECTION = 4612
""":type: int"""

GL_SPOT_EXPONENT = 4613
""":type: int"""

GL_SRC0_ALPHA = 34184
""":type: int"""

GL_SRC0_RGB = 34176
""":type: int"""

GL_SRC1_ALPHA = 34185
""":type: int"""

GL_SRC1_COLOR = 35065
""":type: int"""

GL_SRC1_RGB = 34177
""":type: int"""

GL_SRC2_ALPHA = 34186
""":type: int"""

GL_SRC2_RGB = 34178
""":type: int"""

GL_SRC_ALPHA = 770
""":type: int"""

GL_SRC_ALPHA_SATURATE = 776
""":type: int"""

GL_SRC_COLOR = 768
""":type: int"""

GL_SRGB = 35904
""":type: int"""

GL_SRGB8 = 35905
""":type: int"""

GL_SRGB8_ALPHA8 = 35907
""":type: int"""

GL_SRGB_ALPHA = 35906
""":type: int"""

GL_STACK_OVERFLOW = 1283
""":type: int"""

GL_STACK_UNDERFLOW = 1284
""":type: int"""

GL_STATIC_COPY = 35046
""":type: int"""

GL_STATIC_DRAW = 35044
""":type: int"""

GL_STATIC_READ = 35045
""":type: int"""

GL_STENCIL = 6146
""":type: int"""

GL_STENCIL_ATTACHMENT = 36128
""":type: int"""

GL_STENCIL_BACK_FAIL = 34817
""":type: int"""

GL_STENCIL_BACK_FUNC = 34816
""":type: int"""

GL_STENCIL_BACK_PASS_DEPTH_FAIL = 34818
""":type: int"""

GL_STENCIL_BACK_PASS_DEPTH_PASS = 34819
""":type: int"""

GL_STENCIL_BACK_REF = 36003
""":type: int"""

GL_STENCIL_BACK_VALUE_MASK = 36004
""":type: int"""

GL_STENCIL_BACK_WRITEMASK = 36005
""":type: int"""

GL_STENCIL_BITS = 3415
""":type: int"""

GL_STENCIL_BUFFER_BIT = 1024
""":type: int"""

GL_STENCIL_CLEAR_VALUE = 2961
""":type: int"""

GL_STENCIL_FAIL = 2964
""":type: int"""

GL_STENCIL_FUNC = 2962
""":type: int"""

GL_STENCIL_INDEX = 6401
""":type: int"""

GL_STENCIL_INDEX1 = 36166
""":type: int"""

GL_STENCIL_INDEX16 = 36169
""":type: int"""

GL_STENCIL_INDEX4 = 36167
""":type: int"""

GL_STENCIL_INDEX8 = 36168
""":type: int"""

GL_STENCIL_PASS_DEPTH_FAIL = 2965
""":type: int"""

GL_STENCIL_PASS_DEPTH_PASS = 2966
""":type: int"""

GL_STENCIL_REF = 2967
""":type: int"""

GL_STENCIL_TEST = 2960
""":type: int"""

GL_STENCIL_VALUE_MASK = 2963
""":type: int"""

GL_STENCIL_WRITEMASK = 2968
""":type: int"""

GL_STEREO = 3123
""":type: int"""

GL_STREAM_COPY = 35042
""":type: int"""

GL_STREAM_DRAW = 35040
""":type: int"""

GL_STREAM_READ = 35041
""":type: int"""

GL_SUBPIXEL_BITS = 3408
""":type: int"""

GL_SUBTRACT = 34023
""":type: int"""

GL_SYNC_CONDITION = 37139
""":type: int"""

GL_SYNC_FENCE = 37142
""":type: int"""

GL_SYNC_FLAGS = 37141
""":type: int"""

GL_SYNC_FLUSH_COMMANDS_BIT = 1
""":type: int"""

GL_SYNC_GPU_COMMANDS_COMPLETE = 37143
""":type: int"""

GL_SYNC_STATUS = 37140
""":type: int"""

GL_T = 8193
""":type: int"""

GL_T2F_C3F_V3F = 10794
""":type: int"""

GL_T2F_C4F_N3F_V3F = 10796
""":type: int"""

GL_T2F_C4UB_V3F = 10793
""":type: int"""

GL_T2F_N3F_V3F = 10795
""":type: int"""

GL_T2F_V3F = 10791
""":type: int"""

GL_T4F_C4F_N3F_V4F = 10797
""":type: int"""

GL_T4F_V4F = 10792
""":type: int"""

GL_TEXTURE = 5890
""":type: int"""

GL_TEXTURE0 = 33984
""":type: int"""

GL_TEXTURE1 = 33985
""":type: int"""

GL_TEXTURE10 = 33994
""":type: int"""

GL_TEXTURE11 = 33995
""":type: int"""

GL_TEXTURE12 = 33996
""":type: int"""

GL_TEXTURE13 = 33997
""":type: int"""

GL_TEXTURE14 = 33998
""":type: int"""

GL_TEXTURE15 = 33999
""":type: int"""

GL_TEXTURE16 = 34000
""":type: int"""

GL_TEXTURE17 = 34001
""":type: int"""

GL_TEXTURE18 = 34002
""":type: int"""

GL_TEXTURE19 = 34003
""":type: int"""

GL_TEXTURE2 = 33986
""":type: int"""

GL_TEXTURE20 = 34004
""":type: int"""

GL_TEXTURE21 = 34005
""":type: int"""

GL_TEXTURE22 = 34006
""":type: int"""

GL_TEXTURE23 = 34007
""":type: int"""

GL_TEXTURE24 = 34008
""":type: int"""

GL_TEXTURE25 = 34009
""":type: int"""

GL_TEXTURE26 = 34010
""":type: int"""

GL_TEXTURE27 = 34011
""":type: int"""

GL_TEXTURE28 = 34012
""":type: int"""

GL_TEXTURE29 = 34013
""":type: int"""

GL_TEXTURE3 = 33987
""":type: int"""

GL_TEXTURE30 = 34014
""":type: int"""

GL_TEXTURE31 = 34015
""":type: int"""

GL_TEXTURE4 = 33988
""":type: int"""

GL_TEXTURE5 = 33989
""":type: int"""

GL_TEXTURE6 = 33990
""":type: int"""

GL_TEXTURE7 = 33991
""":type: int"""

GL_TEXTURE8 = 33992
""":type: int"""

GL_TEXTURE9 = 33993
""":type: int"""

GL_TEXTURE_1D = 3552
""":type: int"""

GL_TEXTURE_1D_ARRAY = 35864
""":type: int"""

GL_TEXTURE_2D = 3553
""":type: int"""

GL_TEXTURE_2D_ARRAY = 35866
""":type: int"""

GL_TEXTURE_2D_MULTISAMPLE = 37120
""":type: int"""

GL_TEXTURE_2D_MULTISAMPLE_ARRAY = 37122
""":type: int"""

GL_TEXTURE_3D = 32879
""":type: int"""

GL_TEXTURE_ALPHA_SIZE = 32863
""":type: int"""

GL_TEXTURE_ALPHA_TYPE = 35859
""":type: int"""

GL_TEXTURE_BASE_LEVEL = 33084
""":type: int"""

GL_TEXTURE_BINDING_1D = 32872
""":type: int"""

GL_TEXTURE_BINDING_1D_ARRAY = 35868
""":type: int"""

GL_TEXTURE_BINDING_2D = 32873
""":type: int"""

GL_TEXTURE_BINDING_2D_ARRAY = 35869
""":type: int"""

GL_TEXTURE_BINDING_2D_MULTISAMPLE = 37124
""":type: int"""

GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY = 37125
""":type: int"""

GL_TEXTURE_BINDING_3D = 32874
""":type: int"""

GL_TEXTURE_BINDING_BUFFER = 35884
""":type: int"""

GL_TEXTURE_BINDING_CUBE_MAP = 34068
""":type: int"""

GL_TEXTURE_BINDING_RECTANGLE = 34038
""":type: int"""

GL_TEXTURE_BIT = 262144
""":type: int"""

GL_TEXTURE_BLUE_SIZE = 32862
""":type: int"""

GL_TEXTURE_BLUE_TYPE = 35858
""":type: int"""

GL_TEXTURE_BORDER = 4101
""":type: int"""

GL_TEXTURE_BORDER_COLOR = 4100
""":type: int"""

GL_TEXTURE_BUFFER = 35882
""":type: int"""

GL_TEXTURE_BUFFER_DATA_STORE_BINDING = 35885
""":type: int"""

GL_TEXTURE_COMPARE_FUNC = 34893
""":type: int"""

GL_TEXTURE_COMPARE_MODE = 34892
""":type: int"""

GL_TEXTURE_COMPONENTS = 4099
""":type: int"""

GL_TEXTURE_COMPRESSED = 34465
""":type: int"""

GL_TEXTURE_COMPRESSED_IMAGE_SIZE = 34464
""":type: int"""

GL_TEXTURE_COMPRESSION_HINT = 34031
""":type: int"""

GL_TEXTURE_COORD_ARRAY = 32888
""":type: int"""

GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING = 34970
""":type: int"""

GL_TEXTURE_COORD_ARRAY_POINTER = 32914
""":type: int"""

GL_TEXTURE_COORD_ARRAY_SIZE = 32904
""":type: int"""

GL_TEXTURE_COORD_ARRAY_STRIDE = 32906
""":type: int"""

GL_TEXTURE_COORD_ARRAY_TYPE = 32905
""":type: int"""

GL_TEXTURE_CUBE_MAP = 34067
""":type: int"""

GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 34070
""":type: int"""

GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 34072
""":type: int"""

GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 34074
""":type: int"""

GL_TEXTURE_CUBE_MAP_POSITIVE_X = 34069
""":type: int"""

GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 34071
""":type: int"""

GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 34073
""":type: int"""

GL_TEXTURE_CUBE_MAP_SEAMLESS = 34895
""":type: int"""

GL_TEXTURE_DEPTH = 32881
""":type: int"""

GL_TEXTURE_DEPTH_SIZE = 34890
""":type: int"""

GL_TEXTURE_DEPTH_TYPE = 35862
""":type: int"""

GL_TEXTURE_ENV = 8960
""":type: int"""

GL_TEXTURE_ENV_COLOR = 8705
""":type: int"""

GL_TEXTURE_ENV_MODE = 8704
""":type: int"""

GL_TEXTURE_FILTER_CONTROL = 34048
""":type: int"""

GL_TEXTURE_FIXED_SAMPLE_LOCATIONS = 37127
""":type: int"""

GL_TEXTURE_GEN_MODE = 9472
""":type: int"""

GL_TEXTURE_GEN_Q = 3171
""":type: int"""

GL_TEXTURE_GEN_R = 3170
""":type: int"""

GL_TEXTURE_GEN_S = 3168
""":type: int"""

GL_TEXTURE_GEN_T = 3169
""":type: int"""

GL_TEXTURE_GREEN_SIZE = 32861
""":type: int"""

GL_TEXTURE_GREEN_TYPE = 35857
""":type: int"""

GL_TEXTURE_HEIGHT = 4097
""":type: int"""

GL_TEXTURE_INTENSITY_SIZE = 32865
""":type: int"""

GL_TEXTURE_INTENSITY_TYPE = 35861
""":type: int"""

GL_TEXTURE_INTERNAL_FORMAT = 4099
""":type: int"""

GL_TEXTURE_LOD_BIAS = 34049
""":type: int"""

GL_TEXTURE_LUMINANCE_SIZE = 32864
""":type: int"""

GL_TEXTURE_LUMINANCE_TYPE = 35860
""":type: int"""

GL_TEXTURE_MAG_FILTER = 10240
""":type: int"""

GL_TEXTURE_MATRIX = 2984
""":type: int"""

GL_TEXTURE_MAX_LEVEL = 33085
""":type: int"""

GL_TEXTURE_MAX_LOD = 33083
""":type: int"""

GL_TEXTURE_MIN_FILTER = 10241
""":type: int"""

GL_TEXTURE_MIN_LOD = 33082
""":type: int"""

GL_TEXTURE_PRIORITY = 32870
""":type: int"""

GL_TEXTURE_RECTANGLE = 34037
""":type: int"""

GL_TEXTURE_RED_SIZE = 32860
""":type: int"""

GL_TEXTURE_RED_TYPE = 35856
""":type: int"""

GL_TEXTURE_RESIDENT = 32871
""":type: int"""

GL_TEXTURE_SAMPLES = 37126
""":type: int"""

GL_TEXTURE_SHARED_SIZE = 35903
""":type: int"""

GL_TEXTURE_STACK_DEPTH = 2981
""":type: int"""

GL_TEXTURE_STENCIL_SIZE = 35057
""":type: int"""

GL_TEXTURE_SWIZZLE_A = 36421
""":type: int"""

GL_TEXTURE_SWIZZLE_B = 36420
""":type: int"""

GL_TEXTURE_SWIZZLE_G = 36419
""":type: int"""

GL_TEXTURE_SWIZZLE_R = 36418
""":type: int"""

GL_TEXTURE_SWIZZLE_RGBA = 36422
""":type: int"""

GL_TEXTURE_WIDTH = 4096
""":type: int"""

GL_TEXTURE_WRAP_R = 32882
""":type: int"""

GL_TEXTURE_WRAP_S = 10242
""":type: int"""

GL_TEXTURE_WRAP_T = 10243
""":type: int"""

GL_TIMEOUT_EXPIRED = 37147
""":type: int"""

GL_TIMEOUT_IGNORED = -1
""":type: int"""

GL_TIMESTAMP = 36392
""":type: int"""

GL_TIME_ELAPSED = 35007
""":type: int"""

GL_TRANSFORM_BIT = 4096
""":type: int"""

GL_TRANSFORM_FEEDBACK_BUFFER = 35982
""":type: int"""

GL_TRANSFORM_FEEDBACK_BUFFER_BINDING = 35983
""":type: int"""

GL_TRANSFORM_FEEDBACK_BUFFER_MODE = 35967
""":type: int"""

GL_TRANSFORM_FEEDBACK_BUFFER_SIZE = 35973
""":type: int"""

GL_TRANSFORM_FEEDBACK_BUFFER_START = 35972
""":type: int"""

GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = 35976
""":type: int"""

GL_TRANSFORM_FEEDBACK_VARYINGS = 35971
""":type: int"""

GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH = 35958
""":type: int"""

GL_TRANSPOSE_COLOR_MATRIX = 34022
""":type: int"""

GL_TRANSPOSE_MODELVIEW_MATRIX = 34019
""":type: int"""

GL_TRANSPOSE_PROJECTION_MATRIX = 34020
""":type: int"""

GL_TRANSPOSE_TEXTURE_MATRIX = 34021
""":type: int"""

GL_TRIANGLES = 4
""":type: int"""

GL_TRIANGLES_ADJACENCY = 12
""":type: int"""

GL_TRIANGLE_FAN = 6
""":type: int"""

GL_TRIANGLE_STRIP = 5
""":type: int"""

GL_TRIANGLE_STRIP_ADJACENCY = 13
""":type: int"""

GL_TRUE = 1
""":type: int"""

GL_UNIFORM_ARRAY_STRIDE = 35388
""":type: int"""

GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS = 35394
""":type: int"""

GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = 35395
""":type: int"""

GL_UNIFORM_BLOCK_BINDING = 35391
""":type: int"""

GL_UNIFORM_BLOCK_DATA_SIZE = 35392
""":type: int"""

GL_UNIFORM_BLOCK_INDEX = 35386
""":type: int"""

GL_UNIFORM_BLOCK_NAME_LENGTH = 35393
""":type: int"""

GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = 35398
""":type: int"""

GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER = 35397
""":type: int"""

GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = 35396
""":type: int"""

GL_UNIFORM_BUFFER = 35345
""":type: int"""

GL_UNIFORM_BUFFER_BINDING = 35368
""":type: int"""

GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT = 35380
""":type: int"""

GL_UNIFORM_BUFFER_SIZE = 35370
""":type: int"""

GL_UNIFORM_BUFFER_START = 35369
""":type: int"""

GL_UNIFORM_IS_ROW_MAJOR = 35390
""":type: int"""

GL_UNIFORM_MATRIX_STRIDE = 35389
""":type: int"""

GL_UNIFORM_NAME_LENGTH = 35385
""":type: int"""

GL_UNIFORM_OFFSET = 35387
""":type: int"""

GL_UNIFORM_SIZE = 35384
""":type: int"""

GL_UNIFORM_TYPE = 35383
""":type: int"""

GL_UNPACK_ALIGNMENT = 3317
""":type: int"""

GL_UNPACK_IMAGE_HEIGHT = 32878
""":type: int"""

GL_UNPACK_LSB_FIRST = 3313
""":type: int"""

GL_UNPACK_ROW_LENGTH = 3314
""":type: int"""

GL_UNPACK_SKIP_IMAGES = 32877
""":type: int"""

GL_UNPACK_SKIP_PIXELS = 3316
""":type: int"""

GL_UNPACK_SKIP_ROWS = 3315
""":type: int"""

GL_UNPACK_SWAP_BYTES = 3312
""":type: int"""

GL_UNSIGNALED = 37144
""":type: int"""

GL_UNSIGNED_BYTE = 5121
""":type: int"""

GL_UNSIGNED_BYTE_2_3_3_REV = 33634
""":type: int"""

GL_UNSIGNED_BYTE_3_3_2 = 32818
""":type: int"""

GL_UNSIGNED_INT = 5125
""":type: int"""

GL_UNSIGNED_INT_10F_11F_11F_REV = 35899
""":type: int"""

GL_UNSIGNED_INT_10_10_10_2 = 32822
""":type: int"""

GL_UNSIGNED_INT_24_8 = 34042
""":type: int"""

GL_UNSIGNED_INT_2_10_10_10_REV = 33640
""":type: int"""

GL_UNSIGNED_INT_5_9_9_9_REV = 35902
""":type: int"""

GL_UNSIGNED_INT_8_8_8_8 = 32821
""":type: int"""

GL_UNSIGNED_INT_8_8_8_8_REV = 33639
""":type: int"""

GL_UNSIGNED_INT_SAMPLER_1D = 36305
""":type: int"""

GL_UNSIGNED_INT_SAMPLER_1D_ARRAY = 36310
""":type: int"""

GL_UNSIGNED_INT_SAMPLER_2D = 36306
""":type: int"""

GL_UNSIGNED_INT_SAMPLER_2D_ARRAY = 36311
""":type: int"""

GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE = 37130
""":type: int"""

GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 37133
""":type: int"""

GL_UNSIGNED_INT_SAMPLER_2D_RECT = 36309
""":type: int"""

GL_UNSIGNED_INT_SAMPLER_3D = 36307
""":type: int"""

GL_UNSIGNED_INT_SAMPLER_BUFFER = 36312
""":type: int"""

GL_UNSIGNED_INT_SAMPLER_CUBE = 36308
""":type: int"""

GL_UNSIGNED_INT_VEC2 = 36294
""":type: int"""

GL_UNSIGNED_INT_VEC3 = 36295
""":type: int"""

GL_UNSIGNED_INT_VEC4 = 36296
""":type: int"""

GL_UNSIGNED_NORMALIZED = 35863
""":type: int"""

GL_UNSIGNED_SHORT = 5123
""":type: int"""

GL_UNSIGNED_SHORT_1_5_5_5_REV = 33638
""":type: int"""

GL_UNSIGNED_SHORT_4_4_4_4 = 32819
""":type: int"""

GL_UNSIGNED_SHORT_4_4_4_4_REV = 33637
""":type: int"""

GL_UNSIGNED_SHORT_5_5_5_1 = 32820
""":type: int"""

GL_UNSIGNED_SHORT_5_6_5 = 33635
""":type: int"""

GL_UNSIGNED_SHORT_5_6_5_REV = 33636
""":type: int"""

GL_UPPER_LEFT = 36002
""":type: int"""

GL_V2F = 10784
""":type: int"""

GL_V3F = 10785
""":type: int"""

GL_VALIDATE_STATUS = 35715
""":type: int"""

GL_VENDOR = 7936
""":type: int"""

GL_VERSION = 7938
""":type: int"""

GL_VERTEX_ARRAY = 32884
""":type: int"""

GL_VERTEX_ARRAY_BINDING = 34229
""":type: int"""

GL_VERTEX_ARRAY_BUFFER_BINDING = 34966
""":type: int"""

GL_VERTEX_ARRAY_POINTER = 32910
""":type: int"""

GL_VERTEX_ARRAY_SIZE = 32890
""":type: int"""

GL_VERTEX_ARRAY_STRIDE = 32892
""":type: int"""

GL_VERTEX_ARRAY_TYPE = 32891
""":type: int"""

GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 34975
""":type: int"""

GL_VERTEX_ATTRIB_ARRAY_DIVISOR = 35070
""":type: int"""

GL_VERTEX_ATTRIB_ARRAY_ENABLED = 34338
""":type: int"""

GL_VERTEX_ATTRIB_ARRAY_INTEGER = 35069
""":type: int"""

GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 34922
""":type: int"""

GL_VERTEX_ATTRIB_ARRAY_POINTER = 34373
""":type: int"""

GL_VERTEX_ATTRIB_ARRAY_SIZE = 34339
""":type: int"""

GL_VERTEX_ATTRIB_ARRAY_STRIDE = 34340
""":type: int"""

GL_VERTEX_ATTRIB_ARRAY_TYPE = 34341
""":type: int"""

GL_VERTEX_PROGRAM_POINT_SIZE = 34370
""":type: int"""

GL_VERTEX_PROGRAM_TWO_SIDE = 34371
""":type: int"""

GL_VERTEX_SHADER = 35633
""":type: int"""

GL_VIEWPORT = 2978
""":type: int"""

GL_VIEWPORT_BIT = 2048
""":type: int"""

GL_WAIT_FAILED = 37149
""":type: int"""

GL_WEIGHT_ARRAY_BUFFER_BINDING = 34974
""":type: int"""

GL_WRITE_ONLY = 35001
""":type: int"""

GL_XOR = 5382
""":type: int"""

GL_ZERO = 0
""":type: int"""

GL_ZOOM_X = 3350
""":type: int"""

GL_ZOOM_Y = 3351
""":type: int"""
