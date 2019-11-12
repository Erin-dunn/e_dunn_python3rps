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

	### this is where you would call compare
	comparechoices():
		print(comparechoices)
	
	###end compare stuff

#handle all lives lost for player or AI 
	if gamedunn.player_lives is 0:
		winlose.winorlose("lost")
		print("Your ran out of lives you stupid bitch, play much? loser. play again fuckass?")
		choice = input ("Y/N")
		print(choice)

		if (choice is "N") or (choice is "n"):
			print("bye bye loser.")
			exit()

		elif (choice is "Y") or (choice is "y"):
			#reset the game so that we can start all over again 
			gamedunn.player_lives = 5 
			gamedunn.computer_lives = 5 
			gamedunn.player = False 
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