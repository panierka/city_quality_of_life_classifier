import pandas as pd
import math

class Bayes:
    @staticmethod
    def mean(training_set, quality):
        add = 0
        for element in training_set[quality]:
            add += element
        return add / len(training_set)

    @staticmethod
    def standard_deviation(training_set, mean, quality):
        add = 0
        for element in training_set[quality]:
            add += (element - mean) ** 2
        return (add / len(training_set)) ** (1 / 2)

    @staticmethod
    def normal_distribution(x, mean, stdev):
        return 1 / ((2 * math.pi) ** (1 / 2) * stdev) * math.e ** (-((x - mean) ** 2) / (2 * (stdev ** 2)))

    @staticmethod
    def bayes(training_set, test_set, label):
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
        probabilities_for_rows = [[1 for j in range(len(label_names))] for i in range(len(test_set))]
        counter = 0
        for name in label_names:
            profiled_list = []
            for i in range(len(training_set)):
                result = training_set.iloc[i].tolist()
                result_label = training_set.iloc[i][label]
                if result_label == name:
                    profiled_list.append(result)
            profiled_dataset = pd.DataFrame(profiled_list, columns=col)
            for quality in qualities:
                column_mean = Bayes.mean(profiled_dataset, quality)
                column_stdev = Bayes.standard_deviation(profiled_dataset, column_mean, quality)
                for i in range(len(test_set)):
                    probabilities_for_rows[i][counter] *= Bayes.normal_distribution(test_set[quality].iloc[i],
                                                                                    column_mean, column_stdev)
            counter += 1
        results = [[[1, 1] for i in range(len(label_names))] for i in range(len(test_set))]
        for i in range(len(test_set)):
            for j in range(len(label_names)):
                results[i][j][0] = probabilities_for_rows[i][j]
                results[i][j][1] = label_names[j]
        for i in range(len(test_set)):
            results[i].sort(reverse=True)
        correct = 0
        for i in range(len(test_set)):
            if results[i][0][1] == test_set[label].iloc[i]:
                correct += 1
        return correct / len(test_set) * 100