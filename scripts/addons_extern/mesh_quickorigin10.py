#
# The MIT License (MIT)
#
# Copyright (c) 2014 ishidourou
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# (参考日本語訳：http://sourceforge.jp/projects/opensource/wiki/licenses%2FMIT_licenseより）
#
# Copyright (c) 2014 ishidourou
#
# 以下に定める条件に従い、本ソフトウェアおよび関連文書のファイル（以下「ソフトウェア」）
# の複製を取得するすべての人に対し、ソフトウェアを無制限に扱うことを無償で許可します。
# これには、ソフトウェアの複製を使用、複写、変更、結合、掲載、頒布、サブライセンス、
# および/または販売する権利、およびソフトウェアを提供する相手に同じことを許可する権利も
# 無制限に含まれます。
#
# 上記の著作権表示および本許諾表示を、ソフトウェアのすべての複製または重要な部分に記載
# するものとします。
#
# ソフトウェアは「現状のまま」で、明示であるか暗黙であるかを問わず、何らの保証もなく
# 提供されます。ここでいう保証とは、商品性、特定の目的への適合性、および権利非侵害に
# ついての保証も含みますが、それに限定されるものではありません。 作者または著作権者は、
# 契約行為、不法行為、またはそれ以外であろうと、ソフトウェアに起因または関連し、あるいは
# ソフトウェアの使用またはその他の扱いによって生じる一切の請求、損害、その他の義務に
# ついて何らの責任も負わないものとします。
#
#####################################
# Quick Origin
#	   v.1.0
#  (c)ishidourou 2014
####################################

bl_info = {
    "name": "Quick Origin",
    "author": "ishidourou",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "View3D > Toolbar and View3D",
    "description": "QuickOrigin",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": 'Mesh'}

import bpy
# import re

from bpy.props import *


class mes():
    title = ('Quick Origin', 'クイックオリジン')
    btn01 = ('Set Origin', '原点を設定')


def lang():
    system = bpy.context.user_preferences.system
    if system.use_international_fonts:
        if system.language == 'ja_JP':
            return 1
    return 0


class QuickOriginPanel(bpy.types.Panel):
    bl_category = "Tools"
    bl_label = mes.title[lang()]
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        self.layout.operator("quick.origin")


class QuickOrigin(bpy.types.Operator):
    bl_idname = "quick.origin"
    bl_label = mes.btn01[lang()]
    bl_options = {'REGISTER'}

    def execute(self, context):
        if bpy.context.mode != 'EDIT_MESH':
            bpy.ops.object.editmode_toggle()
            return{'FINISHED'}
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        return{'FINISHED'}


def register():
    bpy.utils.register_class(QuickOriginPanel)
    bpy.utils.register_class(QuickOrigin)
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        kmmm = kc.keymaps.new(name="Mesh", space_type="EMPTY")
        kmmi1 = kmmm.keymap_items.new('quick.origin', 'O', 'PRESS', alt=True, shift=True)


def unregister():
    bpy.utils.unregister_class(QuickOriginPanel)
    bpy.utils.unregister_class(QuickOrigin)
    if kc:
        km = kc.keymaps["Mesh"]
        for kmi in km.keymap_items:
            if kmi.idname == 'quick.origin':
                km.keymap_items.remove(kmi)

if __name__ == "__main__":
    register()
