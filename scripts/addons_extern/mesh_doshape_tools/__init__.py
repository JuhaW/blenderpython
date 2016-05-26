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

bl_info = {
    "name": "doshape Mesh tools",
    "author": "yhoyo (Diego Quevedo",
    "version": (1, 0, 1),
    "blender": (2, 7, 3),
    "category": "Mesh",
    "location": "View3D > EditMode > ToolShelf",
    "wiki_url": "",
    "tracker_url": ""
}


if "bpy" in locals():
    import imp

import bpy
from mesh_doshape_tools.CoDEmanX_pivote import VIEW3D_OT_pivot_point_set, VIEW3D_MT_pivot_point_set
from mesh_doshape_tools.origami_symbols import OBJECT_OT_add_object
from mesh_doshape_tools.OrigamiPanel import opendoshapeurloperator, opendoshapeurlPanel, SeleccionarPanel, ObjetosPanel, FuncionesPanel, DoblarPanel, DoblarbPanel, MundoPanel, MarcasPanel, LineasPanel, RenderPanel, ParamodificarPanel  # MaterialPanel, MaterialesPanel,
from mesh_doshape_tools.lines_origami_freestyle import MontanaOperator, delMontanaOperator, delCreaseOperator, CreaseOperator

from mesh_doshape_tools.separar_unir_caras import SeparaConectaOperator, SeparaConectaOperatorPanel
from mesh_doshape_tools.join_explote import JoinExploteOperator, JoinExploteOperatorPanel
from mesh_doshape_tools.mover import MoverVerticesOperator, MoverVerticesOperatorPanel

from mesh_doshape_tools.HideShow import HideShowOperator, HideShowOperatorPanel
from mesh_doshape_tools.NirenYang_mesh_edges_length_angle_yi import LengthSet, AngleSet
from mesh_doshape_tools.equal_angles import angleBisectorOperator, angleBisectorOperatorPanel
#from mesh_doshape_tools.degree_angle_bisector import DegreeBisectorOperator, DegreeBisectorOperatorPanel
from mesh_doshape_tools.perpendicular_bisector import PerpendicularBisectorOperator, PerpendicularBisectorOperatorPanel
from mesh_doshape_tools.perpendicular_orthocenter import PerpendicularOrthoOperator, PerpendicularOrthoOperatorPanel
from mesh_doshape_tools.perpendicular_circum_center import PerpendicularCircumOperator, PerpendicularCircumOperatorPanel
from mesh_doshape_tools.join_bisector import JoinBisectorOperator, JoinBisectorOperatorPanel
from mesh_doshape_tools.triangle_bisector import TriangleBisectorOperator, TriangleBisectorOperatorPanel
from mesh_doshape_tools.edge_length_equalizer import Edge_Equalizer_LengthOperator, Edge_Equalizer_LengthOperatorPanel

from mesh_doshape_tools.render_save_all import Render_Save_ScenesOperator, Render_Save_ScenesOperatorPanel


doshape_classes = (
    [VIEW3D_OT_pivot_point_set, "Operador pivote"],
    [VIEW3D_MT_pivot_point_set, "menu pivote"],
    [opendoshapeurloperator, "Operador url"],
    [OBJECT_OT_add_object, "add origami symbol"],

    [opendoshapeurlPanel, "Menu url"],
    [SeleccionarPanel, "test"],
    [ObjetosPanel, "test"],
    [FuncionesPanel, "test"],
    [DoblarPanel, "test"],
    [DoblarbPanel, "test"],
    [MundoPanel, "test"],
    [MarcasPanel, "test"],
    [LineasPanel, "test"],
    [RenderPanel, "test"],

    [Render_Save_ScenesOperator, "test"],
    [Render_Save_ScenesOperatorPanel, "test"],

    #[MaterialPanel, "test"],
    #[MaterialesPanel, "test"],
    [ParamodificarPanel, "test"],

    [SeparaConectaOperator, "separa caras operador"],
    [SeparaConectaOperatorPanel, "panel separar caras"],

    [MoverVerticesOperator, "mueve vertices operador"],
    [MoverVerticesOperatorPanel, "panel de mover vertices"],

    [JoinExploteOperator, "explota caras operador"],
    [JoinExploteOperatorPanel, "Une separa caras"],

    [LengthSet, "largo borde"],
    [AngleSet, "angulo borde"],
    [MontanaOperator, "linea montaña"],
    [delMontanaOperator, "borrar montaña"],
    [delCreaseOperator, "linea crease"],
    [CreaseOperator, "borrar linea crease"],

    [HideShowOperator, "ocultar mostrar inverso operador"],
    [HideShowOperatorPanel, "ocultar mostrar inverso panel"],

    [angleBisectorOperator, "divide angulo en partes iguales"],
    [angleBisectorOperatorPanel, "dibuja panel para equally_angle"],
    #	[DegreeBisectorOperator, "divide la malla en un angulo indicado"],
    #	[DegreeBisectorOperatorPanel, "dibuja panel para DegreeBisectorOperator"],
    [PerpendicularBisectorOperator, "divide la malla en un angulos de 90 desde los vertices"],
    [PerpendicularBisectorOperatorPanel, "divide la malla en un angulo indicado"],
    [PerpendicularOrthoOperator, "Dibuja las lineas a 90 grados para formar Orthocentros"],
    [PerpendicularOrthoOperatorPanel, "Dibuje el panel de Ortocentro"],
    [PerpendicularCircumOperator, "Dibuja las lineas a 90 grados para formar circumcentros"],
    [PerpendicularCircumOperatorPanel, "Dibuja el panel de Circumcentro"],
    [JoinBisectorOperator, "Une dos vertices y divide la malla"],
    [JoinBisectorOperatorPanel, "Del panel de Join"],
    [TriangleBisectorOperator, "Triangle bisector"],
    [TriangleBisectorOperatorPanel, "Dibuja el panel del trianglebisector"],
    [Edge_Equalizer_LengthOperator, "edge equalizer operator"],
    [Edge_Equalizer_LengthOperatorPanel, "Edge Equalizer panel"]

)


def menu_func(self, context):
    for i, text in doshape_classes:
        self.layout.operator(i.bl_idname, text=text)


def register():

    try:
        for i, _ in doshape_classes:

            try:
                bpy.utils.register_class(i)
            except:
                print("error al registrar: " + str(i))
    except:
        print("imposible registrar modulos")


def unregister():

    try:
        for i, _ in doshape_classes:

            try:
                bpy.utils.unregister_class(i)
            except:
                print("error al desregistrar: " + str(i))
    except:
        print("imposible esregistrar modulos")

if __name__ == "__main__":
    register()
