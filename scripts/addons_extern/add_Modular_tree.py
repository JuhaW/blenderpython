# This is a beta
# Use it with no restriction
# The code is utterly ugly, I will change that in the future

bl_info = {
    "name": "Modular trees",
    "author": "Herpin Maxime",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "View3D > Add > Mesh > Tree",
    "description": "Adds a Tree",
    "warning": "Beta",
    "wiki_url": "",
    "category": "Add Mesh"}

import bpy
from mathutils import *
from random import *
from math import *
from bpy.props import *
import bmesh




class Module:
	def __init__(self,entree,sortie,verts,faces):
		self.entree = entree
		self.sortie = sortie
		self.verts = verts
		self.faces = faces

	def __repr__(self):
		return('entry vertices:{} , number of splits:{}'.format(len(self.entree),len(self.sortie)))

#[55, 60, 56, 61, 54, 57, 59, 58][58, 59, 57, 54, 61, 56, 60, 55]




class Split:
	def __init__(self,entree,sortie,verts1,verts2,faces,Seams):
		self.entree = entree
		self.sortie = sortie
		self.verts1 = verts1
		self.verts2 = verts2
		self.faces = faces
		self.Seams = Seams
		




def interpolate(verts1,verts2,t):
	return  [Vector(verts1[i])*(1-t) + Vector(verts2[i])*t for i in range(len(verts1))]






S2 = Split([0, 1, 2, 3, 4, 5, 6, 7],([8, 9, 10, 11, 12, 13, 14, 15],[16, 17, 18, 19, 20, 21, 22, 23]),[(-0.0, 1.0, -0.01), (-0.71, 0.71, -0.01), (-1.0, -0.0, -0.01), (-0.71, -0.71, -0.01), (0.0, -1.0, -0.01), (0.71, -0.71, -0.01), (1.0, -0.0, -0.02), (0.71, 0.71, -0.02), (-0.98, 0.89, 1.84), (-1.49, 0.74, 1.62), (-1.78, 0.24, 1.53), (-1.67, -0.33, 1.64), (-1.23, -0.64, 1.87), (-0.73, -0.51, 2.09), (-0.46, 0.0, 2.18), (-0.56, 0.59, 2.07), (0.72, 1.02, 1.8), (1.3, 0.65, 1.8), (1.29, -0.07, 1.93), (0.81, -0.6, 2.07), (0.12, -0.57, 2.13), (-0.37, -0.06, 2.17), (-0.46, 0.62, 2.06), (0.03, 1.05, 1.88), (-1.19, -0.63, 0.6), (-1.42, -0.01, 0.52), (-0.71, -1.0, 0.98), (-0.39, -0.91, 1.36), (0.63, -0.72, 1.11), (-0.2, -0.73, 1.49), (0.85, 0.64, 0.64), (1.12, 0.01, 0.68), (0.28, 0.97, 0.69), (-0.72, 0.91, 0.89), (-1.21, 0.7, 0.6), (-0.36, 0.92, 1.36), (-0.43, -1.0, 0.68), (0.13, -1.05, 0.69),(-.42,.09,.90),(.13,.16,.97)],[(-0.0, 1.0, 0.0), (-0.71, 0.71, 0.0), (-1.0, -0.0, 0.0), (-0.71, -0.71, 0.0), (0.0, -1.0, 0.0), (0.71, -0.71, 0.0), (1.0, -0.0, -0.0), (0.71, 0.71, -0.01), (-1.34, 0.76, 0.99), (-1.43, 0.53, 0.47), (-1.47, -0.01, 0.25), (-1.43, -0.56, 0.48), (-1.33, -0.79, 1.0), (-1.24, -0.58, 1.51), (-1.21, -0.03, 1.72), (-1.26, 0.57, 1.53), (0.73, 1.02, 1.08), (1.08, 0.65, 0.61), (1.18, -0.07, 0.7), (1.0, -0.6, 1.16), (0.63, -0.57, 1.75), (0.35, -0.06, 2.16), (0.21, 0.62, 2.16), (0.38, 1.05, 1.67), (-0.94, -0.63, 0.26), (-1.12, -0.01, 0.09), (-0.8, -1.0, 0.78), (-0.59, -0.81, 1.45), (0.75, -0.72, 0.94), (-0.07, -0.51, 1.66), (0.84, 0.64, 0.42), (1.12, 0.01, 0.39), (0.31, 0.97, 0.63), (-0.79, 0.91, 0.69), (-0.96, 0.7, 0.25), (-0.38, 0.92, 1.37), (-0.43, -1.0, 0.69), (0.13, -1.05, 0.7),(-.98,0,.16),(.85,.16,.49)],[(25, 24, 11, 10), (15, 14, 21, 22), (2, 3, 24, 25), (12, 26, 27, 13), (12, 11, 24, 26), (20, 29, 28, 19), (20, 21, 14, 29), (14, 13, 27, 29), (31, 30, 17, 18), (30, 32, 16, 17), (7, 0, 32, 30), (6, 7, 30, 31), (18, 19, 28, 31), (8, 33, 34, 9), (9, 34, 25, 10), (1, 2, 25, 34), (15, 35, 33, 8), (23, 35, 15, 22), (35, 23, 16, 32), (33, 35, 32, 0), (34, 33, 0, 1), (5, 6, 31, 28), (36, 26, 24, 3), (37, 36, 3, 4), (4, 5, 28, 37), (27, 26, 36, 37), (28, 29, 27, 37)],[(4,37),(36,37),(26,36),(12,26),(28,37),(19,28),(14,21)])







S1 = Split([0,1,2,3,4,5,6,7],([8, 9, 10, 11, 12, 13, 14, 15],[16, 17, 18, 19, 20, 21, 22, 23]),[(0.0, 1.0, 0.0), (-0.71, 0.71, 0.0), (-1.0, -0.0, 0.0), (-0.71, -0.71, 0.0), (0.0, -1.0, 0.0), (0.71, -0.71, 0.0), (1.0, 0.0, 0.0), (0.71, 0.71, 0.0), (-0.0, -0.17, 1.01), (-0.42, -0.29, 0.88), (-0.59, -0.58, 0.58), (-0.42, -0.88, 0.29), (0.0, -1.0, 0.16), (0.42, -0.88, 0.29), (0.59, -0.58, 0.58), (0.42, -0.29, 0.88), (-0.0, 1.0, 0.17), (-0.43, 0.88, 0.29), (-0.61, 0.57, 0.6), (-0.43, 0.26, 0.9), (0.0, 0.13, 1.02), (0.43, 0.26, 0.9), (0.61, 0.57, 0.6), (0.43, 0.88, 0.29), (0.85, 0.44, 0.37), (0.91, -0.38, 0.42), (0.79, 0.04, 0.65), (0.0, -0.02, 1.02), (0.43, -0.02, 0.89), (-0.43, -0.02, 0.89), (-0.91, -0.38, 0.41), (-0.82, 0.04, 0.65), (-0.91, 0.44, 0.37),(0,-1,1),(0,1,1)],[(0.0, 1.0, 0.0), (-0.71, 0.71, 0.0), (-1.0, -0.0, 0.0), (-0.71, -0.71, 0.0), (0.0, -1.0, 0.0), (0.71, -0.71, 0.0), (1.0, 0.0, 0.0), (0.71, 0.71, 0.0), (-0.0, -0.17, 1.01), (-0.42, -0.29, 0.88), (-0.59, -0.58, 0.58), (-0.42, -0.88, 0.29), (0.0, -1.0, 0.16), (0.42, -0.88, 0.29), (0.59, -0.58, 0.58), (0.42, -0.29, 0.88), (-0.0, 1.0, 0.17), (-0.43, 0.88, 0.29), (-0.61, 0.57, 0.6), (-0.43, 0.26, 0.9), (0.0, 0.13, 1.02), (0.43, 0.26, 0.9), (0.61, 0.57, 0.6), (0.43, 0.88, 0.29), (0.85, 0.44, 0.37), (0.91, -0.38, 0.42), (0.79, 0.04, 0.65), (0.0, -0.02, 1.02), (0.43, -0.02, 0.89), (-0.43, -0.02, 0.89), (-0.91, -0.38, 0.41), (-0.82, 0.04, 0.65), (-0.91, 0.44, 0.37),(0,-1,1),(0,1,1)],[(4, 5, 13, 12), (3, 4, 12, 11), (7, 0, 16, 23), (0, 1, 17, 16), (27, 28, 21, 20), (29, 27, 20, 19), (25, 13, 5, 6), (6, 7, 23, 24), (22, 26, 24, 23), (14, 13, 25, 26), (24, 26, 25, 6), (9, 8, 27, 29), (8, 15, 28, 27), (22, 21, 28, 26), (14, 26, 28, 15), (30, 31, 32, 2), (2, 32, 17, 1), (2, 3, 11, 30), (10, 31, 30, 11), (17, 32, 31, 18), (10, 9, 29, 31), (18, 31, 29, 19)],[(4,37),(36,37),(26,36),(12,26),(28,37),(19,28),(14,21)])


Joncts = [S1,S2]



root = Module([],((1,[0, 1, 2, 3, 4, 5, 6, 7])),[Vector((0.0, 0.9928191900253296, 0.9806214570999146)), Vector((-0.7020291090011597, 0.7020291090011597, 0.9806214570999146)), Vector((-0.9928191900253296, -4.3397506033215905e-08, 0.9806214570999146)), Vector((-0.7020291090011597, -0.7020291090011597, 0.9806214570999146)), Vector((8.679501206643181e-08, -0.9928191900253296, 0.9806214570999146)), Vector((0.7020292282104492, -0.7020290493965149, 0.9806214570999146)), Vector((0.9928191900253296, 1.1839250468881346e-08, 0.9806214570999146)), Vector((0.7020292282104492, 0.7020291090011597, 0.9806214570999146)), Vector((0.0, 1.0136922597885132, 0.45493215322494507)), Vector((-0.716788649559021, 0.716788649559021, 0.45493215322494507)), Vector((-1.0136922597885132, -4.4309896196637055e-08, 0.45493215322494507)), Vector((-0.716788649559021, -0.716788649559021, 0.45493215322494507)), Vector((8.861979239327411e-08, -1.0136922597885132, 0.45493215322494507)), Vector((0.7167887687683105, -0.7167885303497314, 0.45493215322494507)), Vector((1.0136922597885132, 1.2088158918288627e-08, 0.45493215322494507)), Vector((0.7167887687683105, 0.7167885899543762, 0.45493215322494507)), Vector((0.0, 1.1711314916610718, 0.011928796768188477)), Vector((-0.8281149864196777, 0.8281149864196777, 0.011928796768188477)), Vector((-1.1711314916610718, -5.119178325685425e-08, 0.011928796768188477)), Vector((-0.8281149864196777, -0.8281149864196777, 0.011928796768188477)), Vector((1.023835665137085e-07, -1.1711314916610718, 0.011928796768188477)), Vector((0.8281151056289673, -0.8281148672103882, 0.011928796768188477)), Vector((1.1711314916610718, 1.3965602896348628e-08, 0.011928796768188477)), Vector((0.8281151056289673, 0.828114926815033, 0.011928796768188477)), Vector((0.0, 1.416882872581482, -0.3086543381214142)), Vector((-1.0018874406814575, 1.0018874406814575, -0.3086543381214142)), Vector((-1.416882872581482, -6.19339104446226e-08, -0.3086543381214142)), Vector((-1.0018874406814575, -1.0018874406814575, -0.3086543381214142)), Vector((1.238678208892452e-07, -1.416882872581482, -0.3086543381214142)), Vector((1.001887559890747, -1.0018872022628784, -0.3086543381214142)), Vector((1.416882872581482, 1.6896155585754968e-08, -0.3086543381214142)), Vector((1.001887559890747, 1.001887321472168, -0.3086543381214142))], [(7, 6, 14, 15), (5, 4, 12, 13), (3, 2, 10, 11), (1, 0, 8, 9), (0, 7, 15, 8), (6, 5, 13, 14), (4, 3, 11, 12), (2, 1, 9, 10), (9, 8, 16, 17), (8, 15, 23, 16), (14, 13, 21, 22), (12, 11, 19, 20), (10, 9, 17, 18), (15, 14, 22, 23), (13, 12, 20, 21), (11, 10, 18, 19), (16, 23, 31, 24), (22, 21, 29, 30), (20, 19, 27, 28), (18, 17, 25, 26), (23, 22, 30, 31), (21, 20, 28, 29), (19, 18, 26, 27), (17, 16, 24, 25)])



branch = Module([0, 1, 2, 3, 4, 5, 6, 7],(1,[0, 1, 2, 3, 4, 5, 6, 7]),[Vector((0.0, 1.0, 0.0)), Vector((-0.7071067690849304, 0.7071067690849304, 0.0)), Vector((-1.0, -4.371138828673793e-08, 0.0)), Vector((-0.7071067690849304, -0.7071067690849304, 0.0)), Vector((8.742277657347586e-08, -1.0, 0.0)), Vector((0.70710688829422, -0.7071066498756409, 0.0)), Vector((1.0, 1.1924880638503055e-08, 0.0)), Vector((0.70710688829422, 0.7071067094802856, 0.0))], [])


trunk = Split(
		[0,1,2,3,4,5,6,7],
		([8,9,10,11,12,13,14,15],[55, 56, 57, 58, 59, 60, 61, 62]),
		[(0.0, 1.0, -0.0), (-0.71, 0.71, -0.0), (-1.0, -0.0, -0.0), (-0.71, -0.71, -0.0), (0.0, -1.0, -0.0), (0.71, -0.71, -0.0), (1.0, 0.0, -0.0), (0.71, 0.71, -0.0), (0.0, 0.98, 1.37), (-0.69, 0.69, 1.37), (-0.98, -0.0, 1.37), (-0.75, -0.64, 1.38), (0.0, -0.91, 1.4), (0.75, -0.64, 1.38), (0.98, 0.0, 1.37), (0.69, 0.69, 1.37), (0.0, -0.95, 1.39), (-0.51, -0.89, 1.21), (-0.64, -1.01, 0.75), (-0.47, -1.22, 0.35), (0.0, -1.34, 0.25), (0.47, -1.22, 0.35), (0.64, -1.01, 0.75), (0.51, -0.89, 1.21), (0.99, -0.04, 0.17), (0.99, -0.04, 1.07), (0.7, 0.7, 1.07), (0.7, 0.7, 0.17), (0.0, -1.23, 0.15), (0.0, -0.93, 1.38), (0.66, -0.74, 1.28), (0.59, -1.03, 0.18), (-0.99, -0.0, 0.17), (-0.99, -0.0, 1.07), (-0.66, -0.74, 1.28), (-0.59, -1.03, 0.18), (0.0, 0.99, 0.17), (0.0, 0.99, 1.07), (-0.7, 0.7, 1.07), (-0.7, 0.7, 0.17), (0.96, -0.11, 0.62), (0.7, 0.7, 0.62), (0.72, -0.8, 0.63), (-0.96, -0.11, 0.62), (-0.72, -0.8, 0.63), (0.0, 0.99, 0.62), (-0.7, 0.7, 0.62), (0.0, -1.0, 1.43), (-0.43, -1.09, 1.3), (-0.6, -1.38, 0.99), (-0.41, -1.66, 0.69), (0.0, -1.78, 0.57), (0.41, -1.66, 0.69), (0.6, -1.38, 0.99), (0.43, -1.09, 1.3), (0.0, -1.08, 1.49), (-0.42, -1.23, 1.41), (-0.59, -1.6, 1.22), (-0.42, -1.98, 1.03), (0.0, -2.13, 0.95), (0.42, -1.98, 1.03), (0.59, -1.6, 1.22), (0.42, -1.23, 1.41),(0,0,1),(0,-.35,.59)],
		[(0.0, 1.0, -0.04), (-0.71, 0.71, -0.04), (-1.0, -0.0, -0.04), (-0.71, -0.71, -0.04), (0.0, -0.98, -0.04), (0.71, -0.71, -0.04), (1.0, 0.0, -0.04), (0.71, 0.71, -0.04), (0.0, 0.98, 1.31), (-0.69, 0.69, 1.31), (-0.98, -0.0, 1.31), (-0.69, -0.69, 1.31), (0.0, -0.95, 1.31), (0.69, -0.69, 1.31), (0.98, 0.0, 1.31), (0.69, 0.69, 1.31), (0.0, -1.02, 1.24), (-0.45, -0.95, 1.07), (-0.59, -0.91, 0.63), (-0.46, -0.96, 0.2), (0.0, -1.03, 0.02), (0.46, -0.96, 0.2), (0.59, -0.91, 0.63), (0.45, -0.95, 1.07), (0.99, -0.04, 0.17), (0.99, -0.04, 1.07), (0.7, 0.7, 1.07), (0.7, 0.7, 0.17), (0.0, -0.99, -0.01), (0.0, -0.99, 1.25), (0.59, -0.85, 1.14), (0.6, -0.85, 0.11), (-0.99, -0.0, 0.17), (-0.99, -0.0, 1.07), (-0.59, -0.85, 1.14), (-0.6, -0.85, 0.11), (0.0, 0.99, 0.17), (0.0, 0.99, 1.07), (-0.7, 0.7, 1.07), (-0.7, 0.7, 0.17), (0.96, -0.11, 0.62), (0.7, 0.7, 0.62), (0.69, -0.75, 0.62), (-0.96, -0.11, 0.62), (-0.69, -0.75, 0.62), (0.0, 0.99, 0.62), (-0.7, 0.7, 0.62), (-0.0, -1.11, 1.19), (-0.39, -1.11, 1.03), (-0.55, -1.11, 0.64), (-0.39, -1.11, 0.25), (0.0, -1.1, 0.09), (0.39, -1.11, 0.25), (0.55, -1.11, 0.64), (0.39, -1.11, 1.03), (0.0, -1.27, 1.18), (-0.38, -1.27, 1.02), (-0.54, -1.26, 0.65), (-0.38, -1.25, 0.27), (0.0, -1.25, 0.11), (0.38, -1.25, 0.27), (0.54, -1.26, 0.65), (0.38, -1.27, 1.02),(0,0,1),(0,-1,0)],
		[(26, 15, 14, 25), (30, 13, 12, 29), (34, 11, 10, 33), (38, 9, 8, 37), (37, 8, 15, 26), (25, 14, 13, 30), (29, 12, 11, 34), (33, 10, 9, 38), (2, 32, 39, 1), (43, 33, 38, 46), (4, 28, 35, 3), (6, 24, 31, 5), (40, 25, 30, 42), (0, 36, 27, 7), (45, 37, 26, 41), (1, 39, 36, 0), (46, 38, 37, 45), (3, 35, 32, 2), (44, 34, 33, 43), (5, 31, 28, 4), (7, 27, 24, 6), (41, 26, 25, 40), (27, 41, 40, 24), (35, 44, 43, 32), (39, 46, 45, 36), (36, 45, 41, 27), (24, 40, 42, 31), (32, 43, 46, 39), (17, 34, 44, 18), (18, 44, 35, 19), (19, 35, 28, 20), (20, 28, 31, 21), (21, 31, 42, 22), (22, 42, 30, 23), (23, 30, 29, 16), (16, 29, 34, 17), (16, 47, 54, 23), (23, 54, 53, 22), (22, 53, 52, 21), (21, 52, 51, 20), (20, 51, 50, 19), (19, 50, 49, 18), (18, 49, 48, 17), (17, 48, 47, 16), (53, 54, 62, 61), (51, 52, 60, 59), (49, 50, 58, 57), (47, 48, 56, 55), (54, 47, 55, 62), (52, 53, 61, 60), (50, 51, 59, 58), (48, 49, 57, 56)],
		[(29, 12), (4, 28), (28, 20), (29, 16), (16, 47), (51, 20), (59, 51), (55, 47)])


def add_tuple(t,x):
	return tuple([x+i for i in t])


def rot_scale(v_co, scale, dir,rot_z_alea = True):
		(x,y,z) = dir
		dir = Vector((-x,-y,z))
		d = Vector((1,0))
		X = Vector((z,y))
		Y = Vector((z,x))
		a = 0 if X == Vector((0,0,0)) else d.angle_signed(X)
		b = 0 if Y == Vector((0,0,0)) else d.angle_signed(Y)
		c = (randint(0,8)/8*2*pi+random()/6) if rot_z_alea else 0		
		q = Vector((0,0,1)).rotation_difference(dir)
		mat_rot = q.to_matrix()
		mat_rot.resize_4x4()		
		Mc = Matrix.Rotation(c,4,'Z')		
		#Ma = Matrix.Rotation(-a,4,'X')
		#Mb = Matrix.Rotation(b,4,'Y')
		v_co = [((v*scale)*Mc)*mat_rot for v in v_co]
		return v_co


def joindre(verts,faces,v1_i,v2_i):
	v1 = verts[v1_i[0]]
	n = len(v1_i)
	d = float('inf')
	decalage = 0
	for i in range(n):
		d1 = (verts[v2_i[i]]- v1).length
		if d1 < d:
			d = d1
			decalage = i
	v2 = verts[v1_i[1]]
	k = 1
	if ((verts[v2_i[(decalage+1)%n]]- v2).length > (verts[v2_i[(decalage-1)%n]]- v2).length):
		k = -1		
	for i in range(n):
		faces.append([v1_i[i],v2_i[(decalage+i*k)%(n)],v2_i[(decalage+(i+1)*k)%(n)],v1_i[(i+1)%(n)]])



def join(verts,faces,indexes,object_verts,object_faces,scale,i1,i2,entree,dir,branch_length,s_index,Seams,Jonc_seams,random_angle):
	random1 = random_angle * (random()-.5)
	random2 = random_angle * (random()-.5)
	random3 = random_angle * (random()-.5)

	randX = Matrix.Rotation(random1, 4, 'X')
	randY = Matrix.Rotation(random2, 4, 'Y')
	randZ = Matrix.Rotation(random3, 4, 'Z')
	
	dir = (((dir*randX)*randY)*randZ)	
	barycentre = Vector((0,0,0))
	for i in indexes:
		barycentre += verts[i]
	barycentre/=len(indexes)
	v1 = verts[indexes[0]]-verts[indexes[len(indexes)//2]]
	v2 = verts[indexes[-1]] - verts[indexes[3]]
	#dir = v1.cross(v2)
	dir.normalize()
	barycentre+= dir*branch_length
	r1 = (object_verts[i1[0]]-object_verts[i1[4]]).length /2
	r2 = (object_verts[i2[0]]-object_verts[i2[4]]).length /2
	#print('avt',len(object_verts))
	v = rot_scale(object_verts,scale,dir)
	d2 = v[-1]
	d1 = v[-2]
	n = len(verts)
	nentree = [n+i for i in entree]
	add_seams (nentree,Seams)
	Seams+= [add_tuple(f,n) for f in Jonc_seams]
	faces += [add_tuple(f,n)for f in object_faces]
	verts+=[barycentre+i for i in v]	
	joindre(verts,faces, indexes, nentree)	
	#print(len(v))
	i1 = [n+i for i in i1]
	i2 = [n+i for i in i2]
	add_seams (i1,Seams)
	add_seams (i2,Seams)
	dist = 1000
	ns_index = 0
	for i in nentree:
		length = (verts[s_index] - verts[i]).length
		if length<dist:
			dist = length
			ns_index = i
	Seams.append((s_index,ns_index))
	return i1,i2,d1,d2,r1,r2,i1[0],i2[0]




def join_branch(verts,faces,indexes,scale,branch_length,branch_verts,dir,rand,s_index,Seams):
	barycentre = Vector((0,0,0))
	random1 = rand * (random()-.5)
	random2 = rand * (random()-.5)
	random3 = rand * (random()-.5)
	for i in indexes:
		barycentre+=verts[i]
	barycentre/=len(indexes)
	v1 = verts[indexes[0]]-verts[indexes[len(indexes)//2]]
	v2 = verts[indexes[-1]] - verts[indexes[3]]
	#dir = v1.cross(v2)
	dir.normalized()
	randX = Matrix.Rotation(random1, 4, 'X')
	randY = Matrix.Rotation(random2, 4, 'Y')
	randZ = Matrix.Rotation(random3, 4, 'Z')
	#rand = Vector((random()-.5,random()-.5,random()-.5))/4
	#dir+=rand
	dir = (((dir*randX)*randY)*randZ)
	barycentre+=dir*branch_length	
	n = len(verts)
	v = rot_scale(branch_verts,scale,dir)
	nentree = [n+i for i in range(8)]
	verts += [ve + barycentre for ve in v]
	joindre(verts,faces, indexes, nentree)
	ns_index = 0
	dist = 1000
	for i in nentree:
		length = (verts[s_index] - verts[i]).length
		if length<dist:
			dist = length
			ns_index = i	
	Seams.append((s_index,ns_index))
	return nentree,dir,ns_index



def gravity(dir,r,gravity_strength):
	v = Vector((0,0,-1))	
	norm = dir.length
	factor = (dir.cross(v)).length/norm/100*gravity_strength
	return dir+v*factor



def add_seams(indexes,seams):
	n = len(indexes)
	for i in range(n):
		seams.append((indexes[i],indexes[(i+1)%n]))



def Create_tree2(iteration,split_proba,trunk_split_proba,radius,branch_length,trunc_length,trunc_space,randomangle,radiusdec,gravity_strength,repel_force,bones_iterations,armature,uv,trunk_variation,split_angle,visualize,trunk_split_angle,preserve_trunk,trunk_end,obstacle_name,visualize_leafs,leaves_group_size):
	Trunk= preserve_trunk
	visu_verts = [Vector((0,0,0)),(Vector((0,0,1))*radius)]
	visu_edges = [(0,1)]
	Bones = []
	leafs_group = []
	leafs_start_index = 0
	J = S1
	Seams = [(0,8),(8,16),(16,24)]
	verts = []
	faces = []
	verts = [v*radius for v in root.verts]
	faces = [f for f in root.faces]
	extr = [i for i in root.sortie[1]]
	#add_seams(extr,Seams)
	#(i1,r1,i2,r2) = (J.sortie[0][3],J.sortie[0][0],J.sortie[1][3],J.sortie[1][0])
	entree = [i for i in J.entree]
	dir = Vector((0,0,1))
	Last_bone = (1,Vector((0,0,1)))
	extremites = [(extr,radius,dir,extr[0],Last_bone,Trunk)]
	
	for i in range(iteration+trunc_length):
		n = len(extremites)
		if i == iteration + trunc_length -leaves_group_size:
			leafs_start_index = len(verts)
			
		nextremites = []
		
		for E in extremites:			
			indexes,radius,dir,s_index, Lb,Trunk = E
			if i>trunk_end:
				Trunk=False
			pos = Vector((0,0,0))
			for k in indexes:
				pos += verts[k]
			pos/=len(indexes)
			dir.normalize()
			end = pos + dir*10
			
			if bpy.data.objects.get(obstacle_name) is not None:
				obs =  bpy.data.objects.get(obstacle_name)
				d = obs.data
				bpy.context.scene.update()
				(hit_pos,face_normal,face_index) = obs.ray_cast(pos,end)
				if face_index!=-1:
					force = abs(min(dir.dot(face_normal),0))*repel_force/(((hit_pos-pos).length)+1)*2
					dir += face_normal*force			
			
			split_probability = trunk_split_proba if Trunk else split_proba
			
			if i <=trunc_length:
				branch_verts = [v for v in branch.verts]
				ni,dir,nsi = join_branch(verts,faces,indexes,radius,trunc_space,branch_verts,dir,trunk_variation,s_index,Seams)
				sortie = pos + dir*branch_length
				visu_verts.append(pos + dir*branch_length)
				if i <= bones_iterations: Bones.append((Lb[0],len(Bones)+2,Lb[1],sortie))
				Nb = (len(Bones)+1,sortie)
				nextremites.append((ni,radius*.98,dir,nsi,Nb,Trunk))	
						
			elif (i == trunc_length+1) or (random()< split_probability):
				variation = trunk_variation if Trunk else randomangle
				randJ = 1 
				J = Joncts[randJ] if (not(Trunk)) else trunk
				i1 = [i for i in J.sortie[0]]
				i2 = [i for i in J.sortie[1]]
				Jonct_seams = [s for s in J.Seams]
				
				#print(indexes)
				inter_fact = trunk_split_angle if Trunk else split_angle
				Jonct_verts = interpolate(J.verts1,J.verts2,inter_fact)
				Jonct_faces = [f for f in J.faces]
				Length = trunc_space if Trunk else branch_length
				ni1,ni2,dir1,dir2,r1,r2,nsi1,nsi2 = join(verts,faces,indexes,Jonct_verts,J.faces,radius*(1+radiusdec)/2,i1,i2,entree,dir,Length,s_index,Seams,Jonct_seams,variation)
				sortie1 = (verts[ni1[0]]+verts[ni1[4]])/2
				sortie2 = (verts[ni2[0]]+verts[ni2[4]])/2
				visu_verts.append(sortie1)
				visu_verts.append(sortie2)
				Nb = len(Bones)
				if i <= bones_iterations:Bones.append((Lb[0],Nb+2,Lb[1],sortie1))
				if i <= bones_iterations:Bones.append((Lb[0],Nb+3,Lb[1],sortie2))
				Nb1 = (Nb+2,sortie1)
				Nb2 = (Nb+3,sortie2)
				nextremites.append((ni1,radius*radiusdec*r1,gravity(dir1,radius,gravity_strength),nsi1,Nb1,Trunk))
				nextremites.append((ni2,radius*radiusdec*r2,gravity(dir2,radius,gravity_strength),nsi2,Nb2,False))
			else:
				branch_verts = [v for v in branch.verts]
				variation = trunk_variation if Trunk else randomangle
				Length = trunc_space if Trunk else branch_length
				ni,dir,nsi = join_branch(verts,faces,indexes,radius,Length,branch_verts,dir,variation,s_index,Seams)
				sortie = pos + dir*branch_length
				visu_verts.append(sortie)
				if i <= bones_iterations:Bones.append((Lb[0],len(Bones)+2,Lb[1],sortie))
				Nb = (len(Bones)+1,sortie)
				nextremites.append((ni,radius*radiusdec,gravity(dir,radius,gravity_strength),nsi,Nb,Trunk))
						
		extremites = nextremites	
	
	mesh = bpy.data.meshes.new("tree")
	if visualize:
		mesh.from_pydata(visu_verts,[], [])
		mesh.update(calc_edges=False)
		object = bpy.data.objects.new("tree", mesh)
		#object.location = bpy.context.scene.cursor_location
		object.location = (0,0,0)
		bpy.context.scene.objects.link(object)
	
	else :
		mesh.from_pydata(verts,[], faces)
		mesh.update(calc_edges=False)
		object = bpy.data.objects.new("tree", mesh)
		#object.location = bpy.context.scene.cursor_location
		object.location = (0,0,0)
		bpy.context.scene.objects.link(object)
		bpy.context.scene.objects.active = object
		g = object.vertex_groups.new("leaf")
		vgroups = object.vertex_groups
		vgroups.active_index = vgroups["leaf"].index
		

			
		#print(leafs_start_index)
		g.add([i for i in range (leafs_start_index,len(verts))], 1.0, "ADD")
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_all(action='SELECT') 
		bpy.ops.mesh.normals_make_consistent(inside=False)
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.mesh.select_mode(type="EDGE")	
		bpy.ops.object.editmode_toggle()
	
	if uv and not(visualize):		
		Test = [[False,[]] for i in range(len(verts))]
		for (a,b) in Seams:
			a,b = min(a,b),max(a,b)
			Test[a][0] = True
			Test[b][0] = True
			Test[a][1].append(b)
			Test[b][1].append(a)
		for e in mesh.edges:
			v0,v1 = e.vertices[0],e.vertices[1]
			if Test[v0][0] and v1 in Test[v0][1] :
				e.select = True
		bpy.ops.object.editmode_toggle()
		bpy.ops.mesh.mark_seam(clear=False)
		bpy.ops.mesh.select_all(action='SELECT') 
		bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
		bpy.ops.object.editmode_toggle()
	
	if armature and not(visualize):		
		bpy.ops.object.add(
			type='ARMATURE', 
			enter_editmode=True,
			location=Vector((0,0,0)))
		arm = bpy.context.object
		arm.show_x_ray = True
		amt = arm.data
		arm.data.draw_type = 'STICK'
		bone = amt.edit_bones.new('1')
		bone.head = Vector((0,0,0))
		bone.tail = Vector((0,0,1))
		last = '0'
		#print([(b[0],b[1]) for b in Bones])
		for (pname,name,h,t) in Bones:		
			last = pname
			bone = amt.edit_bones.new(str(name))	
			bone.parent = arm.data.edit_bones[str(pname)]
			bone.use_connect = True
			bone.head = h
			bone.tail = t
		bpy.ops.object.editmode_toggle()
		bpy.ops.object.select_all(action='DESELECT')
		object.select = True
		arm.select = True
		bpy.context.scene.objects.active = arm
		bpy.ops.object.parent_set(type='ARMATURE_AUTO')
		bpy.ops.object.select_all(action='DESELECT')
	
	if visualize_leafs:
		object.select = True
		bpy.context.scene.objects.active = object
		vgroups.active_index = vgroups["leaf"].index
		bpy.ops.paint.weight_paint_toggle()



class make_tree(bpy.types.Operator):
	"""Make a tree"""
	bl_idname = "object.add_tree"
	bl_label = "Add_modular_tree"
	bl_options = {"REGISTER","UNDO"}
	
	
	
	preserve_trunk = BoolProperty(
			name = "preserve trunk",default = False,
            description = "preserves the trunk growth, check and see.")
	
	trunk_split_angle = FloatProperty(
			name= "trunk split angle",
			min = 0.0,
			max = 1,			
			default=0,
			description="how wide is the angle in a split if this split comes from the trunk",
			)	
	randomangle = FloatProperty(
			name = "Branches variations",
			default = .5,
			)
	trunk_variation = FloatProperty(
			name = "trunk variation",
			default = .1,
			)		

	radius = FloatProperty(
			name = "Radius",
			min = 0.01,
			default = 1,
			)
	radius_dec = FloatProperty(
			name = "radius decrease",
			min = 0.01,
			max = 1.0,
			default = 0.95,
			description = "relative radius after each iteration, low value means fast radius decrease")

	iteration = IntProperty(
			name= "branch iterations",
			min = 1,			
			default=20,
			)
	
	preserve_end = IntProperty(
			name = "trunk end",
			min = 0,
			default = 25,
            description = "iteration on which trunk preservation will end")
	
	trunk_length = IntProperty(
			name= "trunk iteration",
			min = 0,			
			default=9,
			description="iteration from from which first split occures",
			)
	trunk_split_proba = FloatProperty(
			name = "trunk split probability",
			min = 0.0,
			max = 1.0,
			default = 0.5,
			description = "probability for a branch to split. WARNING : sensitive",
			)

	split_proba = FloatProperty(
			name = "split probability",
			min = 0.0,
			max = 1.0,
			default = 0.25,
			description = "probability for a branch to split. WARNING : sensitive",
			)
	trunk_space = FloatProperty(
			name= "trunk_length",
			min = 0.01,			
			default=.7,
			description="trunk length",
			)

	branch_length = FloatProperty(
			name= "branch_length",
			min = 0.01,			
			default=.7,
			description="branch length",
			)
	split_angle = FloatProperty(
			name= "split angle",
			min = 0.0,
			max = 1,	
			default=.2,
			description="how wide is the angle in a split",
			)
	
	gravity_strength = FloatProperty(
			name = "gravity factor",
			default = 0.0,
			)
	
	obstacle = StringProperty(
			name = 'obstacle name',
			default = '',
            description = "the name of the obstacle to avoid. WARNING: location,rotaion and scale must be applied. Check the normals.")
			
	obstacle_strength = FloatProperty(
			name = "obstacle avoidance strength",
			default = 1)
	
	SeedProp = IntProperty(
			name = "Seed",
			default = randint(0,1000),
			)
	
	Create_armature = BoolProperty(
			name = 'create armature',
			default = False)
	
	Armature_iterations = IntProperty(
			name = 'armature iterations',
			default = 8)
	
	visualize_leafs = BoolProperty(
			name = 'visualize leaves weight group',
			default = False)
	
	leaves_group_size = IntProperty(
			name = 'leaves_vertex_group_size',min = 1,
			default = 4)
	
	uv = BoolProperty(
			name = "unwrap",
			default = False,
            description = "unwrap tree. WARNING: takes time, check last")
	
	
                                   
	
	def draw(self, context):
		layout = self.layout
		#layout.prop(self, "chooseSet", expand=True)  
		scene = context.scene
		box = layout.box()
		box.label("basic")
		box.prop(self, "SeedProp")
		box.prop(self, "iteration")
		box.prop(self,'radius')
		box.prop(self,'radius_dec')
		
		box = layout.box()
		box.label("Trunk")
		box.prop(self,'trunk_length')
		box.prop(self,'trunk_variation')
		box.prop(self,'trunk_space')
		sbox = box.box()
		sbox.prop(self,'preserve_trunk')
		sbox.prop(self,'preserve_end')
		sbox.prop(self,'trunk_split_proba')
		sbox.prop(self,'trunk_split_angle')
		
		box = layout.box()
		box.label("branches")
		box.prop(self,'branch_length')
		box.prop(self,'randomangle')
		box.prop(self,'split_proba')
		box.prop(self,'split_angle')
		
		box = layout.box()
		box.prop(self,'gravity_strength')
		box.prop(self,'obstacle')
		box.prop(self,'obstacle_strength')
		
		box = layout.box()
		col = box.column()
		col.prop(self, 'Create_armature')
		col.prop(self, 'Armature_iterations')
		col = box.column()
		col.prop(self, 'visualize_leafs')
		col.prop(self, 'leaves_group_size')
		box.prop(self,'uv')
		
	
	
	def execute(self,context):
		seed(self.SeedProp)
		Create_tree2(self.iteration,self.split_proba, self.trunk_split_proba,self.radius,self.branch_length,self.trunk_length,self.trunk_space,self.randomangle,self.radius_dec,self.gravity_strength,self.obstacle_strength,self.Armature_iterations,self.Create_armature,self.uv,self.trunk_variation,self.split_angle,False,self.trunk_split_angle,self.preserve_trunk,self.preserve_end,self.obstacle,self.visualize_leafs,self.leaves_group_size)
		return {'FINISHED'}
	

def add_tree_button(self, context):
    self.layout.operator(
        make_tree.bl_idname,
        text="Add Modular tree",
        icon='PLUGIN')



def register():
    bpy.utils.register_class(make_tree)
    bpy.types.INFO_MT_mesh_add.append(add_tree_button)


def unregister():
    bpy.utils.unregister_class(make_tree)
    bpy.types.INFO_MT_mesh_add.remove(add_tree_button)


if __name__ == "__main__":
    register()