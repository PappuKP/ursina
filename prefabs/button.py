import sys
sys.path.append("..")
from pandaeditor import *

class Button(Entity):


    def __init__(self):
        super().__init__()
        self.name = 'button'
        self.parent = scene.ui
        self.model = 'quad'
        self.model.setBin("fixed", 0)
        self.model.setDepthTest(False)
        self.model.setDepthWrite(False)

        self.collision = True
        self.collider = 'box'
        self.button_script = self.add_script('button')
        self.button_script.color = color.gray
        self.text = ''
        self.text_entity = None
        # self.scale = (1 / camera.aspect_ratio,1,1)

    def __setattr__(self, name, value):
        if name == 'color':
            try:
                self.button_script.color = value
            except:
                pass

        if name == 'position':
            value = (value[0] / 2, (value[1] / 2), -.1)


        if name == 'text':

            if len(value) > 0:
                self.text_entity = load_prefab('text')
                # self.text_entity.parent = scene.render
                self.text_entity.is_editor = self.is_editor
                # self.text_entity.scale *= .5
                self.text_entity.scale = (.5 / camera.aspect_ratio, .5 , 1)
                # self.text_entity.scale_x /= camera.aspect_ratio
                self.text_entity.wrtReparentTo(self.model)
                # self.text_entity.parent = self.model
                self.text_entity.position = (0, 0, 0)
                self.text_entity.text = value
                # self.text_entity.parent = scene.render
                # self.text_entity.color = color.red


                # object.__setattr__(self, name, self.text_entity)

        else:
            super().__setattr__(name, value)