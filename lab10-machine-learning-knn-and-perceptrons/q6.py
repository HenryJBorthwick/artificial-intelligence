def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    # iterate over epochs
    for epoch in range(max_epochs):
        # assume no errors
        no_errors_in_epoch = True

        # iterate through tuples, extract out input [X1,X2] and target output t
        for x_tuple, t in training_examples:

            # compute activation for each weight and input
            activation = sum(w * xi for w, xi in zip(weights, x_tuple)) + bias

            # determine predicted output
            y = 1 if activation >= 0 else 0

            # calculate error, target output - predicted output
            error = t - y

            # update weights and bias if not 0
            if error != 0:
                # original weight + learning rate * input * error rate
                weights = [w + learning_rate * xi * error for w, xi in zip(weights, x_tuple)]

                # original bias + learning rate * error rate
                bias += learning_rate * error

                # move to next epoch
                no_errors_in_epoch = False
    
        # if no errors remains true after an epoch, break early as perceptron converged
        if no_errors_in_epoch:
            break
    
    return weights, bias
      

# HELPER FUNCTION
def construct_perceptron(weights, bias):
    def perceptron(input_vector):
        activation = sum(w * x for w, x in zip(weights, input_vector)) + bias
        return 1 if activation >= 0 else 0
    return perceptron


# TESTS
weights = [2, -4]
bias = 0
learning_rate = 0.5
examples = [
  ((0, 0), 0),
  ((0, 1), 0),
  ((1, 0), 0),
  ((1, 1), 1),
  ]
max_epochs = 50

weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
print(f"Weights: {weights}")
print(f"Bias: {bias}\n")

perceptron = construct_perceptron(weights, bias)

print(perceptron((0,0)))
print(perceptron((0,1)))
print(perceptron((1,0)))
print(perceptron((1,1)))
print(perceptron((2,2)))
print(perceptron((-3,-3)))
print(perceptron((3,-1)))

print("\n")

weights = [2, -4]
bias = 0
learning_rate = 0.5
examples = [
  ((0, 0), 0),
  ((0, 1), 1),
  ((1, 0), 1),
  ((1, 1), 0),
  ]
max_epochs = 50

weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
print(f"Weights: {weights}")
print(f"Bias: {bias}\n")
