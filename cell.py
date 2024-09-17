class Cell:
    """ A class representing a cell within a maze. 
    Contains information about the cell such as it's position (index within maze_list), wall or free cell, and neighbor cells
    """

    def __init__(self, index: int, neighbors: list[int] = [], is_wall: bool = True):
        """ Creates a Cell with the given index. Defaults to a wall cell with empty neighbors

        Args:
            index (int): The position of the cell as an index within the maze_list. Defaults to None.
            neighbors (list[int]): The neighboring cells that can be reached from this cell by indices. Defaults to empty list
            is_wall (bool): Denotes if this cell is a wall or not. Defaults to wall
        """
        self.index = index
        self.neighbors = neighbors
        self.is_wall = is_wall
        self.is_free = not (is_wall)

    def set_wall(self):
        self.is_wall = True
        self.is_free = False

    def set_free(self):
        self.is_free = True
        self.is_wall = False

    def set_neighbors(self, neighbors: list[int]):
        self.neighbors = neighbors

    def get_neighbors(self):
        return self.neighbors

    def get_wall(self):
        return self.is_wall

    def get_index(self):
        return self.index

    def __repr__(self) -> str:
        return f"{self.index}"

    def __eq__(self, value: object) -> bool:
        # Equality is based on the cell's index within maze_list
        return self.index == value.index if isinstance(value, Cell) else False


class HexCell:
    """ A class representing a hexagonal cell within a maze. 
    Contains information about the cell such as it's position (index within maze_list), wall or free cell, and neighbor cells
    """

    def __init__(self, index: tuple, neighbors: list[tuple] = [], is_wall: bool = True):
        """ Creates a Cell with the given index. Defaults to a wall cell with empty neighbors

        Args:
            index (int): The position of the cell as an index within the maze_list. Defaults to None.
            neighbors (list[int]): The neighboring cells that can be reached from this cell by indices. Defaults to empty list
            is_wall (bool): Denotes if this cell is a wall or not. Defaults to wall
        """
        self.index = index
        self.neighbors = neighbors
        self.is_wall = is_wall
        self.is_free = not (is_wall)

    def set_wall(self):
        self.is_wall = True
        self.is_free = False

    def set_free(self):
        self.is_free = True
        self.is_wall = False

    def set_neighbors(self, neighbors: list[tuple]):
        self.neighbors = neighbors

    def get_neighbors(self):
        return self.neighbors

    def get_wall(self):
        return self.is_wall

    def get_index(self):
        return self.index

    def __repr__(self) -> str:
        return f"{self.index}"

    def __eq__(self, value: object) -> bool:
        # Equality is based on the cell's index within maze_list
        return self.index == value.index if isinstance(value, HexCell) else False