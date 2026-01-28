def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0: #Jika num habis dibagi i
            return False
    return True

angka = int(input("Masukan angka: "))
print(is_prime(angka))