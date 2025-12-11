import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)

# memilih kata acak
chosen_word = random.choice(word_list)

# membuat garis bawah misal 'APEL' jadi '____'
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    # cek apakah sudah pernah diinput
    if guess in correct_letters:
        print(f"Kamu sudah pernah menginput huruf ini {guess}")
        continue# untuk lanjutkan langsung ke input gues

    if guess in chosen_word:
        correct_letters.append(guess)
        print(f"Kata yang anda tebak benar dan nyawamu sisa {lives}")
    else:
        lives -= 1
        print(f"Kamu salah menebak dan nyawamu dikurang satu sisa {lives}")
        #cek kalah
        if lives == 0:
            game_over = True
            print("You lose")

    # update tampilan display
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # cek menang
    if "_" not in display:
        game_over = True
        print("You win")

    # tampilkan gambar
    print(stages[lives])
