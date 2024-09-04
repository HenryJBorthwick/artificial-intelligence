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
        return self.goal_nodes == node
    
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
    

# test 1
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


# test 2
graph = LocationGraph(
    location={'SW': (-2, -2),
              'NW': (-2, 2),
              'NE': (2, 2),
              'SE': (2, -2)},
    radius = 5,
    starting_nodes=['NE'],
    goal_nodes={'SW'}
)

for arc in graph.outgoing_arcs('NE'):
    print(arc)

print()

for arc in graph.outgoing_arcs('NW'):
    print(arc)

print()

for arc in graph.outgoing_arcs('SW'):
    print(arc)

print()


for arc in graph.outgoing_arcs('SE'):
    print(arc)