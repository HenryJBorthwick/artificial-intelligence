import numpy
from abc import abstractmethod, ABCMeta

class Function(metaclass=ABCMeta):

    @abstractmethod
    def __call__(self, inputs):
        """Uses the call operator so the layer can be called like an ordinary function.
        The method takes a vector (numpy array, list, etc) of numbers and must returns the vector of values resulting
        from function the layer is implementing."""


class Sigmoid(Function):
    def __call__(self, inputs):
        return 1 / (1 + numpy.exp(-inputs))


#TESTS
sigmoid = Sigmoid()
inputs = numpy.array([0.44, 1.02, 1.37, -0.43, -0.09])
outputs = sigmoid(inputs)
print(type(outputs) == numpy.ndarray)

inputs = numpy.array([0.44, 1.02, 1.37, -0.43, -0.09])
sigmoid = Sigmoid()
print(f"{'' : <3}Sigmoid")
for i, o in zip(inputs, sigmoid(inputs)):
    print(f"{f'{i:.2f}' : <5} -> " + f"{o:.2f}")