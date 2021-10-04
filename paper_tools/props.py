import bpy

from bpy.props import PointerProperty

def paper_size_update(self, context):
    paper_size = context.scene.anitools.paper_setting.paper_size
    render = context.scene.render
    render.resolution_x = paper_size.x
    render.resolution_y = paper_size.y

def multiple_to_px(self,context):
    paper_size = context.scene.anitools.paper_setting.paper_size
    overflow_area = context.scene.anitools.paper_setting.overflow_area
    overflow_area.px_width = paper_size.x * overflow_area.width
    overflow_area.px_height = paper_size.y * overflow_area.height


class OptionalProps:
    enable : bpy.props.BoolProperty(name="Enable",default=True)
    renderable : bpy.props.BoolProperty(name="Renderable",default=True)

class PaperSizeProps(bpy.types.PropertyGroup):
    x : bpy.props.IntProperty(name="Width",min=0,max=8192,soft_max=4096, subtype='PIXEL'
                                        ,default=1920,update=multiple_to_px)
    y : bpy.props.IntProperty(name="Height",min=0,max=8192,soft_max=4096, subtype='PIXEL'
                                        ,default=1080,update = multiple_to_px)
    dpi : bpy.props.IntProperty(name="dpi", min=1, max=800, subtype='PIXEL', default= 144)

class TitleSafeAreaProps(OptionalProps,bpy.types.PropertyGroup):
    top : bpy.props.IntProperty(name="Top",min=0,subtype='PIXEL')
    bottom : bpy.props.IntProperty(name="Bottom",min=0,subtype='PIXEL')
    left : bpy.props.IntProperty(name="Left",min=0,subtype='PIXEL')
    right : bpy.props.IntProperty(name="Right",min=0,subtype='PIXEL')

class OverflowAreaProps(OptionalProps,bpy.types.PropertyGroup):
    width : bpy.props.FloatProperty(name="Width",min=1,default=1.1,update=multiple_to_px)
    height : bpy.props.FloatProperty(name="Height",min=1,default=1.1,update=multiple_to_px)
    px_width: bpy.props.IntProperty(name="Offset X",min=0,default=2112,subtype='PIXEL')
    px_height: bpy.props.IntProperty(name="Offset Y",min=0,default=1188,subtype='PIXEL')

    pixel_offset_x: bpy.props.FloatProperty(name="pixel_offset_x")
    pixel_offset_y: bpy.props.FloatProperty(name="pixel_offset_y")

class BlankSpaceProps(bpy.types.PropertyGroup):
    top : bpy.props.IntProperty(name="Top",min=0,subtype='PIXEL',default=54)
    bottom : bpy.props.IntProperty(name="Bottom",min=0,subtype='PIXEL',default=54)
    left : bpy.props.IntProperty(name="Left",min=0,subtype='PIXEL',default=72)
    right : bpy.props.IntProperty(name="Right",min=0,subtype='PIXEL',default=72)

class AniPaperProps(bpy.types.PropertyGroup):
    paper_size : PointerProperty(type = PaperSizeProps)
    title_safe : PointerProperty(type = TitleSafeAreaProps)
    overflow_area: PointerProperty(type = OverflowAreaProps)
    blank_space : PointerProperty(type = BlankSpaceProps)

classes = (
    PaperSizeProps,
    TitleSafeAreaProps,
    OverflowAreaProps,
    BlankSpaceProps,
    AniPaperProps,
)