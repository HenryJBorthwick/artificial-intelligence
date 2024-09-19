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
    
graph = ExplicitGraph(nodes=set('SAG'),
                      edge_list=[('S','A'), ('S', 'G'), ('A', 'G')],
                      starting_nodes=['S'],
                      goal_nodes={'G'})
                         
solutions = generic_search(graph, DFSFrontier())
solution = next(solutions, None)
print_actions(solution)