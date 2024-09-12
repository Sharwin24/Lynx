class Cell:
    index = 0
    neighbors = []
    is_wall = False

    def __init__(self, i, n, w):
        self.index = i
        self.neighbors = n
        self.is_wall = w

    def set_wall(self, w):
        self.is_wall = w

    def get_neighbors(self):
        return self.neighbors
    
    def get_wall(self):
        return self.is_wall
    
    def get_index(self):
        return self.index
    