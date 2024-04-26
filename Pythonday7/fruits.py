def main():
    # Create an empty list to store the fruits
    fruits = []

    # Prompt the user to input 5 fruits
    for i in range(5):
        fruit = input(f"Enter fruit {i+1}: ")
        fruits.append(fruit)

    # Print each fruit in the list
    print("List of fruits:")
    for fruit in fruits:
        print(fruit)

if __name__ == "__main__":
    main()
