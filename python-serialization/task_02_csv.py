#!/usr/bin/python3
"""
This module provides a function to convert a CSV file to a JSON file.
Each row in the CSV is read as a dictionary and written as a JSON array.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Converts a CSV file to a JSON file named 'data.json'.

    Args:
        filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if conversion is successful, False if an error occurs.
    """
    try:
        with open(filename, "r", encoding="utf-8") as cfile:
            reader = csv.DictReader(cfile)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as dfile:
            json.dump(data, dfile, indent=4)
            return True

    except Exception:
        return False
