from os import name, path
import bpy
from bpy.props import BoolProperty
from . import support
from .props import AniOutputProps
from ..utils import nodes
import math

class OUTPUT_OT_output(bpy.types.Operator):
    bl_idname = "anitools.output"
    bl_label = "Render"

    def get_gp_objs(self,objects):
        gp_objs = []
        for object in objects:
            if type(object.data) == bpy.types.GreasePencil:
                gp_objs.append(object)
        return gp_objs

    def key_frames(self,gps_obj,use_selected = False):
        keys = set()

        for gp_obj in gps_obj:
            gp = bpy.types.GreasePencil
            if gp_obj.hide_render == False:
                gp = gp_obj.data
            else:
                continue
            for layer in gp.layers:
                for frame in layer.frames:
                    if use_selected is True:
                        if frame.select is True:
                            keys.add(frame.frame_number)
                    else:
                        keys.add(frame.frame_number)

        return keys

    def key_selected_objects(self,context)->int:
        objects = context.selected_objects
        gps_obj = self.get_gp_objs(objects)

        keys = self.key_frames(gps_obj,use_selected=False)
        keys.discard(0)

        return keys

    def keys_selected_frames(self,context)->int:
        objects = context.scene.objects
        gps_obj = self.get_gp_objs(objects)

        return self.key_frames(gps_obj,use_selected=True)
    
    def keys_all(self,context)->int:
        objects = context.scene.objects
        gps_obj = self.get_gp_objs(objects)

        keys = self.key_frames(gps_obj,use_selected=False)
        keys.discard(0)

        return keys

    def execute(self,context):
        scene = context.scene
        output_path = scene.render.filepath
        if context.scene.use_nodes is False :
            context.scene.use_nodes = True
        
        compositor = context.scene.node_tree
        
        # Generate Nodes if Nodes not prepared
        generateNodes(compositor)

        # Set Nodes Properties Value
        support.setNodesProps(compositor,context)

        render_action = context.scene.anitools.output_setting.render_action

        if render_action == 'DEF':
            return {'CANCLED'}

        switch = {
            'OBJ' : self.key_selected_objects,
            'SEL' : self.keys_selected_frames,
            'ALL' : self.keys_all,
        }

        keys = switch.get(render_action)(context)

        frame_numbers = sorted(list(keys))
        print(frame_numbers)
        rendered_frames = []

        for frame_num in frame_numbers:
            path_frame = scene.render.frame_path(frame = frame_num)
            scene.frame_set(frame_num)
            scene.render.filepath = path_frame
            bpy.ops.render.render(write_still=True)
            scene.render.filepath = output_path
            rendered_frames.append(frame_num)

        if rendered_frames:
            folder = path.dirname(scene.render.frame_path(frame=0))
            info = "Rendered: {}".format(", ".join(map(str, rendered_frames)))
            self.report({'INFO'}, info)

        return {'FINISHED'}

    def modal(self, context, event):
        
        return

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
    # OUTPUT_OT_output_type,
)