import random


def n_queens_neighbours(state):
    n = len(state)
    neighbours = []

    for i in range(n):
        for j in range(i + 1, n):
            state_list = list(state)
            state_list[i], state_list[j] = state_list[j], state_list[i]
            new_state = tuple(state_list)
            neighbours.append(new_state)

    neighbours = sorted(neighbours)
    return neighbours


def n_queens_cost(state):
    n = len(state)
    conflicts = 0

    for col1 in range(n):
        row1 = state[col1]
        for col2 in range(col1 + 1, n):
            row2 = state[col2]

            if abs(col1 - col2) == abs(row1 - row2):
                conflicts += 1

    return conflicts


def greedy_descent(initial_state, neighbours_func, cost):
    path = [initial_state]

    while True:
        current_state = path[-1]
        current_state_cost = cost(current_state)

        neighbor_states = neighbours_func(current_state)
        if not neighbor_states:
            break

        best_neighbour = min(neighbor_states, key=cost)
        best_neighbour_cost = cost(best_neighbour)

        if best_neighbour_cost < current_state_cost:
            path.append(best_neighbour)
        else:
            break

    return path


def greedy_descent_with_random_restart(random_state, neighbours_func, cost):
    while True:
        # Get random state and print
        current_state = random_state()
        print(current_state)

        # Perform greedy descent function
        path = greedy_descent(current_state, neighbours_func, cost)

        # Print each state from path returned from greedy descent
        # Exclude the initial state as it's already printed
        for state in path[1:]:
            print(state)

        # Check for solution
        final_state = path[-1]
        final_state_cost = cost(final_state)

        if final_state_cost == 0:
            # Solution found
            break
        else:
            # Restart as local minimum is not a solution
            print("RESTART")


# Tests
N = 6
random.seed(0)


def random_state():
    return tuple(random.sample(range(1, N + 1), N))


greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)

print("\n")

N = 8
random.seed(0)


def random_state():
    return tuple(random.sample(range(1, N + 1), N))


greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)
