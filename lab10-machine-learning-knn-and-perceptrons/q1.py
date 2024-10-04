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
    majoirty_labels = [label for label, count in frequency.items() if count == max_count]

    return majoirty_labels[0]


# test
print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))


print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
print(majority_element("ababc") in "ab")