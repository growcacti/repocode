#!/usr/bin/python3.6
# coding: utf-8

"""
brief description for this script
reference: https://pythonbasics.org/seaborn-heatmap/
"""

import matplotlib.pyplot as plt

# import pandas as pd
import numpy as np
import seaborn as sns


def test():
    """test"""
    np.random.seed(0)
    sns.set()
    uniform_data = np.random.rand(10, 12)
    _ = sns.heatmap(uniform_data, vmin=0, vmax=1)
    plt.show()


def main():
    """main"""
    test()


if __name__ == "__main__":
    main()
