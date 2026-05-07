import random

# Predefined list of words
words = ["python", "apple", "computer", "science", "gaming"]

# Randomly choose a word
secret_word = random.choice(words)

# Create empty spaces for guessed letters
guessed_word = ["_"] * len(secret_word)

# Store guessed letters
guessed_letters = []

# Maximum incorrect attempts
max_attempts = 6
wrong_attempts = 0

print("===================================")
print("      WELCOME TO HANGMAN GAME      ")
print("===================================")

# Game loop
while wrong_attempts < max_attempts and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", guessed_letters)
    print("Remaining Attempts:", max_attempts - wrong_attempts)

    # Take input from user
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter only ONE alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check if letter exists in word
    if guess in secret_word:
        print(" Correct Guess!")

        # Reveal correct letters
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        print(" Wrong Guess!")
        wrong_attempts += 1

# Final result
print("\n===================================")

if "_" not in guessed_word:
    print(" Congratulations! You Won!")
    print("The word was:", secret_word)
else:
    print(" Game Over!")
    print("The correct word was:", secret_word)

print("===================================")