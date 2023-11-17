
from src.models.maze import Maze
class MazeFactory():

    @staticmethod
    def create_maze(maze_string):
        maze_obj = []
        start, end = None, None
        for index, row  in enumerate(maze_string.split("\n")):
            maze_obj.append([])
            for sec_index, value in enumerate(row):
                if value == "S":
                    start = (index, sec_index)
                elif value == "E":
                    end = (index, sec_index)
                maze_obj[index].append(value)
        return Maze(maze_obj, start, end)