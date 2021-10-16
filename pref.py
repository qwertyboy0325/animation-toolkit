from .classes import classes,AniToolsScene
import os
import subprocess
import bpy
from bpy.types import AddonPreferences,Operator,Panel
from collections import namedtuple
import importlib
import sys
from . import bl_info

Dependency = namedtuple("Dependency",["module","package","name"])

dependencies = (
        Dependency(module="PIL" ,package="pillow" ,name="PIL"),
    )

is_dependencies_installed = False

def import_module(module_name, global_name=None):
    if global_name is None:
        global_name = module_name
    if global_name is globals():
        importlib.reload(globals()[global_name])
    else:
        globals()[global_name] = importlib.import_module(module_name)

def install_pip():
    try:
        subprocess.run([sys.executable,"-m","pip","--version"], check=True)
    except subprocess.CalledProcessError:
        import ensurepip
        ensurepip.bootstrap()
        os.environ.pop("PIP_REQ_TRACKER",None)

def install_and_import_module(module_name, package_name=None, global_name=None):
    if package_name is None:
        package_name = module_name

    if global_name is None:
        global_name = module_name
    
    environ_copy = dict(os.environ)
    environ_copy["PYTHONNOUSERSITE"] = "1"

    subprocess.run([sys.executable, "-m", "pip", "install", package_name], check=True, env = environ_copy)

    import_module(module_name, global_name)

class ANITOOLS_preferences(AddonPreferences):
    bl_idname = __package__

    @classmethod
    def draw(self,context):
        layout = self.layout
        layout.operator(ANITOOLS_OT_install_dependencies.bl_idname, icon="CONSOLE")

class ANITOOLS_OT_install_dependencies(Operator):
    bl_idname = "anitools.install_dependencies"
    bl_label = "install dependencies"
    bl_description = ("")
    bl_options = {"REGISTER","INTERNAL"}

    @classmethod
    def poll(self, context):
        # Deactiveate when dependencies have been installed
        return not is_dependencies_installed

    def execute(self, context):
        try:
            install_pip()
            for dependency in dependencies:
                install_and_import_module(dependency.module,dependency.package,dependency.name)
        except (subprocess.CalledProcessError, ImportError) as err:
            self.report({"ERROR"}, err.msg)
            return {"CANCELLED"}

        global is_dependencies_installed
        is_dependencies_installed = True

        for cls in classes:
            bpy.utils.register_class(cls)
        bpy.types.Scene.anitools = bpy.props.PointerProperty(type=AniToolsScene)
        
        return {"FINISHED"}


class ANITOOLS_PT_warning_panel(Panel):
    bl_idname = "ANITOOLS_PT_warning_panel"
    bl_label = "AniTools Warning"
    bl_category = "2D Animation Toolkit"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    @classmethod
    def poll(self, context):
        return not is_dependencies_installed
    
    def draw(self, context):
        layout = self.layout

        lines = [
                    f"Please install the missing dependencies for the \"{bl_info.get('name')}\" add-on.",
                    f"1. Open the preferences (Edit > Preferences > Add-ons).",
                    f"2. Search for the \"{bl_info.get('name')}\" add-on.",
                    f"3. Open the details section of the add-on.",
                    f"4. Click on the \"{ANITOOLS_OT_install_dependencies.bl_label}\" button.",
                    f"   This will download and install the missing Python packages, if Blender has the required",
                    f"   permissions.",
                    f"If you're attempting to run the add-on from the text editor, you won't see the options described",
                    f"above. Please install the add-on properly through the preferences.",
                    f"1. Open the add-on preferences (Edit > Preferences > Add-ons).",
                    f"2. Press the \"Install\" button.",
                    f"3. Search for the add-on file.",
                    f"4. Confirm the selection by pressing the \"Install Add-on\" button in the file browser."
                ]
        for line in lines:
            layout.label(text=line)

preference_classes =    (ANITOOLS_PT_warning_panel,
                         ANITOOLS_OT_install_dependencies,
                         ANITOOLS_preferences,
                        )

def preference_register():
    global is_dependencies_installed
    is_dependencies_installed = False

    for cls in preference_classes:
        bpy.utils.register_class(cls)

def preference_unregister():
    for cls in preference_classes:
        bpy.utils.unregister_class(cls)

def import_dependencies_and_check():
    global is_dependencies_installed

    try:
        for dependency in dependencies:
            import_module(module_name=dependency.module, global_name=dependency.name)
    except ModuleNotFoundError:
        return False
    else:
        is_dependencies_installed = True
        return True
