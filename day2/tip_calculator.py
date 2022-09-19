#!/usr/bin/python

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_persons = int(input("How many people are to split the bill? "))

#Here the calculations begin
total_bill = bill * ((percent_tip + 100)/100)
each_pay = total_bill / no_persons

print(f"Each person should pay: ${each_pay}")
