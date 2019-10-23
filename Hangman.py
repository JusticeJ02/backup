print("Welcome to Hangman!")

myString = "_ _ _ _ _ _ _ _ _"
myList = list(myString)
print(myList)

myWord= "Pineapple"
letter = input(" Guess a letter ")
if letter in myWord:
	print("Letter is in the word")
else:
	print("Letter is not in the word")

count = 0
for l in myWord:
	if l == letter:
		print(count)
	count += 1

misses = 0
while misses < 10:
	guess = input("Guess a letter:")
	if guess in myWord:
		print("letter is in the word")
	else:
		misses += 1
		print(hangmanList[misses])

		
print(" GAME OVER, TRY AGAIN ")