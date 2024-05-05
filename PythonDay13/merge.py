# Function to merge two dictionaries
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Make a copy of the first dictionary
    merged_dict.update(dict2)   # Update it with the second dictionary
    return merged_dict

# Example dictionaries to merge
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}

# Merging dictionaries
merged_dict = merge_dicts(dict1, dict2)

# Printing the merged dictionary
print("Merged dictionary:")
print(merged_dict)
