from os import name
import bpy
from bpy.props import BoolProperty
from . import support
from ..utils import nodes

class OUTPUT_OT_output(bpy.types.Operator):
    bl_idname = "anitools.output"
    bl_label = "Render"

    animation = BoolProperty(default=False)

    def execute(self,context):

        if context.scene.use_nodes is False :
            context.scene.use_nodes = True
        
        compositor = context.scene.node_tree
        
        # Generate Nodes if Nodes not prepared
        generateNodes(compositor)
        # Set Nodes Properties Value
        support.setNodesProps(compositor,context)

        #TODO: Render(check animantion)

        return {'FINISHED'}

def generateNodes(parent):
        render_layers = parent.nodes['Render Layers'] if 'Render Layers' in parent.nodes else generateRLayers(parent)
        render_layers.location = (-400,0)

        composite = parent.nodes['Composite'] if 'Composite' in parent.nodes else generateComposite(parent)
        composite.location = (200,0)


        scanner = parent.nodes['AniTools Scanner'] if 'AniTools Scanner' in parent.nodes else generateScanner(parent)
        scanner.location = (0,0)

        link = parent.links.new

        link(render_layers.outputs[0],scanner.inputs[0])
        link(scanner.outputs[0],composite.inputs[0])

def generateRLayers(parent):
    return parent.nodes.new('CompositorNodeRLayers')

def generateComposite(parent):
    return parent.nodes.new('CompositorNodeComposite')

def generateScanner(parent):
    return nodes.AniScannerNode.new(name="AniTools Scanner",parent=parent)



classes = (
    OUTPUT_OT_output,
)