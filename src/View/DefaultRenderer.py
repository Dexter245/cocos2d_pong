from cocos.text import Label

from Model.GameModel import GameModel
from Utils import Gamestate
from View.Renderer import Renderer


class DefaultRenderer(Renderer):

    def __init__(self, model: GameModel):
        from Main import Main
        super(DefaultRenderer, self).__init__(model)
        self.add(self.model.bat)
        self.add(self.model.ball)
        self.add(self.model.enemy)

        self.add(self.model.wall_left)
        self.add(self.model.wall_right)
        self.add(self.model.wall_top)
        self.add(self.model.wall_bottom)

        self.label_time = Label("Time: ", font_name="Arial", font_size=36, align="center")
        self.label_time.position = (Main.SCREEN_WIDTH / 2, Main.SCREEN_HEIGHT / 2)
        self.add(self.label_time)


    def render(self, delta: float):
        # print("render delta: " + str(delta))

        if self.model.gamestate == Gamestate.RUNNING:
            self.label_time.element.text = "%.1fs" % self.model.score
