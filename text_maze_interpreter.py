#! /usr/bin/env python3

from cell import Cell
from maze import Maze
import os


class MazeInterpreter:

    def __init__(self, name):
        self.name = name

    # Takes in an external file path and loads the maze from the .txt file.
    def interpret_external(self, filepath):
        
        interpreted_maze = Maze()

        with open(filepath) as file:
            for line in file.readlines():
                for char in line:
                    match char:
                        case "%":
                            
                        
