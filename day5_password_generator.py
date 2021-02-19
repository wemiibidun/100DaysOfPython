#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n"))

letter_pswd = ''
for letter in range(0,nr_letters):
  letter_index = random.randint(0,len(letters)-1)
  letter_pswd += letters[letter_index]
#print(letter_pswd)

#Another method
#for char in range(1, nr_letters + 1):
  #password += random.choice(letters)
#for char in range(1, nr_letters + 1):
  #password_list.append(random.choice(letters)  ) 

nr_symbols = int(input(f"How many symbols would you like?\n"))

symbol_pswd = ''
for symbol in range(0,nr_symbols):
  symbol_index = random.randint(0,len(symbols)-1)
  symbol_pswd += symbols[symbol_index]
#print(symbol_pswd)

nr_numbers = int(input(f"How many numbers would you like?\n"))

number_pswd = ''
for i in range(0,nr_numbers):
  number_index = random.randint(0,len(numbers)-1)
  number_pswd += numbers[number_index]
#print(number_pswd)


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = letter_pswd + symbol_pswd + number_pswd
print(f"Your password is: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#password = letter_pswd + symbol_pswd + number_pswd
#randomised_password = list(password)
#random.shuffle(randomised_password)
#print(''.join(randomised_password))

