from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

jawaban = "yes"

while jawaban == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # def encrypt(original_text, shift_amount):
    #      cipher_text = ""
    #      for letter in original_text:
    #          shifted_position = alphabet.index(letter) + shift_amount
    #          shifted_position %= len(alphabet)
    #          cipher_text += alphabet[shifted_position]
    #      print(f"Here is the encoded result: {cipher_text}")


    # def decrypt(original_text, shift_amount):
    #     cipher_text = ""
    #     for letter in original_text:
    #         shifted_position = alphabet.index(letter) - shift_amount
    #         shifted_position %= len(alphabet)
    #         cipher_text += alphabet[shifted_position]
    #     print(f"Here is the decoded result: {cipher_text}")

    #menggabungkan
    def caesar(original_text, shift_amount, direction):
        chiper_text = ""
        if direction == "encode":
            shift_amount *= -1

        for letter in original_text:
            if letter in alphabet:    
                shifted_position = alphabet.index(letter) - shift_amount
                shifted_position %= len(alphabet)
                chiper_text += alphabet[shifted_position]
            else:
                chiper_text += letter
        print(f"Here is the {direction} result: {chiper_text}")
    caesar(original_text=text, shift_amount=shift, direction=direction)
    jawaban = input("Apakah kamu ingin mengulang? ").lower()

print("Thank You")
