import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the dice rolling simulator!")
    input("Press Enter to roll the dice...")

    result = roll_dice()
    print(f"You rolled: {result}")

if __name__ == "__main__":
    main()
