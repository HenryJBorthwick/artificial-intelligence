def knn_predict(input, examples, distance, combine, k):
    # Compute distances between input and each example
    distances = [(distance(input, ex_input), ex_output) for ex_input, ex_output in examples]
    
    # Sort the distances
    sorted_distances = sorted(distances, key=lambda x: x[0])
    
    # Select the first k neighbors
    k_neighbors = sorted_distances[:k]
    kth_distance = k_neighbors[-1][0]
    
    # Handle tie-breaking by including neighbors with equal distance
    index = k
    while index < len(sorted_distances) and sorted_distances[index][0] == kth_distance:
        k_neighbors.append(sorted_distances[index])
        index += 1
    
    # Extract outputs from the selected neighbors
    outputs = [output for _, output in k_neighbors]
    
    # Combine outputs to make the final prediction
    prediction = combine(outputs)
    
    # Return the prediction
    return prediction


# HELPER FUNCTIONS
import math

def euclidean_distance(v1, v2):
    # Calculate squared differences and sum them
    squared_diffs = [(a - b) ** 2 for a, b in zip(v1, v2)]
    sum_of_squared_diffs = sum(squared_diffs)

    # Compute the square root of the sum
    distance = math.sqrt(sum_of_squared_diffs)
    return distance

def majority_element(labels):
    # Count frequenices
    frequency = {}
    for label in labels:
        frequency[label] = frequency.get(label, 0) + 1

    # find max frequency
    max_count = max(frequency.values())

    #Find labels with max frequency
    majority_labels = [label for label, count in frequency.items() if count == max_count]

    # Return the smallest label among the majority labels
    return min(majority_labels)


# TESTS

examples = [
    ([2], '-'),
    ([3], '-'),
    ([5], '+'),
    ([8], '+'),
    ([9], '+'),
]

distance = euclidean_distance
combine = majority_element

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print(x, knn_predict([x], examples, distance, combine, k))
    print()

# insert space between answers
print('\n')

# using knn for predicting numeric values
examples = [
    ([1], 5),
    ([2], -1),
    ([5], 1),
    ([7], 4),
    ([9], 8),
]

def average(values):
    return sum(values) / len(values)

distance = euclidean_distance
combine = average

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
    print()
