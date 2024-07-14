import pygame
import numpy as np
import copy
from random import randint, shuffle
from utilities import UnionFind


class RandomizedKruskal:
    box_boarder_color = (24, 27, 30)

    def __init__(self, maze, box):
        self.maze = copy.deepcopy(maze)
        self.box = box
        self.edges = []

        self.colors = np.empty(self.maze.shape, dtype=object)
        self.union_find_sets = UnionFind(maze)

        for i in range(self.maze.shape[0]):
            for j in range(self.maze.shape[1]):
                self.colors[i, j] = (
                    randint(0, 255), randint(0, 255), randint(0, 255))
                if i > 0:
                    self.edges.append(((i-1, j), (i, j)))
                if j > 0:
                    self.edges.append(((i, j-1), (i, j)))

        self.generated = False

    def iterate(self):
        if len(self.edges):
            shuffle(self.edges)

            e1, e2 = self.edges.pop()

            while self.union_find_sets.find(e1) == self.union_find_sets.find(e2) and len(self.edges):
                e1, e2 = self.edges.pop()

            if self.union_find_sets.find(e1) == self.union_find_sets.find(e2):
                return

            self.union_find_sets.union(e1, e2)
            self.maze[e1].remove_wall(self.maze[e2])
        else:
            self.generated = True

    def draw(self, screen):
        # Drawing maze
        for i in range(self.maze.shape[0]):
            for j in range(self.maze.shape[1]):
                color = self.colors[self.union_find_sets.find((i, j))]
                self.draw_node(self.maze[i, j], screen,
                               self.box_boarder_color, color)

    def draw_node(self, node, screen, boarder_color, fill_color):
        x, y = node.position
        current_box = self.box.move((self.box.width*x, self.box.height*y))

        thicc = 3

        pygame.draw.rect(screen, fill_color, current_box)
        if node.north_boarder:
            pygame.draw.line(screen, boarder_color, (self.box.width*x, self.box.height*y),
                             (self.box.width*(x+1), self.box.height*y),	thicc)
        if node.south_boarder:
            pygame.draw.line(screen, boarder_color, (self.box.width*x, self.box.height *
                             (y+1)), 	(self.box.width*(x+1), self.box.height*(y+1)), thicc)
        if node.east_boarder:
            pygame.draw.line(screen, boarder_color, (self.box.width*x, self.box.height*y),
                             (self.box.width*x, self.box.height*(y+1)),	thicc)
        if node.west_boarder:
            pygame.draw.line(screen, boarder_color, (self.box.width*(x+1),
                             self.box.height*y),	(self.box.width*(x+1), self.box.height*(y+1)), thicc)
