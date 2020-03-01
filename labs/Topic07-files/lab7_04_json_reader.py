# Daniel Mc Callion
# This program reads a dict object from a json file

import json
filename = "testdict.json"

def read_dict(file_to_open):
    # Throws an error if the file does not exist
    with open(file_to_open) as f:
        return json.load(f)

# Test the function
dict_in = read_dict(filename)
print(dict_in)
