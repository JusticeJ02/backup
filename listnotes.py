print("Welcome to the To Do List")
todoList = []
while True: 
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")

	choice = input(" Make your choice: ")
	if choice == "q":
		break
	elif choice == "a":
		a = input(" What would you like to add?")
		todoList.append(a) 
	elif choice == "r":
		r = input(" What would you like to remove?")
		todoList.remove(r) 
	elif choice == "p":
		p = print("Tasks:" + str(todoList))
	else:
		print("That is not a choice")

