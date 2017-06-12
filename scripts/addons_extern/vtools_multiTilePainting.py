bl_info = {
    "name": "vtools MultiTile-UDIM Painting System",
    "author": "Antonio Mendoza Salado - www.vertigostudio.es",
    "version": (0, 3, 1),
    "blender": (2, 77, 0),
    "location": "View3D > Panel Tools > Slots > Multi Painting panel (paint mode)",
    "warning": "",
    "description": "UI to paint in a non-destructive way using cycles nodes. Also it Allows MultiTile (UDIM) painting",
    "category": "Paint",
}



import bpy
import os
import math, mathutils
from bpy.props import (StringProperty,BoolProperty,IntProperty,FloatProperty,FloatVectorProperty,EnumProperty,PointerProperty)
from bpy.types import (Panel,Operator,AddonPreferences,PropertyGroup)
                       
from bpy_extras.io_utils import (ExportHelper, ImportHelper)



#-------- CREATE NODE GROUPS NEEDED--------#


def create_mtColorNode():
    
    # create a group
    mt_node = bpy.data.node_groups.new('MTPaintLayer_Color', 'ShaderNodeTree')
    
    #------- INPUTS --------------#
    
    #frame inputs
    
    mt_inputsFrame = mt_node.nodes.new('NodeFrame')
    mt_inputsFrame.label = "Inputs"
    mt_inputsFrame.name = "PL_FrameInputs"
    
    # create group inputs
    mt_colorInputs = mt_node.nodes.new('NodeGroupInput')
    
    mt_colorInputs.label = 'layer Inputs'
    mt_colorInputs.name = "PL_LayerInput"
    
    mt_colorInputs.parent = mt_inputsFrame
    
    #inputs below
    n_colorBelow = mt_node.inputs.new('NodeSocketColor','colorBelow')
    n_alphaBelow = mt_node.inputs.new('NodeSocketColor','alphaBelow')

    n_colorBelow.default_value = [0,0,0,0]
    n_alphaBelow.default_value = [0,0,0,0]

    #node color and alpha
    n_color = mt_node.inputs.new('NodeSocketColor','Color')
    n_colorAlpha = mt_node.inputs.new('NodeSocketColor','ColorAlpha')

    #node mask

    n_mask = mt_node.inputs.new('NodeSocketColor','Mask')
    n_mask.default_value = [1,1,1,1]
    
    #inputs values
    
    mt_inLayerOpacity = mt_node.nodes.new('ShaderNodeValue')
    mt_inLayerOpacity.name = "PL_InputOpacity"
    mt_inLayerOpacity.label = "Layer Opacity"
    mt_inLayerOpacity.outputs[0].default_value = 1
    mt_inLayerOpacity.parent = mt_inputsFrame
    
    mt_inMaskOpacity = mt_node.nodes.new('ShaderNodeValue')
    mt_inMaskOpacity.name = "PL_InputMaskOpacity"
    mt_inMaskOpacity.label = "Mask Opacity"
    mt_inMaskOpacity.outputs[0].default_value = 1
    mt_inMaskOpacity.parent = mt_inputsFrame
    
    #locations
    mt_colorInputs.location = (0,0)
    mt_inLayerOpacity.location = (0,-160)
    mt_inMaskOpacity.location = (0,-260)
    
    
    #---------- FILTERS -------------------
    
    #frame
    mt_filterFrame = mt_node.nodes.new('NodeFrame')
    mt_filterFrame.name = "PL_FrameClippingMaskFilters"
    mt_filterFrame.label = "Clipping Mask Filters"
    
    #reroutes
    mt_filterRerouteIN = mt_node.nodes.new('NodeReroute')
    mt_filterRerouteIN.name = "PL_filtersColorInput"
    mt_filterRerouteIN.label = "Filters Input"
    mt_filterRerouteIN.parent = mt_filterFrame
    
    mt_filterRerouteOUT = mt_node.nodes.new('NodeReroute')
    mt_filterRerouteOUT.name = "PL_filtersColorOutput"
    mt_filterRerouteOUT.label = "Filters Output"
    mt_filterRerouteOUT.parent = mt_filterFrame
    
    #locations
    mt_filterRerouteIN.location = (-50,0)
    mt_filterRerouteOUT.location = (50,0)
    mt_filterFrame.location = (300, 100)
    
    #---------- LAYER SYSTEM -------------------
    
    #frame
    mt_systemFrame = mt_node.nodes.new('NodeFrame')
    mt_systemFrame.name = "PL_FrameLayerSystem"
    mt_systemFrame.label = "Layer System"
    
    #opacity offset
    mt_opacityOffset = mt_node.nodes.new('ShaderNodeMath')
    mt_opacityOffset.name = "PL_OpacityOffset"
    mt_opacityOffset.label = "Opacity Offset"
    mt_opacityOffset.operation = "ADD"
    mt_opacityOffset.inputs[0].default_value = -1
    mt_opacityOffset.inputs[1].default_value = 0
    mt_opacityOffset.parent = mt_systemFrame
    
    
    #layer opacity
    mt_layerOpacity = mt_node.nodes.new('ShaderNodeMixRGB')
    mt_layerOpacity.name = "PL_LayerOpacity"
    mt_layerOpacity.label = "Layer Opacity"
    mt_layerOpacity.blend_type = "MIX"
    mt_layerOpacity.parent = mt_systemFrame
    
    #mask switcher
    mt_maskSwitcher = mt_node.nodes.new('ShaderNodeMixRGB')
    mt_maskSwitcher.name = "PL_MaskSwitcher"
    mt_maskSwitcher.label = "Mask Switcher"
    mt_maskSwitcher.blend_type = "MIX"
    mt_maskSwitcher.inputs["Color1"].default_value = [1,1,1,1]
    mt_maskSwitcher.parent = mt_systemFrame
    
    #masks adition
    mt_masksAdition = mt_node.nodes.new('ShaderNodeMixRGB')
    mt_masksAdition.name = "PL_MaskAddition"
    mt_masksAdition.label = "Masks"
    mt_masksAdition.blend_type = "MULTIPLY"
    mt_masksAdition.inputs["Fac"].default_value = 1
    mt_masksAdition.parent = mt_systemFrame
    
    #masks opacity
    mt_masksOpacity = mt_node.nodes.new('ShaderNodeBrightContrast')
    mt_masksOpacity.name = "PL_MaskOpacity"
    mt_masksOpacity.label = "Mask Opacity"
    mt_masksOpacity.inputs["Contrast"].default_value = 0
    mt_masksOpacity.parent = mt_systemFrame
    
    #locations
    mt_systemFrame.location = (400,0)
    mt_opacityOffset.location = (0,0)
    mt_layerOpacity.location = (160,0)
    mt_maskSwitcher.location = (0,-200)
    mt_masksAdition.location = (160,-200)
    mt_masksOpacity.location = (320,-200)
    
    
    #---------- BLEND MODE -------------------
    
    #frame
    mt_blendModeFrame = mt_node.nodes.new('NodeFrame')
    mt_blendModeFrame.name = "PL_FrameBlendMode"
    mt_blendModeFrame.label = "Blend Mode"
    
    #blend mode node
    mt_blendMode = mt_node.nodes.new('ShaderNodeMixRGB')
    mt_blendMode.name = "PL_BlendMode"
    mt_blendMode.label = "Blend Mode"
    mt_blendMode.blend_type = "MIX"
    mt_blendMode.parent = mt_blendModeFrame
    
    #locations
    mt_blendModeFrame.location = (1000,0)
    
    #---------- ALPHA OUT ADD -------------------
    
    #frame
    mt_alphaOutAddFrame = mt_node.nodes.new('NodeFrame')
    mt_alphaOutAddFrame.name = "PL_FrameAlphaAdd"
    mt_alphaOutAddFrame.label = "Alpha  Add"
    
    #blend mode node
    mt_alphaOutAdd = mt_node.nodes.new('ShaderNodeMixRGB')
    mt_alphaOutAdd.name = "PL_alphaOutAdd"
    mt_alphaOutAdd.label = "Alpha Add"
    mt_alphaOutAdd.blend_type = "ADD"
    mt_alphaOutAdd.inputs["Fac"].default_value = 1
    mt_alphaOutAdd.parent = mt_alphaOutAddFrame
    
    #locations
    mt_alphaOutAddFrame.location = (1000,-300)
    
    #----- OUTPUT-----------------
    
    # create group output
    mt_colorOutput = mt_node.nodes.new('NodeGroupOutput')
    mt_colorOutput.name = "PL_LayerOutput"
    mt_colorOutput.label = 'Layer Output'
    
    #outputs
    n_colorOutput = mt_node.outputs.new('NodeSocketColor','colorOutput')
    n_alphaOutput = mt_node.outputs.new('NodeSocketColor','alphaOutput')
    
    n_colorOutput.default_value = [0,0,0,0]
    n_alphaOutput.default_value = [0,0,0,0]
    
    #location 
    mt_colorOutput.location = (1300,0)
    
    
    #---- INTERNAL LINKS ------
    
    #reroutes
    mt_node.links.new(mt_colorInputs.outputs['Color'], mt_filterRerouteIN.inputs[0])
    mt_node.links.new(mt_filterRerouteIN.outputs[0], mt_filterRerouteOUT.inputs[0])
    
    #layer opacity
    mt_node.links.new(mt_colorInputs.outputs['colorBelow'], mt_layerOpacity.inputs["Color1"])
    mt_node.links.new(mt_filterRerouteOUT.outputs[0], mt_layerOpacity.inputs["Color2"])
    mt_node.links.new(mt_inLayerOpacity.outputs[0], mt_layerOpacity.inputs["Fac"])
    
    #opacity offset
    mt_node.links.new(mt_inLayerOpacity.outputs[0], mt_opacityOffset.inputs[1])
    
    #mask switcher
    mt_node.links.new(mt_colorInputs.outputs['Mask'], mt_maskSwitcher.inputs["Color2"])
    mt_node.links.new(mt_inMaskOpacity.outputs[0], mt_maskSwitcher.inputs["Fac"])
    
    #masks
    mt_node.links.new(mt_maskSwitcher.outputs[0], mt_masksAdition.inputs["Color1"])
    mt_node.links.new(mt_colorInputs.outputs['ColorAlpha'], mt_masksAdition.inputs["Color2"])
    
    #mask opacity
    mt_node.links.new(mt_masksAdition.outputs[0], mt_masksOpacity.inputs["Color"])
    mt_node.links.new(mt_opacityOffset.outputs[0], mt_masksOpacity.inputs["Bright"])
    
    #blend mode
    mt_node.links.new(mt_colorInputs.outputs['colorBelow'], mt_blendMode.inputs["Color1"])
    mt_node.links.new(mt_layerOpacity.outputs[0], mt_blendMode.inputs["Color2"])
    mt_node.links.new(mt_masksOpacity.outputs[0], mt_blendMode.inputs["Fac"])
    
    #alpha out
    mt_node.links.new(mt_masksOpacity.outputs[0], mt_alphaOutAdd.inputs["Color1"])
    mt_node.links.new(mt_colorInputs.outputs['alphaBelow'], mt_alphaOutAdd.inputs["Color2"])
    
    #output
    mt_node.links.new(mt_blendMode.outputs[0], mt_colorOutput.inputs["colorOutput"])
    mt_node.links.new(mt_alphaOutAdd.outputs[0], mt_colorOutput.inputs["alphaOutput"])
   


def create_mtFilterNode():
    
    # create a group
    mt_node = bpy.data.node_groups.new('MTPaintLayer_Filter', 'ShaderNodeTree')
    
     #------- INPUTS --------------#
    
    #frame inputs
    
    mt_inputsFrame = mt_node.nodes.new('NodeFrame')
    mt_inputsFrame.label = "Inputs"
    mt_inputsFrame.name = "PL_FrameInputs"
    
    # create group inputs
    mt_colorInputs = mt_node.nodes.new('NodeGroupInput')
    mt_colorInputs.name = "PL_LayerInput"
    mt_colorInputs.label = 'layer Inputs'
    
    
    mt_colorInputs.parent = mt_inputsFrame
    
    #inputs below
    n_colorBelow = mt_node.inputs.new('NodeSocketColor','colorBelow')
    n_alphaBelow = mt_node.inputs.new('NodeSocketColor','alphaBelow')

    n_colorBelow.default_value = [0,0,0,0]
    n_alphaBelow.default_value = [0,0,0,0]

    #node mask

    n_mask = mt_node.inputs.new('NodeSocketColor','Mask')
    n_mask.default_value = [1,1,1,1]
    
    #inputs values
    
    mt_inLayerOpacity = mt_node.nodes.new('ShaderNodeValue')
    mt_inLayerOpacity.name = "PL_InputOpacity"
    mt_inLayerOpacity.label = "Layer Opacity"
    mt_inLayerOpacity.outputs[0].default_value = 1
    mt_inLayerOpacity.parent = mt_inputsFrame
    
    mt_inMaskOpacity = mt_node.nodes.new('ShaderNodeValue')
    mt_inMaskOpacity.name = "PL_InputMaskOpacity"
    mt_inMaskOpacity.label = "Mask Opacity"
    mt_inMaskOpacity.outputs[0].default_value = 1
    mt_inMaskOpacity.parent = mt_inputsFrame
    
    #locations
    mt_colorInputs.location = (0,0)
    mt_inLayerOpacity.location = (0,-160)
    mt_inMaskOpacity.location = (0,-260)
    
    
    #---------- FILTERS -------------------
    
    #frame
    mt_filterFrame = mt_node.nodes.new('NodeFrame')
    mt_filterFrame.name = "FPL_FrameFilters"
    mt_filterFrame.label = "Nested Filters"
    
    #reroutes
    mt_filterRerouteIN = mt_node.nodes.new('NodeReroute')
    mt_filterRerouteIN.name = "FPL_filtersColorInput"
    mt_filterRerouteIN.label = "Filters Input"
    mt_filterRerouteIN.parent = mt_filterFrame
    
    mt_filterRerouteOUT = mt_node.nodes.new('NodeReroute')
    mt_filterRerouteOUT.name = "FPL_filtersColorOutput"
    mt_filterRerouteOUT.label = "Filters Output"
    mt_filterRerouteOUT.parent = mt_filterFrame
    
    #locations
    mt_filterRerouteIN.location = (-50,0)
    mt_filterRerouteOUT.location = (50,0)
    mt_filterFrame.location = (300, 100)
    

    #---------- LAYER SYSTEM -------------------
    
    #frame
    mt_systemFrame = mt_node.nodes.new('NodeFrame')
    mt_systemFrame.name = "FPL_FrameSystem"
    mt_systemFrame.label = "Layer System"
    
    #opacity offset
    mt_opacityOffset = mt_node.nodes.new('ShaderNodeMath')
    mt_opacityOffset.name = "FPL_MaskOpacityOffset"
    mt_opacityOffset.label = "Mask Opacity Offset"
    mt_opacityOffset.operation = "ADD"
    mt_opacityOffset.inputs[0].default_value = -1
    mt_opacityOffset.inputs[1].default_value = 0
    mt_opacityOffset.parent = mt_systemFrame
    
    #mask switcher
    mt_maskSwitcher = mt_node.nodes.new('ShaderNodeMixRGB')
    mt_maskSwitcher.name = "FPL_MaskSwitcher"
    mt_maskSwitcher.label = "Mask Switcher"
    mt_maskSwitcher.blend_type = "MIX"
    mt_maskSwitcher.inputs["Color1"].default_value = [1,1,1,1]
    mt_maskSwitcher.parent = mt_systemFrame
    
    #layer opacity
    mt_layerOpacity = mt_node.nodes.new('ShaderNodeMixRGB')
    mt_layerOpacity.name = "FPL_LayerOpacity"
    mt_layerOpacity.label = "Layer Opacity"
    mt_layerOpacity.blend_type = "MIX"
    mt_layerOpacity.parent = mt_systemFrame
      
    #masks opacity
    mt_masksOpacity = mt_node.nodes.new('ShaderNodeBrightContrast')
    mt_masksOpacity.name = "FPL_MaskOpacity"
    mt_masksOpacity.label = "Mask Opacity"
    mt_masksOpacity.inputs["Contrast"].default_value = 0
    mt_masksOpacity.parent = mt_systemFrame
    
    #Invert
    mt_nInvert = mt_node.nodes.new('ShaderNodeInvert')
    mt_nInvert.name = "FPL_InvertMask"
    mt_nInvert.label = "Invert"
    mt_nInvert.parent = mt_systemFrame
    
    #locations
    mt_systemFrame.location = (400,0)
    mt_opacityOffset.location = (0,0)
    mt_layerOpacity.location = (160,0)
    mt_maskSwitcher.location = (0,-200)
    mt_masksOpacity.location = (160,-200)
    mt_nInvert.location = (320,-200)
    
     #---------- BLEND MODE -------------------
    
    #frame
    mt_blendModeFrame = mt_node.nodes.new('NodeFrame')
    mt_blendModeFrame.name = "FPL_FrameBlendMode"
    mt_blendModeFrame.label = "Blend Mode"
    
    #blend mode node
    mt_blendMode = mt_node.nodes.new('ShaderNodeMixRGB')
    mt_blendMode.name = "PL_BlendMode"
    mt_blendMode.label = "Blend Mode"
    mt_blendMode.blend_type = "MIX"
    mt_blendMode.parent = mt_blendModeFrame
    
    #locations
    mt_blendModeFrame.location = (1000,0)

    #----- OUTPUT-----------------
    
    # create group output
    mt_colorOutput = mt_node.nodes.new('NodeGroupOutput')
    mt_colorOutput.name = "FPL_LayerOutput"
    mt_colorOutput.label = 'Layer Output'
    
    #outputs
    n_colorOutput = mt_node.outputs.new('NodeSocketColor','colorOutput')
    n_alphaOutput = mt_node.outputs.new('NodeSocketColor','alphaOutput')
    
    n_colorOutput.default_value = [0,0,0,0]
    n_alphaOutput.default_value = [0,0,0,0]
    
    #location 
    mt_colorOutput.location = (1300,0)
    
    
    #---- INTERNAL LINKS ------
    
    #reroutes
    mt_node.links.new(mt_colorInputs.outputs['colorBelow'], mt_filterRerouteIN.inputs[0])
    mt_node.links.new(mt_filterRerouteIN.outputs[0], mt_filterRerouteOUT.inputs[0])
    
    #layer opacity
    mt_node.links.new(mt_colorInputs.outputs['colorBelow'], mt_layerOpacity.inputs["Color1"])
    mt_node.links.new(mt_filterRerouteOUT.outputs[0], mt_layerOpacity.inputs["Color2"])
    mt_node.links.new(mt_inLayerOpacity.outputs[0], mt_layerOpacity.inputs["Fac"])
    
    #opacity offset
    mt_node.links.new(mt_inLayerOpacity.outputs[0], mt_opacityOffset.inputs[1])
    
    #mask switcher
    mt_node.links.new(mt_colorInputs.outputs['Mask'], mt_maskSwitcher.inputs["Color2"])
    mt_node.links.new(mt_inMaskOpacity.outputs[0], mt_maskSwitcher.inputs["Fac"])
    
    #mask opacity
    mt_node.links.new(mt_maskSwitcher.outputs[0], mt_masksOpacity.inputs["Color"])
    mt_node.links.new(mt_opacityOffset.outputs[0], mt_masksOpacity.inputs["Bright"])
    
    #invet 
    mt_node.links.new(mt_inMaskOpacity.outputs[0], mt_nInvert.inputs[0])
    mt_node.links.new(mt_masksOpacity.outputs[0], mt_nInvert.inputs[1])
    
    #blend mode
    mt_node.links.new(mt_layerOpacity.outputs[0], mt_blendMode.inputs["Color1"])
    mt_node.links.new(mt_colorInputs.outputs['colorBelow'], mt_blendMode.inputs["Color2"])
    mt_node.links.new(mt_nInvert.outputs[0], mt_blendMode.inputs["Fac"])
    
    #output
    mt_node.links.new(mt_blendMode.outputs[0], mt_colorOutput.inputs["colorOutput"])
    mt_node.links.new(mt_colorInputs.outputs['alphaBelow'], mt_colorOutput.inputs["alphaOutput"])
   

   
def create_mtPaintShader():
    
    # create a group
    mt_node = bpy.data.node_groups.new('MTPaintShader', 'ShaderNodeTree')
    
     #------- INPUTS --------------#
    

    # create group inputs
    mt_colorInputs = mt_node.nodes.new('NodeGroupInput')
    mt_colorInputs.name = "PL_Input"
    mt_colorInputs.label = 'Shader Inputs'

    
    #inputs below
    n_colorBelow = mt_node.inputs.new('NodeSocketColor','Color')
    n_alphaBelow = mt_node.inputs.new('NodeSocketColor','Alpha')
    n_shadeless = mt_node.inputs.new('NodeSocketFloat', 'Shadeless')
    n_transparent = mt_node.inputs.new('NodeSocketFloat', 'Transparent')
    
    n_colorBelow.default_value = [0,0,0,0]
    n_alphaBelow.default_value = [1,1,1,1]
    n_shadeless.default_value = 0
    n_transparent.default_value = 0

    #------ REMOVE ALPHA 
    
    #Frame
    mt_removeAlphaFrame = mt_node.nodes.new('NodeFrame')
    mt_removeAlphaFrame.name = "PL_removeAlpha"
    mt_removeAlphaFrame.label = "Remove Alpha"
    
    #masks opacity
    mt_separateAlpha = mt_node.nodes.new('ShaderNodeSeparateRGB')
    mt_separateAlpha.name = "PL_separateAlpha"
    mt_separateAlpha.label = "Separate Alpha"
    mt_separateAlpha.parent = mt_removeAlphaFrame
    
    #masks opacity
    mt_combineRGB = mt_node.nodes.new('ShaderNodeCombineRGB')
    mt_combineRGB.name = "PL_combineRGB"
    mt_combineRGB.label = "Combine RGB"
    mt_combineRGB.parent = mt_removeAlphaFrame
    
    #location
    mt_removeAlphaFrame.location = (200,-500)
    mt_separateAlpha.location = (0,0)
    mt_combineRGB.location = (200,0)
    
    
    #------ SHADELESS SETTINGS
    
    #Frame
    mt_shadelessFrame = mt_node.nodes.new('NodeFrame')
    mt_shadelessFrame.name = "PL_ShadelessSettings"
    mt_shadelessFrame.label = "Shadeless Settings"
    
    #light path
    mt_lightPath = mt_node.nodes.new('ShaderNodeLightPath')
    mt_lightPath.name = "PL_LightPath"
    mt_lightPath.label = "Light Path"
    mt_lightPath.parent = mt_shadelessFrame
    
    #transparent node
    mt_transparentNode = mt_node.nodes.new('ShaderNodeBsdfTransparent')
    mt_transparentNode.name = "PL_TransparentNode"
    mt_transparentNode.label = "Transparent Shader"
    mt_transparentNode.parent = mt_shadelessFrame
    
    #emission node
    mt_emissionNode = mt_node.nodes.new('ShaderNodeEmission')
    mt_emissionNode.name = "PL_FlatColor"
    mt_emissionNode.label = "Flat Color"
    mt_emissionNode.parent = mt_shadelessFrame
    
    #mix shader
    mt_shadelessOUT = mt_node.nodes.new('ShaderNodeMixShader')
    mt_shadelessOUT.name = "PL_shadelessOutput"
    mt_shadelessOUT.label = "Shadeless Output"
    mt_shadelessOUT.parent = mt_shadelessFrame
    
    #location
    mt_shadelessFrame.location = (640,-200)
    mt_lightPath.location = (0,0)
    mt_transparentNode.location = (0,-270)
    mt_emissionNode.location = (0,-350)
    mt_shadelessOUT.location = (200,0)
    
    
    #------ ALPHA SETTINGS
    
    #Frame
    mt_alphaSettignsFrame = mt_node.nodes.new('NodeFrame')
    mt_alphaSettignsFrame.name = "PL_AlphaSettings"
    mt_alphaSettignsFrame.label = "Alpha Settings"
    
    #transparent node
    mt_transparentAlphaNode = mt_node.nodes.new('ShaderNodeBsdfTransparent')
    mt_transparentAlphaNode.name = "PL_transparentAlphaNode"
    mt_transparentAlphaNode.label = "Transparent Alpha Shader"
    mt_transparentAlphaNode.parent = mt_alphaSettignsFrame
    
    #mix shader
    mt_alphaSettingsOUT = mt_node.nodes.new('ShaderNodeMixShader')
    mt_alphaSettingsOUT.name = "PL_Transparency"
    mt_alphaSettingsOUT.label = "Alpha Settings Output"
    mt_alphaSettingsOUT.parent = mt_alphaSettignsFrame
    
    #location
    mt_alphaSettignsFrame.location = (1000,150)
    mt_transparentAlphaNode.location = (0,0)
    mt_alphaSettingsOUT.location = (150,0)
    
    #---------- COLOR TO SHADER 
    
    #Diffuse shader
    mt_inputDiffuseShader = mt_node.nodes.new('ShaderNodeBsdfDiffuse')
    mt_inputDiffuseShader.name = "PL_DiffuseColor"
    mt_inputDiffuseShader.label = "Color to shader"
    
    mt_inputDiffuseShader.location = (610,0)
    
    #switcher 
    mt_flatSwitcher = mt_node.nodes.new('ShaderNodeMixShader')
    mt_flatSwitcher.name = "PL_FlatSwitch"
    mt_flatSwitcher.label = "Flat Switcher"
    
    mt_flatSwitcher.location = (800,0)
    
    #---------- OUTPUT 
    
    #transparency mixer
    mt_transparencySwitcher = mt_node.nodes.new('ShaderNodeMixShader')
    mt_transparencySwitcher.name = "PL_TransparencySwitch"
    mt_transparencySwitcher.label = "Transparency Switcher"
    
    mt_transparencySwitcher.location = (1400,0) 
    
    # create group output
    mt_shaderOutput = mt_node.nodes.new('NodeGroupOutput')
    mt_shaderOutput.name = "PL_Outuput"
    mt_shaderOutput.label = 'Shader Output'
    
    #outputs
    n_shaderOutput = mt_node.outputs.new('NodeSocketShader','Shader')

    #location 
    mt_shaderOutput.location = (1600,0)
    
    
    #---- INTERNAL LINKS ------
    
    #separate alpha
    mt_node.links.new(mt_colorInputs.outputs['Color'], mt_separateAlpha.inputs[0])
    
    #combine RGB
    mt_node.links.new(mt_separateAlpha.outputs['R'], mt_combineRGB.inputs['R'])
    mt_node.links.new(mt_separateAlpha.outputs['G'], mt_combineRGB.inputs['G'])
    mt_node.links.new(mt_separateAlpha.outputs['B'], mt_combineRGB.inputs['B'])
    
    #inputDiffuseShader
    mt_node.links.new(mt_colorInputs.outputs['Color'], mt_inputDiffuseShader.inputs['Color'])
    
    #Flath Switcher
    mt_node.links.new(mt_colorInputs.outputs['Shadeless'], mt_flatSwitcher.inputs[0])
    mt_node.links.new(mt_shadelessOUT.outputs[0], mt_flatSwitcher.inputs[2])
    mt_node.links.new(mt_inputDiffuseShader.outputs[0], mt_flatSwitcher.inputs[1])
    
    #shadeless emission
    mt_node.links.new(mt_combineRGB.outputs[0], mt_emissionNode.inputs['Color'])
    
    #shadeless output
    mt_node.links.new(mt_lightPath.outputs["Is Camera Ray"], mt_shadelessOUT.inputs[0])
    mt_node.links.new(mt_transparentNode.outputs[0], mt_shadelessOUT.inputs[1])
    mt_node.links.new(mt_emissionNode.outputs[0], mt_shadelessOUT.inputs[2])
    
    #alpha settings transparent
    mt_node.links.new(mt_colorInputs.outputs['Color'], mt_transparentAlphaNode.inputs[0])
    
    #alpha settings output
    mt_node.links.new(mt_colorInputs.outputs['Alpha'], mt_alphaSettingsOUT.inputs[0])
    mt_node.links.new(mt_transparentAlphaNode.outputs[0], mt_alphaSettingsOUT.inputs[1])
    mt_node.links.new(mt_flatSwitcher.outputs[0], mt_alphaSettingsOUT.inputs[2])
    
    #transparency switcher
    mt_node.links.new(mt_colorInputs.outputs['Transparent'], mt_transparencySwitcher.inputs[0])
    mt_node.links.new(mt_flatSwitcher.outputs[0], mt_transparencySwitcher.inputs[1])
    mt_node.links.new( mt_alphaSettingsOUT.outputs[0], mt_transparencySwitcher.inputs[2])
    
    #output
    mt_node.links.new(mt_transparencySwitcher.outputs[0], mt_shaderOutput.inputs[0])

    return mt_node               
               
# ------------  Toggle selection ------------------- #

def deselectAllNodes():
    
    mainTree = bpy.context.object.active_material.node_tree
    
    for node in mainTree.nodes:
        node.select = False
        
def selectNode(pTargetLayer):
    
    mainTree = bpy.context.object.active_material.node_tree
    
    deselectAllNodes()
    pTargetLayer.select = True    
    mainTree.nodes.active = pTargetLayer
    
#----------------------------------------------------#

       



# ----------- CONFIGURE MULTITILE MATERIALS --------------- #       


#---------- put every uv vertix in the correct tile -----------#

def createMultiTileGrid(pUVLayer, pNumRows, pNumCols):
    
    multiTileGrid = [[[] for x in range(pNumRows)] for x in range(pNumCols)]
    index = 0
    for vec in pUVLayer.data:
        mtpos_x = round(vec.uv[0],2)%10
        mtpos_y = round(vec.uv[1],2)%10  
        
        numRows = 9
        numCols = 9
        
        if mtpos_x < numCols and mtpos_y < numRows:
            multiTileGrid[int(mtpos_x)][int(mtpos_y)].append(index)
            index += 1
        else:
            return "TILES_OVERFLOW"
            break
    
    return multiTileGrid




#---------- create a new uv map layer ------------#

def createMTPaintUVLayer(pObj):
    
    
    bpy.ops.mesh.uv_texture_add()
    lastUVLayerIndex = len(pObj.data.uv_layers)-1
    lastUVLayer = pObj.data.uv_layers[lastUVLayerIndex]
    lastUVLayer.name = "MTP_PaintingLayer"
    
    return lastUVLayerIndex
    
    
def createMTBakeUVLayer(pObj):
    
    lastUVLayer = None
    prevUVMap = pObj.data.uv_textures.active_index
    
    
    bpy.ops.mesh.uv_texture_add()
    lastUVLayerIndex = len(pObj.data.uv_layers)-1
    lastUVLayer = pObj.data.uv_layers[lastUVLayerIndex]
    lastUVLayer.name = "MTP_BakeLayer"
    
    #-- and create a first paint layer
    createMTPaintUVLayer(pObj)
    
    pObj.data.uv_textures.active_index= prevUVMap
    
    return lastUVLayer
    

#-------------- move uv tiles ---------------#

def moveTo00Tile(pUVLayer, pMultiTileGrid, pNumRows, pNumCols):
    
    for column in range(0,pNumCols):
        for row in range(0,pNumRows):
            for index in pMultiTileGrid[row][column]:
                pUVLayer.data[index].uv[0] -= row
                pUVLayer.data[index].uv[1] -= column


def focusToSelectedTile(pObj):
    
    #bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.object.mode_set(mode = 'OBJECT')
    uvLayer = None
    prevUVMap = pObj.data.uv_textures.active_index
    
    #pObj.data.uv_layers[obj.data.uv_textures.active_index]
    

    finder = pObj.data.uv_textures.find("MTP_PaintingLayer")
    if finder >= 0:
        
        uvLayer = pObj.data.uv_textures[finder]
    
        pObj.data.uv_textures.remove(uvLayer)
        pObj.data.uv_textures.active_index = 0
        newUVLayerIndex = createMTPaintUVLayer(pObj)
        
        pObj.data.uv_textures.active_index = newUVLayerIndex
        
        matName = pObj.active_material.name
         
        focusRow = int(matName[3]) - 1
        focusColumn = int(matName[2])
        
        uvLayer = pObj.data.uv_layers[finder]
        if uvLayer != None:
            for vec in uvLayer.data:
                vec.uv[0] -= focusRow
                vec.uv[1] -= focusColumn
            
    
        pObj.data.uv_textures.active_index = newUVLayerIndex
    
    bpy.ops.object.mode_set(mode = 'OBJECT')


#---------- Use Shader -------------------#

#not implemented
    
#----------create multi tile vertex group --------------#

def deselectAllVertices(pObj):
    
    for v in pObj.data.vertices:
        v.select = False
    
    
def createMTMaterials(pObj, pBaseMaterial, pMultiTileGrid, pNumRows,pNumCols):
    
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.select_mode(type="VERT") 
    bpy.ops.mesh.select_all(action='DESELECT')
    
    for column in range(0,pNumCols):
        for row in range(0,pNumRows):

            bpy.ops.object.mode_set(mode = 'OBJECT')
            for index in pMultiTileGrid[row][column]:    
                v = pObj.data.loops[index].vertex_index
                pObj.data.vertices[v].select = True


            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.mesh.select_mode(type="VERT") 
            
            baseMaterial = pBaseMaterial
            
            if pObj.data.total_vert_sel > 0:
                nCol = str(column)
                nRow = str(row+1)    
                bpy.ops.object.vertex_group_assign_new()
                newVGName = "10" + nCol + nRow + "_multiTile"
                lastVG = len(pObj.vertex_groups)- 1
                pObj.vertex_groups[lastVG].name = newVGName
                
                newMaterialName= "10" + nCol + nRow + "_" + pObj.name
                
                
                if baseMaterial != None:
                    newMaterial = baseMaterial.copy()
                    newMaterial.name = newMaterialName
                else:
                    newMaterial = bpy.data.materials.new(newMaterialName)
                    
                newMaterial.use_nodes = True
                pObj.data.materials.append(newMaterial) 
                pObj.active_material_index = (len(pObj.data.materials) - 1)
                    
                bpy.ops.object.material_slot_assign()
             
            bpy.ops.mesh.select_all(action='DESELECT')
     
    bpy.ops.object.mode_set(mode = 'OBJECT')

# ---------- Running ---------------#


            
def createMultiTileMaterials(pBaseMaterial):
    obj = bpy.context.object
    uvLayerCount = len(obj.data.uv_layers)
    success = "FAIL"
    
    if uvLayerCount > 0:
        uvLayer = obj.data.uv_layers[obj.data.uv_textures.active_index]
        
        numRows = 9
        numCols = 9
            
        deselectAllVertices(obj)
            
        mtGrid = createMultiTileGrid(uvLayer, numRows,numCols)
        if mtGrid != "TILES_OVERFLOW": 
            uvMTBakeLayer = createMTBakeUVLayer(obj)
            moveTo00Tile(uvMTBakeLayer, mtGrid, numRows, numCols)
            createMTMaterials(obj, pBaseMaterial, mtGrid, numRows,numCols)
            success = "SUCCESS"
        else: 
            success = "TILES_OVERFLOW"

    return success
        

def createMultiTileUVLayers(): 
    
    obj = bpy.context.object
    uvLayerCount = len(obj.data.uv_layers)
    success = "FAIL"
     
    if uvLayerCount > 0:
        uvLayer = obj.data.uv_layers[obj.data.uv_textures.active_index]
        
        numRows = 9
        numCols = 9
        
        deselectAllVertices(obj)
            
        mtGrid = createMultiTileGrid(uvLayer, numRows,numCols)
        
        if mtGrid != "TILES_OVERFLOW": 
            uvMTBakeLayer = createMTBakeUVLayer(obj)
            moveTo00Tile(uvMTBakeLayer, mtGrid, numRows, numCols)
            success = "SUCCESS"
        else: 
            success = "TILES_OVERFLOW"
            
    return success

# -------------------------- #        


# ------------  New texture Image ------------------- #

def sumToIndex(pIndex):
    
    data = int(pIndex)
    data += 1
    sData = str(data)
    
    while len(sData) < 3:
        sData = "0" + sData
    
    return sData
    
def getFirstUnusedImageName(pName):
    
    newName = pName 
    for i in range(0, len(bpy.data.images)):
        image = bpy.data.images[i]
        if image.name == newName:
            if len(newName) > 3:
                if newName[-4] == '.':
                    
                    newIndex = sumToIndex(newName[-3:])
                    newName = newName[:-3] + newIndex
                    
                else:
                    newName = newName + ".001"    
            else:
                newName = newName + ".001"
        
        i = 0
                
    return newName      
            
            

# ------------------------------- #

# ---------- Texture node operations --------------------- #

def newTextureImage(pName = "layerPaintImage", pWidth = 1024, pHeight = 1024, pColor = (0.0,0.0,0.0,0.0), pAlpha = True, pFloat=False):
    
  
    unusedImageName = getFirstUnusedImageName(pName)
    #imageProperties = [unusedImageName , pWidth, pHeight, pColor, pAlpha, pDepth]
    img = bpy.ops.image.new(name = unusedImageName, width = pWidth, height = pHeight, color = pColor, alpha = pAlpha, float=pFloat)
    textureImage = bpy.data.images[unusedImageName]
    textureImage.user_clear()     
    return textureImage
   
   
def newTextureNode(pCurrentTree, pTextureImage):
    
    textureNode = pCurrentTree.nodes.new("ShaderNodeTexImage")
    textureNode.image = pTextureImage
    
    return textureNode
        
def addTextureNode():
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot

    numMaterials = len(bpy.context.object.material_slots)

    for i in range(0,numMaterials):
        bpy.context.object.active_material_index = i
        bpy.ops.node.add_node(type="ShaderNodeTexImage", use_transform = False)
        
    bpy.context.object.active_material_index = currentMatIndex


# ---------- save layers operations --------------------- #

def saveImageTexture(pTexture,pFilePath, pLayerName):
    
    img = pTexture.image
    
    if pTexture.image != None:
        
        imagePath = pTexture.image.filepath_from_user()
        currentMaterial = bpy.context.object.active_material
        
        fileName = bpy.path.basename(pFilePath)
        filePath = pFilePath.replace(fileName,"")
        fileName = currentMaterial.name + "_" + pLayerName + bpy.context.scene.render.file_extension
        filePath = os.path.join(filePath, fileName)
        img.filepath_raw = filePath
        img.save_render(img.filepath_raw)
    
         
def saveTexturesLayer(pLayer, pFilePath, pAction):

    if pAction == "SELECTED":
        colorTexture = conectedFromNode(pLayer, "Color")[0]
        maskTexture = conectedFromNode(pLayer, "Mask")[0]
        
        if colorTexture != None:
            saveImageTexture(colorTexture,pFilePath, pLayer.name)
        
        if maskTexture != None:
            saveImageTexture(maskTexture,pFilePath, pLayer.name)
        
    elif pAction == "ALL":
        firstLayer = findFirstLayer(pLayer)
            
        if firstLayer != None:
            currentLayer = firstLayer        
            while currentLayer != None and isPaintLayerNode(currentLayer):
                
                
                colorTexture = conectedFromNode(currentLayer, "Color")[0]
                maskTexture = conectedFromNode(currentLayer, "Mask")[0]

                if colorTexture != None:
                    saveImageTexture(colorTexture,pFilePath, currentLayer.name)
                
                if maskTexture != None:
                    saveImageTexture(maskTexture,pFilePath, currentLayer.name)
                    
                currentLayer = conectedToNode(currentLayer, "colorOutput")[0]
        
              
def packTexturesLayer(pLayer):
    
    colorTexture = conectedFromNode(pLayer, "Color")[0]
    maskTexture = conectedFromNode(pLayer, "Mask")[0]
    if colorTexture != None and colorTexture.image != None:
        
        if colorTexture.image.is_dirty:
            colorTexture.image.pack(as_png=True)
    
    if maskTexture != None and maskTexture.image != None:
        if maskTexture.image.is_dirty:
            maskTexture.image.pack(as_png=True)
        
#------------- bake layer operations ------------------#

def setbakeLayers(pCurrentLayer):
    
    obj = bpy.context.object

    prevUVMap = obj.data.uv_textures.active_index
    uvNode = getUVNode(pCurrentLayer,bpy.context.scene.mtlayerPaintingSpace) 
    #uv_layer = obj.data.uv_textures[].name
    uvNode.uv_map = "MTP_BakeLayer"
    multiTile_propagateUVChannel()
    obj.data.uv_textures.active_index = obj.data.uv_layers.find("MTP_BakeLayer")
    obj.data.uv_textures["MTP_BakeLayer"].active_render = True
    
    #bpy.ops.object.bake(use_clear=True)
    #obj.data.uv_textures.active_index = prevUVMap
    
    bpy.context.scene.render.layers[0].use_pass_diffuse_direct = True
    bpy.context.scene.render.layers[0].use_pass_diffuse_direct = True
    bpy.context.scene.cycles.bake_type = 'DIFFUSE'


# ---------- Node links operations --------------------- #

def hasInput(pCurrentNode, pInput):
    
    found = False
    finder = pCurrentNode.inputs.find(pInput)
    if finder > -1:
        found = True
    
    return found

def hasOutput(pCurrentNode, pOutput):
    
    found = False
    finder = pCurrentNode.outputs.find(pOutput)
    if finder > -1:
        found = True
    
    return found


def conectedToNode(pCurrentNode, pOutput):
    
    conection = [None, None]
    if pCurrentNode != None:
        if hasOutput(pCurrentNode,pOutput):
            for i in range(0,len(pCurrentNode.outputs[pOutput].links)):
                toNode = pCurrentNode.outputs[pOutput].links[i].to_node
                if toNode != None:
                    
                    toSocket = pCurrentNode.outputs[pOutput].links[i].to_socket.name
                    conection = [toNode,toSocket]
                    break
                    
                else:
                    conection = [None, None]
    
    return conection

def conectedFromNode(pCurrentNode, pInput):
    
    conection = [None, None]
    
    if pCurrentNode != None:
        if hasInput(pCurrentNode,pInput):
            if len(pCurrentNode.inputs[pInput].links) > 0:
                fromNode = pCurrentNode.inputs[pInput].links[0].from_node
                fromSocket = pCurrentNode.inputs[pInput].links[0].from_socket.name
                
                conection = [fromNode, fromSocket]
            else:
                conection = [None, None]
        
    return conection


# ---------- Find nodes operations --------------------- #

def findTextureNode():
    
    mainTree = bpy.context.object.active_material.node_tree
    activeTexture = bpy.context.object.active_material.texture_paint_images[bpy.context.object.active_material.paint_active_slot]
    layerNode = None
    textureNode = None
    
    for node in mainTree.nodes: 
        if node.type == "TEX_IMAGE" and node.image == activeTexture:
            textureNode = node
            
    return textureNode
    
def findLayerNode():
    
    mainTree = bpy.context.object.active_material.node_tree
    layerNode = [None, None]
    textureNode = findTextureNode()    
    
    if textureNode != None:
        layerNode = conectedToNode(textureNode, "Color")
        previousNode = conectedFromNode(textureNode,"Vector")
        #mainTree.nodes.active = layerNode[0]
        
        if layerNode[0].type != "GROUP":
            layerNode = [None, None]
               
    return layerNode                

def findNodeByName(pName):
    
    mainTree = bpy.context.object.active_material.node_tree
    node = None
    
    for n in mainTree.nodes:
        if n.name == pName:
            node = n
            
    return node    
    
def findBlendModeNode():
    
    blendModeNode = None
    mainTree = bpy.context.object.active_material.node_tree
    selectedLayer = getActiveLayer()
    #mainTree.nodes.active = selectedLayer
    
    #selectedLayer = mainTree.nodes.active
     
    
    
    if isPaintLayerNode(selectedLayer):
        blendModeNode = selectedLayer.node_tree.nodes["PL_BlendMode"]
    
    return blendModeNode


def findOpacityLayerNode():
    
    opacityNode = None
    mainTree = bpy.context.object.active_material.node_tree
    #selectedLayer = mainTree.nodes.active
    selectedLayer = getActiveLayer()
    #mainTree.nodes.active = selectedLayer
    
    if isPaintLayerNode(selectedLayer):
        opacityNode = selectedLayer.node_tree.nodes["PL_InputOpacity"]
        
    return opacityNode

def findUVLayerNode(pPaintingSpace):
    
    uvLayerNode = None
    mainTree = bpy.context.object.active_material.node_tree
    #selectedLayer = mainTree.nodes.active
    selectedLayer = getActiveLayer()
    
    if isPaintLayerNode(selectedLayer):
        
        layerType = getLayerType(selectedLayer)
        if pPaintingSpace == True and layerType == "COLOR": #search color texture
            textureNode = conectedFromNode(selectedLayer,"Color")
            uvLayerNode = conectedFromNode(textureNode[0],"Vector")
            uvLayerNode = uvLayerNode[0]
        else: #search mask texture
            textureNode = conectedFromNode(selectedLayer,"Mask")
            uvLayerNode = conectedFromNode(textureNode[0],"Vector")    
            uvLayerNode = uvLayerNode[0]
   
    return uvLayerNode


#------------ Layers operations (add, delete, etc...) ---------------- #

def setOpacityLayer(pLayer, pValue):
    
    nodeId = pLayer.node_tree.nodes.find("PL_InputOpacity")
    if nodeId >= 0:
        pLayer.node_tree.nodes[nodeId].outputs["Value"].default_value = pValue
     
def getOpacityLayer(pLayer):
    
    value = -1000
    nodeId = pLayer.node_tree.nodes.find("PL_InputOpacity")
    if nodeId >= 0:
        value = pLayer.node_tree.nodes[nodeId].outputs["Value"].default_value
        
    return value


def setLayerName(pCurrentLayer, pName):
    
    pCurrentLayer.node_tree.nodes["PL_FrameInputs"].label = pName
    pCurrentLayer.name = pName
    pCurrentLayer.label = pName
    
    
def getLayerName(pCurrentLayer):
    
    name = ""
    if pCurrentLayer != None:
        name = pCurrentLayer.node_tree.nodes["PL_FrameInputs"].label 
    
    return name

def getLayerType(pCurrentLayer):
    
    layerType = None
    if pCurrentLayer != None:
        finder = pCurrentLayer.node_tree.name.find("_Color")
        
        if finder > -1:
            layerType = "COLOR"
        else:
            finder = pCurrentLayer.node_tree.name.find("_Filter")
            if finder > -1:
                layerType = "FILTER"
        
    return layerType
   
def getUVNode(pCurrentLayer,pPaintingSpace):
    
    uvNode = None 
    layerType = getLayerType(pCurrentLayer)
    
    if layerType == "COLOR":
        if pPaintingSpace:
            textureNode = conectedFromNode(pCurrentLayer ,"Color")
        else:
            textureNode = conectedFromNode(pCurrentLayer ,"Mask")
    elif layerType == "FILTER":
        textureNode = conectedFromNode(pCurrentLayer ,"Mask")
                
    if textureNode[0] != None:  
        uvNode = conectedFromNode(textureNode[0],"Vector")
        uvNode = uvNode[0]
        
    return uvNode

def getTextureNode(pCurrentLayer,pPaintingSpace):
    
    textureNode = None 
    
    if pPaintingSpace:
        textureNode = conectedFromNode(pCurrentLayer ,"Color")
        textureNode = textureNode[0]
    else:
        textureNode = conectedFromNode(pCurrentLayer ,"Mask")
        textureNode = textureNode[0]
            
    return textureNode

def getFiltersFrame(pCurrentLayer):
    
    filtersFrame = None

    if pCurrentLayer.node_tree.nodes.find("PL_FrameClippingMaskFilters") > - 1:
        filtersFrame = pCurrentLayer.node_tree.nodes["PL_FrameClippingMaskFilters"]
    elif pCurrentLayer.node_tree.nodes.find("FPL_FrameFilters") > - 1: 
        filtersFrame = pCurrentLayer.node_tree.nodes["FPL_FrameFilters"]
            
    return filtersFrame

    
def getFilters(pCurrentLayer):
    
    nodeTree = pCurrentLayer.node_tree
    filtersParent = None
    filters = []
    
    for node in nodeTree.nodes:
        if node.name == "PL_FrameClippingMaskFilters" or node.name == "FPL_FrameFilters":
            filtersParent = node
            break
        
    if filtersParent != None:
        fChildren = getNodeChildren(nodeTree, filtersParent)
        for node in fChildren:
            if node.type != 'REROUTE':
                filters.append(node)
    
    return filters        

def collectInnerFilters():
    
    filtersSet = bpy.context.scene.nodeFiltersSet
    filtersSet.clear()
    mainTree = bpy.context.object.active_material.node_tree
    selectedLayer = getActiveLayer()
    mainTree.nodes.active = selectedLayer
    #mainTree.nodes.active.select = True
    
    if isPaintLayerNode(selectedLayer):
        filters  = []
        filters = getFilters(selectedLayer)
        
        for f in filters:
            n = filtersSet.add()
            n.name = f.name
        
        #bpy.context.scene.nodeFiltersSet_id = ""
                        

def propagateTexture(pCurrentLayer, pTextureNode, pPaintingSpace):
    
    mainTree = bpy.context.object.active_material.node_tree
    if pPaintingSpace:
        textureNode = conectedFromNode(pCurrentLayer,"Color") 
    else:
        textureNode = conectedFromNode(pCurrentLayer,"Mask")
    
    
    textureNode = textureNode[0]
    currentImage= textureNode.image
    textureNode.image= pTextureNode.image
    
    if currentImage != None and currentImage.users == 0:
        bpy.data.images.remove(currentImage)
        
def selectPaintSlotTexture(pMainLayer, pPaintingSpace):    
    
    mainTree = bpy.context.object.active_material.node_tree
    currentLayer = getLayerByType(pMainLayer)
    
    if currentLayer != None:
        
        layerType = getLayerType(currentLayer)
        if pPaintingSpace and layerType == "COLOR" :
            textureNode = conectedFromNode(currentLayer,"Color")
        else:
            textureNode = conectedFromNode(currentLayer,"Mask")
        
        if textureNode[0] != None:  
            textureImg = textureNode[0].image
            
            for i in range(0, len(bpy.context.object.active_material.texture_paint_images)):
                tmpTexture = bpy.context.object.active_material.texture_paint_images[i]
                if textureImg == tmpTexture:
                    bpy.context.object.active_material.paint_active_slot = i
                    break
        
        selectNode(currentLayer)

def getNumNodeChildren(pCurrentTree, pNode):
    
    cont = 0
    
    for node in pCurrentTree.nodes:
        if node.parent == pNode:
            cont += 1
        
    return cont 

def getNodeChildren(pCurrentTree, pNode):
    
    children = []
    
    for node in pCurrentTree.nodes:
        if node.parent == pNode:
            children.append(node)
    
    return children

def getChildLayerNode(pCurrentTree, pNode):
    
    layerNode = None
    
    for node in pCurrentTree.nodes:
        if node.parent == pNode:
            if isPaintLayerNode(node):
                layerNode = node
                break

    return layerNode

def unselectAllNodes(pMainTree):
    
    if pMainTree != None:
        for node in pMainTree.nodes:
            node.select = False
    
        pMainTree.nodes.active = None
    
    
    
def removeNodeTree(pCurrentTree, pBaseNode):
    
    layerNode = pBaseNode
    mainTree = pCurrentTree
    colorTexture = None
    maskTexture = None
    colorUVNode = None
    maskUVNode = None
    
    layerParent = pBaseNode.parent
    children = getNodeChildren(pCurrentTree, layerParent)
    
    for node in children:
        hasImg = hasattr(node, "image")
        if hasImg:
            img = node.image
            if img != None and img.users == 0:
                bpy.data.images.remove(img)
        
        pCurrentTree.nodes.remove(node) 
        
    mainTree.nodes.remove(layerParent)  
            
    return True
            
def deleteLayerNode(pBaseNode):
    
    mainTree = bpy.context.object.active_material.node_tree
    layerNode = getLayerByType(pBaseNode)
    #layerNode = mainTree.nodes.active
    #layerNode = getActiveLayer()
    #mainTree.nodes.active = layerNode
    
    newLayerID = -1

    if layerNode != None:
        
        nextLayer = conectedToNode(layerNode, "colorOutput")
        nextAlphaLayer = conectedToNode(layerNode, "alphaOutput")
        previousLayer = conectedFromNode(layerNode, "colorBelow")
        
        validPreviousLayer = isPaintLayerNode(previousLayer[0])
        
        if nextLayer[0] != None and previousLayer[0] != None and isPaintLayerNode(previousLayer[0]):
            
            while len(layerNode.outputs["colorOutput"].links) > 0:
                mainTree.links.remove(layerNode.outputs["colorOutput"].links[0])
            while len(layerNode.outputs["alphaOutput"].links) > 0:
                mainTree.links.remove(layerNode.outputs["alphaOutput"].links[0])
            
            while len(layerNode.inputs["colorBelow"].links) > 0:
                mainTree.links.remove(layerNode.inputs["colorBelow"].links[0])
            while len(layerNode.inputs["alphaBelow"].links) > 0:
                mainTree.links.remove(layerNode.inputs["alphaBelow"].links[0])
                
            if nextLayer[0] != None:    
                mainTree.links.new(previousLayer[0].outputs["colorOutput"], nextLayer[0].inputs[nextLayer[1]]) 
            if nextAlphaLayer[0] != None: 
                mainTree.links.new(previousLayer[0].outputs["alphaOutput"], nextAlphaLayer[0].inputs[nextAlphaLayer[1]]) 
                 
            selectNode(previousLayer[0])
            #newLayerID = selectedLayerID
                 
        elif nextLayer[0] == None and previousLayer[0] != None:
            newLayerID = 0
            selectNode(previousLayer[0])
            
        elif nextLayer[0] != None and previousLayer[0] == None or validPreviousLayer == False:
            #newLayerID = selectedLayerID - 1
            
            nextTextureLayer = conectedFromNode(nextLayer[0], "Color")[0]
            
            if isPaintLayerNode(nextLayer[0]):
                while len(nextLayer[0].inputs["colorBelow"].links) > 0:
                    mainTree.links.remove(nextLayer[0].inputs["colorBelow"].links[0])
                while len(nextLayer[0].inputs["alphaBelow"].links) > 0:    
                    mainTree.links.remove(nextLayer[0].inputs["alphaBelow"].links[0])
            
                #mainTree.links.new(nextLayer[0].inputs["colorBelow"],nextTextureLayer.outputs["Color"])
                if nextLayer[0] != None and nextTextureLayer != None:
                    mainTree.links.new(nextLayer[0].inputs["alphaBelow"],nextTextureLayer.outputs["Alpha"])
            
            if nextLayer[0] != None:
                selectNode(nextLayer[0])
            
        elif nextLayer[0] == None and previousLayer[0] == None:
            deselectAllNodes()
            mainTree.nodes.active = None                 
        

        removeNodeTree(mainTree, layerNode)
                
    else:
        textureNode = findTextureNode()
        if textureNode != None:
            mainTree.nodes.remove(textureNode)
    
        
    #updateUILayerTree()
    
def isPaintLayerNode(pLayerNode):
    
    isLayer = False
    if pLayerNode != None:
        
        hasNodeTree = hasattr(pLayerNode, "node_tree")
        if hasNodeTree:
            treeName = pLayerNode.node_tree.name
            finder = treeName.find("PaintLayer")

            if finder > -1:
                isLayer = True
                    
    return isLayer



    
def sortNodesPosition(pLayerNode, pTextureNode, pUvNode, pPosition):
    
    pLayerNode.location = [0,0]
    pTextureNode.location =[0,0]
    pUvNode.location = [0,0]
    
    pTextureNode.location[0] = pTextureNode.width * (pPosition*1.2)
    pTextureNode.location[1] -= (pLayerNode.height*0.65)
    
    pUvNode.location[0] = pTextureNode.location[0]
    pUvNode.location[1] -= ((pTextureNode.height + pLayerNode.height)*0.65)
     
          
def insertNode(pCurrentTree, pCurrentNode, pNewLayer):
    
    if pCurrentNode != None and pNewLayer != None:
        if len(pCurrentNode.outputs["colorOutput"].links) > 0:
            
            numLinks = len(pCurrentNode.outputs["colorOutput"].links) 
            if numLinks > 0:
                l = 0
                while l < numLinks:
                    toNode = pCurrentNode.outputs["colorOutput"].links[0].to_node
                    toSocket = pCurrentNode.outputs["colorOutput"].links[0].to_socket.name
                    pCurrentTree.links.new(pNewLayer.outputs["colorOutput"], toNode.inputs[toSocket])
                    l += 1
                
            numLinks = len(pCurrentNode.outputs["alphaOutput"].links)
            if numLinks > 0: 
                l = 0
                while l < numLinks:
                    toAlphaNode = pCurrentNode.outputs["alphaOutput"].links[0].to_node
                    toAlphaSocket = pCurrentNode.outputs["alphaOutput"].links[0].to_socket.name
                    pCurrentTree.links.new(pNewLayer.outputs["alphaOutput"], toAlphaNode.inputs[toAlphaSocket])
                    l += 1
                                
        pCurrentTree.links.new(pCurrentNode.outputs["colorOutput"], pNewLayer.inputs["colorBelow"])
        pCurrentTree.links.new(pCurrentNode.outputs["alphaOutput"], pNewLayer.inputs["alphaBelow"])
    
    else:
        out_color = getActiveLayerSetOutput("Color")
        out_alpha = getActiveLayerSetOutput("Alpha")
        
        if pNewLayer != None and out_color != None and out_alpha != None: 
            pCurrentTree.links.new(pNewLayer.outputs["colorOutput"], out_color.inputs["Input"])
            pCurrentTree.links.new(pNewLayer.outputs["alphaOutput"], out_alpha.inputs["Input"])
        
        
        
        
def connectTexture(pNodeTree, pTextureNode, pLayerNode, pConnectTo, pPosition):
    
    pNodeTree.links.new(pTextureNode.outputs["Color"], pLayerNode.inputs[pConnectTo])            

def createUvNode(pNodeTree, pTextureNode):
    
    uvNode = pNodeTree.nodes.new("ShaderNodeUVMap")
    if len(bpy.context.object.data.uv_layers) > 0:
        uvNode.uv_map = bpy.context.object.data.uv_layers.active.name
    pNodeTree.links.new(uvNode.outputs["UV"], pTextureNode.inputs["Vector"])
    
    return uvNode 

#---- Create Paint shader
    
def createPaintingShader(pMainTree):
    
    paintShader = None
    existPaintShaderGroup = bpy.data.node_groups.find('MTPaintShader')
    
    if existPaintShaderGroup < 0:
        create_mtPaintShader()
    
    paintingShaderNodeID = pMainTree.nodes.find('MTPaintShader')
    
    if paintingShaderNodeID < 0: #can be only one
        paintShader = pMainTree.nodes.new(type="ShaderNodeGroup")    
        paintShader.node_tree = bpy.data.node_groups['MTPaintShader']
        paintShader.label = "Painting Shader"
        paintShader.name = "MTPaintShader"
        #paintShader.parent = newLayerSetFrame
        paintShader.location = (600,0)
    else:
        paintShader = pMainTree.nodes[paintingShaderNodeID]
        
    return paintShader

def toogleShadeless(pMainTree):
    
    paintingShaderNodeID = pMainTree.nodes.find('MTPaintShader')
    if paintingShaderNodeID > -1:
        paintingShaderNode = pMainTree.nodes[paintingShaderNodeID]
        
        if paintingShaderNode.inputs['Shadeless'].default_value == 0:
            paintingShaderNode.inputs['Shadeless'].default_value = 1
        else: 
            paintingShaderNode.inputs['Shadeless'].default_value = 0
        
def toogleTransparency(pMainTree):
    
    paintingShaderNodeID = pMainTree.nodes.find('MTPaintShader') 
    if paintingShaderNodeID > -1:
        paintingShaderNode = pMainTree.nodes[paintingShaderNodeID]
        
        if paintingShaderNode.inputs['Transparent'].default_value == 0:
            paintingShaderNode.inputs['Transparent'].default_value = 1
        else: 
            paintingShaderNode.inputs['Transparent'].default_value = 0
        
                  
def createColorLayerGroup(pName):
    
    newLayer = None
    mainTree = bpy.context.object.active_material.node_tree
    newLayer = mainTree.nodes.new(type="ShaderNodeGroup")
    newLayer.node_tree = bpy.data.node_groups['MTPaintLayer_Color'].copy()    
    setLayerName(newLayer, pName)
    
    return newLayer

def createFilterLayerGroup(pName):
    
    newLayer = None
    mainTree = bpy.context.object.active_material.node_tree
    newLayer = mainTree.nodes.new(type="ShaderNodeGroup")
    newLayer.node_tree = bpy.data.node_groups['MTPaintLayer_Filter'].copy()    
    setLayerName(newLayer, pName)
    
    return newLayer
               


def newLayerNode(pNewLayer, pLayerName, pBaseNode, pTextureImage):
    currentMatIndex = bpy.context.object.active_material_index
    numPaintTextures =  len(bpy.context.object.active_material.texture_paint_slots)
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    newLayer = None
    textureImage = None
    baseLayerSetNodeLocation = [0,0]
    
    mainTree = bpy.context.object.active_material.node_tree
    currentLayerNode = getLayerByType(pBaseNode)
    layerSetNode = getActiveLayerSetNode()
    
    if layerSetNode != None:
        
        baseLayerSetNodeLocation = layerSetNode.location.copy()
        layerSetNode.location = [0,0]
        
        newLayerFrame = createFrameLayer(mainTree, "layerContainer.Color")
        newLayerFrame.location = [0,0]
        newLayerFrame.parent = layerSetNode
             
        if pNewLayer == None:
            newLayer = createColorLayerGroup(pLayerName)
            textureImage = pTextureImage
        else:
            newLayer = mainTree.nodes.new(type="ShaderNodeGroup")
            newLayer.name = pNewLayer.name
            newLayer.node_tree = pNewLayer.node_tree
            if pTextureImage != None:
                textureImage = pTextureImage.copy()
                
        if textureImage != None: 
            textureImage.name = bpy.context.object.active_material.name + "_" + newLayer.name + "_color"
         
        
        newColorTexture = newTextureNode(mainTree, textureImage)
        newUvNode = createUvNode(mainTree, newColorTexture)
        
        if newLayer != None:
            newLayer.hide = True
        if newColorTexture != None:
            newColorTexture.hide = True
        if newUvNode != None:
            newUvNode.hide = True
        #--- connect color texture ---- #
        
        mainTree.links.new(newColorTexture.outputs["Color"], newLayer.inputs["Color"])   
        mainTree.links.new(newColorTexture.outputs["Alpha"], newLayer.inputs["ColorAlpha"])   
        
        #mainTree.links.new(newColorTexture.outputs["Color"], newLayer.inputs["colorBelow"])   
        mainTree.links.new(newColorTexture.outputs["Alpha"], newLayer.inputs["alphaBelow"])   
        
        newLayer.location = [0,0]
        newColorTexture.location = [0,0]
        newUvNode.location = [0,0]
        
        newLayer.parent = newLayerFrame
        newColorTexture.parent = newLayerFrame
        newUvNode.parent = newLayerFrame
        
        
        
        #---- put it in right position --------#
        
        #if currentLayerNode != None: 
        insertNode(mainTree, currentLayerNode, newLayer)

        sortNodesPosition(newLayer, newColorTexture, newUvNode, 0)
        
        
        if currentLayerNode != None:
            selectNode(currentLayerNode)
        else:
            selectNode(newLayer)
       
        #--- put layer set node in the previous location ----#
         
        layerSetNode.location = baseLayerSetNodeLocation
        
         
        
    return newLayer    

def newFilterLayerNode(pNewLayer, pLayerName, pBaseNode, pTextureImage):
    
    currentMatIndex = bpy.context.object.active_material_index
    numPaintTextures =  len(bpy.context.object.active_material.texture_paint_slots)
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    newLayer = None
    textureImage = None
    baseLayerSetNodeLocation = [0,0]
    
        
    mainTree = bpy.context.object.active_material.node_tree
    currentLayerNode = getLayerByType(pBaseNode)
    layerSetNode = getActiveLayerSetNode()
    
    if layerSetNode != None:
        
        baseLayerSetNodeLocation = layerSetNode.location.copy()
        layerSetNode.location = [0,0]
            
        newLayerFrame = createFrameLayer(mainTree, "layerContainer.Filter")
        newLayerFrame.location = [0,0]
        newLayerFrame.parent = layerSetNode
             
        if pNewLayer == None:
            newLayer = createFilterLayerGroup(pLayerName)
            textureImage = pTextureImage
        else:
            newLayer = mainTree.nodes.new(type="ShaderNodeGroup")
            newLayer.name = pNewLayer.name
            newLayer.node_tree = pNewLayer.node_tree
            textureImage = pTextureImage.copy()
        
        if textureImage != None: 
            textureImage.name = bpy.context.object.active_material.name + "_" + newLayer.name + "_mask"
            
        newMaskTexture = newTextureNode(mainTree, textureImage)
        newUvNode = createUvNode(mainTree, newMaskTexture)
        
        if newLayer != None:
            newLayer.hide = True
        if newMaskTexture != None:
            newMaskTexture.hide = True
        if newUvNode != None:
            newUvNode.hide = True
            
        #--- connect color texture ---- #
        
        mainTree.links.new(newMaskTexture.outputs["Color"], newLayer.inputs["Mask"])    
        
        newLayer.location = [0,0]
        newMaskTexture.location = [0,0]
        newUvNode.location = [0,0]
        
        newLayer.parent = newLayerFrame
        newMaskTexture.parent = newLayerFrame
        newUvNode.parent = newLayerFrame
        
        newLayer.hide = True
        newMaskTexture.hide = True
        newUvNode.hide = True
        
        #---- put it in right position --------#
        
        if currentLayerNode != None: 
            insertNode(mainTree, currentLayerNode, newLayer)

        sortNodesPosition(newLayer, newMaskTexture, newUvNode, 0)
        selectNode(newLayer)
        
        #--- put layer set node in the previous location ----#
         
        layerSetNode.location = baseLayerSetNodeLocation 
        
    return newLayer  
    

def addLayerTexture(pPreviousTexture, pBaseNode, pTextureImage, pConnectTo, pPosition):
    
    textureCreated = False
    textureImage = None
    currentMatIndex = bpy.context.object.active_material_index
    mainTree = bpy.context.object.active_material.node_tree
    baseLayerSetNodeLocation = [0,0]
    
    currentLayerNode = getLayerByType(pBaseNode)
    
    if currentLayerNode != None: 
        
        #layerSetNode = getActiveLayerSetNode()
        baseLayerSetNodeLocation = currentLayerNode.parent.location.copy()
        currentLayerNode.parent.location = [0,0]
    
        if pPreviousTexture == False:
            textureImage = pTextureImage
        else:
            textureImage = pTextureImage.copy()
        
        textureImage.name = bpy.context.object.active_material.name + "_" + currentLayerNode.name
        
        if pPosition == 1:
            textureImage.name = bpy.context.object.active_material.name + "_" + currentLayerNode.name + "_mask"
            
        newTexture = newTextureNode(mainTree, textureImage)
        newUvNode = createUvNode(mainTree, newTexture)
        
        
        newTexture.hide = True
        newUvNode.hide = True
        
        newTexture.location = currentLayerNode.location
        newUvNode.location = currentLayerNode.location
        
        newTexture.parent = pBaseNode.parent
        newUvNode.parent = pBaseNode.parent
        
        #connectTexture(mainTree, newTexture , pBaseNode,  pConnectTo,pPosition)
        mainTree.links.new(newTexture.outputs["Color"], pBaseNode.inputs[pConnectTo])   
        
        sortNodesPosition(pBaseNode, newTexture, newUvNode, pPosition)
            
        if newTexture != None:
            textureCreated = True
        
        currentLayerNode.parent.location = baseLayerSetNodeLocation 
             
    return textureCreated 

def moveLayer(pCurrentLayer, pDirection):
    
    mainTree = bpy.context.object.active_material.node_tree
    activeLayerId = bpy.context.scene.layerTreeCollection_ID_index
    endLayerId = 0
    
    selectedLayer = getActiveLayer()
    mainTree.nodes.active = selectedLayer
    mainTree.nodes.active.select = True
    
    if pDirection == "UP":  
        if activeLayerId > 0:
            bpy.context.scene.layerTreeCollection_ID_index = activeLayerId
            pCurrentLayer = mainTree.nodes.active
            endLayerId = activeLayerId
        else:
            pCurrentLayer = None    
    elif pDirection == "DOWN":
        
        activeLayerId +=1
        if activeLayerId < len(bpy.context.scene.layerTreeCollection):
            bpy.context.scene.layerTreeCollection_ID_index = activeLayerId
            pCurrentLayer = mainTree.nodes.active
            endLayerId = activeLayerId - 1 
                
        else:
            pCurrentLayer = None
            
   
    if pCurrentLayer != None and isPaintLayerNode(pCurrentLayer):
        nextLayer = conectedToNode(pCurrentLayer, "colorOutput")[0]
        previousLayer = conectedFromNode(pCurrentLayer, "colorBelow")[0]
        
        if nextLayer != None and isPaintLayerNode(nextLayer):
            
            outCont = 0
            while outCont < len(pCurrentLayer.outputs):
                currentConnectTo = conectedToNode(pCurrentLayer, pCurrentLayer.outputs[outCont].name)
                nextConnectTo = conectedToNode(nextLayer, nextLayer.outputs[outCont].name)

                # next layer
                if nextLayer != None:
                    
                    #remove links
                    while len(pCurrentLayer.outputs[outCont].links) > 0:
                        mainTree.links.remove(pCurrentLayer.outputs[outCont].links[0])
                    while len(nextLayer.outputs[outCont].links) > 0:
                        mainTree.links.remove(nextLayer.outputs[outCont].links[0])
                    
                    #create links
                    
                    if nextConnectTo[0] != None:
                        mainTree.links.new(pCurrentLayer.outputs[outCont], nextConnectTo[0].inputs[nextConnectTo[1]])                
                    mainTree.links.new(nextLayer.outputs[outCont], pCurrentLayer.inputs[outCont])
                
                #previous layer
                
                if previousLayer != None:
                    isValidLayer = isPaintLayerNode(previousLayer)
                    if isValidLayer:
                        mainTree.links.new(previousLayer.outputs[outCont], nextLayer.inputs[outCont])
                    else:
                        mainTree.links.new(textureNode.outputs[outCont], nextLayer.inputs[outCont])
                
                outCont += 1
            
        bpy.context.scene.layerTreeCollection_ID_index = endLayerId
            
#-------------------------------------------- #

#------------ Getting layer nodes ------------#

def findLayerSets(pMainTree, pList):
    
    layerSets = []
    if pMainTree != None:
        for node in pMainTree.nodes:
            if node.name.find("layerSet.") > -1:
                #pList.add().name = node.name    
                layerSets.append(node)
                
    return layerSets

def findFirstLayer(pCurrentLayer):
    
    firstLayer = pCurrentLayer
    previousLayer = conectedFromNode(pCurrentLayer, "colorBelow")
    
    while previousLayer[0] != None and isPaintLayerNode(previousLayer[0]):
        firstLayer = previousLayer[0]
        previousLayer = conectedFromNode(previousLayer[0], "colorBelow")
        
        
    return firstLayer

def findLastLayer(pCurrentLayer):
    
    lastLayer = pCurrentLayer
    nextLayer = conectedToNode(pCurrentLayer, "colorOutput")[0]
    
    while nextLayer != None and isPaintLayerNode(nextLayer):
        lastLayer = nextLayer
        nextLayer = conectedToNode(nextLayer, "colorOutput")[0]    
    
    return lastLayer
    
def getLayerPosition(pCurrentLayer):
    
    firstLayer = None
    previousLayer = conectedFromNode(pCurrentLayer, "colorBelow")
    layerPos = 0
    
    while previousLayer[0] != None:
        layerPos += 1
        previousLayer = conectedFromNode(previousLayer[0], "colorBelow")
          
    return layerPos

def getLayerByPos(pPosition):
    layerSelected = findLayerNode()
    #firstLayer = findFirstLayer(layerSelected[0])
    firstLayer = findLastLayer(layerSelected[0])
    
    currentLayer = firstLayer
    
    for i in range(0, pPosition):
        if currentLayer != None:
            if isPaintLayerNode(currentLayer):
                nextLayer = conectedFromNode(currentLayer, "colorBelow")
                currentLayer = nextLayer[0]
        else:
            currentLayer = None
            break
    
    return currentLayer 
    
def getLayerByType(pBaseNode):
    
    currentNode = None
    mainTree = bpy.context.object.active_material.node_tree
    
    if pBaseNode != None:
        for node in mainTree.nodes:
            hasNodeTree = hasattr(node, "node_tree")
            if hasNodeTree and node.node_tree != None and pBaseNode.node_tree != None:
                if node.node_tree.name == pBaseNode.node_tree.name:
                    currentNode = node
    
    return currentNode        

def getLayerByTypeName(pBaseNodeName):
    
    currentNode = None
    mainTree = bpy.context.object.active_material.node_tree
    
    if pBaseNodeName != None and pBaseNodeName != "":
        for node in mainTree.nodes:
            hasNodeTree = hasattr(node, "node_tree")
            if hasNodeTree and node.node_tree != None:
                if node.node_tree.name == pBaseNodeName:
                    currentNode = node
    
    return currentNode        

def getActiveLayerSetNode():
    
    layerSetNode = None
    mainTree = bpy.context.object.active_material.node_tree
    
    if mainTree != None: 
        id = bpy.context.scene.mtLayerSets.find(bpy.context.scene.mtLayerSets_id)
        if id > -1:
            layerId = bpy.context.scene.mtLayerSets[id].layerSetID
            
            if mainTree != None:
                for node in mainTree.nodes:
                    if node.name == layerId:
                        layerSetNode = node
                        break
    
    return layerSetNode     

def getActiveLayerSetOutput(pType):
    
    mainTree = bpy.context.object.active_material.node_tree
    output = None
    
    layerSetNode = getActiveLayerSetNode()
    children = getNodeChildren(mainTree,layerSetNode)
    
    if pType.upper() == "COLOR":
        for n in children:
            if n.name.find("colorOutput") >= 0:
                output = n
                return n
                #break
                        
    elif pType.upper() == "ALPHA":
        for n in children:
            if n.name.find("alphaOutput") >= 0:
                output = n
                return n
                #break
         
    return output

def getActiveLayer():
    
    layerNode = None
    selectedNode = None
    layerSetNode = getActiveLayerSetNode()
    activeLayerId = bpy.context.scene.layerTreeCollection_ID_index
    
    numUILayers = len(bpy.context.scene.layerTreeCollection)
    
    if  numUILayers > activeLayerId:
        selectedNode = bpy.context.scene.layerTreeCollection[activeLayerId]
   
        
    if selectedNode != None:
        layerNode = getLayerByTypeName(selectedNode.layerNode)
    
    else:
        mainTree = bpy.context.object.active_material.node_tree
        if mainTree.nodes.active != None:
            if isPaintLayerNode(mainTree.nodes.active):
                layerNode = mainTree.nodes.active    
        
    return layerNode
    
    
#------------------------------------------------------#

#------- Layer Tree properties ------------#
    
def getLayerTree():
    
    uiLayerTree = []
    mainTree = bpy.context.object.active_material.node_tree
    
    #find and collect layer set node
    layerSetNode = getActiveLayerSetNode()

    if layerSetNode != None:
        
        firstLayer = None
        layerTree = getNodeChildren(mainTree,layerSetNode)
        for layerParent in layerTree:
            layer = getChildLayerNode(mainTree, layerParent)
            if layer != None and isPaintLayerNode(layer):
                firstLayer = findFirstLayer(layer)
                uiLayerTree.append(firstLayer)
                break
            
        if firstLayer != None:        
            currentLayer = conectedToNode(firstLayer, "colorOutput")
            while isPaintLayerNode(currentLayer[0]):
                uiLayerTree.append(currentLayer[0])
                currentLayer = conectedToNode(currentLayer[0], "colorOutput")

    uiLayerTree.reverse()
    
    return uiLayerTree

def getLayerProperties(pCurrentLayer):
    
    layerProperties = ["PAINT", False, False] # ["Type","HasColorTexture", "HasMaskTexture"] 
    mainTree = bpy.context.object.active_material.node_tree
    if isPaintLayerNode(pCurrentLayer):
        finder = pCurrentLayer.node_tree.name.find("Color")
        if finder >= 0:
            layerProperties[0] = "PAINT"
            colorLayer = conectedFromNode(pCurrentLayer, "Color")
            maskLayer = conectedFromNode(pCurrentLayer, "Mask")
            
            if colorLayer[0] != None:
                layerProperties[1] = True
            if maskLayer[0] != None:
                layerProperties[2] = True
    
        else:
            finder = pCurrentLayer.node_tree.name.find("Filter")
            if finder >= 0:
                layerProperties[0] = "FILTER" 
                maskLayer = conectedFromNode(pCurrentLayer, "Mask")
                if maskLayer[0] != None:
                    layerProperties[2] = True
    
    
        
    return layerProperties

def hasLocalFilter(pCurrentLayer):
    
    localFilters = False
    running = True
    if isPaintLayerNode(pCurrentLayer):
        layer = pCurrentLayer.node_tree.nodes["PL_LayerInput"]
        layer = conectedToNode(layer, "Color")[0]
        if layer != None and layer.type == "REROUTE":
            layer = conectedToNode(layer, "Output")[0]
            if layer != None and layer.type != "REROUTE":
                localFilters = True
        elif layer != None and layer.type != "REROUTE":
            localFilters = True
            
    return localFilters

#------------- UI sorting -----------------#

def updateUILayerTree():
    
    layerTree = getLayerTree()
    mainTree = bpy.context.object.active_material.node_tree
    selectedLayer = mainTree.nodes.active
    #selectedLayer = getActiveLayer()
    #mainTree.nodes.active = selectedLayer
    currentLayerId = bpy.context.scene.layerTreeCollection_ID_index
    
    if currentLayerId < 0:
        currentLayerId = 0
        
    bpy.context.scene.layerTreeCollection.clear()
    
    cont = 0
    for layer in layerTree: 
        layerName = getLayerName(layer)
        newLayer = bpy.context.scene.layerTreeCollection.add()
        layerProperties = getLayerProperties(layer)  
        newLayer.name = layer.name
        newLayer.layerID = cont
        newLayer.layerName = layerName
        newLayer.layerNode = layer.node_tree.name
        newLayer.localFilters = hasLocalFilter(getLayerByTypeName(newLayer.layerNode))
        
   
        # -- update node label ---#
        if layerName != layer.label:
            setLayerName(layer, layerName)
       
        
        if layerProperties[0] == "PAINT":   
            newLayer.isRGBLayer = True
            newLayer.isFilterLayer =  False
        elif layerProperties[0] == "FILTER": 
            newLayer.isRGBLayer = False
            newLayer.isFilterLayer =  True
            
        newLayer.hasColorTexture = layerProperties[1]
        newLayer.hasMaskTexture = layerProperties[2]
        
        if layer.select and not newLayer.selected:
            newLayer.selected = selectedLayer.select
            bpy.context.scene.layerTreeCollection_ID_index = cont
        cont += 1
    
    return layerTree



def sortUINodeTree(pCurrentLayer):
    
    basePosition = None
    pCurrentLayer = getActiveLayer()
    
    if isPaintLayerNode(pCurrentLayer):        
        firstLayer = findFirstLayer(pCurrentLayer)
        #sortNodesPosition(firstLayer) 
        
        firstLayer.parent.location = [0,0]
        base_YPosition = firstLayer.parent.location[1]
        previousLocation = firstLayer.parent.location
        previousFrameWidth = firstLayer.parent.width 
        
        layer = conectedToNode(firstLayer, "colorOutput")[0]
        
        cont = 0
        while layer != None and isPaintLayerNode(layer):
            
            layer.parent.location = [previousLocation[0],0]
            layer.parent.location[0] += (previousFrameWidth+10)
            previousLocation = layer.parent.location
            previousFrameWidth = layer.parent.width
            layer = conectedToNode(layer, "colorOutput")[0]
            cont += 1
        
        layerSetOut_color = getActiveLayerSetOutput("Color")
        layerSetOut_alpha = getActiveLayerSetOutput("Alpha")
        
        layerSetOut_color.location = previousLocation + mathutils.Vector([100 + previousFrameWidth, 0])
        layerSetOut_alpha.location = previousLocation + mathutils.Vector([100 + previousFrameWidth, -50])
        
    updateUILayerTree()
       
    

#------- Connect to shader --------------#
            
def getSameTypeShaderNode(pShaderNode):
    
    shaderNode = None
    
    mainTree = bpy.context.object.active_material.node_tree
    for node in mainTree.nodes:
        if node.type == pShaderNode.type:
            shaderNode = node
            break
        
    return shaderNode
            
def connectToShader(pLayer, pShaderNode, pShaderSlot, pSearch):
    
    connected = False
    shaderNode = pShaderNode
    mainTree = bpy.context.object.active_material.node_tree    
    
    if pSearch:
        shaderNode = getSameTypeShaderNode(pShaderNode)

    if shaderNode != None:
        if hasInput(pShaderNode, pShaderSlot):
            mainTree.links.new(pLayer.outputs["colorOutput"], shaderNode.inputs[pShaderSlot])  
                
    return connected
      
def makeNameUnique(pName, pCollection):
    
    newName = pName 
    for i in range(0, len(pCollection)):
        image = pCollection[i]
        if image.name == newName:
            if len(newName) > 3:
                if newName[-4] == '.':
                    
                    newIndex = sumToIndex(newName[-3:])
                    newName = newName[:-3] + newIndex
                    
                else:
                    newName = newName + ".001"    
            else:
                newName = newName + ".001"
        
        i = 0
                
    return newName     
            
def createFrameLayer(pCurrentTree, pType):
    
    newFrame= pCurrentTree.nodes.new(type="NodeFrame")
    newFrame.name = pType
    newFrame.label = pType
    

    return newFrame
            
def addLayerSet(pMainTree, pName, pAddToList):
    
    name = pName
    newLayerSet = None
    layerSetName = name
    layerSetId = "layerSet." + name
    
    if pAddToList:
        name = makeNameUnique(pName, bpy.context.scene.mtLayerSets)
        newLayerSet = bpy.context.scene.mtLayerSets.add()  
        
        layerSetName = name
        layerSetId = "layerSet." + name
      
        newLayerSet.name = layerSetName
        newLayerSet.layerSetID = layerSetId

    newLayerSetFrame = createFrameLayer(pMainTree, layerSetId)
    
    
    #-- Creates outputs ---#
    
    frameOutput_color = pMainTree.nodes.new(type="NodeReroute")
    frameOutput_color.name = layerSetId + "_colorOutput"
    frameOutput_color.label = "Color Output"
    
    frameOutput_alpha = pMainTree.nodes.new(type="NodeReroute")
    frameOutput_alpha.name = layerSetId + "_alphaOutput"
    frameOutput_alpha.label = "Alpha Output"
    
    frameOutput_color.location = [0,0]
    frameOutput_alpha.location = [0,0]
    
    frameOutput_color.parent = newLayerSetFrame
    frameOutput_alpha.parent = newLayerSetFrame
    
    frameOutput_color.location = [300,0]
    frameOutput_alpha.location = [300,-50]
    
    
    
    
    #----#
    # Create painting shader and connect layer set to it
    
    bpy.context.scene.mtLayerSets_id  = bpy.context.scene.mtLayerSets[len(bpy.context.scene.mtLayerSets)-1].name
    
    paintShaderNode = createPaintingShader(pMainTree)
    
    pMainTree.links.new(frameOutput_color.outputs[0], paintShaderNode.inputs["Color"])
    pMainTree.links.new(frameOutput_alpha.outputs[0], paintShaderNode.inputs["Alpha"])
    
    
    return newLayerSetFrame

def renameLayerSetNode(pMainTree, pName):
    
    name = pName
    layerSetId = "" 
    layerSetNode = getActiveLayerSetNode()
    
    if layerSetNode != None:
        
        colorOutputId = layerSetNode.name + "_colorOutput"
        alphaOutputId = layerSetNode.name + "_alphaOutput"
        
        layerSetId = "layerSet." + name  
        layerSetNode.name = layerSetId
        layerSetNode.label = layerSetId
        
        pMainTree.nodes[colorOutputId].name = layerSetId + "_colorOutput"
        pMainTree.nodes[alphaOutputId].name = layerSetId + "_alphaOutput"
        
    return layerSetId        

def renameLayerSet(pMainTree, pName):
    
    name = pName
    layerSetId = "layerSet." + name

    id = bpy.context.scene.mtLayerSets.find(bpy.context.scene.mtLayerSets_id)
    bpy.context.scene.mtLayerSets[id].name = name
    bpy.context.scene.mtLayerSets[id].layerSetID = layerSetId    
    bpy.context.scene.mtLayerSets_id = name
    
        
    return name
        
def deleteLayerSetNode(pMainTree):
    
    mainTree = pMainTree
    id = bpy.context.scene.mtLayerSets.find(bpy.context.scene.mtLayerSets_id)
    
    #find and delete layer set nodes
    layerSetNode = getActiveLayerSetNode()

    if layerSetNode != None:
        
        layerTree = getNodeChildren(mainTree,layerSetNode)
        for layerParent in layerTree:
            layer = getChildLayerNode(mainTree, layerParent)
            if layer != None and isPaintLayerNode(layer):
                deleteLayerNode(layer)
            elif layer == None:
                mainTree.nodes.remove(layerParent)
            
        mainTree.nodes.remove(layerSetNode)


def deleteLayerSetFromList(pMainTree):
    
    mainTree = pMainTree
    id = bpy.context.scene.mtLayerSets.find(bpy.context.scene.mtLayerSets_id)

    #delete from list 
    bpy.context.scene.mtLayerSets.remove(id)
    
    # select another layer set
    if len(bpy.context.scene.mtLayerSets) > 0:
        bpy.context.scene.mtLayerSets_id  = bpy.context.scene.mtLayerSets[0].name
    else:
        bpy.context.scene.mtLayerSets_id = ""       
     

def selectLayerSet(pMainTree):
    
    mainTree = pMainTree
    if mainTree != None:
        unselectAllNodes(mainTree)
        layerSetNode = getActiveLayerSetNode()
       
        if layerSetNode != None :
            layers  = getNodeChildren(mainTree, layerSetNode)
            if len(layers) > 2:
                i = 0
                layerNodeParent = layers[i]
                while layerNodeParent != None and layerNodeParent.name.find("output") >= 0:
                    i += 1
                    layerNodeParent = layers[i]
                
                layerTmp = getChildLayerNode(mainTree, layerNodeParent)
                layer = findFirstLayer(layerTmp)
                layer.select = True
                mainTree.nodes.active = layer

def getFilderNodes():
    
    nodes = []
    listTypes = dir(bpy.types)
    for t in listTypes:
        if t.find("ShaderNode") > -1:
            nodes.append(t)
    
    return nodes        
            
                        
# ----------------- Multi tile definitions -------------------- #


def connectPaintingShader(pMainTree, pLayerSetOutput, pTargetNode, pTargetNodeInput, pRemove):
    
    mainTree = pMainTree
    layer = getActiveLayer()
    #outputLayer = findLastLayer(layer)
    targetNode = findNodeByName(pTargetNode)
    
    outputLayer = mainTree.nodes['MTPaintShader']
    outputLayerSlot = mainTree.nodes['MTPaintShader'].outputs[0] #outputLayer.outputs[pLayerSetOutput]
    
    if outputLayer != None:
        if targetNode != None and  outputLayerSlot != None and targetNode.inputs.find(pTargetNodeInput) > -1:
            
            if pRemove == True:
                
                while len(outputLayerSlot.links) > 0:
                    mainTree.links.remove(outputLayerSlot.links[0]) 
                    
                while len(targetNode.inputs[pTargetNodeInput].links) > 0:
                    mainTree.links.remove(targetNode.inputs[pTargetNodeInput].links[0])    
                
            mainTree.links.new(outputLayerSlot, targetNode.inputs[pTargetNodeInput])
        
def multiTile_connectPaintingShader(pLayerSetOutput, pTargetNode, pTargetNodeInput, pRemove):
    
    mainTree = bpy.context.object.active_material.node_tree
    currentMatIndex = bpy.context.object.active_material_index
    numMaterials = len(bpy.context.object.material_slots)
    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            bpy.context.object.active_material_index = i
            currentTree = bpy.context.object.active_material.node_tree
            #------ action  here
            connectPaintingShader(currentTree, pLayerSetOutput, pTargetNode, pTargetNodeInput, pRemove)        
            #-----------
          
        bpy.context.object.active_material_index = currentMatIndex
    else:
        connectPaintingShader(mainTree, pLayerSetOutput, pTargetNode, pTargetNodeInput, pRemove)
    

           
           
def multitile_createPaintingShader():
    
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    mainTree = bpy.context.object.active_material.node_tree
    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            
            bpy.context.object.active_material_index = i
            currentTree = bpy.context.object.active_material.node_tree
            createPaintingShader(currentTree)
    else:
        createPaintingShader(mainTree)
    
    bpy.context.object.active_material_index =  currentMatIndex
    
def multitile_toogleShadeless():
    
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    mainTree = bpy.context.object.active_material.node_tree
    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            
            bpy.context.object.active_material_index = i
            currentTree = bpy.context.object.active_material.node_tree
            toogleShadeless(currentTree)
    else:
        toogleShadeless(mainTree)
    
    bpy.context.object.active_material_index =  currentMatIndex

def multitile_toogleTransparency():
    
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    mainTree = bpy.context.object.active_material.node_tree
    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            
            bpy.context.object.active_material_index = i
            currentTree = bpy.context.object.active_material.node_tree
            toogleTransparency(currentTree)
    else:
        toogleTransparency(mainTree)
    
    bpy.context.object.active_material_index =  currentMatIndex
    
def multitile_addLayerSet(pName):

    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    mainTree = bpy.context.object.active_material.node_tree
    
    addToList = True
    newLayerSet  = None
    
    #paintShaderNode = create_mtPaintShader()
    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            
            bpy.context.object.active_material_index = i
            currentTree = bpy.context.object.active_material.node_tree
            addLayerSet(currentTree,pName, addToList)
            addToList = False

    else:
        addLayerSet(mainTree,pName, addToList)
    
    bpy.context.object.active_material_index =  currentMatIndex        

def multitile_renameLayerSet(pName):
    
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    newName = ""
    
    numMaterials = len(bpy.context.object.material_slots)   
    mainTree = bpy.context.object.active_material.node_tree
    
    name = makeNameUnique(pName, bpy.context.scene.mtLayerSets)
    
    if bpy.context.scene.multitileSelectionActive:

        for i in range(0,numMaterials):
            
            bpy.context.object.active_material_index = i
            currentTree = bpy.context.object.active_material.node_tree
            renameLayerSetNode(mainTree, name)
            
        renameLayerSet(currentTree,name)    
        
    else:
        renameLayerSetNode(mainTree,name)
        renameLayerSet(mainTree,name)
        
        
    bpy.context.object.active_material_index =  currentMatIndex        



def multitile_deleteLayerSet():

    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    mainTree = bpy.context.object.active_material.node_tree

    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            bpy.context.object.active_material_index = i
            currentTree = bpy.context.object.active_material.node_tree
            deleteLayerSetNode(currentTree)
        
        deleteLayerSetFromList(mainTree)   
    else:
        deleteLayerSetNode(mainTree)
        deleteLayerSetFromList(mainTree)
    
    bpy.context.object.active_material_index =  currentMatIndex  
        

def multiTile_selectLayer(pPaintingSpace):
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    
    mainTree = bpy.context.object.active_material.node_tree
    #selectedLayer = mainTree.nodes.active
    selectedLayer = getActiveLayer()
    mainTree.nodes.active = selectedLayer
    mainTree.nodes.active.select = True
    
    if bpy.context.scene.multitileSelectionActive:
        if isPaintLayerNode(selectedLayer) == True:
            for i in range(0,numMaterials):
                
                #if not is the base active material
                if i != currentMatIndex:
                    bpy.context.object.active_material_index = i
                    #------ action  here
                    selectPaintSlotTexture(selectedLayer, pPaintingSpace)
                    #-----------
            
        bpy.context.object.active_material_index = currentMatIndex   
        selectedLayer = getActiveLayer()
        mainTree.nodes.active = selectedLayer
        mainTree.nodes.active.select = True
        #selectedLayer = mainTree.nodes.active
        selectPaintSlotTexture(selectedLayer, pPaintingSpace)
        
    else:
        selectPaintSlotTexture(selectedLayer, pPaintingSpace)
        
    
            
def multiTile_addLayer(pLayerName, pTextureImage, pConnectToShader, pShaderSlot):    
    
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    
    mainTree = bpy.context.object.active_material.node_tree
    selectedLayer = getActiveLayer()
    mainTree.nodes.active = selectedLayer
    selectedShaderNode = getActiveLayer()
    mainTree.nodes.active = selectedShaderNode
    
    if selectedLayer != None: 
        mainTree.nodes.active.select = True
    
    if isPaintLayerNode(selectedLayer) == False or mainTree.nodes.active.select == False:
        selectedLayer = None
        
    newLayer = None
    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            bpy.context.object.active_material_index = i
            #------ action  here
            newLayer = newLayerNode(newLayer, pLayerName, selectedLayer,pTextureImage)
            currentLayer = bpy.context.object.active_material.node_tree.nodes.active  
            sortUINodeTree(currentLayer)
            selectPaintSlotTexture(currentLayer,bpy.context.scene.mtlayerPaintingSpace)
            
            if pConnectToShader:
                connectToShader(newLayer, selectedShaderNode, pShaderSlot, True)           
            #-----------
          
        bpy.context.object.active_material_index = currentMatIndex
    else:
        newLayer = newLayerNode(newLayer, pLayerName, selectedLayer, pTextureImage)
        sortUINodeTree(mainTree.nodes.active)
        
        if pConnectToShader:
            connectToShader(newLayer, selectedShaderNode, pShaderSlot, False)   
                
    
def multiTile_addLayerFilter(pLayerName, pTextureImage):
    
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    
    mainTree = bpy.context.object.active_material.node_tree
    #selectedLayer = mainTree.nodes.active
    selectedLayer = getActiveLayer()
    mainTree.nodes.active = selectedLayer
    mainTree.nodes.active.select = True
    
    if isPaintLayerNode(selectedLayer) == False or mainTree.nodes.active.select == False:
        selectedLayer = None
        
    newFilterLayer = None
    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            bpy.context.object.active_material_index = i
            #------ action  here
            newFilterLayer = newFilterLayerNode(newFilterLayer, pLayerName, selectedLayer,pTextureImage)
            currentFilterLayer = bpy.context.object.active_material.node_tree.nodes.active  
            sortUINodeTree(currentFilterLayer)
            #-----------
            
        bpy.context.object.active_material_index = currentMatIndex
    else:
        newFilterLayer = newFilterLayerNode(newFilterLayer, pLayerName, selectedLayer,pTextureImage)
        sortUINodeTree(mainTree.nodes.active)
    
        
def multiTile_addLayerMask(pTextureImage):    
    
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    
    mainTree = bpy.context.object.active_material.node_tree
    #selectedLayer = mainTree.nodes.active
    selectedLayer = getActiveLayer()
    mainTree.nodes.active = selectedLayer
    mainTree.nodes.active.select = True
    
    if isPaintLayerNode(selectedLayer) == False or mainTree.nodes.active.select == False:
        selectedLayer = None
        
    previousTexture = False
    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            bpy.context.object.active_material_index = i
            #------ action  here
            currentLayer = bpy.context.object.active_material.node_tree.nodes.active
            previousTexture = addLayerTexture (previousTexture, currentLayer,pTextureImage, "Mask",1)
            currentLayer = bpy.context.object.active_material.node_tree.nodes.active  
            sortUINodeTree(currentLayer)
            #-----------
            
        bpy.context.object.active_material_index = currentMatIndex
    else:
        previousTexture = addLayerTexture(previousTexture, selectedLayer,pTextureImage, "Mask",1)
        sortUINodeTree(mainTree.nodes.active)
    
        
def multiTile_deleteLayer():    
    
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    
    mainTree = bpy.context.object.active_material.node_tree
    #selectedLayer = mainTree.nodes.active
    selectedLayer = getActiveLayer()
    
    
    if selectedLayer != None:
        
        mainTree.nodes.active = selectedLayer
        mainTree.nodes.active.select = True
    
        if bpy.context.scene.multitileSelectionActive:
        
            for i in range(0,numMaterials):
                if i != currentMatIndex:
                    bpy.context.object.active_material_index = i
                    #------ action  here
                    deleteLayerNode(selectedLayer)
                    currentLayer = bpy.context.object.active_material.node_tree.nodes.active  
                    sortUINodeTree(currentLayer)
                #-----------
            
            
            bpy.context.object.active_material_index = currentMatIndex
            deleteLayerNode(selectedLayer)
            sortUINodeTree(mainTree.nodes.active)
            
        else:
            deleteLayerNode(selectedLayer)
            sortUINodeTree(mainTree.nodes.active)
    

def multiTile_saveTexturesLayer(pFilePath, pAction):
    
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    
    mainTree = bpy.context.object.active_material.node_tree
    #selectedLayer = mainTree.nodes.active
    selectedLayer = getActiveLayer()
    mainTree.nodes.active = selectedLayer
    mainTree.nodes.active.select = True
    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            bpy.context.object.active_material_index = i
            #------ action  here
            layerNode = getLayerByType(selectedLayer)
            saveTexturesLayer(layerNode, pFilePath, pAction)
            #-----------
        
        bpy.context.object.active_material_index = currentMatIndex
        
    else:
        saveTexturesLayer(selectedLayer, pFilePath, pAction)
                
def multiTile_packTexturesLayer():
    
    
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    
    mainTree = bpy.context.object.active_material.node_tree
    #selectedLayer = mainTree.nodes.active
    selectedLayer = getActiveLayer()
    mainTree.nodes.active = selectedLayer
    mainTree.nodes.active.select = True
    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            bpy.context.object.active_material_index = i
            
            #------ action  here
            layerTree = getLayerTree()
            
            for layer in layerTree:
                layerNode = getLayerByType(layer)
                packTexturesLayer(layerNode)
                
            #-----------
        
        bpy.context.object.active_material_index = currentMatIndex
        
    else:
        
        for layer in bpy.context.scene.layerTreeCollection:
            layerNode = getLayerByTypeName(layer.layerNode)
            packTexturesLayer(layerNode)
                   

def multiTile_propagateUVChannel():
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    
    mainTree = bpy.context.object.active_material.node_tree
    #selectedLayer = mainTree.nodes.active
    selectedLayer = getActiveLayer()
    mainTree.nodes.active = selectedLayer
    mainTree.nodes.active.select = True
    
    mainUVNode = getUVNode(selectedLayer,bpy.context.scene.mtlayerPaintingSpace)
    
    print("entra ", mainUVNode)
    if mainUVNode != None:
        if bpy.context.scene.multitileSelectionActive:
            print("entra 2")
            for i in range(0,numMaterials):
                if i != currentMatIndex:
                    bpy.context.object.active_material_index = i
                    #------ action  here
                    layer = getLayerByType(selectedLayer)
                    print("layer ",layer)
                    layerUVNode = getUVNode(layer, bpy.context.scene.mtlayerPaintingSpace)
                    if layerUVNode != None:
                        layerUVNode.uv_map = mainUVNode.uv_map
                    #-----------
                
            bpy.context.object.active_material_index = currentMatIndex
        
    
def multiTile_propagateTexture():
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    
    mainTree = bpy.context.object.active_material.node_tree
    #selectedLayer = mainTree.nodes.active
    selectedLayer = getActiveLayer()
    mainTree.nodes.active = selectedLayer
    mainTree.nodes.active.select = True
    
    textureNode = getTextureNode(selectedLayer, bpy.context.scene.mtlayerPaintingSpace )
    

    if textureNode != None:
        if bpy.context.scene.multitileSelectionActive:
        
            for i in range(0,numMaterials):
                if i != currentMatIndex:
                    bpy.context.object.active_material_index = i
                    #------ action  here
                    layer = getLayerByType(selectedLayer)
                    if layer != None:
                       
                        propagateTexture(layer, textureNode,bpy.context.scene.mtlayerPaintingSpace)
                        
                    #-----------
            
            bpy.context.object.active_material_index = currentMatIndex
            
    
def multTile_sortUINodeTree():
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    
    mainTree = bpy.context.object.active_material.node_tree
    #selectedLayer = mainTree.nodes.active
    
    selectedLayer = getActiveLayer()
    if selectedLayer != None:
        mainTree.nodes.active = selectedLayer
        mainTree.nodes.active.select = True
        
        if bpy.context.scene.multitileSelectionActive:
        
            for i in range(0,numMaterials):
                bpy.context.object.active_material_index = i
                #------ action  here
                layer = getLayerByType(selectedLayer)
                if layer != None:
                    sortUINodeTree(layer)
                #-----------
            
            bpy.context.object.active_material_index = currentMatIndex
        
        else:
            sortUINodeTree(selectedLayer)
                

def multitile_moveLayer(pDirection):    
    
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    
    mainTree = bpy.context.object.active_material.node_tree
    #selectedLayer = mainTree.nodes.active
    
    selectedLayer = getActiveLayer()
    mainTree.nodes.active = selectedLayer
    mainTree.nodes.active.select = True
    
    selectedShaderNode = mainTree.nodes.active
    
    if isPaintLayerNode(selectedLayer) == False or mainTree.nodes.active.select == False:
        selectedLayer = None
        
    newLayer = None
    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            bpy.context.object.active_material_index = i
            #------ action  here
            layer = getLayerByType(selectedLayer)
            if layer != None:
                moveLayer(layer, pDirection)         
            #-----------
          
        bpy.context.object.active_material_index = currentMatIndex
    else:
        moveLayer(selectedLayer, pDirection)
            

def multitile_useCurrentShader():    
    
    currentMatIndex = bpy.context.object.active_material_index
    currentPaintIndex = bpy.context.object.active_material.paint_active_slot
    
    numMaterials = len(bpy.context.object.material_slots)
    
    mainTree = bpy.context.object.active_material.node_tree
    
    selectedLayer = getActiveLayer()
    mainTree.nodes.active = selectedLayer
    mainTree.nodes.active.select = True
    
    selectedLayer = mainTree.nodes.active
    selectedShaderNode = mainTree.nodes.active
    
    lastLayer = getLastLayer(selectedLayer)
    currentShader = conectedToNode(lastLayer, "colorOutput")
    selectedLayer = lastLayer
    
    if bpy.context.scene.multitileSelectionActive and isPaintLayerNode(selectedLayer):
        for i in range(0,numMaterials):
            bpy.context.object.active_material_index = i
            #------ action  here
            layer = getLayerByType(selectedLayer)
            if layer != None:
                useCurrentShader(layer, currentShader[0], currentShader[1])         
            #-----------
          
        bpy.context.object.active_material_index = currentMatIndex
        
def multiTile_selectLayerSet():
    
    mainTree = bpy.context.object.active_material.node_tree
    currentMatIndex = bpy.context.object.active_material_index
    numMaterials = len(bpy.context.object.material_slots)
    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            bpy.context.object.active_material_index = i
            currentTree = bpy.context.object.active_material.node_tree
            #------ action  here
            selectLayerSet(currentTree)        
            #-----------
          
        bpy.context.object.active_material_index = currentMatIndex
    else:
        selectLayerSet(mainTree)
            

def connectLayerSet(pMainTree, pLayerSetOutput, pTargetNode, pTargetNodeInput, pRemove):
    
    mainTree = pMainTree
    layer = getActiveLayer()
    #outputLayer = findLastLayer(layer)
    targetNode = findNodeByName(pTargetNode)
    
    outputLayer = getActiveLayerSetOutput(pLayerSetOutput)
    outputLayerSlot = outputLayer.outputs["Output"] #outputLayer.outputs[pLayerSetOutput]
        
    if outputLayer != None:
        if targetNode != None and  outputLayerSlot != None and targetNode.inputs.find(pTargetNodeInput) > -1:
            
            if pRemove == True:
                
                while len(outputLayerSlot.links) > 0:
                    mainTree.links.remove(outputLayerSlot.links[0]) 
                    
                while len(targetNode.inputs[pTargetNodeInput].links) > 0:
                    mainTree.links.remove(targetNode.inputs[pTargetNodeInput].links[0])    
                
            mainTree.links.new(outputLayerSlot, targetNode.inputs[pTargetNodeInput])
        
    
def multiTile_connectLayerSet(pLayerSetOutput, pTargetNode, pTargetNodeInput, pRemove):
    
    mainTree = bpy.context.object.active_material.node_tree
    currentMatIndex = bpy.context.object.active_material_index
    numMaterials = len(bpy.context.object.material_slots)
    
    if bpy.context.scene.multitileSelectionActive:
        for i in range(0,numMaterials):
            bpy.context.object.active_material_index = i
            currentTree = bpy.context.object.active_material.node_tree
            #------ action  here
            connectLayerSet(currentTree, pLayerSetOutput, pTargetNode, pTargetNodeInput, pRemove)        
            #-----------
          
        bpy.context.object.active_material_index = currentMatIndex
    else:
                
        connectLayerSet(mainTree, pLayerSetOutput, pTargetNode, pTargetNodeInput, pRemove)
    

            
    
        
             
#--------------- properties callbacks -----------------#

def callback_editFilter(self, value):
    
    if bpy.context.scene.nodeFiltersSet_id != "":
        bpy.ops.vtools.mtopenfilterpanel('INVOKE_DEFAULT', filterNode = bpy.context.scene.nodeFiltersSet_id)
    
def callback_selectLayerSetUI(self, value):
    
    multiTile_selectLayerSet() 
    updateUILayerTree()
            
def callback_selectLayerUI(self, value):       
    selectedId = bpy.context.scene.layerTreeCollection_ID_index
    layerName = bpy.context.scene.layerTreeCollection[selectedId].layerNode
    layer = getLayerByTypeName(layerName)
    
    if not layer.select: 
        selectNode(layer)
    
    multiTile_selectLayer(bpy.context.scene.mtlayerPaintingSpace)
    collectInnerFilters()
    bpy.context.scene.nodeFiltersSet_id = ""
    
    
def callback_setColorSpace(self, value): 
    
    if self.selectColorSpace == "color":
        self.mtlayerPaintingSpace = True
    elif self.selectColorSpace == "mask":
        self.mtlayerPaintingSpace = False
        
    multiTile_selectLayer(bpy.context.scene.mtlayerPaintingSpace)
    updateUILayerTree()
        

def changeLayerNameUI(self, value):
    mainTree = bpy.context.object.active_material.node_tree
    #selectedLayer = mainTree.nodes.active
    selectedLayer = getActiveLayer()
    mainTree.nodes.active = selectedLayer
    
    
    if selectedLayer != None:
        mainTree.nodes.active.select = True 
        selectedLayerName = getLayerName(selectedLayer)
        selectedID = bpy.context.scene.layerTreeCollection_ID_index
    

        if self.layerID == selectedID and selectedLayer.node_tree.name == self.layerNode and self.layerName != selectedLayerName:
            setLayerName(selectedLayer,self.layerName)
        

def setAutosaveState(self, context):
    
    if bpy.context.scene.mtAutoPackAtive:
        bpy.ops.wm.mtpackimagesselectedlayer()
    

def updateFileNameFormat(self,context):
    self.filename_ext = bpy.context.scene.render.file_extension
                 
#----- Blender classes -----#

class VTOOLS_OP_selectLayerHandler(bpy.types.Operator):
    bl_idname = "vtools.selectlayerhandler"
    bl_label = "Start/Stop multi tile painting"
    
    lastNodeSelected = None  
    
   
    def execute(self,context):
        if context.scene.multitileSelectionActive == False:
            context.scene.multitileSelectionActive  = True
        else:
            context.scene.multitileSelectionActive  = False
           
        context.window_manager.modal_handler_add(self)            
        return {'RUNNING_MODAL'}
    
    
         
    def modal(self, context, event):
       
        active = context.scene.multitileSelectionActive  
        if active == True:
            mainTree = bpy.context.object.active_material.node_tree
            #selectedLayer = mainTree.nodes.active
            selectedLayer = getActiveLayer()
            mainTree.nodes.active = selectedLayer
            mainTree.nodes.active.select = True
            
            if self.lastNodeSelected  != selectedLayer:
                self.lastNodeSelected = selectedLayer
                if self.lastNodeSelected != None and isPaintLayerNode(self.lastNodeSelected) != False:
                    #selectedId = bpy.context.scene.layerTreeCollection_ID_index    
                    multiTile_selectLayer(bpy.context.scene.mtlayerPaintingSpace)    
                    
                    
            return {'PASS_THROUGH'}
        else:
            return {'FINISHED'} 
              
        return {'PASS_THROUGH'}    
    
class VTOOLS_OP_layerNodeSelector(bpy.types.Operator):
    bl_idname = "vtools.layernode"
    bl_label = "Layer node selector"
    bl_description = "Select this layer node"
    
    layerNode = bpy.props.StringProperty()
    
    def execute(self,context):
        if self.layerNode != None:
            layer = getLayerByTypeName(self.layerNode)
            selectNode(layer)
            
            multiTile_selectLayer(bpy.context.scene.mtlayerPaintingSpace)
                            
        return {'FINISHED'}
 
    
class VTOOLS_OP_mtAddNewLayer(bpy.types.Operator):
    bl_idname = "vtools.mtaddnewlayer"
    bl_label = "Create new layer"
    bl_description = "Add a new layer above the selected layer node"
    
    imageName = bpy.props.StringProperty(name="Name")
    imageWidth = bpy.props.IntProperty(name="Width", default=1024)
    imageHeight = bpy.props.IntProperty(name="Height", default=1024)
    imageColor = bpy.props.FloatVectorProperty(name="Image color", subtype='COLOR', size = 4, default=(0.0, 0.0, 0.0,0.0),min=0.0, max=1.0, description="color picker")
    imageDepth = bpy.props.BoolProperty(name="32 Bit Float Image", default = False) 
    isEmpty = bpy.props.BoolProperty(name="empty layer", default=False)
    connectToShaderNode = bpy.props.BoolProperty(name="Connected to Shader", default=False)
    shaderConnectionSlot = bpy.props.StringProperty(name = "Shader connection slot", default="Color")
    
    def execute(self, context):
        textureImage = None
        
        if not self.isEmpty:
            textureImage = newTextureImage(pName = self.imageName, pWidth = self.imageWidth, pHeight = self.imageHeight, pColor = self.imageColor, pAlpha = True, pFloat=self.imageDepth)
        
        multiTile_addLayer(self.imageName, textureImage, self.connectToShaderNode, self.shaderConnectionSlot)
        updateUILayerTree()
        
        
        #if len(bpy.context.scene.layerTreeCollection) == 1:
        #    bpy.ops.vtools.mtconnecttonode('INVOKE_DEFAULT')
        

        return {'FINISHED'}
 
    def invoke(self, context, event):
        self.imageName = "layer Name"
        
        existPaintLayerGroup = bpy.data.node_groups.find('MTPaintLayer_Color')
        existFilterLayerGroup = bpy.data.node_groups.find('MTPaintLayer_Filter')
        
        if existPaintLayerGroup == -1:
            create_mtColorNode()
            existPaintLayerGroup = bpy.data.node_groups.find('MTPaintLayer_Color')
            
        if existFilterLayerGroup == -1:
            create_mtFilterNode()
            existFilterLayerGroup = bpy.data.node_groups.find('MTPaintLayer_Filter')

        if existPaintLayerGroup > -1 and existFilterLayerGroup > -1:
            nodeLayerColor = bpy.data.node_groups[existPaintLayerGroup]
            nodeLayerFilter = bpy.data.node_groups[existFilterLayerGroup]
            
            nodeLayerColor.use_fake_user = True
            nodeLayerFilter.use_fake_user = True
            
            return context.window_manager.invoke_props_dialog(self) 
        else:
            self.report({'INFO'}, "MTPaintLayer_Color not found, please Append it") 
            self.connectToShaderNode = False
            return {'FINISHED'}

     
class VTOOLS_OP_mtDeleteInnerFilter(bpy.types.Operator):
    bl_idname = "vtools.mtdeleteinnerfilter"
    bl_label = "Delete Filter from Layer"
    bl_description = "Delete Layer from Filter"
    
    def collectInnerFilters(self):
        self.filtersSet_id = ""
        self.filtersSet.clear()
        mainTree = bpy.context.object.active_material.node_tree
        selectedLayer = getActiveLayer()
        mainTree.nodes.active = selectedLayer
        mainTree.nodes.active.select = True
        
        if isPaintLayerNode(selectedLayer):
            filters  = []
            filters = getFilters(selectedLayer)
            
            for f in filters:
                n = self.filtersSet.add()
                n.name = f.name
            
            self.filtersSet_id = ""
            
    filtersSet = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    filtersSet_id = bpy.props.StringProperty()
    
    def removeFilterNode(self, pSelectedLayer, pFilterNode):
        
        fromNode = None
        toNode = None
        activeInput = None
        activeOutput = None
        
        for input in pFilterNode.inputs:
            if len(input.links) > 0:
                activeInput = input
                fromNode = conectedFromNode(pFilterNode, input.name)
                break
            
        for output in pFilterNode.outputs:
            if len(output.links) > 0:
                activeOutput = output
                toNode = conectedToNode(pFilterNode, output.name)
                break
        
        pSelectedLayer.node_tree.nodes.remove(pFilterNode)  
        pSelectedLayer.node_tree.links.new(fromNode[0].outputs[fromNode[1]], toNode[0].inputs[toNode[1]])
        
            
        return {'FINISHED'}
    
    def execute(self, context):
        
        mainTree = bpy.context.object.active_material.node_tree
        selectedLayer = getActiveLayer()
        
        if selectedLayer != None:
            
            if self.filtersSet_id != "":
                fNode = selectedLayer.node_tree.nodes[self.filtersSet_id]
                self.removeFilterNode(selectedLayer, fNode)
                updateUILayerTree()
         
        updateUILayerTree()
        return {'FINISHED'}
    
    def draw(self, context):
        
        layout = self.layout
        layout.prop_search(self, "filtersSet_id", self, "filtersSet", text = "Filter to Delete ", icon='NODETREE')
        
    def invoke(self, context, event):
            
        self.collectInnerFilters()
        
        if bpy.context.scene.mtLayerSets_id != '':
            return context.window_manager.invoke_props_dialog(self) 
    
        else:
            return {'FINISHED'}

        

class VTOOLS_OP_mtOpenFilterPanel(bpy.types.Operator):
    bl_idname = "vtools.mtopenfilterpanel"
    bl_label = "Edit filter"
    bl_description = "Open and Edit filter node"
    
    mainNode = bpy.props.StringProperty(default = "None") 
    filterNode = bpy.props.StringProperty(default = "None") 
    
    filterInputs = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    filterInputs_id = bpy.props.StringProperty() 
    
    filterOutputs = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    filterOutputs_id = bpy.props.StringProperty() 
    
    
    def execute(self, context):
        
        mainTree = bpy.context.object.active_material.node_tree
        selectedLayer = getActiveLayer()
        
        if self.filterInputs_id != "":     
            self.setDefaultInput(selectedLayer, self.filterInputs_id)
        
        if self.filterOutputs_id != "":
            self.setDefaultOutput(selectedLayer, self.filterOutputs_id )
            
        updateUILayerTree()                         
        return {'FINISHED'}
    
    def setDefaultInput(self, pSelectedLayer, pInput):

        selectedLayer = pSelectedLayer 
        targetInput = None
        baseInput = None
        if selectedLayer != None:
            fNode = selectedLayer.node_tree.nodes[self.filterNode]
            for input in fNode.inputs:
                if input.name == self.filterInputs_id:
                    targetInput = input
                elif len(input.links) > 0:
                    baseInput = input
                    
            if baseInput != None and targetInput != None:
                if baseInput != targetInput:
                    previousFilter = conectedFromNode(fNode, baseInput.name)
                    selectedLayer.node_tree.links.remove(previousFilter[0].outputs[previousFilter[1]].links[0])
                    selectedLayer.node_tree.links.new(previousFilter[0].outputs[previousFilter[1]], fNode.inputs[targetInput.name])
                    
                    #mainTree.links.remove(layerNode.outputs["colorOutput"].links[0])
                    #mainTree.links.new(previousLayer[0].outputs["colorOutput"], nextLayer[0].inputs[nextLayer[1]]) 
                    
                
        return {'FINISHED'}
    
    def setDefaultOutput(self, pSelectedLayer, pOutput):
        
        selectedLayer = pSelectedLayer 
        targetOutput = None
        baseOutput = None
        if selectedLayer != None:
            fNode = selectedLayer.node_tree.nodes[self.filterNode]
            for output in fNode.outputs:
                if output.name == self.filterOutputs_id:
                    targetOutput = output
                elif len(output.links) > 0:
                    baseOutput = output
                    
            if baseOutput != None and targetOutput != None:
                if baseOutput != targetOutput:
                    nextFilter = conectedToNode(fNode, baseOutput.name)
                    selectedLayer.node_tree.links.remove(nextFilter[0].inputs[nextFilter[1]].links[0])
                    selectedLayer.node_tree.links.new(nextFilter[0].inputs[nextFilter[1]], fNode.outputs[targetOutput.name])
                    
                    #mainTree.links.remove(layerNode.outputs["colorOutput"].links[0])
                    #mainTree.links.new(previousLayer[0].outputs["colorOutput"], nextLayer[0].inputs[nextLayer[1]]) 
                    
                
        return {'FINISHED'}
    
    def collectNodeInputs(self, pSelectedLayer):
        
        if bpy.context.scene.nodeFiltersSet_id != "":
            selectedLayer = pSelectedLayer
            self.filterInputs.clear()
            fNode = selectedLayer.node_tree.nodes[self.filterNode]
            
            for input in fNode.inputs:
                n = self.filterInputs.add()
                n.name = input.name
                if len(input.links) > 0:
                    self.filterInputs_id = input.name
                
           
        return {'FINISHED'}
    
    def collectNodeOutputs(self, pSelectedLayer):
        
        if bpy.context.scene.nodeFiltersSet_id != "":
            selectedLayer = pSelectedLayer
            self.filterOutputs.clear()
            fNode = selectedLayer.node_tree.nodes[self.filterNode]
            
            for output in fNode.outputs:
                n = self.filterOutputs.add()
                n.name = output.name
                if len(output.links) > 0:
                    self.filterOutputs_id = output.name
        
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        
        mainTree = bpy.context.object.active_material.node_tree
        selectedLayer = getActiveLayer()
        
        if selectedLayer != None:
            
            
            col.label(self.filterNode)
            col.separator()
            box = col.box()
            scol = box.column(align = True)
            
            scol.prop_search(self, "filterInputs_id", self, "filterInputs", text = "Active Input")
            scol.prop_search(self, "filterOutputs_id", self, "filterOutputs", text = "Active Output")
            
            col.separator()
            col.separator()
            
            fNode = selectedLayer.node_tree.nodes[self.filterNode]
            
            for input in fNode.inputs:
                
                if input.type != "RGBA":
                    col.prop(input, "default_value", text=input.name)
            
            col.separator()
            fNode.draw_buttons(context,col)
         
        
    def invoke(self, context, event):
        
        if bpy.context.scene.nodeFiltersSet_id != "":
            mainTree = bpy.context.object.active_material.node_tree
            selectedLayer = getActiveLayer()
            
            if selectedLayer != None: 
                
                self.collectNodeInputs(selectedLayer)
                self.collectNodeOutputs(selectedLayer)
                
                if bpy.context.scene.mtLayerSets_id != '':
                    return context.window_manager.invoke_props_dialog(self) 
                else:
                    return {'FINISHED'}
            else:
                return {'FINISHED'}
            
        return {'FINISHED'}

class VTOOLS_OP_mtAddFilterNode(bpy.types.Operator):
    bl_idname = "vtools.mtaddfilternode"
    bl_label = "Add Filter"
    bl_description = ""
    
    filterInputs = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    filterInputs_id = bpy.props.StringProperty() 
    
    filterOutputs = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    filterOutputs_id = bpy.props.StringProperty() 
    
    filterType = bpy.props.StringProperty()
    
    def collectNodeInputs(self, pSelectedLayer, pFilterNodeName):
        selectedLayer = pSelectedLayer
        self.filterInputs.clear()
        fNode = selectedLayer.node_tree.nodes[pFilterNodeName]
        
        for input in fNode.inputs:
            n = self.filterInputs.add()
            n.name = input.name
            if len(input.links) > 0:
                self.filterInputs_id = input.name
                
           
        return {'FINISHED'}
    
    def collectNodeOutputs(self, pSelectedLayer, pFilterNodeName):
        selectedLayer = pSelectedLayer
        self.filterOutputs.clear()
        fNode = selectedLayer.node_tree.nodes[pFilterNodeName]
        
        for output in fNode.outputs:
            n = self.filterOutputs.add()
            n.name = output.name
            if len(output.links) > 0:
                self.filterOutputs_id = output.name
        
        return {'FINISHED'}
    
    def draw(self,context):
        layout = self.layout
        layout.prop_search(self, "filterInputs_id", self, "filterInputs", text = "Active Input")
        layout.prop_search(self, "filterOutputs_id", self, "filterOutputs", text = "Active Output")
            
            
    def execute(self, context):

        mainTree = bpy.context.object.active_material.node_tree
        selectedLayer = getActiveLayer()
        
        if selectedLayer != None:
            layerFrame = getFiltersFrame(selectedLayer)
            nodeFilter = selectedLayer.node_tree.nodes.new(type=self.filterType)
            
            filtersOutput_id= selectedLayer.node_tree.nodes.find("FPL_filtersColorOutput")
            if filtersOutput_id >= 0:
                filterOutputNode = selectedLayer.node_tree.nodes[filtersOutput_id]
            else:
                filtersOutput_id = selectedLayer.node_tree.nodes.find("PL_filtersColorOutput")
                if filtersOutput_id >= 0:
                    filterOutputNode = selectedLayer.node_tree.nodes[filtersOutput_id]
                
                
            lastFilterNode = conectedFromNode(filterOutputNode, "Input")

            numChildren = getNumNodeChildren(selectedLayer.node_tree, layerFrame)
                
            nodeFilter.location = [0,0]
            nodeFilter.parent = layerFrame
            nodeFilter.location = [10*numChildren,0]
            nodeFilter.label = nodeFilter.name
            
            found = False
            contInput = 0
            for input in nodeFilter.inputs:
                if input.name.upper() == "COLOR" or input.name.upper() == "IMAGE":
                    found = True
                    break
                contInput += 1 
            
            if not found:
                contInput = 0
            
            found = False
            contOutput = 0
            for output in nodeFilter.outputs:
                if output.name.upper() == "COLOR" or output.name.upper() == "IMAGE":
                    found = True
                    break
                contOutput += 1 
            
            if not found:
                contOutput = 0
                
            selectedLayer.node_tree.links.new(nodeFilter.inputs[contInput], lastFilterNode[0].outputs[lastFilterNode[1]])
            selectedLayer.node_tree.links.new(nodeFilter.outputs[contOutput], filterOutputNode.inputs[0])
            
            
            # -- EDIT -- #
            
            bpy.context.scene.nodeFiltersSet_id = nodeFilter.name
            #bpy.ops.vtools.mtopenfilterpanel('INVOKE_DEFAULT', filterNode = nodeFilter.name)
            
            #self.collectNodeInputs(selectedLayer, nodeFilter.name)
            #self.collectNodeOutputs(selectedLayer, nodeFilter.name)
            
            
            
        updateUILayerTree()    
        return {'FINISHED'}
    
    
     
class VTOOLS_OP_mtAddFilterToLayerMenu(bpy.types.Menu):
    bl_idname = "vtools.mtaddfiltertolayermenu"
    bl_label = ""
    bl_description = "Add a filter to selected layer"
    

    #["",""],
    filterTypes = [
    ["RGB Curves","ShaderNodeRGBCurve"], 
    ["Hue/Saturation","ShaderNodeHueSaturation"],
    ["Gamma","ShaderNodeGamma"],
    ["Invert","ShaderNodeInvert"],
    ["Bright/Contrast","ShaderNodeBrightContrast"],
    ["Color Ramp","ShaderNodeValToRGB"],
    ["Color to BW","ShaderNodeRGBToBW"],
    ["Separate RGB","ShaderNodeSeparateRGB"],
    ["Combine RGB","ShaderNodeCombineRGB"]
    ]
        
    def draw(self,context):
        layout = self.layout
        #layout.operator_context = 'INVOKE_DEFAULT'
        for type in self.filterTypes:
            op = layout.operator(VTOOLS_OP_mtAddFilterNode.bl_idname, text=type[0])
            op.filterType = type[1]

         
class VTOOLS_OP_mtEditExistingFilters(bpy.types.Operator):
    bl_idname = "vtools.mteditexistingfilters"
    bl_label = "Edit Existing Filters"
    bl_description = "Configure existing filters within the layer node"
    
    def collectInnerFilters(self):
        self.filtersSet_id = ""
        self.filtersSet.clear()
        mainTree = bpy.context.object.active_material.node_tree
        selectedLayer = getActiveLayer()
        mainTree.nodes.active = selectedLayer
        mainTree.nodes.active.select = True
        
        if isPaintLayerNode(selectedLayer):
            filters  = []
            filters = getFilters(selectedLayer)
            
            for f in filters:
                n = self.filtersSet.add()
                n.name = f.name
            
            self.filtersSet_id = ""
            
        
    def callback_getSelectedFilter(self, value):
        
        mainTree = bpy.context.object.active_material.node_tree
        layerNode = mainTree.nodes.active
        fNode = None
        
        if isPaintLayerNode(layerNode):
            for n in layerNode.node_tree.nodes:
                if n.name == self.filtersSet_id:
                    fNode = n
                    self.filterNode = fNode.name
                    bpy.ops.vtools.mtopenfilterpanel('INVOKE_DEFAULT', filterNode = fNode.name)
                    
                       
    filtersSet = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    filtersSet_id = bpy.props.StringProperty(update = callback_getSelectedFilter) 
    filterNode = bpy.props.StringProperty()    
    
    def execute(self, context):
        #updateUILayerTree()               
        return {'FINISHED'}
    
    def draw(self, context):
        
        layout = self.layout
        col = layout.column(align=True)
        col.label("Existing Filters:")
        
        for f in self.filtersSet:
            filterText = "      - " + f.name
            col.label(filterText)
        
        col.separator()    
        col.label("Select from list to Edit:")
        col.prop_search(self, "filtersSet_id", self, "filtersSet", text = "", icon='NODETREE')

        col.separator()
        
    def invoke(self, context, event):
        
        self.collectInnerFilters()
            
        if bpy.context.scene.mtLayerSets_id != '':
            return context.window_manager.invoke_props_dialog(self, width = 200) 
        else:
            return {'FINISHED'}

class VTOOLS_OP_mtNewLayerMenu(bpy.types.Menu):
    bl_idname = "vtools.mtnewlayermenu"
    bl_label = "New Layer"
    bl_description = "New Layer Menu"
    
    def draw(self, context):
        
        layout = self.layout
        col = layout.column(align=True)
        
        setEmboss = True
        col.operator_context = 'INVOKE_DEFAULT'
        col.operator(VTOOLS_OP_mtAddNewLayer.bl_idname, text="Create New Layer", icon='FILE', emboss=setEmboss)
        col.operator(VTOOLS_OP_mtAddNewFilterLayer.bl_idname, text="Create Adjustment Layer", icon='PARTICLES', emboss = setEmboss)
              

class VTOOLS_OP_mtLayerSetOperationsMenu(bpy.types.Menu):
    bl_idname = "vtools.mtlayersetoperationsmenu"
    bl_label = "Layer Set operations"
    bl_description = "Open Layer Set Operations Menu"
    
    def draw(self, context):
        
        layout = self.layout
        col = layout.column(align=True)
        
        setEmboss = True
        col.operator_context = 'INVOKE_DEFAULT'
        col.operator(VTOOLS_OP_mtConnectLayerSet.bl_idname, text = "Connect Layer Set to...", icon = "LIBRARY_DATA_DIRECT")
        col.operator(VTOOLS_OP_mtRenameLayerSet.bl_idname, text = "Rename Layer Set", icon = "OUTLINER_DATA_FONT")
        
        col.separator()
        
        col.operator(VTOOLS_OP_mtCreatePaintingShaderNode.bl_idname, text = "Create Painting Shader Node", icon = "GROUP_VCOL")    
        mainTree = bpy.context.object.active_material.node_tree
        paintingShaderNodeID = mainTree.nodes.find('MTPaintShader')
        
        col = layout.column(align=True)
        col.enabled = False
        
        if paintingShaderNodeID > -1:
             col.enabled = True
        
        col.operator(VTOOLS_OP_mtConnectPaintingShader.bl_idname, text = "Connect painting shader node to...", icon = "LIBRARY_DATA_DIRECT")
        col.operator(VTOOLS_OP_mtToogleShadeless.bl_idname, text = "Toogle Painting Shader Shadeless ", icon = "OUTLINER_OB_LAMP")
        col.operator(VTOOLS_OP_mtToogleTransparency.bl_idname, text = "Toogle Painting Shader Transparency", icon = "RESTRICT_VIEW_OFF")
        
        
        
class VTOOLS_OP_mtLayersOperationsMenu(bpy.types.Menu):
    bl_idname = "vtools.mtlayersoperationsmenu"
    bl_label = "Layersoperations"
    bl_description = "Open Layers Operations Menu"
    
    def draw(self, context):
        
        setEmboss = True
        
        layout = self.layout
        col = layout.column(align=True)
        col.operator_context = 'INVOKE_DEFAULT'

        #col.operator(VTOOLS_OP_mtAddNewLayer.bl_idname, text="Create New Layer", icon='FILE', emboss=setEmboss)
        #col.operator(VTOOLS_OP_mtDeleteLayer.bl_idname, text="Delete Layer", icon='CANCEL', emboss= setEmboss)
        #col.operator(VTOOLS_OP_mtFiltersActionsButton.bl_idname, text="Create Adjustment Layer", icon='PARTICLES', emboss= setEmboss)
        
        col.operator(VTOOLS_OP_mtAddMaskLayer.bl_idname, text="Add Texture Mask", icon='IMAGE_ALPHA', emboss= setEmboss)


        col.separator()
        
        col.operator(VTOOLS_OP_mtSortUILayerNodes.bl_idname, text="Sort UI Nodes", icon='MESH_GRID', emboss= setEmboss)            
        col.operator(VTOOLS_OP_mtFocusToSelected.bl_idname, text="Focus to active UV Tile", icon='ZOOM_SELECTED', emboss = setEmboss )            
        
        col.separator()
        
        col.operator(VTOOLS_OP_mtBakeSelected.bl_idname, text="Bake Over Selected", icon='RENDER_STILL', emboss = setEmboss)             
        col.operator(VTOOLS_OP_mtPackAllTextureLayers.bl_idname, text ="Pack Layers" , icon='PACKAGE', emboss = setEmboss)
        col.operator(VTOOLS_OP_mtSaveAllTextureLayers.bl_idname, text = "Export Selected Layer", icon='FILE_TICK', emboss = setEmboss).action = "SELECTED" 
        col.operator(VTOOLS_OP_mtSaveAllTextureLayers.bl_idname, text = "Export All Layers", icon='SAVE_COPY', emboss = setEmboss).action = "ALL"
        
class VTOOLS_OP_mtMultiTileMenu(bpy.types.Menu):
    bl_idname = "vtools.mtmultitilemenu"
    bl_label = "Multi Tiles Operations"
    bl_description = "Multi Tiles Operations Menu"
    
    def draw(self, context):
        
        setEmboss = True
        
        layout = self.layout
        col = layout.column(align=True)
        col.operator_context = 'INVOKE_DEFAULT'
        
        col.operator(VTOOLS_OP_mtCreateMaterials.bl_idname, text="MultiTIle Set", icon="MATERIAL")    
        col.operator(VTOOLS_OP_mtCreateMaterialsFromSelected.bl_idname, text=" Set from selected", icon="NODETREE")
        col.operator(VTOOLS_OP_mtCreateUVLayers.bl_idname, text="Add UV Layers", icon="MESH_DATA")

      
                 
                                  
class VTOOLS_OP_mtAddNewFilterLayer(bpy.types.Operator):
    bl_idname = "vtools.mtaddnewfilterlayer"
    bl_label = "Create new filter layer"
    bl_description = "Add a new filter layer above the selected layer node"
    
    imageName = bpy.props.StringProperty(name="Name")
    imageWidth = bpy.props.IntProperty(name="Width", default=1024)
    imageHeight = bpy.props.IntProperty(name="Height", default=1024)
    imageColor = bpy.props.FloatVectorProperty(name="Mask color", subtype='COLOR', size = 4, default=(1.0, 1.0, 1.0,1.0),min=0.0, max=1.0, description="color picker")
    imageDepth = bpy.props.BoolProperty(name="32 Bit Float Image", default = False)
    
    def execute(self, context):
        self.imageColor[3] = 1.0
        textureImage = newTextureImage(pName = self.imageName, pWidth = self.imageWidth, pHeight = self.imageHeight, pColor = self.imageColor, pAlpha = False, pFloat=self.imageDepth)
        multiTile_addLayerFilter(self.imageName, textureImage)
        updateUILayerTree()
        
        return {'FINISHED'}
 
    def invoke(self, context, event):
        
        self.imageName = "layer Name"
        
        existPaintLayerGroup = bpy.data.node_groups.find('MTPaintLayer_Color')
        existFilterLayerGroup = bpy.data.node_groups.find('MTPaintLayer_Filter')
        
        if existPaintLayerGroup > -1 and existFilterLayerGroup > -1:
            nodeLayerColor = bpy.data.node_groups[existPaintLayerGroup]
            nodeLayerFilter = bpy.data.node_groups[existFilterLayerGroup]
            
            nodeLayerColor.use_fake_user = True
            nodeLayerFilter.use_fake_user = True
            
            return context.window_manager.invoke_props_dialog(self) 
        else:
            self.report({'INFO'}, "MTPaintLayer_Filter not found, please Append it") 
            return {'FINISHED'}            

  
        
class VTOOLS_OP_mtAddMaskLayer(bpy.types.Operator):
    bl_idname = "vtools.mtaddmasklayer"
    bl_label = "Create new mask texture"
    bl_description = "Add a layer mask to the selected layer"
    
    #imageName = bpy.props.StringProperty(name="Name")
    imageWidth = bpy.props.IntProperty(name="Width", default=1024)
    imageHeight = bpy.props.IntProperty(name="Height", default=1024)
    imageColor = bpy.props.FloatVectorProperty(name="Mask color", subtype='COLOR', size = 4, default=(1.0, 1.0, 1.0,1.0),min=0.0, max=1.0, description="color picker")
    imageDepth = bpy.props.BoolProperty(name="32 Bit Float Image", default = False)
    
    def execute(self, context):
        
        self.imageColor[3] = 1.0
        
        textureImage = newTextureImage(pName = "MTP_layerMaskNameTMP", pWidth = self.imageWidth, pHeight = self.imageHeight, pColor = self.imageColor, pAlpha = False, pFloat=self.imageDepth)
        multiTile_addLayerMask(textureImage)
        updateUILayerTree()
        
        return {'FINISHED'}
 
    def invoke(self, context, event):
        self.imageName = "Mask texture Name"
        return context.window_manager.invoke_props_dialog(self)     

class VTOOLS_OP_mtDeleteLayer(bpy.types.Operator):
    bl_idname = "vtools.mtdeletelayer"
    bl_label = "Delete layer"
    bl_description = "Delete the selected layer node"
    
    def execute(self,context):
        multiTile_deleteLayer()
        updateUILayerTree()
        return {'FINISHED'}
        
class VTOOLS_OP_mtSelectLayer(bpy.types.Operator):
    bl_idname = "vtools.mtselectlayer"
    bl_label = "Select layer"
    bl_description = "Select the correct texture in every multi tile material"
    
    def execute(self,context):
        multiTile_selectLayer(bpy.context.scene.mtlayerPaintingSpace)
        updateUILayerTree()
        return {'FINISHED'}

class VTOOLS_OP_mtSelectPaintingSpace(bpy.types.Operator):
    bl_idname = "vtools.mtselectpaintingspace"
    bl_label = "select paint space"
    bl_description = "Paint into color or mask texture. Click active to switch"
    
    def execute(self,context):
        #change any propertie
        bpy.context.scene.mtlayerPaintingSpace = not bpy.context.scene.mtlayerPaintingSpace 
        multiTile_selectLayer(bpy.context.scene.mtlayerPaintingSpace)
        updateUILayerTree()
        return {'FINISHED'}

class  VTOOLS_OP_mtMoveLayerUp(bpy.types.Operator):
    bl_idname = "vtools.mtmovelayerup"
    bl_label = "Move layer Up"
    bl_description = "Move selected layer up"
    
    def execute(self,context): 
        multitile_moveLayer("UP")
        updateUILayerTree()
        return {'FINISHED'}
    
class  VTOOLS_OP_mtMoveLayerDown(bpy.types.Operator):
    bl_idname = "vtools.mtmovelayerdown"
    bl_label = "Mode layer Down"
    bl_description = "Move selected layer down"
    
    def execute(self,context): 
        multitile_moveLayer("DOWN")
        updateUILayerTree()
        return {'FINISHED'}
            
class VTOOLS_OP_mtOpenTexture(bpy.types.Operator):
    bl_idname = "vtools.mtopentexture"
    bl_label = "open a image as texture"
    bl_description = "Open and use a new image as texture"
    
    def execute(self, contet):
        
        image = bpy.ops.image.open('INVOKE_DEFAULT')
        updateUILayerTree()
        return {'FINISHED'}
    
class VTOOLS_OP_mtSaveAllTextureLayers(bpy.types.Operator, ExportHelper):
    bl_idname = "vtools.mtsavealltexturelayers"
    bl_label = "Export selected layer"
    bl_description = "export layer selected to disk (will export that layer of every material)"
    
    filename_ext = bpy.props.StringProperty()
    filepath = bpy.props.StringProperty(subtype="FILE_PATH")
    filename = bpy.props.StringProperty(set=updateFileNameFormat)
    check_extension = True
    action = bpy.props.StringProperty(default = "SELECTED")
    
    def execute(self, context):
        
        multiTile_saveTexturesLayer(pFilePath = self.filepath, pAction = self.action)
        self.report({'INFO'}, "Textures have been saved") 
            
        return {'FINISHED'}
    
    def draw(self,context):
       
        self.layout.template_image_settings(bpy.context.scene.render.image_settings, color_management=False)
        
  

class VTOOLS_OP_mtPackAllTextureLayers(bpy.types.Operator):
    bl_idname = "vtools.mtpackalltexturelayers"
    bl_label = "pack all texture layers"
    bl_description = "Pack all textures used by paint layers within Blender"
    
    def execute(self, contet):
        
        multiTile_packTexturesLayer()
        updateUILayerTree()
        return {'FINISHED'}


class VTOOLS_OP_mtPropagateUVChannel(bpy.types.Operator):
    bl_idname = "vtools.mtpropagateuvchannel"
    bl_label = "propagate uv channel"
    bl_description = "copy this uv channel in the connected Paint Layers"
    
    def execute(self, contet):
        
        multiTile_propagateUVChannel()
        return {'FINISHED'}
    
class VTOOLS_OP_mtPropagateTexture(bpy.types.Operator):
    bl_idname = "vtools.mtpropagatetexture"
    bl_label = "propagate texture"
    bl_description = "use this texture in the connected Paint Layers"
    
    def execute(self, contet):
        
        multiTile_propagateTexture()
        return {'FINISHED'}

class VTOOLS_OP_mtSortUILayerNodes(bpy.types.Operator):
    bl_idname = "vtools.mtsortuilayernodes"
    bl_label = "sort node Paint Layer tree"
    bl_description = "sort Paint Layer tree nodes UI"
    
    def execute(self, contet):
        multTile_sortUINodeTree()
        return {'FINISHED'}

class  VTOOLS_OP_mtCreateMaterials(bpy.types.Operator):
    bl_idname = "vtools.mtcreatematerials"
    bl_label = "create material set"
    bl_description = "create a new multi tile material set based on selected uv map layer"
    
    def execute(self,context):
        
        obj = bpy.context.scene.objects.active
        while len(obj.data.materials) > 0:
            obj.data.materials.pop(0)
            
        res = createMultiTileMaterials(None)
        bpy.ops.object.mode_set(mode = 'TEXTURE_PAINT') 
        
        if res == "FAIL": 
            self.report({'INFO'}, "Error: Add almost one uv layer") 
        elif res == "TILES_OVERFLOW":
            self.report({'INFO'}, "Error: Maximum tile grid size 9x9") 
        else:
            self.report({'INFO'}, "Tile Materials Created") 
            obj.active_material_index = 0
                          
        return {'FINISHED'}
    
    

class  VTOOLS_OP_mtCreateMaterialsFromSelected(bpy.types.Operator):
    bl_idname = "vtools.mtcreatematerialsfromselected"
    bl_label = "create material set from selected"
    bl_description = "create a new multi tile set material copying the selected material and based on selected uv map layer"
    
    def execute(self,context): 
        baseMaterial = context.object.active_material
        obj = bpy.context.scene.objects.active
        baseMat_id = obj.data.materials.find(baseMaterial.name)
        obj.data.materials.pop(baseMat_id)
        res = createMultiTileMaterials(baseMaterial)    
        bpy.ops.object.mode_set(mode = 'TEXTURE_PAINT')       
        
        
        if res == "FAIL": 
            self.report({'INFO'}, "Error: Add almost one uv layer") 
        elif res == "TILE_OVERFLOW":
            self.report({'INFO'}, "Error: Maximum tile grid size 9x9") 
        else:
            self.report({'INFO'}, "Tile Materials Created") 
            obj.active_material_index = 0
              
        return {'FINISHED'}

class  VTOOLS_OP_mtCreateUVLayers(bpy.types.Operator):
    bl_idname = "vtools.mtcreateuvlayers"
    bl_label = "create MultiTile UVlayers "
    bl_description = "Create uv_layers needed for baking and painting"
    
    def execute(self,context): 
        res = createMultiTileUVLayers()   
        bpy.ops.object.mode_set(mode = 'TEXTURE_PAINT')       
        
        if not res: 
            self.report({'INFO'}, "Error: Add almost one uv layer") 
                
        return {'FINISHED'}

class  VTOOLS_OP_mtFocusToSelected(bpy.types.Operator):
    bl_idname = "vtools.mtfocustoselectedtile"
    bl_label = "Focus paint uv layer to selected tile"
    bl_description = "Move the painting uv layer to center the selected tile (material)"
    
    def execute(self,context): 
        focusToSelectedTile(context.object)  
        bpy.ops.object.mode_set(mode = 'TEXTURE_PAINT')       
        return {'FINISHED'}
    
class  VTOOLS_OP_mtUseCurrentShader(bpy.types.Operator):
    bl_idname = "vtools.mtconnecttosameshader"
    bl_label = "Connect to shader"
    bl_description = "Connect every tile to the same shader"
    
    def execute(self,context): 
        multitile_useCurrentShader()           
        return {'FINISHED'}
    

class  VTOOLS_OP_mtBakeSelected(bpy.types.Operator):
    bl_idname = "vtools.mtbaketoselected"
    bl_label = "Bake layers"
    bl_description = "Bake Layers Below to Selected"
    
    def hideLayersBelow(self, pSelectedLayer):
        
        
        lastLayer = pSelectedLayer
        prevLayer = conectedFromNode(lastLayer, "colorBelow")[0]
        opacityList = []
        cont = 0 
        
        #-- Move N layers below
        while prevLayer != None and isPaintLayerNode(prevLayer):
            
            if cont < self.numLayersBelowAffected:
                lastLayer = prevLayer
                prevLayer = conectedFromNode(lastLayer, "colorBelow")[0]   
                cont += 1
            else:
                break
        
        
        prevLayer = conectedFromNode(lastLayer, "colorBelow")[0]
        
        #-- Hide layerse until first
        
        while prevLayer != None and isPaintLayerNode(prevLayer):
            opacity = getOpacityLayer(prevLayer)
            opacityList.append(opacity)                
            setOpacityLayer(prevLayer, 0)
            lastLayer = prevLayer
            prevLayer = conectedFromNode(lastLayer, "colorBelow")[0]      
                    
        return opacityList
    
    def restoreOpacitiesBelow(self, pSelectedLayer, pOpacityList):
        
        lastLayer = pSelectedLayer
        prevLayer = conectedFromNode(lastLayer, "colorBelow")[0]
        opacityList = []
        cont = 0 
        
        #-- Move N layers below
        while prevLayer != None and isPaintLayerNode(prevLayer):
            
            if cont < self.numLayersBelowAffected:
                lastLayer = prevLayer
                prevLayer = conectedFromNode(lastLayer, "colorBelow")[0]   
                cont += 1
            else:
                break
            
        #-- Restore layerse until first
        prevLayer = conectedFromNode(lastLayer, "colorBelow")[0]
        
        contList = 0

        while prevLayer != None and isPaintLayerNode(prevLayer):
            setOpacityLayer(prevLayer, pOpacityList[contList])
            lastLayer = prevLayer
            prevLayer = conectedFromNode(lastLayer, "colorBelow")[0]  
            contList += 1
                
        return {'FINISHED'}
        
    def hideLayersAbove(self, pSelectedLayer):
        
        lastLayer = pSelectedLayer
        nextLayer = conectedToNode(lastLayer, "colorOutput")[0]
        opacityList = []
        
        while nextLayer != None and isPaintLayerNode(nextLayer):
            opacity = getOpacityLayer(nextLayer)
            opacityList.append(opacity)
            
            setOpacityLayer(nextLayer, 0)
            
            lastLayer = nextLayer
            nextLayer = conectedToNode(nextLayer, "colorOutput")[0]    
        
        return opacityList
    
    def restoreOpacitiesAbove(self, pSelectedLayer, pOpacityList):
        
        lastLayer = pSelectedLayer
        nextLayer = conectedToNode(lastLayer, "colorOutput")[0]
        
        cont = 0
        while nextLayer != None and isPaintLayerNode(nextLayer):
            setOpacityLayer(nextLayer, pOpacityList[cont])
            lastLayer = nextLayer
            nextLayer = conectedToNode(nextLayer, "colorOutput")[0]  
            cont += 1
                
        return {'FINISHED'}
    
       
    def setUpBake(self, context):
        if self.uvLayers_id != "":
            obj = bpy.context.scene.objects.active
            uvId = obj.data.uv_textures.find(self.uvLayers_id)
            
            if uvId >= 0:
                mainTree = bpy.context.object.active_material.node_tree
                selectedLayer = getActiveLayer()
                mainTree.nodes.active = selectedLayer
                
                obj.data.uv_textures.active_index = uvId
                uvNode = getUVNode(selectedLayer,bpy.context.scene.mtlayerPaintingSpace) 
                uvNode.uv_map = self.uvLayers_id
                multiTile_propagateUVChannel()

    
        
    def collectUVLayers(self, pObj):
        
        obj = pObj
        if obj != None:
            self.uvLayers_id = ""
            self.uvLayers.clear()
            for uv in obj.data.uv_textures:
                nUV = self.uvLayers.add()
                nUV.name = uv.name
            
        return {'FINISHED'}
    
    uvLayers = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    uvLayers_id = bpy.props.StringProperty(update = setUpBake)
    numLayersBelowAffected = bpy.props.IntProperty(default = 1)
    
    def execute(self,context): 
        
        mainTree = bpy.context.object.active_material.node_tree
        selectedLayer = getActiveLayer()
        opacityList = []
        bakeLayerOpacity = getOpacityLayer(selectedLayer)
             
        # Save Config 
        
        oldSquaredSample = bpy.context.scene.cycles.use_square_samples
        oldSamples = bpy.context.scene.cycles.samples
        
        # Configure 
        
        opacityListAbove = self.hideLayersAbove(selectedLayer)
        opacityListBelow = self.hideLayersBelow(selectedLayer)
        setOpacityLayer(selectedLayer, 0)
        
        bpy.context.scene.render.bake.use_pass_indirect = False
        bpy.context.scene.render.bake.use_pass_direct = False
        bpy.context.scene.render.bake.use_pass_color = True
    

    
        bpy.context.scene.render.layers[0].use_pass_diffuse_direct = True
        bpy.context.scene.render.layers[0].use_pass_diffuse_color = True
        bpy.context.scene.cycles.bake_type = 'DIFFUSE'
        bpy.context.scene.render.bake.use_clear = True
        
        bpy.context.scene.cycles.use_square_samples = False
        bpy.context.scene.cycles.samples = 1

        
        # -- Bake Action ---#
        bpy.ops.object.bake(type = 'DIFFUSE')
        
        # Back to old Settings
        
        bpy.context.scene.cycles.use_square_samples = oldSquaredSample
        bpy.context.scene.cycles.samples = oldSamples
        self.restoreOpacitiesAbove(selectedLayer, opacityListAbove)
        self.restoreOpacitiesBelow(selectedLayer, opacityListBelow)
        setOpacityLayer(selectedLayer, bakeLayerOpacity)
        
        return {'FINISHED'}
    
    def draw(self, context):
        
        layout = self.layout
        col = layout.column(align = True)
        
        obj = bpy.context.scene.objects.active
        #obj.select = True
        self.collectUVLayers(obj)  
        
        col.label("Select uv layer to bake over:")
        col.prop_search(self, "uvLayers_id", self, "uvLayers", text = "")
        col.prop(self, "numLayersBelowAffected", text = "Numer Layers Below Affected")
        col.separator()
        
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self) 
    
class VTOOLS_OP_mtAddLayerSet(bpy.types.Operator):
    bl_idname = "vtools.mtaddlayerset"
    bl_label = "Add Layer Set"
    bl_description = "Add layer set"
    
    layerSetName =  bpy.props.StringProperty(default='', name = "Layer Set Name")
    
    def execute(self, context):
        mainTree = bpy.context.object.active_material.node_tree
        multitile_addLayerSet(self.layerSetName)
        #bpy.ops.vtools.mtconnecttonode('INVOKE_DEFAULT')
        bpy.ops.vtools.mtconnectpaintingshader('INVOKE_DEFAULT')
        
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self) 


class VTOOLS_OP_mtRenameLayerSet(bpy.types.Operator):
    bl_idname = "vtools.mtrenamelayerset"
    bl_label = "Rename Layer Set"
    bl_description = "Rename layer set"
    
    layerSetName =  bpy.props.StringProperty(default='', name = "New Name")
    
    def execute(self, context):
        multitile_renameLayerSet(self.layerSetName)
        return {'FINISHED'}

    def invoke(self, context, event):
        if bpy.context.scene.mtLayerSets_id != '':
            return context.window_manager.invoke_props_dialog(self) 
        else:
            return {'FINISHED'}


            
class VTOOLS_OP_mtConnectLayerSet(bpy.types.Operator):
    bl_idname = "vtools.mtconnecttonode"
    bl_label = "Connect to Node"
    bl_description = "Connect Layer Set To Node"
    
    def callback_selectNodeToConnect(self,value):
        
        
        self.nodeInputs.clear()
        self.nodeInputs_id = ""
        mainTree = bpy.context.object.active_material.node_tree
        for node in mainTree.nodes:
            if node.name == self.layerSets_id:
                for input in node.inputs:
                    newInput = self.nodeInputs.add()
                    newInput.name = input.name
        
    layerSets = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    layerSets_id = bpy.props.StringProperty(update=callback_selectNodeToConnect)
    nodeInputs = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    nodeInputs_id = bpy.props.StringProperty() 
    
    outputSelector = bpy.props.EnumProperty(
    items=(
        ("color", "Color", 'color output',  'COLOR_OUTPUT', 1),
        ("alpha", "Alpha", 'alpha output',  'ALPHA_OUTPUT', 2),
    ),
    name="LayerSet Output",
    default="color"
    )
    

    removeLink = bpy.props.BoolProperty(name = "Remove Previous Links", default = True)
    
    def execute(self, context):
        
        #output = "colorOutput"
        output = "Color"
        if self.outputSelector == "alpha" or self.outputSelector == "Alpha": 
            output = "Alpha"
            #output = "alphaOutput"
        
        multiTile_connectLayerSet(output, self.layerSets_id, self.nodeInputs_id, self.removeLink)
        updateUILayerTree()
                        
        return {'FINISHED'}
    
    def draw(self, context):

        layout = self.layout
        layout.label("Layer Set Options:")
        box = layout.box() 
        #col.label("LayerSet Output")
        box.prop(self, "outputSelector")
        box.prop(self, "removeLink")
        layout.separator()
        layout.label("Target Node Options:")
        box = layout.box()
        box.prop_search(self, "layerSets_id", self, "layerSets", text = "Target Node", icon='NODETREE')
        box.prop_search(self, "nodeInputs_id", self, "nodeInputs", text = "Target Slot", icon='FORWARD')
        layout.separator()

        
    def invoke(self, context, event):
        
        mainTree = bpy.context.object.active_material.node_tree
        self.layerSets.clear()
        # collect nodes
        for node in mainTree.nodes:
            if node.parent != None and node.name.find("layerSet.") < 0:
                if node.parent.name.find("layerSet.") < 0 and node.parent.name.find("layerContainer.") < 0 and node.name.find("layerSet.") < 0:
                    n = self.layerSets.add()
                    n.name = node.name
            elif node.name.find("layerSet.") < 0:
                n = self.layerSets.add()
                n.name = node.name
                  
        if bpy.context.scene.mtLayerSets_id != '':
            return context.window_manager.invoke_props_dialog(self) 
        else:
            return {'FINISHED'}

class VTOOLS_OP_mtConnectPaintingShader(bpy.types.Operator):
    bl_idname = "vtools.mtconnectpaintingshader"
    bl_label = "Connect Painting Shader Node to"
    bl_description = "Connect painting shader node to..."
    
    def callback_selectNodeToConnect(self,value):
        self.nodeInputs.clear()
        self.nodeInputs_id = ""
        mainTree = bpy.context.object.active_material.node_tree
        for node in mainTree.nodes:
            if node.name == self.layerSets_id:
                for input in node.inputs:
                    newInput = self.nodeInputs.add()
                    newInput.name = input.name
        
    layerSets = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    layerSets_id = bpy.props.StringProperty(update=callback_selectNodeToConnect)
    nodeInputs = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    nodeInputs_id = bpy.props.StringProperty() 
    removeLink = bpy.props.BoolProperty(name = "Remove Existing Links", default = True)
    
    def execute(self, context):
        
        multiTile_connectPaintingShader("Shader", self.layerSets_id, self.nodeInputs_id, self.removeLink)
        updateUILayerTree()
                        
        return {'FINISHED'}
    
    def draw(self, context):

        layout = self.layout
        layout.label("Target Node Options:")
        layout.prop(self, "removeLink")
        box = layout.box()
        box.prop_search(self, "layerSets_id", self, "layerSets", text = "Target Node", icon='NODETREE')
        box.prop_search(self, "nodeInputs_id", self, "nodeInputs", text = "Target Slot", icon='FORWARD')
        layout.separator()

        
    def invoke(self, context, event):
        
        mainTree = bpy.context.object.active_material.node_tree
        self.layerSets.clear()
        # collect nodes
        for node in mainTree.nodes:
            if node.parent != None and node.name.find("layerSet.") < 0 and node.name != 'MTPaintShader':
                if node.parent.name.find("layerSet.") < 0 and node.parent.name.find("layerContainer.") < 0 and node.name.find("layerSet.") < 0:
                    n = self.layerSets.add()
                    n.name = node.name
            elif node.name.find("layerSet.") < 0 and node.name != 'MTPaintShader':
                n = self.layerSets.add()
                n.name = node.name
                  
        if bpy.context.scene.mtLayerSets_id != '':
            return context.window_manager.invoke_props_dialog(self) 
        else:
            return {'FINISHED'}
        
class VTOOLS_OP_mtCreatePaintingShaderNode(bpy.types.Operator):
    bl_idname = "vtools.mtcreatepaintingshader"
    bl_label = "Create Painting shader node"
    bl_description = "If this node is created you will have shadeless option and will be allowed to create transparent textures"
    
    def execute(self, context):
        mainTree = bpy.context.object.active_material.node_tree
        multitile_createPaintingShader()
        return {'FINISHED'}    

class VTOOLS_OP_mtToogleShadeless(bpy.types.Operator):
    bl_idname = "vtools.mttoogleshadeless"
    bl_label = "Toogle Painting shader node shadeless"
    bl_description = "Toogle Painting shader node shadeless parameter"
    
    def execute(self, context):
        mainTree = bpy.context.object.active_material.node_tree
        multitile_toogleShadeless()
        return {'FINISHED'}    

class VTOOLS_OP_mtToogleTransparency(bpy.types.Operator):
    bl_idname = "vtools.mttoogletransparency"
    bl_label = "Toogle shader node Transparency"
    bl_description = "Toogle Painting shader node transparency parameter"
    
    def execute(self, context):
        mainTree = bpy.context.object.active_material.node_tree
        multitile_toogleTransparency()
        return {'FINISHED'}     
 
     
class VTOOLS_OP_mtDeleteLayerSet(bpy.types.Operator):
    bl_idname = "vtools.mtdeletelayerset"
    bl_label = "Delete Layer Set"
    bl_description = "Delete layer set"
    
    def execute(self, context):
        mainTree = bpy.context.object.active_material.node_tree
        multitile_deleteLayerSet()
        return {'FINISHED'}
    
        
class VTOOLS_UIL_layerTreeDisplay(bpy.types.UIList):
     def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        row = layout.row()
        if item.isRGBLayer:
            row.label(text="", icon='BRUSH_DATA')       
        if item.isFilterLayer:
            row.label(text="", icon='PARTICLES')
            
        row.prop(item, "layerName", text="", emboss=False, translate=False)
        
        if item.localFilters:
            row.label(text="",icon='PARTICLES')
                       
        if item.hasColorTexture:
            row.label(text="",icon='COLOR')
        if item.hasMaskTexture:
            row.label(text="", icon='IMAGE_ALPHA')
        

class VTOOLS_CC_layerSetCollection(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty(default='')
    layerSetID = bpy.props.StringProperty()

class VTOOLS_CC_layerTreeCollection(bpy.types.PropertyGroup):
       
    name = bpy.props.StringProperty(default='')
    layerID = bpy.props.IntProperty()
    layerName = bpy.props.StringProperty(name="layerName", default="", update=changeLayerNameUI)
    layerNode = bpy.props.StringProperty(name="layerNode", default="")
    isRGBLayer = bpy.props.BoolProperty(default=False)
    isFilterLayer = bpy.props.BoolProperty(default=False)
    hasColorTexture = bpy.props.BoolProperty(default=False)
    hasMaskTexture = bpy.props.BoolProperty(default=False)
    selected = bpy.props.BoolProperty(default=False)
    localFilters = bpy.props.BoolProperty(default=False)
    
    

    
class VTOOLS_PN_MultiTilePainting(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Multi Painting"
    #bl_category = 'Slots'
    bl_options = {'DEFAULT_CLOSED'}       
    
    filtersSet = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    filtersSet_id = bpy.props.StringProperty()
    

                
    @classmethod
    def poll(cls, context):
        return (context.mode == 'PAINT_TEXTURE')
    
    def draw(self,context):
        
        
        layout = self.layout
        
        #material panel
        ob = context.active_object
        
        if bpy.context.object.active_material != None:     
            mainTree = bpy.context.object.active_material.node_tree
            if mainTree != None: 
                selectedMaterial = bpy.context.object.active_material
                selectedLayer = mainTree.nodes.active
                
                passThrough = True
                selectedLayerSet = getActiveLayerSetNode()
                selectedLayer = getActiveLayer()
                
                layerSetActive = False
                if selectedLayerSet != None: 
                    layerSetActive = True
                    
                
                if not layerSetActive:
                    row = layout.row()
                    row.label("Create or select a Layer Set")
                
                col = layout.column(align = True)
                row = col.row(align = True)
                row.prop_search(context.scene, "mtLayerSets_id", context.scene, "mtLayerSets", text = "", icon='IMGDISPLAY')
                row.operator(VTOOLS_OP_mtAddLayerSet.bl_idname, text = "",  icon = "ZOOMIN")
                row.operator(VTOOLS_OP_mtDeleteLayerSet.bl_idname, text = "",  icon = "ZOOMOUT")
                row.menu("vtools.mtlayersetoperationsmenu", icon='DOWNARROW_HLT', text="")
                    
                if not passThrough: #not isPaintLayerNode(selectedLayer):
                            
                    box = layout.box()
                    # Activate tile painting section
                    box.label("Select a PaintLayer node to see the layer tree or ")
                    box.operator(VTOOLS_OP_mtAddNewLayer.bl_idname, text="Create a new PaintLayer", icon='NEW')                   
                else:          
                   
                   # ------- layer properties ------# 
                    
                    ob = context.object
                    mat = context.object.active_material
                    slot = None
                    
                    if len(mat.texture_paint_slots) > 0: 
                        slot = mat.texture_paint_slots[mat.paint_active_slot]
                        
                    blendModeNode = findBlendModeNode()
                    opacityLayer = findOpacityLayerNode()
                    uvLayerNode = findUVLayerNode(bpy.context.scene.mtlayerPaintingSpace)
                
                
                    
                    
                    # ---------- layer tree -----------#
                    
                    setEmboss = True
                    if layerSetActive:
                        
                        if blendModeNode != None:
                            col.operator(VTOOLS_OP_mtPackAllTextureLayers.bl_idname, text ="Pack Layers" , icon='PACKAGE', emboss = setEmboss)
                                 
                        box = layout.box()
                        box.enabled = layerSetActive
                       
                        # -------- texture space selection -------------#
                        
                        
                        
                        if blendModeNode != None and opacityLayer != None:
                            
                            row = box.row(align=False)
                            row.prop(bpy.context.scene,"selectColorSpace", expand=True)
                            #row.separator()
                            
                            row.prop(blendModeNode, "blend_type", text="")
                            row.prop(opacityLayer.outputs["Value"], "default_value", text = "")

                        else:
                            row = box.row()
                            row.label("Empty - Create a New Layer")
                            
                           
                        #--- layer tree ------#
                        
                        row = layout.row(align = True)
                        col = row.column()
                        col.template_list('VTOOLS_UIL_layerTreeDisplay', "layerID ", context.scene, "layerTreeCollection", context.scene, "layerTreeCollection_ID_index", rows=3)
                        col = row.column(align = True)
                        
                        col.menu("vtools.mtnewlayermenu", icon='ZOOMIN', text="")
                        col.operator(VTOOLS_OP_mtDeleteLayer.bl_idname, text="", icon='ZOOMOUT', emboss= setEmboss)
                        
                        if blendModeNode != None:
                            col.menu("vtools.mtlayersoperationsmenu", icon='DOWNARROW_HLT', text="")

                            col.separator()
                            
                            col.operator(VTOOLS_OP_mtMoveLayerUp.bl_idname, text="", icon='TRIA_UP', emboss= setEmboss)
                            col.operator(VTOOLS_OP_mtMoveLayerDown.bl_idname, text="", icon='TRIA_DOWN', emboss= setEmboss)
                            
                            
                        # ------- Image Data ------------- #
                        
                        if layerSetActive and blendModeNode != None:
                            report = ""                
                            layerType = getLayerType(selectedLayer)    
                            
                            box = layout.box()               
                            
                           
                            col = box.column()    
                            row = col.row(align=True)
                            
                            # --- filter UI ---#
                            
                            row.prop_search(context.scene, "nodeFiltersSet_id", context.scene, "nodeFiltersSet", text = "", icon='PARTICLES')     
                            row.menu(VTOOLS_OP_mtAddFilterToLayerMenu.bl_idname, text="", icon='ZOOMIN')
                            row.operator(VTOOLS_OP_mtDeleteInnerFilter.bl_idname, text="", icon='ZOOMOUT', emboss = setEmboss)
                            col.separator()
                                                      
                          
                            if bpy.context.scene.mtlayerPaintingSpace and layerType == "COLOR" :
                                textureNode = conectedFromNode(selectedLayer, "Color")
                                report = "-- No color texture --"
                            else:
                                textureNode = conectedFromNode(selectedLayer, "Mask")
                                report = "-- No mask texture -- "
                                
                            if textureNode[0] != None and slot != None:    
                                
                                
                                row = col.row(align=True)
                                row.template_ID(textureNode[0], "image", open=VTOOLS_OP_mtOpenTexture.bl_idname)
                                row.operator(VTOOLS_OP_mtPropagateTexture.bl_idname, text="", icon='LINKED', emboss = True) #use this texture in other multitile layers
                                
                                row = col.row(align=True)                                
                                row.prop_search(slot, "uv_layer", ob.data, "uv_textures", text="")
                                row.operator(VTOOLS_OP_mtPropagateUVChannel.bl_idname, text="", icon='LINKED', emboss = True) #copy uv map in other multitile layers
                                
                            else:
                                
                                row = layout.row()
                                row.label(text=report, icon='ERROR')
                            
                
                col = layout.column(align=True)    
                col.separator()
                row = col.row(align = True)
                row.prop(context.scene,'multitileSelectionActive',text="Active MultiTile", icon= 'IMGDISPLAY')
                
         
                if bpy.context.scene.multitileSelectionActive:
                    
                    row.menu("vtools.mtmultitilemenu", icon='DOWNARROW_HLT', text="")
                    col.separator()
                    col.template_list("MATERIAL_UL_matslots", "layers",ob, "material_slots",ob, "active_material_index", rows=2)

        else:
            layout.label("No material detected")
        
        
    

def register():
    
    
    bpy.utils.register_module(__name__)
    
    bpy.types.Scene.multitileSelectionActive = bpy.props.BoolProperty(name='multi tile selection active', default=False, description = "Active Multi-Tile painting")
    bpy.types.Scene.mtlayerPaintingSpace = bpy.props.BoolProperty(name='painting space color/mask', default=True)
    bpy.types.Scene.layerTreeCollection_ID_index = bpy.props.IntProperty(update=callback_selectLayerUI)   
    bpy.types.Scene.layerTreeCollection = bpy.props.CollectionProperty(type=VTOOLS_CC_layerTreeCollection)
    
    bpy.types.Scene.multtileLayersFolder = bpy.props.StringProperty(name="LayersFolder", subtype = 'DIR_PATH')
    bpy.types.Scene.mtPreviousPaintLayerSelected = bpy.props.StringProperty(default = "None")
    bpy.types.Scene.mtPreviousActiveMaterial = bpy.props.StringProperty(default = "None")
    
    bpy.types.Scene.selectColorSpace = bpy.props.EnumProperty(
    items=(
        ("color", "", 'color space',  'COLOR', 1),
        ("mask", "", 'mask space',  'IMAGE_ALPHA', 2),
    ),
    name="colorSpaceEnum",
    default="color",
    update = callback_setColorSpace
    )

    bpy.types.Scene.mtLayerSets = bpy.props.CollectionProperty(type=VTOOLS_CC_layerSetCollection)
    bpy.types.Scene.mtLayerSets_id = bpy.props.StringProperty(update = callback_selectLayerSetUI)
    
    bpy.types.Scene.nodeFiltersSet = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    bpy.types.Scene.nodeFiltersSet_id = bpy.props.StringProperty(update = callback_editFilter)
    
def unregister():
    
    bpy.utils.unregister_module(__name__)
    
    del bpy.types.Scene.multitileSelectionActive 
    
    del bpy.types.Scene.mtlayerPaintingSpace
    del bpy.types.Scene.selectColorSpace
      
    del bpy.types.Scene.layerTreeCollection
    del bpy.types.Scene.layerTreeCollection_ID_index 
    del bpy.types.Scene.multtileLayersFolder 
    del bpy.types.Scene.mtPreviousPaintLayerSelected 
    del bpy.types.Scene.mtPreviousActiveMaterial
    
    del bpy.types.Scene.mtLayerSets
    del bpy.types.Scene.mtLayerSets_name 
    
    del bpy.types.Scene.nodeFiltersSet
    del bpy.types.Scene.nodeFfiltersSet_id
    
if __name__ == "__main__":
    register()        