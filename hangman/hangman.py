import random
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
game_over = False
remaining_lives = 6
from hangman_art import logo
print(logo)
display = []
for _ in range(word_length):
    display += "_"
while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        remaining_lives -= 1
        if remaining_lives == 0:
            game_over = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        game_over = True
        print("You win.")
    from hangman_art import stages
    print(stages[remaining_lives])
