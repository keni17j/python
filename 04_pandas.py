"""
Pandas.
"""

import os
import sys

import numpy as np
import pandas as pd


def main():

    # Series
    #x = pd.Series([1,2,3,np.nan,5,6,7,8,9])
    #print(x)

    # Data Frame
    df = pd.DataFrame({"CIS": [1,5,3,7],
                      "USS": [6,9,2,6],
                      "MSNS": [4,7,5,8],})

    # view datas
    print(df)
    print(df.dtypes)
    print(df.head(2))
    print(df.tail(2))
    print(df.index)
    print(df.columns)
    print(df.to_numpy()) # only datas
    print(df.describe()) # simple statistics
    print(df.T) # transpose
    print(df.sort_index(axis=0,ascending=False)) # culmns
    print(df.sort_index(axis=1,ascending=False)) # index


def func():
    """
    ドックストリング
    """

    print('goobye')


if __name__ == '__main__':
    main()
