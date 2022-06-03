from membership_functions import Function


class FuzzySystem:
    def __init__(self):
        self.__antecedents = {}  # słownik nazwa : (słownik lingwi : funkcja)
        self.__consequents = {}  # słownik nazwa : (słownik lingwi : funkcja)
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
