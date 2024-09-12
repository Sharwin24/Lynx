#! /usr/bin/env python3

from cell import Cell
from maze import Maze
import os


class MazeInterpreter:
    """_summary_
    """
    def __init__(self):
        self.interpreted_maze = Maze()

    # Takes in an external file path and loads the maze from the .txt file.
    def interpret_external(self, filepath):
        """interpreter for an externally loaded maze

        Args:
            filepath (str): path to the maze txt file

        Returns:
            interpreted_maze: interpreted maze object with populated maze list
        """
        cell_index = 0

        with open(filepath) as file:
            rows = len(file.readlines())

        with open(filepath) as file:
            for line in file.readlines():
                print(line)
                cols = len(line) -1 
                for char in line:
                    match char:
                        case "%":
                            current_cell = Cell(cell_index, self.find_neighbors(cell_index, rows, cols), False)
                            self.interpreted_maze.start_index = cell_index
                        case "#":
                            current_cell = Cell(cell_index, self.find_neighbors(cell_index, rows, cols), False)
                        case "@":
                            current_cell = Cell(cell_index, self.find_neighbors(cell_index, rows, cols), True)
                        case "&":
                            current_cell = Cell(cell_index, self.find_neighbors(cell_index, rows, cols), False)
                            self.interpreted_maze.goal_index = cell_index
                    
                    cell_index += 1
                    self.interpreted_maze.maze_list.append(current_cell)
    
        return self.interpreted_maze    

    # Finds and returns a list of found neighbors to this cell index.
    def find_neighbors(self, index, rows, cols):
        """mathmatically finds neighboring cell indeces based on current cell location

        Args:
            index (ind): current cell index
            rows (ind): row size of maze
            cols (ind): col size of maze

        Returns:
            neighbors_list: populated list of neighboring indices 
        """
        neighbors_list = []
        end = rows * cols - 1
        loc_r = index // rows
        loc_c = index % cols
        up_ind = index - cols
        if up_ind >= 0:
            neighbors_list.append(up_ind)
        right_ind = index + 1
        if loc_c + 1 <= cols - 1:
            neighbors_list.append(right_ind)
        down_ind = index + cols 
        if down_ind <= end:
            neighbors_list.append(down_ind)
        left_ind = index - 1
        if loc_c -1 >= 0:
            neighbors_list.append(left_ind)

        return neighbors_list