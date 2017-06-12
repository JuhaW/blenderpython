KX_TEXFACE_MATERIAL = None
"""Materials as defined by the texture face settings."""

KX_BLENDER_MULTITEX_MATERIAL = None
"""Materials approximating blender materials with multitexturing."""

KX_BLENDER_GLSL_MATERIAL = None
"""Materials approximating blender materials with GLSL."""

VSYNC_OFF = None
"""Disables vsync"""

VSYNC_ON = None
"""Enables vsync"""

VSYNC_ADAPTIVE = None
"""Enables adaptive vsync if supported.
                        Adaptive vsync enables vsync if the framerate is above the monitors refresh rate.
                        Otherwise, vsync is diabled if the framerate is too low.
"""

LEFT_EYE = None
"""Left eye being used during stereoscopic rendering."""

RIGHT_EYE = None
"""Right eye being used during stereoscopic rendering."""

RAS_OFS_RENDER_BUFFER = None
"""The pixel buffer for offscreen render is a RenderBuffer. Argument to bge.render.offScreenCreate"""

RAS_OFS_RENDER_TEXTURE = None
"""The pixel buffer for offscreen render is a Texture. Argument to bge.render.offScreenCreate"""


class RASOffScreen:
    """"""

    width = None
    """The width in pixel of the FBO
    
    :type: int
    """

    height = None
    """The height in pixel of the FBO
    
    :type: int
    """

    color = None
    """The underlying OpenGL bind code of the texture object that holds
                                    the rendered image, 0 if the FBO is using RenderBuffer.
                                    The choice between RenderBuffer and Texture is determined
                                    by the target argument of bge.render.offScreenCreate.
    
    :type: int
    """


def getWindowWidth():
    """Gets the width of the window (in pixels)
    
    :rtype: int
    """


def getWindowHeight():
    """Gets the height of the window (in pixels)
    
    :rtype: int
    """


def setWindowSize(width, height):
    """Set the width and height of the window (in pixels). This also works for fullscreen applications.
    <Note> Only works in the standalone player, not the Blender-embedded player.
    
    :param width: width in pixels
    :type width: int
    :param height: height in pixels
    :type height: int
    """


def setFullScreen(enable):
    """Set whether or not the window should be fullscreen.
    <Note> Only works in the standalone player, not the Blender-embedded player.
    
    :param enable: True to set full screen, False to set windowed.
    :type enable: bool
    """


def getFullScreen():
    """Returns whether or not the window is fullscreen.
    <Note> Only works in the standalone player, not the Blender-embedded player; there it always returns False.
    
    :rtype: bool
    """


def getDisplayDimensions():
    """Get the display dimensions, in pixels, of the display (e.g., the
                            monitor). Can return the size of the entire view, so the
                            combination of all monitors; for example, (3840, 1080) for two
                            side-by-side 1080p monitors.
    
    :rtype: tuple (width, height)
    """


def makeScreenshot(filename):
    """Writes an image file with the current displayed frame.
    The image is written to 'filename'.
                            The path may be absolute (eg. /home/foo/image) or relative when started with
                            // (eg. //image). Note that absolute paths are not portable between platforms.
                            If the filename contains a #,
                            it will be replaced by an incremental index so that screenshots can be taken multiple
                            times without overwriting the previous ones (eg. image-#).
    Settings for the image are taken from the render settings (file format and respective settings,
                            gamma and colospace conversion, etc).
                            The image resolution matches the framebuffer, meaning, the window size and aspect ratio.
                            When running from the standalone player, instead of the embedded player, only PNG files are supported.
                            Additional color conversions are also not supported.
    
    :param filename: path and name of the file to write
    :type filename: str
    """


def enableVisibility(visible):
    """Deprecated; doesn't do anything."""


def showMouse(visible):
    """Enables or disables the operating system mouse cursor.
    
    :type visible: bool
    """


def setMousePosition(x, y):
    """Sets the mouse cursor position.
    
    :param x: X-coordinate in screen pixel coordinates.
    :type x: int
    :param y: Y-coordinate in screen pixel coordinates.
    :type y: int
    """


def setBackgroundColor(rgba):
    """Deprecated and no longer functional. Use bge.types.KX_WorldInfo.backgroundColor instead."""


def setEyeSeparation(eyesep):
    """Sets the eye separation for stereo mode. Usually Focal Length/30 provides a confortable value.
    
    :param eyesep: The distance between the left and right eye.
    :type eyesep: float
    """


def getEyeSeparation():
    """Gets the current eye separation for stereo mode.
    
    :rtype: float
    """


def setFocalLength(focallength):
    """Sets the focal length for stereo mode. It uses the current camera focal length as initial value.
    
    :param focallength: The focal length.
    :type focallength: float
    """


def getFocalLength():
    """Gets the current focal length for stereo mode.
    
    :rtype: float
    """


def getStereoEye():
    """Gets the current stereoscopy eye being rendered.
                            This function is mainly used in a bge.types.KX_Scene.pre_draw callback
                            function to customize the camera projection matrices for each
                            stereoscopic eye.
    
    :rtype: LEFT_EYE, RIGHT_EYE
    """


def setMaterialMode(mode):
    """Set the material mode to use for OpenGL rendering.
    <Note> Changes will only affect newly created scenes.
    
    :param mode: material mode
        (type: bge.render.KX_TEXFACE_MATERIAL, bge.render.KX_BLENDER_MULTITEX_MATERIAL, bge.render.KX_BLENDER_GLSL_MATERIAL)
    :type mode: KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL
    """


def getMaterialMode(mode):
    """Get the material mode to use for OpenGL rendering.
    
    :rtype: KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL
    """


def setGLSLMaterialSetting(setting, enable):
    """Enables or disables a GLSL material setting.
    
    :type setting: str (bge.types.KX_Scene.lights, freestyle.shaders, shadows, ramps, bpy.types.NodeTree.nodes, extra_textures)
    :type enable: bool
    """


def getGLSLMaterialSetting(setting):
    """Get the state of a GLSL material setting.
    
    :type setting: str (bge.types.KX_Scene.lights, freestyle.shaders, shadows, ramps, bpy.types.NodeTree.nodes, extra_textures)
    :rtype: bool
    """


def setAnisotropicFiltering(level):
    """Set the anisotropic filtering level for textures.
    <Note> Changing this value can cause all textures to be recreated, which can be slow.
    
    :param level: The new anisotropic filtering level to use
    :type level: integer (must be one of 1, 2, 4, 8, 16)
    """


def getAnisotropicFiltering():
    """Get the anisotropic filtering level used for textures.
    
    :rtype: integer (one of 1, 2, 4, 8, 16)
    """


def setMipmapping(value):
    """Change how to use mipmapping.
    <Note> Changing this value can cause all textures to be recreated, which can be slow.
    """


def getMipmapping():
    """Get the current mipmapping setting.
    
    :rtype: RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR
    """


def drawLine(fromVec, toVec, color):
    """Draw a line in the 3D scene.
    
    :param fromVec: the origin of the line
    :type fromVec: bpy.types.ThemeSpaceListGeneric.list [bge.types.KX_VertexProxy.x, bge.types.KX_VertexProxy.y, bge.types.KX_VertexProxy.z]
    :param toVec: the end of the line
    :type toVec: bpy.types.ThemeSpaceListGeneric.list [bge.types.KX_VertexProxy.x, bge.types.KX_VertexProxy.y, bge.types.KX_VertexProxy.z]
    :param color: the color of the line
    :type color: bpy.types.ThemeSpaceListGeneric.list [bge.types.KX_VertexProxy.r, bge.types.KX_VertexProxy.g, bge.types.KX_VertexProxy.b]
    """


def enableMotionBlur(factor):
    """Enable the motion blur effect.
    
    :param factor: the ammount of motion blur to display.
    :type factor: float [0.0 - 1.0]
    """


def disableMotionBlur():
    """Disable the motion blur effect."""


def showFramerate(enable):
    """Show or hide the framerate.
    
    :type enable: bool
    """


def showProfile(enable):
    """Show or hide the profile.
    
    :type enable: bool
    """


def showProperties(enable):
    """Show or hide the debug properties.
    
    :type enable: bool
    """


def autoDebugList(enable):
    """Enable or disable auto adding debug properties to the debug list.
    
    :type enable: bool
    """


def clearDebugList():
    """Clears the debug property list."""


def setVsync(value):
    """Set the vsync value
    
    :param value: One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE
    :type value: int
    """


def getVsync():
    """Get the current vsync value
    
    :param : (type: One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE)
    :rtype: One
    """


def offScreenCreate(width, height, samples=0, target=RAS_OFS_RENDER_BUFFER):
    """Create a Off-screen render buffer object.
    
    :param width: the width of the buffer in pixels
    :type width: int
    :param height: the height of the buffer in pixels
    :type height: int
    :param samples: the number of multisample for anti-aliasing (MSAA), 0 to disable MSAA
    :type samples: int
    :param target: the pixel storage: bge.render.RAS_OFS_RENDER_BUFFER to render on RenderBuffers (the default),
                                                    bge.render.RAS_OFS_RENDER_TEXTURE to render on texture.
                                                    The later is interesting if you want to access the texture directly (see bge.render.RASOffScreen.color).
                                                    Otherwise the default is preferable as it's more widely supported by GPUs and more efficient.
                                                    If the GPU does not support MSAA+Texture (e.g. Intel HD GPU), MSAA will be disabled.
    :type target: int
    :param : (type: bge.render.RASOffScreen)
    :rtype: RASOffScreen
    """
