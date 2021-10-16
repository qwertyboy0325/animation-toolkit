import bpy

class ANITOOLS_PT:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = '2D Animation Toolkit'
    # bl_options = {'DEFAULT_CLOSED'}

class ANITOOLS_PT_paper_panel(ANITOOLS_PT,bpy.types.Panel):
    bl_idname = "ANITOOLS_PT_paper_panel"
    bl_label = "Papper Setting"

    def draw(self,context):
        layout = self.layout

        layout.operator("anitools.generate_paper", text='Generate')


class ANITOOLS_PT_paper_size(ANITOOLS_PT,bpy.types.Panel):
    bl_idname = "ANITOOLS_PT_paper_size"
    bl_label = "Papper Size"
    bl_parent_id = "ANITOOLS_PT_paper_panel"

    def draw(self, context):
        layout = self.layout
        anitools = context.scene.anitools
        paper_setting = anitools.paper_setting

        row = layout.row()
        column = layout.column()

        paper_size = paper_setting.paper_size

        column.prop(paper_size , 'x')
        column.prop(paper_size , 'y')
        column.prop(paper_size , 'dpi')


class ANITOOLS_PT_title_safe_area(ANITOOLS_PT,bpy.types.Panel):
    bl_idname = "ANITOOLS_PT_title_safe_area"
    bl_label = "Title Safe Area"
    bl_parent_id = "ANITOOLS_PT_paper_panel"

    def draw_header(self, context):
        layout = self.layout
        title_safe = context.scene.anitools.paper_setting.title_safe
        layout.prop(title_safe,'enable',text="")

    def draw(self, context):
        layout = self.layout
        anitools = context.scene.anitools
        paper_setting = anitools.paper_setting

        row = layout.row()
        column = layout.column()

        title_safe = paper_setting.title_safe

        column.prop(title_safe, 'top')
        column.prop(title_safe, 'bottom')
        column.prop(title_safe, 'left')
        column.prop(title_safe, 'right')
        column.prop(title_safe, 'renderable')


class ANITOOLS_PT_overflow_area(ANITOOLS_PT,bpy.types.Panel):
    bl_idname = "ANITOOLS_PT_overflow_area"
    bl_label = "Overflow Area"
    bl_parent_id = "ANITOOLS_PT_paper_panel"

    def draw_header(self, context):
        layout = self.layout
        overflow_area = context.scene.anitools.paper_setting.overflow_area
        layout.prop(overflow_area,'enable',text="")

    def draw(self, context):
        layout = self.layout
        anitools = context.scene.anitools
        paper_setting = anitools.paper_setting

        row = layout.row()
        column = layout.column()

        overflow_area = paper_setting.overflow_area

        column.prop(overflow_area, 'width')
        column.prop(overflow_area, 'height')
        # column.prop(overflow_area, 'offset_x')
        # column.prop(overflow_area, 'offset_y')
        column.prop(overflow_area, 'renderable')


class ANITOOLS_PT_blank_space(ANITOOLS_PT,bpy.types.Panel):
    bl_idname = "ANITOOLS_PT_blank_space"
    bl_label = "Blank Space"
    bl_parent_id = "ANITOOLS_PT_paper_panel"

    def draw(self, context):
        layout = self.layout
        anitools = context.scene.anitools
        paper_setting = anitools.paper_setting

        row = layout.row()
        column = layout.column()

        blank_space = paper_setting.blank_space

        column.prop(blank_space, 'top')
        column.prop(blank_space, 'bottom')
        column.prop(blank_space, 'left')
        column.prop(blank_space, 'right')

# class AniTools_PT_generate_paper(AniTools_PT,bpy.types.Panel):
#     bl_idname="AniTools_PT_generate_paper"
#     bl_label = ""
#     bl_parent_id = "AniTools_PT_paper_panel"

classes = (
    ANITOOLS_PT_paper_panel,
    ANITOOLS_PT_paper_size,
    ANITOOLS_PT_title_safe_area,
    ANITOOLS_PT_overflow_area,
    ANITOOLS_PT_blank_space,
)