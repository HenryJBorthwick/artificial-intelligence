def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        # Compute weighted sum (activation) # input = input_vector
        activation = sum(w * x for w,x in zip(weights, input)) + bias

        return 1 if activation >= 0 else 0
    
    return perceptron


# TEST
weights = [2, -4]
bias = 0
perceptron = construct_perceptron(weights, bias)

print(perceptron([1, 1]))
print(perceptron([2, 1]))
print(perceptron([3, 1]))
print(perceptron([-1, -1]))
