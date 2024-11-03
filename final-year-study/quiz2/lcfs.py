from search import *
import heapq

class LCFSFrontier(Frontier):
    def __init__(self):
        self.container = []
        self.order = 0

    def add(self, path):
        path_cost = 0
        for arc in path:
            path_cost += arc.cost

        heapq.heappush(self.container, (path_cost, self.order, path))

        self.order += 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.container) > 0:
            cost, order, path = heapq.heappop(self.container)
            return path
        else:
            raise StopIteration