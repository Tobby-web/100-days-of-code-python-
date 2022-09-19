#!/usr/bin/python

age = float(input("How old are you? "))

years_left = 90 - age

months_left = years_left * 12

weeks_left = years_left * 52

days_left = years_left * 365

print(f"YOu have the {years_left} years left to live. That means you have {weeks_left} weeks or {days_left} days left.\nOur assumptions are that you have a lifespan of 90 years. Dark!!")
