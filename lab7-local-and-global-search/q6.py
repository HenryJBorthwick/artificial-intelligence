def roulette_wheel_select(population, fitness, r):
    # create list of fitness values for each individual in the population
    individuals_fitness = [fitness(individual) for individual in population]

    # sum all the fitnesses
    total_fitness = sum(individuals_fitness)

    # calculate cumulative probabilities
    cumulative_fitness = []
    cumulative_fitness_sum = 0

    for fv in individuals_fitness:
        cumulative_fitness_sum += fv
        cumulative_fitness.append(cumulative_fitness_sum)

    # normalize cumulative probabilities (get between 0 and 1)
    probabilites = [cf / total_fitness for cf in cumulative_fitness]
    
    # iterate through selection
    for individual, cumulative_probability in zip(population, probabilites):
        if r < cumulative_probability:
            return individual

# tests
population = ['a', 'b']

def fitness(x):
    return 1 # everyone has the same fitness

for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
    print(roulette_wheel_select(population, fitness, r))

print("\n")

population = [0, 1, 2]

def fitness(x):
    return x

for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))