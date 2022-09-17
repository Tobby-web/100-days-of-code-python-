#!/usr/bin/python

#input the given set of numbers
number = input("Give me any number of your choice and I'll give you the sum.\n ")

#calculate the length of the string to use in a for loop
length_of_number = len(number)


#create a for loop that runs through the list, converts to string and adds them to a variable

for i in number:
	sum = 0
	n = int(i)
	sum = sum + n
print(sum)
