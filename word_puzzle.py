# 1. Choose a secret word (must be lowercase)
secret_word = "mosiah"

print("Welcome to the word puzzle game!")

# Generate the initial hint dynamically using a loop
initial_hint = ""
for letter in secret_word:
    initial_hint += "_ "

# Display the initial hint right when the game starts
print(f"Your hint is: {initial_hint}")

# 2. Initialize the guess count and get the first guess
guess_count = 1
guess = input("What is your guess? ").lower()

# 3. Loop while the guess is wrong
while guess != secret_word:
    print("Your guess was not correct.")
    
    # ALWAYS initialize the hint text here so line 35 never crashes
    hint = ""
    
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        # Fill the hint with blank underscores if the length doesn't match
        for letter in secret_word:
            hint += "_ "
    else:
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                hint += guess[i].upper() + " "
            elif guess[i] in secret_word:
                hint += guess[i].lower() + " "
            else:
                hint += "_ "
                
    print(f"Your hint is: {hint}")
    guess = input("What is your guess? ").lower()
    guess_count += 1

# 4. Success message when they finally break out of the loop
print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")
