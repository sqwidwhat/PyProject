from art import logo

print(logo)


def cari_pemenang_lelang(data_tawaran):
    tawaran_tertinggi = 0
    pemenang = ""

    for peserta in data_tawaran:
        jumlah_tawaran = data_tawaran[peserta]
        if jumlah_tawaran > tawaran_tertinggi:
            tawaran_tertinggi = jumlah_tawaran
            pemenang = peserta

    print(f"Pemenangnya adalah {pemenang} dengan tawaran sebesar ${tawaran_tertinggi}")


data_lelang = {}
lanjut_lelang = True

while lanjut_lelang:
    nama = input("Siapa nama Anda?: ")
    harga = int(input("Berapa tawaran Anda?: $"))
    #nambah data dalam dictionary
    data_lelang[nama] = harga

    lanjut = input("Apakah ada penawar lain? Ketik 'yes' atau 'no'.\n")
    if lanjut == "no":
        lanjut_lelang = False
        cari_pemenang_lelang(data_lelang)
    elif lanjut == "yes":
        print("\n" * 5)