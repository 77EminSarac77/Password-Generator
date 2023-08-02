import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '*', '+', '&', '(', ')']

print('Welcome to the Password Generator.')
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
count_letter = 0
count_symbol = 0
count_number = 0
run = 0
password_length = num_letters + num_numbers + num_symbols
password = ''
while len(password) != password_length:
    num_rand = random.randint(1, 3)
    if num_rand == 1:
        if count_letter < num_letters:
            password += letters[random.randint(0, len(letters) - 1)]
            count_letter += 1

    if num_rand == 2:
        if count_symbol < num_symbols:
            password += symbols[random.randint(0, len(symbols) - 1)]
            count_symbol += 1

    if num_rand == 3:
        if count_number < num_numbers:
            password += numbers[random.randint(0, len(numbers) - 1)]
            count_number += 1
    run += 1
print('Generated Password:', password)

