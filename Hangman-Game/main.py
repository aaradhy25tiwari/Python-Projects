import random

words = ['python', 'java', 'kotlin', 'javascript', 'html', 'ruby', 'swift']

# Randomly select a word from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
attempts = 6

print("Welcome to Hangman!")
while attempts > 0 and '_' in word_display:
    print("\n" + " ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character.")
        continue

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")
# Completion of the game
if '_' not in word_display:
    print(f"\nCongratulations! You've guessed the word: {chosen_word}")
else:
    print(f"\nGame over! The word was: {chosen_word}")
