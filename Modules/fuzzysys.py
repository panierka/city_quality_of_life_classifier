from Modules.membership_functions import Function
from Modules.norms import Norm, AdditiveNorm
from pandas import Series
from typing import Dict, Callable, List
import Modules.defuzzification_methods as defuzz


class FuzzySystem:
    def __init__(self, norm: Norm = AdditiveNorm()):
        self.__antecedents = {}  # słownik[nazwa : (słownik[lingwi : funkcja])]
        self.__consequents = {}  # słownik[nazwa : (słownik[lingwi : funkcja])]
        self.__rules = []
        self.__methods = {
            'fom': max,
            'lom': defuzz.lom
        }
        self.__inference_norm_method = norm

    def add_antecedent(self, antecedent: str, linguistic_value: str, membership_function: Function):
        if antecedent not in self.__antecedents:
            self.__antecedents[antecedent] = {}
        self.__antecedents[antecedent][linguistic_value] = membership_function

    def add_consequent(self, consequent: str, linguistic_value: str, membership_function: Function):
        if consequent not in self.__consequents:
            self.__consequents[consequent] = {}
        self.__consequents[consequent][linguistic_value] = membership_function

    def add_rule(self, rule: Dict):
        last_key = rule.keys()[-1]
        rule[last_key] = {rule[last_key]:self.__consequents[last_key][rule[last_key]]}
        self.__rules.append(rule)

    def test_display(self):
        print('\n'.join(map(str, self.__antecedents.items())))

    def fuzzify(self, sample: Dict) -> dict:
        fuzzy_sample = {}

        for attribute in sample.keys():
            if attribute not in self.__antecedents.keys():
                continue

            membership_degrees = {}
            for linguistic_value, membership_function in self.__antecedents[attribute].items():
                value = sample[attribute]
                membership_degrees[linguistic_value] = membership_function.calculate(value)
            fuzzy_sample[attribute] = {
                'linguistic': max(membership_degrees, key=membership_degrees.get),
                'numerical': max(membership_degrees.values())
            }

        return fuzzy_sample

    def inference(self, fuzzified_sample: Dict[str, Dict]) -> List[float]:
        results = self.__inference_norm_method.calculate(fuzzified_sample, self.__rules)
        return results

    def defuzzify(self, rule_results: List[float], method_name: str) -> float:
        assert method_name in self.__methods.keys()
        method = self.__methods[method_name]
        return method(rule_results)

    def classify(self, crisp_result: float):
        max_value = 0
        decision = ''
        for consequent in self.__consequents.values():
            for attribute, function in consequent.items():
                membership_function_value = function.calculate(crisp_result)
                if membership_function_value > max_value:
                    max_value = membership_function_value
                    decision = attribute
        return decision

    def compute(self, sample: Series, defuzzify_method_name: str) -> str:
        sample_data = dict(sample.to_dict())
        fuzzified_sample = self.fuzzify(sample_data)
        # print(f'{fuzzified_sample=}')
        rule_results = self.inference(fuzzified_sample)
        # print(f'{rule_results=}')
        crisp_result = self.defuzzify(rule_results, defuzzify_method_name)
        print(f'{crisp_result=}')
        decision = self.classify(crisp_result)

        return decision

#%%
