myWord = "Hello"

choice = input("Type a word: ")

if choice == myWord:
	print("It's a match")
else:
	print("Not a match")

# how to check if a letter is in a word
letter = input("Type a letter")
if letter in myWord:
	print("Letter is in the word")
else:
	print("Letter is not in the word")

count = 0
for l in myWord:
	if l == letter:
		print(count)
	count += 1

#how to turn a string to a list
myString = "arizona"
myList = list(myString)
print(myList)

# how to create a list with _ there the letters go
guessList = []
for a in myList:
	guessList.append("_")

print(guessList)

# How to replace a specific item in a list
# So say the user types r for guess you would
guessList[1] = "r"
print(guessList)