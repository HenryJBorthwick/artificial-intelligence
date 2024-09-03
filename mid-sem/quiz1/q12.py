from search import *
from itertools import dropwhile
from collections import deque


class FunkyNumericGraph(Graph):
    
    def __init__(self, starting_number):
        self.starting_number = starting_number

    def starting_nodes(self):
        return [self.starting_number]

    def is_goal(self, node):
        # divisible by 10
        return (node % 10 == 0)
    
    def outgoing_arcs(self, tail_node):
        return [Arc(tail_node, tail_node -1, action="1down", cost=1),
                Arc(tail_node, tail_node +2, action="2up", cost=1)]


class BFSFrontier(Frontier):

    def __init__(self):
        # create queue
        self.container = deque()

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.container) > 0:
            # dequeue operation
            return self.container.popleft()
        else:
            raise StopIteration
        

# test1
graph = FunkyNumericGraph(4)
for node in graph.starting_nodes():
    print(node)

# test2
graph = FunkyNumericGraph(4)
for arc in graph.outgoing_arcs(7):
    print(arc)

# test3
graph = FunkyNumericGraph(3)
solutions = generic_search(graph, BFSFrontier())
print_actions(next(solutions))
print()
print_actions(next(solutions))

#test4
graph = FunkyNumericGraph(3)
solutions = generic_search(graph, BFSFrontier())
print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))