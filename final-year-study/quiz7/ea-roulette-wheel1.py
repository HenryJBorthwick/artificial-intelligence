# ea
# compute fitness
# compute cum_fit
# compute total fitness
# compute norm_cum_fit
# select r < norm_cum_fit

def roulette_wheel_select(population, fitness, r):
    # compute fitness
    fitnesses = []
    for individual in population:
        fitnesses.append(fitness(individual))
    
    # compute cum fit
    cum_fit = []
    total_cum_fit = 0
    for fv in fitnesses:
        total_cum_fit += fv
        cum_fit.append(total_cum_fit)

    # compute norm cum fit
    norm_cum_fit = []
    total_fit = sum(fitnesses)
    for cf in cum_fit:
        norm_cum_fit.append(cf / total_fit)
    
    # select r < norm_cum_fit
    for individual, norm_cum_fit_val in zip(population, norm_cum_fit):
        if r < norm_cum_fit_val:
            return individual


# population = ['a', 'b']

# def fitness(x):
#     return 1 # everyone has the same fitness

# for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
#     print(roulette_wheel_select(population, fitness, r))


population = [0, 1, 2]

def fitness(x):
    return x

for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))