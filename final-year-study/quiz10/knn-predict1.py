# knn 
# compute input distance, 
# add distance, output tuple
# sort distance
# select k neighbors
# updating k neighbors with tie breaking
# extract distance, output from k_neighbors
# add output to outputs
# compute combine/predicted final answer from k_neighbors

def knn_predict(input, examples, distance, combine, k):
    # compute distance
    distances = []
    for ex_input, ex_output in examples:
        # compute input distance
        dist = distance(input, ex_input)
        
        # add distance, output tuple
        distances.append((dist, ex_output))

    # sort distances
    distances.sort()

    # select k neighbors
    k_neighbors = distances[:k]

# updating k neighbors with tie breaking
    index = k
    while index < len(distances) and distances[index][0] == distances[k-1][0]:
        k_neighbors.append(distances[index])
        index += 1

    # extract distance, output from k_neighbors
    outputs = []
    for dist, ex_output in k_neighbors:
        # add output to outputs
        outputs.append(ex_output)

    # compute combine/predicted final answer from k_neighbors
    prediction = combine(outputs)

    return prediction

##################
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
###############

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
