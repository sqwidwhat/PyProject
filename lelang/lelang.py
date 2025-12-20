from art import logo

print(logo)


def cariPenawaranTertinggi(paraPenawar):
    penawaranTertinggi = 0
    pemenang = ""
    for peserta in paraPenawar:
        jumlahPenawaran = paraPenawar[peserta]
        if jumlahPenawaran > penawaranTertinggi:
            penawaranTertinggi = jumlahPenawaran
            pemenang = peserta
    print(f"Pemenangnya adalah {pemenang} dengan tawaran sebesar ${penawaranTertinggi}")


tawaran = {}
lanjutLelang = True

while lanjutLelang:
    nama = input("Masukan nama anda: ").lower()
    penawaran = int(input("Masukan jumlah penawaran anda: $"))
    tawaran[nama] = penawaran
    jawaban = input("Apakah ada penawaran lain? 'ya' atau 'tidak' ")
    if jawaban == "tidak":
        lanjutLelang = False
        cariPenawaranTertinggi(tawaran)
    elif jawaban == "ya":
        print("\n" * 5)

print(tawaran)