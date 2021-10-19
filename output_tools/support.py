import bpy

def setNodesProps(parent,context):
    if parent is None:
        return
    if ('AniTools Scanner' in parent.nodes)is False:
        return
    anitools_scanner = parent.nodes['AniTools Scanner']
    binarization = anitools_scanner.node_tree.nodes['Binarization']
    binarization_switch = anitools_scanner.node_tree.nodes['Binarization Switch']
    paper_switch = anitools_scanner.node_tree.nodes['Paper Switch']
    paper_output = anitools_scanner.node_tree.nodes['Paper Output']

    setBinarizationThreshold(binarization,context)
    setPaperImages(paper_output,context)
    setPaperImagesSwitch(paper_output,context)
    setBinarizationSwitch(binarization_switch,context)
    setPaperSwitch(paper_switch,context)
    return None

def setBinarizationThreshold(binarization,context):
    data = context.scene.anitools.output_setting.scanner_setting.binirization

    blk_threshold = binarization.inputs['Black Threshold']
    red_threshold = binarization.inputs['Red Threshold']
    green_threshold = binarization.inputs['Green Threshold']
    blue_threshold = binarization.inputs['Blue Threshold']

    blk_threshold.default_value = data.black_threshold
    red_threshold.default_value = data.red_threshold
    green_threshold.default_value = data.green_threshold
    blue_threshold.default_value = data.blue_threshold

    return

def setPaperImages(paper_output,context):
    imgs_name = ["A01_ovf.png","B02_bsc.png","C03_tsf.png","D04_cnt.png"]
    imgs = []
    input_imgs = (
        paper_output.node_tree.nodes['A01'],
        paper_output.node_tree.nodes['B02'],
        paper_output.node_tree.nodes['C03'],
        paper_output.node_tree.nodes['D04'],
    )
    for img_name in imgs_name:
        if img_name in bpy.data.images:
            imgs.append(bpy.data.images[img_name])
        else:
            imgs.append(None)

    for idx,input_img in enumerate(input_imgs):
        input_img.image = imgs[idx]

    return

def setPaperImagesSwitch(paper_output,context):
    data = context.scene.anitools.paper_setting

    title_safe = data.title_safe
    overflow_area = data.overflow_area

    title_safe_switch = (title_safe.enable and title_safe.renderable)
    overflow_area_switch = (overflow_area.enable and overflow_area.renderable)

    a01_switch = paper_output.node_tree.nodes['A01 Switch']
    b02_switch = paper_output.node_tree.nodes['B02 Switch']
    c03_switch = paper_output.node_tree.nodes['C03 Switch']
    d04_switch = paper_output.node_tree.nodes['D04 Switch']

    b02_switch.check = title_safe_switch
    c03_switch.check = overflow_area_switch

    return

def setBinarizationSwitch(switch,context):
    data = context.scene.anitools.output_setting.scanner_setting.binirization
    enable = data.enable
    switch.check = enable

    return

def setPaperSwitch(switch,context):
    data = context.scene.anitools.output_setting.scanner_setting
    enable = data.render_paper
    switch.check = enable

    return