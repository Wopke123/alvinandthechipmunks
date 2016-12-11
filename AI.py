import tictactoe
import random
import math
from os import remove

class ai:
    def __init__(self):    
        #this vector will contain the previously seen states, and the weight vector
        self.moves = {}

    def loadSave(self, savefile):
        try:
            f = open(savefile, 'r')
            for i in f:
                a, b = i.strip('\n').split('#')
                d = []
                d = b.split('|')
                for i in range(0, len(d)):
                    d[i] = float(d[i])
                self.moves[a] = d
        except:
            print "Load Error"
            return

    def saveSelf(self, savefile):
        f = open(savefile, 'w+')
        f.truncate()
        print len(self.moves)
        for i in self.moves:
            tempstr = i + '#'
            tempWeight = self.moves[i]
            for j in range(0, len(tempWeight) - 1):
                tempstr += str(tempWeight[j]) + '|'
            tempstr += str(tempWeight[len(tempWeight) - 1]) + '\n'
            f.write(tempstr)

    def chooseMove(self, board, player):
        features = getFeat(board, player)
        found = self.moves.get(features)
        if(found != None):
            options = []
            for j in range (0, 9):
                if board.grid[j][1] == False:
                    options.append(j)
            bestWeight = random.choice(options)
            bestoptions = []
            for j in options:
                if found[j] > found[bestWeight]:
                    bestWeight = j
            for j in options:
                if found[j] > (found[bestWeight] - 0.05):
                    bestoptions.append(j)
            return random.choice(bestoptions)
        else:
            return returnRandom(board)

    def train(self, hist, player, win):
        if win == True:
            reversedhist = []
            for i in reversed(hist):
                reversedhist.append(i)
            for i in range (0, len(reversedhist)):
                tempstr = ''
                for j in range(0, len(reversedhist[i]) - 2):
                    tempstr += str(reversedhist[i][j]) + '|'
                tempstr += str(reversedhist[i][len(reversedhist[i]) - 2])
                move = int(reversedhist[i][len(reversedhist[i]) - 1])
                found = self.moves.get(tempstr)
                if(found == None):
                    tempWeight = []
                    for h in range(0,9):
                        if h == move:
                            tempWeight.append(0.6)
                        elif(reversedhist[i][0][h] == 0):
                            tempWeight.append(0.5)
                        else:
                            tempWeight.append(0.0)
                    self.moves[tempstr] = tempWeight
                else:
                    found[move] = sigmoid(found[move] + (reward(i / 10)))
                    self.moves[tempstr] = found

        elif win == False:
            for i in range(0, len(hist)):
                tempstr = ''
                for j in range(0, len(hist[i]) - 2):
                    tempstr += str(hist[i][j]) + '|'
                tempstr += str(hist[i][len(hist[i]) - 2])
                move = int(hist[i][len(hist[i]) - 1])
                found = self.moves.get(tempstr)
                if(found == None):
                    tempWeight = []
                    for h in range(0,9):
                        if h == move:
                            tempWeight.append(0.4)
                        elif(hist[i][0][h] == 0):
                            tempWeight.append(0.5)
                        else:
                            tempWeight.append(0.0)
                    self.moves[tempstr] = tempWeight
                else:
                    found[move] = sigmoid(found[move] - (reward(i) / 10))
                    self.moves[tempstr] = found


def reward(iter):
    return math.exp(-0.21*(iter+10))

def sigmoid(a):
#    return 1 / (1 + math.exp(-(a - 0.5) * 5))
    return 1 / (1 + math.exp(a))

def returnRandom(board):
    options = []
    for i in range (0, 9):
        if board.grid[i][1] == False:
            options.append(i)
    return random.choice(options)

def getFeat(board, player):
    tempstr = ''
    markers = []
    for i in range (0, 9):
        markers.append(board.grid[i][0])
    for i in range (0,len(markers)):
        if player == "p1":
            if markers[i] == "X":
                markers[i] = 1
            elif markers[i] == "O":
                markers[i] = -1
            else:
                markers[i] = 0
        elif player == "p2":
            if markers[i] == "X":
                markers[i] = -1
            elif markers[i] == "O":
                markers[i] = 1
            else:
                markers[i] = 0
    for j in range(0, len(markers) - 1):
        tempstr += str(markers[j]) + '|'
    tempstr += str(markers[len(markers) - 1])
    return tempstr
