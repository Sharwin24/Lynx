from maze import Maze
import os
import time

class Ascii_Vizualizer:

    def __init__(self, maze:Maze, path:list):

        self.maze_string = repr(maze).strip("\n")
        self.path = path
        self.step_string = []
        self.step_col = []


    def populate(self):   
        for i in range(len(self.path)):
            step_string = self.maze_string[:self.path[i]] + "*" + self.maze_string[self.path[i]+1:]
            self.step_col.append(step_string)
        

    def ascii_play(step:list):
        for i in range(len(step)):
            os.system("clear")
            print(step[i])
            time.sleep(0.5)
