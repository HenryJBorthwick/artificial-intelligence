def greedy_descent(inital_state, neighbours, cost):

    # keep track of visited states
    path = []

    # initialize path with initial state
    path.append(inital_state)

    # greedy loop
    while True:
        # get current state from path, being the end state from list
        current_state = path[-1]
        # get current states path cost using cost function
        current_state_cost = cost(current_state)

        # get list of neighbouring states for current state
        neighbour_states = neighbours(current_state)
        #no neighbours check
        if not neighbour_states:
            break

        # get lowest cost neighbour using min and key cost function
        best_neighbour = min(neighbour_states, key=cost)

        # once you have the best neighbour, get the cost of that neighbour
        best_neighbour_cost = cost(best_neighbour)

        # move to neighbour if lower cost neighbour
        if best_neighbour_cost < current_state_cost:
            path.append(best_neighbour)
        else:
            # no neighbour has lower cost, exit loop reached local minimum
            break

    # return path of states
    return path

# tests
def cost(x):
    return x**2

def neighbours(x):
    return [x - 1, x + 1]

for state in greedy_descent(4, neighbours, cost):
    print(state)

for state in greedy_descent(-6.75, neighbours, cost):
    print(state)