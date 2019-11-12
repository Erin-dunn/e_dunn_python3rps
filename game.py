#import the random package so that we can generate a random choice 
from random import randint
from gameFunctions import winlose, gamedunn
#changes
#set up some variables for player and AI lives


while gamedunn.player is False: 
	#set player to true
	print("***********************************\n")
	print("Computer lives: ", gamedunn.computer_lives, "/", gamedunn.total_lives,"\n")
	print("Player lives: ", gamedunn.player_lives, "/\n")
	print("==================================\n")
	print("Welcome to Rock, Paper, Scissors...\n")
	print("The rules are very simple; paper covers rock, rock smahes scissors and scissors cuts paper\n")
	print("Ready to play?\n")
	print("==================================\n")
	print("Choose your weapon!\n")
	print("***********************************\n")

	player = input("choose rock, paper or scissors\n")
	player = player.lower()



	print("computer chose ", gamedunn.computer, "\n")
	print("player chose ", player, "\n")

	if player == "quit":
		exit()
	elif gamedunn.computer == player:
		print("tie! no one wins, play again")

	elif player.lower()=="rock":
		if gamedunn.computer == "paper":
			print("you lose :( ", gamedunn.computer, "covers", player, "\n")
			player_lives = player_lives - 1
		else:
			print("you win :) ", player, "smashes", gamedunn.computer, "\n")
			gamedunn.computer_lives = gamedunn._lives - 1

	elif player.lower() =="paper":
		if gamedunn.computer == "scissors":
			print("you lose :( ", gamedunn.computer, "cuts", player, "\n")
			player_lives = player_lives - 1
		else:
			print("you win :) ", player, "smashes", gamedunn.computer, "\n")
			gamedunn.computer_lives = gamedunn.computer_lives - 1

	elif player.lower() =="scissors":
		if gamedunn.computer == "rock":
			print("you lose :( ", gamedunn.computer, "smashes", player, "\n")
			player_lives = player_lives - 1
		else:
			print("you win :) ", player, "cuts", gamedunn.computer, "\n")
			gamedunn.computer_lives = gamedunn.computer_lives - 1

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
			gamedunn.computer_lives = 5 
			player = False 
			gamedunn.computer = choices[randint(0,2)]

	elif gamedunn.computer_lives is 0:
		print("Congrats you won fuckass. Play again?")
		choice = input ("Y/N")
		print(choice)

		if (choice is "N") or (choice is "n"):
			print("bye bye loser.")
			exit()

		elif (choice is "Y") or (choice is "y"):
			#reset the game so that we can start all over again 
			player_lives = 5 
			gamedunn.computer_lives = 5 
			player = False 
			gamedunn.computer = choices[randint(0,2)]
	else: 
		#need to check all of our conditions after checking for a tie
		player = False
		gamedunn.computer_lives = choices[randint(0,2)]