from search import *

class BFSFrontier(Frontier):
    def __init__(self):
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop(0)
        else:
            raise StopIteration
        

graph = ExplicitGraph(nodes=set('SAG'),
                      edge_list = [('S','A'), ('S', 'G'), ('A', 'G')],
                      starting_nodes = ['S'],
                      goal_nodes = {'G'})

solutions = generic_search(graph, BFSFrontier())
solution = next(solutions, None)
print_actions(solution)


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