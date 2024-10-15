from ASCII_art_cipher import logo

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
def encrypt_decrypt_cipher(encode_or_decode, original_text, shift_amount):
    cipher_text = ""
    if encode_or_decode == 'decode':
        shift_amount *= -1

    letters_len = len(letters)
    for letter in original_text:
        if letter not in letters:
            cipher_text += letter
        else:
            new_index = letters.index(letter) + shift_amount
            new_index %= letters_len
            cipher_text += letters[new_index]

    return cipher_text


print(logo)
yes_or_no = True
while yes_or_no:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    print(f"Here is the result : {encrypt_decrypt_cipher(direction, text, shift)}")

    choice = input("Type 'yes' to continue, 'no' otherwise : ").lower()
    if choice != "yes":
        yes_or_no = False
        print("Goodbye!")
