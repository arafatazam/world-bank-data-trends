#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
World bank data analysis
@author: Muhammad Arafat Azam (id: 21087019)
"""

import pandas as pd
import matplotlib.pyplot as plt


def greenhouse_gas_emission_barchart(df: pd.DataFrame):
    df = df.loc["Total greenhouse gas emissions (kt of CO2 equivalent)"]
    years = ["1990", "1995", "2000", "2005", "2010", "2015"]
    df = df[years]
    ax = df.plot(kind='bar', rot=20)
    ax.set_title('Total greenhouse gas emissions')
    ax.set_xlabel('Countries')
    ax.set_ylabel('kt of CO2 equivalent')
    ax.get_figure().set_size_inches(6, 5)
    plt.show()


def main():
    df = pd.read_excel('wb_data.xlsx', index_col=[0, 1])
    greenhouse_gas_emission_barchart(df)


if __name__ == "__main__":
    main()
