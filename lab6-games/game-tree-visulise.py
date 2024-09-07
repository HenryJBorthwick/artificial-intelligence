def print_game_tree(tree, depth=0, is_max=True):
    """ Recursively prints the game tree with alternating min/max layers.
    
    Parameters:
    - tree: list representing the game tree
    - depth: current depth of the tree (used for indentation)
    - is_max: boolean flag indicating whether the current layer is a max layer
    """
    indent = "  " * depth  # indentation based on depth
    layer_type = "MAX" if is_max else "MIN"
    
    if isinstance(tree, list):
        print(f"{indent}{layer_type} Layer:")
        for subtree in tree:
            print_game_tree(subtree, depth + 1, not is_max)  # alternate between min and max layers
    else:
        # Leaf node
        print(f"{indent}{tree}")
        

# q3
# game_tree = [2, [-1, 5], [1, 3], 4]


# q5
game_tree = [3, [[2, 1], [4, [7, -2]]], 0]

# Print the game tree with min/max layers
print_game_tree(game_tree)
