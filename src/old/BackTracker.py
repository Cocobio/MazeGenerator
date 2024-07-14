import pygame
import numpy as np
import copy
from random import randint

class BackTracker:
	box_boarder_color = (24, 27, 30)
	box_fill_color = (78, 245, 236)
	box_visited_fill_color = (255, 174, 43)
	box_current_fill_color = (0, 255, 0)
	box_stack_color = (18, 94, 161)

	def __init__(self, maze, box):
		self.stack = []
		self.maze = copy.deepcopy(maze)
		self.box = box
		self.visited = np.zeros(self.maze.shape)

		self.generated = False

	def iterate(self):
		if len(self.stack):
			self.current_node = self.stack.pop()
			neighbor_not_checked = len(self.current_node.neighbor)
			if neighbor_not_checked != 0:
				self.stack.append(self.current_node)
				r = self.current_node.neighbor.pop(randint(0, neighbor_not_checked-1))

				if self.visited[r] == 0:
					self.visited[r] = 1
					self.current_node.remove_wall(self.maze[r])
					self.current_node = self.maze[r]

					self.stack.append(self.current_node)
		elif self.visited[0,0] == 0:
			r = (randint(0, self.maze.shape[0]-1), randint(0, self.maze.shape[1]-1))
			self.visited[r] = 1
			self.stack.append(self.maze[r])
			self.current_node = self.maze[r]
		else:
			self.generated = True

			self.current_node = None

	def draw(self, screen):
		# Drawing maze
		for i in range(self.maze.shape[0]):
			for j in range(self.maze.shape[1]):
				if self.visited[i,j] == 0:
					color = self.box_fill_color
				else:
					color = self.box_visited_fill_color
				self.draw_node(self.maze[i,j], screen, self.box_boarder_color, color)

		# Drawing nodes that are still on the stack
		for n in self.stack:
			self.draw_node(n, screen, self.box_boarder_color, self.box_stack_color)
		# Drawing current Position
		if self.current_node != None:
			self.draw_node(self.current_node, screen, self.box_boarder_color, self.box_current_fill_color)

	def draw_node(self, node, screen, boarder_color, fill_color):
		x, y = node.position
		current_box = self.box.move((self.box.width*x,self.box.height*y))

		thicc = 3

		pygame.draw.rect(screen, fill_color, current_box)
		if node.north_boarder:
			pygame.draw.line(screen, boarder_color, (self.box.width*x, self.box.height*y), 		(self.box.width*(x+1), self.box.height*y),	thicc)
		if node.south_boarder:
			pygame.draw.line(screen, boarder_color, (self.box.width*x, self.box.height*(y+1)), 	(self.box.width*(x+1), self.box.height*(y+1)),thicc)
		if node.east_boarder:
			pygame.draw.line(screen, boarder_color, (self.box.width*x, self.box.height*y),		(self.box.width*x, self.box.height*(y+1)),	thicc)
		if node.west_boarder:
			pygame.draw.line(screen, boarder_color, (self.box.width*(x+1), self.box.height*y),	(self.box.width*(x+1), self.box.height*(y+1)),thicc)








