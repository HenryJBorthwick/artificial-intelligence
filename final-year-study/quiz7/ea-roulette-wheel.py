def roulette_wheel_select(population, fitness, r):
    # compute fitness
    individuals_fitness = []
    for individual in population:
        individuals_fitness.append(fitness(individual))

    # sum fitnesses
    total_fitness = sum(individuals_fitness)

    # compute cumulative fitness
    cumulative_fitness = []
    cumulative_fitness_sum = 0
    for fv in individuals_fitness:
        cumulative_fitness_sum += fv
        cumulative_fitness.append(cumulative_fitness_sum)

    # normalize cumulative fitness
    normalize_cumulative_fitness = []
    for cf in cumulative_fitness:
        normalize_cumulative_fitness.append(cf / total_fitness)

    # selection
    for individual, norm_cum_fitness in zip(population, normalize_cumulative_fitness):
        if r < norm_cum_fitness:
            return individual

# compute fitness
# sum fitness
# compute cumulative fitness
# compute normalized cumulative fitness
# select fit

    
population = ['a', 'b']

def fitness(x):
    return 1 # everyone has the same fitness

for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
    print(roulette_wheel_select(population, fitness, r))


population = [0, 1, 2]

def fitness(x):
    return x

for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))