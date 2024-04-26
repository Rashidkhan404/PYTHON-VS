import random
word_list = ["apple", "orange", "mango"]
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    guessed_latter = input("GUSS A LETTER :")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_latter:
            display[position] = guessed_latter
    print(display)
    if guessed_latter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("YOU LOSE :")
    if '_' not in display:
        game_over = True
        print("YOU WIN :")
