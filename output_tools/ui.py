import bpy
from bpy.types import Panel,Operator


class ANITOOLS_PT_output:
    bl_label = "Output Setting"
    bl_category = '2D Animation Toolkit'
    bl_region_type = "UI"

    def draw(self,context):
        layout = self.layout
        row = layout.row(align=True)
        # row.lable(text="")
        

class ANITOOLS_PT_output_3d(ANITOOLS_PT_output,Panel):
    bl_idname = "ANITOOLS_PT_output_3d"
    bl_space_type = "VIEW_3D"

class ANITOOLS_PT_output_img(ANITOOLS_PT_output,Panel):
    bl_idname = "ANITOOLS_PT_output_img"
    bl_space_type = "IMAGE_EDITOR"

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


classes = (
    ANITOOLS_PT_output_3d,
    ANITOOLS_PT_output_img,
    ANITOOLS_PT_file_setting_3d,
    ANITOOLS_PT_file_setting_img,
    ANITOOLS_PT_scanner_setting_3d,
    ANITOOLS_PT_scanner_setting_img
)