import bpy
from bpy.types import Operator
from ..utils import support

class PRESET_OT_ani_workspace(Operator):
    bl_idname = "anitools.preset_workspace"
    bl_label = "Add Ani Workspace"

    def execute(self, context):
        root_path = support.get_rootpath()
        import os
        preset_path = os.path.join(root_path, "utils", "presets", "preset.blend")
        bpy.ops.workspace.append_activate(idname='FUYO_set',filepath = preset_path)

        return {"FINISHED"}

class PRESET_OT_ani_human(Operator):
    bl_idname = "anitools.preset_human"
    bl_label = "Import Human Preset"

    def execute(self, context):
        root_path = support.get_rootpath()
        import os
        human_path = os.path.join(root_path, "utils", "presets", "human_preset.blend")
        colls = []

        with bpy.data.libraries.load(human_path) as (data_from, _):
            for name in data_from.collections:
                if name == "character1":
                    colls.append({'name': name})
            action = bpy.ops.wm.link
            action(directory=human_path + "/Collection/", files=colls)

            bpy.ops.object.make_override_library()

        return {"FINISHED"}


classes = (
    PRESET_OT_ani_workspace,
    PRESET_OT_ani_human,
)