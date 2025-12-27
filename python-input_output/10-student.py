#!/usr/bin/python3
"""
Defines a Student class.
"""


class Student:
    """Student with basic information."""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the student."""
        if attrs is None:
            return self.__dict__

        return {
            key: getattr(self, key)
            for key in attrs
            if hasattr(self, key)
        }
