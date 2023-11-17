from src.strategies.base_classes.base_class import BaseStrategy

class MoveAll(BaseStrategy):
    def solve(self, maze):
        current_position = list(maze.start)
        # Row is 0 (UP AND DOWN)
        # Col is 1 (LEFT AND RIGHT)
        while current_position != list(maze.end):
            maze.maze[current_position[0]][current_position[1]] = "."
            open_directions = self._check_get_available_directions(maze.maze, current_position[0], current_position[1])
            # This is where we would store T insterections
            for direction in open_directions.items():
                current_position[0] += direction[1][0]
                current_position[1] += direction[1][1]
        return maze

    def _check_get_available_directions(self, maze, y, x):
        return_hash = {}
        all_directions = {
                            "up": [-1,0],
                            "left": [0,-1],
                            "right":[0 , 1],
                            "down": [1,0],
                        }
        for direction in all_directions.items():
            y_coord = direction[1][0]
            x_coord = direction[1][1]
            if maze[y + y_coord][x + x_coord] == " " or maze[y + y_coord][x + x_coord] == "E":
                return_hash[direction[0]] = [y_coord, x_coord]
        return return_hash