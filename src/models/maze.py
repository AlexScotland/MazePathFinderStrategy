class Maze():
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
    
    def print_maze(self):
        for row_char in self.maze:
            print(row_char)