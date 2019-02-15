from abc import ABC, abstractmethod


class BatController(ABC):

    def __init__(self):
        super(BatController, self).__init__()
        self.action_up = False
        self.action_down = False

    @abstractmethod
    def update(self, delta: float):
        pass
