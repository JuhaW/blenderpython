def new(width, height, samples=0):
    """Return a GPUOffScreen.
    
    :param width: Horizontal dimension of the buffer.
    :type width: int`
    :param height: Vertical dimension of the buffer.
    :type height: int`
    :param samples: OpenGL samples to use for MSAA or zero to disable.
    :type samples: int
    :return: Newly created off-screen buffer.
    :rtype: gpu.GPUOffscreen
    """


class GPUOffscreen:
    """This object gives access to off screen buffers."""

    def bind(self, save=True):
        """Bind the offscreen object.
        
        :param save: save OpenGL current states.
        :type save: bool
        """

    def draw_view3d(self, scene, view3d, region, modelview_matrix, projection_matrix):
        """Draw the 3d viewport in the offscreen object.
        
        :param scene: Scene to draw.
        :type scene: bpy.types.Scene
        :param view3d: 3D View to get the drawing settings from.
        :type view3d: bpy.types.SpaceView3D
        :param region: Region of the 3D View.
        :type region: bpy.types.Region
        :param modelview_matrix: ModelView Matrix.
        :type modelview_matrix: mathutils.Matrix
        :param projection_matrix: Projection Matrix.
        :type projection_matrix: mathutils.Matrix
        """

    def free(self):
        """Free the offscreen object
                                    The framebuffer, texture and render objects will no longer be accessible.
        """

    def unbind(self, restore=True):
        """Unbind the offscreen object.
        
        :param restore: restore OpenGL previous states.
        :type restore: bool
        """

    color_texture = None
    """Color texture.
    
    :type: int
    """

    height = None
    """Texture height.
    
    :type: int
    """

    width = None
    """Texture width.
    
    :type: int
    """
