from typing import Tuple
import pandas as pd


class ProcessingData:
    @staticmethod
    def normalize(df: pd.DataFrame):
        values = df.select_dtypes(include=float)
        column_names = values.columns.tolist()
        for column_name in column_names:
            min_value = df[column_name].min()
            max_value = df[column_name].max()
            val = (df[column_name] - min_value) / (max_value - min_value)
            df[column_name] = val
        pass

    @staticmethod
    def split(df: pd.DataFrame, ratio: float) \
            -> Tuple[pd.DataFrame, pd.DataFrame]:
        # walidacja ratio
        center_index: int = int(len(df) * ratio)
        train_set = df.iloc[:center_index]
        test_set = df.iloc[center_index:]
        return train_set, test_set

    @staticmethod
    def shuffle(df: pd.DataFrame):
        import random

        for j in range(len(df) - 1, -1, -1):
            random_index = random.randint(0, j)
            df.iloc[j], df.iloc[random_index] = df.iloc[random_index], df.iloc[j]

    @staticmethod
    def prepare_data(data: pd.DataFrame, split_ratio=0.7):
        df = data.copy()
        ProcessingData.normalize(df)
        ProcessingData.shuffle(df)
        return ProcessingData.split(df, split_ratio)