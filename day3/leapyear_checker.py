#!/usr/bin/python

print("Welcome to the Leap Year Checker")
year = int(input("Input any year: "))

test1 = year % 4
test2 = year % 100
test3 = year % 400

if test1 == 0:
	if test2 != 0:
		print(f"{year} is a leap year")
	else:
		if test3 == 0:
			print(f"{year} is a leap year")
		else:
			print(f"{year} is not a leap year")
else:
	print(f"{year} is not a leap year")
