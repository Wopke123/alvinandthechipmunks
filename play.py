import tictactoe as game

import random

def playGame(p1, p2):
    newgame = game.Grid()
    move = "player1"
    gameComplete = 1
    while(gameComplete == 1):
        newgame.show()
        if (move == "player1"):
            while(gameComplete != 0):
                gameComplete = newgame.move(int(raw_input("Move: ")))
            move = "player2"
        else:
            while(gameComplete != 0):
                gameComplete = newgame.move(random.randrange(0, 8))
            move = "player1"


if __name__ == "__main__":
    #Step 1: capture board as features
    #Step 2: maximize reward from moves
    #Step 3: add complexity

    playGame('h', 'a')


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
        print tester.grid
        hinput = raw_input("continue? ")
