# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define a function to print even numbers
def print_even_numbers(number_list):
    even_numbers = [num for num in number_list if num % 2 == 0]
    print("Even numbers in the list:", even_numbers)

# Call the function with the list of numbers
print_even_numbers(numbers)
