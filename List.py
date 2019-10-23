# how to make a list
favMovies = ["The Equalizer", "Rambo", "John Wick"]
# print the whole list
print(favMovies)
# print individuals 
print(favMovies[0])
# to add you can use append or insert
# append adds to the end
favMovies.append("Kung fu Panda")
print(favMovies)
favMovies.insert(1, "White Chicks")
print(favMovies)
# how to remove items
# remove by name or by index
#remove by name use remove
favMovies.remove("Kung fu Panda")
print(favMovies)
# favMovies.remove("Endgame")
# pop will remove the last item
favMovies.pop()
print(favMovies)
favMovies.pop(1) # will remove whatever is in the index
print(favMovies)

# get the length of a list 
# this is a function
# the function name is len
print("My list has " + str(len(favMovies)) + " items")
favMovie = input("What is your favorite Movie ")
favMovies.append(favMovie)
print(favMovies)
print(favMovies[len(favMovies) - 1])

#loop through a list
count = 1

for movie in favMovies:
	print("My number" + str(count) + " movie is " + movie)
	count = count + 1

numList = [2, 4, 6, 8, 10, 12, 14, 16]
# challenge: Loop though the list  and add all the numbers together, then print the sum

total = 0

for number in numList:
	total = total + number

print("The sum is " + str(total))

if "White Chicks" in favMovies:
	favMovies.remove ("Star Wars")
	print("removed")
else:
	print("not in List")