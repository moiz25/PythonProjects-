def min_max(numbers):
    if not numbers:
        return None  # Return None if the list is empty

    smallest = largest = numbers[0]  # Initialize smallest and largest to the first element of the list

    for num in numbers:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return (smallest, largest)

# Example usage:
user_list = [int(x) for x in input("Enter numbers separated by space: ").split()]
result = min_max(user_list)
print("Smallest and largest numbers:", result)
