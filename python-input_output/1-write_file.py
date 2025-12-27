#!/usr/bin/python3
"""Module that defines a function to write text to a file."""


def write_file(filename="", text=""):
    """Writes text to a file and returns the number of characters written."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
