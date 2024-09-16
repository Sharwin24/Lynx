from cell import Cell
from maze import Maze
from solver import Solver
from maze_interpreter import MazeInterpreter
import pygame
import time
import os

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

class Visualizer:

    def __init__(self, maze, path):
        self.maze = maze
        self.path = path

    def display_maze(self):
        rows = self.maze.info.size[0]
        cols = self.maze.info.size[1]
        mlist = self.maze.maze_list
        start = self.maze.start_index
        goal = self.maze.goal_index
        robot = start

        
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        top_left = pygame.Vector2(screen.get_width() / (cols*2), screen.get_height() / (rows*2))
        rect_height = (screen.get_height() / rows) - 10
        rect_width = (screen.get_width() / cols) - 10
        font = pygame.font.Font(None, 24)
        running = True
        color = "white"
        path_index = 0
        filled_in = False

        screen.fill("black")
        for j in range(rows):
            for i in range(cols):
                if mlist[j*cols + i].is_wall:
                    color = "black"
                elif mlist[j*cols + i].is_free:
                    if (j*cols + i) == start:
                        color = "green"
                        start_text = font.render('Start', True, "black")
                        start_text_rect = start_text.get_rect()
                        start_text_rect.center = (top_left.x + i*screen.get_width()/cols, top_left.y + j*screen.get_height()/rows)
                    elif (j*cols + i) == goal:
                        color = "red"
                        goal_text = font.render('Goal', True, "black")
                        goal_text_rect = goal_text.get_rect()
                        goal_text_rect.center = (top_left.x + i*screen.get_width()/cols, top_left.y + j*screen.get_height()/rows)
                    else:
                        color = "white"

                pygame.draw.rect(screen, color, pygame.Rect((top_left.x + i*screen.get_width()/cols) - rect_width/2, (top_left.y + j*screen.get_height()/rows)
                                                                - rect_height/2, rect_width, rect_height))

        screen.blit(start_text, start_text_rect)
        screen.blit(goal_text, goal_text_rect)
        pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            
            if not filled_in:
                if not (self.path[path_index] == goal or self.path[path_index] == start):
                    pygame.draw.rect(screen, "cyan", pygame.Rect((top_left.x + (self.path[path_index]%cols)*screen.get_width()/cols) - rect_width/2,
                                                                (top_left.y + (self.path[path_index]//cols)*screen.get_height()/rows)- rect_height/2,
                                                                rect_width, rect_height))
                    pygame.display.flip()
                    path_index += 1
                    time.sleep(.2)
                elif self.path[path_index] == start:
                    path_index += 1
                else:
                    filled_in = True

        pygame.quit()

maze_filepath = "sample_maze_2.txt"
interpreter = MazeInterpreter()
maze = interpreter.interpret_external(maze_filepath)
print(maze.info.size)


# dfs_solver = Solver(Solver.SolverAlgorithm.DFS, maze)
# dfs_solver.solve()
# print(f"DFS Path: {dfs_solver.path}")
# print(dfs_solver.path == [])
# print(maze)

wavefront_solver = Solver(Solver.SolverAlgorithm.Wavefront, maze)
wavefront_solver.solve()
print(f"Wavefront Path: {wavefront_solver.path}")
print(wavefront_solver.path == [])
print(maze)



# vis1 = Visualizer(maze, dfs_solver.path)
# vis1.display_maze()

vis2 = Visualizer(maze, wavefront_solver.path)
vis2.display_maze()