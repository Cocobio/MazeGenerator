from src.builders.back_tracker import BackTracker
from src.builders.randomized_kruskal import RandomizedKruskal
from typing import List, Callable

algorithms_list: List[Callable] = [BackTracker,
                                   RandomizedKruskal]
