import random
from ASCII_art_hangman import HANGMANPICS, logo
from HangmanWordsList import word_list

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

chosen_word_list = list(chosen_word)
chosen_word_len = len(chosen_word_list)

guessed_list = []
for letter in range(0, chosen_word_len):
    guessed_list += '_'
guessed_list_string = ''.join(guessed_list)
print(f"Can you guess letters in this word: {guessed_list_string}")

chances = 6
life = 0
correct_guess = False

game_over = False
while not game_over :
    print(f"-------------------{chances} / 6 Chances----------------------")
    print(HANGMANPICS[life])
    guess = str(input("Guess a letter : ")).lower()

    if guess in guessed_list:
        print(f"You already guessed: {guess}")
    else:
        for letter_index in range(0, chosen_word_len):
            if chosen_word_list[letter_index] == guess:
                guessed_list[letter_index] = guess
                correct_guess = True

        if not correct_guess:
            chances = chances - 1
            life += 1
            print(f"You guessed letter {guess}. It is not in the word. You lose a chance.")
            print(f"Chances reduced to : {chances}")

        correct_guess = False
        guessed_list_string = ''.join(guessed_list)
        print(f"Word: {guessed_list_string}")

        if not '_' in guessed_list:
            print("You guessed the word correct.")
            game_over = True

        if chances == 0:
            print(f"You lose. No chances left. It was {chosen_word}")
            game_over = True
