def max_action_value(game_tree):

    # check terminal node
    if isinstance(game_tree, int):
        return (None, game_tree)
    
    #init alpha
    max_util = float('-inf')
    # init best action
    best_action = None

    #loop through tree
    for index, child in enumerate(game_tree):
        # get min util
        action, util = min_action_value(child)

        # check if better
        if util > max_util:
            # update max util
            max_util = util
            # update best action
            best_action = index

    # return alpha and best action
    return (best_action, max_util)



def min_action_value(game_tree):

    # check terminal node
    if isinstance(game_tree, int):
        return (None, game_tree)
    
    #init alpha
    min_util = float('inf')
    # init best action
    best_action = None

    #loop through tree
    for index, child in enumerate(game_tree):
        # get min util
        action, util = max_action_value(child)

        # check if better
        if util < min_util:
            # update max util
            min_util = util
            # update best action
            best_action = index

    # return alpha and best action
    return (best_action, min_util)


game_tree = [2, [-3, 1], 4, 1]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)