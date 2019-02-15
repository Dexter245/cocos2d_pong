from Model.GameModel import GameModel
from View.Renderer import Renderer


class NullRenderer(Renderer):

    def __init__(self, model: GameModel):
        super(NullRenderer, self).__init__(model)

    def render(self, delta: float):
        pass
