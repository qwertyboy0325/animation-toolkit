from . import paper_tools
import bpy
from bpy.types import PropertyGroup

class AniToolsScene(PropertyGroup):
    paper_setting : bpy.props.PointerProperty(type=paper_tools.props.AniPaperProps)

classes = \
    paper_tools.classes + \
    (AniToolsScene,)