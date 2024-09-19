from search import Arc, Graph
from math import sqrt

class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
    
    def starting_nodes(self):
        return self._starting_nodes
    
    def is_goal(self, node):
        if node in self.starting_nodes():
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

# test
graph = LocationGraph(
    location={'A': (0, 0),
              'B': (3, 0),
              'C': (3, 4),
              'D': (7, 0),},
    radius = 5,
    starting_nodes=['A'],
    goal_nodes={'C'}
)

for node in graph.starting_nodes():
    print(node)

print()

for arc in graph.outgoing_arcs('A'):
    print(arc)

print()

for arc in graph.outgoing_arcs('B'):
    print(arc)

print()

for arc in graph.outgoing_arcs('C'):
    print(arc)