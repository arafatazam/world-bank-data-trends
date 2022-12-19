#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
World bank data analysis
@author: Muhammad Arafat Azam (id: 21087019)
"""

import pandas as pd


def main():
    df = pd.read_excel('wb_data.xlsx', index_col=[0, 1])
    print(df.head())


if __name__ == "__main__":
    main()
