#! /usr/bin/env python3
from maze import Maze, MazeInfo
from cell import Cell

import random


class Generator:
    """Class that generates the the maze utilizing randomized prim's algorithm"""

    def generate_rectangular_maze(self, info: MazeInfo, num_cols: int, num_rows: int, start: tuple[int, int] = None) -> Maze:
        """ Generates a rectangular maze using inputs about the size of the maze and the start state

        Args:
            info (MazeInfo): The information about the maze including type and
            num_cols (int): The maze width in number of cells
            num_rows (int): The maze height in number of cells
            start tuple(int, int): The start cell expressed as a tuple of (row, column). Defaults to None which will be random

        Returns:
            Maze: A Maze object that is populated with the generated maze
        """
        maze_list: list[Cell] = []
        index = 0
        # Create a grid of wall cells with the correct size
        for r in range(num_rows):
            for c in range(num_cols):
                maze_list.append(Cell(index))
                index += 1
        '''
        This creates an index system based on the grid:
          _ _ _     0 1 2
          _ _ _  -> 3 4 5
          _ _ _     6 7 8
        To convert a (r,c) to an index: index = ((c + 1) * num_columns) + (r + 1)
        '''
        if start == None:  # Randomize start position if not already picked
            start = (random.randint(0, num_rows - 1),
                     random.randint(0, num_cols - 1))
        # Convert the (row, column) position to the index in maze_list
        start_index = ((start[1] + 1) * num_cols) + (start[0] + 1)

        '''
        Randomly choose a cell Q and mark it as free, let's pick our start index
        Add cell Q's neighbors to the wall list
        While the wall list is not empty:
          Randomly choose a wall W from wall list
          If wall W is adjacent to exactly one free cell
            Let F be the free cell that W is adjacent to
            W is to a direction DIR of F
            Let A be the cell to the direction DIR of W
            Make W free
            Make A Free
            Add the walls of A to the wall list
          Remove W from wall list
        '''
        generated_maze = Maze(info=MazeInfo(
            MazeInfo.MazeType.GridMaze,
            size=(num_rows, num_cols),
            maze_list=maze_list)
        )

        # Set start cell as free and create empty wall_list
        maze_list[start_index].set_free(True)
        wall_list: list[Cell] = []
        # Get neighbors of start cell and add to wall list
        for n in generated_maze.get_neighbors(cell=maze_list[start_index], maze_list=maze_list):
            wall_list.append(n)
        while not wall_list:
            random_wall = wall_list[random.randint(0, len(wall_list) - 1)]
            # If random_wall's neighbors has exactly one free cell
            random_wall_neighbors: list[Cell] = generated_maze.get_neighbors(
                cell=random_wall, maze_list=maze_list)
            if len(filter(lambda c: c.is_wall(), random_wall_neighbors)) == 1:
                # Find the neighhbor that is free
                free_neighbor = filter(
                    lambda c: c.is_wall(), random_wall_neighbors)
                free_neighbor.set_free()

        # Populate the Maze with the maze list
        generated_maze.populate_maze(
            maze_list=maze_list,
            start_index=start_index,
            goal_index=goal_index,
            robot_index=start_index  # Robot starts at starting cell
        )
        return generated_maze


g = Generator()
g.generate_rectangular_maze(4, 3, ())
