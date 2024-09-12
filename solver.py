import cell
import maze

class Solver:
    algo = any
    path = []
    visited = []
    maz = Maze()

    def __init__(self, a : str, m : maze):
        self.algo = a
        self.maz = m
        self.visited.append(self.maz)

    def solve(self):
        if self.algo == 0:
            self.wavefront()
        elif self.algo == 1:
            self.dfs() 

    def wavefront(self, pos):
        start = pos

    def dfs(self, pos : cell):
        if pos.get_index() == maze.get_goal():
            self.path.append(pos.)
            return True
        else:
            for n in 