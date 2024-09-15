from cell import Cell
from maze import Maze
from solver import Solver
from maze_interpreter import MazeInterpreter
import pygame

class Visualizer:

    def __init__(self, maze, path):
        self.maze = maze
        self.path = path

    def display_maze(self):
        rows = maze.info.size[0]
        cols = maze.info.size[1]
        mlist = maze.maze_list
        start = maze.start_index
        goal = maze.goal_index
        robot = maze.robot_index

        
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        top_left = pygame.Vector2(screen.get_width() / (cols*2), screen.get_height() / (rows*2))
        rect_height = (screen.get_height() / rows) - 10
        rect_width = (screen.get_width() / cols) - 10
        clock = pygame.time.Clock()
        running = True
        color = "white"


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("black")
            for j in range(rows):
                for i in range(cols):
                    if mlist[j*cols + i].is_wall:
                        color = "black"
                    elif mlist[j*cols + i].is_free:
                        if (j*cols + i) == start:
                            color = "green"
                        elif (j*cols + i) == goal:
                            color = "red"
                        else:
                            color = "white"

                    pygame.draw.rect(screen, color, pygame.Rect((top_left.x + i*screen.get_width()/cols) - rect_width/2, (top_left.y + j*screen.get_height()/rows)
                                                                   - rect_height/2, rect_width, rect_height))


            pygame.display.flip()

            clock.tick(60)

        pygame.quit()

maze_filepath = "sample_maze_2.txt"
interpreter = MazeInterpreter()
maze = interpreter.interpret_external(maze_filepath)
print(maze.info.size)
dfs_solver = Solver(1, maze)
dfs_solver.solve()
# print(f"DFS Path: {dfs_solver.path}")
# print(maze)

vis = Visualizer(maze, dfs_solver.path)
vis.display_maze()