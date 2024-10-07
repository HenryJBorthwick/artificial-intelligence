import random

def random_expression(function_symbols, leaves, max_depth):
    # base case, if max_depth is 0, return a random leaf node
    if max_depth == 0:
        return random.choice(leaves)
    else:
        # decide randomly whether to return a leaf or a function application
        # increase probability of leaves as we reach max_depth
        if random.choice([True, False]):
            return random.choice(leaves)
        else:
            # recursive case, create a function application
            func_symbol = random.choice(function_symbols)
            left_expr = random_expression(function_symbols, leaves, max_depth - 1)
            right_expr = random_expression(function_symbols, leaves, max_depth - 1)
            return [func_symbol, left_expr, right_expr]


# HELPER FUNCTIONS
def is_valid_expression(obj, function_symbols, leaf_symbols):
    if isinstance(obj, int):
        return True
    if obj in leaf_symbols:
        return True
    if isinstance(obj, list):
        if len(obj) != 3:
            return False
        func, arg1, arg2 = obj
        if not isinstance(func, str) or func not in function_symbols:
            return False
        return (is_valid_expression(arg1, function_symbols, leaf_symbols) and
                is_valid_expression(arg2, function_symbols, leaf_symbols))
    return False


def depth(expression):
    if isinstance(expression, (int, str)):
        return 0
    elif isinstance(expression, list):
        left_depth = depth(expression[1])
        right_depth = depth(expression[2])
        return 1 + max(left_depth, right_depth)
    else:
        return 0


# TEST VALID
# All the generated expressions must be valid
function_symbols = ['f', 'g', 'h']
constant_leaves =  list(range(-2, 3))
variable_leaves = ['x', 'y', 'i']
leaves = constant_leaves + variable_leaves
max_depth = 4

for _ in range(10000):
    expr = random_expression(function_symbols, leaves, max_depth)
    if not is_valid_expression(expr, function_symbols, leaves):
        print("Invalid expression:", expr)
        break
else:
    print("All expressions are valid.")


# TEST DISTINCTIVE
function_symbols = ['f', 'g', 'h']
leaves = ['x', 'y', 'i'] + list(range(-2, 3))
max_depth = 4

expressions = [random_expression(function_symbols, leaves, max_depth)
               for _ in range(10000)]

# Out of 10000 expressions, at least 1000 must be distinct
expressions = [str(random_expression(function_symbols, leaves, max_depth))
               for _ in range(10000)]
distinct_expressions = set(expressions)
if len(distinct_expressions) >= 1000:
    print("Sufficiently diverse expressions.")
else:
    print("Not enough distinct expressions.")


# TEST DIVERSITY
function_symbols = ['f', 'g', 'h']
leaves = ['x', 'y', 'i'] + list(range(-2, 3))
max_depth = 4

expressions = [random_expression(function_symbols, leaves, max_depth)
               for _ in range(10000)]

# Out of 10000 expressions, there must be at least 100 expressions
# of depth 0, 100 of depth 1, ..., and 100 of depth 4.
depth_counts = {}
for expr in expressions:
    expr_depth = depth(expr)
    depth_counts[expr_depth] = depth_counts.get(expr_depth, 0) + 1

for d in range(max_depth + 1):
    if depth_counts.get(d, 0) >= 100:
        print(f"At least 100 expressions of depth {d}.")
    else:
        print(f"Not enough expressions of depth {d}.")
