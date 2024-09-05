def max_value(tree):
    # base case: tree is terminal node return utility
    if isinstance(tree, int):
        return tree
    else:
        # recursive case: tree is list of children, return max value of children
        return max(min_value(child) for child in tree)
    
def min_value(tree):
    # base case: tree is terminal node, return utility
    if isinstance(tree, int):
        return tree
    else:
        # recursive case: tree is list of children, return min value of children
        return min(max_value(child) for child in tree)


# test1
game_tree = 3

print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))

# result1
# Root utility for minimiser: 3
# Root utility for maximiser: 3


# test2
game_tree = [1, 2, 3]

print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))

# result2
# Root utility for minimiser: 1
# Root utility for maximiser: 3


# test3
game_tree = [1, 2, [3]]

print(min_value(game_tree))
print(max_value(game_tree))

# result3
# 1
# 3


# test4
game_tree = [[1, 2], [3]]

print(min_value(game_tree))
print(max_value(game_tree))

# result4
# 2
# 3
