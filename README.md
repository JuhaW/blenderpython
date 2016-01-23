blenderpython
=============

My collection of Blender Addons

Installation 
============

* Download recent Blender Build from here: https://builder.blender.org/download/
* This repo is kept mostly uptodate with recent Builds.
* Currently Blender 2.75b is supported also & would represent a minimum requirement for all features.

* Download the blenderpython zip file & unpack.
* Copy the "scripts" folder or it's contents & paste over the Blender "scripts" folder on your os or to the buildbot build "scripts" folder.
* This will replace addons_utils.py in modules to activate the addons extern folder.

Optional Config Folder 
=======================

* I reccommend for all d/l zip builds & custom builds you make yourself to add the secret config folder.
* After downloading a build from buildbot:
* Create the config folder here: 'blender_version'/2.75/config
* The config folder makes the build save the user preferences & user settings into that folder & bypasses appdata, which is used by Blender Installers.
* By keeping your modified build seperate from blender, there's little chance of anything going wrong with your install.

Addons Extern Folder
====================
* you need patched addons_utils.py to use this folder. see note.

* addons_extern is a very useful folder, once set up, you can drop any addon in there & it's recognized.
* This allows you to delete any scripts you don't need & repopulate with ones you like at any time.
* The added benifit of this is there's no need to mix in your favorite external addons into blenders addons folders, 
then have to find & replace for each new Blender version.
* 
 
* The addons_extern folder I use contains many working addons I've collected over the years.
* Currently the addons_extern is reasonably up to date for blender 2.75b.
* However, I cannot guarentee every addon will be up to date at any given time.
* Please check original authors site/s for updates.
* The flip side of this is there's many addons here that are not working elsewhere...

Note: 
====================
* addons_extern should be placed next to addons & addons contrib in "blender version"\2.75\scripts
* some addons in the repo are hard coded to addons_extern folder

* Update the addons_utils.py to activate addons_extern folder & paste into new blender scripts directory & your favorites are right there.
* addons_utils.py is found in the modules folder eg: \2.76\scripts\modules.

Note 2:
=====================

Duplicate addons may occur as the collection is very large, just delete any duplicates you don't need.

Editing/Updating:
=====================

* Some "in their own folder" addons may have hard coded path to addons folder. 
* open the __init__.py file for the addon & shortly below the addon information there will be text with path & addons in it.
* change addons to addons_extern to make work in external folder.

Windows Pre built version for 2.75a: http://www.graphicall.org/1155
===================

Known Issues:
===================
* Addons Factory script is huge, it may take a few seconds to load. 

Disclaimer:
==================
* Be careful using addons, some addons may cause crashes if used in wrong context or using huge amounts of verts.

* I'm not responsible for any lost effort or broken addons. Save Often.

* Use at Own Risk!

Enjoy
=======
* All of this works very well for me & should do so also for you.


Help Wanted
===========

Feel free to drop into irc #blenderpython if you have any question about this repo & especially if you would like to help & contribute.
Thanks.