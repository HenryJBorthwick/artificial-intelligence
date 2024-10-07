def is_valid_expression(obj, function_symbols, leaf_symbols):
    # Base case: Check if the object is an integer (constant leaf)
    if isinstance(obj, int):
        return True
    
    # Base case: Check if the object is in the set of variable leaves
    if obj in leaf_symbols:
        return True
    
    # Recursive case: Check if the object is a valid function application
    if isinstance(obj, list):
        # Must have exactly three elements
        if len(obj) != 3:
            return False
        func, arg1, arg2 = obj
        # The first element must be a string in function_symbols
        if not isinstance(func, str) or func not in function_symbols:
            return False
        # Recursively validate the arguments
        return (is_valid_expression(arg1, function_symbols, leaf_symbols) and
                is_valid_expression(arg2, function_symbols, leaf_symbols))
    
    # If none of the above, it's not a valid expression
    return False



# TESTS
function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = 1

print(is_valid_expression(expression, function_symbols, leaf_symbols))


function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = 'y'

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))


function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = 2.0

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))


function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['f', 123, 'x']

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))


function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['f', ['+', 0, -1], ['f', 1, 'x']]

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))


function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['+', ['f', 1, 'x'], -1]

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))


function_symbols = ['f', '+']
leaf_symbols = ['x', 'y', -1, 0, 1]
expression = ['f', 0, ['f', 0, ['f', 0, ['f', 0, 'x']]]]

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))


function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = 'f'

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))


function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['f', 1, 0, -1]

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))


function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['x', 0, 1]

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))


function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['g', 0, 'y']

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))
