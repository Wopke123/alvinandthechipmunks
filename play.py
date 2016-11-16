import tictactoe as game
import subprocess as sp

import random

########################################################
#
#playGame is the function that builds the game board and
#is responsible for swapping turns and positioning 
#each players moves
#
########################################################

def playGame(p1, p2):
    newgame = game.Grid()
    move = [p1, "p1"]
    gameComplete = 1
    while(gameComplete == 1):
        gameComplete = 0
        tmp = sp.call('clear',shell=True)
        newgame.show()
        while(gameComplete == 0):
            gameComplete = newgame.move(makeMove(move[0]))
        move = switchTurn(move, p1, p2)

#playGame helper functions 

def makeMove(ptype):
    if(ptype == 'h'):
        return int(raw_input("Move: "))
    elif(ptype == 'a'):
        return random.randrange(0, 8)   #this is where the AI should move
    return 0

def switchTurn(move, p1, p2):
    if(move[1] == "p1"):
        return [p2, "p2"]
    else:
        return [p1, "p1"]



if __name__ == "__main__":
    #Step 1: capture board as features
    #Step 2: maximize reward from moves
    #Step 3: add complexity

    playGame('h', 'h')


    numarr = []
    for i in range (0, 9):
        numarr.append(i)
    hinput = ""
    while(hinput != "n"):
        print "\nNew Test:"
        tester = game.Grid()
        ret = 1
        random.shuffle(numarr)
        for j in numarr:
            if (ret == 1):
                ret = tester.move(j)
        hinput = raw_input("continue? ")
