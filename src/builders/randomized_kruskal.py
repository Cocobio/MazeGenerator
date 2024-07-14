from random import randint
from src.maze_builder_interface import MazeBuilderInterface
from src.utilities import UnionFind


class RandomizedKruskal(MazeBuilderInterface):
    def __init__(self, columns: int, rows: int) -> None:
        super().__init__(columns, rows)
        self._edges = []

        self._sets: UnionFind = UnionFind(self._dims)

        for i in range(self._dims[0]):
            for j in range(self._dims[1]):
                if i > 0:
                    self._edges.append(((i-1, j), (i, j)))
                if j > 0:
                    self._edges.append(((i, j-1), (i, j)))

    def iterate(self) -> None:
        if self._edges:
            rnd: int = randint(0, len(self._edges)-1)
            self._edges[-1], self._edges[rnd] = self._edges[rnd], self._edges[-1]

            e1, e2 = self._edges.pop()

            while self._sets.find(e1) == self._sets.find(e2) and self._edges:
                rnd = randint(0, len(self._edges)-1)
                self._edges[-1], self._edges[rnd] = self._edges[rnd], self._edges[-1]
                e1, e2 = self._edges.pop()

            if self._sets.find(e1) == self._sets.find(e2):
                return

            self._sets.union(e1, e2)
            self._maze[e1].remove_wall(self._maze[e2])
        else:
            self._generated = True
