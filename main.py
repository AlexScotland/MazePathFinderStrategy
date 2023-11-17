from src.models.maze_solver import MazeSolver
from src.factories.maze_factory import MazeFactory
from src.strategies.move_all import MoveAll

if __name__ == "__main__":
    with open("maze.txt") as f:
        solved_maze = MazeSolver(MazeFactory.create_maze(f.read()), MoveAll()).solve()
        with open("solution.txt", "w") as writer:
            for row in solved_maze.maze:
                for value in row:
                    writer.write(value)
                writer.write("\n")