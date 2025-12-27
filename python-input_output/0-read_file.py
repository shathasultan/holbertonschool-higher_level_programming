#!/usr/bin/python3
"""Module that defines a function to read a file and print its contents."""


def read_file(filename=""):
    """Reads and prints the contents of a text file."""
    with open(filename) as file:
        info = file.read()
        print(info, end="")
