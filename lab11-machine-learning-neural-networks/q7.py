import numpy as np

# Base Function class
from abc import ABCMeta, abstractmethod

class Function(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, inputs):
        pass

    @abstractmethod
    def cache(self):
        pass

# Linear function class
class Linear(Function):
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        self._cache = None

    def __call__(self, inputs):
        output = np.matmul(self.weights, inputs) + self.bias
        self._cache = output
        return output

    def cache(self):
        return self._cache

# ReLU activation function class
class ReLU(Function):
    def __init__(self):
        self._cache = None

    def __call__(self, inputs):
        output = np.maximum(0, inputs)
        self._cache = output
        return output

    def cache(self):
        return self._cache

# Forward pass function
def forward_pass(functions, input_vector):
    output = input_vector
    for function in functions:
        output = function(output)
    return output

# Input dimension (8x8 grayscale image flattened to a vector)
input_dim = 64

# Hidden layer size (you can choose any reasonable number)
hidden_units = 32

# Output dimension (digits 0-9)
output_dim = 10

# Initialize weights and biases (values are not important)
weights1 = np.random.random_sample((hidden_units, input_dim)) - 0.5
bias1 = np.random.random_sample(hidden_units) - 0.5
weights2 = np.random.random_sample((output_dim, hidden_units)) - 0.5
bias2 = np.random.random_sample(output_dim) - 0.5

# Create Linear layers
linear1 = Linear(weights1, bias1)
linear2 = Linear(weights2, bias2)

# Create ReLU activation function
relu = ReLU()

# Instantiate the list of Function objects
functions = [
    linear1,
    relu,
    linear2
]

# Test code
print(sum(type(f) == Linear for f in functions))
