from typing import Callable, Any


class RuleCondition:
    not_operator: Callable[[Any, float], float] = lambda s, a: 1 - a
    and_operator: Callable[[Any, float, float], float] = lambda s, a, b: a * b
    or_operator: Callable[[Any, float, float], float] = lambda s, a, b: a + b - (a * b)

    def __init__(self, key, value):
        self.__antecedents_attribute = key
        self.__antecedents_value = value
        self.__fire = lambda d: self.get_x(d)

    def evaluate(self, fuzzified_sample: dict) -> float:
        return self.__fire(fuzzified_sample)

    def get_x(self, fuzzified_sample):
        if self.__antecedents_attribute not in fuzzified_sample.keys():
            return 0

        if fuzzified_sample[self.__antecedents_attribute]['linguistic'] is not self.__antecedents_value:
            return 0
        x = fuzzified_sample[self.__antecedents_attribute]['numerical']
        return x

    def __and__(self, other):
        def f(x):
            return self.and_operator(self.__fire(x), other.__fire(x))

        r = RuleCondition(self.__antecedents_attribute, self.__antecedents_value)
        r.__fire = f
        return r

    def __or__(self, other):
        def f(x):
            return self.or_operator(self.__fire(x), other.__fire(x))

        r = RuleCondition(self.__antecedents_attribute, self.__antecedents_value)
        r.__fire = f
        return r

    def __invert__(self):
        def f(x):
            return self.not_operator(self.__fire(x))

        r = RuleCondition(self.__antecedents_attribute, self.__antecedents_value)
        r.__fire = f
        return r
