import operator
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


# TESTS
bindings = {}
expression = 12
print(evaluate(expression, bindings))

bindings = {'x':5, 'y':10, 'time':15}
expression = 'y'
print(evaluate(expression, bindings))

bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
expression = ['add', 12, 'x']
print(evaluate(expression, bindings))

bindings = dict(x = 5, y = 10, blah = 15, add = operator.add)
expression = ['add', ['add', 22, 'y'], 'x']
print(evaluate(expression, bindings))