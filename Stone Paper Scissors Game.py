# Stone Paper Scissors Game
import random
print("Welcome to Game: \"Stone Paper Scissors\"")
while True:
    print("Press: \n\'S\' for Stone\n\'P\' for Paper\n\'X\' for Scissors")
    i = 1
    uscr = 0
    cscr = 0
    while i<=10:
        lst = ['S','P','X']
        cmp = random.choice(lst)
        var = input("Enter your choice: ")
        print("Bot\'s choice: ",cmp)
        if (cmp=='S' or cmp=='s') and (var=='P' or var=='p'):
            uscr = uscr+1
            print("You Win")
        elif (cmp=='P' or cmp=='p') and (var=='S' or var=='s'):
            cscr = cscr+1
            print("Bot Wins")
        elif (cmp=='S' or cmp=='s') and (var=='X' or var=='x'):
            cscr = cscr + 1
            print("Bot Wins")
        elif (cmp=='X' or cmp=='x') and (var=='S' or var=='s'):
            uscr = uscr + 1
            print("You Win")
        elif (cmp=='P' or cmp=='p') and (var=='X' or var=='x'):
            uscr = uscr + 1
            print("You Win")
        elif (cmp=='X' or cmp=='x') and (var=='P' or var=='p'):
            cscr = cscr + 1
            print("Bot Wins")
        elif (cmp=='S' or cmp=='s') and (var == 'S' or var=='s'):
            print("Tie")
        elif (cmp=='P' or cmp=='p') and (var == 'P' or var=='p'):
            print("Tie")
        elif (cmp=='X' or cmp=='x') and (var == 'X' or var=='x'):
            print("Tie")
        i = i + 1
        continue
    if cscr>uscr:
        print("Bot Wins the Game!")
        print("Bot Score: ",cscr)
        print("Your Score: ",uscr)
    elif uscr>cscr:
        print("Congrats! You Won!!!")
        print("Your Score: ", uscr)
        print("Bot Score: ",cscr)
    elif uscr==cscr:
        print("Game Tie!!")
        print("Your Score: ", uscr)
        print("Bot Score: ", cscr)
    code = input("\nQuit the Game(y/n): ")
    if code == 'y' or code=='Y':
        print("Thank you")
        exit()
    elif code == 'n' or code=='N':
        continue