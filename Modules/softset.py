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
        for i in range(len(training_set)):
            result = training_set.iloc[i][label]
            if result not in label_names:
                label_names.append(result)
        results_for_test_rows = [[1 for j in range(len(label_names))] for i in range(len(test_set))]
        counter = 0
        for name in label_names:
            profiled_list = []
            for i in range(len(test_set)):
                result = test_set.iloc[i].tolist()
                result_label = training_set.iloc[i][label]
                if result_label == name:
                    profiled_list.append(result)
            profiled_dataset = pd.DataFrame(profiled_list, columns=col)
            for quality in qualities:
                column_mean = SoftSet.mean(profiled_dataset, quality)
                for i in range(len(test_set)):
                    if test_set.iloc[i][quality] < column_mean:
                        multiplier = 0
                    else:
                        multiplier = 1
                    results_for_test_rows[i][counter] += multiplier * test_set.iloc[i][quality]
            counter += 1
        correct = 0
        for i in range(len(test_set)):
            result = results_for_test_rows[i].index(max(results_for_test_rows[i]))
            if label_names[result] == test_set.iloc[i][label]:
                correct += 1
        return correct/len(test_set)

