def evaluate(expression, bindings):
    # base case, if the expression is an integer
    if isinstance(expression, int):
        return expression
    
    # if the expression is a variable name retrieve its value from bindings
    elif isinstance(expression, str):
        if expression in bindings:
            return bindings[expression]

    # recursive case, the expression is a list representing an operation
    elif isinstance(expression, list):
        # the operator ('+', '-', or '*')
        operator = expression[0]
        # left operand
        left_expr = expression[1]
        # right operand
        right_expr = expression[2]

        # recursively evaluate the left and right operands
        left_operand = evaluate(left_expr, bindings)
        right_operand = evaluate(right_expr, bindings)

        # perform operations based on operator
        if operator == '+':
            return left_operand + right_operand
        elif operator == '-':
            return left_operand - right_operand
        elif operator == '*':
            return left_operand * right_operand


# HELPER FUNCTION
def generate_rest(initial_sequence, expression, length):
    result = []
    x = initial_sequence[-2]
    y = initial_sequence[-1]
    seq_len = len(initial_sequence)
    for k in range(length):
        i = seq_len + k
        bindings = {'x': x, 'y': y, 'i': i}
        value = evaluate(expression, bindings)
        result.append(value)
        x, y = y, value
    return result


# TESTS
initial_sequence = [0, 1, 2]
expression = 'i' 
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression,
                    length_to_generate))

print("\n")

# no particular pattern, just an example expression
initial_sequence = [-1, 1, 367]
expression = 'i' 
length_to_generate = 4
print(generate_rest(initial_sequence,
                    expression,
                    length_to_generate))

print("\n")

initial_sequence = [4, 6, 8, 10]
expression = ['*', ['+', 'i', 2], 2]
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))

print("\n")

initial_sequence = [4, 6, 8, 10]
expression = ['+', 2, 'y']
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))

print("\n")

initial_sequence = [0, 1]
expression = 'x'
length_to_generate = 6
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))

print("\n")

# Fibonacci sequence
initial_sequence = [0, 1]
expression = ['+', 'x', 'y']
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))

print("\n")

initial_sequence = [367, 367, 367]
expression = 'y'
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))

print("\n")

# no pattern, just a demo
initial_sequence = [0, 1, 2]
expression = -1 
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))

print("\n")

initial_sequence = [0, 1, 2]
expression = 'i'
length_to_generate = 0
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))
