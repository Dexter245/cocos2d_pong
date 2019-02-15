import cocos
import pyglet
from cocos.text import Label

from pyglet.window import key

from Controller.GameController import GameController
from Model.GameModel import GameModel
from Utils import Direction, Gamestate
from View import Renderer, DefaultRenderer
from View.DefaultRenderer import DefaultRenderer


class Main(cocos.layer.Layer):
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    KEY_MOVE_UP = pyglet.window.key.W
    KEY_MOVE_DOWN = pyglet.window.key.S

    def __init__(self, fastmode: bool = False, net=None):
        super(Main, self).__init__()

        self.model: GameModel = GameModel(fastmode)
        self.controller: GameController = GameController(self.model)
        self.renderer: Renderer = DefaultRenderer(self.model)

        self.is_event_handler = True
        self.add(self.controller)
        self.add(self.renderer)

        cocos.director.director.set_show_FPS(True)
        self.schedule(self.update)



    def update(self, delta):
        print()
        if self.model.fastmode:
            delta = 0.16
        self.delta = delta

        self.controller.update(delta)
        self.renderer.render(delta)






def get_score(net):
    if not hasattr(cocos.director.director, "window"):
        cocos.director.director.init(width=Main.SCREEN_WIDTH, height=Main.SCREEN_HEIGHT, resizable=True, vsync=False)
    main = Main()
    # main = Main(fastmode=True, net=net)
    main_scene = cocos.scene.Scene(main)
    cocos.director.director.run(main_scene)
    return cocos.director.director.return_value



score = get_score(net=None)
print("score: " + str(score))
