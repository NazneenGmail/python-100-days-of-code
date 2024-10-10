import random
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print("Welcome to the PyPassword Generator!")
password_string = ''
uc_letters_cnt = int(input("How many uppercase letters would you like in your password : "))
uc_letters_len = len(uppercase_letters)
for letter_no in range(0, uc_letters_cnt):
    password_string += uppercase_letters[random.randint(0, uc_letters_len-1)]

letters_cnt = int(input("How many lowercase letters would you like in your password? : "))
letters_len = len(lowercase_letters)
for letter_no in range(0, letters_cnt):
    password_string += lowercase_letters[random.randint(0, letters_len-1)]

symbols_len = len(symbols)
symbols_cnt = int(input("How many symbols would you like? : "))
for symbol_no in range(0, symbols_cnt):
    password_string += symbols[random.randint(0, symbols_len-1)]

numbers_len = len(numbers)
numbers_cnt = int(input("How many numbers would you like? : "))
for number_no in range(0, numbers_cnt):
    password_string += numbers[random.randint(0, numbers_len-1)]

print(f"Easy to guess password : {password_string}")

list_password = list(password_string)
random.shuffle(list_password)
hard_password = ''.join(list_password)
print(f"Hard to guess password : {hard_password}")