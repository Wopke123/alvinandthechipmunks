import tictactoe as game
import AI
import sys

import random

########################################################
#
#playGame is the function that builds the game board and
#is responsible for swapping turns and positioning 
#each players moves
#
########################################################

def playGame(p1, p2, p1AImodel, p2AImodel):
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
        if p1[1] == 'a':
            p1[0].train(p1moves, 'p1', True)
        if p2[1] == 'a':
            p2[0].train(p2moves, 'p2', False)
        if (p1[1] == 'h' or p2[1] == 'h'):
            if(p1[1] == 'h'):
                p1AImodel.train(p1moves, 'p1', True)
            if(p2[1] == 'h'):
                p2AImodel.train(p2moves, 'p2', False)
            newgame.show()
            print "X Wins!"
        return "X"
    elif gameComplete == "O":
        if p1[1] == 'a':
            p1[0].train(p1moves, 'p1', False)
        if p2[1] == 'a':
            p2[0].train(p2moves, 'p2', True)
        if (p1[1] == 'h' or p2[1] == 'h'):
            if(p1[1] == 'h'):
                p1AImodel.train(p1moves, 'p1', False)
            if(p2[1] == 'h'):
                p2AImodel.train(p2moves, 'p2', True)
            newgame.show()
            print "O Wins!"
        return "O"
    else:
        if p1[1] == 'a':
            p1[0].train(p1moves, 'p1', True)
        if p2[1] == 'a':
            p2[0].train(p2moves, 'p2', True)
        if (p1[1] == 'h' or p2[1] == 'h'):
            if(p1[1] == 'h'):
                p1AImodel.train(p1moves, 'p1', True)
            if(p2[1] == 'h'):
                p2AImodel.train(p2moves, 'p2', True)
            newgame.show()
            print "Draw"
        return "D"


#playGame helper functions 

#returns the position of the desired move, calling the
#appropriate function given the player type. (Human asks
#for stdin, AI calls the AI, etc.)
def makeMove(ptype, board):
    if(ptype[0][1] == 'h'):
        board.show()
        humove = -1
        while(humove < 0 or humove > 8):
            humove = raw_input("Move: ")
            try:
                humove = int(humove)
                break
            except ValueError:
                humove = -1
                print "Must be a number between 0 and 8"
        return humove
    elif(ptype[0][1] == 'a'):
        return ptype[0][0].chooseMove(board, ptype[1])
    elif(ptype[0][1] == 'r'):
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

    #Args = Numruns, p1 save file, p2 save file, human testing? (bool)
    if(len(sys.argv) == 5):
        try:
            numruns = int(sys.argv[1])
        except ValueError:
            "Number of runs must be a number"
        p1save = sys.argv[2]
        p2save = sys.argv[3]
        humantest = bool(int(sys.argv[4]))

        p1model = AI.ai()
        p2model = AI.ai()
        p1model.loadSave(p1save)
        p2model.loadSave(p2save)
        results = [0, 0, 0, 0] #X wins, O wins, Draws, num games

        if(humantest):
            while(raw_input("Continue? ") != "n"):
                playGame([p1model, 'a'], ['null', 'h'], p1model, p2model)
                raw_input("Press enter to continue...")
                playGame(['null', 'h'], [p2model, 'a'], p1model, p2model)

        for i in range (0, numruns):
            playGame([p1model, 'a'], ['null', 'r'], p1model, p2model)
            playGame(['null', 'r'], [p2model, 'a'], p1model, p2model)
            playGame(['null', 'r'], ['null', 'r'], p1model, p2model)
            results[3] += 1
            res = playGame([p1model, 'a'], [p2model, 'a'], p1model, p2model)
            if res == "X": 
                results[0] += 1
            elif res == "O":
                results[1] += 1
            else:
                results[2] += 1
            if(numruns >= 100 and i % (numruns/100) == 0):
                print i * 100 / numruns, "% "

        print "X:", float(results[0]) / results[3], "\tO:", float(results[1]) / results[3], "\tD:", float(results[2]) / results[3]

        if(humantest):
            while(raw_input("Continue (p2)? ") != "n"):
                playGame([model, 'a'], ['null', 'h'], model)

            while(raw_input("Continue (p1)? ") != "n"):
                playGame(['null', 'h'], [model, 'a'], model)

        p1model.saveSelf(p1save)
        p2model.saveSelf(p2save)
    else:
        print "Bad Arguments"
