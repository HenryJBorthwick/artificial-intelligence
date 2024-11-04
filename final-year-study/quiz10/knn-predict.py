def knn_predict(input, examples, distance, combine, k):
    # distance
    distances = []
    for ex_input, ex_output in examples:
        # distance function
        dist = distance(input, ex_input)

        # add distance
        distances.append((dist, ex_output))

    # sort first element (distance) in each tuple
    distances.sort()

    # select k neighbors
    selected_neighbors = distances[:k]

    # tie breaking
    index = k
    while index < len(distances) and distances[index][0] == distances[k-1][0]:
        selected_neighbors.append(distances[index])
        index += 1

    # extract outputs and combine
    outputs = []
    for dist, output in selected_neighbors:
        outputs.append(output)

    # combine outputs to make a prediction
    prediction = combine(outputs)

    return prediction


def euclidean_distance(v1, v2):
    
    total_euclid_distance = 0
    for a, b in zip(v1, v2):
        euclid_distance = (a - b)**2

        total_euclid_distance += euclid_distance

    return total_euclid_distance**0.5


def majority_element(labels):
    frequency = {}

    for label in labels:
        if label in frequency:
            frequency[label] += 1
        else:
            frequency[label] = 1
    
    max_count = 0
    majority_label = None

    for label, count in frequency.items():
        if count > max_count:
            max_count = count
            majority_label = label

    return majority_label



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
