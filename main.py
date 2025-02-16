#Password Generator Project
import random
from random import choice

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


#first choose at random what you letters or symbols or numbers

total_chars = nr_letters+nr_symbols+nr_numbers
# print(total_chars)
password_chars = []
password_complete = ""

for n in range(0, nr_letters):
    password_chars.append(random.choice(letters))
for n in range(0, nr_numbers):
    password_chars.append(random.choice(numbers))
for n in range(0, nr_symbols):
    password_chars.append(random.choice(symbols))

while total_chars>0:
    # print(password_chars)
    char = random.choice(password_chars)
    # print(char)
    password_chars.remove(char)
    # print(password_chars)
    password_complete += char
    total_chars -= 1

print(password_complete)