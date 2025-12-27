#!/usr/bin/python3
"""
This script adds command-line arguments to a JSON file.
If the file exists, it loads its content first.
"""

import json
import os
import sys

load_from_json = __import__("6-load_from_json_file").load_from_json_file
save_to_json = __import__("5-save_to_json_file").save_to_json_file


if __name__ == "__main__":
    """
    Main execution block.
    Loads existing items from a JSON file if it exists,
    then appends command-line arguments and saves them back.
    """
    file = "add_item.json"

    if os.path.exists(file):
        a_list = load_from_json(file)
    else:
        a_list = []

    a_list.extend(sys.argv[1:])
    save_to_json(a_list, file)
