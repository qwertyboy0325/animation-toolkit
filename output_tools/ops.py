from os import name, path
import bpy
from bpy.props import BoolProperty
from . import support
from .support import KeyFrameHelper
from .props import AniOutputProps
from ..utils import nodes
import math

class OUTPUT_OT_output(bpy.types.Operator):
    bl_idname = "anitools.output"
    bl_label = "Render"

    _timer = None
    frame_nums = set()
    cur_frame_idx = 0
    lst_frame_idx = 0
    stop = None
    rendering = None
    rendered_frames = []

    def pre(self, scene,context = None):
        self.rendering = True

    def post(self, scene,context = None):
        self.rendering = False
        self.cur_frame_idx += 1
        frame_num = self.frame_nums[self.cur_frame_idx]
        self.rendered_frames.append(frame_num)
        print(self.cur_frame_idx)

    def cancelled(self,scene,context = None):
        self.stop = True

    def add_handlers(self,context):
        bpy.app.handlers.render_pre.append(self.pre)
        bpy.app.handlers.render_post.append(self.post)
        bpy.app.handlers.render_cancel.append(self.cancelled)

        self._timer = context.window_manager.event_timer_add(0.1, window=context.window)
        context.window_manager.modal_handler_add(self)

    def remove_handlers(self,context):
        bpy.app.handlers.render_pre.remove(self.pre)
        bpy.app.handlers.render_post.remove(self.post)
        bpy.app.handlers.render_cancel.remove(self.cancelled)

        context.window_manager.event_timer_remove(self._timer)

    @classmethod
    def poll(cls,context):
        render_action = context.scene.anitools.output_setting.render_action
        if render_action == 'OBJ':
            return KeyFrameHelper.objs_selected(context) is True
        # elif render_action == 'SEL':
        #     return KeyFrameHelper.keys_selected(context) is True
        elif render_action == 'ALL':
            return KeyFrameHelper.keys_all(context) != set()
        return True


    def execute(self,context):
        self.stop = False
        self.rendering = False
        self.add_handlers(context)

        scene = context.scene
        if scene.use_nodes is False :
            scene.use_nodes = True
        
        compositor = scene.node_tree
        
        # Generate Nodes if Nodes not prepared
        generateNodes(compositor)

        # Set Nodes Properties Value
        support.setNodesProps(compositor,context)

        render_action = scene.anitools.output_setting.render_action

        switch = {
            'OBJ' : KeyFrameHelper.key_selected_objects,
            'SEL' : KeyFrameHelper.keys_selected_frames,
            'ALL' : KeyFrameHelper.keys_all,
        }

        keys = switch.get(render_action)(context)
        self.frame_nums = sorted(list(keys))
        self.lst_frame_idx = len(self.frame_nums) -1

        bpy.ops.render.view_show('INVOKE_DEFAULT')

        return {"RUNNING_MODAL"}

    def modal(self, context, event):
        if event.type == 'ESC':
            self.remove_handlers(context)
            return {"CANCELLED"}

        if event.type == 'TIMER':
            if self.stop:
                self.remove_handlers(context)
                return {"CANCELLED"}

            if self.cur_frame_idx > self.lst_frame_idx:
                self.remove_handlers(context)
                if self.rendered_frames:
                    info = "Rendered: {}".format(", ".join(map(str, self.rendered_frames)))
                    self.report({'INFO'}, info)
                    return {"FINISHED"}

            if self.rendering is False:
                scene = context.scene
                output_path = scene.render.filepath
                frame_num = self.frame_nums[self.cur_frame_idx]
                path_frame = scene.render.frame_path(frame = frame_num)
                print(path_frame)
                scene.frame_set(frame_num)
                scene.render.filepath = path_frame
                bpy.ops.render.render(write_still=True)
                scene.render.filepath = output_path

        return {"PASS_THROUGH"}

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