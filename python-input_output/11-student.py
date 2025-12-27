#!/usr/bin/python3
"""
Defines a Student class with serialization and deserialization capabilities.
"""


class Student:
    """Represents a student with basic information."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                                    If None, return all attributes.

        Returns:
            dict: Dictionary of selected attributes.
        """
        if attrs is None:
            return self.__dict__

        return {
            key: value for key, value in self.__dict__.items()
            if key in attrs
        }

    def reload_from_json(self, json):
        """
        Replace all attributes of the instance using a dictionary.

        Args:
            json (dict): Dictionary with attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
