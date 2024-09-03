from search import *


class DFSFrontier(Frontier):

    def __init__(self):
        # create stack
        self.container = []


    def add(self, path):
        # add path to stack
        self.container.append(path)

    def __iter__(self):
        # return self
        return self

    def __next__(self):
        if len(self.container) > 0:
            # return top of stack
            return self.container.pop()
        else:
            raise StopIteration

# test1
graph = ExplicitGraph(nodes=set('SAG'),
                      edge_list=[('S','A'), ('S', 'G'), ('A', 'G')],
                      starting_nodes=['S'],
                      goal_nodes={'G'})
                         
solutions = generic_search(graph, DFSFrontier())
solution = next(solutions, None)
print_actions(solution)

# test2
graph = ExplicitGraph(nodes=set('SAG'),
                      edge_list=[('S', 'G'), ('S','A'), ('A', 'G')],
                      starting_nodes=['S'],
                      goal_nodes={'G'})

solutions = generic_search(graph, DFSFrontier())
solution = next(solutions, None)
print_actions(solution)

# test 3
available_flights = ExplicitGraph(
    nodes=['Christchurch', 'Auckland', 
           'Wellington', 'Gold Coast'],
    edge_list=[('Christchurch', 'Gold Coast'),
               ('Christchurch','Auckland'),
               ('Christchurch','Wellington'),
               ('Wellington', 'Gold Coast'),
               ('Wellington', 'Auckland'),
               ('Auckland', 'Gold Coast')],
    starting_nodes=['Christchurch'],
    goal_nodes={'Gold Coast'})

my_itinerary = next(generic_search(available_flights, DFSFrontier()), None)
print_actions(my_itinerary)