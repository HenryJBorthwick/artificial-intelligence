import random


def n_queens_neighbours(state):
    n = len(state)
    neighbours = []

    for i in range(n):
        for j in range(i + 1, n):
            state_list = list(state)

            state_list[i], state_list[j] = state_list[j], state_list[i]

            state_tuple = tuple(state_list)

            neighbours.append(state_tuple)

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


def greedy_descent(initial_state, neighbours, cost):
    path = []
    path.append(initial_state)

    while True:
        current_state = path[-1]
        current_state_cost = cost(current_state)

        neighbour_states = neighbours(current_state)
        if not neighbour_states:
            break

        best_neighbour = min(neighbour_states, key=cost)
        best_neighbour_cost = cost(best_neighbour)

        if best_neighbour_cost < current_state_cost:
            path.append(best_neighbour)
        else:
            break

    return path


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    while True:
        # Get random state and print
        current_state = random_state()
        print(current_state)

        # perform greedy descent function
        path = greedy_descent(current_state, neighbours, cost)

        # print each state from path returned from greedy algorithm
        # exclude initial state or current state as already printed
        for state in path[1:]:
            print(state)

        # check for soultion
        # get last state from path
        final_state = path[-1]
        # get final states cost
        final_state_cost = cost(final_state)

        # check if cost is final
        if final_state_cost == 0:
            # soultion found
            break
        else:
            # Restart as local minimum is not soultion
            print("RESTART")


# tests
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
    return tuple(random.sample(range(1,N+1), N))

greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)