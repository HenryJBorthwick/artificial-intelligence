def max_action_value(game_tree):
    if isinstance(game_tree, int):
        return (None, game_tree)
    
    max_util = float('-inf')
    best_action = None

    for index, child in enumerate(game_tree):
        _, util = min_action_value(child)

        if util > max_util:
            max_util = util
            best_action = index

    return (best_action, max_util)



def min_action_value(game_tree):
    if isinstance(game_tree, int):
        return (None, game_tree)
    
    min_util = float('inf')
    best_action = None

    for index, child in enumerate(game_tree):
        _, util = max_action_value(child)

        if util < min_util:
            min_util = util
            best_action = index

    return (best_action, min_util)


game_tree = [2, [-3, 1], 4, 1]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)

game_tree = 3

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)


game_tree = [1, 2, [3]]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)