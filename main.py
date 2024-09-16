#! /usr/bin/env python3

"""
This is the main python file for team robotic-lynx's a-Maze-ing challenge submission.
"""

from enum import Enum
from generator import Generator
from maze import Maze, MazeInfo
from solver import Solver
from visualizer import *


def interactive_mode():
    print("Interactive mode selected")


def autogenerated_mode():
    print("Autogenerated mode selected")
    filepath = input("Please enter the file path here to load a maze: ")


class UserType(Enum):
    Interactive = 0
    Autogenerated = 1
    ########## Begin_Citation [2S] ##########

    @property
    def funcs(self):
        return {
            UserType.Interactive: interactive_mode,
            UserType.Autogenerated: autogenerated_mode
        }
    ########## End_Citation [2S] ##########

    def __repr__(self) -> str:
        return f"\"{self.name}\" ({self.value})"

    def run(self, *args, **kwargs):
        self.funcs[self]()


# If you want to skip inputs and determine parameters manually
BYPASS_USER_INPUT = True


if __name__ == "__main__" and not BYPASS_USER_INPUT:
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
    solver.solve()
    # Visualize the maze and the solved path
    print(
        f"Start {maze.start_index} Goal {maze.goal_index} Maze:\n{maze}\nPath: {solver.path}\n")
