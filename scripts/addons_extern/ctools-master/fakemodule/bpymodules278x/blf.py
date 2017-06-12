def aspect(fontid, aspect):
    """Set the aspect for drawing text.
    
    :param fontid: The id of the typeface as returned by blf.load, for default font use 0.
    :type fontid: int
    :param aspect: The aspect ratio for text drawing to use.
    :type aspect: float
    """


def blur(fontid, radius):
    """Set the blur radius for drawing text.
    
    :param fontid: The id of the typeface as returned by blf.load, for default font use 0.
    :type fontid: int
    :param radius: The radius for blurring text (in pixels).
    :type radius: int
    """


def clipping(fontid, xmin, ymin, xmax, ymax):
    """Set the clipping, enable/disable using CLIPPING.
    
    :param fontid: The id of the typeface as returned by blf.load, for default font use 0.
    :type fontid: int
    :param xmin: Clip the drawing area by these bounds.
    :type xmin: float
    :param ymin: Clip the drawing area by these bounds.
    :type ymin: float
    :param xmax: Clip the drawing area by these bounds.
    :type xmax: float
    :param ymax: Clip the drawing area by these bounds.
    :type ymax: float
    """


def dimensions(fontid, text):
    """Return the width and height of the text.
    
    :param fontid: The id of the typeface as returned by blf.load, for default font use 0.
    :type fontid: int
    :param text: the text to draw.
    :type text: str
    :return: the width and height of the text.
    :param : (type: tuple of 2 floats)
    :rtype: tuple
    """


def disable(fontid, option):
    """Disable option.
    
    :param fontid: The id of the typeface as returned by blf.load, for default font use 0.
    :type fontid: int
    :param option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT.
    :type option: int
    """


def draw(fontid, text):
    """Draw text in the current context.
    
    :param fontid: The id of the typeface as returned by blf.load, for default font use 0.
    :type fontid: int
    :param text: the text to draw.
    :type text: str
    """


def enable(fontid, option):
    """Enable option.
    
    :param fontid: The id of the typeface as returned by blf.load, for default font use 0.
    :type fontid: int
    :param option: One of ROTATION, CLIPPING, SHADOW or KERNING_DEFAULT.
    :type option: int
    """


def load(filename):
    """Load a new font.
    
    :param filename: the filename of the font.
    :type filename: str
    :return: the new font's fontid or -1 if there was an error.
    :rtype: int
    """


def position(fontid, x, y, z):
    """Set the position for drawing text.
    
    :param fontid: The id of the typeface as returned by blf.load, for default font use 0.
    :type fontid: int
    :param x: X axis position to draw the text.
    :type x: float
    :param y: Y axis position to draw the text.
    :type y: float
    :param z: Z axis position to draw the text.
    :type z: float
    """


def rotation(fontid, angle):
    """Set the text rotation angle, enable/disable using ROTATION.
    
    :param fontid: The id of the typeface as returned by blf.load, for default font use 0.
    :type fontid: int
    :param angle: The angle for text drawing to use.
    :type angle: float
    """


def shadow(fontid, level, r, g, b, a):
    """Shadow options, enable/disable using SHADOW .
    
    :param fontid: The id of the typeface as returned by blf.load, for default font use 0.
    :type fontid: int
    :param level: The blur level, can be 3, 5 or 0.
    :type level: int
    :param r: Shadow color (red channel 0.0 - 1.0).
    :type r: float
    :param g: Shadow color (green channel 0.0 - 1.0).
    :type g: float
    :param b: Shadow color (blue channel 0.0 - 1.0).
    :type b: float
    :param a: Shadow color (alpha channel 0.0 - 1.0).
    :type a: float
    """


def shadow_offset(fontid, x, y):
    """Set the offset for shadow text.
    
    :param fontid: The id of the typeface as returned by blf.load, for default font use 0.
    :type fontid: int
    :param x: Vertical shadow offset value in pixels.
    :type x: float
    :param y: Horizontal shadow offset value in pixels.
    :type y: float
    """


def size(fontid, size, dpi):
    """Set the size and dpi for drawing text.
    
    :param fontid: The id of the typeface as returned by blf.load, for default font use 0.
    :type fontid: int
    :param size: Point size of the font.
    :type size: int
    :param dpi: dots per inch value to use for drawing.
    :type dpi: int
    """


def unload(filename):
    """Unload an existing font.
    
    :param filename: the filename of the font.
    :type filename: str
    """


def word_wrap(fontid, wrap_width):
    """Set the wrap width, enable/disable using WORD_WRAP.
    
    :param fontid: The id of the typeface as returned by blf.load, for default font use 0.
    :type fontid: int
    :param wrap_width: The width (in pixels) to wrap words at.
    :type wrap_width: int
    """


CLIPPING = 2
""":type: int"""

KERNING_DEFAULT = 8
""":type: int"""

ROTATION = 1
""":type: int"""

SHADOW = 4
""":type: int"""

WORD_WRAP = 128
""":type: int"""
