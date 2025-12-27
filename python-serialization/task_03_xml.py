#!/usr/bin/python3
"""
This module handles XML serialization and deserialization
of a basic Python dictionary using xml.etree.ElementTree.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): The data to serialize.
        filename (str): The name of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)  # Ensure all values are strings

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception:
        pass


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a dictionary.

    Args:
        filename (str): The name of the input XML file.

    Returns:
        dict: The deserialized data as a dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return {child.tag: child.text for child in root}
    except Exception:
        return {}
