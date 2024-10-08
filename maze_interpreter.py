#! /usr/bin/env python3

""" interpreter for sample txt mazes

    sample usage:
    mi = MazeInterpreter()
    mi.interpret_external("sample_maze_1.txt")
    
    result:
    mi.interpreted_maze now contains an instance of Maze object

"""

from cell import Cell
from maze import Maze, MazeInfo


class MazeInterpreter:
    """
    Interpreter for txt based sample maze.

    """

    # Takes in an external file path and loads the maze from the .txt file.
    def interpret_external(self, filepath):
        """interpreter for an externally loaded maze

        Args:
            filepath (str): path to the maze txt file

        Returns:
            interpreted_maze: interpreted maze object with populated maze list
        """
        cell_index = 0
        cell_list = []

        with open(filepath) as file:
            rows = len(file.readlines())

        with open(filepath) as file:
            for line in file.readlines():
                # print(line)
                # Need to strip line return to make lines consistent
                ############################### Begin_Citation [1] ############################
                cols = len(line.strip("\n"))
                ############################### End_Citation [1]  #############################
                
                for char in line:
                    match char:
                        case "%":
                            current_cell = Cell(cell_index, self.find_neighbors(
                                cell_index, rows, cols), False)
                            start_index = cell_index
                        case "#":
                            current_cell = Cell(cell_index, self.find_neighbors(
                                cell_index, rows, cols), False)
                        case "@":
                            current_cell = Cell(cell_index, self.find_neighbors(
                                cell_index, rows, cols), True)
                        case "&":
                            current_cell = Cell(cell_index, self.find_neighbors(
                                cell_index, rows, cols), False)
                            goal_index = cell_index
                ############################### Begin_Citation [2] ############################
                        case _:
                            continue
                ############################### End_Citation [2]  #############################

                    cell_index += 1
                    cell_list.append(current_cell)

        sample_maze_info = MazeInfo(MazeInfo.MazeType.GridMaze, (rows, cols))
        interpreted_maze = Maze(sample_maze_info, cell_list, start_index, goal_index, start_index)

        print(f"The start index is : {start_index}")
        print(f"The goal index is: {goal_index}")
        print(f"This maze has {rows} rows, and {cols} cols.")

        return interpreted_maze

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
        if loc_c - 1 >= 0:
            neighbors_list.append(left_ind)

        return neighbors_list


if __name__ == "__main__":
    filepath = "sample_maze_3.txt"
    mi = MazeInterpreter()
    maze = mi.interpret_external(filepath)
    # print(maze.maze_list)
    test_ind = 26
    print(f"The neighbors of {test_ind} is {maze.maze_list[test_ind].get_neighbors()}")

    print(maze)


# [1]D. Creates, "Removing Trailing Newline in Python Strings | by Doug Creates | Medium", Medium, 2024. Available: https://medium.com/@Doug-Creates/removing-trailing-newline-in-python-strings-0bce6b94ed0c#:~:text=# To remove a trailing newline,removing characters from both ends. [Accessed 15 September. 2024].
# [2]"python - How to do an else (default) in match-case? - Stack Overflow", Stackoverflow, 2021. Available: https://stackoverflow.com/questions/68804209/how-to-do-an-else-default-in-match-case. [Accessed 12 September. 2024].