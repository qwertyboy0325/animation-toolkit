import bpy
from . import props, ui , ops , support

classes = props.classes + ops.classes + ui.classes
support.InitLibrary()
# Panels Structure
# ------------------------------
# Main Panel
#   ∟ Papper Panel (紙張設定)
#       ∟ Basic Size (基本尺寸)
#       ∟ Title-safe Area (演出畫格)
#       ∟ Overflow Frame (作畫尺寸)
#       ∟ Blank Space (餘白)