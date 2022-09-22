#!/usr/bin/python

#this program would sum even numbers from 0 to any given number inputed
num =int(input("Up to what number do you want to get the sum of even numbers inbetween? "))
sum = 0
for i in range(0, num + 1):
	if i % 2 == 0:
		sum += i
print(f"Sum of the even numbers from 0 to {num} is {sum}.\nUnfortunately I didn't account for negative numbers.")
