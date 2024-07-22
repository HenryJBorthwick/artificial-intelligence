from collections import deque

from search import *

class FunkyNumericGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""

    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        """Takes a node (which is an integer in this problem) and returns
        outgoing arcs (always two arcs in this problem)"""
        return [Arc(tail_node, tail_node - 1, "1down", 1),
                Arc(tail_node, tail_node + 2, "2up", 1)
                ]

    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the seqence always has one element."""
        return [self.starting_number]

    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal."""
        return node % 10 == 0

class BFSFrontier(Frontier):
    """ Implements a frontier container appropriate for breadth-first
    search """

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty queue."""
        self.container = deque()

    def add(self, path):
        """ Adds a path to the queue """
        self.container.append(path)  # enqueue operation

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            return self.container.popleft()  # dequeue operation
        else:
            raise StopIteration


def main():
    # purly for testing
    from itertools import dropwhile

    # test 1
    graph = FunkyNumericGraph(4)
    for node in graph.starting_nodes():
        print(node)

    # test 2
    graph = FunkyNumericGraph(4)
    for arc in graph.outgoing_arcs(7):
        print(arc)

    # test 3
    graph = FunkyNumericGraph(3)
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))
    print()
    print_actions(next(solutions))

    # test 4
    graph = FunkyNumericGraph(3)
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))


if __name__ == "__main__":
    main()
