#!/usr/bin/python
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
rand_name = random.randint(0,len(names)-1)

payer = names[rand_name]
print(f"{payer} is going to pay the bill today, unfortunately!. lol")
