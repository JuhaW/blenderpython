'''
BEGIN GPL LICENSE BLOCK

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

END GPL LICENCE BLOCK
'''

#bl_info = {  
# "name": "Perpendicular Bisector",  
# "author": "Diego Quevedo ( http://doshape.com/ )",  
# "version": (1, 0),  
# "blender": (2, 7 , 3),  
# "location": "View3D > EditMode > ToolShelf",  
# "description": "allow create a line bisector that always crosses the line segment at right angles (90°).only work with 3 vertex selected",  
# "warning": "",  
# "wiki_url": "",  
# "tracker_url": "",  
# "category": "Mesh"} 

import bpy
import bmesh
import math

        
class perpendicularBisectorOperator(bpy.types.Operator):
    "divide a 90 grados"
    bl_idname = 'mesh.perpbisector'
    bl_label = 'Perpendicular Bisector'
    bl_description  = "allow create a line bisector that always crosses the line segment at right angles (90°)."
    bl_options = {'REGISTER', 'UNDO'}
    
    Vertices = bpy.props.EnumProperty(attr='nameless', items=(
            ('1', 'Vert 1', 'The first vert'),
            ('2', 'Vert 2', 'The second vert'),
            ('3', 'Vert 3', 'The third vert')), default='1')

    def main(self, context, Vertices):
        
        obj = bpy.context.object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        
              
         
        vertices = [v for v in bm.verts if (v.select and not v.hide)]
        
        if not len(vertices) == 3:
            msg = "select ONLY 3 vertices"
            self.report({"WARNING"}, msg)
            return {'CANCELLED'}  
        
        
        v1,v2,v3 = [v for v in vertices]
        
        visible_geom = [g for g in bm.faces[:]
            + bm.verts[:] + bm.edges[:] if not g.hide]

        if Vertices == '1':
            verticeje = v1.co
            plane_no = v2.co - v3.co
            plane_co = verticeje
            print('cordenadas plano:\n', plane_no, '\n', plane_co)
            dist = 0.0001

            # hidden geometry will not be affected.
            bmesh.ops.bisect_plane(
                bm,
                geom=visible_geom,
                dist=dist,
                plane_co=plane_co, plane_no=plane_no,
                use_snap_center=False,
                clear_outer=False,
                clear_inner=False)
        elif Vertices == '2': 
            verticeje = v2.co
            plane_no = v1.co - v3.co
            plane_co = verticeje
            print('cordenadas plano:\n', plane_no, '\n', plane_co)
            dist = 0.0001

            # hidden geometry will not be affected.
            bmesh.ops.bisect_plane(
                bm,
                geom=visible_geom,
                dist=dist,
                plane_co=plane_co, plane_no=plane_no,
                use_snap_center=False,
                clear_outer=False,
                clear_inner=False)
        elif Vertices == '3': 
            verticeje = v3.co
            plane_no = v1.co - v2.co
            plane_co = verticeje
            print('cordenadas plano:\n', plane_no, '\n', plane_co)
            dist = 0.0001

            # hidden geometry will not be affected.
            bmesh.ops.bisect_plane(
                bm,
                geom=visible_geom,
                dist=dist,
                plane_co=plane_co, plane_no=plane_no,
                use_snap_center=False,
                clear_outer=False,
                clear_inner=False)
        else:
            print("Select 1 option")
    
    
    
        bmesh.update_edit_mesh(me, True)   
    
    
    @classmethod
    def poll(self, context):
        obj = context.active_object
        return all([obj is not None, obj.type == 'MESH', obj.mode == 'EDIT'])

    def execute(self, context):
        
        self.main(context, self.Vertices)
        #bisectoroperator(self)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)          
                 
    
"""
class perpendicularBisectorOperatorPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    #bl_context = "editmode"
    bl_label = "Perpendicular bisector"
    @classmethod
    def poll(cls, context):
        return (context.mode == 'EDIT_MESH')
    
    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator(perpendicularBisectorOperator.bl_idname) 
"""        
    

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()