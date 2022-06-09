import numpy as np

import Modules.fuzzysys as fsys
from Modules.norms import *
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay


class FuzzyTest:
    def __init__(self, norm: Norm = ExtendedMangerNorm(), defuzzification_method='centroid',
                 score_threshold=70):
        self.__norm = norm
        self.__defuzzification_method = defuzzification_method
        self.__score_threshold = score_threshold
        pass

    def run(self, fuzzy: fsys.FuzzySystem, df, n=None, show_confusion_matrix=False, display=False):
        if n is None:
            n = len(df)
        n = min(len(df), n)
        fuzzy.set_norm(self.__norm)
        atomic_ratings = {
            'tp': 0,
            'tn': 0,
            'fp': 0,
            'fn': 0
        }

        for i in range(n):
            sample = df.iloc[i]
            result = fuzzy.compute(sample, self.__defuzzification_method, display=display)
            assumed_better = result > self.__score_threshold
            factually_better = sample['Label'] == 'better'

            rating_id = ''
            rating_id += 't' if assumed_better == factually_better else 'f'
            rating_id += 'p' if assumed_better else 'n'
            atomic_ratings[rating_id] += 1

        rating = {
            'accuracy': (atomic_ratings['tp'] + atomic_ratings['tn']) / n,
            'recall': atomic_ratings['tp'] / (atomic_ratings['tp'] + atomic_ratings['fn']),
            'specificity': atomic_ratings['tn'] / (atomic_ratings['tn'] + atomic_ratings['fp']),
            'precision': atomic_ratings['tp'] / (atomic_ratings['tp'] + atomic_ratings['fp'])
        }

        print(f'FOR NORM = {type(self.__norm).__name__}, '
              f'DEFUZZIFICATION METHOD = {self.__defuzzification_method}, '
              f'THRESHOLD = {self.__score_threshold}')

        if show_confusion_matrix:
            matrix_data = np.array([[atomic_ratings['tp'], atomic_ratings['tn']],
                                    [atomic_ratings['fp'], atomic_ratings['fn']]])
            matrix_display = ConfusionMatrixDisplay(matrix_data, display_labels=['better', 'worse'])
            matrix_display.plot()
            plt.show()

        print('\n'.join(map(lambda x: f' > {x[0]}: {round(x[1] * 100, 1)}%', rating.items())))
        print('----------------------------------------------------------------------------------')
