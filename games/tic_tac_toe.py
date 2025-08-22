theboard= {'1' : ' ' , '2' : ' ' , '3' : ' ',
           '4' : ' ' , '5' : ' ' , '6' : ' ',
           '7' : ' ' , '8' : ' ' , '9' : ' '}
board_keys= []
for key in theboard:
    board_keys.append(key)

def printboard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game():

    turn= 'X'
    count= 0
    
    for i in range(10):
        printboard(theboard)
        print("It's your turn!" + turn + "move to which place?")
        move= input()
        if theboard[move]== ' ':
            theboard[move]==turn
            count= count + 1
        else:
            print("The place is already filled.")
            print("Move to which place?")
            continue

        if count >= 5:
            if theboard['7']==theboard['8']==theboard['9']!= ' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print("****" + turn + "Won!!! :)" + "****")
                break
            elif theboard['6']==theboard['5']==theboard['4']!= ' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print("****" + turn + "Won!!! :)" + "****")
                break
            elif theboard['3']==theboard['2']==theboard['1']!= ' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print("****" + turn + "Won!!! :)" + "****")
                break
            elif theboard['1']==theboard['4']==theboard['7']!= ' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print("****" + turn + "Won!!! :)" + "****")
                break
            elif theboard['2']==theboard['5']==theboard['8']!= ' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print("****" + turn + "Won!!! :)" + "****")
                break
            elif theboard['3']==theboard['6']==theboard['9']!= ' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print("****" + turn + "Won!!! :)" + "****")
                break
            elif theboard['7']==theboard['5']==theboard['3']!= ' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print("****" + turn + "Won!!! :)" + "****")
                break
            elif theboard['1']==theboard['5']==theboard['9']!= ' ':
                printboard(theboard)
                print("\nGame Over.\n")
                print("****" + turn + "Won!!! :)" + "****")
                break
        if count==9:
            print("\nGame Over\n")
            print("\nIt's a tie\n")
        if turn=='X':
            turn= 'O'
        else:
            turn= 'X'
    restart= input("DO you want to play again? (y/n):  ")
    if restart=='y' or restart=='Y':
        for key in board_keys:
            theboard[key]= ' '
        game()
if __name__ == "__main__":
    game()