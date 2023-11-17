from abc import ABC, abstractmethod

class BaseStrategy(ABC):

    @abstractmethod
    def solve(self, maze: list):
        pass
