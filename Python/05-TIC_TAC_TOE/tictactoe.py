# Modules importation
import numpy as np
# Function to show the table in the terminal
def showboard(table):
    print("    a   b   c")
    print("  -------------")
    print(f"1 | {convertValue(table[0,0])} | {convertValue(table[0,1])} | {convertValue(table[0,2])} |")
    print("  -------------")
    print(f"2 | {convertValue(table[1,0])} | {convertValue(table[1,1])} | {convertValue(table[1,2])} |")
    print("  -------------")
    print(f"3 | {convertValue(table[2,0])} | {convertValue(table[2,1])} | {convertValue(table[2,2])} |") 
    print("  -------------")
# Function to convert numerical values (1,2,n) to mark (O,X,-) on the board
def convertValue(txt):
    if(txt==1):
        return "X"
    elif(txt==2):
        return "O"
    else:
        return " "    
# Function to validate the input value from the player
def inputValidation(player, tabl):
    rep=False
    while(rep==False):
        buffer=str(input(f"\nEnter move player 0{player}: "))
        for i in range(len(authorizedListe)):
            if(buffer==authorizedListe[i]): # compare with the authorizedListe of input move
                rep=True    
        if rep==True:
            for i in range(len(history)): # compare with the previous inputs move
                if(buffer==history[i]):
                    rep=False
        if rep==False:
            print(chr(27) + "[2J")  # Clear the terminal with escape sequences
            print(f"Bad input player 0{player} --- Please re-enter (ex: a1, b2,...)\n")
            showboard(tabl) # Show the board(table)
    history.append(buffer)
    return buffer
# Function to apply the move (m) of a player in the table
def sendMove(tabl, m, player):
    match m :
        case 'a1':
            tabl[0,0]=player
        case 'a2':
            tabl[1,0]=player
        case 'a3':
            tabl[2,0]=player
        case 'b1':
            tabl[0,1]=player
        case 'b2':
            tabl[1,1]=player
        case 'b3':
            tabl[2,1]=player
        case 'c1':
            tabl[0,2]=player
        case 'c2':
            tabl[1,2]=player           
        case 'c3':
            tabl[2,2]=player
# Function to verify if is there a winner or not
def isThereWinner(tabl):
    if (tabl[0,0]+tabl[1,1]+tabl[2,2]==3 or tabl[0,2]+tabl[1,1]+tabl[2,0]==3 or
        tabl[0,0]+tabl[0,1]+tabl[0,2]==3 or tabl[1,0]+tabl[1,1]+tabl[1,2]==3 or tabl[2,0]+tabl[2,1]+tabl[2,2]==3 or
        tabl[0,0]+tabl[1,0]+tabl[2,0]==3 or tabl[0,1]+tabl[1,1]+tabl[2,1]==3 or tabl[0,2]+tabl[1,2]+tabl[2,2]==3):
        print("\nPlayer 01 Wins!!!\n")
        return True
    elif (tabl[0,0]+tabl[1,1]+tabl[2,2]==6 or tabl[0,2]+tabl[1,1]+tabl[2,0]==6 or
        tabl[0,0]+tabl[0,1]+tabl[0,2]==6 or tabl[1,0]+tabl[1,1]+tabl[1,2]==6 or tabl[2,0]+tabl[2,1]+tabl[2,2]==6 or
        tabl[0,0]+tabl[1,0]+tabl[2,0]==6 or tabl[0,1]+tabl[1,1]+tabl[2,1]==6 or tabl[0,2]+tabl[1,2]+tabl[2,2]==6):
        print("\nPlayer 02 Wins!!!\n")
        return True
    else:
        return False  
# Set initial variables : table, history, authorizedListe, rnd
table=np.array(([8,8,8],[8,8,8],[8,8,8]))
history=[]
authorizedListe=['a1','a2','a3','b1','b2','b3','c1','c2','c3']
rnd=1
# The main loop
while(True):
    print(chr(27) + "[2J")  # Clear the terminal with escape sequences
    showboard(table) # Show the board(table)
    if len(history)>=9 : # Verify if players played all possible cases on the board
        print("\nDraw game\n")
        exit()
    #print(history) # To show move history
    if(isThereWinner(table)): # Verify Winner
        exit()
    play=inputValidation(rnd, table) # Ask player to play
    sendMove(table, play, rnd) # Send move to the board(table)
    rnd=(1^(rnd-1))+1 # passer de joueur 1 à 2, puis de joueur 2 à 1 la boucle suivante, et ainsi de suite...
