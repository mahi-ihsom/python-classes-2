#Write a program to generante a nadom integer and match it with the input given by the user
import random
play= True
num= str(random.randint(10,20))
#random inbuilt function
print("I will generate a random number from 0-9, and you have to guess the number one diguit at a time.")
print("The game ends when you get 1 hero.")
#iterate loop til the condition is true
while play:
    guess= input("give me your best guess!!!   ")
    if num==guess:
        print("You win the game!")
        print("The number was", num)
        break
    else:
        print("Your guess is not quite right! Try again later.")