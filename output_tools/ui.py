import bpy
from bpy.types import Panel,Operator


class ANITOOLS_PT_export:
    bl_label = "Export Setting"
    bl_category = '2D Animation Toolkit'
    bl_region_type = "UI"

    def draw(self,context):
        self.layout.label(text="Export Setting")

class ANITOOLS_PT_export_3d(ANITOOLS_PT_export,Panel):
    bl_idname = "ANITOOLS_PT_export_3d"
    bl_space_type = "VIEW_3D"

class ANITOOLS_PT_export_img(ANITOOLS_PT_export,Panel):
    bl_idname = "ANITOOLS_PT_export_img"
    bl_space_type = "IMAGE_EDITOR"




classes = (
    ANITOOLS_PT_export_3d,
    ANITOOLS_PT_export_img,
)