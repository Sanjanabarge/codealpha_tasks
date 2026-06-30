import random

# Step 1: Word list
words = ["apple", "tiger", "chair", "pizza", "robot"]

# Step 2: Random word
chosen_word = random.choice(words)

# Step 3: Create display
display = []

for letter in chosen_word:
    display.append("_")

# Step 4: Variables
lives = 6
guessed_letters = []

print("Welcome to Hangman!")

# Step 5: Game loop
while lives > 0 and "_" in display:

    print("\nWord:", " ".join(display))

    guess = input("Guess a letter: ").lower()

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in chosen_word:

        for position in range(len(chosen_word)):

            if chosen_word[position] == guess:
                display[position] = guess

        print("Correct!")

    # Wrong guess
    else:
        lives -= 1
        print("Wrong guess!")
        print("Lives left:", lives)

# Step 6: Result
if "_" not in display:
    print("\nCongratulations! You won!")
else:
    print("\nGame Over!")
    print("The word was:", chosen_word)
