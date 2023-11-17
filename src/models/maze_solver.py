from dataclasses import dataclass
from src.models.maze import Maze
from src.strategies.base_classes.base_class import BaseStrategy

@dataclass
class MazeSolver:
    """
    Class that solves mazes by using given strategies
    """
    maze: Maze
    strategy: BaseStrategy

    def solve(self):
        return self.strategy.solve(self.maze)