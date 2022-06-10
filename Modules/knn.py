import numpy as np
import pandas as pd

class KNN:

    @staticmethod
    def distance(x, y, m):
        add = 0
        length = 0
        first = True
        first_noted = 0
        for i in range(len(x)):
            if (not isinstance(x[i], str)) and (not isinstance(x[i], bool)):
                if first:
                    first = False
                    first_noted = i
                length += 1
        for i in range(length):
            difference = abs(x[i+first_noted] - y[i+first_noted])
            power = 1
            for j in range(m):
                power *= difference
            add += power
        return add**(1/m)

    @staticmethod
    def knn_for_single_row(sample, dataset, m, k, label):
        distances = []
        for i in range(len(dataset)):
            distance_s_from_d = KNN.distance(sample,dataset.iloc[i],m)
            distances.append((dataset[label].iloc[i], distance_s_from_d))
        distances.sort(key=lambda x: x[1])
        neighbours = []
        for i in range(k):
            neighbours.append(distances[i])
        results = []
        help = []
        counter_1 = 0
        counter_2 = 0
        basic_counter = 0
        while counter_1 < len(neighbours):
            counter_2 = counter_1 + 1
            candidate = neighbours[counter_1][0]
            if candidate not in help:
                    basic_counter += 1
            else:
                counter_1 += 1
                continue
            while counter_2 < len(neighbours) - counter_1:
                if neighbours[counter_2][0] == candidate:
                    basic_counter += 1
                counter_2 += 1
            help.append(candidate)
            results.append((candidate, basic_counter))
            basic_counter = 0
        results.sort(key=lambda x: x[1])
        if sample[label] == results[0][0] and sample[label] == 'better':
            return 1
        elif sample[label] == results[0][0] and sample[label] == 'worse':
            return 2
        elif sample[label] != results[0][0] and results[0][0] == 'better':
            return 3
        elif sample[label] != results[0][0] and results[0][0] == 'worse':
            return 4

    @staticmethod
    def knn_for_every_row(training_dataset, test_dataset, m, k, label):
        fp = 0
        tn = 0
        fn = 0
        tp = 0
        for i in range(len(test_dataset)):
            result = KNN.knn_for_single_row(test_dataset.iloc[i], training_dataset, m, k, label)
            if result == 1:
                tp += 1
            if result == 2:
                tn += 1
            if result == 3:
                fp += 1
            if result == 4:
                fn += 1
        accuracy = (tp + tn) / (tp + tn + fn + fp) * 100
        precision = tp / (tp + fp) * 100
        recall = tp / (tp + fn) * 100
        specificity = tn / (tn + fp) * 100
        return accuracy, precision, recall, specificity
