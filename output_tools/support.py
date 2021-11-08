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

def file_rename(name,num,replace_ch = '#'):
    end = name.rfind(replace_ch)
    start = 0
    for i in range(end-1,0,-1):
        if name[i] is not replace_ch:
            start = i + 1
            break

    count = (end - start) + 1
    out_num = str(num).zfill(count)
    new_name = str()

    for i in range(start,end+1):
        new_name = name[:start] + out_num + name[end+1:]
    return new_name

class KeyFrameHelper:
    @staticmethod
    def get_gp_objs(objects):
        gp_objs = []
        for object in objects:
            if type(object.data) == bpy.types.GreasePencil:
                gp_objs.append(object)
        return gp_objs

    @staticmethod
    def key_frames(gps_obj,use_selected = False,use_invisible_layer = False):
        keys = set()

        for gp_obj in gps_obj:
            gp = bpy.types.GreasePencil
            if gp_obj.hide_render == False:
                gp = gp_obj.data
            else:
                continue
            for layer in gp.layers:
                if use_invisible_layer is False and layer.hide is True:     #Skip Invisible Layer
                    continue
                for frame in layer.frames:
                    if use_selected is True and frame.select is False:
                        continue
                    keys.add(frame.frame_number)

        return keys

    @staticmethod
    def key_selected_objects(context)->set:
        objects = context.selected_objects
        gps_obj = KeyFrameHelper.get_gp_objs(objects)

        keys = KeyFrameHelper.key_frames(gps_obj,use_selected=False)
        keys.discard(0)

        return keys

    @staticmethod
    def keys_selected_frames(context)->set:
        objects = context.scene.objects
        gps_obj = KeyFrameHelper.get_gp_objs(objects)

        return KeyFrameHelper.key_frames(gps_obj,use_selected=True)
    
    @staticmethod
    def keys_all(context)->set:
        objects = context.scene.objects
        gps_obj = KeyFrameHelper.get_gp_objs(objects)

        keys = KeyFrameHelper.key_frames(gps_obj,use_selected=False)
        keys.discard(0)

        return keys
    
    @staticmethod
    def keys_selected(context)->bool:
        objects = context.scene.objects
        gps_obj = context.gpencil
        # gps_obj = KeyFrameHelper.get_gp_objs(objects)

        return KeyFrameHelper.gp_obj_selected(gps_obj,use_selected=True,use_invisible_layer=True)
    
    @staticmethod
    def objs_selected(context)->bool:
        objects = context.selected_objects
        gps_obj = KeyFrameHelper.get_gp_objs(objects)

        return KeyFrameHelper.gp_obj_selected(gps_obj)

    @staticmethod
    def gp_obj_selected(gps_obj,use_selected = False,use_invisible_layer = False)->bool:
        for gp_obj in gps_obj:
            gp = bpy.types.GreasePencil
            if gp_obj.hide_render == True:                                  #Skip Invisible Object
                continue
            gp = gp_obj.data                                                #Unpack Object to GP Object
            for layer in gp.layers:
                if use_invisible_layer is False and layer.hide is True:     #Skip Invisible Layer
                    continue
                for frame in layer.frames:
                    if use_selected is True and frame.select is False:
                        continue
                    return True
        return False