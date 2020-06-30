##########################################################################################################################
#
# Generated by Ignacio Osorio
#
# Backtracking algorithm implemented, using pygame as GUI
# algorithm reference: https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker
# solution: .............................
#
##########################################################################################################################


import pygame
import numpy as np
from random import randint

##########################################################################################################################
def draw_node(node, screen, box, box_boarder_color, box_fill_color):
	x, y = node.position
	current_box = box.move((box.width*x,box.height*y))

	thicc = 3

	pygame.draw.rect(screen, box_fill_color, current_box)
	if node.north_boarder:
		pygame.draw.line(screen, box_boarder_color, (box.width*x, box.height*y), 		(box.width*(x+1), box.height*y),	thicc)
	if node.south_boarder:
		pygame.draw.line(screen, box_boarder_color, (box.width*x, box.height*(y+1)), 	(box.width*(x+1), box.height*(y+1)),thicc)
	if node.east_boarder:
		pygame.draw.line(screen, box_boarder_color, (box.width*x, box.height*y),		(box.width*x, box.height*(y+1)),	thicc)
	if node.west_boarder:
		pygame.draw.line(screen, box_boarder_color, (box.width*(x+1), box.height*y),	(box.width*(x+1), box.height*(y+1)),thicc)

def backtracker(stack, maze, visited):
	if len(stack):
		current_node = stack.pop()
		neighbor_not_checked = len(current_node.neighbor)
		if neighbor_not_checked != 0:
			stack.append(current_node)
			r = current_node.neighbor.pop(randint(0, neighbor_not_checked-1))

			if visited[r] == 0:
				visited[r] = 1
				current_node.remove_wall(maze[r])
				current_node = maze[r]

				stack.append(current_node)
		return current_node
	else:
		return maze[0][0]
##########################################################################################################################

# Screen size
width = 800
height = 800

# maze parameters
maze_rows = 42
maze_columns = 42
# Creates rectangle for maze potition
box = pygame.Rect(0, 0, width/maze_columns, height/maze_rows)
box_boarder_color = (24, 27, 30)
box_fill_color = (78, 245, 236)
box_visited_fill_color = (255, 174, 43)
box_current_fill_color = (0, 255, 0)
box_stack_color = (18, 94, 161)

pygame.init()

# Create screen, set title and icon
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MazeGenerator")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Maze spects
class node:

	def __init__(self, position):
		self.position = position

		self.north_boarder = True
		self.south_boarder = True
		self.east_boarder = True
		self.west_boarder = True

		self.neighbor = []

	def remove_wall(self, other_node):
		x = self.position[0] - other_node.position[0]
		y = self.position[1] - other_node.position[1]

		if y<0:
			self.south_boarder = False
			other_node.north_boarder = False
		elif y>0:
			self.north_boarder = False
			other_node.south_boarder = False
		elif x<0:
			self.west_boarder = False
			other_node.east_boarder = False
		elif x>0:
			self.east_boarder = False
			other_node.west_boarder = False

maze = np.ones((maze_columns, maze_rows), dtype=node)
visited = np.zeros((maze_columns, maze_rows))

for i in range(maze_columns):
	for j in range(maze_rows):
		maze[i][j] = node((i,j))
		if (i>0):
			maze[i][j].neighbor.append((i-1, j))
		if (i<maze_columns-1):
			maze[i][j].neighbor.append((i+1, j))
		if (j>0):
			maze[i][j].neighbor.append((i,   j-1))
		if (j<maze_rows-1):
			maze[i][j].neighbor.append((i,   j+1))

# depth first algorithm
stack = []
visited[0][0] = 1
stack.append(maze[0][0])

running = True

while running:
	pygame.time.wait(2)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_PRINT:
				pygame.image.save(screen, "screenshot.jpeg")

	screen.fill((255,255,255))

	# Update maze
	current_node = backtracker(stack, maze, visited)

	# Drawing maze
	for i in range(maze_columns):
		for j in range(maze_rows):
			if visited[i][j] == 0:
				color = box_fill_color
			else:
				color = box_visited_fill_color
			draw_node(maze[i][j], screen, box, box_boarder_color, color)

	# Drawing nodes that are still on the stack
	for n in stack:
		draw_node(n, screen, box, box_boarder_color, box_stack_color)
	# Drawing current Position
	draw_node(current_node, screen, box, box_boarder_color, box_current_fill_color)

	pygame.display.update()
