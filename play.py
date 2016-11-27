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
    p1moves = []
    p2moves = []
    move = [p1, "p1"]
    gameComplete = 1
    while(gameComplete == 1):
        moveMade = 0
        gameComplete = 0

        temp = (AI.getFeat(newgame, move[1]))

        while(gameComplete == 0):
            moveMade = makeMove(move, newgame)
            gameComplete = newgame.move(moveMade)
        
        if move[1] == "p1":
            p1moves.append([temp, moveMade])
        elif move[1] == "p2":
            p2moves.append([temp, moveMade])

        move = switchTurn(move, p1, p2)
    if gameComplete == "X":
        p1[0].train(p1moves, True)
        p2[0].train(p2moves, False)
    elif gameComplete == "O":
        p1[0].train(p1moves, False)
        p2[0].train(p2moves, True)
    else:
        p1[0].train(p1moves, True)
        p2[0].train(p2moves, True)

    print p1[0].moves
    print p2[0].moves

#playGame helper functions 

#returns the position of the desired move, calling the
#appropriate function given the player type. (Human asks
#for stdin, AI calls the AI, etc.)
def makeMove(ptype, board):
    if(ptype[0][1] == 'h'):
        board.show()
        return int(raw_input("Move: "))
    elif(ptype[0][1] == 'a'):
        return ptype[0][0].chooseMove(board, ptype[1])
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

    player1 = AI.ai()
    player2 = AI.ai()

    while(raw_input("Continue? ") != "n"):
        playGame([player1, 'a'], [player2, 'a'])

    #hinput = ""
    #numarr = []
    #for i in range (0, 9):
    #    numarr.append(i)
    #while(hinput != "n"):
    #    print "\nNew Test:"
    #    tester = game.Grid()
    #    ret = 1
    #    random.shuffle(numarr)
    #    for j in numarr:
    #        if (ret == 1):
    #            ret = tester.move(j)
    #    hinput = raw_input("continue? ")
