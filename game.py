import random
import math

def path1(score):
	print("You Choose path 1! You begin walking up a stairway...")
	choice = int(input("At the top of the stairway is a hallway leading right and one leading left"))
		
	
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