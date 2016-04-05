Archimesh
=======

Blender add-on for creating architecture elements.

- Rooms
- Houses
- Columns
- Stairs
- Doors
- Windows
- Tile roofs
- Kitchen cabinets
- Japanese curtains
- Roller curtains
- Venetian blind
- Books
- Lamps

You can get more information in: https://www.youtube.com/playlist?list=PLQAfj95MdhTJ7zifNb5ab-n-TI0GmKwWQ

Changes in version 0.6
=============================
Kitchen cabinets

Changes in version 0.7
=============================
- Shelves
- Windows
- Japanese curtains
- Roller curtains
- Venetian blind
- Books
- Lamps

The source code has been reorganized and some parameters have been moved from init.py

Changes in version 0.7.1
=============================
- Fixed error wih invisible walls in UV unwrap

Changes in version 0.8
=============================
- Rooms now are editable after creation
- Support of Curved walls
- Import and Export rooms
- New "Auto Hole" function for Windows and Doors
- New Kitchen inventory
- New Tools panel
- Rooms UI adapted to new features
- UI adapted to new Blender tabs
- Source reorganization and minor bug fixing

Changes in version 0.8.1
=============================
- Fixed error in "Close Walls" parameter if the last walls was defined as "Advanced".


Changes in version 1.0.0
=============================
(The version 0.9 was an internal release and it was not published)


- New Grease Pencil tool for creating rooms.
- The kitchen cabinets can be rotated.
- More options for kitchen countertop.
- The doors can be rotated during creation.
- The windows can be rotated during creation.
- Improved boolean operator for autohole function.
- Fixed error using languages different of English.
- Small bug fixing.

Changes in version 1.0.1
=============================
- Fix problem installing addon in previous versions (< 2.71)

Changes in version 1.0.2
=============================
- Fixed error importing rooms created with grease pencil. This fix required to re-export the room.

Changes in version 1.1.0
=============================
- NEW: Display measures for Walls (wall number too), Doors and Windows. Now it's easier to create exact measures.
- NEW: Doors are now editable after creation.
- NEW: Windows are now editable after creation.
- NEW: Venetian curtains are now editable after creation.
- NEW: Integrated Window generator script. Now it's possible to create different windows shapes.
- NEW: Now it's possible to create wall covers with boards automatically for creating external walls.
- Changed UI for using color picker for venetians, lamps and books.
- Improved Room Import/Export process.
- Autohole controllers are now visible for improving usability.
- Changed glass material for avoiding wrong reflections.
- Some code has been renamed for improving code maintenance.
- All python code has been reformatted for PEP8 syntax.
- Minor UI changes.
- Minor bug fixing.
 
V1.1 video: http://youtu.be/fxIoDvJHl3Q

Changes in version 1.1.1
=============================
- Fixed error with OSX.
- Fixed incompatibility with windows generator install on same PC.
- Some minor fix.

This release contains changes in how the meshes are created due a change in Blender. Clear the archimesh folder before install new version.
