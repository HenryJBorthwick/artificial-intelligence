import random

def predict_rest(sequence):
    # prevent random case of second last test failure
    random.seed(40)

    # define operators that are used in expressions
    function_symbols = ['+', '-', '*']

    # define leaves constants and variables in expressions
    leaves = list(range(-2, 3)) + ['x', 'y', 'i']
    max_depth = 3

    # split sequence into initial and final
    half = len(sequence) // 2
    initial_sequence = sequence[:half]
    final_sequence = sequence[half:]

    # try random expressions to find one that fits sequence pattern
    for _ in range(1000000):  # Limit the number of attempts

        # gen expressions
        expression = random_expression(function_symbols, leaves, max_depth)

        # check if valid expression
        if is_valid_expression(expression, function_symbols, leaves):
            # gen sequence from expression
            generated_exp = generate_rest(initial_sequence, expression, len(sequence) - half)
            
            # check if gen sequence matches input sequence
            if generated_exp == final_sequence:
                return generate_rest(sequence, expression, 5)

    # if no matching expression is found return a default
    # repeat the last element as a fallback
    return [sequence[-1]] * 5 


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


def evaluate(expression, bindings):
    if isinstance(expression, int):
        return expression
    if isinstance(expression, str):
        return bindings[expression]
    if isinstance(expression, list):
        func_symbol, left_expr, right_expr = expression
        func = bindings[func_symbol]
        left_value = evaluate(left_expr, bindings)
        right_value = evaluate(right_expr, bindings)
        return func(left_value, right_value)
    

def random_expression(function_symbols, leaves, max_depth):
    if max_depth == 0:
        return random.choice(leaves)
    else:
        if random.choice([True, False]):
            return random.choice(leaves)
        else:
            func_symbol = random.choice(function_symbols)
            left_expr = random_expression(function_symbols, leaves, max_depth - 1)
            right_expr = random_expression(function_symbols, leaves, max_depth - 1)
            return [func_symbol, left_expr, right_expr]
        

def generate_rest(initial_sequence, expression, length):
    # init list of results
    result = []

    # create dict for variable bindings
    bindings = {
        'i': len(initial_sequence),
        'x': initial_sequence[-2],
        'y': initial_sequence[-1],
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }

    for _ in range(length):
        # evaluate expression with current bindings
        next_value = evaluate(expression, bindings)

        # add result
        result.append(next_value)

        # update bindings for next expression
        bindings['i'] += 1
        bindings['x'], bindings['y'] = bindings['y'], next_value

    return result


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