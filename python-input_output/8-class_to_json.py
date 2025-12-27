#!/usr/bin/python3
"""
Converts an object to a dictionary for JSON serialization.
"""


def class_to_json(obj):
    """
    Get object's attributes as a dictionary.
    """
    return obj.__dict__
