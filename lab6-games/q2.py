def max_action_value(tree):
    # Base case: If the tree is a terminal node (leaf), return None for the action and the utility
    if isinstance(tree, int):
        return None, tree

    # Recursive case: If the tree is a list of subtrees, evaluate them and select the max utility
    else:
        best_action = None
        best_value = float('-inf')

        for i, subtree in enumerate(tree):
            _, subtree_value = min_action_value(subtree)  # Maximizer assumes next level is minimizing
            if subtree_value > best_value:
                best_value = subtree_value
                best_action = i

        return best_action, best_value

def min_action_value(tree):
    # Base case: If the tree is a terminal node (leaf), return None for the action and the utility
    if isinstance(tree, int):
        return None, tree

    # Recursive case: If the tree is a list of subtrees, evaluate them and select the min utility
    else:
        best_action = None
        best_value = float('inf')

        for i, subtree in enumerate(tree):
            _, subtree_value = max_action_value(subtree)  # Minimizer assumes next level is maximizing
            if subtree_value < best_value:
                best_value = subtree_value
                best_action = i

        return best_action, best_value
    

# test1
game_tree = [2, [-3, 1], 4, 1]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)

# result1
# Best action if playing min: 1
# Best guaranteed utility: 1

# Best action if playing max: 2
# Best guaranteed utility: 4


# test2
game_tree = 3

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)

# result2
# Best action if playing min: None
# Best guaranteed utility: 3

# Best action if playing max: None
# Best guaranteed utility: 3


# test3
game_tree = [1, 2, [3]]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)

# result3
# Best action if playing min: 0
# Best guaranteed utility: 1

# Best action if playing max: 2
# Best guaranteed utility: 3

# test answers
game_tree = [2, [-1, 5], [1, 3], 4]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)