#Rock, paper, scissors
import random
while True:
    ui= input("ENTER A CHOICE(rock, paper, scissors):  ")
    p_a= ["Rock", "Paper", "Scissors"]
    comp_act= random.choice(p_a)
    print(f"You chose {ui}, computer chose {comp_act}. \n")
    if ui==comp_act:
        print(f"Both players selected {ui}, it's a tie.")
    elif ui=="Rock":
        if comp_act=="Scissors":
            print("Rock smashes scissors")
            print("You win.")
        else:
            print("Paper covers Rock")
            print("You lose.")
    elif ui=="Paper":
        if comp_act=="Rock":
            print("Paper covers Rock")
            print("You win.")
        else:
            print("Scissors cut paper.")
            print("You lose.")
    elif ui=="Scissors":
        if comp_act=="Paper":
            print("Scissors cut paper.")
            print("You win.")
        else:
            print("Rock smashes scissor.")
            print("You lose.")
    play_again= input("Play again? (y/n)  ")
    if play_again!="y":
        break