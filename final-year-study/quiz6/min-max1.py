def max_value(tree):

    # check terminal node
    if isinstance(tree, int):
        return tree
    
    #init alpha
    max_util = float('-inf')

    #loop through tree
    for child in tree:
        # get min util
        util = min_value(child)

        # check if better
        if util > max_util:
            # update max util
            max_util = util

    # return alpha
    return max_util

def min_value(tree):

    # check terminal node
    if isinstance(tree, int):
        return tree
    
    #init beta
    min_util = float('inf')

    #loop through tree
    for child in tree:
        # get max util
        util = max_value(child)

        # check if better
        if util < min_util:
            # update max util
            min_util = util

    # return alpha
    return min_util

# implementation notes
# dont forget to flip equality sign

# min-max
# check terminal
# init util
# loop through tree
# get util
# compare util and update if better
# return best util

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