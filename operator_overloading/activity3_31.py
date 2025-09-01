import random
class FruitQuiz:
    def __init__(self):
        self.fruits= {'apple' : 'red' , 'banana' : 'yellow' , 'orange' : 'orange'}
    def quiz(self):
        while True:
            fruit, color= random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            ans= input()
            if (ans.lower()==color):
                print("CORRRRECTTT!!!!!")
            else:
                print("wrong.")
            
            option= int(input("Enter 0 if you want to play again, else enter 1"))
            if (option):
                break

print("Welcome to the fruit quiz!")
fq= FruitQuiz()
fq.quiz()