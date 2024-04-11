# List of hangman game stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Importing the random module to choose a random word
import random
# List of possible words
word_list = ["python", "banana", "computer", "elephant", "sunflower", "guitar", "ocean", "mountain", "pizza", "book"]
# Randomly choose a word from the list
chosen_word = random.choice(word_list)
print(f"\n The chosen word is {chosen_word}.")  # Display the chosen word (for debugging purposes)
# Create a list of underscores to represent the word to be guessed
display = []
for __ in chosen_word:
    display += "_"

# Guessing system
lives = 6  # Number of lives

end_game = False  # Initialize the variable that controls the end of the game
while not end_game:  # Main game loop
    guess = input("Guess a letter: ").lower()  # Prompt the player to guess a letter
    for position in range(len(chosen_word)):  
        letter = chosen_word[position]  
        if guess == letter:  
            display[position] = guess  # Update the display with the correct letter
        
    if guess not in chosen_word:  # If the guessed letter is not in the word
        lives -= 1  # Decrease the number of lives
        print(f"You are wrong, you have {lives} lives left")  # Inform the player how many lives are left
        if lives == 0:  # If lives run out
            end_game = True  # End the game
            print("You lose the game")  

    if "_" not in display:  # If there are no more underscores in the display (all letters have been guessed)
        end_game = True  # End the game
        print("You win the game")

    print(stages[lives])  # Show the current stage of the game (the image corresponding to the remaining lives)
    print(display)  # Show the updated display
