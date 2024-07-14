from abc import abstractmethod
import numpy as np
from typing import Tuple, List


class MazeBuilderInterface:
    class Node:
        def __init__(self, position: Tuple[int, int]) -> None:
            self._pos = position

            self.north_boarder: bool = True
            self.south_boarder: bool = True
            self.east_boarder: bool = True
            self.west_boarder: bool = True

            self.neighbor: List[Tuple[int, int]] = []

        # todo: Add correct type hinting for other node
        def remove_wall(self, other_node) -> None:
            x: int = self._pos[0] - other_node._pos[0]
            y: int = self._pos[1] - other_node._pos[1]

            if y == -1:
                self.south_boarder = False
                other_node.north_boarder = False
            elif y == 1:
                self.north_boarder = False
                other_node.south_boarder = False
            elif x == -1:
                self.east_boarder = False
                other_node.west_boarder = False
            elif x == 1:
                self.west_boarder = False
                other_node.east_boarder = False
            else:
                raise ValueError(f'''Other node (Node{other_node._pos})
                                 does not border current one
                                 (Node{self._pos}).''')

    def __init__(self, columns: int, rows: int) -> None:
        self._dims: Tuple[int, int] = (columns, rows)
        self._maze: np.ndarray = np.empty(
            self._dims, dtype=MazeBuilderInterface.Node)

        for i in range(self._dims[0]):
            for j in range(self._dims[1]):
                self._maze[i][j] = MazeBuilderInterface.Node((i, j))

                if (i > 0):
                    self._maze[i][j].neighbor.append((i-1, j))
                if (i < self._dims[0]-1):
                    self._maze[i][j].neighbor.append((i+1, j))
                if (j > 0):
                    self._maze[i][j].neighbor.append((i,   j-1))
                if (j < self._dims[1]-1):
                    self._maze[i][j].neighbor.append((i,   j+1))

        self._generated = False

    @abstractmethod
    def iterate(self) -> None:
        raise NotImplementedError(
            "Algorithms not fully implemented. Missing next iteration")

    def build(self) -> None:
        while not self._generated:
            self.iterate()

    def __str__(self) -> str:
        rep: list[str] = []
        for i in range(self._dims[1]):
            for j in range(self._dims[0]):
                rep.append("0")
                if j != self._dims[0]-1:
                    rep.append("1" if self._maze[j, i].east_boarder else "0")
            rep.append("\n")
            if i != self._dims[1]-1:
                for j in range(self._dims[0]):
                    rep.append("1" if self._maze[j, i].south_boarder else "0")
                    if j != self._dims[0]-1:
                        rep.append("1")
            if i != self._dims[1]-1:
                rep.append("\n")

        return ''.join(rep)
