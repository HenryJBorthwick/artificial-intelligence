from math import inf

# Minimax-Decision: Returns the best action for the Max player

def minimax_decision_max(game_tree):

    # Handle terminal node case (single number)
    if isinstance(game_tree, int):
        return None, game_tree  # No action, return the terminal value
    

    best_action = None
    best_value = -inf  # Start with -∞ for maximizer

    # Process each action (child) of the root
    for i, subtree in enumerate(game_tree):
        value = min_value(subtree)  # Min player plays next
        if value > best_value:
            best_value = value
            best_action = i  # Store the index of the best action
    
    return best_action, best_value


# Minimax-Decision: Returns the best action for the Min player
def minimax_decision_min(game_tree):
    # Handle terminal node case (single number)
    if isinstance(game_tree, int):
        return None, game_tree  # No action, return the terminal value
    
    best_action = None
    best_value = inf  # Start with +∞ for the minimizer

    # Process each action (child) of the root (Min node)
    for i, subtree in enumerate(game_tree):
        value = max_value(subtree)  # Max player plays next
        if value < best_value:
            best_value = value
            best_action = i  # Store the index of the best action
    
    return best_action, best_value



# Max-Value: Returns the utility value for the Max player
def max_value(state):
    if isinstance(state, int):  # Terminal-Test: If it's a leaf node
        return state

    v = -inf  # Start with -∞
    for child in state:
        v = max(v, min_value(child))  # Max player chooses the highest value
    return v

# Min-Value: Returns the utility value for the Min player
def min_value(state):
    if isinstance(state, int):  # Terminal-Test: If it's a leaf node
        return state

    v = inf  # Start with +∞
    for child in state:
        v = min(v, max_value(child))  # Min player chooses the lowest value
    return v


# Test the implementation with the given tree
game_tree = [1, 2, [3]]

# Min root
best_min_action, best_min_value = minimax_decision_min(game_tree)

print("Best action for Min:", best_min_action)
print("Best guaranteed utility for Min:", best_min_value)

# Max root
best_max_action, best_max_value = minimax_decision_max(game_tree)

print("Best action for Max:", best_max_action)
print("Best guaranteed utility for Max:", best_max_value)

