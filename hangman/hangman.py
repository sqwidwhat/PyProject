import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

# memilih kata acak
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game_over = False
correct_letters = []
# Tambahan: List untuk menyimpan SEMUA tebakan (agar tidak kena denda 2x kalau salah nebak huruf yg sama)
all_guesses = [] 
lives = 6

# Setup tampilan awal
print("_" * word_length)

while not game_over:
    guess = input("Guess a letter: ").lower()

    # 1. CEK DUPLIKAT (Cek di list all_guesses)
    if guess in all_guesses:
        print(f"Kamu sudah pernah mencoba huruf '{guess}', coba huruf lain.")
        continue
    
    # Masukkan tebakan ke daftar riwayat
    all_guesses.append(guess)

    # 2. LOGIKA BENAR / SALAH
    if guess in chosen_word:
        correct_letters.append(guess)
        print(f"Benar! Nyawamu masih {lives}")
    else:
        lives -= 1
        print(f"Salah! Huruf '{guess}' tidak ada. Nyawamu sisa {lives}")
        
        # Cek Kalah
        if lives == 0:
            game_over = True
            print("You lose!")
            # Memberi tahu kata yang benar saat kalah
            print(f"Jawabannya adalah: {chosen_word}")

    # 3. UPDATE TAMPILAN DISPLAY
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(display)

    # 4. CEK MENANG
    if "_" not in display:
        game_over = True
        print("You win!")

    # 5. PRINT GAMBAR
    print(stages[lives])