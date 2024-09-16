from cell import Cell
from maze import Maze, MazeInfo
from collections import deque
from maze_interpreter import MazeInterpreter
from enum import Enum

import numpy as np


class Solver:
    class SolverAlgorithm(Enum):
        Wavefront = 0
        DFS = 1
        RecursiveBackTracking = 2
        BeliefStatePlanner = 3

    def __init__(self, algo: SolverAlgorithm, m: Maze):
        self.algo = algo
        self.maze = m
        self.path = []
        self.visited = []

    # Chooses which solving algorithm to use
    def solve(self):
        if self.algo == self.SolverAlgorithm.Wavefront:
            self.wavefront()
        elif self.algo == self.SolverAlgorithm.DFS:
            self.dfs(self.maze.maze_list[self.maze.start_index])

    # Wavefront algorithm
    def wavefront(self):
        weight = [0] * len(self.maze.maze_list)
        goal = self.maze.maze_list[self.maze.goal_index]
        weight[goal.get_index()] = 2
        # print(self.visited)
        # Assign walls
        for c in self.maze.maze_list:
            if c.get_wall():
                weight[c.get_index()] = 1

        w_vis = np.array(weight).reshape(self.maze.info.size)
        print(f"Planner:\n {w_vis}")

        q = deque()
        q.append(goal)
        self.visited.append(goal.get_index())
        while q:
            front = q.popleft()
            # print(front.get_index())
            for n in front.get_neighbors():
                if not (n in self.visited) and not self.maze.maze_list[n].get_wall():
                    weight[n] = weight[front.get_index()] + 1
                    self.visited.append(n)
                    q.append(self.maze.maze_list[n])
            w_vis = np.array(weight).reshape(self.maze.info.size)
            # print(f"Planner:\n {w_vis}")

        pos = self.maze.start_index
        self.path.append(pos)
        while pos != goal.get_index():
            cur_weight = weight[pos]
            next_move = -1
            for n in self.maze.maze_list[pos].get_neighbors():
                if weight[n] > 1 and weight[n] < cur_weight:
                    cur_weight = weight[n]
                    next_move = n
            self.path.append(next_move)
            pos = self.maze.maze_list[next_move].get_index()

    def dfs(self, pos: Cell):
        self.visited.append(pos.get_index())
        self.path.append(pos.get_index())
        if pos.get_index() == self.maze.goal_index:
            return True
        elif pos.get_wall():
            self.path.pop()
            return False
        else:
            for n in pos.get_neighbors():
                if n not in self.visited:
                    if self.dfs(self.maze.maze_list[n]):
                        return True
            self.path.pop()
            return False


def main():

    filepath = "sample_maze_3.txt"
    mi = MazeInterpreter()
    loaded_maze = mi.interpret_external(filepath)
    print(loaded_maze)

    s = Solver(1, loaded_maze)
    s.solve()
    print(f"DFS Path: {s.path}")

    w = Solver(0, loaded_maze)
    w.solve()
    print(f"BFS Path: {w.path}")


if __name__ == "__main__":
    main()
