"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
from fileinput import filename

import numpy as np

from inflammation import models, views

class JSONDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_inflammation_data(self):
        """Load data from a directory

        data_dir: directory name
        filename: name of file stored in directory
        """
        data_file_paths = glob.glob(os.path.join(self.data_dir, "inflammation*.json"))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in path {self.data_dir}")
        data = map(models.load_json, data_file_paths)
        data = list(data)
        return data

class CSVDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_inflammation_data(self):
        """Load data from a directory

        data_dir: directory name
        filename: name of file stored in directory
        """
        data_file_paths = glob.glob(os.path.join(self.data_dir, "inflammation*.csv"))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.data_dir}")
        data = map(models.load_csv, data_file_paths)
        data = list(data)
        return data

def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means.

    data_dir: directory name
    filename: names of file. Default is "inflammation*.csv" (accesses all "inflammation.csv" files in directory)
    """

    data=data_source.load_inflammation_data()

    means_by_day_matrix = np.stack(list(models.daily_mean(data)))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }

    views.visualize(graph_data)