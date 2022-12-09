"""Module for data preparation"""
import pandas as pd


def convert_cols_type(df: pd.DataFrame, features_l: list, type_: str):
    for feature in features_l:
        df[feature] = df[feature].astype(type_)
    return df