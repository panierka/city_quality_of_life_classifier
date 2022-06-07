from abc import ABCMeta, abstractmethod
from collections import namedtuple
from typing import Dict, List


class Norm:
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, fuzzified_sample: Dict[str, Dict], rules: List) -> List[Dict]:
        raise NotImplementedError


class ProductNorm(Norm):
    def calculate(self, fuzzified_sample: Dict[str, Dict], rules: List) -> List[Dict]:
        rules_results = []
        for rule in rules:
            tmp = 1
            tmp *= rule['antecedents'].evaluate(fuzzified_sample)
            rules_results.append({'class': rule['consequent.id'], 'value': round(tmp, 3)})
        return rules_results
