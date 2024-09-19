from search import *

class DFSFrontier(Frontier):
    
    def __init__(self):
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration
    

# test
graph = ExplicitGraph(nodes=['Knowledge',
                             'Commerce',
                             'Wisdom',
                             'Wealth',
                             'Happiness'],
                      edge_list=[('Knowledge', 'Wisdom'),
                             ('Commerce', 'Wealth'),
                             ('Happiness', 'Happiness')],
                      starting_nodes=['Commerce'],
                      goal_nodes={'Happiness'})

solutions = generic_search(graph, DFSFrontier())
solution = next(solutions, None)
print_actions(solution)