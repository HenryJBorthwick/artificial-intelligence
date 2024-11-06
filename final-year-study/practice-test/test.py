# knn:
# Compute distance between input and input data
# Add to distance, output data tuple
# sort distances
# get k_neighbors from distance
# tie break k_neighbors, update their distances
# extract distance, output data from k_neighbors and compute outcomes
# use function/combine to compute prediction

def estimate(time, observations, k):
    # compute distance
    distances = []
    for data_input, data_output in observations:
        dist = abs(time-data_input)
        distances.append((dist, data_output))

    # sort distances
    distances.sort()

    # get k_neighbors from distance
    k_neighbors = distances[:k]

    # tie break k_neighbors and add distances
    index = k
    while index < len(distances) and distances[index][0] == distances[k-1][0]:
        k_neighbors.append(distances[index])
        index += 1

    # extract output from k_neighbors
    output = []
    for time_distances, temp_data in k_neighbors:
        output.append(temp_data)

    # compute final prediction for temp
    prediction = sum(output) / len(output)

    return prediction


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