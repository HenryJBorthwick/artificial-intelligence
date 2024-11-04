def estimate(time, observations, k):
    # compute distance
    distances = []
    for obs_time, obs_temperature in observations:
        dist = abs(time - obs_time)
        distances.append((dist, obs_temperature))

    # sort distances
    distances.sort()

    # select k neighbors
    selected_neighbors = distances[:k]
        
    # tie break
    index = k
    while index < len(distances) and distances[index][0] == distances[k-1][0]:
        selected_neighbors.append(distances[index])
        index += 1

    # extract outputs and temp perform function (average temp in this case)
    outputs = []
    for dist, obs_temperature in selected_neighbors:
        outputs.append(obs_temperature)

    # average = total / length
    average_temp = sum(outputs) / len(outputs)

    return average_temp

# knn
# compute distance, use provided function if needed
# sort distance
# select k neighbors
# tie break
# extract selected neighbors, apply function or compute output


observations = [
    (-1, 1),
    (0, 0),
    (-1, 1),
    (5, 6),
    (2, 0),
    (2, 3),
]

for time in [-1, 1, 3, 3.5, 6]:
    print(estimate(time, observations, 2))


observations = [
    (-1, 1),
    (0, 0),
    (-1, 1),
    (5, 6),
    (2, 0),
    (2, 3),
]

for time in [-1, 1, 3, 3.5, 6]:
    print("{:1.3}".format(estimate(time, observations, 10)))