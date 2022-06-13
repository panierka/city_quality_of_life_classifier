import numpy as np
import pandas as pd

class SoftSet:

    @staticmethod
    def mean(training_set, quality):
        add = 0
        for element in training_set[quality]:
            add += element
        return add / len(training_set)


    @staticmethod
    def softset(training_set, test_set, label):
        col = training_set.columns.tolist()
        qualities = []
        label_names = []
        for i in col:
            column = training_set.loc[:, i].tolist()
            if (not isinstance(column[0], str)) and (not isinstance(column[0], bool)):
                qualities.append(i)
        qualities.pop(len(qualities) - 1)
        for i in range(len(training_set)):
            result = training_set.iloc[i][label]
            if result not in label_names:
                label_names.append(result)
        results_for_test_rows = [[0 for j in range(len(label_names))] for i in range(len(test_set))]
        for quality in qualities:
            column_mean = SoftSet.mean(training_set, quality)
            for i in range(len(test_set)):
                if test_set.iloc[i][quality] < column_mean:
                    results_for_test_rows[i][1] += 1
                else:
                    results_for_test_rows[i][0] += 1
        fp = 0
        tn = 0
        fn = 0
        tp = 0
        for i in range(len(test_set)):
            result = results_for_test_rows[i].index(max(results_for_test_rows[i]))
            if label_names[result] == test_set.iloc[i][label] and label_names[result] == 'better':
                tp += 1
            elif label_names[result] == test_set.iloc[i][label] and label_names[result] == 'worse':
                tn += 1
            elif label_names[result] != test_set.iloc[i][label] and test_set.iloc[i][label] == 'better':
                fp += 1
            elif label_names[result] != test_set.iloc[i][label] and test_set.iloc[i][label] == 'worse':
                fn += 1
        accuracy = (tp + tn) / (tp + tn + fn + fp) * 100
        precision = tp / (tp + fp) * 100
        recall = tp / (tp + fn) * 100
        specificity = tn / (tn + fp) * 100
        return accuracy, precision, recall, specificity

