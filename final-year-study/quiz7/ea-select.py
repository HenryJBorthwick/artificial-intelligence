# compute fitness
# sum fitness
# compute cumulative fitness
# compute normalized cumulative fitness
# select fit

# fitness
# low error is better 
# error functions returns error
# max error is the highest possible error
# the fitness of a maximum error antenna is zero
# therefore, higher fitness is better, so a lower error antenna produces a high fitness value
# thus it is the max - the antennas error

def select(population, error, max_error, r):
    # compute fitness
    fitnesses = []
    for individual in population:
        fitnesses.append((max_error - error(individual)))
    
    # sum fitness
    fitness_sum = sum(fitnesses)

    # compute cumulative fitness
    cumulative_fitness = []
    cumulative_fitness_sum = 0
    for fv in fitnesses:
        cumulative_fitness_sum += fv
        cumulative_fitness.append(cumulative_fitness_sum)
    
    # compute normalized cumulative fitness
    norm_cum_fitness = []
    for cf in cumulative_fitness:
        norm_cum_fitness.append(cf / fitness_sum)

    # select fit
    for individual, norm_cum_fit in zip(population, norm_cum_fitness):
        if r < norm_cum_fit:
            return individual
        

population = ['a', 'b']

def error(x):
    return {'a': 14,
            'b': 12}[x]

max_error = 15

for r in [0, 0.1, 0.24, 0.26, 0.5, 0.9]:
    print(select(population, error, max_error, r))

# since the fitness of 'a' is 1 and the fitness of 'b' is 3,
# for r's below 0.25 we get 'a', for r's above it we get 'b'.