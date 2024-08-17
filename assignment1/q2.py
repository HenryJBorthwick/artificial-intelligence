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

    # ADDED FOR Q2
    def estimated_cost_to_goal(self, node):
        return 0


class AStarFrontier(Frontier):
    def __init__(self, map_graph):
        self.container = []
        self.order = 0
        self.map_graph = map_graph
        self.visited = set()
        self.expanded = []

    def add(self, path):
        cost = 0
        for arc in path:
            cost += arc.cost
        h = self.map_graph.estimated_cost_to_goal(path[-1].head)
        if path[-1].head not in self.visited:
            heapq.heappush(self.container, (cost + h, self.order, path))
            self.visited.add(path[-1].head)
        self.order += 1

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.container) > 0:
            total, order, path = heapq.heappop(self.container)
            self.expanded.append(path)

            return path
        else:
            raise StopIteration

# TEST 1
# map_str = """\
# +-------+
# |   G   |
# |       |
# |   S   |
# +-------+
# """
#
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)


# TEST 2
map_str = """\
+-------+
|  GG   |
|S    G |
|  S    |
+-------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_actions(solution)


# TEST 3
# map_str = """\
# +-------+
# |     XG|
# |X XXX  |
# | S     |
# +-------+
# """
#
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)


# TEST 4
# map_str = """\
# +-------+
# |  F  X |
# |X XXXXG|
# | 3     |
# +-------+
# """
#
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)


# TEST 5
# map_str = """\
# +--+
# |GS|
# +--+
# """
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)


# TEST 6
# map_str = """\
# +---+
# |GF2|
# +---+
# """
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)


# TEST 7
# map_str = """\
# +----+
# | S  |
# | SX |
# |GX G|
# +----+
# """
#
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)


# TEST 8
# map_str = """\
# +---------+
# |         |
# |    G    |
# |         |
# +---------+
# """
#
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)


# CUSTOM TEST 9
# map_str = """\
# +----------+
# |    X     |
# | S  X  G  |
# |    X     |
# +----------+
# """
#
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)


# CUSTOM TEST 10
# map_str = """\
# +----------+
# |       F  |
# |1 XXXXXXX |
# |FXX F     |
# |X   XXXXXX|
# |         G|
# +----------+
# """

# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)