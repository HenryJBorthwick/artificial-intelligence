from search import *
from math import sqrt
import heapq


class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
    
    def starting_nodes(self):
        return self._starting_nodes
    
    def is_goal(self, node):
        return node in self.goal_nodes
    
    def outgoing_arcs(self, tail):
        arcs = []

        for node in self.location.keys():
            
            if tail != node:
                # current node
                x1, y1 = self.location[tail]
                # each node in dict
                x2, y2 = self.location[node]

                euclid = sqrt((x1 - x2)**2 + (y1 - y2)**2)

                if euclid <= self.radius:
                    arcs.append(Arc(tail=tail, head=node, action=tail + "->" + node, cost=euclid))
        
        arcs = sorted(arcs)
        return arcs


class LCFSFrontier(Frontier):

    def __init__(self):
        self.container = []
        self.order = 0

    def add(self, path):
        path_cost = 0
        for node in path:
            path_cost += node.cost

        heapq.heappush(self.container, (path_cost, self.order, path))
        self.order += 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.container) > 0:
            return heapq.heappop(self.container)[2]
        else:
            raise StopIteration
        

# TEST
graph = LocationGraph(
    location={'A': (25, 7),
              'B': (1, 7),
              'C': (13, 2),
              'D': (37, 2)},
    radius=15,
    starting_nodes=['B'],
    goal_nodes={'D'}
)

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)