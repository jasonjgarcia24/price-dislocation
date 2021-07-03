# -*- coding: utf-8 -*-
"""Validator Suite for Specified Folder and CSV Filename.

This contains functions for verifying folder name and CSV filename defintions
exist.
"""
import os

from pathlib import Path

not_csv_ext_str      = "Please enter a file with extension '.csv' (Ctrl+C to escape)."
not_csv_exist_str    = "Please enter an existing .csv file (Ctrl+C to escape)."
csv_no_overwrite_str = "Please enter a .csv file that does not already exist (Ctrl+C to escape)."
not_path_str         = "The path is not valid (Ctrl+C to escape)."


def csv_ext_validator(file_name):
    """Verifies the string FILE_NAME contains a valid path and a .csv
    extension.

    Args:
        file_name (str): The string for .csv extension verification.

    Returns:
        response (bool|str): If file_name contains a .csv extension and the
        path is valid, response = True. Else, response = the appropriate string
        response.
    """
    csvpath_split = os.path.split(file_name)
    is_path       = prnt_path_validator(file_name)
    is_csv        = os.path.split(file_name)[-1].endswith(".csv")

    if is_csv and is_path: response = True
    elif not is_path:      response = not_path_str
    else:                  response = not_csv_ext_str

    return response


def csv_exist_validator(file_name):
    """Verifies the string FILE_NAME contains a valid path and an existing .csv
    file.

    Args:
        file_name (str): The string for .csv extension verification.

    Returns:
        response (bool|str): If file_name is a .csv file and the path is valid, response = True.
        Else, response = the appropriate string response.
    """
    csvpath_split = os.path.split(file_name)
    is_path       = prnt_path_validator(file_name)
    is_csv        = os.path.split(file_name)[-1].endswith(".csv") and Path(file_name).exists()

    if is_csv and is_path: response = True
    elif not is_path:      response = not_path_str
    else:                  response = not_csv_exist_str

    return response


def csv_no_overwrite_validator(file_name):
    """Verifies the string FILE_NAME contains a valid path and an existing .csv
    file, but not an existing .csv file.

    Args:
        file_name (str): The string for .csv extension verification.

    Returns:
        response (bool|str): If file_name is a .csv file and the path is valid but the .csv file
        does not exist, response = True. Else, response = the appropriate string response.
    """
    csvpath_split = os.path.split(file_name)
    is_path       = prnt_path_validator(file_name)
    is_csv        = os.path.split(file_name)[-1].endswith(".csv")
    is_exist      = Path(file_name).exists()

    if is_csv and is_path and not is_exist : response = True
    elif not is_path:                        response = not_path_str
    elif not is_csv:                         response = not_csv_ext_str
    else:                                    response = csv_no_overwrite_str

    return response


def prnt_path_validator(file_name):
    """Verifies the string FILE_NAME contains a valid path.

    Args:
        file_name (str): The string for path verification.

    Returns:
        response (bool): If file_name contains a valid path, response = True.
    """
    csvpath_split = os.path.split(file_name)
    response      = os.path.isdir("".join(csvpath_split[0]))

    return response