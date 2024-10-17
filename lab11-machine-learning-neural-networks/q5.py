from abc import abstractmethod, ABCMeta
import numpy as np

class Function(metaclass=ABCMeta):

    @abstractmethod
    def __call__(self, inputs):
        """Uses the call operator so the layer can be called like an ordinary function.
        The method takes a vector (numpy array, list, etc) of numbers and must returns the vector of values resulting
        from function the layer is implementing."""

    @abstractmethod
    def cache(self):
        """Returns the cached values from the last call to the function."""


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

    def __call__(self, inputs):
        output = np.matmul(self.weights, inputs) + self.bias
        self._cache = output
        return output
    
    def cache(self):
        return self._cache
    

def forward_pass(functions, input_vector):
    # init output
    output = input_vector

    # iterate over instantiated functions
    for function in functions:
        output = function(output)

    # return 
    return output



# TEST
input_vector = np.array([1, 0, 2], dtype=float)
func = Sigmoid()
output = func(func(func(input_vector)))
print(np.all(output == func.cache()))


input1 = np.array([-0.05, 0.25, 0.15])
input2 = np.array([0.75, -0.5, 0.25])
func = ReLU()
output1 = func(input1)
output2 = func(input2)
print(np.all(output2 == func.cache()))


layer = Linear(
    np.array([[2.0, 0.0, 1.0], [0.0, -1.0, 3.0]]),
    np.array([1.0, 0.5])
)
input_vector = np.array([1.0, -1.0, -1.0])
functions = [layer, ReLU()]
z = forward_pass(functions, input_vector)
print(input_vector, '->', layer.cache(), '->', z)
