import cocos
import pyglet
from cocos.director import director
from cocos.text import Label

from pyglet.window import key

from Controller.GameController import GameController
from Model.GameModel import GameModel
from Utils import Direction, Gamestate
from View import Renderer, DefaultRenderer
from View.DefaultRenderer import DefaultRenderer
from View.NullRenderer import NullRenderer


class Main(cocos.layer.Layer):
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    KEY_MOVE_UP = pyglet.window.key.W
    KEY_MOVE_DOWN = pyglet.window.key.S

    def __init__(self, fastmode: bool = False, net=None, gen=None):
        super(Main, self).__init__()

        # print("main init")

        self.model: GameModel = GameModel(fastmode, net)
        self.controller: GameController = GameController(self.model)
        if net is not None and fastmode:
            self.renderer: Renderer = NullRenderer(self.model)
        else:
            self.renderer: Renderer = DefaultRenderer(self.model)

        self.is_event_handler = True
        self.add(self.controller)
        self.add(self.renderer)

        cocos.director.director.set_show_FPS(True)
        self.schedule(self.update)

        self.label_gen = Label(text="Generation: " + str(gen), font_size=48)
        self.label_gen.position = (300, 200)
        self.add(self.label_gen)

        self.runtime = 0.0

    def update(self, delta):
        # print("main update")
        # if self.model.fastmode:
        #     delta = 0.16
        # self.delta = delta
        delta = 0.016
        self.runtime += delta
        if self.runtime > 61.0:
            self.controller.on_game_end()

        self.controller.update(delta)
        self.renderer.render(delta)


def get_score(net, fastmode=True, gen=None):
    # if not hasattr(cocos.director.director, "window"):
    if net is not None and fastmode:
        director.init(visible=False, width=Main.SCREEN_WIDTH, height=Main.SCREEN_HEIGHT, resizable=True, vsync=False)
    else:
        director.init(width=Main.SCREEN_WIDTH, height=Main.SCREEN_HEIGHT, resizable=True, vsync=True)
    main = Main(fastmode=fastmode, net=net, gen=gen)
    main_scene = cocos.scene.Scene(main)
    director.run(main_scene)
    director.window.close()
    return cocos.director.director.return_value


# score = get_score(net=None, fastmode=False)
# print("score: " + str(score))
