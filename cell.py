class Cell:

    def __init__(self, index: int = None):
        self.index = index
        self.neighbors = []
        self.is_wall = True

    def set_wall(self, is_wall: bool):
        self.is_wall = is_wall

    def set_free(self, is_free: bool):
        self.is_free = is_free

    def get_neighbors(self):
        return self.neighbors

    def get_wall(self):
        return self.is_wall

    def get_index(self):
        return self.index

    def __repr__(self) -> str:
        return f"{self.index}"
