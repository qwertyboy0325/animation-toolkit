import importlib
import bpy
import os
import sys

# TODO: FIX DIRTY CODE
# from PIL import Image,ImageDraw
def InitLibrary():
    try:
        from PIL import Image, ImageDraw
    except:
        print(sys.exc_info())
    else:
        globals()["Image"] = Image
        globals()["ImageDraw"]=ImageDraw

def GeneratePaper(context):
    
    scene_resolution = SceneResolution(context)
    SetSceneResolution(context,scene_resolution)
    DrawPaper(context,scene_resolution)
    
def SceneResolution(context):
    paper_setting = context.scene.anitools.paper_setting

    paper_size = paper_setting.paper_size
    overflow_area = paper_setting.overflow_area
    blank_space = paper_setting.blank_space

    # if(overflow_area.enable):
    #     overflow_area.width = 1~
    #     overflow_area.height = 1

    x = int(paper_size.x * (overflow_area.width if overflow_area.enable == True else 1) + blank_space.left + blank_space.right)
    y = int(paper_size.y * (overflow_area.height if overflow_area.enable == True else 1) + blank_space.top + blank_space.bottom)

    return [x,y]

def SetSceneResolution(context,scene_resolution):
    render = context.scene.render

    render.resolution_x = scene_resolution[0]
    render.resolution_y = scene_resolution[1]

def DrawPaper(context,scene_resolution):
    paper_setting = context.scene.anitools.paper_setting
    blank_space = paper_setting.blank_space
    overflow_area = paper_setting.overflow_area
    paper_size = paper_setting.paper_size
    title_safe = paper_setting.title_safe

    overflow_verts_pos = [
        (blank_space.left,blank_space.top),
        (scene_resolution[0]-blank_space.right,blank_space.top),
        (scene_resolution[0]-blank_space.right,scene_resolution[1]-blank_space.bottom),
        (blank_space.left,scene_resolution[1]-blank_space.bottom),
    ]
    
    basic_margin_x = (overflow_area.px_width - paper_size.x)/2
    basic_margin_y = (overflow_area.px_height - paper_size.y)/2
    print(overflow_verts_pos[0][0])

    basic_verts_pos =   [
        (overflow_verts_pos[0][0] + basic_margin_x, overflow_verts_pos[0][1] + basic_margin_y),
        (overflow_verts_pos[1][0] - basic_margin_x, overflow_verts_pos[1][1] + basic_margin_y),
        (overflow_verts_pos[2][0] - basic_margin_x, overflow_verts_pos[2][1] - basic_margin_y),
        (overflow_verts_pos[3][0] + basic_margin_x, overflow_verts_pos[3][1] - basic_margin_y),
    ]
    
    titlesafe_vert_pos = [
        (basic_verts_pos[0][0] + title_safe.left, basic_verts_pos[0][1] + title_safe.top),
        (basic_verts_pos[1][0] - title_safe.right, basic_verts_pos[1][1] + title_safe.top),
        (basic_verts_pos[2][0] - title_safe.right, basic_verts_pos[2][1] - title_safe.bottom),
        (basic_verts_pos[3][0] + title_safe.left, basic_verts_pos[3][1] - title_safe.bottom)
    ]

    center_vert_pos = (abs(basic_verts_pos[2][0]+basic_verts_pos[0][0])/2 , abs(basic_verts_pos[2][1]+basic_verts_pos[0][1])/2)


    DrawOverflowArea(overflow_verts_pos,scene_resolution)
    DrawBasicArea(basic_verts_pos,scene_resolution)
    DrawTitleSafeArea(titlesafe_vert_pos,scene_resolution)
    DrawCenter(center_vert_pos,scene_resolution)

def DrawOverflowArea(overflow_verts_pos,scene_resolution):
    DrawArea("A01_ovf",overflow_verts_pos,scene_resolution)

def DrawBasicArea(basic_verts_pos,scene_resolution):
    DrawArea("B02_bsc",basic_verts_pos,scene_resolution)

def DrawTitleSafeArea(titlesafe_vert_pos,scene_resolution):
    DrawArea("C03_tsf",titlesafe_vert_pos,scene_resolution)

def DrawArea(name,verts_pos,scene_resolution,col=(0,0,255,255)):
    path = os.path.abspath(str(bpy.app.binary_path)+"/../anitools")
    filepath = path + "/" + name + ".png"

    if not os.path.isdir(path):
        os.makedirs(path)

    os.remove(filepath) if os.path.isfile(filepath) else None

    img = Image.new("RGBA",size=tuple(scene_resolution),color=(0,0,0,0))
    draw = ImageDraw.Draw(img)
    for i in range(0,4):
        draw.line((verts_pos[i],verts_pos[((i+1)%4)]),fill=col,width=1)
    img.save(filepath, "PNG",)

def DrawCenter(center_vert_pos,scene_resolution,col=(0,0,255,255)):
    path = os.path.abspath(str(bpy.app.binary_path)+"/../anitools")
    print(path)
    filepath = path + "/D04_cnt.png"

    if not os.path.isdir(path):
        os.makedirs(path)

    os.remove(filepath) if os.path.isfile(filepath) else None

    img = Image.new("RGBA",size=tuple(scene_resolution),color=(0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.line(((center_vert_pos[0]-15,center_vert_pos[1]),(center_vert_pos[0]+15,center_vert_pos[1])),fill=col,width=1)
    draw.line(((center_vert_pos[0],center_vert_pos[1]-15),(center_vert_pos[0],center_vert_pos[1]+15)),fill=col,width=1)
    
    img.save(filepath,"PNG")

def SetAniBackground(cam):
    cam.data.background_images.clear()
    path = os.path.abspath(str(bpy.app.binary_path)+"/../anitools")
    if not os.path.isdir(path):
        os.makedirs(path)

    names = ["A01_ovf.png","B02_bsc.png","C03_tsf.png","D04_cnt.png"]

    imgs = []
    cam.data.show_background_images = True

    for name in names:
        imgs.append(bpy.data.images.load(path + "\\" + name))
    
    for img in imgs:
        bg = cam.data.background_images.new()
        bg.image = img
        bg.alpha = 1
