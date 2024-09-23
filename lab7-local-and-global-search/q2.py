def n_queens_cost(state):
    # size of board, from number of queens (number of elements in tuple)
    n = len(state)

    # conflict counter
    conflicts = 0

    # iterate through pairs of queens
    for col1 in range(n):
        # tuple index
        row1 = state[col1]

        for col2 in range(col1 + 1, n):
            row2 = state[col2]

            # check diagonal conflict
            # col1 - col2 = horizontal distance between pair queens
            # row1 - row2 = vertical distance between pair queens
            if abs(col1 - col2) == abs(row1 - row2):
                conflicts += 1

    return conflicts

# test
print(n_queens_cost((1, 2)))

print(n_queens_cost((1, 3, 2)))

print(n_queens_cost((1, 2, 3)))

print(n_queens_cost((1,)))

print(n_queens_cost((1, 2, 3, 4, 5, 6, 7, 8)))

print(n_queens_cost((2, 3, 1, 4)))