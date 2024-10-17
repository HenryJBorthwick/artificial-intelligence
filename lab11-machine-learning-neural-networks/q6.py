import numpy as np

def random_array(shape):
    return np.random.random_sample(shape) - 0.5

def backward_pass(functions, input_vector, target_vector):
    linear1, relu, linear2, sigmoid = functions
    error = sigmoid.cache() - target_vector
    linear2.gradient_wrt_weights += np.outer(error, relu.cache())
    linear2.gradient_wrt_bias += error
    dz1 = linear2.weights.T @ error * (linear1.cache() > 0)
    linear1.gradient_wrt_weights += np.outer(dz1, input_vector)
    linear1.gradient_wrt_bias += dz1

def learn_two_layer_classifier(training_examples, hidden_units, epochs, batch_size, learning_rate):
    # Get input and output dimensions
    input_dim = training_examples[0][0].shape[0]
    output_dim = training_examples[0][1].shape[0]

    # Initialize weights and biases using random_array
    W1 = random_array((hidden_units, input_dim))
    b1 = random_array(hidden_units)
    W2 = random_array((output_dim, hidden_units))
    b2 = random_array(output_dim)

    # Create Linear layers
    linear1 = Linear(W1, b1)
    linear2 = Linear(W2, b2)

    # Create ReLU and Sigmoid functions
    relu = ReLU()
    sigmoid = Sigmoid()

    # Create functions list
    functions = [linear1, relu, linear2, sigmoid]

    for epoch in range(epochs):
        # Loop over batches in a sliding window fashion
        for batch_start in range(0, len(training_examples), batch_size):
            batch = training_examples[batch_start:batch_start+batch_size]

            # Initialize gradients to zero
            linear1.gradient_wrt_weights.fill(0)
            linear1.gradient_wrt_bias.fill(0)
            linear2.gradient_wrt_weights.fill(0)
            linear2.gradient_wrt_bias.fill(0)

            for input_vector, target_vector in batch:
                # Perform the forward pass of the network
                forward_pass(functions, input_vector)
                # Using back-propagation, accumulate the gradients from this batch
                backward_pass(functions, input_vector, target_vector)

            # Update parameters with gradient descent
            linear1.weights -= learning_rate * linear1.gradient_wrt_weights
            linear1.bias -= learning_rate * linear1.gradient_wrt_bias
            linear2.weights -= learning_rate * linear2.gradient_wrt_weights
            linear2.bias -= learning_rate * linear2.gradient_wrt_bias

    # Return a function which evaluates the network
    def network(input_vector):
        return forward_pass(functions, input_vector)

    return network

# Required classes and functions
from abc import abstractmethod, ABCMeta

class Function(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, inputs):
        pass

    @abstractmethod
    def cache(self):
        pass

class ReLU(Function):
    def __init__(self):
        self._cache = None

    def __call__(self, inputs):
        output = np.maximum(0, inputs)
        self._cache = output
        return output

    def cache(self):
        return self._cache

class Sigmoid(Function):
    def __init__(self):
        self._cache = None

    def __call__(self, inputs):
        output = 1 / (1 + np.exp(-inputs))
        self._cache = output
        return output

    def cache(self):
        return self._cache

class Linear(Function):
    def __init__(self, weights, bias):
        self._cache = None
        self.weights = weights
        self.bias = bias
        self.gradient_wrt_weights = np.zeros_like(weights)
        self.gradient_wrt_bias = np.zeros_like(bias)

    def __call__(self, inputs):
        output = np.matmul(self.weights, inputs) + self.bias
        self._cache = output
        return output

    def cache(self):
        return self._cache

def forward_pass(functions, input_vector):
    output = input_vector
    for function in functions:
        output = function(output)
    return output


# TESTS
np.random.seed(12575991)

training_examples = [ # The XOR function
    (np.array([0, 0]), np.array([0])),
    (np.array([0, 1]), np.array([1])),
    (np.array([1, 0]), np.array([1])),
    (np.array([1, 1]), np.array([0]))
]
# The network looks like this:
# o -> o
#    X  -> o
# o -> o
network = learn_two_layer_classifier(training_examples, 2, 1000, 4, 0.01)

print("Input | prediction | target")
for input_vector, target in training_examples:
    predicted_class = network(input_vector).item() > 0.5
    print(f"{str(input_vector):<10}{str(predicted_class):<11}{bool(target.item())}")

np.random.seed(12933277)

print("\n")

training_examples = [ # f = (x and y) or (not x and z)
    (np.array([0, 0, 0]), np.array([0])),
    (np.array([0, 0, 1]), np.array([1])),
    (np.array([0, 1, 0]), np.array([0])),
    (np.array([0, 1, 1]), np.array([1])),
    (np.array([1, 0, 0]), np.array([0])),
    (np.array([1, 0, 1]), np.array([0])),
    (np.array([1, 1, 0]), np.array([1])),
    (np.array([1, 1, 1]), np.array([1]))
]
network = learn_two_layer_classifier(training_examples, 2, 1000, 4, 0.01)

print("Input | prediction | target")
for input_vector, target in training_examples:
    print(f"{str(input_vector):<10}{str(network(input_vector).item() > 0.5):<11}{bool(target.item())}")