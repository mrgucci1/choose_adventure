import random
import math

def path1(score):
	print("You Choose path 1! You begin walking up a stairway...")
	print("At the top of the stairway is a hallway leading right and one leading left")
	choice = int(input("enter 1 to go left and 2 to go right"))
	number = [1,1,1,1,1,1,1]
	if choice == 1:
		for x in number:
			print("================")
		print("you get submerged in cement and suffocate!")
		print("plus 3 points")
		score = score + 3
		print("Score: " ,score)	
	if choice == 2:
		print("you discover the something shiny and gold.......")
		print("its an enchated golden apple!")
		choice = int(input("consume? enter 1 for yes and 2 for no"))
		if choice == 1:
			print("you become a KING with superpowers")
			score = score + 14000
			print("Score: " ,score)
		if choice == 2:
			print("you sell the apple for a MILLIONS!!!!!!!")
			print("plus 16.7k points")
			score = score + 16700
			print("Score: " ,score)	
		
		
def path2(score):
	print("You Choose path 2! You begin walking throw a meadow...")
	print("you see something in the grass....investigate?")
	choice = int(input("Enter 1 to investigate or Enter 2 to run away"))
	#use of random libary
	number = random.randint(0,100)
	if choice == 1:
		print("you encounter a wild beast with ", number," health!")
		#nested if statement
		if number > 60: 
			print("the beast's health was to much for you to handle! you dided")
			print("your final score was ", score)
		else:
			print("you killed the beast and gained 100 points!")
			score = score + 100
			print("Score: " ,score)		
	elif choice == 2:
		print("you run past the beast and see it attaking another person!")
		print("you sneak up behind the beast")
		count = 0;
		arr = [1,3,6,8,9]
		#use of math libary
		num1 = sum(arr,choice)
		print(num1)
		num1 = str(num1)
		number = str(number)
		choice = str(choice)
		#condition controlled loop
		while count < 3:
			if count == 0:
				in1 = str(input("Enter "+num1+" to attack!"))
				if in1 != num1:
					in1 = int(input("Enter "+num1+" to attack!"))
				count = count + 1;
			elif count == 1:
				in1 = str(input("Enter "+number+" to attack!"))
				if in1 != number:
					in1 = int(input("Enter "+number+" to attack!"))
				count = count + 1;
			elif count == 2:
				in1 = str(input("Enter "+choice+" to attack!"))
				if in1 != choice:
					in1 = int(input("Enter "+choice+" to "))
				count = count + 1;
		print("you killed the beast and saved a life!")
		print("plus 1000 points!")
		score = score + 1000
		print("Score: " ,score)		
				
				
		
			
		
#path 3 is loss right away
def path3(score):
	print("You Choose path 3! You disapear!")
	print("your final score was: ",score)
	
def main():
	print "Welcome to Choose your own Adventure!"
	print("Your are in front of 3 doors")
	score = 0
	print("Score: " ,score)
	choice = int(input("Enter 1, 2, or 3 to choose one "))
	#condition controlled while loop
	while True:
		if choice == 1:
			path1(score)
			break;
		elif choice == 2:
			path2(score)
			break;
		elif choice == 3:
			path3(score)
			break;
		else:
			choice = int(input("Enter 1, 2, or 3 to choose one "))
	print("Game Over")
		
	
main()