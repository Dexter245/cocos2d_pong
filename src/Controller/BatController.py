from abc import ABC, abstractmethod


class BatController(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def update(self, delta: float):
        pass
