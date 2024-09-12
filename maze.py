from enum import Enum
from cell import Cell


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

    def get_neighbors(self, maze_list: list[Cell], cell: Cell):
        pass

    def __repr__(self) -> str:
        """ Returns the string representation of the maze

        Text representation for mazes:

        #: Free cell
        @: Wall cell
        %: Start cell
        &: Goal cell
        *: Current bot cell

        Example text representation:

        %*###@##
        @##@@@@&
        ##@@####
        ######@@

        Returns:
            str: The ASCII representation of the maze
        """
        pass
