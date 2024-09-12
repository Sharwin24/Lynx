from maze import Maze

class Generator():
  """Class that generates the the maze utilizing randomized prim's algorithm"""

  def __init__(self) -> None:
    pass

  def generate_rectangular_maze(self, width: int, height: int, start: tuple[int, int] = None, goal: tuple[int, int] = None) -> Maze:
    """ Generates a rectangular maze using inputs about the size of the maze and the start and goal state

    Args:
        width (int): The maze width in number of cells
        height (int): The maze height in number of cells
        start tuple(int, int): The start cell expressed as a tuple of (row, column). Defaults to None
        goal tuple(int, int): The goal cell expressed as a tuple of (row, column). Defaults to None

    Returns:
        Maze: _description_
    """
    maze = [] # Maze will be a list of Cell objects that then get put into Maze

