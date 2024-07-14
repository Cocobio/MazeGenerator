import numpy as np
from random import randint
from src.maze_builder_interface import MazeBuilderInterface
from typing import List, Tuple


class BackTracker(MazeBuilderInterface):
    def __init__(self, columns: int, rows: int) -> None:
        super().__init__(columns, rows)

        # Select random node and initialize stack & visited
        rand_node: Tuple[int, int] = (randint(0, self._dims[0]-1),
                                      randint(0, self._dims[1]-1))
        self._current_node: MazeBuilderInterface.Node = self._maze[rand_node]
        self._stack: List[MazeBuilderInterface.Node] = [
            self._maze[rand_node]]
        self._visited: np.ndarray = np.zeros(self._dims, dtype=np.int8)
        self._visited[rand_node] = 1

    def iterate(self) -> None:
        if self._stack:
            self._current_node = self._stack.pop()
            neighbor_not_checked = len(self._current_node.neighbor)
            if neighbor_not_checked:
                self._stack.append(self._current_node)
                random_move = self._current_node.neighbor.pop(
                    randint(0, neighbor_not_checked-1))

                if self._visited[random_move] == 0:
                    self._visited[random_move] = 1
                    self._current_node.remove_wall(self._maze[random_move])
                    self._current_node = self._maze[random_move]

                    self._stack.append(self._current_node)
        else:
            self._generated = True
