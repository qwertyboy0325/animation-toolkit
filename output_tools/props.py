import bpy

from bpy.props import PointerProperty

# color_depth_t = [
#     ("8","8 bit","",1),
#     ("16","16 bit","",2),
# ]

def update_filepath(self,context):
    file_setting = context.scene.anitools.output_setting.file_setting
    filepath = file_setting.filepath
    filename = file_setting.filename
    if (filepath.endswith("\\") or filepath.endswith("/")) is False:
        filepath += "\\"

    
    output_filepath = filepath + filename
    bpy.context.scene.render.filepath = output_filepath
    print(bpy.context.scene.render.filepath)

class FileSettingProps(bpy.types.PropertyGroup):
    filepath: bpy.props.StringProperty(name="Path", default="/tmp\\", subtype='FILE_PATH', update=update_filepath)
    filename: bpy.props.StringProperty(name="File Name", default="####", subtype='FILE_NAME', update= update_filepath)
    # color_depth: bpy.props.EnumProperty(name="Color Depth", default=1,items=color_depth_t)

class BinarizationSettingProps(bpy.types.PropertyGroup):
    enable: bpy.props.BoolProperty(name="Binarization", default=False)
    black_threshold: bpy.props.FloatProperty(name="Black Threshold", default=0.5, max=1.0, min=0.0)
    red_threshold: bpy.props.FloatProperty(name="Red Threshold", default=0.5, max=1.0, min=0.0)
    green_threshold: bpy.props.FloatProperty(name="Green Threshold", default=0.5, max=1.0, min=0.0)
    blue_threshold: bpy.props.FloatProperty(name="Blue Threshold", default=0.5, max=1.0, min=0.0)

class ScannerSettingProps(bpy.types.PropertyGroup):
    render_paper: bpy.props.BoolProperty(name="Render Paper", default=True)
    binirization: bpy.props.PointerProperty(type = BinarizationSettingProps)

class AniOutputProps(bpy.types.PropertyGroup):
    file_setting: bpy.props.PointerProperty(type = FileSettingProps)
    scanner_setting: bpy.props.PointerProperty(type = ScannerSettingProps)

classes = (
    FileSettingProps,
    BinarizationSettingProps,
    ScannerSettingProps,
    AniOutputProps,
)