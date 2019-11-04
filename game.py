#import the random package so that we can generate a random choice 
from random import randint
#changes
#set up some variables for player and AI lives
player_lives = 5
computer_lives = 5 

#choices is an array => an array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]
#choices go "0 1 2" not "1 2 3" ie. rock = 0 paper = 1 scissors = 2
#set the computer variable to one of these choices
computer = choices[randint(0,2)]

#set up game loop so that we don't have to restart al the time
player = False

while player is False: 
	#set player to true
	print("***********************************\n")
	print("Computer lives: ", computer_lives, "/5\n")
	print("Player lives: ", player_lives, "/5\n")
	print("Choose your weapon!\n")
	print("***********************************\n")

	player = input("choose rock, paper or scissors\n")
	player = player.lower()



	print("computer chose ", computer, "\n")
	print("player chose ", player, "\n")

	if player == "quit":
		exit()
	elif computer == player:
		print("tie! no one wins, play again")

	elif player.lower()=="rock":
		if computer == "paper":
			print("you lose :( ", computer, "covers", player, "\n")
			player_lives = player_lives - 1
		else:
			print("you win :) ", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() =="paper":
		if computer == "scissors":
			print("you lose :( ", computer, "cuts", player, "\n")
			player_lives = player_lives - 1
		else:
			print("you win :) ", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() =="scissors":
		if computer == "rock":
			print("you lose :( ", computer, "smashes", player, "\n")
			player_lives = player_lives - 1
		else:
			print("you win :) ", player, "cuts", computer, "\n")
			computer_lives = computer_lives - 1

	else:
		print("That's not a valid option, try again")

#handle all lives lost for player or AI 
	if player_lives is 0:
		print("Your ran out of lives you stupid bitch, play much? loser. play again fuckass?")
		choice = input ("Y/N")
		print(choice)

		if (choice is "N") or (choice is "n"):
			print("bye bye loser.")
			exit()

		elif (choice is "Y") or (choice is "y"):
			#reset the game so that we can start all over again 
			player_lives = 5 
			computer_lives = 5 
			player = False 
			computer = choices[randint(0,2)]

	elif computer_lives is 0:
		print("Congrats you won fuckass. Play again?")
		choice = input ("Y/N")
		print(choice)

		if (choice is "N") or (choice is "n"):
			print("bye bye loser.")
			exit()

		elif (choice is "Y") or (choice is "y"):
			#reset the game so that we can start all over again 
			player_lives = 5 
			computer_lives = 5 
			player = False 
			computer = choices[randint(0,2)]
	else: 
		#need to check all of our conditions after checking for a tie
		player = False
		computer = choices[randint(0,2)]