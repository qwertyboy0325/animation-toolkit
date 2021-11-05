from typing import Text
import bpy
from bpy import props
from bpy.types import Panel,Operator
from .props import AniOutputProps


def draw_threshold(layout,binirization,label,prop_name):
        row = layout.row()
        row.scale_x = 0.6
        row.label(text = label)
        row.scale_x = 0.4
        row.prop(binirization,prop_name,text = "")

class ANITOOLS_PT_output:
    bl_label = "Output Setting"
    bl_category = '2D Animation Toolkit'
    bl_region_type = "UI"

    def draw(self,context):
        layout = self.layout
        column = layout.column()
        column.label(text = "Render:")
        row = column.row(align=True)

        render_action = context.scene.anitools.output_setting.render_action
        if render_action == 'DEF':
            op = row.operator("render.render",text = "Animation",icon = "RENDER_ANIMATION")
            op.animation = True
        else:
            op = row.operator("anitools.output",text = "Animation",icon = "RENDER_ANIMATION")

        
class ANITOOLS_PT_file_setting:
    bl_label = "File Setting"
    bl_region_type = "UI"

    
    def draw(self,context):
        layout = self.layout

        lines = [
            f"Tips:",
            f"You can customize your sequence naming rules.",
            f"'#' represents the number of the sequence",
            f"Example:",
            f"Name: Example###^",
            f"Output result: Example001^, Example002^"
        ]

        file_setting = context.scene.anitools.output_setting.file_setting
        image_setting = context.scene.render.image_settings
        # filepath = file_setting.filepath

        column = layout.column(align=False)
        subrow = column.row()
        subrow.scale_x = 0.5
        subrow.label(text="Output Path")
        subrow.scale_x = 0.5
        subrow.prop(file_setting, 'filepath', text = "")

        column.separator()

        subrow = column.row()
        subrow.scale_x = 0.5
        subrow.label(text="Name")
        subrow.scale_x = 0.5
        subrow.prop(file_setting, 'filename', text = "")

        column.separator()

        row = column.row()
        row.scale_x = 0.5
        row.label(text="Color Depth")
        row.scale_x = 0.25
        row.prop_enum(image_setting, 'color_depth',"8")
        row.prop_enum(image_setting, 'color_depth',"16")

        column.separator()

        row = column.row()
        row.scale_x = 0.5
        row.label(text="Format")
        row.prop_menu_enum(image_setting,"file_format",text=image_setting.file_format,icon='IMAGE_DATA')

        column.separator()

        box = column.box()
        col = box.column()
        for line in lines:
            col.label(text = line)

class ANITOOLS_PT_scanner_setting:
    bl_label = "Scanner Setting"
    bl_region_type = "UI"

    def draw(self,context):
        layout = self.layout
        scanner_setting = context.scene.anitools.output_setting.scanner_setting

        column = layout.column()
        column.prop(scanner_setting,"render_paper")

class ANITOOLS_PT_binirize_setting:
    bl_label = "Binirization"
    bl_region_type = "UI"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        layout = self.layout
        binirization = context.scene.anitools.output_setting.scanner_setting.binirization
        layout.prop(binirization,'enable',text="")

    def draw(self, context):
        layout = self.layout
        binirization = context.scene.anitools.output_setting.scanner_setting.binirization

        column = layout.column(align = True)

        column.label(text = "Threshold:")

        box = column.box()
        draw_threshold(box,binirization,"Black:","black_threshold")
        draw_threshold(box,binirization,"Red:","red_threshold")
        draw_threshold(box,binirization,"Green:","green_threshold")
        draw_threshold(box,binirization,"Blue:","blue_threshold")

        # row = column.row()
        # row.scale_x = 0.7
        # row.label("Black:")
        # row.scale_x = 0.3
        # row.prop(binirization,"black_threshold",text = "")

class ANITOOLS_PT_basic_setting:
    bl_label = "Basic Setting"
    bl_region_type = "UI"

    def draw(self,context):
        layout = self.layout

        scene = context.scene
        
        row = layout.row()

        ani_output = context.scene.anitools.output_setting
        render_action = ani_output.render_action

        column = row.column()
        column.label(text="Render Type")
        column.prop(ani_output, 'render_action', icon_only=False, emboss=True, text='')
        column.separator(factor = 2)


        column1 = layout.column(align=False)
        subrow = column1.row()
        subrow.scale_x = 0.5
        subrow.label(text="Frame Start")
        subrow.scale_x = 0.5
        subrow.prop(scene, 'frame_start', text = "")

        column1.separator()

        subrow = column1.row()
        subrow.scale_x = 0.5
        subrow.label(text="Frame End")
        subrow.scale_x = 0.5
        subrow.prop(scene, 'frame_end', text = "")

        column1.separator()

        subrow = column1.row()
        subrow.scale_x = 0.5
        subrow.label(text="Step")
        subrow.scale_x = 0.5
        subrow.prop(scene, 'frame_step', text = "")
        column1.enabled = True if render_action == 'DEF' else False

class ANITOOLS_PT_output_3d(ANITOOLS_PT_output,Panel):
    bl_idname = "ANITOOLS_PT_output_3d"
    bl_space_type = "VIEW_3D"

class ANITOOLS_PT_output_img(ANITOOLS_PT_output,Panel):
    bl_idname = "ANITOOLS_PT_output_img"
    bl_space_type = "IMAGE_EDITOR"


class ANITOOLS_PT_scanner_setting_3d(ANITOOLS_PT_scanner_setting,Panel):
    bl_parent_id = "ANITOOLS_PT_output_3d"
    bl_space_type = "VIEW_3D"

class ANITOOLS_PT_scanner_setting_img(ANITOOLS_PT_scanner_setting,Panel):
    bl_parent_id = "ANITOOLS_PT_output_img"
    bl_space_type = "IMAGE_EDITOR"

class ANITOOLS_PT_file_setting_3d(ANITOOLS_PT_file_setting,Panel):
    bl_parent_id = "ANITOOLS_PT_output_3d"
    bl_space_type = "VIEW_3D"

class ANITOOLS_PT_file_setting_img(ANITOOLS_PT_file_setting,Panel):
    bl_parent_id = "ANITOOLS_PT_output_img"
    bl_space_type = "IMAGE_EDITOR"

class ANITOOLS_PT_binirize_setting_3d(ANITOOLS_PT_binirize_setting,Panel):
    bl_parent_id = "ANITOOLS_PT_scanner_setting_3d"
    bl_space_type = "VIEW_3D"

class ANITOOLS_PT_binirize_setting_img(ANITOOLS_PT_binirize_setting,Panel):
    bl_parent_id = "ANITOOLS_PT_scanner_setting_img"
    bl_space_type = "IMAGE_EDITOR"

class ANITOOLS_PT_basic_setting_3d(ANITOOLS_PT_basic_setting,Panel):
    bl_parent_id = "ANITOOLS_PT_output_3d"
    bl_space_type = "VIEW_3D"

class ANITOOLS_PT_basic_setting_img(ANITOOLS_PT_basic_setting,Panel):
    bl_parent_id = "ANITOOLS_PT_output_img"
    bl_space_type = "IMAGE_EDITOR"

classes = (
    ANITOOLS_PT_output_3d,
    ANITOOLS_PT_output_img,
    ANITOOLS_PT_basic_setting_3d,
    ANITOOLS_PT_basic_setting_img,
    ANITOOLS_PT_file_setting_3d,
    ANITOOLS_PT_file_setting_img,
    ANITOOLS_PT_scanner_setting_3d,
    ANITOOLS_PT_scanner_setting_img,
    ANITOOLS_PT_binirize_setting_3d,
    ANITOOLS_PT_binirize_setting_img,
)