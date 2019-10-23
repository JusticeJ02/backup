# Jarell Justice
# Period 4
# October 2, 2019
# Rolling Dice Simulator

import random

print("Welcome to dice rolling simulator")
Num1= 0
Num2= 0
Num3= 0
Num4= 0
Num5= 0
Num6= 0
Rolls = int(input("How many rolls would you like? ")) 
x = 1
while x < Rolls:
	randomNum = random.randint(1, 6)
	x += 1 
	if randomNum == 1:
		Num1+= 1
	if randomNum == 2:
		Num2+= 1
	if randomNum == 3:
		Num3+= 1
	if randomNum == 4:
		Num4+= 1
	if randomNum == 5:
		Num5+= 1
	if randomNum == 6:
		Num6+= 1
	
	print("Roll " + str(x) +)
		




