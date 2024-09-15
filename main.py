#! /usr/bin/env python3

"""
This is the main python file for team robotic-lynx's a-Maze-ing challenge submission.
"""

from enum import Enum
from generator import Generator
from maze import Maze, MazeInfo
from solver import Solver
from visualizer import *

# select an existing text maze
# input maze type
# input maze size (mxn for reg, l for hex)

# select mode: interactive vs path generated


def interactive_mode():
    print("Interactive mode selected")


def autogenerated_mode():
    print("Autogenerated mode selected")
    filepath = input("Please enter the file path here to load a maze: ")


class UserType(Enum):
    Interactive = 0
    Autogenerated = 1

    @property  # Citation [2S]
    def funcs(self):
        return {
            UserType.Interactive: interactive_mode,
            UserType.Autogenerated: autogenerated_mode
        }

    def __repr__(self) -> str:
        return f"\"{self.name}\" ({self.value})"

    def run(self, *args, **kwargs):
        self.funcs[self]()


# If you want to skip inputs and determine parameters manually
BYPASS_USER_INPUT = True


if __name__ == "__main__" and not BYPASS_USER_INPUT:
    # Ask about the maze type and size
    # Ask about what mode they want to enter (interactive, autogenerated)
    type = input(
        f"Enter the input mode you would like as an string or integer matching the mode's name or value\n{[e for e in UserType]}: ")
    if type.isdigit():
        type = int(type)
        user_type = UserType(type)
        user_type.run()
    elif type in [e.name for e in UserType]:
        user_type = UserType[type]
        user_type.run()
    else:
        print("Invalid input. Please try again.")
        exit()
else:  # Bypass user input and run testing code
    # Generate a maze
    creator = Generator()
    maze = creator.generate_rectangular_maze(
        MazeInfo(MazeInfo.MazeType.GridMaze, size=(10, 10)))
    # Solve the maze and obtain the solution
    solver = Solver(Solver.SolverAlgorithm.Wavefront, maze)
    path = solver.solve()
    # Visualize the maze and the solved path
