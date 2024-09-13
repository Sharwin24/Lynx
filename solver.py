from cell import Cell
from maze import Maze, MazeInfo
from collections import deque
from maze_interpreter import MazeInterpreter


class Solver:

    def __init__(self, a: str, m: Maze):
        self.algo = a
        self.maze = m
        self.path = []
        self.visited = []

    def solve(self):
        if self.algo == 0:
            self.wavefront(self.maze)
        elif self.algo == 1:
            self.dfs(self.maze.maze_list[self.maze.start_index])

    def wavefront(self, m):
        weight = [0] * len(self.maze.maze_list)
        goal = self.maze.maze_list[self.maze.goal_index]
        print(goal.get_index())
        weight[goal.get_index()] = 2

        q = deque()

        q.append(goal)
        self.visited.append(goal.get_index())
        while q:
            front = q.popleft()
            for n in front.get_neighbors():
                if n not in self.visited:
                    if self.maze.maze_list[n].get_wall():
                        weight[n] = 1
                    else:
                        weight[n] = weight[front.get_index()] + 1
                    q.append(self.maze.maze_list[n])
            self.visited.append(front.get_index())

        pos = self.maze.maze_list[self.maze.start_index]
        self.path.append(pos.get_index())
        while pos.get_index() != goal.get_index():
            print("Second")
            cur_weight = weight[pos.get_index()]
            next_move = -1
            for n in pos.get_neighbors():
                if weight[n] > 1 and weight[n] < cur_weight:
                    cur_weight = weight[n]
                    next_move = n
            self.path.append(next_move)
            pos = self.maze.maze_list[next_move]

    def dfs(self, pos: Cell):
        self.visited.append(pos.get_index())
        self.path.append(pos.get_index())
        if pos.get_index() == self.maze.goal_index:
            return True
        elif pos.get_wall():
            return False
        else:
            for n in pos.get_neighbors():
                if n not in self.visited:
                    if self.dfs(self.maze.maze_list[n]):
                        return True
            self.path.pop()
            return False


def main():

    filepath = "sample_maze_1.txt"
    mi = MazeInterpreter()
    loaded_maze = mi.interpret_external(filepath)

    # maze_list = []
    # maze_list.append(Cell(0, [1], False))
    # maze_list.append(Cell(1, [0, 2, 3], False))
    # maze_list.append(Cell(2, [1], False))
    # maze_list.append(Cell(3, [1, 4], False))
    # maze_list.append(Cell(4, [5, 9, 3], False))
    # maze_list.append(Cell(5, [4, 6, 8], False))
    # maze_list.append(Cell(6, [5, 7], False))
    # maze_list.append(Cell(7, [6, 8], False))
    # maze_list.append(Cell(8, [5, 7], False))
    # maze_list.append(Cell(9, [4, 10], False))
    # maze_list.append(Cell(10, [9], False))
    # m = Maze(info=MazeInfo(type=MazeInfo.MazeType.GridMaze, size=(4, 4)),
    #          maze_list=maze_list,
    #          start_index=0,
    #          goal_index=10,
    #          robot_index=0
    #          )

    s = Solver(1, loaded_maze)
    s.solve()
    print(f"DFS Path: {s.path}")

    w = Solver(0, loaded_maze)
    w.solve()
    print(f"BFS Path: {w.path}")


if __name__ == "__main__":
    main()
