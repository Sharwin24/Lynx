#! /usr/bin/env python3

"""
This is the main python file for team robotic-lynx's a-Maze-ing challenge submission.
"""

from enum import Enum
from generator import Generator
from maze import Maze, MazeInfo
from solver import Solver
from visualizer import Visualizer
from maze_interpreter import MazeInterpreter


def interactive_mode():
    print("Interactive mode selected")
    maze_type = input(
        f"Enter the type of Maze as an integer matching the mode's value\n{[e for e in MazeInfo.MazeType]}:")
    if maze_type.isdigit() and int(maze_type) in [e.value for e in MazeInfo.MazeType]:
        if int(maze_type) == MazeInfo.MazeType.GridMaze.value:
            maze_size = input(
                f"Creating Grid Maze! Please enter the size as a tuple of (num_rows, num_cols): ")
            maze_size = maze_size.replace("(", "")
            maze_size = maze_size.replace(")", "")
            ############## Begin_Citation [3S] ##############
            size = tuple(map(int, maze_size.split(',')))
            ############## End_Citation [3S] ##############
            print(f"Building Grid maze with size {size}")
            maze_start = input(
                f"Please enter the start position as a tuple of row, col\nAlternatively, leave blank for a random start position ")
            start = None
            if maze_start != "":
                start = tuple(map(int, maze_start.split(',')))
            print(f"Using Start {start if start != None else "Random"}")
            creator = Generator()
            grid_maze = creator.generate_rectangular_maze(
                MazeInfo(MazeInfo.MazeType.GridMaze, size), start)
            algo = input(
                f"Which algorithm would you like to visualize? Enter as an integer matching the mode's value\n{
                    [e for e in Solver.SolverAlgorithm]}:"
            )
            if algo.isdigit() and int(algo) in [e.value for e in Solver.SolverAlgorithm]:
                if int(algo) == Solver.SolverAlgorithm.Wavefront.value:
                    wavefront_solver = Solver(
                        Solver.SolverAlgorithm.Wavefront, grid_maze)
                    wavefront_solver.solve()
                    print(f"Wavefront Solver's Path: {wavefront_solver.path}")
                    viz = Visualizer(grid_maze, wavefront_solver.path)
                    viz.display_maze()
                elif int(algo) == Solver.SolverAlgorithm.DFS.value:
                    dfs_solver = Solver(Solver.SolverAlgorithm.DFS, grid_maze)
                    dfs_solver.solve()
                    print(f"DFS Solver's Path: {dfs_solver.path}")
                    viz = Visualizer(grid_maze, dfs_solver.path)
                    viz.display_maze()
            else:
                print(f"Invalid Algorithm input given")
            print(f"Maze:\n{grid_maze}")
        elif int(maze_type) == MazeInfo.MazeType.HexMaze.value:
            maze_size = input(
                f"Creating Hex Maze! Please enter the size as an int representing the radius in hexagons: ")
            if maze_size.isdigit():
                maze_size = int(maze_size)
                if maze_size < 0:
                    print("Size cannot be negative!")
                    return
                print(f"Building Hex maze with size {maze_size}")
            else:
                print("Invalid size given")
                return
            maze_start = input(
                f"Please enter the start position as a tuple index (Axial coordinates)\nAlternatively, leave blank for a random start position ")
            start = None
            if maze_start != "":
                maze_start = maze_start.replace("(", "")
                maze_start = maze_start.replace(")", "")
                start = tuple(map(int, maze_start.split(',')))
            creator = Generator()
            hex_maze = creator.generate_hexagonal_maze(
                MazeInfo(MazeInfo.MazeType.HexMaze, maze_size), start)
            wavefront_solver = Solver(
                Solver.SolverAlgorithm.Wavefront, hex_maze)
            dfs_solver = Solver(Solver.SolverAlgorithm.DFS, hex_maze)
            wavefront_solver.solve()
            dfs_solver.solve()
            print(f"Hex Maze:\n{hex_maze}")
            print(f"Wavefront Solver's Path: {wavefront_solver.path}")
            print(f"DFS Solver's Path: {dfs_solver.path}")
            viz = Visualizer(hex_maze, wavefront_solver.path)
            viz.display_maze()
    else:
        print("Invalid maze type selected")


def filegenerated_mode():
    print("File Generated mode selected")
    filepath = input("Please enter the file path here to load a maze: ")
    mi = MazeInterpreter()
    loaded_maze = mi.interpret_external(filepath)
    wavefront_solver = Solver(Solver.SolverAlgorithm.Wavefront, loaded_maze)
    dfs_solver = Solver(Solver.SolverAlgorithm.DFS, loaded_maze)
    wavefront_solver.solve()
    dfs_solver.solve()
    print(f"Maze:\n{loaded_maze}")
    print(f"Wavefront Solver's Path: {wavefront_solver.path}")
    print(f"DFS Solver's Path: {dfs_solver.path}")
    viz = Visualizer(loaded_maze, wavefront_solver.path)
    viz.display_maze()


class UserType(Enum):
    Interactive = 0
    Filegenerated = 1
    ########## Begin_Citation [2S] ##########

    @ property
    def funcs(self):
        return {
            UserType.Interactive: interactive_mode,
            UserType.Filegenerated: filegenerated_mode
        }
    ########## End_Citation [2S] ##########

    def __repr__(self) -> str:
        return f"\"{self.name}\" ({self.value})"

    def run(self, *args, **kwargs):
        self.funcs[self]()


# If you want to skip inputs and determine parameters manually
BYPASS_USER_INPUT = False


if __name__ == "__main__" and not BYPASS_USER_INPUT:
    type = input(
        f"Enter the input mode you would like as a string or integer matching the mode's name or value\n{[e for e in UserType]}: ")
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
