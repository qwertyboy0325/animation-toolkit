bl_info = {
    "name" : "2d_animation_toolkit",
    "author" : "Ezra Wu",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from . import preference
from .classes import classes,AniToolsScene


def register():
    preference.preference_register()
    
    if preference.import_dependencies_and_check():
        for cls in classes:
            bpy.utils.register_class(cls)
        bpy.types.Scene.anitools = bpy.props.PointerProperty(type=AniToolsScene)

def unregister():
    preference.preference_unregister()

    if preference.is_dependencies_installed:
        for cls in classes:
            bpy.utils.unregister_class(cls)
        del bpy.types.Scene.anitools

if __name__ == "__main__":
    register()