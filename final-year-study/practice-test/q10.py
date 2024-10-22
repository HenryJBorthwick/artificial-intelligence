def select(population, error, max_error, r):

    # convert error into fitness
    fitness_values = []
    for individual in population:
        fit = max_error - error(individual)
        fitness_values.append(fit)

    # compute total fitness
    total_fitness = sum(fitness_values)

    # calculate cumulative probabilities
    cumulative_fitness_prop = []
    cumulative_fit_sum = 0
    for fit in fitness_values:
        cumulative_fit_sum += fit
        cumulative_fitness_prop.append(cumulative_fit_sum / total_fitness)
    
    # select individual based on random number
    for individual, cumulative_prob in zip(population, cumulative_fitness_prop):
        if r < cumulative_prob:
            return individual
        


# TEST
population = ['a', 'b']

def error(x):
    return {'a': 14,
            'b': 12}[x]

max_error = 15

for r in [0, 0.1, 0.24, 0.26, 0.5, 0.9]:
    print(select(population, error, max_error, r))

# since the fitness of 'a' is 1 and the fitness of 'b' is 3,
# for r's below 0.25 we get 'a', for r's above it we get 'b'.


# Q7 Quiz 7 Evolutionary algorithm implementation
# def roulette_wheel_select(population, fitness, r):
#     # create list of fitness values for each individual in the population
#     individuals_fitness = [fitness(individual) for individual in population]

#     # sum all the fitnesses
#     total_fitness = sum(individuals_fitness)

#     # calculate cumulative probabilities
#     cumulative_fitness = []
#     cumulative_fitness_sum = 0

#     for fv in individuals_fitness:
#         cumulative_fitness_sum += fv
#         cumulative_fitness.append(cumulative_fitness_sum)

#     # normalize cumulative probabilities (get between 0 and 1)
#     probabilites = [cf / total_fitness for cf in cumulative_fitness]
    
#     # iterate through selection
#     for individual, cumulative_probability in zip(population, probabilites):
#         if r < cumulative_probability:
#             return individual