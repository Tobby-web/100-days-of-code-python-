#!/usr/bin/python
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

#Calculate the number of times "True" appears in the names.
t = 0
l = 0
for i in "true":
	n1 = name1.count(i)
	t += n1
	n2 = name2.count(i)
	t += n2
for i in "love":
	n1 = name1.count(i)
	l += n1
	n2 = name2.count(i)
	l += n2
compactibility = int(str(t) + str(l))

#print(type(compactibility))
#print(compactibility)

print(f"Your score is {compactibility}%")
if compactibility < 10 or compactibility > 90:
	print("You go together like coke and mentos.")
if compactibility > 40 and compactibility < 50:
	print("You are alright together.")
