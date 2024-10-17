from abc import abstractmethod, ABCMeta
import numpy as np

class Function(metaclass=ABCMeta):

    @abstractmethod
    def __call__(self, inputs):
        """Uses the call operator so the layer can be called like an ordinary function.
        The method takes a vector (numpy array, list, etc) of numbers and must returns the vector of values resulting
        from function the layer is implementing."""


class ReLU(Function):

    def __call__(self, inputs):
        return np.maximum(0, inputs)
    

class Sigmoid(Function):

    def __call__(self, inputs):
        return 1 / (1 + np.exp(-inputs))


class Linear(Function):

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def __call__(self, inputs):
        return np.matmul(self.weights, inputs) + self.bias
    

def forward_pass(functions, input_vector):
    # init output
    output = input_vector

    # iterate over instantiated functions
    for function in functions:
        output = function(output)

    # return 
    return output


# TESTS
layer = Linear(
    np.array([[2.0, 0.0, 1.0], [0.0, -1.0, 3.0]]),
    np.array([1.0, 0.5])
)
input_vector = np.array([1.0, 1.0, 1.0])
functions = [layer, ReLU()]
print(forward_pass(functions, input_vector))


np.set_printoptions(precision=4)

input_vector = np.array([1, 2], dtype=float)
functions = [
    Linear(np.array([[1, -0.5], [0, 1]]), np.array([-3, 1])),
    ReLU(),
    Linear(np.array([[1, 0.5]]), np.array([-1])),
    Sigmoid()
]
print(forward_pass(functions, input_vector))
