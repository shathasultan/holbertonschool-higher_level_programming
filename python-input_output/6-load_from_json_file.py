#!/usr/bin/python3
"""
This module provides a function to load data from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Load data from a JSON file and return the corresponding Python object.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object resulting from parsing the JSON content.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
