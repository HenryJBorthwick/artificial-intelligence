from search import Arc, Graph, Frontier, print_actions, generic_search, ExplicitGraph
from math import sqrt
import heapq


class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location  # dictionary, keys are string and nodes of the graph, value are tuple of numbers (x, y)
        self.radius = radius  # non negative number
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes

    def starting_nodes(self):
        return self._starting_nodes

    def is_goal(self, node):
        return node in self.goal_nodes

    def outgoing_arcs(self, tail):  # destination node
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

            euclid_dist_x = (tail_dist[0] - head_dist[0]) ** 2
            euclid_dist_y = (tail_dist[1] - head_dist[1]) ** 2
            euclid_dist = sqrt(euclid_dist_x + euclid_dist_y)

            # Check if the distance is within the radius
            # AND the avoid self loops
            if euclid_dist <= self.radius and head != tail:
                # Create edge and add to list of edges plane can be
                arcs.append(Arc(tail, head, f"{tail}->{head}", euclid_dist))

        # Return arcs sorted alphabetically by head node
        return sorted(arcs, key=lambda arc: arc.head)


class LCFSFrontier(Frontier):
    # Priority Queue as heapq

    def __init__(self):
        # Holds the paths in the priority queue
        self.container = []
        # Ensure the priority queue remains stable.
        # Ensure that elements of the same value/cost are
        # returned in the order they were added.
        self.count = 0

    def add(self, path):
        # Calculate the cost of added path
        path_cost = sum(arc.cost for arc in path)
        # Take priority queue and add path, again the count ensuring ordered by insertion time
        heapq.heappush(self.container, (path_cost, self.count, path))
        # Update insertion count
        self.count += 1

    def __next__(self):
        # Check if there is path to explore
        if len(self.container) > 0:
            # heapq pops the lowest cost element, the index [2] makes it return the path
            # return heapq.heappop(self.container)[2]
            path_cost, count, path = heapq.heappop(self.container)
            return path
        else:
            # Signal there is no elements left in the priority queue
            raise StopIteration

    def __iter__(self):
        # Return the LCFSFrontier as an iterator object
        return self


def main():
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

if __name__ == '__main__':
    main()