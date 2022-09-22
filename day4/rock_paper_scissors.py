#!/usr/bin/python
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player_choice = input("Play the game of ROCK, PAPER, SCISSORS with computer\nChoose 1 for ROCK, 2 for PAPER and 3 for SCISSORS\n")
play =  int(player_choice) -1
game = [rock, paper, scissors]
computer_choice = random.randint(0,2)
game1 = ["rock", "paper", "scissors"]

print(f"You played {game1[play]}")
print(game[play])
print(f"Computer played {game1[computer_choice]}")
print(game[computer_choice])

if play == computer_choice:
	print("Draw!! Play again")
elif play > computer_choice:
	if play - computer_choice == 1:
		print("You won against computer")
else:
	if computer_choice - play == 2:
		print("You won.Rejoice")
	else:
		print("You lost, bro. Try again")












