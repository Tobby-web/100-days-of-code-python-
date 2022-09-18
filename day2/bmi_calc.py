#!/usr/bin/python

weight = input("What is your weight in kilogram? ")
height = input("what is your height in meters? " )

w = float(weight)
h = float(height)

bmi = w/(h**2)

print(f"Okay. Here it is:\nYour Body Mass Index is: {bmi}")
