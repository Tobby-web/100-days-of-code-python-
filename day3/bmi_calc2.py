#!/usr/bin/python

height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kilograms? "))

bmi = weight / (height ** 2)
bmi_r = round(bmi, 2)
print("\n")
print(f"Your BODY MASS INDEX is {bmi_r}")
if bmi_r < 18.5:
	print("Hence you're UNDERWEIGHT.")
elif bmi_r < 25:
	print("Hence you have a NORMAL weight.")
elif bmi_r < 30:
	print("Hence you're OVERWEIGHT.")
elif bmi_r < 35:
	print("Hence you're OBESE")
else:
	print("This means you're CLINICALLY OBESE")
