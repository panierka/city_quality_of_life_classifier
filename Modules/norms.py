from abc import ABCMeta, abstractmethod
from collections import namedtuple
from typing import Dict, List


class Norm:
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, fuzzified_sample: Dict[str, Dict], rules: List) -> List[Dict]:
        raise NotImplementedError


class AdditiveNorm(Norm):
    def calculate(self, fuzzified_sample: Dict[str, Dict], rules: List) -> List[Dict]:
        rules_results = []
        for rule in rules:
            antecedents_conjunction = rule['antecedents']
            tmp = 1
            reset = True
            for key, value in fuzzified_sample.items():
                if value['linguistic'] == antecedents_conjunction.get(key):
                    tmp *= value['numerical']
                    reset = False
            if reset:
                tmp = 0

            rules_results.append({'class': rule['consequent.id'], 'value': tmp})
        return rules_results
