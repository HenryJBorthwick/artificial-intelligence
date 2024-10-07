def attach(expression1, expression2, position):
    def _attach_helper(expr, new_subexpr, target_position, current_position):
        if current_position == target_position:
            return new_subexpr, current_position + 1
        if isinstance(expr, (int, str)):
            return expr, current_position + 1
        if isinstance(expr, list):
            func_symbol = expr[0]
            # visit root node (current_position already counted)
            # traverse left subtree
            left_expr, next_position = _attach_helper(expr[1], new_subexpr, target_position, current_position + 1)
            # traverse right subtree
            right_expr, final_position = _attach_helper(expr[2], new_subexpr, target_position, next_position)
            return [func_symbol, left_expr, right_expr], final_position
    modified_expr, _ = _attach_helper(expression1, expression2, position, 0)
    return modified_expr


# HELPER FUNCTION
def _attach_helper(expr, new_subexpr, target_position, current_position):
    # base case, if current position matches the target
    if current_position == target_position:
        # replace the current node with the new_subexpr
        return new_subexpr, current_position + 1
    
    # if the expression is a leaf node
    if isinstance(expr, (int, str)):
        # no further traversal needed
        return expr, current_position + 1
    
    # if the expression is a function node
    if isinstance(expr, list):
        # visit the root node (already done)
        # traverse the left subtree
        left_expr, next_position = _attach_helper(expr[1], new_subexpr, target_position, current_position + 1)
        # traverse the right subtree
        right_expr, final_position = _attach_helper(expr[2], new_subexpr, target_position, next_position)
        # reconstruct the expression with possibly modified subtrees
        return [expr[0], left_expr, right_expr], final_position


# TESTS
expression1 = ['+', 'a', 'b']
expression2 = 'x'
position = 1
print(attach(expression1, expression2, position))

print("\n")

expression1 = ['+', 'a', 'b']
expression2 = ['-', 'x', 'y']
position = 2
print(attach(expression1, expression2, position))

print("\n")

expression = ['*', 'x', ['+', 'y', 1]]
subtree = ['-', 'a', 'b']
position = 1
print("Expression:", expression)
print("New subtree:", subtree)
print(f"Subtree attached at position {position}:", attach(expression, subtree, position))

print("\n")

expression = ['*', 'x', ['+', 'y', 1]]
subtree = ['-', 'a', 'b']
position = 3
print("Expression:", expression)
print("New subtree:", subtree)
print(f"Subtree attached at position {position}:", attach(expression, subtree, position))

print("\n")

expression = 'a'
subtree = 'b'
position = 0
print("Expression:", expression)
print("New subtree:", subtree)
print(f"Subtree attached at position {position}:", attach(expression, subtree, position))

print("\n")

expression = ['+', ['g', 3, 4], ['f', 'x', 2]]
sub_expression = ['h', 'i', 'j']

for position in range(7):
    print(f"Attached at position {position}:", attach(expression, sub_expression, position))


