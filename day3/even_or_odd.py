#!/usr/bin/python

print("Welcome to the odd and even number checker")
number = int(input("Give me a whole number and I'll tell you if it is odd or even. "))
if number % 2 == 1:
	print(f"{number} is an odd number")
else:
	print(f"{number} is an even number")
