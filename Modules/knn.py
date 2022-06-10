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
        if sample[label] == results[0][0]:
            return True
        else:
            return False

    @staticmethod
    def knn_for_every_row(training_dataset, test_dataset, m, k, label):
        correct = 0
        for i in range(len(test_dataset)):
            result = KNN.knn_for_single_row(test_dataset.iloc[i], training_dataset, m, k, label)
            if result:
                correct += 1
        return str((correct / len(test_dataset))*100)+"%"
