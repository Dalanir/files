import pandas as pd
import numpy as np

def generate_numeric_column(df, value):
    df[value.column_name] = np.random.randint(
        low=value.min, high=value.max*10**value.digits, size=len(df))/10**value.digits 

    return df


def generate_breakdown_column(df, label):
    list_of_df = []
    for group_value in label.values_list:
        df[label.column_name] = group_value
        list_of_df += [df.copy()]
    return pd.concat(list_of_df)
