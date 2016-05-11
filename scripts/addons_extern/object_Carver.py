# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


#########################################################################################################
bl_info = {
    "name": "Carve MT",
    "category": "Object",
    "author": "Pixivore",
    "version": (1,0,0),
    "blender": (2, 77, 0),
    "description": "Multiple tools for carve objects.",
}
#########################################################################################################


#########################################################################################################
import bpy
import bgl
import blf
import math
import mathutils
import bmesh
from bpy_extras.view3d_utils import region_2d_to_vector_3d, region_2d_to_location_3d
#########################################################################################################


#########################################################################################################
class CarverPrefs(bpy.types.AddonPreferences):
    bl_idname = __name__

    bpy.types.Scene.Enable_Tab_01 = bpy.props.BoolProperty(default=False)
    bpy.types.Scene.Enable_Tab_02 = bpy.props.BoolProperty(default=False)
    

    def draw(self, context):
        layout = self.layout

        layout.prop(context.scene, "Enable_Tab_01", text="Info", icon="QUESTION")
        if context.scene.Enable_Tab_01:
            row = layout.row()
            layout.label(text="Carver Operator")
            layout.label(text="Select object and [CTRL]+[SHIFT]+[Q] to carve")
            
        layout.prop(context.scene, "Enable_Tab_02", text="URL's", icon="URL")   
        if context.scene.Enable_Tab_02:
            row = layout.row()
            row.operator("wm.url_open", text="pixivores.com").url = "http://pixivores.com"
#########################################################################################################


#########################################################################################################
# Opengl draws
#########################################################################################################
def draw_callback_px(self, context):
    font_id = 0  # XXX, need to find out how best to get this.

    region = context.region

    # Tente de positionner le texte au milieu de la fenetre (à refaire)
    xt = int(region.width/2.0)
    yt = 70
    
    # Mode de découpe
    if(self.shift == False):
        BooleanMode = "Difference Ops (Shift)"
    else:        
        BooleanMode = "Rebool Ops (Shift)"
        
    # Position et affichage du texte du mode en cours avec les infos dessous (Voir pour mieux centrer le texte)        
    blf.position(font_id, xt - blf.dimensions(font_id, BooleanMode)[0], 65 + yt, 0)
    blf.size(font_id, 20, 82)
    bgl.glColor4f(0.900, 0.4, 0.00, 1.0)
    blf.draw(font_id, BooleanMode)
    
    bgl.glLineWidth(2)
    bgl.glColor4f(0.900, 0.4, 0.00, 1.0)
    bgl.glBegin(bgl.GL_LINE_STRIP)
    if(self.shift == False):
        bgl.glVertex2i(int(xt - blf.dimensions(font_id, BooleanMode)[0] + 150), 55 + yt)
        bgl.glVertex2i(int(xt - blf.dimensions(font_id, BooleanMode)[0] + 350), 55 + yt)
    else:
        bgl.glVertex2i(int(xt - blf.dimensions(font_id, BooleanMode)[0] + 110), 55 + yt)
        bgl.glVertex2i(int(xt - blf.dimensions(font_id, BooleanMode)[0] + 310), 55 + yt)
                
    bgl.glEnd()
    
    # Selon le mode, l'ecriture change de largeur donc le centre est décalé. Ca permet de "réparer" les erreurs.
    if(self.shift == False):
        xt = xt - blf.dimensions(font_id, BooleanMode)[0] + 150
    else:
        xt = xt - blf.dimensions(font_id, BooleanMode)[0] + 110
        
    # Affichage des infos        
    blf.size(font_id, 20, 50)
    blf.position(font_id, xt + 15, 35 + yt, 0)
    bgl.glColor4f(0.912, 0.919, 0.994, 1.0)
    if(self.CutMode == 0):
        blf.draw(font_id, "Cut Type Rectangle (SPACE)")
    if(self.CutMode == 1):
        blf.draw(font_id, "Cut Type Circle (SPACE)")
    if(self.CutMode == 2):
        blf.draw(font_id, "Cut Type Line (SPACE)")

    if(self.CutMode == 0):
        blf.size(font_id, 20, 50)
        blf.position(font_id, xt + 15, 15 + yt, 0)
        bgl.glColor4f(0.912, 0.919, 0.994, 1.0)
        blf.draw(font_id, "Dimension (MouseMove)")
        blf.position(font_id, xt + 15, -5 + yt, 0)
        bgl.glColor4f(0.912, 0.919, 0.994, 1.0)
        blf.draw(font_id, "Move all(Alt + MouseMove)")

    if(self.CutMode == 1):
        blf.size(font_id, 20, 50)
        blf.position(font_id, xt + 15, 15 + yt, 0)
        bgl.glColor4f(0.912, 0.919, 0.994, 1.0)
        blf.draw(font_id, "Rotation inc (Ctrl + MouseWheel)")
        blf.position(font_id, xt + 15, -5 + yt, 0)
        blf.draw(font_id, "Rotation and Radius (Vertical and Horizontal mouse)")
        blf.position(font_id, xt + 15, -25 + yt, 0)
        blf.draw(font_id, "Subdivision (MouseWheel)")
        blf.position(font_id, xt + 15, -45 + yt, 0)
        blf.draw(font_id, "Move all(Alt + MouseMove)")

    if(self.CutMode == 2):
        blf.size(font_id, 20, 50)
        blf.position(font_id, xt + 15, 15 + yt, 0)
        bgl.glColor4f(0.912, 0.919, 0.994, 1.0)
        blf.draw(font_id, "New point (Left Mouse)")
        blf.position(font_id, xt + 15, -5 + yt, 0)
        blf.draw(font_id, "Move all(Alt + MouseMove)")
        blf.position(font_id, xt + 15, -25 + yt, 0)
        blf.draw(font_id, "Incremental (Ctrl)")


    # Mode, couleur et largeur des lignes
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glColor4f(0.812, 0.519, 0.094, 0.5)
    bgl.glLineWidth(2)

    # Permet de smoother les points pour les arrondir
    bgl.glEnable(bgl.GL_POINT_SMOOTH)
    if(self.bDone):
        # Affichage des primitives selon le type de découpe choisie
        
        if(len(self.mouse_path) > 1):
            x0 = self.mouse_path[0][0] 
            y0 = self.mouse_path[0][1]
            x1 = self.mouse_path[1][0]
            y1 = self.mouse_path[1][1]
        
        # Affichage de la ligne de coupe
        if(self.CutMode == 2):
            bgl.glBegin(bgl.GL_LINE_STRIP)
            for x, y in self.mouse_path:
                bgl.glVertex2i(x + self.xpos, y + self.ypos)
            bgl.glEnd()

            bgl.glPointSize(6)
            bgl.glBegin(bgl.GL_POINTS)
            for x, y in self.mouse_path:
                bgl.glVertex2i(x + self.xpos, y + self.ypos)
            bgl.glEnd()
            
        # Affichage du rectange de découpe    
        if(self.CutMode == 0):
            bgl.glColor4f(0.812, 0.519, 0.094, 0.5)
            # Selon si on appuie sur SHIFT, le rectangle est plein ou pas
            if(self.shift):
                bgl.glBegin(bgl.GL_QUADS)
                bgl.glVertex2i(x0 + self.xpos, y0 + self.ypos)
                bgl.glVertex2i(x1 + self.xpos, y0 + self.ypos)
                bgl.glVertex2i(x1 + self.xpos, y1 + self.ypos)
                bgl.glVertex2i(x0 + self.xpos, y1 + self.ypos)
                bgl.glEnd()
            else:                
                bgl.glBegin(bgl.GL_LINE_STRIP)
                bgl.glVertex2i(x0 + self.xpos, y0 + self.ypos)
                bgl.glVertex2i(x1 + self.xpos, y0 + self.ypos)
                bgl.glVertex2i(x1 + self.xpos, y1 + self.ypos)
                bgl.glVertex2i(x0 + self.xpos, y1 + self.ypos)
                bgl.glVertex2i(x0 + self.xpos, y0 + self.ypos)
                bgl.glEnd()
            bgl.glPointSize(6)
            bgl.glColor4f(0.812, 0.519, 0.094, 1.0)
            bgl.glBegin(bgl.GL_POINTS)
            bgl.glVertex2i(x0 + self.xpos, y0 + self.ypos)
            bgl.glVertex2i(x1 + self.xpos, y0 + self.ypos)
            bgl.glVertex2i(x1 + self.xpos, y1 + self.ypos)
            bgl.glVertex2i(x0 + self.xpos, y1 + self.ypos)
            bgl.glEnd()

        # Affichage du cercle            
        if(self.CutMode == 1):
            DEG2RAD = 3.14159/180;
            v0 = mathutils.Vector((self.mouse_path[0][0], self.mouse_path[0][1], 0))
            v1 = mathutils.Vector((self.mouse_path[1][0], self.mouse_path[1][1], 0))
            v0 -= v1
            radius = self.mouse_path[1][0] - self.mouse_path[0][0]  
            DEG2RAD = 3.14159/(180/self.stepAngle[self.step])
            if(self.ctrl):
                shift = (3.14159/(360/self.stepAngle[self.step])) * self.stepRotation
            else:
                shift = (self.mouse_path[1][1] - self.mouse_path[0][1])/50
            
            # Selon si on appuie sur SHIFT, le rectangle est plein ou pas                            
            if(self.shift == False):
                bgl.glColor4f(0.812, 0.519, 0.094, 1.0)
                bgl.glBegin(bgl.GL_LINE_LOOP)
                for i in range(0, int(360/self.stepAngle[self.step])):
                    degInRad = i * DEG2RAD
                    bgl.glVertex2i(x0 + self.xpos + int(math.cos(degInRad + shift) * radius), y0 + self.ypos + int(math.sin(degInRad + shift) * radius))
                bgl.glEnd()
            else:                
                bgl.glBegin(bgl.GL_TRIANGLE_FAN)
                bgl.glVertex2i(x0 + self.xpos, y0 + self.ypos)
                for i in range(0, int(360/self.stepAngle[self.step])):
                    degInRad = i * DEG2RAD
                    bgl.glVertex2i(x0 + self.xpos + int(math.cos(degInRad + shift) * radius), y0 + self.ypos + int(math.sin(degInRad + shift) * radius))
                bgl.glVertex2i(x0 + self.xpos + int(math.cos(0 + shift) * radius), y0 + self.ypos + int(math.sin(0 + shift) * radius))
                bgl.glEnd()

    # Opengl par défaut
    bgl.glLineWidth(1)
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
    bgl.glDisable(bgl.GL_POINT_SMOOTH)



#########################################################################################################
# Découpe en rectangle
#########################################################################################################
def CreateCutSquare(self, context):
    # Creation du mesh
    me = bpy.data.meshes.new('CutSquare') 

    # Creation de l'objet
    ob = bpy.data.objects.new('CutSquare', me) 
    # Sauvegarde l'objet créé
    self.CurrentObj = ob
    # Récup des infos de la scene
    scene = context.scene
    region = context.region
    rv3d = context.region_data
    coord = self.mouse_path[0][0], self.mouse_path[0][1]
    # Calcul du vecteur de direction selon l'angle de vue
    depthLocation = region_2d_to_vector_3d(region, rv3d, coord)
    self.ViewVector = depthLocation
    loc = region_2d_to_location_3d(region, rv3d, coord, depthLocation)
    mat = context.space_data.region_3d.view_matrix.transposed().to_3x3().to_4x4()
    # Indique à l'objet sa locatiopn et sa matrice "WORLD"
    ob.matrix_world = mat
    ob.location = loc
    
    # Lie l'objet à la scene
    bpy.context.scene.objects.link(ob)

    # Creation du bmesh
    t_bm = bmesh.new()
    t_bm.from_mesh(me)
    # Convertit les coords de la souris en espace 3D
    v0 = self.mouse_path[0][0] + self.xpos, self.mouse_path[0][1] + self.ypos
    v1 = self.mouse_path[1][0] + self.xpos, self.mouse_path[1][1] + self.ypos
    vec =  region_2d_to_vector_3d(region, rv3d, v0)
    loc0 = region_2d_to_location_3d(region, rv3d, v0, vec) - loc
    vec = region_2d_to_vector_3d(region, rv3d, v1)
    loc1 = region_2d_to_location_3d(region, rv3d, v1, vec) - loc
    
    loc0 = loc0 * mat
    loc1 = loc1 * mat
    
    # !!!! encore utile ???
    vl = self.mouse_path[1][0] - self.mouse_path[0][0], self.mouse_path[1][1] - self.mouse_path[0][1]
    vecl =  region_2d_to_vector_3d(region, rv3d, vl)
    length = region_2d_to_location_3d(region, rv3d, vl, vecl)

    # Récup des coordonnées et création des vertices
    # !!!! a mettre directement !!!
    x0 = loc0[0]
    y0 = loc0[1]
    z0 = loc0[2]
    x1 = loc1[0]
    y1 = loc1[1]
    z1 = loc1[2]

    t_v0 = t_bm.verts.new((x0, y0, z0))
    t_v1 = t_bm.verts.new((x1, y0, z0))
    t_v2 = t_bm.verts.new((x1, y1, z1))
    t_v3 = t_bm.verts.new((x0, y1, z1))

    # Mise à jour de l'index des vertices
    t_bm.verts.index_update()
    # Creation des faces
    t_face = t_bm.faces.new([t_v0, t_v1, t_v2, t_v3]) 
    # Sauvegarde du mesh
    t_bm.to_mesh(me)



#########################################################################################################
# Ligne de découpe
#########################################################################################################
def CreateCutLine(self, context):
    me = bpy.data.meshes.new('CutLine') 

    ob = bpy.data.objects.new('CutLine', me)   
    self.CurrentObj = ob

    scene = context.scene
    region = context.region
    rv3d = context.region_data
    coord = self.mouse_path[0][0], self.mouse_path[0][1]
    depthLocation = region_2d_to_vector_3d(region, rv3d, coord)
    self.ViewVector = depthLocation
    loc = region_2d_to_location_3d(region, rv3d, coord, depthLocation)
    mat = context.space_data.region_3d.view_matrix.transposed().to_3x3().to_4x4()

    ob.matrix_world = mat
    ob.location = loc

    bpy.context.scene.objects.link(ob)

    t_bm = bmesh.new() 
    t_bm.from_mesh(me) 

    # Parcours tous les points et les convertit avant de les sauvegarder
    NbVertices = 0    
    for x, y in self.mouse_path:
        v0 = x + self.xpos, y + self.ypos
        vec =  region_2d_to_vector_3d(region, rv3d, v0)
        loc0 = region_2d_to_location_3d(region, rv3d, v0, vec) - loc

        loc0 = loc0 * mat
    
        x0 = loc0[0]
        y0 = loc0[1]
        z0 = loc0[2]

        NbVertices += 1
        if(NbVertices == 1):
            t_v0 = t_bm.verts.new((x0, y0, z0))
            t_bm.verts.index_update()
        else:
            t_v1 = t_bm.verts.new((x0, y0, z0))
            t_edges = t_bm.edges.new([t_v0, t_v1]) 
            NbVertices = 1
            t_v0 = t_v1
    
    t_bm.to_mesh(me)



#########################################################################################################
# Cercle de découpe
#########################################################################################################
def CreateCutCircle(self, context):
    me = bpy.data.meshes.new('CutCircle') 

    ob = bpy.data.objects.new('CutCircle', me) 
    self.CurrentObj = ob

    scene = context.scene
    region = context.region
    rv3d = context.region_data
    coord = self.mouse_path[0][0], self.mouse_path[0][1]
    depthLocation = region_2d_to_vector_3d(region, rv3d, coord)
    self.ViewVector = depthLocation
    loc = region_2d_to_location_3d(region, rv3d, coord, depthLocation)
    mat = context.space_data.region_3d.view_matrix.transposed().to_3x3().to_4x4()

    ob.matrix_world = mat
    ob.location = loc
    
    bpy.context.scene.objects.link(ob)

    t_bm = bmesh.new() 
    t_bm.from_mesh(me) 

    x0 = self.mouse_path[0][0]
    y0 = self.mouse_path[0][1]
    x1 = self.mouse_path[1][0]
    y1 = self.mouse_path[1][1]
    
    v0 = mathutils.Vector((self.mouse_path[0][0], self.mouse_path[0][1], 0))
    v1 = mathutils.Vector((self.mouse_path[1][0], self.mouse_path[1][1], 0))
    v0 -= v1
    radius = self.mouse_path[1][0] - self.mouse_path[0][0]  
    DEG2RAD = 3.14159/(180/self.stepAngle[self.step])
    if(self.ctrl):
        shift = (3.14159/(360/self.stepAngle[self.step])) * self.stepRotation
    else:
        shift = (self.mouse_path[1][1] - self.mouse_path[0][1])/50

    # Passe en revue tous les points du cercle pour les convertir
    FacesList = []
    for i in range(0, int(360/self.stepAngle[self.step])):
        degInRad = i * DEG2RAD
        v0 = x0 + self.xpos + int(math.cos(degInRad + shift) * radius), y0 + self.ypos + int(math.sin(degInRad + shift) * radius)
        vec =  region_2d_to_vector_3d(region, rv3d, v0)
        loc0 = region_2d_to_location_3d(region, rv3d, v0, vec) - loc
        loc0 = loc0 * mat

        t_v0 = t_bm.verts.new(loc0)
        
        FacesList.append(t_v0)


    t_bm.verts.index_update()

    t_face = t_bm.faces.new(FacesList) 

    t_bm.to_mesh(me)



#########################################################################################################
# Dimensions de l'objet à découper (SCULPT Tools tips)
#########################################################################################################
def objDiagonal(obj):
    return ((obj.dimensions[0]**2)+(obj.dimensions[1]**2)+(obj.dimensions[2]**2))**0.5



#########################################################################################################
# Modal Operator
#########################################################################################################
class Carver(bpy.types.Operator):
    bl_idname = "object.carve"
    bl_label = "Carve"
    bl_description = "Cut mesh in object mode"
    bl_options = {'REGISTER', 'UNDO'}


    #---------------------------------------------------------------------------------------------------
    @classmethod
    def poll(cls, context):
        ob = context.active_object
        # Il faut au moins un mesh de selectionner
        return(ob and ob.type == 'MESH' and context.mode == 'OBJECT')
    #---------------------------------------------------------------------------------------------------
    
    #---------------------------------------------------------------------------------------------------
    def modal(self, context, event):
        context.area.tag_redraw()
        
        # [Shift] appuyé
        self.shift = False
        if(event.shift):
            self.shift = True

        # [Ctrl] appuyé
        self.ctrl = False
        if(event.ctrl):
            self.ctrl = True
            
        # [Alt] appuyé
        self.alt = False
        if(event.alt and event.value == 'PRESS'):
            if(self.InitPosition == False):
                # Initialise les variables pour la position de la forme de découpe
                self.xpos = 0
                self.ypos = 0
                self.last_mouse_region_x = event.mouse_region_x
                self.last_mouse_region_y = event.mouse_region_y
                self.InitPosition = True
            self.alt = True
        # [Alt] relaché
        if(self.InitPosition and self.alt == False):
            # Mise à jour des coordonnées 
            # !!! Voir pour mieux coordonnéer le tout !!!
            for i in range(0, len(self.mouse_path) - 1):
                l = list(self.mouse_path[i])
                l[0] += self.xpos
                l[1] += self.ypos
                self.mouse_path[i] = tuple(l)
            
            self.xpos = self.ypos = 0  
            self.InitPosition = False    
                  
        # Changement du mode (Possible tant que l'on n'a pas appuyé sur [LEFT mouse]
        if event.type == 'SPACE' and event.value == 'PRESS':
            if(self.bDone == False):
                # Cut Mode
                self.CutMode += 1
                if(self.CutMode > 2):
                    self.CutMode = 0
             
        # Mouvement de la souris
        if event.type == 'MOUSEMOVE':
            if(self.alt == False):
                if(self.bDone):
                    if(self.ctrl and (self.CutMode == 2)):
                        # Mode "incremental"
                        coord = list(self.mouse_path[len(self.mouse_path) - 1])
                        coord[0] = int(self.mouse_path[len(self.mouse_path) - 2][0] + int((event.mouse_region_x - self.mouse_path[len(self.mouse_path) - 2][0])/self.Increment) * self.Increment)
                        coord[1] = int(self.mouse_path[len(self.mouse_path) - 2][1] + int((event.mouse_region_y - self.mouse_path[len(self.mouse_path) - 2][1])/self.Increment) * self.Increment)
                        self.mouse_path[len(self.mouse_path) - 1] = tuple(coord)
                    else:                        
                        self.mouse_path[len(self.mouse_path) - 1] = (event.mouse_region_x, event.mouse_region_y)
            else:
                # [ALT] appuyé, mise à jour de la position de la forme de découpe
                self.xpos += (event.mouse_region_x - self.last_mouse_region_x)
                self.ypos += (event.mouse_region_y - self.last_mouse_region_y)
                
                self.last_mouse_region_x = event.mouse_region_x
                self.last_mouse_region_y = event.mouse_region_y
        
        # Appui sur [LEFT mouse], récupère des coordonnées de la souris
        elif event.type == 'LEFTMOUSE' and event.value == 'RELEASE':
            if(self.CutMode == 2):
                if(self.bDone == False):
                    self.mouse_path.clear()
                    self.mouse_path.append((event.mouse_region_x, event.mouse_region_y))

                self.mouse_path.append((event.mouse_region_x, event.mouse_region_y))
            else:                
                self.mouse_path[0] = (event.mouse_region_x, event.mouse_region_y)
                self.mouse_path[1] = (event.mouse_region_x, event.mouse_region_y)
            self.bDone = True
            
        # Molette de la souris. Permet de changer la subdivision du cercle
        elif event.type == 'WHEELDOWNMOUSE':
            if(self.CutMode == 1):
                if(self.ctrl):
                    self.stepRotation += 1
                else:                
                    self.step += 1
                    if(self.step >= len(self.stepAngle)):
                        self.step = len(self.stepAngle) - 1
        elif event.type == 'WHEELUPMOUSE':
            if(self.CutMode == 1):
                if(self.ctrl):
                    self.stepRotation -= 1
                else:                
                    if(self.step > 0):
                        self.step -= 1

        # Quitter le modal, créér la découpe
        # !!! Voir pour que ce soit plus "User-friendly"
        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            if(self.CutMode == 0):
                CreateCutSquare(self, context)
            if(self.CutMode == 1):
                CreateCutCircle(self, context)
            if(self.CutMode == 2):
                CreateCutLine(self, context)    
                            
            self.finish()
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'FINISHED'}

        return {'RUNNING_MODAL'}
    #---------------------------------------------------------------------------------------------------

    
    #---------------------------------------------------------------------------------------------------
    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            args = (self, context)

            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, args, 'WINDOW', 'POST_PIXEL')

            self.mouse_path = [(0, 0), (0,0)]
            
            self.bDone = False
            
            # Type de découpe (Rectangle, Cercle, Ligne)
            self.CutMode = 0

            # Cercle variables
            self.stepAngle = [2, 4, 5, 6, 9, 10, 15, 20, 30, 40, 45, 60, 72, 90]
            self.step = 4
            self.stepRotation = 0
            
            # Position des primitives
            self.xpos = 0
            self.ypos = 0
            self.InitPosition = False
            
            # Increment de la ligne
            self.Increment = 15
            
            self.ViewVector = mathutils.Vector()
            
            # Objet créé
            self.CurrentObj = None
            
            # type d'operation booleenne
            self.BooleanType = 0
            
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run operator")
            return {'CANCELLED'}
    #---------------------------------------------------------------------------------------------------


    #---------------------------------------------------------------------------------------------------
    def finish(self):            

        context = bpy.context

        objBBDiagonal = objDiagonal(bpy.context.active_object)
        subdivisions = 32
        #viewZAxis = tuple([z * objBBDiagonal for z in context.area.spaces[0].region_3d.view_matrix[2][0:3]])
        #negViewZAxis = tuple([z * (-2 * objBBDiagonal*(1/subdivisions)) for z in context.area.spaces[0].region_3d.view_matrix[2][0:3]])

        ActiveObj = context.active_object
        bpy.ops.object.select_all(action='TOGGLE')

        context.scene.objects.active = self.CurrentObj

        bpy.data.objects[self.CurrentObj.name].select = True
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        
        # Prend l'objet créé, translation vers l'arrière et extrude vers l'avant pour tenter de "choper" toute la geometrie
        # !!! Voir pour trouver un autre systeme !!!
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.select_mode(type="EDGE")
        bpy.ops.transform.translate(value = self.ViewVector * objBBDiagonal)
        for i in range(0, subdivisions):
            bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":-self.ViewVector * objBBDiagonal})
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent()
        bpy.ops.object.mode_set(mode='OBJECT')

        # Selection de l'objet à découper
        bpy.data.objects[ActiveObj.name].select = True
        context.scene.objects.active = ActiveObj
        
        # Opération booleenne selon le type
        if(self.shift == False):
            # On coupe 
            if(self.CutMode != 2):
                # Si c'est pas la ligne, on utilise "booltool" avec une simple difference
                bpy.ops.btool.boolean_diff()
            else:
                # Selectionne la ligne
                bpy.data.objects[self.CurrentObj.name].select = True
                # Active Object
                context.scene.objects.active = ActiveObj
                # Intersection (booltool)
                bpy.ops.btool.boolean_inters()
                # Applique les booleens
                BMname = "BTool_" + self.CurrentObj.name
                
                for mb in ActiveObj.modifiers:
                    if((mb.type == 'BOOLEAN') and (mb.name == BMname)):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=BMname)  

                bpy.ops.object.select_all(action='TOGGLE')

        else:
            # Mode different de decoupe avec la ligne
            if(self.CutMode != 2):
                # Rebool
                bpy.ops.object.rebool()
            else:
                # Pour le rebool avec la ligne
                # 1 - Duplique l'objet à découper
                # 2 - Intersection avec l'objet à découper avec la ligne
                # 3 - Inverse les normales de la "ligne" de découpe
                # 4 - Intersection avec l'objet dupliqué à découper avec la ligne pour obtenir l'autre moitié
                # Duplique l'objet
                bpy.ops.object.select_all(action='TOGGLE')
                bpy.data.objects[ActiveObj.name].select = True
                bpy.ops.object.duplicate()            
                ActiveObject2 = context.active_object    
                # Selectionne la line
                bpy.data.objects[self.CurrentObj.name].select = True
                # Active Objet
                context.scene.objects.active = ActiveObject2
                # Intersection
                bpy.ops.btool.boolean_inters()
                # Applique le modifier
                BMname = "BTool_" + self.CurrentObj.name
                
                for mb in ActiveObject2.modifiers:
                    if((mb.type == 'BOOLEAN') and (mb.name == BMname)):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=BMname)  

                bpy.ops.object.select_all(action='TOGGLE')
                # Reselectionne la ligne et inverse ses normales
                bpy.data.objects[self.CurrentObj.name].select = True
                context.scene.objects.active = self.CurrentObj
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.flip_normals()
                bpy.ops.object.mode_set(mode='OBJECT')

                bpy.data.objects[ActiveObj.name].select = True
                # Active Objet
                context.scene.objects.active = ActiveObj
                # Intersection
                bpy.ops.btool.boolean_inters()
                # Applique le booleen
                BMname = "BTool_" + self.CurrentObj.name
                for mb in ActiveObj.modifiers:
                    if((mb.type == 'BOOLEAN') and (mb.name == BMname)):
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=BMname)  
                
                
        # Applique les booleens
        if(self.CutMode != 2):
            BMname = "BTool_" + self.CurrentObj.name
            for mb in ActiveObj.modifiers:
                if((mb.type == 'BOOLEAN') and (mb.name == BMname)):
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=BMname)  
                    
        # Supprime l'objet de découpe
        lastSelected = None
        if(len(context.selected_objects) > 0):
            if(self.shift == True):
                # Get the last object selected
                lastSelected = context.selected_objects[0]
                if(self.CutMode == 2):
                    lastSelected = ActiveObject2
            bpy.ops.object.select_all(action='TOGGLE')
        bpy.data.objects[self.CurrentObj.name].select = True
        cname = self.CurrentObj.name
        bpy.ops.object.delete(use_global=False)
        
        # Selectionne les objets "fraichement" découpés
        if(lastSelected != None):
            bpy.data.objects[lastSelected.name].select = True
        bpy.data.objects[ActiveObj.name].select = True
        context.scene.objects.active = ActiveObj
        
        # Mise à jour des objets à la manière d'hardops
#########################################################################################################        
        
                


#########################################################################################################
classes = [Carver]
addon_keymaps = []
#########################################################################################################


#########################################################################################################
def register():
    bpy.utils.register_class(CarverPrefs) 

    bpy.utils.register_class(Carver)
    # add keymap entry
    kcfg = bpy.context.window_manager.keyconfigs.addon
    if kcfg:
        km = kcfg.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new("object.carve", 'Q', 'PRESS', shift=True, ctrl=True)
        addon_keymaps.append((km, kmi))
#########################################################################################################


#########################################################################################################
def unregister():
    bpy.utils.unregister_class(CarverPrefs) 

   # remove keymap entry
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
 
    bpy.utils.unregister_class(Carver)
#########################################################################################################



if __name__ == "__main__":
    register()
