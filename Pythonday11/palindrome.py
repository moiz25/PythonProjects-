def is_palindrome(word):
    # Convert the word to lowercase to ignore case
    word = word.lower()
    
    # Remove spaces and punctuation from the word
    word = ''.join(char for char in word if char.isalnum())
    
    # Check if the word is equal to its reverse
    return word == word[::-1]

# Test the function
word = input("Enter a word: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
