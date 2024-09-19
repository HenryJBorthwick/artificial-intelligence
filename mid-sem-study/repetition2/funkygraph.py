from search import *
from collections import deque

class BFSFrontier(Frontier):

    def __init__(self):
        self.container = deque()

    def add(self, path):
        self.container.appendleft(path)
    
    def __iter__(self):
        return self

    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration
        


class FunkyNumericGraph(Graph):

    def __init__(self, starting_node):
        self.starting_node = starting_node

    def is_goal(self, node):
        if node % 10 == 0:
            return True
    
    def starting_nodes(self):
        return [self.starting_node]
    
    def outgoing_arcs(self, tail_node):
        return [Arc(tail=tail_node, head=tail_node-1, action="1down", cost=1),
                Arc(tail=tail_node, head=tail_node+2, action="2up", cost=1)]
    

from itertools import dropwhile

graph = FunkyNumericGraph(3)
solutions = generic_search(graph, BFSFrontier())
print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))