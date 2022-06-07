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
            antecedents_conjunction = rule['antecedents']
            tmp = 1

            """
            reset = True
            for key, value in fuzzified_sample.items():
                if value['linguistic'] == antecedents_conjunction.get(key):
                    print(value['linguistic'], key, antecedents_conjunction.get(key))
                    tmp *= value['numerical']
                    reset = False"""
            # print(fuzzified_sample, antecedents_conjunction)
            for attribute, classification in antecedents_conjunction.items():
                if attribute not in fuzzified_sample.keys():
                    tmp = 0
                    break

                if fuzzified_sample[attribute]['linguistic'] is not classification:
                    tmp = 0
                    break

                tmp *= fuzzified_sample[attribute]['numerical']

            """if reset:
                tmp = 0"""

            rules_results.append({'class': rule['consequent.id'], 'value': round(tmp, 3)})
        # print(rules_results)
        return rules_results
