import bpy
import math

bl_info = {
    "name": "AmasawaTools",
    "description": "",
    "author": "AmasawaRasen",
    "version": (0, 5, 0),
    "blender": (2, 7, 2),
    "location": "View3D > Toolbar",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"}

#パスを作る関数
def make_Path(verts):
    bpy.ops.curve.primitive_nurbs_path_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False))
    for i,point in enumerate(bpy.context.scene.objects.active.data.splines[0].points):
        point.co = verts[i]
        
#NURBS円を作る関数
def make_circle(verts):
    bpy.ops.curve.primitive_nurbs_circle_add(radius=0.1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False))
    for i,point in enumerate(bpy.context.scene.objects.active.data.splines[0].points):
        point.co = verts[i]
        
#Bevel用のカーブを作成する
#verts : 頂点配列
#loopFlag : ループするかしないか
#order_uValue : 次数
#resulution_uValue : 解像度
#splineType : NURBS・ベジエ・多角形などのスプラインのタイプ
def make_bevelCurve(verts, loopFlag, order_uValue, resolution_uValue,splineType='NURBS'):
    bpy.ops.curve.primitive_nurbs_circle_add(radius=0.1, view_align=False,
    enter_editmode=False, location=(0, 0, 0), layers=(False, False, False,
    False, False, False, False, False, False, False, False, False, False,
    False, False, False, False, False, True, False))
    curve = bpy.context.scene.objects.active
    #頂点をすべて消す
    curve.data.splines.clear()
    newSpline = curve.data.splines.new(type='NURBS')
    #頂点を追加していく
    newSpline.points.add(len(verts)-1)
    for vert,newPoint in zip(verts,newSpline.points):
        newPoint.co = vert
    #ループにする
    newSpline.use_cyclic_u = loopFlag
    #次数を2にする
    newSpline.order_u = order_uValue
    #解像度を1にする
    newSpline.resolution_u = resolution_uValue
    newSpline.use_endpoint_u = True
    #スプラインのタイプを設定
    newSpline.type = splineType

#オペレータークラス
#オブジェクトの辺をアニメ風の髪に変換
#カーブの再変換もできる
class AnimeHairOperator(bpy.types.Operator):
    bl_idname = "object.animehair"
    bl_label = "AnimeHair"
    bl_options = {'REGISTER','UNDO'}
    bl_description = "メッシュの辺をアニメ風の髪の毛に変換"

    my_int_bevelType = bpy.props.IntProperty(name="BevelType",min=0,max=13)
    my_int_taparType = bpy.props.IntProperty(name="TaperType",min=0,max=7)
    my_float_x = bpy.props.FloatProperty(name="X",default=1.0,min=0.0)
    my_float_y = bpy.props.FloatProperty(name="Y",default=1.0,min=0.0)
    my_float_weight = bpy.props.FloatProperty(name="SoftBody Goal",default=0.3,min=0.0,max=1.0)
    my_float_mass = bpy.props.FloatProperty(name="SoftBody Mass",default=0.3,min=0.0,)
    my_float_goal_friction = bpy.props.FloatProperty(name="SoftBody Friction",default=5.0,min=0.0)

    def execute(self, context):
        #選択オブジェクトを保存
        active = bpy.context.scene.objects.active
        #選択オブジェクトのタイプを保存
        actype = active.type
        #選択オブジェクトがガーブ＆メッシュ以外だったらReturn
        if not (actype=='MESH' or actype=='CURVE'):
            return {'FINISHED'}
        #選択オブジェクトのメッシュがメッシュだったらカーブに変換
        if actype == 'MESH':
        	#カーブに変換
        	bpy.ops.object.convert(target='CURVE')
        
        #Nurbsに変換
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.curve.spline_type_set(type='NURBS') 
        bpy.ops.object.mode_set(mode='OBJECT')
        
        #終点とスムーズを設定
        for spline in bpy.context.scene.objects.active.data.splines:
            spline.use_endpoint_u = True #終点を設定
            spline.use_smooth = True #スムーズを設定
            
        #元々設定されているベベルとテーパーを削除
        taperobj = bpy.context.scene.objects.active.data.taper_object
        bevelobj = bpy.context.scene.objects.active.data.bevel_object
        for scene in bpy.data.scenes:
            for obj in scene.objects:
                if obj == taperobj:
                    scene.objects.unlink(taperobj)
                if obj == bevelobj:
                    scene.objects.unlink(bevelobj)
        if taperobj != None:
            bpy.data.objects.remove(taperobj)
        if bevelobj != None:
            bpy.data.objects.remove(bevelobj)
    
        #テイパーを設定
        target = bpy.context.scene.objects.active
        if self.my_int_taparType == 0:
            for spline in bpy.context.active_object.data.splines:
                spline.points[len(spline.points)-1].radius = 0.0
            print("0")
        elif self.my_int_taparType == 1:
            for spline in bpy.context.active_object.data.splines:
                for point in spline.points:
                    point.radius = 1.0
        elif self.my_int_taparType == 2:
            verts = [(-2.0, 1.29005, 0.0, 1.0), (-1.0, 0.97704, 0.0, 1.0), (0.0, 0.67615, 0.0, 1.0), (1.0, 0.33936, 0.0, 1.0), (2.0, 0.0, 0.0, 1.0)]
            make_Path(verts)
        elif self.my_int_taparType == 3:
            verts = [(-2.0, 0.82815, 0.0, 1.0), (-1.0, 1.08073, 0.0, 1.0), (0.0, 1.12222, 0.0, 1.0), (1.0, 0.14653, 0.0, 1.0), (2.0, 0.0, 0.0, 1.0)]
            make_Path(verts)
        elif self.my_int_taparType == 4:
            verts = [(-2.0, 1.74503, 0.0, 1.0), (-1.0, 1.74503, 0.0, 1.0), (0.0, 1.74503, 0.0, 1.0), (1.0, 1.74503, 0.0, 1.0), (2.0, 0.0, 0.0, 1.0)]
            make_Path(verts)
        elif self.my_int_taparType == 5:
            verts = [(-2.0, 0.0, 0.0, 1.0), (-1.0, 1.517, 0.0, 1.0), (0.0, 1.9242, 0.0, 1.0), (1.0, 1.81018, 0.0, 1.0), (2.0, 0.0, 0.0, 1.0)]
            make_Path(verts)
        elif self.my_int_taparType == 6:
            verts = [(-2.0, 1.6929, 0.0, 1.0), (-1.0, 0.79381, 0.0, 1.0), (0.0, 0.3801, 0.0, 1.0), (1.0, 0.12926, 0.0, 1.0), (2.0, 0.0, 0.0, 1.0)]
            make_Path(verts)
        elif self.my_int_taparType == 7:
            verts = [(-2.0, 1.17495, 0.0, 1.0), (-1.0, 1.27268, 0.0, 1.0), (0.0, 0.9632, 0.0, 1.0), (1.0, -1.26827, 0.0, 1.0), (2.0, 0.0, 0.0, 1.0)]
            make_Path(verts)
        else:
            print("errer 01")
        target.data.taper_object = bpy.context.scene.objects.active
        bpy.context.scene.objects.active = target
        
        #ベベルを設定
        target = bpy.context.scene.objects.active
        if self.my_int_bevelType == 0:
            verts = [(0.0, -0.1, 0.0, 1.0), (-0.1, -0.1, 0.0, 0.354), (-0.1, 0.0, 0.0, 1.0), (-0.1, 0.1, 0.0, 0.354), (0.0, 0.1, 0.0, 1.0), (0.1, 0.1, 0.0, 0.354), (0.1, 0.0, 0.0, 1.0), (0.1, -0.1, 0.0, 0.354)]
            make_bevelCurve(verts,True,4,3)
        elif self.my_int_bevelType == 1:
            verts = [(0.0, -0.1, 0.0, 1.0), (-0.01341, -0.01341, 0.0, 0.354), (-0.1, 0.0, 0.0, 1.0), (-0.01341, 0.01341, 0.0, 0.354), (0.0, 0.1, 0.0, 1.0), (0.01341, 0.01341, 0.0, 0.354), (0.1, 0.0, 0.0, 1.0), (0.01341, -0.01341, 0.0, 0.354)]
            make_bevelCurve(verts,True,4,3)
        elif self.my_int_bevelType == 2:
            verts = [(0.0, -0.05443, 0.0, 1.0), (-0.10876, -0.05093, 0.0, 0.354), (-0.15258, 0.05083, 0.0, 1.0), (-0.04917, 0.01237, 0.0, 0.354), (0.0, 0.08072, 0.0, 1.0), (0.04216, 0.00711, 0.0, 0.354), (0.17186, 0.05083, 0.0, 1.0), (0.10351, -0.04917, 0.0, 0.354)]
            make_bevelCurve(verts,True,4,3)
        elif self.my_int_bevelType == 3:
            verts = [(0.0, -0.1, 0.0, 1.0), (-0.1, -0.1, 0.0, 0.354), (-0.15173, -0.07836, 0.0, 1.0), (-0.11293, 0.07718, 0.0, 0.354), (0.0, 0.1, 0.0, 1.0), (0.12282, 0.0749, 0.0, 0.354), (0.1601, -0.07608, 0.0, 1.0), (0.1, -0.1, 0.0, 0.354)]
            make_bevelCurve(verts,True,4,3)
        elif self.my_int_bevelType == 4:
            verts = [(0.0, -0.1, 0.0, 1.0), (-0.1, -0.1, 0.0, 0.354), (-0.15173, -0.07836, 0.0, 1.0), (-0.02207, -0.02882, 0.0, 0.354), (0.0, 0.1, 0.0, 1.0), (0.03385, -0.02542, 0.0, 0.354), (0.1601, -0.07608, 0.0, 1.0), (0.1, -0.1, 0.0, 0.354)]
            make_bevelCurve(verts,True,4,3)
        elif self.my_int_bevelType == 5:
            verts = [(0.0,-0.10737,0.0,1.0),(-0.02482,-0.05971,0.0,1.0),(-0.07637,-0.07637,0.0,1.0)\
            ,(-0.05971,-0.02482,0.0,1.0),(-0.10737,0.0,0.0,1.0),(-0.05971,0.02482,0.0,1.0)\
            ,(-0.07637,0.07637,0.0,1.0),(-0.02482,0.05971,0.0,1.0),(0.0,0.10737,0.0,1.0)\
            ,(0.02482,0.05971,0.0,1.0),(0.07637,0.07637,0.0,1.0),(0.05971,0.02482,0.0,1.0)\
            ,(0.10737,0.0,0.0,1.0),(0.05971,-0.02482,0.0,1.0),(0.07637,-0.07637,0.0,1.0)\
            ,(0.02482,-0.05971,0.0,1.0)]
            make_bevelCurve(verts,True,2,1)
        elif self.my_int_bevelType == 6:
            verts = [(-0.10737,0.0,0.0,1.0),(-0.05971,0.02482,0.0,1.0)\
            ,(-0.07637,0.07637,0.0,1.0),(-0.02482,0.05971,0.0,1.0),(0.0,0.10737,0.0,1.0)\
            ,(0.02482,0.05971,0.0,1.0),(0.07637,0.07637,0.0,1.0),(0.05971,0.02482,0.0,1.0)\
            ,(0.10737,0.0,0.0,1.0)]
            make_bevelCurve(verts,False,2,1,'POLY')
        elif self.my_int_bevelType == 7:
            verts = [(-0.21377,-0.01224,0.0,1.0),(-0.21369,0.01544,0.0,1.0),(-0.05366,0.01465,0.0,1.0),\
            (0.0,0.08072,0.0,1.0),(0.04366,0.01472,0.0,1.0),(0.23172,0.01658,0.0,1.0),\
            (0.23112,-0.00807,0.0,1.0)]
            make_bevelCurve(verts,False,4,3)
        elif self.my_int_bevelType == 8:
            verts = [(-0.21369,-0.00024,0.0,1.0),(0.0,0.06504,0.0,1.0),\
            (0.23172,0.0009,0.0,1.0)]
            make_bevelCurve(verts,False,3,3)
        elif self.my_int_bevelType == 9:
            verts = [(-0.21369,-0.00024,0.0,1.0),(0.0,-0.06517,0.0,1.0),\
            (0.23172,0.0009,0.0,1.0)]
            make_bevelCurve(verts,False,3,3)
        elif self.my_int_bevelType == 10:
            verts = [(-0.21369,-0.00024,0.0,1.0),(0.23172,0.0009,0.0,1.0)]
            make_bevelCurve(verts,False,2,2)
        elif self.my_int_bevelType == 11:
            verts = [(0.0,-0.00981,0.0,1.0),(-0.160276,-0.012221,0.0,1.0),(-0.179911,-0.052557,0.0,1.0),
            (-0.208451,0.0,0.0,1.0),(-0.17869,0.051167,0.0,1.0),(-0.159358,0.00654,0.0,1.0),
            (0.0,-0.00414,0.0,1.0),(0.169297,0.008569,0.0,1.0),(0.186631,0.039629,0.0,1.0),
            (0.215239,0.0,0.0,1.0),(0.186103,-0.035806,0.0,1.0),(0.151654,-0.014581,0.0,1.0)]
            make_bevelCurve(verts,True,6,2)
        elif self.my_int_bevelType == 12:
            verts = [(-0.179911,-0.029543,0.0,1.0),
            (-0.208451,0.0,0.0,1.0),(-0.17869,0.051167,0.0,1.0),(-0.159358,0.00654,0.0,1.0),
            (0.0,-0.00414,0.0,1.0),(0.169297,0.008569,0.0,1.0),(0.186631,0.039629,0.0,1.0),
            (0.215239,0.0,0.0,1.0),(0.186103,-0.035806,0.0,1.0)]
            make_bevelCurve(verts,False,6,2)
        elif self.my_int_bevelType == 13:
            verts = [(-0.21369,0.0,0.0,1.0),(-0.185852,0.016927,0.0,1.0),(-0.158014,0.0,0.0,1.0),
            (-0.130176,0.017069,0.0,1.0),(-0.102337,0.0,0.0,1.0),(-0.074499,0.017212,0.0,1.0),
            (-0.046661,0.0,0.0,1.0),(-0.018823,0.017354,0.0,1.0),(0.009015,0.0,0.0,1.0),
            (0.036853,0.017497,0.0,1.0),(0.064691,0.0,0.0,1.0),(0.092529,0.017639,0.0,1.0),
            (0.120367,0.0,0.0,1.0),(0.148206,0.017782,0.0,1.0),(0.176044,0.0,0.0,1.0),
            (0.203882,0.017924,0.0,1.0),(0.23172,0.0,0.0,1.0)]
            make_bevelCurve(verts,False,2,1,'POLY')
        else:
            print("errer 02")
        bpy.context.object.scale[0] = self.my_float_x
        bpy.context.object.scale[1] = self.my_float_y
        target.data.bevel_object = bpy.context.scene.objects.active
        bpy.context.scene.objects.active = target
        
        #UVを設定
        bpy.context.object.data.use_uv_as_generated = True
        bpy.context.object.data.use_fill_caps = False

        #選択オブジェクトの名前を取得
        objname = bpy.context.scene.objects.active.data.name
        
        #元々がメッシュだったらゴールウェイトを設定
        if actype == 'MESH':
	        #すべてのpointsのゴールウェイトに0を設定
	        for spline in bpy.data.curves[objname].splines:
	            for point in spline.points:
	                point.weight_softbody = self.my_float_weight
	        #根本とその次のゴールウェイトに1を設定
	        for spline in bpy.data.curves[objname].splines:
	            spline.points[0].weight_softbody = 1
	            spline.points[1].weight_softbody = 1
            
        #ソフトボディを設定
        bpy.ops.object.modifier_add(type='SOFT_BODY')
        bpy.context.scene.objects.active.soft_body.mass = self.my_float_mass
        bpy.context.scene.objects.active.soft_body.goal_friction = self.my_float_goal_friction
        softbody = bpy.context.scene.objects.active.modifiers[0]
        for m in bpy.context.scene.objects.active.modifiers:
        	if m.type == 'SOFT_BODY':
        		softbody = m
        softbody.point_cache.frame_step = 1
        return {'FINISHED'}
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
#カーブの全制御点の半径の値をソフトボディウェイトにコピー
class Radius2weight(bpy.types.Operator):
    bl_idname = "object.radiustoweight"
    bl_label = "Radius -> SoftBody_Weight"
    bl_options = {'REGISTER','UNDO'}
    bl_description = "カーブの全制御点の半径の値をソフトボディウェイトにコピー"
    def execute(self, context):
    	active = bpy.context.scene.objects.active
    	for spline in active.data.splines:
    		for point in spline.points:
    			point.weight_softbody = point.radius
    	return {'FINISHED'}

#Curveをアーマチュア付きメッシュに変換
class Hair2MeshOperator(bpy.types.Operator):
	bl_idname = "object.hair2mesh"
	bl_label = "Hair -> Mesh"
	bl_options = {'REGISTER','UNDO'}
	bl_description = "Curveをアーマチュア付きメッシュに変換"

	my_boneName = bpy.props.StringProperty(name="BoneName",default="Untitled")

	def execute(self, context):
		active = bpy.context.scene.objects.active
		curveList = []
		amaList = []
		meshList = []
		defaultrot = active.rotation_euler
		for i,spline in enumerate(active.data.splines):
		    #スプライン一つ一つにカーブオブジェクトを作る
		    pos = active.location
		    bpy.ops.curve.primitive_nurbs_path_add(radius=1, view_align=False,
		        enter_editmode=False, location=pos)
		    #Curveの設定からコピーできるものをコピーする
		    curve = bpy.context.scene.objects.active
		    oldCurve = active
		    #splineを全て消し、既存のものからコピーする
		    curve.data.splines.clear()
		    newSpline = curve.data.splines.new(type='NURBS')
		    newSpline.points.add(len(spline.points)-1)
		    for point,newPoint in zip(spline.points,newSpline.points):
		        newPoint.co = point.co
		        newPoint.radius = point.radius
		        newPoint.tilt = point.tilt
		        newPoint.weight_softbody = point.weight_softbody
		    newSpline.use_smooth = spline.use_smooth
		    newSpline.use_endpoint_u = spline.use_endpoint_u
		    newSpline.use_bezier_u = spline.use_bezier_u
		    newSpline.id_data.bevel_object = spline.id_data.bevel_object
		    newSpline.id_data.taper_object = spline.id_data.taper_object
		    newSpline.id_data.use_fill_caps = False
		    newSpline.id_data.resolution_u = spline.id_data.resolution_u
		    newSpline.id_data.render_resolution_u = spline.id_data.render_resolution_u
		    newSpline.order_u = spline.order_u
		    newSpline.resolution_u = spline.resolution_u
		    curve.data.twist_mode = oldCurve.data.twist_mode
		    curve.data.use_auto_texspace = oldCurve.data.use_auto_texspace
		    curve.data.use_uv_as_generated = oldCurve.data.use_uv_as_generated
		    if newSpline.id_data.bevel_object == None:
		        newSpline.id_data.bevel_depth = spline.id_data.bevel_depth
		        newSpline.id_data.bevel_resolution = spline.id_data.bevel_resolution
		        curve.data.fill_mode = oldCurve.data.fill_mode
		        curve.data.offset = oldCurve.data.offset
		        curve.data.extrude = oldCurve.data.extrude
		        curve.data.bevel_depth = oldCurve.data.bevel_depth
		        curve.data.bevel_resolution = oldCurve.data.bevel_resolution
		    #ソフトボディを設定
		    if oldCurve.soft_body != None:
			    bpy.ops.object.modifier_add(type='SOFT_BODY')
			    curve.soft_body.mass = oldCurve.soft_body.mass
			    curve.soft_body.goal_friction = oldCurve.soft_body.goal_friction 
			    curve.soft_body.friction = oldCurve.soft_body.friction
			    curve.soft_body.speed = oldCurve.soft_body.speed
			    curve.soft_body.goal_default = oldCurve.soft_body.goal_default
			    curve.soft_body.goal_max = oldCurve.soft_body.goal_max
			    curve.soft_body.goal_min = oldCurve.soft_body.goal_min
			    curve.soft_body.goal_spring = oldCurve.soft_body.goal_spring
		    #アーマチュアを作る
		    bpy.ops.object.armature_add(location=pos,enter_editmode=False)
		    activeAma = bpy.context.scene.objects.active
		    bpy.ops.object.editmode_toggle()
		    bpy.ops.armature.select_all(action='SELECT')
		    bpy.ops.armature.delete()
		    bpy.ops.armature.bone_primitive_add()
		    print(len(activeAma.data.edit_bones))
		    activeAma.data.edit_bones[0].head = [newSpline.points[0].co[0],
		                                            newSpline.points[0].co[1],
		                                            newSpline.points[0].co[2]]
		    activeAma.data.edit_bones[0].name = self.my_boneName + str(i)
		    print("koko4",len(newSpline.points))
		    if len(newSpline.points) >= 3:
		        for i,newPoint in enumerate(newSpline.points[1:-1]):
		            print("koko2",newPoint.co)
		            rootBoneName = activeAma.data.edit_bones[0].name
		            newBone = activeAma.data.edit_bones.new(rootBoneName)
		            print("koko3",i,newBone)
		            newBone.parent = activeAma.data.edit_bones[i]
		            newBone.use_connect = True
		            newBone.head = [newPoint.co[0],
		                            newPoint.co[1],
		                            newPoint.co[2]]
		    else:
		        newBone = activeAma.data.edit_bones[0]
		    lastBone = newBone
		    lastBone.tail = [newSpline.points[-1].co[0],
		                    newSpline.points[-1].co[1],
		                    newSpline.points[-1].co[2]]
		    activeAma.data.draw_type = "STICK"
		    #ボーンのセグメントを設定（設定しない方が綺麗に動くので終了）
		    #for bone in activeAma.data.edit_bones:
		    #    bone.bbone_segments = newSpline.order_u
		    #カーブを実体化する
		    #物理に使うので元のカーブは残す
		    bpy.ops.object.editmode_toggle()
		    bpy.ops.object.select_all(action='DESELECT')
		    bpy.context.scene.objects.active = curve
		    bpy.ops.object.select_pattern(pattern=curve.name, case_sensitive=False, extend=False)
		    print("koko5",bpy.context.scene,bpy.context.scene.objects.active,curve.rotation_euler)
		    bpy.ops.object.convert(target='MESH', keep_original=True)
		    meshobj = bpy.context.scene.objects.active
		    print("koko6",meshobj)
		    #マテリアルをコピーする
		    print("koko12",meshobj.data.materials,spline.material_index)
		    if len(oldCurve.data.materials) >= 1:
		        material = oldCurve.data.materials[spline.material_index]
		        meshobj.data.materials.append(material) 
		    #元のカーブは多角形にしてBevelやテイパーやメッシュを外してを設定して、物理として使う
		    bpy.ops.object.select_all(action='DESELECT')
		    bpy.context.scene.objects.active = curve
		    bpy.ops.object.select_pattern(pattern=curve.name, case_sensitive=False, extend=False)
		    bebelObj = curve.data.bevel_object
		    curve.data.bevel_object = None
		    curve.data.taper_object = None
		    curve.data.bevel_depth = 0
		    curve.data.bevel_resolution = 0
		    curve.data.extrude = 0
		    newSpline.type = 'POLY'
		    #アーマチュアにスプラインIKをセット
		    if len(activeAma.pose.bones) >= 1:
		        print("koko7",activeAma.pose.bones[-1].constraints)
		        spIK = activeAma.pose.bones[-1].constraints.new("SPLINE_IK")
		        spIK.target = curve
		        spIK.chain_count = len(activeAma.data.bones)
		        spIK.use_chain_offset = False
		        spIK.use_y_stretch = True
		        spIK.use_curve_radius = False
		    activeAma.pose.bones[-1]["spIKName"] = curve.name
		    curve.data.resolution_u = 64
		    #重複した頂点を削除
		    bpy.ops.object.select_all(action='DESELECT')
		    bpy.ops.object.select_pattern(pattern=meshobj.name, case_sensitive=False, extend=False)
		    bpy.context.scene.objects.active = meshobj
		    bpy.ops.object.editmode_toggle()
		    bpy.ops.mesh.select_all(action='TOGGLE')
		    bpy.ops.mesh.remove_doubles(threshold=0.0001)
		    bpy.ops.object.editmode_toggle()
		    #自動のウェイトでアーマチュアを設定
		    bpy.ops.object.select_all(action='DESELECT')
		    bpy.ops.object.select_pattern(pattern=meshobj.name, case_sensitive=False, extend=False)
		    bpy.ops.object.select_pattern(pattern=activeAma.name, case_sensitive=False, extend=True)
		    bpy.context.scene.objects.active = activeAma
		    bpy.ops.object.parent_set(type='ARMATURE_AUTO')
		    #シェイプキーを２つ追加し、一つをBasis、一つをKey1にする
		    bpy.ops.object.select_all(action='DESELECT')
		    bpy.context.scene.objects.active = curve
		    bpy.ops.object.select_pattern(pattern=curve.name, case_sensitive=False, extend=False)
		    bpy.ops.object.shape_key_add(from_mix=False)
		    bpy.ops.object.shape_key_add(from_mix=False)
		    curve.data.shape_keys.key_blocks[1].value = 1
		    bpy.context.object.active_shape_key_index = 1
		    print("koko13",curve.data.shape_keys)
		    #Curveをレントゲンにして透けて見えるように
		    curve.show_x_ray = True
		    #Curveとアーマチュアとメッシュは後でまとめるのでリストにする
		    curveList.append(curve)
		    amaList.append(activeAma)
		    meshList.append(meshobj)
		print("koko8",curveList,amaList,meshList)
		#Curveの親用のEmptyを作る
		bpy.ops.object.empty_add(type='PLAIN_AXES', view_align=False, location=active.location)
		emptyobj = bpy.context.scene.objects.active
		emptyobj.name = self.my_boneName + "Emp"
		#アーマチュアの親オブジェクトを作る
		bpy.ops.object.armature_add(location=active.location,enter_editmode=False)
		pama = bpy.context.scene.objects.active
		pama.data.bones[0].use_deform = False
		#Curveの親を設定
		for c in curveList:
		    bpy.ops.object.select_all(action='DESELECT')
		    bpy.ops.object.select_pattern(pattern=c.name, case_sensitive=False, extend=False)
		    bpy.ops.object.select_pattern(pattern=emptyobj.name, case_sensitive=False, extend=True)
		    bpy.context.scene.objects.active = emptyobj
		    bpy.ops.object.parent_set(type='OBJECT', xmirror=False, keep_transform=True)
		#アーマチュアを合成
		bpy.ops.object.select_all(action='DESELECT')
		for ama in amaList:
		    bpy.ops.object.select_pattern(pattern=ama.name, case_sensitive=False, extend=True)
		bpy.ops.object.select_pattern(pattern=pama.name, case_sensitive=False, extend=True)
		bpy.context.scene.objects.active = pama
		pama.data.draw_type = "STICK"
		bpy.ops.object.join()
		pama = bpy.context.scene.objects.active
		bpy.ops.object.select_all(action='DESELECT')
		bpy.ops.object.select_pattern(pattern=pama.name, case_sensitive=False, extend=False)
		bpy.ops.object.select_pattern(pattern=emptyobj.name, case_sensitive=False, extend=True)
		bpy.context.scene.objects.active = emptyobj
		bpy.ops.object.parent_set(type='OBJECT', xmirror=False, keep_transform=True)
		pama.name = self.my_boneName
		#メッシュを合成
		bpy.ops.object.select_all(action='DESELECT')
		for m in meshList:
		    bpy.ops.object.select_pattern(pattern=m.name, case_sensitive=False, extend=True)
		if len(meshList) >= 1:
		    bpy.context.scene.objects.active = meshList[0]
		    bpy.ops.object.join()
		    activeMesh = bpy.context.scene.objects.active
		    activeMesh.modifiers["Armature"].object = pama
		#親エンプティの回転を元のCurveと同じにする
		emptyobj.rotation_euler = defaultrot
		#アーマチュアのデータを随時更新に変更
		pama.use_extra_recalc_data = True
		#このアーマチュアの名前のボーングループをセット
		boneGroups = pama.pose.bone_groups.new(self.my_boneName)
		print("koko14",boneGroups)
		for bone in pama.pose.bones:
		    bone.bone_group = boneGroups
		layers=(False, False,
		     False, False, False, False, False, False,
		     False, False, False, False, False, False,
		     False, False, False, False, False, False,
		     False, False, False, True, False, False,
		     False, False, False, False, False, False)
		for i,bone in enumerate(pama.data.bones):
		    if i != 0:
		        bone.layers = layers
		#選択をEmptyに
		bpy.ops.object.select_all(action='DESELECT')
		bpy.ops.object.select_pattern(pattern=emptyobj.name, case_sensitive=False, extend=False)
		return {'FINISHED'}
	def invoke(self, context, event):
		wm = context.window_manager
		return wm.invoke_props_dialog(self)

#Curveをアーマチュアに変換
class Curve2AmaOperator(bpy.types.Operator):
	bl_idname = "object.curve2ama"
	bl_label = "Curve -> Ama"
	bl_options = {'REGISTER','UNDO'}
	bl_description = "Curveをアーマチュアに変換"

	my_boneName = bpy.props.StringProperty(name="BoneName",default="Untitled")

	def execute(self, context):
		active = bpy.context.scene.objects.active
		curveList = []
		amaList = []
		#meshList = []
		for i,spline in enumerate(active.data.splines):
		    #スプライン一つ一つにカーブオブジェクトを作る
		    pos = active.location
		    defaultrot = active.rotation_euler
		    bpy.ops.curve.primitive_nurbs_path_add(radius=1, view_align=False,
		        enter_editmode=False, location=pos)
		    #Curveの設定からコピーできるものをコピーする
		    curve = bpy.context.scene.objects.active
		    oldCurve = active
		    #splineを全て消し、既存のものからコピーする
		    curve.data.splines.clear()
		    newSpline = curve.data.splines.new(type='NURBS')
		    newSpline.points.add(len(spline.points)-1)
		    for point,newPoint in zip(spline.points,newSpline.points):
		        newPoint.co = point.co
		        newPoint.radius = point.radius
		        newPoint.tilt = point.tilt
		        newPoint.weight_softbody = point.weight_softbody
		    newSpline.use_smooth = spline.use_smooth
		    newSpline.use_endpoint_u = spline.use_endpoint_u
		    newSpline.use_bezier_u = spline.use_bezier_u
		    newSpline.id_data.bevel_object = spline.id_data.bevel_object
		    newSpline.id_data.taper_object = spline.id_data.taper_object
		    newSpline.id_data.use_fill_caps = False
		    newSpline.id_data.resolution_u = spline.id_data.resolution_u
		    newSpline.id_data.render_resolution_u = spline.id_data.render_resolution_u
		    newSpline.order_u = spline.order_u
		    newSpline.resolution_u = spline.resolution_u
		    curve.data.twist_mode = oldCurve.data.twist_mode
		    if newSpline.id_data.bevel_object == None:
		        newSpline.id_data.bevel_depth = spline.id_data.bevel_depth
		        newSpline.id_data.bevel_resolution = spline.id_data.bevel_resolution
		    #ソフトボディを設定
		    if oldCurve.soft_body != None:
			    bpy.ops.object.modifier_add(type='SOFT_BODY')
			    curve.soft_body.mass = oldCurve.soft_body.mass
			    curve.soft_body.goal_friction = oldCurve.soft_body.goal_friction
			    curve.soft_body.friction = oldCurve.soft_body.friction
			    curve.soft_body.speed = oldCurve.soft_body.speed
			    curve.soft_body.goal_default = oldCurve.soft_body.goal_default
			    curve.soft_body.goal_max = oldCurve.soft_body.goal_max
			    curve.soft_body.goal_min = oldCurve.soft_body.goal_min
			    curve.soft_body.goal_spring = oldCurve.soft_body.goal_spring
		    #アーマチュアを作る
		    bpy.ops.object.armature_add(location=pos,enter_editmode=False)
		    activeAma = bpy.context.scene.objects.active
		    bpy.ops.object.editmode_toggle()
		    bpy.ops.armature.select_all(action='SELECT')
		    bpy.ops.armature.delete()
		    bpy.ops.armature.bone_primitive_add()
		    print(len(activeAma.data.edit_bones))
		    activeAma.data.edit_bones[0].head = [newSpline.points[0].co[0],
		                                            newSpline.points[0].co[1],
		                                            newSpline.points[0].co[2]]
		    activeAma.data.edit_bones[0].name = self.my_boneName + str(i)
		    print("koko4",len(newSpline.points))
		    if len(newSpline.points) >= 3:
		        for i,newPoint in enumerate(newSpline.points[1:-1]):
		            print("koko2",newPoint.co)
		            rootBoneName = activeAma.data.edit_bones[0].name
		            newBone = activeAma.data.edit_bones.new(rootBoneName)
		            print("koko3",i,newBone)
		            newBone.parent = activeAma.data.edit_bones[i]
		            newBone.use_connect = True
		            newBone.head = [newPoint.co[0],
		                            newPoint.co[1],
		                            newPoint.co[2]]
		    else:
		        newBone = activeAma.data.edit_bones[0]
		    lastBone = newBone
		    lastBone.tail = [newSpline.points[-1].co[0],
		                    newSpline.points[-1].co[1],
		                    newSpline.points[-1].co[2]]
		    activeAma.data.draw_type = "STICK"
		    #元のカーブは多角形にしてBevelやテイパーやメッシュを外してを設定して、物理として使う
		    bpy.ops.object.editmode_toggle()
		    bpy.ops.object.select_all(action='DESELECT')
		    bpy.context.scene.objects.active = curve
		    bpy.ops.object.select_pattern(pattern=curve.name, case_sensitive=False, extend=False)
		    bebelObj = curve.data.bevel_object
		    curve.data.bevel_object = None
		    curve.data.taper_object = None
		    curve.data.bevel_depth = 0
		    curve.data.bevel_resolution = 0
		    newSpline.type = 'POLY'
		    #アーマチュアにスプラインIKをセット
		    if len(activeAma.pose.bones) >= 1:
		        print("koko7",activeAma.pose.bones[-1].constraints)
		        spIK = activeAma.pose.bones[-1].constraints.new("SPLINE_IK")
		        spIK.target = curve
		        spIK.chain_count = len(activeAma.data.bones)
		        spIK.use_chain_offset = False
		        spIK.use_y_stretch = True
		        spIK.use_curve_radius = False
		        activeAma.pose.bones[-1]["spIKName"] = curve.name
		    curve.data.resolution_u = 64
		    #シェイプキーを２つ追加し、一つをBasis、一つをKey1にする
		    bpy.ops.object.select_all(action='DESELECT')
		    bpy.context.scene.objects.active = curve
		    bpy.ops.object.select_pattern(pattern=curve.name, case_sensitive=False, extend=False)
		    bpy.ops.object.shape_key_add(from_mix=False)
		    bpy.ops.object.shape_key_add(from_mix=False)
		    curve.data.shape_keys.key_blocks[1].value = 1
		    bpy.context.object.active_shape_key_index = 1
		    print("koko13",curve.data.shape_keys)
		    #Curveをレントゲンにして透けて見えるように
		    curve.show_x_ray = True
		    #Curveとアーマチュアとメッシュは後でまとめるのでリストにする
		    curveList.append(curve)
		    amaList.append(activeAma)
		#Curveの親用のEmptyを作る
		bpy.ops.object.empty_add(type='PLAIN_AXES', view_align=False, location=active.location)
		emptyobj = bpy.context.scene.objects.active
		emptyobj.name = self.my_boneName + "Emp"
		#アーマチュアの親オブジェクトを作る
		bpy.ops.object.armature_add(location=active.location,enter_editmode=False)
		pama = bpy.context.scene.objects.active
		pama.data.bones[0].use_deform = False
		#Curveの親を設定
		for c in curveList:
		    bpy.ops.object.select_all(action='DESELECT')
		    bpy.ops.object.select_pattern(pattern=c.name, case_sensitive=False, extend=False)
		    bpy.ops.object.select_pattern(pattern=emptyobj.name, case_sensitive=False, extend=True)
		    bpy.context.scene.objects.active = emptyobj
		    bpy.ops.object.parent_set(type='OBJECT', xmirror=False, keep_transform=True)
		#アーマチュアを合成
		bpy.ops.object.select_all(action='DESELECT')
		for ama in amaList:
		    bpy.ops.object.select_pattern(pattern=ama.name, case_sensitive=False, extend=True)
		bpy.ops.object.select_pattern(pattern=pama.name, case_sensitive=False, extend=True)
		bpy.context.scene.objects.active = pama
		pama.data.draw_type = "STICK"
		bpy.ops.object.join()
		pama = bpy.context.scene.objects.active
		bpy.ops.object.select_all(action='DESELECT')
		bpy.ops.object.select_pattern(pattern=pama.name, case_sensitive=False, extend=False)
		bpy.ops.object.select_pattern(pattern=emptyobj.name, case_sensitive=False, extend=True)
		bpy.context.scene.objects.active = emptyobj
		bpy.ops.object.parent_set(type='OBJECT', xmirror=False, keep_transform=True)
		pama.name = self.my_boneName
		#親エンプティの回転を元のCurveと同じにする
		emptyobj.rotation_euler = defaultrot
		#アーマチュアのデータを随時更新に変更
		pama.use_extra_recalc_data = True
		#このアーマチュアの名前のボーングループをセット
		boneGroups = pama.pose.bone_groups.new(self.my_boneName)
		print("koko14",boneGroups)
		for bone in pama.pose.bones:
		    bone.bone_group = boneGroups
		layers=(False, False,
		     False, False, False, False, False, False,
		     False, False, False, False, False, False,
		     False, False, False, False, False, False,
		     False, False, False, True, False, False,
		     False, False, False, False, False, False)
		for i,bone in enumerate(pama.data.bones):
		    if i != 0:
		        bone.layers = layers
		#選択をEmptyに
		bpy.ops.object.select_all(action='DESELECT')
		bpy.ops.object.select_pattern(pattern=emptyobj.name, case_sensitive=False, extend=False)
		return {'FINISHED'}
	def invoke(self, context, event):
		wm = context.window_manager
		return wm.invoke_props_dialog(self)

#全てのボーンのスプラインIKのミュートを外す
class ViewSpIKOperator(bpy.types.Operator):
	bl_idname = "object.viewspik"
	bl_label = "ViewSPIK"
	bl_options = {'REGISTER','UNDO'}
	bl_description = "全てのボーンのスプラインIKのミュートを外す"
	def execute(self, context):
		ama = bpy.context.scene.objects.active
		print("koko1",ama)
		for bone in ama.pose.bones:
		    print("koko2",bone)
		    if len(bone.constraints) >= 1:
		        for con in bone.constraints:
		            print("koko3",con)
		            if con.type == "SPLINE_IK":
		                con.mute = False
		bpy.ops.object.editmode_toggle()
		bpy.ops.object.editmode_toggle()
		return {'FINISHED'}

#全てのボーンのスプラインIKをミュート
class HiddenSpIKOperator(bpy.types.Operator):
	bl_idname = "object.hiddenspik"
	bl_label = "MuteSPIK"
	bl_options = {'REGISTER','UNDO'}
	bl_description = "全てのボーンのスプラインIKをミュート"
	def execute(self, context):
		ama = bpy.context.scene.objects.active
		print("koko1",ama)
		for bone in ama.pose.bones:
		    print("koko2",bone)
		    if len(bone.constraints) >= 1:
		        for con in bone.constraints:
		            print("koko3",con)
		            if con.type == "SPLINE_IK":
		                con.mute = True
		bpy.ops.object.editmode_toggle()
		bpy.ops.object.editmode_toggle()
		return {'FINISHED'}

#Menu in tools region
class AnimeHairPanel(bpy.types.Panel):
    bl_label = "Amasawa Tools"
    bl_space_type = "VIEW_3D"
    bl_context = "objectmode"
    bl_region_type = "TOOLS"
    bl_category = "Tools"
 
    def draw(self, context):
        hairCol = self.layout.column(align=True)
        hairCol.label(text="Create:")
        hairCol.operator("object.animehair")
        hairCol.operator("object.radiustoweight")

        col = self.layout.column(align=True)
        col.label(text="Convert:")
        col.operator("object.hair2mesh")
        col.operator("object.curve2ama")

        col.label(text="all of Spline IK:")
        row = col.row(align=True)
        row.operator("object.viewspik",text="View")
        row.operator("object.hiddenspik",text="Mute")
  
def register():# 登録
    bpy.utils.register_class(AnimeHairOperator)
    bpy.utils.register_class(Radius2weight)
    bpy.utils.register_class(Hair2MeshOperator)
    bpy.utils.register_class(Curve2AmaOperator)
    bpy.utils.register_class(AnimeHairPanel)
    bpy.utils.register_class(ViewSpIKOperator)
    bpy.utils.register_class(HiddenSpIKOperator)
    
def unregister():# 解除
    bpy.utils.unregister_class(AnimeHairOperator)
    bpy.utils.unregister_class(Radius2weight)
    bpy.utils.unregister_class(Hair2MeshOperator)
    bpy.utils.unregister_class(Curve2AmaOperator)
    bpy.utils.unregister_class(AnimeHairPanel)
    bpy.utils.unregister_class(ViewSpIKOperator)
    bpy.utils.unregister_class(HiddenSpIKOperator)
  
#入力
#bpy.ops.object.animehair('INVOKE_DEFAULT')

if __name__ == "__main__":
    register()