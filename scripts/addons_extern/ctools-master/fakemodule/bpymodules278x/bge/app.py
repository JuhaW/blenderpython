version = None
"""The Blender/BGE version as a tuple of 3 ints, eg. (2, 75, 1).
(type: tuple of three ints)

:type: tuple
"""

version_string = ""
"""The Blender/BGE version formatted as a string, eg. "2.75 (sub 1)".

:type: str
"""

version_char = ""
"""The Blender/BGE version character (for minor releases).

:type: str
"""

has_texture_ffmpeg = None
"""True if the BGE has been built with FFmpeg support,
                    enabling use of bge.texture.ImageFFmpeg and bge.texture.VideoFFmpeg.

:type: bool
"""

has_joystick = None
"""True if the BGE has been built with joystick support.

:type: bool
"""

has_physics = None
"""True if the BGE has been built with physics support.

:type: bool
"""
