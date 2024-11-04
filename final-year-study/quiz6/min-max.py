def max_value(tree):
    
    # Base case
    if isinstance(tree, int):
        return tree
    
    # Recursive case
    # init alpha
    max_util = -float('inf')

    # navigate to children
    for child in tree:
        # get min value
        util = min_value(child)
        # if child value greater than parent value
        if util > max_util:
            # update alpha to greater value
            max_util = util
    
    return max_util


def min_value(tree):

    # Base case
    if isinstance(tree, int):
        return tree
    
    # Recursive case
    # init beta
    min_util = float('inf')

    # navigate to children
    for child in tree:
        # get min value
        util = max_value(child)
        # if child value greater than parent value
        if util < min_util:
            # update alpha to greater value
            min_util = util
    
    return min_util

# TODO When converting, swap equality sign, remove -ve, 

game_tree = 3

print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))

game_tree = [1, 2, 3]

print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))


game_tree = [1, 2, [3]]

print(min_value(game_tree))
print(max_value(game_tree))


game_tree = [[1, 2], [3]]

print(min_value(game_tree))
print(max_value(game_tree))


# def max_value(tree):
    
#     # Base case
#     if isinstance(tree, int):
#         return tree
    
#     return max(min_value(x) for x in tree)