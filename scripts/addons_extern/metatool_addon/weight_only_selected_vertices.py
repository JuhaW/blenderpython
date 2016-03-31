#
#The MIT License (MIT)
#
#Copyright (c) 2014 ishidourou
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
#
#(参考日本語訳：http://sourceforge.jp/projects/opensource/wiki/licenses%2FMIT_licenseより）
#
#Copyright (c) 2014 ishidourou
#
#以下に定める条件に従い、本ソフトウェアおよび関連文書のファイル（以下「ソフトウェア」）
#の複製を取得するすべての人に対し、ソフトウェアを無制限に扱うことを無償で許可します。
#これには、ソフトウェアの複製を使用、複写、変更、結合、掲載、頒布、サブライセンス、
#および/または販売する権利、およびソフトウェアを提供する相手に同じことを許可する権利も
#無制限に含まれます。
#
#上記の著作権表示および本許諾表示を、ソフトウェアのすべての複製または重要な部分に記載
#するものとします。
#
#ソフトウェアは「現状のまま」で、明示であるか暗黙であるかを問わず、何らの保証もなく
#提供されます。ここでいう保証とは、商品性、特定の目的への適合性、および権利非侵害に
#ついての保証も含みますが、それに限定されるものではありません。 作者または著作権者は、
#契約行為、不法行為、またはそれ以外であろうと、ソフトウェアに起因または関連し、あるいは
#ソフトウェアの使用またはその他の扱いによって生じる一切の請求、損害、その他の義務に
#ついて何らの責任も負わないものとします。
#

######################################
#  Set Weight Only Selected Vertices 
#        (English/Japanese)
#               v.0.53
#       (c)ishidourou 2014
#####################################

import bpy
from bpy.props import *

#bl_info = {
#    "name": "Set Weight Only Selected Vertices",
#    "author": "ishidourou",
#    "version": (0, 53),
#    "blender": (2, 65, 0),
#    "location": "Mesh>PROPERTIES",
#    "description": "Set Weight Only Selected Vertices",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": 'Mesh'}

#    メッセージ（英語,日本語）
class mes():
    title = ('Set Weight Only Selected Vertices','ウエイトを選択頂点だけに設定')
    label = ('to Selected Vertex Group:','選択中の頂点グループに対して:')
    label2 = ('to All Vertex Groups:','すべての頂点グループに対して:')
    btn01 = ('Set Weight','ウエイトを設定')
    btn02 = ('Del All','すべて削除')
    btn03 = ('Del Others','選択外削除')

def lang():
    system = bpy.context.user_preferences.system
    if system.use_international_fonts:
        if system.language == 'ja_JP':
            return 1
    return 0

"""
class AosPanel(bpy.types.Panel):
    bl_label = mes.title[lang()]
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"

    def draw(self , context):
        ob = context.object
        
        if ob.vertex_groups and (ob.mode == 'EDIT' or (ob.mode == 'WEIGHT_PAINT' and ob.type == 'MESH')):
            layout = self.layout
            col = layout.column(align=True)
            col.label(text=mes.label[lang()])
            row = col.row(align=True)
            row.operator("assignonly.selected",text=mes.btn01[lang()])
            row.operator("del.unselected",text=mes.btn03[lang()])
            row.operator("remall.vertex",text=mes.btn02[lang()])
            col = layout.column(align=True)
            col.label(text=mes.label2[lang()])
            row = col.row(align=True)
            row.operator("all_assignonly.selected",text=mes.btn01[lang()])
            row.operator("all_del.unselected",text=mes.btn03[lang()])
            row.operator("all_remall.vertex",text=mes.btn02[lang()])
"""

def assign_only_selected(mode):
    cobj = bpy.context.object
    vg = cobj.vertex_groups
    avg = vg.active
    if avg.lock_weight:
        return -1
    mmode = cobj.mode
    if mmode != 'EDIT':
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()
        return 0

    if mode == 'ASSIGN':
        bpy.ops.object.vertex_group_assign()
    elif mode == 'REMOVE':
        bpy.ops.object.vertex_group_remove_from()
    bpy.ops.mesh.select_all(action='INVERT')
    bpy.ops.object.vertex_group_remove_from()
    bpy.ops.mesh.select_all(action='INVERT')
    
    bpy.ops.object.mode_set(mode='WEIGHT_PAINT')  

def all_assign_only_selected(mode):
    cobj = bpy.context.object
    vg = cobj.vertex_groups
    avg = vg.active
    mmode = cobj.mode

    if mmode != 'EDIT':
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()
        return 0

    ct = 0
    for i in vg:
        vg.active_index = ct
        if not i.lock_weight:
            if mode == 'ASSIGN' or mode == 'DELOTHER':
                if i == avg:
                    if mode == 'ASSIGN':
                        bpy.ops.object.vertex_group_assign()
                    bpy.ops.mesh.select_all(action='INVERT')
                    bpy.ops.object.vertex_group_remove_from()
                    bpy.ops.mesh.select_all(action='INVERT')
                else:
                    bpy.ops.object.vertex_group_remove_from()                
            else:
                bpy.ops.object.vertex_group_remove_from()
                bpy.ops.mesh.select_all(action='INVERT')
                bpy.ops.object.vertex_group_remove_from()
                bpy.ops.mesh.select_all(action='INVERT')
        ct += 1
    bpy.ops.object.mode_set(mode='WEIGHT_PAINT')  

class AssignOnlySelected(bpy.types.Operator):
    bl_idname = "assignonly.selected"
    bl_label = mes.btn01[lang()]
    bl_options = {'REGISTER','UNDO'}
 
    def execute(self, context):
        assign_only_selected('ASSIGN')
        return{'FINISHED'}

class DelUnselected(bpy.types.Operator):
    bl_idname = "del.unselected"
    bl_label = mes.btn03[lang()]
    bl_options = {'REGISTER','UNDO'}
 
    def execute(self, context):
        assign_only_selected('DELOTHER')
        return{'FINISHED'}

class RemAllVertex(bpy.types.Operator):
    bl_idname = "remall.vertex"
    bl_label = mes.btn02[lang()]
    bl_options = {'REGISTER','UNDO'}
 
    def execute(self, context):
        assign_only_selected('REMOVE')
        return{'FINISHED'}

class AllAssignOnlySelected(bpy.types.Operator):
    bl_idname = "all_assignonly.selected"
    bl_label = mes.btn01[lang()]
    bl_options = {'REGISTER','UNDO'}
 
    def execute(self, context):
        all_assign_only_selected('ASSIGN')
        return{'FINISHED'}

class AlldelUnelected(bpy.types.Operator):
    bl_idname = "all_del.unselected"
    bl_label = mes.btn03[lang()]
    bl_options = {'REGISTER','UNDO'}
 
    def execute(self, context):
        all_assign_only_selected('DELOTHER')
        return{'FINISHED'}

class AllRemAllVertex(bpy.types.Operator):
    bl_idname = "all_remall.vertex"
    bl_label = mes.btn02[lang()]
    bl_options = {'REGISTER','UNDO'}
 
    def execute(self, context):
        all_assign_only_selected('REMOVE')
        return{'FINISHED'}

def register():
    #bpy.utils.register_class(AosPanel)
    bpy.utils.register_class(RemAllVertex)
    bpy.utils.register_class(AssignOnlySelected)
    bpy.utils.register_class(AllRemAllVertex)
    bpy.utils.register_class(AllAssignOnlySelected)
    bpy.utils.register_class(DelUnselected)
    bpy.utils.register_class(AlldelUnelected)

def unregister():
    #bpy.utils.unregister_class(AosPanel)
    bpy.utils.unregister_class(RemAllVertex)
    bpy.utils.unregister_class(AssignOnlySelected)
    bpy.utils.unregister_class(AllRemAllVertex)
    bpy.utils.unregister_class(AllAssignOnlySelected)
    bpy.utils.unregister_class(DelUnselected)
    bpy.utils.unregister_class(AlldelUnelected)

if __name__ == "__main__":
    register()



