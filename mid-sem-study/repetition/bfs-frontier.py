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

#test1
flights = ExplicitGraph(nodes=['Christchurch', 'Auckland', 
                               'Wellington', 'Gold Coast'],
                        edge_list = [('Christchurch', 'Gold Coast'),
                                 ('Christchurch','Auckland'),
                                 ('Christchurch','Wellington'),
                                 ('Wellington', 'Gold Coast'),
                                 ('Wellington', 'Auckland'),
                                 ('Auckland', 'Gold Coast')],
                        starting_nodes = ['Christchurch'],
                        goal_nodes = {'Gold Coast'})

my_itinerary = next(generic_search(flights, BFSFrontier()), None)
print_actions(my_itinerary)