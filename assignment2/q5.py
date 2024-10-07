import random

def prune(expression, max_depth, leaf_symbols, current_depth=0):

    # base case, if the expression is a leaf node, return it as is
    if isinstance(expression, (int, str)):
        return expression
    
    # depth check
    if current_depth == max_depth:
        # replace function node with a random leaf
        return random.choice(leaf_symbols)
    
    # recursive case, if the expression is a function node and depth is less than max_depth
    if isinstance(expression, list):
        func_symbol, left_expr, right_expr = expression
        # recursively prune the sub-expressions
        pruned_left = prune(left_expr, max_depth, leaf_symbols, current_depth + 1)
        pruned_right = prune(right_expr, max_depth, leaf_symbols, current_depth + 1)
        return [func_symbol, pruned_left, pruned_right]
    else:
        # in case of invalid expression (should not happen with valid inputs)
        return expression


# TESTS
expression = ['*', 'x', ['+', 'y', 1]]
max_depth = 1
pruned = prune(expression, max_depth, ['!'])
print("Expression: ", expression)
print("Pruned Expression: ", pruned)

expression = ['-', ['+', 'a', ['*', 'b', 'c']], ['*', ['+', 'x', 1], 'y']]
max_depth = 2
pruned = prune(expression, max_depth, ['!'])
print("Expression: ", expression)
print("Pruned Expression: ", pruned)

expression = ['+', 'x', 'z']
max_depth = 0
pruned = prune(expression, max_depth, ['!'])
print("Expression: ", expression)
print("Pruned Expression: ", pruned)

expression = 'a'
max_depth = 1
pruned = prune(expression, max_depth, ['!'])
print(expression)
print(pruned)