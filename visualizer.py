class Visualizer:

    def __init__(self, maze, path):
        self.maze = maze
        self.path = path

    def set_maze(self, maze):
        self.maze = maze

    def get_maze(self):
        return self.maze
    
    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path
    
    