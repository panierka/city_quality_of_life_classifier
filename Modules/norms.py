from abc import ABCMeta, abstractmethod
from typing import Dict, List


class Norm:
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, fuzzified_sample: Dict[str, Dict], rules: List) -> List[float]:
        raise NotImplementedError


class AdditiveNorm(Norm):
    def calculate(self, fuzzified_sample: Dict[str, Dict], rules: List) -> List[float]:
        rules_results = []
        for rule in rules:
            tmp = 1
            reset = True
            for key, value in fuzzified_sample.items():
                print(key, value, rule.get(key))
                if value['linguistic'] == rule.get(key):
                    tmp *= value['numerical']
                    reset = False
            if reset:
                tmp = 0
            rules_results.append(tmp)
        return rules_results
