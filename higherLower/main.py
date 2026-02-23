from game_data import data
from art import logo, vs
import random

def format_data(account):
    #Mengambil data akun dan mengembalikannya dalam format yang dapat dicetak.
    account_name  = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    #Mengambil tebakan user dan jumlah followers, lalu mengembalikan True jika benar, False jika salah.
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

score = 0
game_should_continue = True
# Ambil satu akun acak pertama kali untuk posisi B
account_b = random.choice(data)
while game_should_continue:
    # AKSI 1: Geser posisi. Pemenang sebelumnya (B) sekarang jadi (A)
    account_a = account_b
    account_b = random.choice(data)

    # AKSI 2: Pastikan A dan B tidak orang yang sama
    while account_a == account_b:
        account_b = random.choice(data)

    # AKSI 3: Tampilkan ke layar pakai fungsi format_data yang kamu buat tadi
    print(logo)
    print(f"Bandingkan A: {format_data(account_a)}")
    print(vs)
    print(f"Bandingkan b: {format_data(account_b)}")

    # AKSI 4: Minta tebakan user
    guess = input("Siapa yang lebih banyak fllowers?  'A' atau 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"Benar! Score kamu: {score}")
        print("\n" * 20)
    else:
        game_should_continue = False
        print(f"Salah! Final score kamu: {score}")



