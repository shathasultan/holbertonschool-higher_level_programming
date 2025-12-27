"""
This module provides basic serialization and deserialization functions.
It allows saving a Python dictionary to a JSON file and loading it back
from the JSON file into a Python dictionary.
"""

import json

def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary and save it to a JSON file."""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """Load JSON from file and return it as a dictionary."""
    with open(filename, 'r') as json_file:
        return json.load(json_file)
