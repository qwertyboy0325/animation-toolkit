import bpy

from . import support

class PAPER_OT_generate_paper(bpy.types.Operator):
    bl_idname = "anitools.generate_paper"
    bl_label = "Generate Paper"
    def execute(self,context):
        cam = context.scene.camera
        # for test
        bpy.context.scene.use_nodes = True
        # end
        support.GeneratePaper(context)
        support.SetAniBackground(cam)
        return {'FINISHED'}

classes = (
    PAPER_OT_generate_paper,
)