from search import *
import heapq

# from q1 import *
CHECK_PROXIMITY = \
    [('N', -1, 0),
     ('NE', -1, 1),
     ('E', 0, 1),
     ('SE', 1, 1),
     ('S', 1, 0),
     ('SW', 1, -1),
     ('W', 0, -1),
     ('NW', -1, -1)]


class RoutingGraph(Graph):
    def __init__(self, map_str):
        self.map_str = map_str.split("\n")
        self.map_list = []
        for i in range(len(self.map_str) - 1):
            row = list(self.map_str[i])
            self.map_list.append(row)

        self.num_rows = len(self.map_list[0])
        self.num_cols = len(self.map_list)
        self.agent = []
        self.portal = []
        self.goal = []
        self.find_vals()

    def starting_nodes(self):
        return self.agent

    def find_vals(self):
        for col in range(self.num_cols):
            for row in range(self.num_rows):

                if self.map_list[col][row] == "P":
                    self.portal.append((col, row))

                if self.map_list[col][row].isnumeric():
                    self.agent.append((col, row, int(self.map_list[col][row])))

                if self.map_list[col][row] == "S":
                    self.agent.append((col, row, float("inf")))

                if self.map_list[col][row] == "G":
                    self.goal.append((col, row))

    def is_goal(self, node):
        col, row, fuel = node
        return (col, row) in self.goal

    def outgoing_arcs(self, tail_node):
        arcs = []
        initial_col, initial_row, fuel = tail_node
        tail = self.map_list[initial_col][initial_row]

        for direction, col, row in CHECK_PROXIMITY:
            new_col = initial_col + col
            new_row = initial_row + row
            head = self.map_list[new_col][new_row]

            # Check for boundary
            if head not in ["|", "+", "-", "X"] and fuel > 0:
                # Change time costs whether Diagonal or Orthogonal movement
                cost = 5 if direction in ['N', 'E', 'S', 'W'] else 7

                # Move with cost of 1 unit fuel
                arcs.append(Arc(tail_node, (new_col, new_row, fuel - 1), direction, cost))

        # Fuel station
        if tail == "F" and fuel < 9:
            arcs.append(Arc(tail_node, (initial_col, initial_row, 9), "Fuel up", 15))

        # Teleportation portal
        if tail == "P":
            arcs += self.teleport(tail_node, (initial_col, initial_row))

        return arcs

    def teleport(self, node, portal):
        output = []
        initial_col, initial_row, fuel = node

        for col, row in self.portal:
            if (col, row) != portal:
                output.append(Arc(node, (col, row, fuel), f"Teleport to {(col, row)}", 10))

        return output

    # MODIFIED FOR Q3
    def estimated_cost_to_goal(self, node):
        col1, row1, fuel = node
        min_cost = float('inf')

        for goal_node in self.goal:
            col2, row2 = goal_node
            # Compute differences
            d_col = abs(col1 - col2)
            d_row = abs(row1 - row2)

            # Diagonal and straight line movement
            diagonal_moves = min(d_col, d_row)
            straight_moves = max(d_col, d_row) - diagonal_moves

            # Cost with diagonal and straight moves
            cost = diagonal_moves * 7 + straight_moves * 5

            min_cost = min(min_cost, cost)

        return min_cost


class AStarFrontier(Frontier):
    def __init__(self, map_graph):
        self.container = []
        self.order = 0
        self.map_graph = map_graph
        self.visited = set()
        self.expanded = []

    def add(self, path):
        # PATH COST
        cost = 0
        for arc in path:
            cost += arc.cost

        h = self.map_graph.estimated_cost_to_goal(path[-1].head)

        heapq.heappush(self.container, (cost + h, self.order, path))
        self.order += 1

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.container) > 0:
            total, order, path = heapq.heappop(self.container)
            head = path[-1].head

            if head not in self.visited:
                self.visited.add(head)
                self.expanded.append(path)
                return path
        else:
            raise StopIteration


def print_map(map_graph, frontier, solution):
    path_trace = map_graph.map_list

    for path in frontier.expanded:
        for arc in path:
            col, row, fuel = arc.head
            if not map_graph.is_goal(arc.head) and arc.head not in map_graph.agent:
                path_trace[col][row] = "."

    if solution != None:
        for arc in solution:
            col, row, fuel = arc.head
            if not map_graph.is_goal(arc.head) and arc.head not in map_graph.agent:
                path_trace[col][row] = "*"

    print("\n".join("".join(s) for s in path_trace))


# TEST 1
map_str = """\
+----------------+
|                |
|                |
|                |
|                |
|                |
|                |
|        S       |
|                |
|                |
|     G          |
|                |
|                |
|                |
+----------------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)


# TEST 2
map_str = """\
+----------------+
|                |
|                |
|                |
|                |
|                |
|                |
|        S       |
|                |
|                |
|     G          |
|                |
|                |
|                |
+----------------+
"""

map_graph = RoutingGraph(map_str)
# changing the heuristic so the search behaves like LCFS
map_graph.estimated_cost_to_goal = lambda node: 0

frontier = AStarFrontier(map_graph)

solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)


# TEST 3 TO FIX
map_str = """\
+-------------+
| G         G |
|      S      |
| G         G |
+-------------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)


# TEST 4
map_str = """\
+-------+
|     XG|
|X XXX  |
|  S    |
+-------+
"""
map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)


# TEST 5
map_str = """\
+--+
|GS|
+--+
"""
map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)


# TEST 6
map_str = """\
+----+
|    |
| SX |
| X G|
+----+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)


# TEST 7 TO FIX
map_str = """\
+---------------+
|    G          |
|XXXXXXXXXXXX   |
|           X   |
|  XXXXXX   X   |
|  X S  X   X   |
|  X        X   |
|  XXXXXXXXXX   |
|               |
+---------------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)


# TEST 8
map_str = """\
+---------+
|         |
|    G    |
|         |
+---------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)


# CUSTOM TEST 9
# map_str = """\
# +-------------+
# |S            |
# |             |
# |   G      S  |
# |             |
# | G           |
# +-------------+
# """
#
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_map(map_graph, frontier, solution)