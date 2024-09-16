from cell import Cell
from maze import Maze, MazeInfo
from collections import deque
from maze_interpreter import MazeInterpreter
from enum import Enum
from visualizer import Ascii_Vizualizer

import numpy as np

class Solver:
    class SolverAlgorithm(Enum):
        Wavefront = 0
        DFS = 1
        RecursiveBackTracking = 2
        BeliefStatePlanner = 3
    
    class Node:
        def __init__(self, state, index):
            self.state = state
            self.index = index
            self.chil = []
        
        def get_state(self):
            return self.state
        
        def get_index(self):
            return self.index
        
        def set_child(self, node):
            self.chil.append[node]
    

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
        # print(f"Planner:\n {w_vis}")

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

    def belief_state(self, m: Maze):
        s = deque()
        graph = []
        curr = self.Node(0, m.robot_index)
        s.append(curr)

        while s:
            curr = s.pop()
            m.set_robot_index(curr.get_index())
            if curr.get_index() == m.goal_index:
                return
            for n in m.maze_list[curr.i].get_neighbors():
                child = None
                if not n.get_wall():
                    child = self.Node(0, n)
                    s.append(child)
                else:
                    child = self.Node(1, n)
                curr.set_child(child)


                    


        
def main():

    filepath = "sample_maze_2.txt"
    mi = MazeInterpreter()
    loaded_maze = mi.interpret_external(filepath)
    print(loaded_maze)

    s = Solver(Solver.SolverAlgorithm.DFS, loaded_maze)
    s.solve()
    print(f"DFS Path: {s.path}")

    w = Solver(Solver.SolverAlgorithm.Wavefront, loaded_maze)
    w.solve()
    print(f"BFS Path: {w.path}")

    b = Solver(Solver.SolverAlgorithm.BeliefStatePlanner, loaded_maze)
    b.solve()
    print(f"BS Path: {b.path}")


if __name__ == "__main__":
    main()
