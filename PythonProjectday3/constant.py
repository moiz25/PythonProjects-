import math

# Define constant for the value of PI
PI = math.pi

# Function to calculate circumference
def calculate_circumference(radius):
    return 2 * PI * radius

# Main function
def main():
    try:
        # Get user input for radius
        radius = float(input("Enter the radius of the circle: "))
        
        # Calculate circumference
        circumference = calculate_circumference(radius)
        
        # Print the result
        print("The circumference of the circle with radius", radius, "is:", circumference)
    except ValueError:
        print("Please enter a valid number for the radius.")

if __name__ == "__main__":
    main()
