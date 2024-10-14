import json


def userData():
    # Path to your JSON file
    file_path = 'C:/Users/Change Me/Desktop/Swags/TestData/user.json'

    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)  # Parse JSON into a Python dictionary
        return data


