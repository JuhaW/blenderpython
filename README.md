blenderpython
=============

My collection of Blender Addons

[Prebuilt collection for Windows x86_64 (Blender 2.75a)](http://www.graphicall.org/1155)
--

Requirements
--
* Blender 2.76+ build from [buildbot](https://builder.blender.org/download/).
* blenderpython zip, unpacked.
* Included in this repo: addon_utils.py, [space_view3d.py](https://developer.blender.org/T46853)
* Optional: Blender's [config folders](https://www.blender.org/manual/getting_started/installing/configuration/directories.html) to keep a special Blender config for addons_extern.

addons_extern
--
* addons_extern should be placed next to addons & addons contrib in `$BLENDER_ROOT\2.76\scripts`
* Using addons_extern, there is no need to mix external addons with Blender's bundled addons. Upgrading requires less filtering and easier maintenance.
* Addons are kept reasonably up-to-date. Check the author's source for the most recent updates.
* addons_extern often serves as a home for abandoned addons, with fixes for later versions of blender. Please submit a report or a pull request to submit updates.

Note:
--
* Use at your own risk!
* Some addons are hard coded to addons_extern folder. Open the \__init__.py file for the addon & shortly below the addon information there will be text with path & addons in it.
* Be careful using addons_extern! Some addons work on high volumes of data, resulting in slow calculations and higher potential to crash.
* Addons Factory script is huge, it may take a few seconds to load.
* Save Often. I'm not responsible for any lost effort or broken addons.

Help Wanted
--
Have questions or would like to contribute? Drop into [irc](https://webchat.freenode.net/) #blenderpython and let us know.

Thanks.
