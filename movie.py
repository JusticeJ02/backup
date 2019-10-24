import time
import os

frameList = [
''' 
    +---+
    O   |
   /|\  |
   / \  |
   	   === ''', '''
   	+---+
   \O/  |
    |   |
    \\\\  |
        === '''
]


while True:
	for frame in frameList:
		os.system("cls")
		print(frame)
		time.sleep(3)


           




print(frameList[0])



print("Welcome to Hangman!")

mystery = list("pineapple")
guessList = list("_________")

guess = input("Guess a letter: ")
if letter in mystery:
	print("Letter is in the word")
else:
	print("Letter is not in the word")
index = 0 

for letter in mystery:
	if letter == guess:
		guesslist[index] = guess
	index += 1
print(guesslist)

count = 0
for l in myWord:
	if l == letter:
		print(count)
	count += 1


		
print(" GAME OVER, TRY AGAIN ")