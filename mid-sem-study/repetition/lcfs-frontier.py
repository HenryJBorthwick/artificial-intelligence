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
        if node in self.goal_nodes:
            return True

    def outgoing_arcs(self, tail):
        arcs = []
        #sqrt((x1-x2)**2 + (y1-y2)**2)
        for node in self.location.keys():
            if tail != node:
                
                x1, y1 = self.location[tail]
                x2, y2 = self.location[node]

                euclid = sqrt((x1-x2)**2 + (y1-y2)**2)

                if euclid <= self.radius:
                    arcs.append(Arc(tail=tail, head=node, action=tail + "->" + node, cost=euclid))
        arcs = sorted(arcs)
        return arcs
    

class LCFSFrontier(Frontier):

    def __init__(self):
        self.container = []
        self.order = 0

    def add(self, path):
        # sum of total path cost
        path_cost = 0
        for arc in path:
            path_cost += arc.cost

        heapq.heappush(self.container, (path_cost, self.order, path))

        self.order += 1

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.container) > 0:
            return heapq.heappop(self.container)[2]
        else:
            raise StopIteration

# test

graph = ExplicitGraph(nodes=set('ABCD'),
                      edge_list=[('A', 'D', 7), ('A', 'B', 2),
                                 ('B', 'C', 3), ('C', 'D', 1)],
                      starting_nodes=['A'],
                      goal_nodes={'D'})

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)