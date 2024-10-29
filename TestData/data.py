import json
import os


def userData():

    file_path = os.path.join(os.path.dirname(__file__), 'user.json')

    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)  # Parse JSON into a Python dictionary
        return data


