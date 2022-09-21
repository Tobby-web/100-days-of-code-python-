#!/usr/bin/python
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

#Here the code begins with the supplied input.
bill = 0

#This accounts for the size of pizza chosen and choice of pepperoni for 
#the different sizes of pizza
if size == "S":
	bill += 15
	if add_pepperoni == "Y":
		bill += 2
elif size == "M":
	bill += 20
	if add_pepperoni == "Y":
		bill += 3
elif size == "L":
	bill += 25
	if add_pepperoni == "Y":
		bill += 3
else:
	print("Please input the correct data from the given options.")
	
#This accounts for the Extra cheese
if extra_cheese == "Y":
	bill += 1
	
print(f"Your final bill is ${bill}")
	

