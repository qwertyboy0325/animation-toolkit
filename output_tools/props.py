import bpy

from bpy.props import PointerProperty

class FileSettingProps(bpy.types.PropertyGroup):
    filepath: bpy.props.StringProperty(name="File Path", default="/tmp\\" )
    filename: bpy.props.StringProperty(name="File Name", default="A")
    color_depth: bpy.props.StringProperty(name="Color Depth", default="8")

class ScannerSettingProps(bpy.types.PropertyGroup):
    render_paper: bpy.props.BoolProperty(name="Render Paper", default=True)
    

class BinarizationSettingProps:
    enable: bpy.props.BoolProperty(name="Binarization", default=False)
    black_threshold: bpy.props.FloatProperty(name="Black Threshold", default=0.5, max=1.0, min=0.0)
    red_threshold: bpy.props.FloatProperty(name="Red Threshold", default=0.5, max=1.0, min=0.0)
    green_threshold: bpy.props.FloatProperty(name="Green Threshold", default=0.5, max=1.0, min=0.0)
    blue_threshold: bpy.props.FloatProperty(name="Blue Threshold", default=0.5, max=1.0, min=0.0)