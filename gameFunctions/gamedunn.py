from random import randint

player_lives = 1
computer_lives = 1
total_lives = 1

#choices is an array => an array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]
#choices go "0 1 2" not "1 2 3" ie. rock = 0 paper = 1 scissors = 2
#set the computer variable to one of these choices
computer = choices[randint(0,2)]

#set up game loop so that we don't have to restart al the time
player = False