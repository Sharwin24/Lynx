#! /usr/bin/env python3
from maze import Maze, MazeInfo
from cell import Cell

import random


class Generator:
    """Class that generates the the maze utilizing randomized prim's algorithm"""

    def generate_rectangular_maze(self, info: MazeInfo, start: tuple[int, int] = None) -> Maze:
        """ Generates a rectangular maze using inputs about the size of the maze and the start state

        Args:
            info (MazeInfo): The information about the maze including type and size
            start tuple(int, int): The start cell expressed as a tuple of (row, column). Defaults to None which will be random

        Returns:
            Maze: A Maze object that is populated with the generated maze
        """
        maze_ls: list[Cell] = []
        maze_cell_index = 0
        num_rows = info.size[0]
        num_cols = info.size[1]
        # Create a grid of wall cells with the correct size
        for r in range(num_rows):
            for c in range(num_cols):
                maze_ls.append(Cell(maze_cell_index, is_wall=True))
                maze_cell_index += 1
        '''
        This creates an index system based on the grid:
          _ _ _     0 1 2
          _ _ _  -> 3 4 5
          _ _ _     6 7 8
        To convert a (r,c) to an index: index = (c * num_columns) + r
        '''
        if start == None:  # Randomize start position if not already picked
            start = (random.randint(0, num_rows - 1),
                     random.randint(0, num_cols - 1))
        # Convert the (row, column) position to the index in maze_list
        start_index = (start[1] * num_cols) + start[0]

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
            size=(num_rows, num_cols)),
            maze_list=maze_ls
        )
        print(f"Start Index {start_index} \nGenerated Maze {generated_maze}")
        # Set start cell as free and create empty wall_list
        generated_maze.set_cell_free(start_index)
        wall_list: list[Cell] = []
        # Get neighbors of start cell and add to wall list
        wall_list.extend(generated_maze.get_neighbors(
            cell=generated_maze.get_cell(start_index)))
        while wall_list:
            random_wall = random.choice(wall_list)  # Citation [1S]
            # If random_wall's neighbors has exactly one free cell
            random_wall_neighbors = generated_maze.get_neighbors(
                cell=random_wall)
            free_neighbors = [c for c in random_wall_neighbors if c.is_free]
            if len(free_neighbors) == 1:
                # Find the neighhbor that is free, (must be the only one in the list)
                free_neighbor = free_neighbors[0]
                opposite_cell = generated_maze.get_opposite_cell(
                    cell_W=random_wall, cell_F=free_neighbor)
                random_wall.set_free()
                if opposite_cell != None:
                    opposite_cell.set_free()
                # Add the walls of opposite_cell to wall_list
                new_walls = [c for c in generated_maze.get_neighbors(
                    cell=opposite_cell) if c.is_wall]
                wall_list.extend(new_walls)
            wall_list.remove(random_wall)
        # Pick a random goal index from the list of free cells
        free_cells = [c for cell in generated_maze.maze_list if cell.is_free]
        # goal_index = free_cells[random.randint(0, len(free_cells) - 1)]
        goal_index = random.choice(free_cells).get_index()
        print(f"Goal Index {goal_index}")
        # Populate the Maze with the maze list
        generated_maze.populate_maze(
            maze_list=maze_ls,
            start_index=start_index,
            goal_index=goal_index,
            robot_index=start_index  # Robot starts at starting cell
        )
        return generated_maze


if __name__ == '__main__':
    maze_creator = Generator()
    maze = maze_creator.generate_rectangular_maze(
        MazeInfo(MazeInfo.MazeType.GridMaze, (10, 10)),
        start=(0, 0)
    )

    # for i in range(len(maze.maze_list)):
    #     print(maze.maze_list[i].is_free)

    print(f"Maze:\n {maze}")
