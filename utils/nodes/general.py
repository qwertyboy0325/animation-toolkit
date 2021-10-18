import bpy
from bpy.types import NodeTree
from .tree import generalTrees

class AniNodeInterface:
    def new(name: str,parent) ->NodeTree:
        pass
    def update() -> None :
        pass

class ColorBinarizationNode(AniNodeInterface):
    @staticmethod
    def new(name,parent):
        export_group = parent.nodes.new('CompositorNodeGroup')
        if 'AniScannerNodeTree' not in bpy.data.node_groups:
            generalTrees()

        export_group.node_tree = bpy.data.node_groups['ColorBinarizationNodeTree']
        export_group.name = name
        return export_group

class BlackBinarizationNode(AniNodeInterface):
    @staticmethod
    def new(name,parent):
        export_group = parent.nodes.new('CompositorNodeGroup')
        if 'AniScannerNodeTree' not in bpy.data.node_groups:
            generalTrees()

        export_group.node_tree = bpy.data.node_groups['BlackBinarizationNodeTree']
        export_group.name = name
        return export_group

class ColorFilterNode(AniNodeInterface):
    @staticmethod
    def new(name,parent):
        export_group = parent.nodes.new('CompositorNodeGroup')
        if 'AniScannerNodeTree' not in bpy.data.node_groups:
            generalTrees()

        export_group.node_tree = bpy.data.node_groups['ColorFilterNodeTree']
        export_group.name = name
        return export_group
      
class BlackFilterNode(AniNodeInterface):
    @staticmethod
    def new(name,parent):
        export_group = parent.nodes.new('CompositorNodeGroup')
        if 'AniScannerNodeTree' not in bpy.data.node_groups:
            generalTrees()

        export_group.node_tree = bpy.data.node_groups['BlackFilterNodeTree']
        export_group.name = name
        return export_group

class BinarizationNode(AniNodeInterface):
    @staticmethod
    def new(name,parent):
        export_group = parent.nodes.new('CompositorNodeGroup')
        if 'AniScannerNodeTree' not in bpy.data.node_groups:
            generalTrees()

        export_group.node_tree = bpy.data.node_groups['BinarizationNodeTree']
        export_group.name = name
        return export_group


class PaperOutputNode(AniNodeInterface):
    @staticmethod
    def new(name,parent):
        export_group = parent.nodes.new('CompositorNodeGroup')
        if 'AniScannerNodeTree' not in bpy.data.node_groups:
            generalTrees()
        
        export_group.node_tree = bpy.data.node_groups['PaperOutputNodeTree']
        export_group.name = name
        return export_group

class AniScannerNode(AniNodeInterface):
    @staticmethod
    def new(name,parent):
        export_group = parent.nodes.new('CompositorNodeGroup')
        if 'AniScannerNodeTree' not in bpy.data.node_groups:
            generalTrees()
        export_group.node_tree = bpy.data.node_groups['AniScannerNodeTree']
        export_group.name = name
        return export_group

