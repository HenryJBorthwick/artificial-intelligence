from search import *
from collections import deque
import copy

BLANK = ' '


class SlidingPuzzleGraph(Graph):
    """Objects of this type represent (n squared minus one)-puzzles."""

    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""

        n = len(state)  # the size of the puzzle

        # Find i and j such that state[i][j] == BLANK
        indices = [(i, j) for i in range(len(state)) for j in range(len(state[i])) if state[i][j] == BLANK]

        i, j = indices[0]

        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i - 1][j])  # or blank goes up
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i + 1][j])  # or blank goes down
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j - 1])  # or blank goes left
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            action = "Move {} left".format(state[i][j + 1])  # or blank goes right
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        return arcs

    def starting_nodes(self):
        return [self.starting_state]

    def is_goal(self, state):
        """Returns true if the given state is the goal state, False
        otherwise. There is only one goal state in this problem."""

        size = len(state)
        goal = []
        current_row = []

        # Construct the goal state
        for index in range(size * size):
            if index == 0:
                current_row.append(BLANK)
            else:
                current_row.append(index)

            # When a row is complete, add it to the goal state
            if len(current_row) == size:
                goal.append(current_row)
                current_row = []

        return state == goal

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
    # Test 1
    graph = SlidingPuzzleGraph([[1, 2, 5],
                                [3, 4, 8],
                                [6, 7, BLANK]])

    solutions = generic_search(graph, BFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)

    # Test 2
    graph = SlidingPuzzleGraph([[3, BLANK],
                                [1, 2]])

    solutions = generic_search(graph, BFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)

    # Test 3
    graph = SlidingPuzzleGraph([[1, BLANK, 2],
                                [6, 4, 3],
                                [7, 8, 5]])

    solutions = generic_search(graph, BFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)


if __name__ == "__main__":
    main()
