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
        rows = self.maze.info.size[0]
        cols = self.maze.info.size[1]
        mlist = self.maze.maze_list
        start = self.maze.start_index
        goal = self.maze.goal_index
        robot = self.maze.robot_index

        
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        top_left = pygame.Vector2(screen.get_width() / (cols*2), screen.get_height() / (rows*2))
        rect_height = (screen.get_height() / rows) - 10
        rect_width = (screen.get_width() / cols) - 10
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 32)
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

            clock.tick(60)

        pygame.quit()

maze_filepath = "sample_maze_2.txt"
interpreter = MazeInterpreter()
maze = interpreter.interpret_external(maze_filepath)
print(maze.info.size)


dfs_solver = Solver(Solver.SolverAlgorithm.DFS, maze)
dfs_solver.solve()
print(f"DFS Path: {dfs_solver.path}")
print(dfs_solver.path == [])
print(maze)

# wavefront_solver = Solver(Solver.SolverAlgorithm.Wavefront, maze)
# wavefront_solver.solve()
# print(f"Wavefront Path: {wavefront_solver.path}")
# print(wavefront_solver.path == [])
# print(maze)



vis1 = Visualizer(maze, dfs_solver.path)
vis1.display_maze()

# vis2 = Visualizer(maze, wavefront_solver.path)
# vis2.display_maze()