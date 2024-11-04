def euclidean_distance(v1, v2):
    
    total_euclid_distance = 0
    for a, b in zip(v1, v2):
        euclid_distance = (a - b)**2

        total_euclid_distance += euclid_distance

    return total_euclid_distance**0.5

print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))


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

print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
print(majority_element("ababc") in "ab")