#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
World bank data analysis
@author: Muhammad Arafat Azam (id: 21087019)
"""

import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap


def corr_heat_map(data: pd.DataFrame, country: str):
    df = data.xs(country, level=1)
    df = df.dropna(axis='columns')
    df = df.T
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(8, 8))
    im = ax.imshow(corr, interpolation='nearest', cmap='RdYlGn')
    fig.colorbar(im, orientation='vertical', fraction=0.05)
    ax.set_xticklabels(['']+["\n".join(wrap(x, 30))
                       for x in corr.columns.to_list()], rotation=90, fontsize=8)
    ax.set_yticklabels(['']+["\n".join(wrap(x, 30))
                       for x in corr.index.to_list()], rotation=0, fontsize=8)
    for i in range(len(corr.index)):
        for j in range(len(corr.columns)):
            text = ax.text(j, i, round(corr.to_numpy()[i, j], 2),
                           ha="center", va="center", color="black")
    plt.tight_layout()
    plt.show()


def greenhouse_gas_emission_barchart(data: pd.DataFrame):
    df = data.loc["Total greenhouse gas emissions (kt of CO2 equivalent)"]
    years = ["1990", "1995", "2000", "2005", "2010", "2015"]
    df = df[years]
    ax = df.plot(kind='bar', rot=20, figsize=(12,12))
    ax.set_title('Total greenhouse gas emissions')
    ax.set_xlabel('Countries')
    ax.set_ylabel('kt of CO2 equivalent')
    ax.get_figure().set_size_inches(6, 5)
    plt.tight_layout()
    plt.show()


def main():
    df = pd.read_excel('wb_data.xlsx', index_col=[0, 1])
    greenhouse_gas_emission_barchart(df)
    corr_heat_map(df, "United Kingdom")


if __name__ == "__main__":
    main()
