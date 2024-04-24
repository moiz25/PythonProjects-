import random

def guess_number():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Ask the user to guess the number
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue
            if guess == secret_number:
                print("Congratulations! You guessed the correct number.")
                break
            else:
                print("Wrong guess. Try again!")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_number()
