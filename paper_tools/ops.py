import bpy
from . import support,props

class PAPER_OT_generate_paper(bpy.types.Operator):
    bl_idname = "anitools.generate_paper"
    bl_label = "Generate Paper"
    def execute(self,context):
        cam = context.scene.camera
        paper_size = context.scene.anitools.paper_setting.paper_size
        overflow_area = context.scene.anitools.paper_setting.overflow_area
        overflow_area.px_width = paper_size.x * overflow_area.width
        overflow_area.px_height = paper_size.y * overflow_area.height
        support.GeneratePaper(context)
        support.SetAniBackground(cam)

        props.set_background_image(context)

        return {'FINISHED'}

classes = (
    PAPER_OT_generate_paper,
)