import json

"""
Reads a JSON file and parses its content into a dictionary or list.

Parameters
----------
file_path: str
      Path to the JSON file.

Returns
-------
dict or list
      Parsed content of the JSON file as a dictionary or list, depending on the file's structure.
"""


def read_json_file(file_path: str) -> dict | list:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data