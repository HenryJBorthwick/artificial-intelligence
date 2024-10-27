def estimate(time, observations, k):

    # compute distance
    distances = []
    for observation_time, temperature in observations:
        distance = abs(time - observation_time)
        distances.append((distance, temperature))
    
    # sort observations by distance
    distances.sort(key=lambda x: x[0])

    # select k nearest neighbors with tie handling
    # initial selection of k nearest neighbors
    k_neighbors = distances[:k]
    kth_distance = k_neighbors[-1][0]

    index = k
    while index < len(distances) and distances[index][0] == kth_distance:
        k_neighbors.append(distances[index])
        index += 1

    # average temperatures
    temperatures = []
    for _, temp in k_neighbors:
        temperatures.append(temp)
    
    estimated_temp = sum(temperatures) / len(temperatures)

    return estimated_temp


# test
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




# def knn_predict(input, examples, distance, combine, k):
#     # Compute distances between input and each example
#     distances = [(distance(input, ex_input), ex_output) for ex_input, ex_output in examples]
    
#     # Sort the distances
#     sorted_distances = sorted(distances, key=lambda x: x[0])
    
#     # Select the first k neighbors
#     k_neighbors = sorted_distances[:k]
#     kth_distance = k_neighbors[-1][0]
    
#     # Handle tie-breaking by including neighbors with equal distance
#     index = k
#     while index < len(sorted_distances) and sorted_distances[index][0] == kth_distance:
#         k_neighbors.append(sorted_distances[index])
#         index += 1
    
#     # Extract outputs from the selected neighbors
#     outputs = [output for _, output in k_neighbors]
    
#     # Combine outputs to make the final prediction
#     prediction = combine(outputs)
    
#     # Return the prediction
#     return prediction


# import math

# def euclidean_distance(v1, v2):
#     # Calculate squared differences and sum them
#     squared_diffs = [(a - b) ** 2 for a, b in zip(v1, v2)]
#     sum_of_squared_diffs = sum(squared_diffs)

#     # Compute the square root of the sum
#     distance = math.sqrt(sum_of_squared_diffs)
#     return distance

# def majority_element(labels):
#     # Count frequenices
#     frequency = {}
#     for label in labels:
#         frequency[label] = frequency.get(label, 0) + 1

#     # find max frequency
#     max_count = max(frequency.values())

#     #Find labels with max frequency
#     majoirty_labels = [label for label, count in frequency.items() if count == max_count]

#     return majoirty_labels[0]