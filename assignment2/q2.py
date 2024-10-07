def depth(expression):
    # base case, if the expression is a leaf node (int or str), depth is 0
    if isinstance(expression, (int, str)):
        return 0
    # recursive case, if the expression is a list (function application)
    elif isinstance(expression, list):
        # recursively compute the depth of the left and right sub-expressions
        left_depth = depth(expression[1])
        right_depth = depth(expression[2])
        # the depth is 1 plus the maximum depth of the sub-expressions
        return 1 + max(left_depth, right_depth)
    else:
        # if the expression is invalid, return 0 or raise an error
        return 0


# TESTS
expression = 12
print(depth(expression))

expression = 'weight'
print(depth(expression))

expression = ['add', 12, 'x']
print(depth(expression))

expression = ['add', ['add', 22, 'y'], 'x']
print(depth(expression))