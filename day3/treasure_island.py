#!/usr/bin/python
print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to the Treasure Island.\nYour mission is to find the treasure")

step1 = input("Do you choose to go left of right? \n").lower()


if step1 == "left":
	step2 = input("You have a choice to swim or wait, which do you choose? \n").lower()
	if step2 == "wait":
		print("Good job? I don't know. Well,one step a time.")
		step3 = input("There are three doors: Red, Blue, and Yellow. Choose the door to the treasure. Choose wisely!\n").lower()
		if step3 == "yellow":
			print("You have good luck. That's if you tried it once.\nElse you built resilence, blah blah blah.")
		elif step3 == "red":
			print("You just got lost in the abyss.")
		elif step3 == "blue":
			print("What else do you expect? YOu just drowned.")
		else:
			print("If not that the bible said no cussing, I would have called you a fool for exploring beyond the scope. But good job. You got eaten by a liger")
	else:
		print("Didn't your mom warn you that speed kills. Patience my friend, patience!")
else:
	print("Looser from the start. GameOver!\nYou can start again though.")
