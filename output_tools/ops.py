from os import name
import bpy
from bpy.props import BoolProperty
from ..utils import nodes

class OUTPUT_OT_output(bpy.types.Operator):
    bl_idname = "anitools.output"
    bl_label = "Render"

    animation = BoolProperty(default=False)

    def execute(self,context):

        if context.scene.use_nodes is False :
            context.scene.use_nodes = True
        
        compositor = context.scene.node_tree

        
        render_layers = compositor.nodes['Render Layers'] if 'Render Layers' in compositor.nodes else generateRLayers(compositor)
        render_layers.location = (-400,0)

        composite = compositor.nodes['Composite'] if 'Composite' in compositor.nodes else generateComposite(compositor)
        composite.location = (200,0)


        scanner = compositor.nodes['AniTools Scanner'] if 'AniTools Scanner' in compositor.nodes else generateScanner(compositor)
        scanner.location = (0,0)

        link = compositor.links.new

        link(render_layers.outputs[0],scanner.inputs[0])
        link(scanner.outputs[0],composite.inputs[0])

        #TODO: Check Anitool nodes exist
            #TODO: If all nodes not exist then generate
            #TODO: If some nodes exist but some noes not than delete(belone anitools nodes) and generate

        #TODO: Set Nodes Properties Value
        #TODO: Render(check animantion)

        return {'FINISHED'}

def generateRLayers(parent):
    return parent.nodes.new('CompositorNodeRLayers')

def generateComposite(parent):
    return parent.nodes.new('CompositorNodeComposite')

def generateScanner(parent):
    return nodes.AniScannerNode.new(name="AniTools Scanner",parent=parent)

classes = (
    OUTPUT_OT_output,
)