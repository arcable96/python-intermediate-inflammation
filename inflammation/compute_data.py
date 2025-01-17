"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views

def load_inflammation_data(data_dir, filename="inflammation*.csv"):
    """Load data from a directory

    data_dir: directory name
    filename: name of file stored in directory
    """
    data_file_paths = glob.glob(os.path.join(data_dir, filename))
    if len(data_file_paths) == 0:
        raise ValueError(f"No inflammation data CSV files found in path {data_dir}")
    data = map(models.load_csv, data_file_paths)
    data = list(data)
    return data

def analyse_data(data_dir,filename="inflammation*.csv"):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means.

    data_dir: directory name
    filename: names of file. Default is "inflammation*.csv" (accesses all "inflammation.csv" files in directory)
    """

    data=load_inflammation_data(data_dir,filename)

    means_by_day_matrix = np.stack(list(models.daily_mean(data)))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)

    return means_by_day_matrix
