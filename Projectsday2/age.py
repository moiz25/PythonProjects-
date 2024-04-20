def main():
    # Ask the user for their age
    age = int(input("Please enter your age: "))
    
    # Check if the age is even or odd
    if age % 2 == 0:
        print("Your age", age, "is even.")
    else:
        print("Your age", age, "is odd.")

if __name__ == "__main__":
    main()
