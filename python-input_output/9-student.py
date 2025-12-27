#!/usr/bin/python3
"""
Defines a simple Student class.
"""


class Student:
    """
    Student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize student info."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return attributes as a dictionary."""
        return self.__dict__
