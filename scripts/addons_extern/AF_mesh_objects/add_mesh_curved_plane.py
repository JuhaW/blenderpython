bl_info = {
"name": "curved_plane", 
"author": "Gert De Roost",
"version": (1, 0, 0),
"blender": (2, 65, 0),
"location": "Add > Mesh",
"description": "Create curved_plane primitive",
"warning": "",
"wiki_url": "",
"tracker_url": "",
"category": "Add Mesh"}


if "bpy" in locals():
       import imp


import bpy
import bmesh
import math
from mathutils import *
from bpy_extras.object_utils import AddObjectHelper, object_data_add



class curved_plane(bpy.types.Operator, AddObjectHelper):
    bl_idname = "mesh.curved_plane"
    bl_label = "curved_plane"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "add curved_plane primitive"

    def execute(self, context, event):

        mesh = bpy.data.meshes.new(name="curved_plane")
        obj = bpy.data.objects.new(name="curved_plane", object_data=mesh)
        scene = bpy.context.scene
        scene.objects.link(obj)
        obj.location = scene.cursor_location
        bm = bmesh.new()
        bm.from_mesh(mesh)

        idxlist = []
        vertlist = [(-1.099441409111023, -0.9560139179229736, 0.614570140838623), (-1.0339995622634888, -0.9560725092887878, 0.4647560715675354), (-1.0998492240905762, -0.8617904186248779, 0.6159025430679321), (-1.1549675464630127, -0.955838143825531, 0.774651825428009), (-1.0982179641723633, -0.9922654628753662, 0.6105729937553406), (-1.0339995622634888, -0.992499828338623, 0.4647560715675354), (-1.0339994430541992, -0.8617904782295227, 0.4647560715675354), (-1.1565988063812256, -0.8617904186248779, 0.7799813747406006), (-1.1500738859176636, -0.9915623664855957, 0.7586631774902344), (0.505859375, -0.9560139775276184, 0.0), (0.2812499701976776, -0.9560725688934326, 0.0), (0.5, -0.9922655820846558, 0.0), (0.7421875, -0.9558383226394653, 0.0), (0.5078125, -0.8617905974388123, 0.0), (0.2812499701976776, -0.8617905378341675, 0.0), (0.2812499701976776, -0.9924998879432678, 0.0), (0.71875, -0.9915624856948853, 0.0), (0.75, -0.861790657043457, 0.0), (-0.24218755960464478, -0.9560725688934326, 0.004192915745079517), (-0.3750000596046448, -0.9560725688934326, 0.01677166298031807), (-0.24218755960464478, -0.9924998879432678, 0.004192915745079517), (-0.09375005960464478, -0.9560725688934326, 0.0), (-0.24218755960464478, -0.8617905378341675, 0.004192915745079517), (-0.3750000596046448, -0.8617905378341675, 0.01677166298031807), (-0.37500008940696716, -0.9924998879432678, 0.01677166298031807), (-0.09375006705522537, -0.9924999475479126, 0.0), (-0.09375005215406418, -0.8617905378341675, 0.0), (-0.7454500794410706, -0.9560725688934326, 0.14483235776424408), (-0.8567999601364136, -0.9560725688934326, 0.22712451219558716), (-0.7454501390457153, -0.9924998879432678, 0.14483235776424408), (-0.6250001192092896, -0.9560725688934326, 0.08385831117630005), (-0.7454500198364258, -0.8617905378341675, 0.14483235776424408), (-0.8567999601364136, -0.8617905378341675, 0.22712451219558716), (-0.8568000197410583, -0.9924998879432678, 0.22712451219558716), (-0.6250001192092896, -0.9924999475479126, 0.08385831117630005), (-0.6250001192092896, -0.8617905378341675, 0.08385831117630005), (-1.099848985671997, -0.028408333659172058, 0.6159025430679321), (-1.0339993238449097, -0.028408333659172058, 0.4647560715675354), (-1.099848747253418, 0.3289690613746643, 0.6159025430679321), (-1.1565985679626465, -0.028408333659172058, 0.7799813151359558), (-1.0998491048812866, -0.38395291566848755, 0.6159025430679321), (-1.0339994430541992, -0.38395291566848755, 0.4647560715675354), (-1.0339992046356201, 0.3289690613746643, 0.4647560715675354), (-1.156598448753357, 0.3289690613746643, 0.7799813747406006), (-1.156598687171936, -0.38395291566848755, 0.7799813151359558), (-1.0994409322738647, 0.9274912476539612, 0.614570140838623), (-1.0339990854263306, 0.9276643991470337, 0.4647560715675354), (-1.098217487335205, 0.977145254611969, 0.6105729937553406), (-1.1549670696258545, 0.9269717931747437, 0.7746517658233643), (-1.099848747253418, 0.8214690685272217, 0.6159025430679321), (-1.0339990854263306, 0.8214690685272217, 0.4647560715675354), (-1.0339990854263306, 0.977837860584259, 0.4647560715675354), (-1.1500734090805054, 0.9750674962997437, 0.7586631774902344), (-1.1565983295440674, 0.8214691281318665, 0.7799813151359558), (0.5058594346046448, 0.9274909496307373, 0.0), (0.7421875596046448, 0.926971435546875, 0.0), (0.5000001192092896, 0.9771449565887451, 0.0), (0.28125014901161194, 0.9276641607284546, 0.0), (0.5078126192092896, 0.8214687705039978, 0.0), (0.75, 0.821468710899353, 0.0), (0.7187500596046448, 0.975067138671875, 0.0), (0.28125014901161194, 0.9778375625610352, 0.0), (0.28125011920928955, 0.8214688301086426, 0.0), (0.5078125, -0.028408562764525414, 0.0), (0.2812500298023224, -0.028408527374267578, 0.0), (0.5078125, -0.3839530944824219, 0.0), (0.75, -0.028408601880073547, 0.0), (0.5078125, 0.3289687931537628, 0.0), (0.2812500596046448, 0.3289688229560852, 0.0), (0.28125, -0.3839530646800995, 0.0), (0.75, -0.38395315408706665, 0.0), (0.75, 0.32896876335144043, 0.0), (-0.2421872913837433, 0.9276642799377441, 0.004192915745079517), (-0.3749997615814209, 0.9276642799377441, 0.01677166298031807), (-0.24218732118606567, 0.8214689493179321, 0.004192915745079517), (-0.09374980628490448, 0.9276641607284546, 0.0), (-0.2421872913837433, 0.9778376817703247, 0.004192915745079517), (-0.3749997615814209, 0.9778377413749695, 0.01677166298031807), (-0.3749997913837433, 0.8214689493179321, 0.01677166298031807), (-0.09374982863664627, 0.8214688897132874, 0.0), (-0.09374980628490448, 0.9778376817703247, 0.0), (-0.24218744039535522, -0.02840844728052616, 0.004192915745079517), (-0.3749999403953552, -0.028408430516719818, 0.01677166298031807), (-0.2421875, -0.3839530050754547, 0.004192915745079517), (-0.09374994784593582, -0.028408467769622803, 0.0), (-0.24218738079071045, 0.32896894216537476, 0.004192915745079517), (-0.37499988079071045, 0.32896894216537476, 0.01677166298031807), (-0.375, -0.3839529752731323, 0.01677166298031807), (-0.09375, -0.3839530348777771, 0.0), (-0.09374989569187164, 0.32896891236305237, 0.0), (-0.7454496622085571, 0.9276643991470337, 0.14483235776424408), (-0.8567996025085449, 0.9276643991470337, 0.22712451219558716), (-0.7454497218132019, 0.8214690685272217, 0.14483235776424408), (-0.6249997615814209, 0.9276643395423889, 0.08385831117630005), (-0.7454497218132019, 0.9778378009796143, 0.14483235776424408), (-0.8567996025085449, 0.9778378009796143, 0.22712451219558716), (-0.8567996025085449, 0.8214690685272217, 0.22712451219558716), (-0.6249997615814209, 0.8214690089225769, 0.08385831117630005), (-0.6249997615814209, 0.9778378009796143, 0.08385831117630005), (-0.7454499006271362, -0.02840837650001049, 0.14483235776424408), (-0.856799840927124, -0.028408363461494446, 0.22712451219558716), (-0.745449960231781, -0.38395294547080994, 0.14483235776424408), (-0.6249999403953552, -0.028408393263816833, 0.08385831117630005), (-0.7454499006271362, 0.32896900177001953, 0.14483235776424408), (-0.8567997217178345, 0.32896900177001953, 0.22712451219558716), (-0.856799840927124, -0.38395294547080994, 0.22712451219558716), (-0.625, -0.3839529752731323, 0.08385831117630005), (-0.6249998807907104, 0.32896900177001953, 0.08385831117630005), (-1.0339990854263306, 1.000000238418579, 0.4647560715675354), (-1.0965862274169922, 0.9986151456832886, 0.6052435040473938), (-1.1435484886169434, 0.9944597482681274, 0.7373450994491577), (-1.0339995622634888, -0.9999998807907104, 0.4647560715675354), (-1.0965867042541504, -0.999531090259552, 0.6052435040473938), (-1.1435489654541016, -0.9981248378753662, 0.7373450994491577), (0.6875, -0.9981249570846558, 0.0), (0.4921874701976776, -0.9995311498641968, 0.0), (0.2812499403953552, -0.9999998807907104, 0.0), (0.6875000596046448, 0.994459331035614, 0.0), (0.49218761920928955, 0.9986148476600647, 0.0), (0.28125014901161194, 1.0, 0.0), (-0.09375007450580597, -0.9999998807907104, 0.0), (-0.24218758940696716, -0.9999998807907104, 0.004192915745079517), (-0.37500011920928955, -0.9999998807907104, 0.01677166298031807), (-0.8568000197410583, -0.9999998807907104, 0.22712452709674835), (-0.7454501390457153, -0.9999998807907104, 0.14483235776424408), (-0.6250001192092896, -0.9999998807907104, 0.08385831117630005), (-0.09374980628490448, 1.000000238418579, 0.0), (-0.2421872913837433, 1.000000238418579, 0.004192915745079517), (-0.3749997615814209, 1.000000238418579, 0.01677166298031807), (-0.8567996025085449, 1.000000238418579, 0.22712452709674835), (-0.7454496622085571, 1.000000238418579, 0.14483235776424408), (-0.6249997019767761, 1.000000238418579, 0.08385831117630005), (0.9375, -0.9906250238418579, 0.0), (0.984375, -0.9556038975715637, 0.0), (1.0, -0.861790657043457, 0.0), (-0.9544998407363892, -0.8617905378341675, 0.3330079913139343), (-0.9544998407363892, -0.9560725092887878, 0.3330079913139343), (-0.9544998407363892, -0.992499828338623, 0.3330079913139343), (-1.1957485675811768, -0.9906248450279236, 0.9078900218009949), (-1.205535888671875, -0.9556037187576294, 0.9398671984672546), (-1.2087984085083008, -0.8617904186248779, 0.950526237487793), (0.07812495529651642, -0.8617905378341675, 0.0), (0.07812495529651642, -0.9560725688934326, 0.0), (0.07812494784593582, -0.9924999475479126, 0.0), (-0.5000001192092896, -0.8617905378341675, 0.041929155588150024), (-0.5000001192092896, -0.9560725688934326, 0.041929155588150024), (-0.5000001192092896, -0.9924999475479126, 0.041929155588150024), (-1.0339994430541992, -0.6807263493537903, 0.4647560715675354), (-1.0998492240905762, -0.6807263493537903, 0.6159025430679321), (-1.1565988063812256, -0.6807263493537903, 0.7799813151359558), (0.2812499701976776, -0.6807265281677246, 0.0), (0.5078125, -0.6807265281677246, 0.0), (0.75, -0.6807265877723694, 0.0), (-0.3750000596046448, -0.6807264089584351, 0.01677166298031807), (-0.2421875298023224, -0.6807264089584351, 0.004192915745079517), (-0.09375003725290298, -0.6807265281677246, 0.0), (-0.8567999005317688, -0.6807264089584351, 0.22712451219558716), (-0.7454500794410706, -0.6807264089584351, 0.14483235776424408), (-0.6250001192092896, -0.6807264089584351, 0.08385831117630005), (1.0, 0.821468710899353, 0.0), (0.984375, 0.926278829574585, 0.0), (0.9375, 0.9722968339920044, 0.0), (1.0, 0.32896870374679565, 0.0), (1.0, -0.028408639132976532, 0.0), (1.0, -0.38395315408706665, 0.0), (-0.9544996619224548, -0.38395294547080994, 0.3330079913139343), (-0.9544996023178101, -0.028408348560333252, 0.3330079913139343), (-0.9544994831085205, 0.3289690315723419, 0.3330079913139343), (-0.954499363899231, 0.8214690685272217, 0.3330079913139343), (-0.954499363899231, 0.9276643991470337, 0.3330079913139343), (-0.954499363899231, 0.9778378009796143, 0.3330079913139343), (-1.2087979316711426, 0.8214691281318665, 0.950526237487793), (-1.2055354118347168, 0.9262793064117432, 0.9398671984672546), (-1.1957480907440186, 0.972297191619873, 0.9078900218009949), (-1.2087980508804321, 0.3289690613746643, 0.950526237487793), (-1.2087981700897217, -0.02840832620859146, 0.950526237487793), (-1.2087982892990112, -0.38395291566848755, 0.950526237487793), (0.078125, -0.3839530348777771, 0.0), (0.07812504470348358, -0.02840849757194519, 0.0), (0.07812508940696716, 0.3289688527584076, 0.0), (0.07812514901161194, 0.8214688301086426, 0.0), (0.07812516391277313, 0.9276641607284546, 0.0), (0.07812516391277313, 0.9778375625610352, 0.0), (-0.5, -0.3839529752731323, 0.041929155588150024), (-0.4999999403953552, -0.028408410027623177, 0.041929155588150024), (-0.49999985098838806, 0.32896897196769714, 0.041929155588150024), (-0.4999997615814209, 0.8214690089225769, 0.041929155588150024), (-0.4999997615814209, 0.9276643395423889, 0.041929155588150024), (-0.4999997615814209, 0.9778377413749695, 0.041929155588150024), (-1.0339990854263306, 0.631240963935852, 0.4647560715675354), (-1.099848747253418, 0.631240963935852, 0.6159025430679321), (-1.1565983295440674, 0.631240963935852, 0.7799813151359558), (0.75, 0.6312406063079834, 0.0), (0.5078125596046448, 0.6312406659126282, 0.0), (0.28125008940696716, 0.6312406659126282, 0.0), (-0.09374985098838806, 0.6312407851219177, 0.0), (-0.24218733608722687, 0.6312408447265625, 0.004192915745079517), (-0.3749998211860657, 0.6312408447265625, 0.01677166298031807), (-0.8567996025085449, 0.6312409043312073, 0.22712451219558716), (-0.7454497814178467, 0.6312409043312073, 0.14483235776424408), (-0.6249997615814209, 0.6312409043312073, 0.08385831117630005), (0.84375, 0.9861483573913574, 0.0), (0.84375, -0.9953124523162842, 0.0), (-0.9544998407363892, -0.9999998807907104, 0.3330080211162567), (-0.954499363899231, 1.000000238418579, 0.3330080211162567), (-1.1761736869812012, -0.9953123331069946, 0.8439356684684753), (-1.176173210144043, 0.9861487746238708, 0.8439356684684753), (0.07812494039535522, -0.9999998807907104, 0.0), (0.07812516391277313, 1.0000001192092896, 0.0), (-0.5000001192092896, -0.9999998807907104, 0.041929155588150024), (-0.4999997317790985, 1.000000238418579, 0.041929155588150024), (1.0, -0.6807266473770142, 0.0), (-0.9544997811317444, -0.6807264089584351, 0.3330079913139343), (-1.2087984085083008, -0.6807263493537903, 0.950526237487793), (0.07812497019767761, -0.6807265281677246, 0.0), (-0.5000000596046448, -0.6807264089584351, 0.041929155588150024), (1.0, 0.6312404870986938, 0.0), (-0.9544994831085205, 0.631240963935852, 0.3330079913139343), (-1.2087979316711426, 0.631240963935852, 0.950526237487793), (0.07812511920928955, 0.631240725517273, 0.0), (-0.4999997615814209, 0.6312408447265625, 0.041929155588150024)]
        for co in vertlist:
            v = bm.verts.new(co)
            bm.verts.index_update()
            idxlist.append(v.index)
        edgelist = [[0, 1], [1, 136], [1, 5], [4, 5], [5, 111], [5, 137], [0, 2], [2, 148], [2, 6], [1, 6], [6, 135], [6, 147], [0, 3], [3, 139], [3, 7], [2, 7], [7, 149], [7, 140], [0, 4], [4, 112], [4, 8], [3, 8], [8, 138], [8, 113], [9, 10], [10, 142], [10, 14], [13, 14], [14, 150], [14, 141], [9, 11], [11, 115], [11, 15], [10, 15], [15, 143], [15, 116], [9, 12], [12, 133], [12, 16], [11, 16], [16, 114], [16, 132], [9, 13], [13, 151], [13, 17], [12, 17], [17, 134], [17, 152], [18, 19], [19, 145], [19, 23], [22, 23], [23, 153], [23, 144], [18, 20], [20, 121], [20, 24], [19, 24], [24, 146], [24, 122], [18, 21], [21, 142], [21, 25], [20, 25], [25, 120], [25, 143], [18, 22], [22, 154], [22, 26], [21, 26], [26, 141], [26, 155], [27, 28], [28, 136], [28, 32], [31, 32], [32, 156], [32, 135], [27, 29], [29, 124], [29, 33], [28, 33], [33, 137], [33, 123], [27, 30], [30, 145], [30, 34], [29, 34], [34, 125], [34, 146], [27, 31], [31, 157], [31, 35], [30, 35], [35, 144], [35, 158], [36, 37], [37, 166], [37, 41], [40, 41], [41, 147], [41, 165], [36, 38], [38, 190], [38, 42], [37, 42], [42, 167], [42, 189], [36, 39], [39, 175], [39, 43], [38, 43], [43, 191], [43, 174], [36, 40], [40, 148], [40, 44], [39, 44], [44, 176], [44, 149], [45, 46], [46, 169], [46, 50], [49, 50], [50, 189], [50, 168], [45, 47], [47, 109], [47, 51], [46, 51], [51, 170], [51, 108], [45, 48], [48, 172], [48, 52], [47, 52], [52, 110], [52, 173], [45, 49], [49, 190], [49, 53], [48, 53], [53, 171], [53, 191], [54, 55], [55, 160], [55, 59], [58, 59], [59, 192], [59, 159], [54, 56], [56, 118], [56, 60], [55, 60], [60, 161], [60, 117], [54, 57], [57, 181], [57, 61], [56, 61], [61, 119], [61, 182], [54, 58], [58, 193], [58, 62], [57, 62], [62, 180], [62, 194], [63, 64], [64, 178], [64, 68], [67, 68], [68, 194], [68, 179], [63, 65], [65, 151], [65, 69], [64, 69], [69, 177], [69, 150], [63, 66], [66, 163], [66, 70], [65, 70], [70, 152], [70, 164], [63, 67], [67, 193], [67, 71], [66, 71], [71, 162], [71, 192], [72, 73], [73, 187], [73, 77], [76, 77], [77, 128], [77, 188], [72, 74], [74, 196], [74, 78], [73, 78], [78, 186], [78, 197], [72, 75], [75, 181], [75, 79], [74, 79], [79, 195], [79, 180], [72, 76], [76, 127], [76, 80], [75, 80], [80, 182], [80, 126], [81, 82], [82, 184], [82, 86], [85, 86], [86, 197], [86, 185], [81, 83], [83, 154], [83, 87], [82, 87], [87, 183], [87, 153], [81, 84], [84, 178], [84, 88], [83, 88], [88, 155], [88, 177], [81, 85], [85, 196], [85, 89], [84, 89], [89, 179], [89, 195], [90, 91], [91, 169], [91, 95], [94, 95], [95, 129], [95, 170], [90, 92], [92, 199], [92, 96], [91, 96], [96, 168], [96, 198], [90, 93], [93, 187], [93, 97], [92, 97], [97, 200], [97, 186], [90, 94], [94, 130], [94, 98], [93, 98], [98, 188], [98, 131], [99, 100], [100, 166], [100, 104], [103, 104], [104, 198], [104, 167], [99, 101], [101, 157], [101, 105], [100, 105], [105, 165], [105, 156], [99, 102], [102, 184], [102, 106], [101, 106], [106, 158], [106, 183], [99, 103], [103, 199], [103, 107], [102, 107], [107, 185], [107, 200], [204, 108], [108, 109], [109, 110], [110, 206], [203, 111], [111, 112], [112, 113], [113, 205], [202, 114], [114, 115], [115, 116], [116, 207], [201, 117], [117, 118], [118, 119], [119, 208], [207, 120], [120, 121], [121, 122], [122, 209], [203, 123], [123, 124], [124, 125], [125, 209], [208, 126], [126, 127], [127, 128], [128, 210], [204, 129], [129, 130], [130, 131], [131, 210], [202, 132], [132, 133], [133, 134], [134, 211], [212, 135], [135, 136], [136, 137], [137, 203], [205, 138], [138, 139], [139, 140], [140, 213], [214, 141], [141, 142], [142, 143], [143, 207], [215, 144], [144, 145], [145, 146], [146, 209], [212, 147], [147, 148], [148, 149], [149, 213], [214, 150], [150, 151], [151, 152], [152, 211], [215, 153], [153, 154], [154, 155], [155, 214], [212, 156], [156, 157], [157, 158], [158, 215], [216, 159], [159, 160], [160, 161], [161, 201], [216, 162], [162, 163], [163, 164], [164, 211], [212, 165], [165, 166], [166, 167], [167, 217], [217, 168], [168, 169], [169, 170], [170, 204], [218, 171], [171, 172], [172, 173], [173, 206], [218, 174], [174, 175], [175, 176], [176, 213], [214, 177], [177, 178], [178, 179], [179, 219], [219, 180], [180, 181], [181, 182], [182, 208], [215, 183], [183, 184], [184, 185], [185, 220], [220, 186], [186, 187], [187, 188], [188, 210], [217, 189], [189, 190], [190, 191], [191, 218], [216, 192], [192, 193], [193, 194], [194, 219], [219, 195], [195, 196], [196, 197], [197, 220], [217, 198], [198, 199], [199, 200], [200, 220]]
        for verts in edgelist:
            try:
                bm.edges.new((bm.verts[verts[0]], bm.verts[verts[1]]))
            except:
                pass
        facelist = [(0, 4, 5, 1), (1, 5, 137, 136), (4, 112, 111, 5), (5, 111, 203, 137), (0, 1, 6, 2), (2, 6, 147, 148), (1, 136, 135, 6), (6, 135, 212, 147), (0, 2, 7, 3), (3, 7, 140, 139), (2, 148, 149, 7), (7, 149, 213, 140), (0, 3, 8, 4), (4, 8, 113, 112), (3, 139, 138, 8), (8, 138, 205, 113), (9, 13, 14, 10), (10, 14, 141, 142), (13, 151, 150, 14), (14, 150, 214, 141), (9, 10, 15, 11), (11, 15, 116, 115), (10, 142, 143, 15), (15, 143, 207, 116), (9, 11, 16, 12), (12, 16, 132, 133), (11, 115, 114, 16), (16, 114, 202, 132), (9, 12, 17, 13), (13, 17, 152, 151), (12, 133, 134, 17), (17, 134, 211, 152), (18, 22, 23, 19), (19, 23, 144, 145), (22, 154, 153, 23), (23, 153, 215, 144), (18, 19, 24, 20), (20, 24, 122, 121), (19, 145, 146, 24), (24, 146, 209, 122), (18, 20, 25, 21), (21, 25, 143, 142), (20, 121, 120, 25), (25, 120, 207, 143), (18, 21, 26, 22), (22, 26, 155, 154), (21, 142, 141, 26), (26, 141, 214, 155), (27, 31, 32, 28), (28, 32, 135, 136), (31, 157, 156, 32), (32, 156, 212, 135), (27, 28, 33, 29), (29, 33, 123, 124), (28, 136, 137, 33), (33, 137, 203, 123), (27, 29, 34, 30), (30, 34, 146, 145), (29, 124, 125, 34), (34, 125, 209, 146), (27, 30, 35, 31), (31, 35, 158, 157), (30, 145, 144, 35), (35, 144, 215, 158), (36, 40, 41, 37), (37, 41, 165, 166), (40, 148, 147, 41), (41, 147, 212, 165), (36, 37, 42, 38), (38, 42, 189, 190), (37, 166, 167, 42), (42, 167, 217, 189), (36, 38, 43, 39), (39, 43, 174, 175), (38, 190, 191, 43), (43, 191, 218, 174), (36, 39, 44, 40), (40, 44, 149, 148), (39, 175, 176, 44), (44, 176, 213, 149), (45, 49, 50, 46), (46, 50, 168, 169), (49, 190, 189, 50), (50, 189, 217, 168), (45, 46, 51, 47), (47, 51, 108, 109), (46, 169, 170, 51), (51, 170, 204, 108), (45, 47, 52, 48), (48, 52, 173, 172), (47, 109, 110, 52), (52, 110, 206, 173), (45, 48, 53, 49), (49, 53, 191, 190), (48, 172, 171, 53), (53, 171, 218, 191), (54, 58, 59, 55), (55, 59, 159, 160), (58, 193, 192, 59), (59, 192, 216, 159), (54, 55, 60, 56), (56, 60, 117, 118), (55, 160, 161, 60), (60, 161, 201, 117), (54, 56, 61, 57), (57, 61, 182, 181), (56, 118, 119, 61), (61, 119, 208, 182), (54, 57, 62, 58), (58, 62, 194, 193), (57, 181, 180, 62), (62, 180, 219, 194), (63, 67, 68, 64), (64, 68, 179, 178), (67, 193, 194, 68), (68, 194, 219, 179), (63, 64, 69, 65), (65, 69, 150, 151), (64, 178, 177, 69), (69, 177, 214, 150), (63, 65, 70, 66), (66, 70, 164, 163), (65, 151, 152, 70), (70, 152, 211, 164), (63, 66, 71, 67), (67, 71, 192, 193), (66, 163, 162, 71), (71, 162, 216, 192), (72, 76, 77, 73), (73, 77, 188, 187), (76, 127, 128, 77), (77, 128, 210, 188), (72, 73, 78, 74), (74, 78, 197, 196), (73, 187, 186, 78), (78, 186, 220, 197), (72, 74, 79, 75), (75, 79, 180, 181), (74, 196, 195, 79), (79, 195, 219, 180), (72, 75, 80, 76), (76, 80, 126, 127), (75, 181, 182, 80), (80, 182, 208, 126), (81, 85, 86, 82), (82, 86, 185, 184), (85, 196, 197, 86), (86, 197, 220, 185), (81, 82, 87, 83), (83, 87, 153, 154), (82, 184, 183, 87), (87, 183, 215, 153), (81, 83, 88, 84), (84, 88, 177, 178), (83, 154, 155, 88), (88, 155, 214, 177), (81, 84, 89, 85), (85, 89, 195, 196), (84, 178, 179, 89), (89, 179, 219, 195), (90, 94, 95, 91), (91, 95, 170, 169), (94, 130, 129, 95), (95, 129, 204, 170), (90, 91, 96, 92), (92, 96, 198, 199), (91, 169, 168, 96), (96, 168, 217, 198), (90, 92, 97, 93), (93, 97, 186, 187), (92, 199, 200, 97), (97, 200, 220, 186), (90, 93, 98, 94), (94, 98, 131, 130), (93, 187, 188, 98), (98, 188, 210, 131), (99, 103, 104, 100), (100, 104, 167, 166), (103, 199, 198, 104), (104, 198, 217, 167), (99, 100, 105, 101), (101, 105, 156, 157), (100, 166, 165, 105), (105, 165, 212, 156), (99, 101, 106, 102), (102, 106, 183, 184), (101, 157, 158, 106), (106, 158, 215, 183), (99, 102, 107, 103), (103, 107, 200, 199), (102, 184, 185, 107), (107, 185, 220, 200)]
        bm.verts.ensure_lookup_table()
        for verts in facelist:
            vlist = []
            for idx in verts:
                vlist.append(bm.verts[idxlist[idx]])
            try:
                bm.faces.new(vlist)
            except:
                pass

        bm.to_mesh(mesh)
        mesh.update()
        bm.free()
        obj.rotation_quaternion = (Matrix.Rotation(math.radians(90), 3, 'X').to_quaternion())

        return {'FINISHED'}




def menu_item(self, context):
       self.layout.operator(curved_plane.bl_idname, text="curved_plane", icon="PLUGIN")

def register():
       bpy.utils.register_module(__name__)
       bpy.types.INFO_MT_mesh_add.append(menu_item)

def unregister():
       bpy.utils.unregister_module(__name__)
       bpy.types.INFO_MT_mesh_add.remove(menu_item)

if __name__ == "__main__":
       register()