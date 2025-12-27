#!/usr/bin/python3
"""
This module defines a CustomObject class with support for pickling (serialization) and deserialization.
"""

import pickle


class CustomObject:
    """
    CustomObject holds basic attributes and provides methods to
    serialize itself and deserialize from a file using pickle.
    """

    def __init__(self, name="", age=0, is_student=False):
        """
        Initialize the CustomObject.
        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a binary file.

        Args:
            filename (str): The name of the file to save the object to.
        Returns:
            None if serialization fails.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load a serialized object from a binary file.

        Args:
            filename (str): The name of the file to load from.
        Returns:
            CustomObject or None if deserialization fails.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
