def add_item_to_tuple(original_tuple, item):
    new_tuple = original_tuple + (item,)
    return new_tuple

# Example usage:
original_tuple = (1, 2, 3, 4)
item_to_add = 5
updated_tuple = add_item_to_tuple(original_tuple, item_to_add)
print("Original tuple:", original_tuple)
print("Updated tuple:", updated_tuple)
