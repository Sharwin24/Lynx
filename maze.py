from enum import Enum
from cell import Cell


class MazeType(Enum):
    """ An enum for different maze types
    """
    GridMaze = 1
    HexMaze = 2


class Maze():
    """ A class representing the entire maze, containing the list of cell objects, the type of maze, and the start/goal cells
    """

    def __init__(self, maze_list: list[Cell] = [], maze_type: MazeType = MazeType.GridMaze, start_index: int = None, goal_index: int = None, robot_index: int = None) -> None:
        """ Creates a maze object with optional arguments to create an object with initialized values.
            Default behavior will create an empty maze which will need the fields to be populated by using the Generator.
            See generator.py for the logic behind populating these fields.

        Args:
            maze_list (list[Cell], optional): The maze represented as a list of Cell objects. Defaults to None.
            maze_type (MazeType, optional): The type of maze, which will impact the utility of the object. Defaults to MazeType.GridMaze.
            start_index (int, optional): The start cell represented as an index within the maze_list. Defaults to None.
            goal_index (int, optional): The goal cell represented as an index within the maze_list. Defaults to None.
            robot_index (int, optional): The cell the robot occupies as an index within the maze_list. Defaults to None.
        """
        self.maze_list = maze_list
        self.maze_type = maze_type
        self.start_index = start_index
        self.goal_index = goal_index
        self.robot_index = robot_index

    def populate_maze(self, maze_list: list[Cell], maze_type: MazeType, start_index: int, goal_index: int, robot_index: int) -> None:
        """ This method will populate the fields

        Args:
            maze_list (list[Cell]): _description_
            maze_type (MazeType): _description_
            start_index (int): _description_
            goal_index (int): _description_
            robot_index (int): _description_
        """
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
