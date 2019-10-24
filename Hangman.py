print("Welcome to Hangman!")

mystery = list("pineapple")
guessList = list("_________")

guess = input("Guess a letter: ")
if guess in mystery:
	print("Letter is in the word")
	for letter in mystery:
if letter == guess:
		guessList[index] = guess
	index += 1
print(guessList)
else:
	print("Letter is not in the word")
index = 0 

