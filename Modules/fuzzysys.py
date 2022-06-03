from Modules.membership_functions import Function
from pandas import Series


class FuzzySystem:
    def __init__(self):
        self.__antecedents = {}  # słownik[nazwa : (słownik[lingwi : funkcja])]
        self.__consequents = {}  # słownik[nazwa : (słownik[lingwi : funkcja])]
        self.__rules = []

    def add_antecedent(self, antecedent: str, linguistic_value: str, membership_function: Function):
        if antecedent not in self.__antecedents:
            self.__antecedents[antecedent] = {}
        self.__antecedents[antecedent][linguistic_value] = membership_function

    def add_consequent(self, consequent: str, linguistic_value: str, membership_function: Function):
        if consequent not in self.__consequents:
            self.__consequents[consequent] = {}
        self.__consequents[consequent][linguistic_value] = membership_function

    def test_display(self):
        print('\n'.join(map(str, self.__antecedents.items())))

    def fuzzify(self, sample: dict) -> dict:
        fuzzy_sample = {}

        for attribute in sample.keys():
            if attribute not in self.__antecedents.keys():
                continue

            membership_degrees = {}
            for linguistic_value, membership_function in self.__antecedents[attribute].items():
                value = sample[attribute]
                membership_degrees[linguistic_value] = membership_function.calculate(value)
            fuzzy_sample[attribute] = max(membership_degrees, key=membership_degrees.get)
            
        return fuzzy_sample

#%%
