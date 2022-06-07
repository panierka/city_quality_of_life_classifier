from Modules.membership_functions import Function
from Modules.norms import Norm, ProductNorm
from pandas import Series
from typing import Dict, Callable, List
import Modules.defuzzification_methods as defuzz
import numpy as np
from Modules.rule import RuleCondition


class FuzzySystem:
    def __init__(self, norm: Norm = ProductNorm()):
        self.__antecedents = {}  # słownik[nazwa : (słownik[lingwi : funkcja])]
        self.__consequents = {}  # słownik[nazwa : funkcja])]
        self.__rules = []
        self.__methods = {
            'fom': defuzz.fom,
            'lom': defuzz.lom,
            'mom': defuzz.mom
        }
        self.__inference_norm_method = norm

    def add_antecedent(self, antecedent: str, linguistic_value: str, membership_function: Function):
        if antecedent not in self.__antecedents:
            self.__antecedents[antecedent] = {}
        self.__antecedents[antecedent][linguistic_value] = membership_function

    def add_consequent(self, consequent: str, membership_function: Function):
        if consequent not in self.__consequents:
            self.__consequents[consequent] = {}
        self.__consequents[consequent] = membership_function

    def add_rule(self, rule_conditions: RuleCondition, consequent_value_identifier: str):
        rule = {
            'antecedents': rule_conditions,
            'consequent.id': consequent_value_identifier
        }
        self.__rules.append(rule)

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

    def inference(self, fuzzified_sample: Dict[str, Dict]) -> np.array:
        raw_rule_evaluations = self.__inference_norm_method.calculate(fuzzified_sample, self.__rules)
        aggregated_rule_evaluations = {}

        for record in raw_rule_evaluations:
            class_id = record['class']
            if class_id not in aggregated_rule_evaluations:
                aggregated_rule_evaluations[class_id] = []
            aggregated_rule_evaluations[class_id].append(record['value'])

        for k in aggregated_rule_evaluations.keys():
            aggregated_rule_evaluations[k] = max(aggregated_rule_evaluations[k])

        def evaluate(x: float) -> float:
            vals = []
            for name, func in self.__consequents.items():
                val = min(func.calculate(x), aggregated_rule_evaluations[name])
                vals.append(val)
            return max(vals)

        xs = np.linspace(0, 1, num=1000)
        results = []
        for x in xs:
            results.append(evaluate(x))
        return np.array(results)

    def defuzzify(self, rule_results: np.array, method_name: str) -> float:
        assert method_name in self.__methods.keys()
        method = self.__methods[method_name]
        return method(rule_results)

    def classify(self, crisp_result: float):

        """max_value = 0
        decision = ''
        for consequent, function in self.__consequents.items():
            membership_function_value = function.calculate(crisp_result)
            if membership_function_value > max_value:
                max_value = membership_function_value
                decision = consequent'"""
        pass
        # return decision

    def compute(self, sample: Series, defuzzify_method_name: str) -> str:
        sample_data = dict(sample.to_dict())
        fuzzified_sample = self.fuzzify(sample_data)
        # print(f'{fuzzified_sample=}')
        rule_results = self.inference(fuzzified_sample)
        crisp_result = self.defuzzify(rule_results, defuzzify_method_name)
        # print(f'{crisp_result=}')
        # decision = self.classify(crisp_result)

        return crisp_result, rule_results

#%%
