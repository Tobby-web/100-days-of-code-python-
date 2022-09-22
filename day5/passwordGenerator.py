#!/usr/bin/python

#Password Generator Project
import random
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
#we do the hard stuff. We love the hard stuff.


#Select a random number, letter or symbol from the list above.
#r_letter = random.randint(0,len(letters) - 1)
#r_number = random.randint(0,len(numbers) - 1)
#r_symbols = random.randint(0,len(symbols) - 1)



#loop that randomly selects from the list above and adds them to the empty password list
password = []
for i in range(0,nr_letters):
	password.append(letters[random.randint(0,len(letters) - 1)])
	
for i in range(0, nr_symbols):
	password.append(symbols[random.randint(0,len(symbols) - 1)])
	
for i in range(0, nr_numbers):
	password.append(numbers[random.randint(0,len(numbers) - 1)])
#print(password)

#Aim scramble the password list and print it out.
random.shuffle(password)
shuffled_pass = ""
for i in password:
	shuffled_pass += i
print(shuffled_pass)
