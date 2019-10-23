# Jarell Justice
# Rock Paper Scissors
# added a comment
# Variables
import random

pScore = 0
cScore = 0
ties = 0
computerChoices = ["r", "p", "s"]

# Period 4
# Welcome Message
# Print the message
print("Welcome to Rock Paper Scissors")
# prompt for player name
pName = input("What is your name?")
# Game Loop

# Final Score
def printScore():
 	# Write message
 	print("The score is")
# Write player score
print(pName + ":" + str(pScore))
# Write computer score
print("Computer: " + str(cScore))
# write how many ties
print("Ties :" + str(ties))
# game loop
# make a forever loop
while True:
# Print current score
	printScore()
	# prompt for a choice (r(rock), p (paper), s(scissors), q(quit))
	pChoice = input ("Enter r (rock), p (paper), s(scissors), or q (to quit): ")
# deal with player entering q
	if pChoice == "q":
		break

# get computer choice (random)
Choice = random.choice(computerChoices)
# compare for player entering r
if pChoice == "r":
	print ("Computer picked Rock")
	print("This is a tie")
	ties = ties + 1
	#if computer is r
	if cChoice == "r":
		print("Computer picked Rock")
		print("This is a tie")
		ties = ties + 1
	# if computer is p
	elif cChoice == "p":
 		print("Computer picked Paper")
 		print("Paper covers Rock")
 		cScore = cScore + 1

	# if computer is s
	else:
		print("Computer picked scissors")
		print("Rock breaks scissors")
		pScore = pScore + 1


# compare for player entering p
elif pChoice == "p":
	pass
# compare for player entering s
elif pChoice == "s":
	pass

# deal with play entering anything else