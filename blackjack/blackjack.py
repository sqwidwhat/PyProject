import random
from art import logo
#mengambil angka random
def dealCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    kartu = random.choice(cards)
    return kartu

#menjumlahkan kartu
def calculate_score(jumlah):
    #cek apakah blackjack
    if sum(jumlah) == 21 and len(jumlah) == 2:
        return 0
    
    #cek apakah ada kartu 11 dan hasil lebih dari 21
    while 11 in jumlah and sum(jumlah) > 21:
        jumlah.remove(11)
        jumlah.append(1)
    
    hasil = sum(jumlah)
    return hasil

#untung membandingkan
def compare(userScore, computerScore):
    if computerScore == userScore:
        return "Seri"
    elif computerScore == 0:
        return "Anda Kalah"
    elif userScore == 0:
        return "Anda Menang"
    elif userScore > 21:
        return "Anda Kalah"
    elif computerScore > 21:
        return "Anda Menang"
    elif userScore > computerScore:
        return "Anda Menang"
    else:
        return "Anda Kalah"

def start():
    print(logo)
    user_cards = []
    computer_cards = []

    #untuk while cek kartu komputer karena sudah dipakai di whihle cek kartu user
    totalKartuKomputer = -1
    totalKartuUser = -1

    permainan = False

    #mengambil 2 angka secara acak
    for i in range(2):
        user_cards.append(dealCard())
        computer_cards.append(dealCard())

    while not permainan:
        totalKartuUser = calculate_score(user_cards)
        totalKartuKomputer = calculate_score(computer_cards)
        print(f"Kartu Anda: {user_cards}, skor saat ini: {totalKartuUser}")
        print(f"Kartu pertama komputer: {computer_cards[0]}")
        if totalKartuUser == 0 or totalKartuKomputer == 0 or totalKartuUser > 21:
            permainan = True
        else:   
            p2 = input("Ketik 'y' untuk mendapatkan kartu lain, ketik 'n' untuk melewati giliran: ").lower()
            if p2 == "y":
                user_cards.append(dealCard())
            else:
                permainan = True

    while totalKartuKomputer != 0 and totalKartuKomputer < 17:
        computer_cards.append(dealCard())
        totalKartuKomputer = calculate_score(computer_cards)

    print(f"Kartu terakhir Anda: {user_cards}, Skor: {totalKartuUser}")
    print(f"Kartu terakhir Komputer: {computer_cards}, Skor: {totalKartuKomputer}")
    print(compare(totalKartuUser, totalKartuKomputer))

while input("Apakah kamu ingin bermain ulang? Ketik 'y' atau 'n': ").lower() == "y":
    print("\n" * 20)
    start()