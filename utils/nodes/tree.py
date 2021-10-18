import bpy
from . import general

class ColorBinarizationNodeTree:
    def new():
        if 'ColorBinarizationNodeTree' in bpy.data.node_groups:
            return
        export_group_tree = bpy.data.node_groups.new("ColorBinarizationNodeTree",'CompositorNodeTree')


        group_in = export_group_tree.nodes.new('NodeGroupInput')
        group_in.location = (-600,0)

        export_group_tree.inputs.new('NodeSocketFloat','Filter')
        export_group_tree.inputs.new('NodeSocketColor','Strength')
        export_group_tree.inputs.new('NodeSocketFloatFactor','Threshold')

        group_out = export_group_tree.nodes.new('NodeGroupOutput')
        group_out.location = (1200,0)

        export_group_tree.outputs.new('NodeSocketColor','Color')

        invert_node_1 = export_group_tree.nodes.new('CompositorNodeInvert')
        invert_node_1.location = (-400,50)
        invert_node_1.hide=True

        multiply_node_1 = export_group_tree.nodes.new('CompositorNodeMath')
        multiply_node_1.operation = 'MULTIPLY'
        multiply_node_1.location = (-200,50)
        multiply_node_1.hide = True

        greater_node = export_group_tree.nodes.new('CompositorNodeMath')
        greater_node.operation = 'GREATER_THAN'
        greater_node.location = (0,-25)
        greater_node.hide = True

        invert_node_2 = export_group_tree.nodes.new('CompositorNodeInvert')
        invert_node_2.location = (200,50)
        invert_node_2.hide = True

        invert_node_3 = export_group_tree.nodes.new('CompositorNodeInvert')
        invert_node_3.location = (250,-50)
        invert_node_3.hide = True

        multiply_node_3 = export_group_tree.nodes.new('CompositorNodeMath')
        multiply_node_3.operation = 'MULTIPLY'
        multiply_node_3.location = (450,-75)
        multiply_node_3.hide = True

        multiply_node_2 = export_group_tree.nodes.new('CompositorNodeMath')
        multiply_node_2.operation = 'MULTIPLY'
        multiply_node_2.location = (450,-25)
        multiply_node_2.hide = True

        add_node = export_group_tree.nodes.new('CompositorNodeMath')
        add_node.operation = 'ADD'
        add_node.location = (650,-50)
        add_node.hide = True

        link = export_group_tree.links.new

        link(group_in.outputs[1],invert_node_1.inputs[1])
        link(group_in.outputs[0],multiply_node_1.inputs[0])
        link(group_in.outputs[0],invert_node_2.inputs[1])
        link(group_in.outputs[0],multiply_node_3.inputs[1])
        link(group_in.outputs[2],greater_node.inputs[1])
        link(invert_node_1.outputs[0],multiply_node_1.inputs[1])
        link(multiply_node_1.outputs[0],greater_node.inputs[0])
        link(greater_node.outputs[0],invert_node_3.inputs[1])
        link(greater_node.outputs[0],multiply_node_2.inputs[1])
        link(invert_node_2.outputs[0],multiply_node_2.inputs[0])
        link(invert_node_3.outputs[0],multiply_node_3.inputs[0])
        link(multiply_node_2.outputs[0],add_node.inputs[0])
        link(multiply_node_3.outputs[0],add_node.inputs[1])
        link(add_node.outputs[0],group_out.inputs[0])

class BlackBinarizationNodeTree:
    def new():
        if 'BlackBinarizationNodeTree' in bpy.data.node_groups:
            return
        export_group_tree = bpy.data.node_groups.new("BlackBinarizationNodeTree",'CompositorNodeTree')

        group_in = export_group_tree.nodes.new('NodeGroupInput')
        group_in.location = (-600,0)

        export_group_tree.inputs.new('NodeSocketFloat','Filter')
        export_group_tree.inputs.new('NodeSocketColor','Strength')
        export_group_tree.inputs.new('NodeSocketFloatFactor','Threshold')

        group_out = export_group_tree.nodes.new('NodeGroupOutput')
        group_out.location = (1200,0)

        export_group_tree.outputs.new('NodeSocketColor','Color')

        invert_node_1 = export_group_tree.nodes.new('CompositorNodeInvert')
        invert_node_1.location = (-400,50)
        invert_node_1.invert_rgb = False
        invert_node_1.hide = True

        multiply_node_1 = export_group_tree.nodes.new('CompositorNodeMath')
        multiply_node_1.operation = 'MULTIPLY'
        multiply_node_1.location = (-200,50)
        multiply_node_1.hide = True

        greater_node = export_group_tree.nodes.new('CompositorNodeMath')
        greater_node.operation = 'GREATER_THAN'
        greater_node.location = (0,-25)
        greater_node.hide = True

        invert_node_2 = export_group_tree.nodes.new('CompositorNodeInvert')
        invert_node_2.location = (200,50)
        invert_node_2.hide = True

        invert_node_3 = export_group_tree.nodes.new('CompositorNodeInvert')
        invert_node_3.location = (250,-50)
        invert_node_3.hide = True

        multiply_node_3 = export_group_tree.nodes.new('CompositorNodeMath')
        multiply_node_3.operation = 'MULTIPLY'
        multiply_node_3.location = (450,-75)
        multiply_node_3.hide = True

        multiply_node_2 = export_group_tree.nodes.new('CompositorNodeMath')
        multiply_node_2.operation = 'MULTIPLY'
        multiply_node_2.location = (450,-25)
        multiply_node_2.hide = True

        add_node = export_group_tree.nodes.new('CompositorNodeMath')
        add_node.operation = 'ADD'
        add_node.location = (650,-50)
        add_node.hide = True

        invert_node_4 = export_group_tree.nodes.new('CompositorNodeInvert')
        invert_node_4.location = (850,-50)
        invert_node_4.hide = True

        link = export_group_tree.links.new

        link(group_in.outputs[0],multiply_node_1.inputs[0])
        link(group_in.outputs[0],invert_node_2.inputs[1])
        link(group_in.outputs[0],multiply_node_3.inputs[1])
        link(group_in.outputs[1],invert_node_1.inputs[1])
        link(group_in.outputs[2],greater_node.inputs[1])
        link(invert_node_1.outputs[0],multiply_node_1.inputs[1])
        link(multiply_node_1.outputs[0],greater_node.inputs[0])
        link(greater_node.outputs[0],invert_node_3.inputs[1])
        link(greater_node.outputs[0],multiply_node_2.inputs[1])
        link(invert_node_2.outputs[0],multiply_node_2.inputs[0])
        link(invert_node_3.outputs[0],multiply_node_3.inputs[0])
        link(multiply_node_2.outputs[0],add_node.inputs[0])
        link(multiply_node_3.outputs[0],add_node.inputs[1])
        link(add_node.outputs[0],invert_node_4.inputs[1])
        link(invert_node_4.outputs[0],group_out.inputs[0])

class ColorFilterNodeTree:
    def new():
        if 'ColorFilterNodeTree' in bpy.data.node_groups:
            return
        export_group_tree = bpy.data.node_groups.new('ColorFilterNodeTree','CompositorNodeTree')
        group_in = export_group_tree.nodes.new('NodeGroupInput')
        group_in.location = (-600,0)

        export_group_tree.inputs.new('NodeSocketFloatFactor','H')
        export_group_tree.inputs.new('NodeSocketFloatFactor','S')
        export_group_tree.inputs.new('NodeSocketFloatFactor','V')
        export_group_tree.inputs.new('NodeSocketFloatFactor','Hue')

        group_out = export_group_tree.nodes.new('NodeGroupOutput')
        group_out.location = (300,0)

        export_group_tree.outputs.new('NodeSocketColor','Color')

        compare_node_1 = export_group_tree.nodes.new('CompositorNodeMath')
        compare_node_1.operation = 'COMPARE'
        compare_node_1.inputs[2].default_value = 0.001
        compare_node_1.location = (-400,-10)
        compare_node_1.hide = True

        
        compare_node_2 = export_group_tree.nodes.new('CompositorNodeMath')
        compare_node_2.operation = 'COMPARE'
        compare_node_2.inputs[1].default_value = 0
        compare_node_2.inputs[2].default_value = 0.001
        compare_node_2.location = (-400,-45)
        compare_node_2.hide = True

        compare_node_3 = export_group_tree.nodes.new('CompositorNodeMath')
        compare_node_3.operation = 'COMPARE'
        compare_node_3.inputs[1].default_value = 1
        compare_node_3.inputs[2].default_value = 0.05
        compare_node_3.location = (-400,-80)
        compare_node_3.hide = True

        invert_node_1 = export_group_tree.nodes.new('CompositorNodeInvert')
        invert_node_1.location = (-250,-45)
        invert_node_1.hide=True

        multiply_node_1 = export_group_tree.nodes.new('CompositorNodeMath')
        multiply_node_1.operation = 'MULTIPLY'
        multiply_node_1.location = (-100,-27.5)
        multiply_node_1.hide = True

        multiply_node_2 = export_group_tree.nodes.new('CompositorNodeMath')
        multiply_node_2.operation = 'MULTIPLY'
        multiply_node_2.location = (50,-45)
        multiply_node_2.hide = True

        link = export_group_tree.links.new

        link(group_in.outputs[0],compare_node_1.inputs[0])
        link(group_in.outputs[1],compare_node_2.inputs[0])
        link(group_in.outputs[2],compare_node_3.inputs[0])
        link(group_in.outputs[3],compare_node_1.inputs[1])
        link(compare_node_1.outputs[0],multiply_node_1.inputs[0])
        link(compare_node_2.outputs[0],invert_node_1.inputs[1])
        link(invert_node_1.outputs[0],multiply_node_1.inputs[1])
        link(multiply_node_1.outputs[0],multiply_node_2.inputs[0])
        link(compare_node_3.outputs[0],multiply_node_2.inputs[1])
        link(multiply_node_2.outputs[0],group_out.inputs[0])

class BlackFilterNodeTree:
    def new():
        if 'BlackFilterNodeTree' in bpy.data.node_groups:
            return
        export_group_tree = bpy.data.node_groups.new('BlackFilterNodeTree','CompositorNodeTree')

        group_in = export_group_tree.nodes.new('NodeGroupInput')
        group_in.location = (-600,0)

        export_group_tree.inputs.new('NodeSocketFloatFactor','S')
        export_group_tree.inputs.new('NodeSocketFloatFactor','V')

        group_out = export_group_tree.nodes.new('NodeGroupOutput')
        group_out.location = (300,0)

        export_group_tree.outputs.new('NodeSocketColor','Color')

        compare_node_1 = export_group_tree.nodes.new('CompositorNodeMath')
        compare_node_1.operation = 'COMPARE'
        compare_node_1.inputs[1].default_value = 0.0
        compare_node_1.inputs[2].default_value = 0.001
        compare_node_1.location = (-400,-10)
        compare_node_1.hide = True

        
        compare_node_2 = export_group_tree.nodes.new('CompositorNodeMath')
        compare_node_2.operation = 'COMPARE'
        compare_node_2.inputs[1].default_value = 1.0
        compare_node_2.inputs[2].default_value = 0.05
        compare_node_2.location = (-400,-45)
        compare_node_2.hide = True

        multiply_node_1 = export_group_tree.nodes.new('CompositorNodeMath')
        multiply_node_1.operation = 'MULTIPLY'
        multiply_node_1.location = (-100,-27.5)
        multiply_node_1.hide = True

        invert_node_1 = export_group_tree.nodes.new('CompositorNodeInvert')
        invert_node_1.location = (-250,-45)
        invert_node_1.hide = True


        link = export_group_tree.links.new

        link(group_in.outputs[0],compare_node_1.inputs[0])
        link(group_in.outputs[1],compare_node_2.inputs[0])
        link(compare_node_1.outputs[0],multiply_node_1.inputs[0])
        link(compare_node_2.outputs[0],invert_node_1.inputs[1])
        link(invert_node_1.outputs[0],multiply_node_1.inputs[1])
        link(multiply_node_1.outputs[0],group_out.inputs[0])

class BinarizationNodeTree:
    def new():
        if 'BinarizationNodeTree' in bpy.data.node_groups:
            return
        export_group_tree = bpy.data.node_groups.new('BinarizationNodeTree','CompositorNodeTree')

        group_in = export_group_tree.nodes.new('NodeGroupInput')
        group_in.location = (-800,0)

        export_group_tree.outputs.new('NodeSocketColor','Color')

        export_group_tree.inputs.new('NodeSocketColor','Image')
        export_group_tree.inputs.new('NodeSocketFloatFactor','Black Threshold').default_value = 0.5
        export_group_tree.inputs.new('NodeSocketFloatFactor','Red Threshold').default_value = 0.5
        export_group_tree.inputs.new('NodeSocketFloatFactor','Green Threshold').default_value = 0.5
        export_group_tree.inputs.new('NodeSocketFloatFactor','Blue Threshold').default_value = 0.5

        group_out = export_group_tree.nodes.new('NodeGroupOutput')
        group_out.location = (800,0)

        sep_hsva_nodes = export_group_tree.nodes.new('CompositorNodeSepHSVA')
        sep_hsva_nodes.location = (-550,-120)

        blk_binarize_node = general.BlackBinarizationNode.new(name="Black Binarization",parent=export_group_tree)
        blk_binarize_node.location = (-300,310)
        blk_binarize_node.hide = True

        red_binarize_node = general.ColorBinarizationNode.new(name="Red Binarization",parent=export_group_tree)
        red_binarize_node.location = (-300,230)
        red_binarize_node.hide = True

        green_binarize_node = general.ColorBinarizationNode.new(name="Green Binarization",parent=export_group_tree)
        green_binarize_node.location = (-300,150)
        green_binarize_node.hide = True

        blue_binarize_node = general.ColorBinarizationNode.new(name="Blue Binarization",parent=export_group_tree)
        blue_binarize_node.location = (-300,70)
        blue_binarize_node.hide = True

        blk_filter_node = general.BlackFilterNode.new(name="Black Filter",parent=export_group_tree)
        blk_filter_node.location = (-300,-70)
        blk_filter_node.hide = True

        #Red:   Hue = 0.000000
        red_filter_node = general.ColorFilterNode.new(name="Red Filter",parent=export_group_tree)
        red_filter_node.location = (-300,-150)
        red_filter_node.inputs['Hue'].default_value = 0.00
        red_filter_node.hide = True

        #Green: Hue = 0.333333
        green_filter_node = general.ColorFilterNode.new(name="Green Filter",parent=export_group_tree)
        green_filter_node.location = (-300,-230)
        green_filter_node.inputs['Hue'].default_value = 0.333333
        green_filter_node.hide = True

        #Blue:  Hue = 0.666667
        blue_filter_node = general.ColorFilterNode.new(name="Blue Filter",parent=export_group_tree)
        blue_filter_node.location = (-300,-310)
        blue_filter_node.inputs['Hue'].default_value = 0.666667
        blue_filter_node.hide = True

        blk_comb_rgba_node = export_group_tree.nodes.new('CompositorNodeCombRGBA')
        blk_comb_rgba_node.location = (-50,310)
        blk_comb_rgba_node.hide = True

        red_comb_rgba_node = export_group_tree.nodes.new('CompositorNodeCombRGBA')
        red_comb_rgba_node.location = (-50,230)
        red_comb_rgba_node.hide = True

        green_comb_rgba_node = export_group_tree.nodes.new('CompositorNodeCombRGBA')
        green_comb_rgba_node.location = (-50,150)
        green_comb_rgba_node.hide = True

        blue_comb_rgba_node = export_group_tree.nodes.new('CompositorNodeCombRGBA')
        blue_comb_rgba_node.location = (-50,70)
        blue_comb_rgba_node.hide = True

        alph_over_node_1 = export_group_tree.nodes.new('CompositorNodeAlphaOver')
        alph_over_node_1.location = (200,270)
        alph_over_node_1.hide = True

        alph_over_node_2 = export_group_tree.nodes.new('CompositorNodeAlphaOver')
        alph_over_node_2.location = (200,110)
        alph_over_node_2.hide = True

        alph_over_node_3 = export_group_tree.nodes.new('CompositorNodeAlphaOver')
        alph_over_node_3.location = (450,190)
        alph_over_node_3.hide = True

        link = export_group_tree.links.new

        link(group_in.outputs[0],sep_hsva_nodes.inputs[0])
        link(group_in.outputs[1],blk_binarize_node.inputs[2])
        link(group_in.outputs[2],red_binarize_node.inputs[2])
        link(group_in.outputs[3],green_binarize_node.inputs[2])
        link(group_in.outputs[4],blue_binarize_node.inputs[2])

        link(sep_hsva_nodes.outputs['S'],blk_filter_node.inputs['S'])
        link(sep_hsva_nodes.outputs['V'],blk_filter_node.inputs['V'])

        link(sep_hsva_nodes.outputs['H'],red_filter_node.inputs['H'])
        link(sep_hsva_nodes.outputs['S'],red_filter_node.inputs['S'])
        link(sep_hsva_nodes.outputs['V'],red_filter_node.inputs['V'])

        link(sep_hsva_nodes.outputs['H'],green_filter_node.inputs['H'])
        link(sep_hsva_nodes.outputs['S'],green_filter_node.inputs['S'])
        link(sep_hsva_nodes.outputs['V'],green_filter_node.inputs['V'])

        link(sep_hsva_nodes.outputs['H'],blue_filter_node.inputs['H'])
        link(sep_hsva_nodes.outputs['S'],blue_filter_node.inputs['S'])
        link(sep_hsva_nodes.outputs['V'],blue_filter_node.inputs['V'])

        link(blk_filter_node.outputs[0],blk_binarize_node.inputs['Filter'])
        link(sep_hsva_nodes.outputs['V'],blk_binarize_node.inputs['Strength'])
        
        link(red_filter_node.outputs[0],red_binarize_node.inputs['Filter'])
        link(sep_hsva_nodes.outputs['S'],red_binarize_node.inputs['Strength'])

        link(green_filter_node.outputs[0],green_binarize_node.inputs['Filter'])
        link(sep_hsva_nodes.outputs['S'],green_binarize_node.inputs['Strength'])

        link(blue_filter_node.outputs[0],blue_binarize_node.inputs['Filter'])
        link(sep_hsva_nodes.outputs['S'],blue_binarize_node.inputs['Strength'])

        link(blk_binarize_node.outputs[0],blk_comb_rgba_node.inputs['R'])
        link(blk_binarize_node.outputs[0],blk_comb_rgba_node.inputs['G'])
        link(blk_binarize_node.outputs[0],blk_comb_rgba_node.inputs['B'])

        link(red_binarize_node.outputs[0],red_comb_rgba_node.inputs['R'])
        link(red_binarize_node.outputs[0],red_comb_rgba_node.inputs['A'])

        link(green_binarize_node.outputs[0],green_comb_rgba_node.inputs['G'])
        link(green_binarize_node.outputs[0],green_comb_rgba_node.inputs['A'])

        link(blue_binarize_node.outputs[0],blue_comb_rgba_node.inputs['B'])
        link(blue_binarize_node.outputs[0],blue_comb_rgba_node.inputs['A'])

        link(blk_comb_rgba_node.outputs[0],alph_over_node_1.inputs[1])
        link(red_comb_rgba_node.outputs[0],alph_over_node_1.inputs[2])

        link(green_comb_rgba_node.outputs[0],alph_over_node_2.inputs[1])
        link(blue_comb_rgba_node.outputs[0],alph_over_node_2.inputs[2])

        link(alph_over_node_1.outputs[0],alph_over_node_3.inputs[1])
        link(alph_over_node_2.outputs[0],alph_over_node_3.inputs[2])

        link(alph_over_node_3.outputs[0],group_out.inputs[0])
        
class PaperOutputNodeTree:
    def new():
        if 'PaperOutputNodeTree' in bpy.data.node_groups:
            return
        export_group_tree = bpy.data.node_groups.new("PaperOutputNodeTree",'CompositorNodeTree')

        group_out = export_group_tree.nodes.new('NodeGroupOutput')
        group_out.location = (400,0)

        export_group_tree.outputs.new('NodeSocketColor','Color')

        a01_img_node = export_group_tree.nodes.new('CompositorNodeImage')
        a01_img_node.location = (-400,75)
        a01_img_node.hide = True

        a01_switch_node = export_group_tree.nodes.new('CompositorNodeSwitch')
        a01_switch_node.location = (-200,75)
        a01_switch_node.inputs[0].default_value = (0,0,0,0)
        a01_switch_node.check = True
        a01_switch_node.hide = True

        b02_img_node = export_group_tree.nodes.new('CompositorNodeImage')
        b02_img_node.location = (-400,25)
        b02_img_node.hide = True

        b02_switch_node = export_group_tree.nodes.new('CompositorNodeSwitch')
        b02_switch_node.location = (-200,25)
        b02_switch_node.inputs[0].default_value = (0,0,0,0)
        b02_switch_node.check = True
        b02_switch_node.hide = True

        c03_img_node = export_group_tree.nodes.new('CompositorNodeImage')
        c03_img_node.location = (-400,-25)
        c03_img_node.hide = True

        c03_switch_node = export_group_tree.nodes.new('CompositorNodeSwitch')
        c03_switch_node.location = (-200,-25)
        c03_switch_node.inputs[0].default_value = (0,0,0,0)
        c03_switch_node.check = True
        c03_switch_node.hide = True

        d04_img_node = export_group_tree.nodes.new('CompositorNodeImage')
        d04_img_node.location = (-400,-75)
        d04_img_node.hide = True

        d04_switch_node = export_group_tree.nodes.new('CompositorNodeSwitch')
        d04_switch_node.location = (-200,-75)
        d04_switch_node.inputs[0].default_value = (0,0,0,0)
        d04_switch_node.check = True
        d04_switch_node.hide = True

        alpha_over_node_1 = export_group_tree.nodes.new('CompositorNodeAlphaOver')
        alpha_over_node_1.location = (0,25)
        alpha_over_node_1.hide = True

        alpha_over_node_2 = export_group_tree.nodes.new('CompositorNodeAlphaOver')
        alpha_over_node_2.location = (0,-25)
        alpha_over_node_2.hide = True

        alpha_over_node_3 = export_group_tree.nodes.new('CompositorNodeAlphaOver')
        alpha_over_node_3.location = (200,0)
        alpha_over_node_3.hide = True

        link = export_group_tree.links.new

        link(a01_img_node.outputs[0],a01_switch_node.inputs[1])
        link(b02_img_node.outputs[0],b02_switch_node.inputs[1])
        link(c03_img_node.outputs[0],c03_switch_node.inputs[1])
        link(d04_img_node.outputs[0],d04_switch_node.inputs[1])
        link(a01_switch_node.outputs[0],alpha_over_node_1.inputs[1])
        link(b02_switch_node.outputs[0],alpha_over_node_1.inputs[2])
        link(c03_switch_node.outputs[0],alpha_over_node_2.inputs[1])
        link(d04_switch_node.outputs[0],alpha_over_node_2.inputs[2])
        link(alpha_over_node_1.outputs[0],alpha_over_node_3.inputs[1])
        link(alpha_over_node_2.outputs[0],alpha_over_node_3.inputs[2])
        link(alpha_over_node_3.outputs[0],group_out.inputs[0])

class AniScannerNodeTree:
    def new():
        if 'AniScannerNodeTree' in bpy.data.node_groups:
            return
        export_group_tree = bpy.data.node_groups.new("AniScannerNodeTree",'CompositorNodeTree')

        group_in = export_group_tree.nodes.new('NodeGroupInput')
        group_in.location = (-400,0)

        export_group_tree.inputs.new('NodeSocketColor','Image')

        group_out = export_group_tree.nodes.new('NodeGroupOutput')
        group_out.location = (400,0)

        export_group_tree.outputs.new('NodeSocketColor','Color')

        binarize_node = general.BinarizationNode.new("Binarization",export_group_tree)
        binarize_node.location = (-200,-20)
        binarize_node.hide = True

        binarize_switch_node = export_group_tree.nodes.new('CompositorNodeSwitch')
        binarize_switch_node.label = "Binarization Switch"
        binarize_switch_node.check = False
        binarize_switch_node.location = (0,-20)
        binarize_switch_node.hide = True

        paper_node = general.PaperOutputNode.new("Paper Output",export_group_tree)
        paper_node.location = (-200,-70)
        paper_node.hide = True

        paper_switch_node = export_group_tree.nodes.new('CompositorNodeSwitch')
        paper_switch_node.label = "Paper Switch"
        paper_switch_node.inputs[0].default_value = (0,0,0,0)
        paper_switch_node.check = True
        paper_switch_node.location = (0,-70)
        paper_switch_node.hide = True

        alpha_over_node = export_group_tree.nodes.new('CompositorNodeAlphaOver')
        alpha_over_node.location = (150,-45)
        alpha_over_node.hide = True

        link = export_group_tree.links.new

        link(group_in.outputs[0],binarize_node.inputs[0])
        link(group_in.outputs[0],binarize_switch_node.inputs[0])
        link(binarize_node.outputs[0],binarize_switch_node.inputs[1])
        link(paper_node.outputs[0],paper_switch_node.inputs[1])
        link(binarize_switch_node.outputs[0],alpha_over_node.inputs[1])
        link(paper_switch_node.outputs[0],alpha_over_node.inputs[2])
        link(alpha_over_node.outputs[0],group_out.inputs[0])

node_trees = (
    ColorBinarizationNodeTree,
    BlackBinarizationNodeTree,
    ColorFilterNodeTree,
    BlackFilterNodeTree,
    BinarizationNodeTree,
    PaperOutputNodeTree,
    AniScannerNodeTree,
)

def generalTrees():
    for node_tree in node_trees:
        node_tree.new()