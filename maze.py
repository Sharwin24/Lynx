from enum import Enum

class MazeType(Enum):
  GridMaze = 1
  HexMaze = 2

class Maze():
  def __init__(self, maze_list: list[Cell] = None) -> None:
    self.maze_list = []
    self.maze_type = 
