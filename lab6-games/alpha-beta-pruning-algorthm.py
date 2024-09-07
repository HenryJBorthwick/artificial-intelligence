def alpha_beta_search_max(tree):
    """Performs Alpha-Beta Pruning on a given game tree, starting with a maximizer at the root."""
    pruned_tree, pruning_events = max_value(tree, float('-inf'), float('inf'), [])
    return pruned_tree, pruning_events

def alpha_beta_search_min(tree):
    """Performs Alpha-Beta Pruning on a given game tree, starting with a minimizer at the root."""
    pruned_tree, pruning_events = min_value(tree, float('-inf'), float('inf'), [])
    return pruned_tree, pruning_events

def max_value(tree, alpha, beta, pruning_events):
    """Maximizer's move in the Alpha-Beta Pruning algorithm for a game tree."""
    if isinstance(tree, int):  # Leaf node
        return tree, pruning_events

    v = float('-inf')
    pruned_tree = []
    for subtree in tree:
        min_value_result, pruning_events = min_value(subtree, alpha, beta, pruning_events)
        if isinstance(min_value_result, list):  # Skip if it's a subtree
            v = max(v, max(map(lambda x: x if isinstance(x, int) else float('-inf'), min_value_result)))
        else:
            v = max(v, min_value_result)
        pruned_tree.append(min_value_result)
        alpha = max(alpha, v)
        if alpha >= beta:
            pruning_events.append((alpha, beta))
            return pruned_tree, pruning_events  # Prune remaining branches
    return pruned_tree, pruning_events

def min_value(tree, alpha, beta, pruning_events):
    """Minimizer's move in the Alpha-Beta Pruning algorithm for a game tree."""
    if isinstance(tree, int):  # Leaf node
        return tree, pruning_events

    v = float('inf')
    pruned_tree = []
    for subtree in tree:
        max_value_result, pruning_events = max_value(subtree, alpha, beta, pruning_events)
        if isinstance(max_value_result, list):  # Skip if it's a subtree
            v = min(v, min(map(lambda x: x if isinstance(x, int) else float('inf'), max_value_result)))
        else:
            v = min(v, max_value_result)
        pruned_tree.append(max_value_result)
        beta = min(beta, v)
        if alpha >= beta:
            pruning_events.append((alpha, beta))
            return pruned_tree, pruning_events  # Prune remaining branches
    return pruned_tree, pruning_events


# q3
tree = [2, [-1, 5], [1, 3], 4]
pruned_tree, pruning_events = alpha_beta_search_max(tree)

print("pruned game tree:", pruned_tree)
print("pruning events:", pruning_events)

# q5
tree = [3, [[2, 1], [4, [7, -2]]], 0]
pruned_tree, pruning_events = alpha_beta_search_min(tree)

print("pruned game tree:", pruned_tree)
print("pruning events:", pruning_events)