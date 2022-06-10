from abc import ABCMeta, abstractmethod
import math


class Function:
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, x):
        raise NotImplementedError


class TriangularFunction(Function):
    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c

    def calculate(self, x: float) -> float:
        if x == self.__b:
            return 1  # przypadek dla 0

        if x <= self.__a:
            return 0

        if self.__a < x <= self.__b:
            return (x - self.__a) / (self.__b - self.__a)

        if self.__b < x <= self.__c:
            return (self.__c - x)/(self.__c - self.__b)

        if x > self.__c:
            return 0


class TrapezoidalFunction(Function):
    def __init__(self, a: float, b: float, c: float, d: float):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d

    def calculate(self, x: float) -> float:
        if x <= self.__a:
            return 0

        if self.__a < x <= self.__b:
            return (x - self.__a) / (self.__b - self.__a)

        if self.__b < x <= self.__c:
            return 1

        if self.__c < x <= self.__d:
            return (self.__d - x) / (self.__d - self.__c)

        if x > self.__c:
            return 0


class GaussianFunction(Function):
    def __init__(self, a: float, b: float):
        self.__a = a
        self.__b = b
        self.__center = (a + b) / 2
        self.__spread = (b - a)

    def calculate(self, x: float) -> float:
        return math.e ** (-((x - self.__center) / self.__spread))

class GammaFunction(Function):
    def __init__(self, a: float, b: float):
        self.__a = a
        self.__b = b

    def calculate(self, x: float) -> float:
        if x <= self.__a:
            return 0

        if self.__a < x <= self.__b:
            return (x - self.__a) / (self.__b - self.__a)

        if x > self.__b:
            return 1


class BellFunction(Function):
    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c

    def calculate(self, x: float) -> float:
        if x <= self.__a:
            return 0

        if self.__a < x <= self.__b:
            return 2*(((x - self.__a) / (self.__c - self.__a))**2)

        if self.__b < x <= self.__c:
            return 1-2*(((x - self.__a) / (self.__c - self.__a))**2)

        if x > self.__c:
            return 1