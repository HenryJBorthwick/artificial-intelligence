import random

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


def evaluate(expression, bindings):
    # base case, if the expression is an integer, return it
    if isinstance(expression, int):
        return expression

    # base case, if the expression is a variable (string), look up its value
    if isinstance(expression, str):
        return bindings[expression]

    # recursive case, if the expression is a function application (list)
    if isinstance(expression, list):
        # extract the function symbol and operands
        func_symbol, left_expr, right_expr = expression

        # look up the actual function in bindings
        func = bindings[func_symbol]

        # recursively evaluate the left and right operands
        left_value = evaluate(left_expr, bindings)
        right_value = evaluate(right_expr, bindings)

        # apply the function to the operands and return the result
        return func(left_value, right_value)
    

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
        

def generate_rest(initial_sequence, expression, length):
    result = []
    bindings = {
        'i': len(initial_sequence),
        'x': initial_sequence[-2],
        'y': initial_sequence[-1],
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }
    for _ in range(length):
        next_value = evaluate(expression, bindings)
        result.append(next_value)
        bindings['i'] += 1
        bindings['x'], bindings['y'] = bindings['y'], next_value
        
    return result


def predict_rest(sequence):
    function_symbols = ['+', '-', '*']
    leaves = list(range(-2, 3)) + ['x', 'y', 'i']
    max_depth = 3
    half = len(sequence) // 2
    initial_sequence = sequence[:half]
    final_sequence = sequence[half:]
    for _ in range(10000000000):  # Limit the number of attempts
        expression = random_expression(function_symbols, leaves, max_depth)
        if is_valid_expression(expression, function_symbols, leaves):
            try:
                generated_exp = generate_rest(initial_sequence, expression, len(sequence) - half)
                if generated_exp == final_sequence:
                    return generate_rest(sequence, expression, 5)
            except (ValueError, ZeroDivisionError):
                continue
    # If no matching expression is found, return a default
    return [sequence[-1]] * 5  # Repeat the last element as a fallback


# TESTS
# TESTS
sequence = [0, 1, 2, 3, 4, 5, 6, 7]
the_rest = predict_rest(sequence)
print("Test output:")
print(sequence)
print(the_rest)
print("Expected output:")
print("[0, 1, 2, 3, 4, 5, 6, 7]")
print("[8, 9, 10, 11, 12]")
print("\n")

sequence = [0, 2, 4, 6, 8, 10, 12, 14]
print("Test output:")
print(predict_rest(sequence))
print("Expected output:")
print("[16, 18, 20, 22, 24]")
print("\n")

sequence = [31, 29, 27, 25, 23, 21]
print("Test output:")
print(predict_rest(sequence))
print("Expected output:")
print("[19, 17, 15, 13, 11]")
print("\n")

sequence = [0, 1, 4, 9, 16, 25, 36, 49]
print("Test output:")
print(predict_rest(sequence))
print("Expected output:")
print("[64, 81, 100, 121, 144]")
print("\n")

sequence = [3, 2, 3, 6, 11, 18, 27, 38]
print("Test output:")
print(predict_rest(sequence))
print("Expected output:")
print("[51, 66, 83, 102, 123]")
print("\n")

sequence = [0, 1, 1, 2, 3, 5, 8, 13]
print("Test output:")
print(predict_rest(sequence))
print("Expected output:")
print("[21, 34, 55, 89, 144]")
print("\n")

sequence = [0, -1, 1, 0, 1, -1, 2, -1]
print("Test output:")
print(predict_rest(sequence))
print("Expected output:")
print("[5, -4, 29, -13, 854]")
print("\n")

sequence = [1, 3, -5, 13, -31, 75, -181, 437]
print("Test output:")
print(predict_rest(sequence))
print("Expected output:")
print("[-1055, 2547, -6149, 14845, -35839]")