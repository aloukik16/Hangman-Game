# Hangman Game
import random
from words import word_list
from arts import stages, banner_logo


lives = 6

print(banner_logo)

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("word to guess: ", placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"********************<???>/{lives} lives left<???> *********************")
    guess = input("Enter a letter: ").lower()


    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else :
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("************** YOU LOSE **************")
            print("The word was => ", chosen_word)


    if "_" not in display:
        game_over = True
        print("************** YOU WIN **************")

    print(display)
    print(stages[lives])