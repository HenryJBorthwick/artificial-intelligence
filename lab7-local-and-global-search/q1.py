def n_queens_neighbours(state):
    # size of board, from number of queens (number of elements in tuple)
    n = len(state)

    # neighbour states
    neighbours = []

    # from 0 to n-1
    for i in range(n):
        # from i+1 to n-1
        for j in range(i+1, n):
            # ensures that i<j, ensures each pair unique

            # convert state tuple to list which is mutable
            state_list = list(state)

            # swap elements in state
            state_list[i], state_list[j] = state_list[j], state_list[i]

            # covert swapped elements list back to tuple
            new_state = tuple(state_list)

            # add new state to neighbours
            neighbours.append(new_state)

    # sort the neighbours
    neighbours = sorted(neighbours)

    return neighbours

# test
print(n_queens_neighbours((1, 2, 3, 4, 5, 6, 7, 8)))