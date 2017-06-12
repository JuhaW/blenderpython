autoexec_fail = False
"""Undocumented"""

autoexec_fail_message = ""
"""Undocumented"""

autoexec_fail_quiet = False
"""Undocumented"""

binary_path_python = "/usr/bin/python3.6m"
"""String, the path to the python executable (read-only)"""

debug = False
"""Boolean, for debug info (started with --debug / --debug_* matching this attribute name)"""

debug_depsgraph = False
"""Boolean, for debug info (started with --debug / --debug_* matching this attribute name)"""

debug_events = False
"""Boolean, for debug info (started with --debug / --debug_* matching this attribute name)"""

debug_ffmpeg = False
"""Boolean, for debug info (started with --debug / --debug_* matching this attribute name)"""

debug_freestyle = False
"""Boolean, for debug info (started with --debug / --debug_* matching this attribute name)"""

debug_gpumem = False
"""Boolean, for debug info (started with --debug / --debug_* matching this attribute name)"""

debug_handlers = False
"""Boolean, for debug info (started with --debug / --debug_* matching this attribute name)"""

debug_python = False
"""Boolean, for debug info (started with --debug / --debug_* matching this attribute name)"""

debug_simdata = False
"""Boolean, for debug info (started with --debug / --debug_* matching this attribute name)"""

debug_value = 0
"""Int, number which can be set to non-zero values for testing purposes"""

debug_wm = False
"""Boolean, for debug info (started with --debug / --debug_* matching this attribute name)"""

driver_namespace = None
"""Dictionary for drivers namespace, editable in-place, reset on file load (read-only)"""

render_icon_size = 32
"""Reference size for icon/preview renders (read-only)"""

render_preview_size = 128
"""Reference size for icon/preview renders (read-only)"""

tempdir = "/home/hoge/tmp/blender_I2wNgP/"
"""String, the temp directory used by blender (read-only)"""

background = True
"""Boolean, True when blender is running without a user interface (started with -b)"""

translations = None
"""Application and addons internationalization API"""

build_branch = b'base'
"""The branch this blender instance was built from"""

build_cflags = b' -Wall -Wcast-align -Werror=implicit-function-declaration -Werror=return-type -Werror=vla -Wstrict-prototypes -Wmissing-prototypes -Wno-char-subscripts -Wno-unknown-pragmas -Wpointer-arith -Wunused-parameter -Wwrite-strings -Wlogical-op -Wundef -Winit-self -Wnonnull -Wmissing-include-dirs -Wno-div-by-zero -Wtype-limits -Wformat-signedness -Wuninitialized -Wredundant-decls -Wshadow -Wno-error=unused-but-set-variable -fPIC -pipe -DGHOST_OPENGL_STENCIL -DGHOST_OPENGL_ALPHA -fuse-ld=gold -fopenmp -std=gnu11   -msse -pipe -fPIC -funsigned-char -fno-strict-aliasing -msse2'
"""C compiler flags"""

build_commit_date = b'2017-04-09'
"""The date of commit this blender instance was built"""

build_commit_time = b'04:26'
"""The time of commit this blender instance was built"""

build_cxxflags = b' -Wredundant-decls -Wall -Wno-invalid-offsetof -Wno-sign-compare -Wlogical-op -Winit-self -Wmissing-include-dirs -Wno-div-by-zero -Wtype-limits -Werror=return-type -Werror=implicit-function-declaration -Wno-char-subscripts -Wno-unknown-pragmas -Wpointer-arith -Wunused-parameter -Wwrite-strings -Wundef -Wformat-signedness -Wuninitialized -Wundef -Wmissing-declarations -fPIC -pipe -DGHOST_OPENGL_STENCIL -DGHOST_OPENGL_ALPHA -fuse-ld=gold -fopenmp -std=c++11   -msse -pipe -fPIC -funsigned-char -fno-strict-aliasing -msse2'
"""C++ compiler flags"""

build_date = b'2017-04-09'
"""The date this blender instance was built"""

build_hash = b'd988d612a51'
"""The commit hash this blender instance was built with"""

build_linkflags = b" -Wl,--version-script='/home/hoge/bf/blender/source/creator/blender.map'"
"""Binary linking flags"""

build_platform = b'Linux'
"""The platform this blender instance was built for"""

build_system = b'CMake'
"""Build system used"""

build_time = b'18:17:49'
"""The time this blender instance was built"""

build_type = b'Debug'
"""The type of build (Release, Debug)"""

build_commit_timestamp = 1491712004
"""The unix timestamp of commit this blender instance was built"""

binary_path = "/usr/local/opt/blender/bin/blender"
"""The location of blenders executable, useful for utilities that spawn new instances"""

version_char = ""
"""The Blender version character (for minor releases)"""

version_cycle = "alpha"
"""The release status of this build alpha/beta/rc/release"""

version_string = "2.78 (sub 4)"
"""The Blender version formatted as a string"""

version = (2, 78, 4)
"""The Blender version as a tuple of 3 numbers. eg. (2, 50, 11)"""

alembic = None
"""constant value bpy.app.alembic(supported=False, version=(0, 0, 0), version_string='Unknown')"""

build_options = None
"""constant value bpy.app.build_options(bullet=True, codec_avi=True, codec_ffmpeg=True, codec_quicktime=False, codec_sndfile=False, compositor=True, cycles=True, cycles_osl=True, freestyle=True, gameengine=True, image_cineon=True, image_dds=True, image_frameserver=True, image_hdr=True, image_openexr=True, image_openjpeg=True, image_tiff=True, input_ndof=True, audaspace=True, international=True, openal=True, sdl=False, sdl_dynload=False, jack=False, libmv=True, mod_boolean=True, mod_fluid=True, mod_oceansim=True, ...)"""

ffmpeg = None
"""constant value bpy.app.ffmpeg(supported=True, avcodec_version=(57, 64, 101), avcodec_version_string='57, 64, 101', avdevice_version=(57, 1, 100), avdevice_version_string='57,  1, 100', avformat_version=(57, 56, 101), avformat_version_string='57, 56, 101', avutil_version=(55, 34, 101), avutil_version_string='55, 34, 101', swscale_version=(4, 2, 100), swscale_version_string=' 4,  2, 100')"""

handlers = None
"""constant value bpy.app.handlers(frame_change_pre=[], frame_change_post=[], render_pre=[], render_post=[], render_write=[], render_stats=[], render_init=[], render_complete=[], render_cancel=[], load_pre=[], load_post=[], save_pre=[], save_post=[], scene_update_pre=[], scene_update_post=[], game_pre=[], game_post=[], version_update=[], persistent=<class 'persistent'>)"""

ocio = None
"""constant value bpy.app.ocio(supported=True, version=(1, 0, 9), version_string=' 1,  0,  9')"""

oiio = None
"""constant value bpy.app.oiio(supported=True, version=(1, 7, 13), version_string=' 1,  7, 13')"""

openvdb = None
"""constant value bpy.app.openvdb(supported=True, version=(3, 2, 0), version_string=' 3,  2,  0')"""

sdl = None
"""constant value bpy.app.sdl(supported=False, version=(0, 0, 0), version_string='Unknown', available=False)"""
