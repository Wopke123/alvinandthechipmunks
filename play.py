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
        if p1[1] == 'a':
            p1[0].train(p1moves, True)
        if p2[1] == 'a':
            p2[0].train(p2moves, False)
        if (p1[1] == 'h' or p2[1] == 'h'):
            newgame.show()
            print "X Wins!"
        return "X"
    elif gameComplete == "O":
        if p1[1] == 'a':
            p1[0].train(p1moves, False)
        if p2[1] == 'a':
            p2[0].train(p2moves, True)
        if (p1[1] == 'h' or p2[1] == 'h'):
            newgame.show()
            print "O Wins!"
        return "O"
    else:
#        if p1[1] == 'a':
#            p1[0].train(p1moves, True)
#        if p2[1] == 'a':
#            p2[0].train(p2moves, True)
        if (p1[1] == 'h' or p2[1] == 'h'):
            newgame.show()
            print "Draw"
        return "D"

#    print p1[0].moves
#    print p2[0].moves

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

    player1 = AI.ai()
    player2 = AI.ai()
    results = [0, 0, 0, 0] #X wins, O wins, Draws, num games

    numruns = int(raw_input("Runs: "))
 #   while(raw_input("Continue? ") != "n"):
    for i in range (0, numruns):
        res = playGame([player1, 'a'], [player2, 'a'])
        playGame([player1, 'a'], ['null', 'r'])
        playGame(['null', 'r'], [player2, 'a'])
        results[3] += 1
        if res == "X": 
            results[0] += 1
        elif res == "O":
            results[1] += 1
        else:
            results[2] += 1
        if(numruns >= 100 and i % (numruns/20) == 0):
            print i * 100 / numruns, "%"

    p1rand = []
    p2rand = []
    for i in range(0, 10):
        p1rand.append(random.choice(player1.moves))
        p2rand.append(random.choice(player2.moves))
    for i in p1rand:
        print i
    for i in p2rand:
        print i

    print "X:", float(results[0]) / results[3], "\tO:", float(results[1]) / results[3], "\tD:", float(results[2]) / results[3]

    while(raw_input("Continue (p2)? ") != "n"):
        playGame([player1, 'a'], ['null', 'h'])

    while(raw_input("Continue (p1)? ") != "n"):
        playGame(['null', 'h'], [player2, 'a'])
