from search import Arc, Graph
from math import sqrt


class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location # dictionary, keys are string and nodes of the graph, value are tuple of numbers (x, y)
        self.radius = radius # non negative number
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes

    def starting_nodes(self):
        return self._starting_nodes

    def is_goal(self, node):
        return self.goal_nodes == node

    def outgoing_arcs(self, tail): # destination node
        arcs = []

        # Iterate over each head node in the location dict
        # Returns a list of each of the head nodes
        for head in self.location.keys():

            # Get location head node / source node
            head_dist = self.location[head]

            # Get location tail node / destination node
            tail_dist = self.location[tail]

            # Calculate the Euclidean distance between head and tail node
            # FORMULA: d = sqrt(tailx - headx)^2 + (headx - heady)^2)

            euclid_dist_x = (tail_dist[0] - head_dist[0])**2
            euclid_dist_y = (tail_dist[1] - head_dist[1])**2
            euclid_dist = sqrt(euclid_dist_x + euclid_dist_y)

            # Check if the distance is within the radius
            # AND the avoid self loops
            if euclid_dist <= self.radius and head != tail:
                # Create edge and add to list of edges plane can be
                arcs.append(Arc(tail, head, f"{tail}->{head}", euclid_dist))

        # Return arcs sorted alphabetically by head node
        return sorted(arcs, key=lambda arc: arc.head)

def main():
    # Test 1
    graph = LocationGraph(
        location={'A': (0, 0),
                  'B': (3, 0),
                  'C': (3, 4),
                  'D': (7, 0), },
        radius=5,
        starting_nodes=['A'],
        goal_nodes={'C'}
    )

    for arc in graph.outgoing_arcs('A'):
        print(arc)

    print()

    for arc in graph.outgoing_arcs('B'):
        print(arc)

    print()

    for arc in graph.outgoing_arcs('C'):
        print(arc)

if __name__ == '__main__':
    main()