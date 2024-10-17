import numpy
from abc import abstractmethod, ABCMeta


class Function(metaclass=ABCMeta):

    @abstractmethod
    def __call__(self, inputs):
        """Uses the call operator so the layer can be called like an ordinary function.
        The method takes a vector (numpy array, list, etc) of numbers and must returns the
        vector of values resulting from function the layer is implementing."""


class ReLU(Function):

    def __call__(self, inputs):
        return numpy.maximum(0, inputs)




# TESTS
relu = ReLU()
inputs = numpy.array([0.44, 1.02, 1.37, -0.43, -0.09])
outputs = relu(inputs)
print(type(outputs) == numpy.ndarray)

inputs = numpy.array([0.44, 1.02, 1.37, -0.43, -0.09])
relu = ReLU()
print(f"{'' : <5}ReLU")
for i, o in zip(inputs, relu(inputs)):
    print(f"{f'{i:.2f}' : <5} -> " + f"{o:.2f}")