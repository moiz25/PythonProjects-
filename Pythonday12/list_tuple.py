# Define a list of tuples
list_of_tuples = [(1, 5), (3, 2), (2, 7), (4, 1)]

# Sort the list of tuples by the second item in each tuple
sorted_list = sorted(list_of_tuples, key=lambda x: x[1])

# Print the sorted list
print("Sorted list of tuples by the second item:")
print(sorted_list)
