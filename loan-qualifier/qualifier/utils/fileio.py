# -*- coding: utf-8 -*-
"""FileIO Suite for CSV File Import/Export Operations.

This contains functions for loading CSV saving written CSV files.
"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        data (list): A list of lists that contains the rows of data from the
        CSV file.
    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csvpath, data):
    """Writes the CSV file from path provided.

    Args:
        csvpath (str): The csv file path.
        data (list): A list that contains the rows of data from for the CSV
        file.

    Returns:
        result (bool): A result status of the csv save. This can beused for
        verifying expections and allows for ease of use with pytest.
    """
    print(f"Saving your data to {csvpath}")
    with open(csvpath, mode='w', newline='') as data_file:
        data_writer = csv.writer(data_file, delimiter=',')
        data_writer.writerows(data)

    result = True

    return result

