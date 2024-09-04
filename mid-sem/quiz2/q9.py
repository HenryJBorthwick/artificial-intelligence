from search import *
# from collections import heapq (This is for bfs)
import heapq
from math import sqrt

class LCFSFrontier(Frontier):

    def __init__(self):
        # Priority Queue
        self.container = []
        self.order = 0

    def add(self, path):
        # ensure stable and tie breaker when both has same cost to add first added one
        priority = sum(arc.cost for arc in path)
        entry_count = self.order
        task = path
        heapq.heappush(self.container, (priority, entry_count, task))
        self.order += 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.container) > 0:
            priority, entry_count, task = heapq.heappop(self.container)
            return task
        else:
            raise StopIteration
        

class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
    
    def starting_nodes(self):
        return self._starting_nodes
    
    def is_goal(self, node):
        return node in self.goal_nodes #NOTE CAN NOT DO ==
    
    # filter out arcs that do not have matching tail nodes
    def outgoing_arcs(self, tail):
        # start with list of arcs
        arcs = []
        # loop through nodes
        for node in self.location.keys():

            # instead if tails match, we are doing if within radius
            # to do this we need to calculate Euclidean distance
            # euclidean = sqrt((x1 - x2)^2 + (y1 - y2)^2)
            x1, y1 = self.location[tail]
            x2, y2 = self.location[node]

            euclid = sqrt((x1 - x2)**2 + (y1 - y2)**2)

            if euclid <= self.radius and node != tail:
                arcs.append(Arc(tail, node, str(tail) + '->' + str(node), euclid))
        
            arcs.sort()
            
        return arcs
    

# test1
frontier = LCFSFrontier()
frontier.add((Arc(None, None, None, 17),))
frontier.add((Arc(None, None, None, 11), Arc(None, None, None, 4)))
frontier.add((Arc(None, None, None, 7), Arc(None, None, None, 8)))

for path in frontier:
    print(path)


# test2
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


# test3
graph = ExplicitGraph(nodes=set('ABCD'),
                      edge_list=[('A', 'D', 7), ('A', 'B', 2),
                                 ('B', 'C', 3), ('C', 'D', 1)],
                      starting_nodes=['A'],
                      goal_nodes={'D'})

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)