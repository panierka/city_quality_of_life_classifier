from abc import ABCMeta, abstractmethod


class Function:
    __metaclass__ = ABCMeta
    @abstractmethod
    def calculate(self, x) : raise NotImplementedError


class TriangularFunction(Function):
    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c

    def calculate(self, x: float) -> float:
        if x <= self.__a:
            return 0

        if self.__a < x <= self.__b:
            return (x - self.__a) / (self.__b - self.__a)

        if self.__b < x <= self.__c:
            return (self.__c - x)/(self.__c - self.__b)

        if x > self.__c:
            return 0