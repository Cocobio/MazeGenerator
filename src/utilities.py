import numpy as np
from typing import Tuple


class UnionFind:
    def __init__(self, dims: Tuple[int, int]) -> None:
        self.sets: np.ndarray = np.empty(dims, dtype=object)
        self.sets_sizes: np.ndarray = np.ones(dims)
        # self.n_sets: int = dims[0]*dims[1]

        for i in range(dims[0]):
            for j in range(dims[1]):
                self.sets[i, j] = (i, j)

    def find(self, tup: Tuple[int, int]) -> Tuple[int, int]:
        if (self.sets[tup] == tup):
            return tup
        else:
            self.sets[tup] = self.find(self.sets[tup])
            return self.sets[tup]

    def union(self, x: Tuple[int, int], y: Tuple[int, int]) -> None:
        r_x = self.find(x)
        r_y = self.find(y)

        if self.sets_sizes[r_x] > self.sets_sizes[r_y]:
            self.sets[r_y] = r_x
            self.sets_sizes[r_x] += self.sets_sizes[r_y]
        else:
            self.sets[r_x] = r_y
            self.sets_sizes[r_y] += self.sets_sizes[r_x]
