from . import paper_tools,output_tools
import bpy
from bpy.types import PropertyGroup

class AniToolsScene(PropertyGroup):
    paper_setting : bpy.props.PointerProperty(type=paper_tools.props.AniPaperProps)
    output_setting : bpy.props.PointerProperty(type=output_tools.props.AniOutputProps)

classes = \
    paper_tools.classes + \
    output_tools.classes + \
    (AniToolsScene,)