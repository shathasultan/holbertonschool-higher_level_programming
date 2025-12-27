#!/usr/bin/python3
"""Module that defines a function to save an object to a JSON file."""

import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a file in JSON format.

    Args:
        my_obj (object): The Python object to save.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
