from collections import namedtuple
from typing import Dict
import numpy as np
from numpy import array


def get_array(fx: array) -> array:
    return np.linspace(1, 100, num=len(fx), dtype=int)


def fom(fx: array):
    x = get_array(fx)
    return np.min(x[fx == fx.max()])


def lom(fx: array):
    x = get_array(fx)
    return np.max(x[fx == fx.max()])


def mom(fx: array):
    x = get_array(fx)
    return np.mean(x[fx == fx.max()])


def centroid(fx: array):
    x = get_array(fx)
    return np.sum(x * fx) / np.sum(fx)
"""    result = 0
    for i in range(len(x)):
        result += x[i] * fx[i]
    return result / len(x)"""
