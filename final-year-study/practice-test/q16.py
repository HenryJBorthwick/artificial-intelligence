from math import inf

pruned_tree = [0, [-1, 1], [1]]
    

pruning_events = [
    (1, 1),
    (1, 1)
    ]


# technique:
# check terminal node, if so return for min or max
# perform min or max update value 
# check for pruning

# lab6, q5, tree:
"""
    [3, , 0]
    
    []
    
    [2, 1], []
    
    4, [7, -2]
"""

# [3, [[2, 1], [4, [7, -2]]], 0]
# strip a set of brackets
"""
[3, , 0]
[]
[2, 1], []
4, [7, -2]
"""