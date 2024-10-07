def accuracy(classifier, inputs, expected_outputs):
    # init counter for correct predictions
    correct_predictions = 0
    total_predictions = len(inputs)

    # iterate over inputs and expected outputs
    for input_vector, expected_output in zip(inputs, expected_outputs):
        # Get predictions from classifier
        prediction = classifier(input_vector)

        # Compare prediction with expected output
        if prediction == expected_output:
            correct_predictions += 1

    # calculate accuracy
    if total_predictions == 0:
        return 0.0
    accuracy_value = correct_predictions / total_predictions
    
    return accuracy_value


# HELPER FUNCTION
def construct_perceptron(weights, bias):
    def perceptron(input_vector):
        activation = sum(w * x for w, x in zip(weights, input_vector)) + bias
        return 1 if activation >= 0 else 0
    return perceptron


# TEST
perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]

print(accuracy(perceptron, inputs, targets))