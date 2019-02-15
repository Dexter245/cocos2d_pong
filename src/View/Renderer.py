from abc import ABC, abstractmethod

import cocos

from Model.GameModel import GameModel


class Renderer(cocos.layer.Layer):

    def __init__(self, model: GameModel):
        super(Renderer, self).__init__()
        self.model = model

    @abstractmethod
    def render(self, delta: float):
        pass
