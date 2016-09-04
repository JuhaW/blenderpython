blenderpython
==

ita_tools
--
This collection is pruned and more suited specifically for animators, riggers and Python devs. These are tools *I* find useful in my work. *master* branch is more general and periodically synced with meta-androcto's repo.

Requirements
--
* Blender 2.76+ build from [buildbot](https://builder.blender.org/download/).
* blenderpython zip, unpacked.
* Included in this repo: addon_utils.py, [space_view3d.py](https://developer.blender.org/T46853)
* Optional: Use Blender's [config folders](https://www.blender.org/manual/getting_started/installing/configuration/directories.html) to keep a special config for addons_extern.

addons_extern
--
* Using addons_extern, there is no need to mix external addons with Blender's bundled addons. Upgrading requires less filtering and easier maintenance.
* addons_extern often serves as a home for abandoned addons, with fixes for later versions of blender.
* addons_extern should be placed next to addons & addons contrib in `$BLENDER_ROOT\2.76\scripts`

Note:
--
* Use at your own risk!
* Some addons are hard coded to addons_extern folder.
* Open the \__init__.py file for the addon & shortly below the addon information there will be text with path & addons in it.
* Be careful using addons_extern! Some addons work on large amounts of data, resulting in slow calculations and higher potential to crash.
* Save Often. I'm not responsible for any lost effort or broken addons.
