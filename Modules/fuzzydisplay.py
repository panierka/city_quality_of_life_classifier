from typing import Dict
import numpy as np
from Modules.membership_functions import Function
import matplotlib.pyplot as plt


class FuzzyVisualization:
    @staticmethod
    def display_fuzzy_variable(elements: Dict[str, Function], label):
        xs = np.linspace(0, 1, 1000)

        font = {
            'size': 13
        }

        fig = plt.figure()
        fig.set_size_inches(10, 6)
        plt.rc('font', **font)
        plt.title(label)
        plt.xlabel('value')
        plt.ylabel('degree of membership')
        for name, func in elements.items():
            ys = [func.calculate(x) for x in xs]
            plt.plot(xs, ys, label=name)
            plt.legend()

        plt.show()

    @staticmethod
    def display_result(rule_results, crisp_result):
        xs = np.linspace(1, 100, num=1000)
        fig, ax = plt.subplots()
        fig.set_size_inches(8, 5)
        ax.set_ylim([0, 1])
        ax.plot(xs, rule_results)
        y_max = rule_results[10 * crisp_result - 1]
        plt.axvline(x=crisp_result, ymax=y_max, c='red')
        plt.show()
