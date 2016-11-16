import tictactoe as game
import AI

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
        while(gameComplete == 0):
            gameComplete = newgame.move(makeMove(move[0], newgame))
        move = switchTurn(move, p1, p2)

#playGame helper functions 

#returns the position of the desired move, calling the
#appropriate function given the player type. (Human asks
#for stdin, AI calls the AI, etc.)
def makeMove(ptype, board):
    if(ptype == 'h'):
        board.show()
        return int(raw_input("Move: "))
    elif(ptype == 'a'):
        return AI.returnRandom(board)
    return 0

#given the current turn, swaps to the next turn
def switchTurn(move, p1, p2):
    if(move[1] == "p1"):
        return [p2, "p2"]
    else:
        return [p1, "p1"]



if __name__ == "__main__":
    #Step 1: capture board as features
    #Step 2: maximize reward from moves
    #Step 3: add complexity

    playGame('a', 'h')

    while(raw_input("Continue? ") != "n"):
        playGame('a', 'a')

    hinput = ""
    numarr = []
    for i in range (0, 9):
        numarr.append(i)
    while(hinput != "n"):
        print "\nNew Test:"
        tester = game.Grid()
        ret = 1
        random.shuffle(numarr)
        for j in numarr:
            if (ret == 1):
                ret = tester.move(j)
        hinput = raw_input("continue? ")
