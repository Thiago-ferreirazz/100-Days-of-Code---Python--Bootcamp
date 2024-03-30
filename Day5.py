#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

# Gera letras aleatórias conforme a quantidade especificada pelo usuário
for letter in range(1, nr_letters + 1):
    random_letters = random.choice(letters)
    password += random_letters

# Gera símbolos aleatórios conforme a quantidade especificada pelo usuário
for symbol in range(1, nr_symbols + 1):
    random_symbols = random.choice(symbols)
    password += random_symbols

# Gera números aleatórios conforme a quantidade especificada pelo usuário
for number in range(1, nr_numbers + 1):
    random_numbers = random.choice(numbers)
    password += random_numbers

# Embaralha a senha para aumentar sua segurança
password_list = list(password)
random.shuffle(password_list)
shuffled_password = ''.join(password_list)

# Exibe a senha embaralhada
print(f"\nSua nova senha: {shuffled_password}")
