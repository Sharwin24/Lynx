from enum import Enum
from cell import Cell, HexCell


class MazeInfo:
    """ A Class containing the info for a maze. The type is one of the enums defined, and the size
        is dependent on the type
    """
    class MazeType(Enum):
        """ An enum for different maze types
        """
        GridMaze = 1
        HexMaze = 2

    def __init__(self, type: MazeType, size: any) -> None:
        """ Creates info about the maze using its type and size.
            The size must be formatted based on the type:
            1. GridMaze expects size to be a tuple(int,int) for (num_rows, num_columns)
            2. HexMaze expects size to be an int for the number of cells per side of the hexagon

        Args:
            type (MazeType): The type of maze from a physical perspective
            size (any): The size of the maze, with the value format constrained by the MazeType
        """
        self.type = type
        self.size = size


class Maze:
    """ A class representing the entire maze, containing the list of cell objects, the type of maze, and the start/goal cells
    """

    def __init__(self, info: MazeInfo, maze_list: list[Cell] = [], start_index: int = None, goal_index: int = None, robot_index: int = None) -> None:
        """ Creates a maze object with optional arguments to create an object with initialized values.
            Default behavior will create an empty maze which will need the fields to be populated by using the Generator.
            See generator.py for the logic behind populating these fields.
            The two options for generating a maze are:
            1. Generating the maze with generator and populating the Maze using the Maze.__init__() function with all the arguments
            2. Creating an empty maze using Maze.__init()__ without any arguments, then generating a maze with the generator and populating the maze using Maze.populate_maze()

        Args:
            info (MazeInfo): The information about this maze including its type and size.
            maze_list (list[Cell], optional): The maze represented as a list of Cell objects. Defaults to None.
            start_index (int, optional): The start cell represented as an index within the maze_list. Defaults to None.
            goal_index (int, optional): The goal cell represented as an index within the maze_list. Defaults to None.
            robot_index (int, optional): The cell the robot occupies as an index within the maze_list. Defaults to None.
        """
        self.info = info
        self.maze_list = maze_list
        self.start_index = start_index
        self.goal_index = goal_index
        self.robot_index = robot_index

    def populate_maze(self, maze_list: list[Cell], start_index: int, goal_index: int, robot_index: int) -> None:
        """ This method will populate the fields for this maze. This should be used if the Maze object was already constructed without the fields populated.

        Args:
            maze_list (list[Cell]): The maze represented as a list of Cell objects.
            start_index (int): The start cell represented as an index within the maze_list
            goal_index (int): The goal cell represented as an index within the maze_list
            robot_index (int): The cell the robot occupies as an index within the maze_list
        """
        self.maze_list = maze_list
        self.start_index = start_index
        self.goal_index = goal_index
        self.robot_index = robot_index

    def get_neighbors(self, cell: Cell) -> list[Cell]:
        """finds the neighboring cell indices to the given cell index

        Args:
            cell (Cell): index of the target cell

        Returns:
            neighbors_list([ind]): list of indices of found neighbors
        """
        neighbors_list = []

        maze_list = self.maze_list

        if self.info.type == MazeInfo.MazeType.GridMaze:

            index = cell.get_index()
            rows = self.info.size[0]
            cols = self.info.size[1]
            end_ind = rows * cols - 1

            loc_c = index % cols
            up_ind = index - cols
            if up_ind >= 0:
                neighbors_list.append(maze_list[up_ind])
            right_ind = index + 1
            if loc_c + 1 <= cols - 1:
                neighbors_list.append(maze_list[right_ind])
            down_ind = index + cols
            if down_ind <= end_ind:
                neighbors_list.append(maze_list[down_ind])
            left_ind = index - 1
            if loc_c - 1 >= 0:
                neighbors_list.append(maze_list[left_ind])

            return neighbors_list

        else:
            print("Unsupported maze type")

    def get_opposite_cell(self, cell_W: Cell, cell_F: Cell) -> Cell | None:
        """ Gets the cell in the direction opposite to F from W

            Example:
            _ _ _
            F w A
            _ _ _

            In this case, the opposite cell to F from W is A

        Args:
            cell_W (Cell): The wall cell to skip over in the opposing direction of F
            cell_F (Cell): The free cell that is adjacent to W, denoting the direction to skip over (opposite direction from W)

        Returns:
            Cell | None: A wall cell in the direction opposite to F from W,
            imagine going towards W from F but skipping over W to get the next cell.
            If the cell is out of bounds, returns None
        """
        num_rows = self.info.size[0]
        num_cols = self.info.size[1]
        free_row = cell_F.get_index() // num_cols
        free_col = cell_F.get_index() % num_cols
        wall_row = cell_W.get_index() // num_cols
        wall_col = cell_W.get_index() % num_cols

        if wall_row == free_row - 1:  # If the wall is above the free cell
            cell_A_row = free_row - 1
            cell_A_col = free_col
        elif wall_row == free_row + 1:  # If the wall is below the free cell
            cell_A_row = free_row + 1
            cell_A_col = free_col
        elif wall_col == free_col - 1:  # If the wall is left of the free cell
            cell_A_row = free_row
            cell_A_col = free_col - 1
        elif wall_col == free_col + 1:  # If the wall is right of the free cell
            cell_A_row = free_row
            cell_A_col = free_col + 1
        else:
            return None  # The row, col is out of bounds

        # Convert opposite cell's row and column to an index in the maze_list
        if cell_A_row < 0 or cell_A_row >= num_rows or cell_A_col < 0 or cell_A_col >= num_cols:
            return None  # The row, col is out of bounds
        else:
            return self.maze_list[(cell_A_row * self.info.size[1]) + cell_A_col]

    def get_cell(self, index: int) -> Cell:
        """ Returns the cell at the given index

        Args:
            index (int): The index of the cell to be returned

        Returns:
            Cell: The cell at the given index
        """
        return self.maze_list[index]

    def set_cell_free(self, index: int) -> None:
        """ Sets the cell at the given index to be free

        Args:
            index (int): The index of the cell to be set free
        """
        self.maze_list[index].set_free()

    def set_cell_wall(self, index: int) -> None:
        """ Sets the cell at the given index to be a wall

        Args:
            index (int): The index of the cell to be set as a wall
        """
        self.maze_list[index].set_wall()

    def __repr__(self) -> str:
        """ Returns the string representation of the maze

    #     Text representation for mazes:

    #     #: Free cell
    #     @: Wall cell
    #     %: Start cell
    #     &: Goal cell
    #     *: Current bot cell

    #     Example text representation:

    #     %*###@##
    #     @##@@@@&
    #     ##@@####
    #     ######@@

        Returns:
            str: The ASCII representation of the maze
        """

        rows = self.info.size[0]
        cols = self.info.size[1]
        char_ind = 0
        output_str = str("")

        start_ind = self.start_index
        goal_ind = self.goal_index
        # loop through maze_list for char representation
        for row in range(rows):
            for char in range(cols):
                current_cell = self.maze_list[char_ind]
                if current_cell.is_free:
                    if char_ind == start_ind:
                        output_str += "%"
                    elif char_ind == goal_ind:
                        output_str += "&"
                    else:
                        output_str += "#"
                elif current_cell.is_wall:
                    output_str += "@"
                char_ind += 1
            output_str += "\n"

        return output_str


class HexMaze:
    """ A class representing the entire maze, containing the list of cell objects, the type of maze, and the start/goal cells
    """

    def __init__(self, info: MazeInfo, maze_list: list[Cell] = [], start_index: tuple = None, goal_index: tuple = None, robot_index: tuple = None) -> None:
        """ Creates a maze object with optional arguments to create an object with initialized values.
            Default behavior will create an empty maze which will need the fields to be populated by using the Generator.
            See generator.py for the logic behind populating these fields.
            The two options for generating a maze are:
            1. Generating the maze with generator and populating the Maze using the Maze.__init__() function with all the arguments
            2. Creating an empty maze using Maze.__init()__ without any arguments, then generating a maze with the generator and populating the maze using Maze.populate_maze()

        Args:
            info (MazeInfo): The information about this maze including its type and size.
            maze_list (list[Cell], optional): The maze represented as a list of Cell objects. Defaults to None.
            start_index (tuple, optional): The start cell represented as an index within the maze_list. Defaults to None.
            goal_index (tuple, optional): The goal cell represented as an index within the maze_list. Defaults to None.
            robot_index (tuple, optional): The cell the robot occupies as an index within the maze_list. Defaults to None.
        """
        self.info = info
        self.maze_list = maze_list
        self.start_index = start_index
        self.goal_index = goal_index
        self.robot_index = robot_index

    def populate_maze(self, maze_list: list[Cell], start_index: tuple, goal_index: tuple, robot_index: tuple) -> None:
        """ This method will populate the fields for this maze. This should be used if the Maze object was already constructed without the fields populated.

        Args:
            maze_list (list[Cell]): The maze represented as a list of Cell objects.
            start_index (int): The start cell represented as an index within the maze_list
            goal_index (int): The goal cell represented as an index within the maze_list
            robot_index (int): The cell the robot occupies as an index within the maze_list
        """
        self.maze_list = maze_list
        self.start_index = start_index
        self.goal_index = goal_index
        self.robot_index = robot_index

    def get_neighbors(self, cell: Cell) -> list[Cell]:
        """finds the neighboring cell indices to the given cell index

        Args:
            cell (Cell): index of the target cell

        Returns:
            neighbors_list([ind]): list of indices of found neighbors
        """
        neighbors_list = []

        maze_list = self.maze_list

        if self.info.type == MazeInfo.MazeType.HexMaze:

            index = cell.get_index()
            q = index[0]
            r = index[1]
            s = -q - r

            return neighbors_list

        else:
            print("Unsupported maze type")

    def get_opposite_cell(self, cell_W: HexCell, cell_F: HexCell) -> HexCell | None:
        """ Gets the cell in the direction opposite to F from W

            Example:
            _ _ _
            F w A
            _ _ _

            In this case, the opposite cell to F from W is A

        Args:
            cell_W (Cell): The wall cell to skip over in the opposing direction of F
            cell_F (Cell): The free cell that is adjacent to W, denoting the direction to skip over (opposite direction from W)

        Returns:
            Cell | None: A wall cell in the direction opposite to F from W,
            imagine going towards W from F but skipping over W to get the next cell.
            If the cell is out of bounds, returns None
        """
        new_index = ((cell_W.get_index()[0] - cell_F.get_index()[0]) + cell_W.get_index()[0],
                     (cell_W.get_index()[1] - cell_F.get_index()[1]) + cell_W.get_index()[1])
        return self.maze_list[new_index]

    def get_cell(self, index: int) -> Cell:
        """ Returns the cell at the given index

        Args:
            index (int): The index of the cell to be returned

        Returns:
            Cell: The cell at the given index
        """
        return self.maze_list[index]

    def set_cell_free(self, index: int) -> None:
        """ Sets the cell at the given index to be free

        Args:
            index (int): The index of the cell to be set free
        """
        self.maze_list[index].set_free()

    def set_cell_wall(self, index: int) -> None:
        """ Sets the cell at the given index to be a wall

        Args:
            index (int): The index of the cell to be set as a wall
        """
        self.maze_list[index].set_wall()
