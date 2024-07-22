from collections import deque

from search import *

class BFSFrontier(Frontier):
    """ Implements a frontier container appropriate for breadth-first
    search """

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty queue."""
        self.container = deque()

    def add(self, path):
        """ Adds a path to the queue """
        self.container.append(path) #enqueue operation

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0 :
            return self.container.popleft() #dequeue operation
        else:
            raise StopIteration


def main():
    # test 1
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S', 'A'), ('S', 'G'), ('A', 'G')],
                          starting_nodes=['S'],
                          goal_nodes={'G'})

    solutions = generic_search(graph, BFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)

    # test 2
    flights = ExplicitGraph(nodes=['Christchurch', 'Auckland',
                                   'Wellington', 'Gold Coast'],
                            edge_list=[('Christchurch', 'Gold Coast'),
                                       ('Christchurch', 'Auckland'),
                                       ('Christchurch', 'Wellington'),
                                       ('Wellington', 'Gold Coast'),
                                       ('Wellington', 'Auckland'),
                                       ('Auckland', 'Gold Coast')],
                            starting_nodes=['Christchurch'],
                            goal_nodes={'Gold Coast'})

    my_itinerary = next(generic_search(flights, BFSFrontier()), None)
    print_actions(my_itinerary)

if __name__ == "__main__":
    main()