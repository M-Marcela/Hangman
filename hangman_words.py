from replit import clear
import random

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guess_list = []

import hangman_art
print (hangman_art.logo)
#Testing code
# print(f'\nPssst, the solution is {chosen_word}.\n')

display = []
for letter in chosen_word:
    display += "_"

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    clear()
    print (f"You guess letter {guess}.")
    if guess in guess_list:
        print(f"You've already guessed the letter {guess}.")
    guess_list += guess
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print (f"The letter {guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was \'{chosen_word}\'")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
