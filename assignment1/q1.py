import math
from search import *

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


# TEST 1
map_str = """\
+-------+
|  9  XG|
|X XXX P|
| S  0FG|
|XX P XX|
+-------+
"""

graph = RoutingGraph(map_str)

print("Starting nodes:", sorted(graph.starting_nodes()))
print("Outgoing arcs (available actions) at starting states:")
for s in sorted(graph.starting_nodes()):
    print(s)
    for arc in graph.outgoing_arcs(s):
        print("  " + str(arc))

node = (1, 1, 5)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print("  " + str(arc))

node = (1, 7, 2)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print("  " + str(arc))

node = (3, 7, 0)
print("\nIs {} goal?".format(node), graph.is_goal(node))

node = (3, 7, math.inf)
print("\nIs {} goal?".format(node), graph.is_goal(node))

node = (3, 6, 5)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print("  " + str(arc))

node = (3, 6, 9)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print("  " + str(arc))

node = (2, 7, 4)  # at a location with a portal
print("\nOutgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print("  " + str(arc))


# TEST 2
# map_str = """\
# +--+
# |GS|
# +--+
# """
#
# graph = RoutingGraph(map_str)
#
# print("Starting nodes:", sorted(graph.starting_nodes()))
# print("Outgoing arcs (available actions) at the start:")
# for start in graph.starting_nodes():
#     for arc in graph.outgoing_arcs(start):
#         print ("  " + str(arc))
#
#
# node = (1,1,1)
# print("\nIs {} goal?".format(node), graph.is_goal(node))
# print("Outgoing arcs (available actions) at {}:".format(node))
# for arc in graph.outgoing_arcs(node):
#     print ("  " + str(arc))


# TEST 3
# map_str = """\
# +------+
# |S    S|
# |  GXXX|
# |S     |
# +------+
# """
#
# graph = RoutingGraph(map_str)
# print("Starting nodes:", sorted(graph.starting_nodes()))
