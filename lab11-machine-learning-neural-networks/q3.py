from abc import abstractmethod, ABCMeta
import numpy as np

class Function(metaclass=ABCMeta):

    @abstractmethod
    def __call__(self, inputs):
        """Uses the call operator so the layer can be called like an ordinary function.
        The method takes a vector (numpy array, list, etc) of numbers and must returns the vector of values resulting
        from function the layer is implementing."""

class Linear(Function):
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def __call__(self, inputs):
        return np.matmul(self.weights, inputs) + self.bias




# TESTS
f = Linear(np.identity(2), np.zeros(2))
print(type(f.weights) == np.ndarray)
print(type(f.bias) == np.ndarray)

weights = np.array([
    [1, 2, 1],
    [3, -1, 2]
], dtype=float)
bias = np.array([0.5, -0.5])


linear_layer = Linear(weights, bias)
inputs = np.array([1, 1, 1], dtype=float)
outputs = linear_layer(inputs)

print(type(outputs) == np.ndarray)
print(len(outputs) == 2)


weights = np.array([
    [1, 2, 1],
    [3, -1, 2]
], dtype=float)
bias = np.array([0.5, -0.5])

linear_layer = Linear(weights, bias)
inputs = np.array([1, 0, 2], dtype=float)
outputs = linear_layer(inputs)

print(f'{inputs} -> {outputs}')