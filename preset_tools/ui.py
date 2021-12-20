import bpy
from bpy.types import Panel

class ANITOOLS_PT_preset:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'AniTools Presets'

class ANITOOLS_PT_preset_workspace(ANITOOLS_PT_preset,Panel):
    bl_idname = "ANITOOLS_PT_preset_workspace"
    bl_label = "Workspace Preset"

    def draw(self,context):
        layout = self.layout
        column = layout.column()
        column.operator("anitools.preset_workspace",text='workspace')
        column.operator("anitools.preset_human",text='human')

classes = (
    ANITOOLS_PT_preset_workspace,
)