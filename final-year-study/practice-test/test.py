def estimate(time, observations, k):
    # compute distance from input and data input
    distances = []
    for data_input_time, data_output_temperature in observations:
        # add using distance, data output tuples
        # FORGOT abs()
        dist = abs(time - data_input_time)
        distances.append((dist, data_output_temperature))

    # FORGOT THIS
    distances.sort()

    # get k_neighbors
    k_neighbors = distances[:k]

    # tie break k_neighbors distance
    index = k
    while index < len(distances) and distances[index][0] == distances[k-1][0]:
        k_neighbors.append(distances[index])
        #FORGOT THIS
        index += 1
    
    # loop through k_neighbors and generate output
    outputs = []
    for distances, data_output_tempe in k_neighbors:
        outputs.append(data_output_tempe)

    # compute temperature estimate from k_neighbors
    prediction = sum(outputs) / len(outputs)

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