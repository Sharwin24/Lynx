from cell import Cell
from maze import *
from collections import deque

class Solver:
    algo = any
    maze = Maze()

    def __init__(self, a : str, m : Maze):
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

        q = []

        q.append(goal)
        self.visited.append(goal.get_index())
        while q:
            front = q.pop(0)
            print(front.get_index())
            for n in front.get_neighbors():
                if n not in self.visited:
                    weight[n] = weight[front.get_index()] + 1
                    q.append(self.maze.maze_list[n])
                    self.visited.append(front.get_index())

        pos = self.maze.maze_list[self.maze.start_index]
        print(weight)

        while pos.get_index() != goal.get_index():
            cur_weight = weight[pos.get_index()]
            next_move = -1
            for n in pos.get_neighbors():
                if weight[n] < cur_weight:
                    cur_weight = weight[n]
                    next_move = n
            self.path.append(next_move)
            pos = self.maze.maze_list[next_move]

    def dfs(self, pos : Cell):
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
    m = Maze([], MazeType.GridMaze, 0, 10, 0)
    m.maze_list.append(Cell(0, [1], False))
    m.maze_list.append(Cell(1, [0, 2, 3], False))
    m.maze_list.append(Cell(2, [1], False))
    m.maze_list.append(Cell(3, [1, 4], False))
    m.maze_list.append(Cell(4, [5, 9, 3], False))
    m.maze_list.append(Cell(5, [4, 6, 8], False))
    m.maze_list.append(Cell(6, [5, 7], False))
    m.maze_list.append(Cell(7, [6, 8], False))
    m.maze_list.append(Cell(8, [5, 7], False))
    m.maze_list.append(Cell(9, [4, 10], False))
    m.maze_list.append(Cell(10, [9], False))

    s = Solver(1, m)
    s.solve()
    print(s.path)

    w = Solver(0, m)
    w.solve()
    print(w.path)


if __name__=="__main__":
    main()  