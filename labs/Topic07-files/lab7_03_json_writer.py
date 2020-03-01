# Daniel Mc Callion
# This program saves a simple dict to a json

import json

filename = "testdict.json"
sample = dict(name="fred", age=31, grades=[1,34,55])

def write_dict(file_to_write, obj):
    with open(file_to_write, "wt") as f:
        json.dump(obj, f)

# Testing the function
write_dict(filename, sample)
