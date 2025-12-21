import art

def tambah(n1, n2):
    return n1 + n2


def kurang(n1, n2):
    return n1 - n2


def kali(n1, n2):
    return n1 * n2


def bagi(n1, n2):
    return n1 / n2

operasi = {
    "+": tambah,
    "-": kurang,
    "*": kali,
    "/": bagi,
}
def kalkulator():
    print(art.logo)
    a = float(input("Masukan angka pertama: "))

    while True:
        for simbol in operasi:
            print(simbol)
        b = input("Masukan simbol aritmatika yang ingin anda gunakan: ")
        c = float(input("Masukan angka kedua: "))
        jawaban = operasi[b](a, c)
        print(f"{a} {b} {c} = {jawaban}")

        ulang = input(f"Ketik 'y' untuk melanjutkan perhitungan dengan {jawaban}, atau ketik 'n' untuk memulai perhitungan baru dan 'x' untuk kerluar: ")

        if ulang == "y":
            a = jawaban
        elif 'n':
            kalkulator()
        else:
            break
kalkulator()


