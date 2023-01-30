#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
World bank data analysis
@author: Muhammad Arafat Azam (id: 21087019)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap


def read_data(file_name: str) -> pd.DataFrame:
    """
    Read data from the world bank data excel file
    World bank data bank tool was utilized to choose
    specific countries, attributes and years.
    """
    df = pd.read_excel(file_name, index_col=[0, 1])
    return df


def log_normalize(data: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize all the columns of a dataframe using logarithm function.
    It allows comparison among extremely diverse range of data.
    """
    df = data
    for col in data.columns:
        df[col] = np.log(df[col])
    return df


def corr_heat_map(data: pd.DataFrame, country: str):
    """
    Generates heat map from the correlation matrix among the attributes.
    """
    df = data.xs(country, level=1)
    df = df.dropna(axis='columns')
    df = df.T
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(8, 8))
    im = ax.imshow(corr, interpolation='nearest',
                   cmap='RdYlGn', vmin=-1, vmax=1)
    fig.colorbar(im, orientation='vertical', fraction=0.05)
    ax.set_xticklabels(['']+["\n".join(wrap(x, 30))
                       for x in corr.columns.to_list()], rotation=90, fontsize=8)
    ax.set_yticklabels(['']+["\n".join(wrap(x, 30))
                       for x in corr.index.to_list()], rotation=0, fontsize=8)
    for i in range(len(corr.index)):
        for j in range(len(corr.columns)):
            text = ax.text(j, i, round(corr.to_numpy()[i, j], 2),
                           ha="center", va="center", color="black")

    plt.title(f'Correlation - {country}')
    plt.tight_layout()
    plt.show()


def greenhouse_gas_emission_barchart(data: pd.DataFrame):
    """
    Generates barchart to show the increase and decrease of greenhouse gas emission
    over the years.
    """
    df = data.loc["Total greenhouse gas emissions (kt of CO2 equivalent)"]
    years = [f'{year}' for year in range(1991, 2020, 4)]
    df = df[years]
    df = log_normalize(df)
    ax = df.plot(kind='bar', rot=90, figsize=(10, 7))
    ax.set_title('Total greenhouse gas emissions')
    ax.set_xlabel('Countries')
    ax.set_ylabel('Total greenhouse gas emissions\nlog(kt) CO2 equivalent)')
    ax.set_ylim(ymin=11)
    ax.get_figure().set_size_inches(10, 7)
    plt.tight_layout()
    plt.show()


def main():
    df = read_data('wb_data.xlsx')
    greenhouse_gas_emission_barchart(df)

    countries = df.index.get_level_values(1).unique()
    for country in countries:
        corr_heat_map(df, country)


if __name__ == "__main__":
    main()
