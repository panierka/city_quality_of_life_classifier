from abc import ABCMeta, abstractmethod
from typing import Dict, List


class Norm:
    __metaclass__ = ABCMeta

    @staticmethod
    def calculate(fuzzified_sample: Dict[str, Dict], rules: List) -> List[Dict]:
        rules_results = []
        for rule in rules:
            tmp = 1
            tmp *= rule['antecedents'].evaluate(fuzzified_sample)
            rules_results.append({'class': rule['consequent.id'], 'value': round(tmp, 3)})
        return rules_results

    @abstractmethod
    def and_operator(self, a, b):
        raise NotImplementedError

    @abstractmethod
    def or_operator(self, a, b):
        raise NotImplementedError


class ExtendedMangerNorm(Norm):
    def or_operator(self, a, b):
        return a + b - (a * b)

    def and_operator(self, a, b):
        return a * b


class ZadehNorm(Norm):
    def or_operator(self, a, b):
        return max(a, b)

    def and_operator(self, a, b):
        return min(a, b)


class LukasiewiczNorm(Norm):
    def or_operator(self, a, b):
        return min(1, a + b)

    def and_operator(self, a, b):
        return max(0, a + b - 1)
