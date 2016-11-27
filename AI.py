import tictactoe
import random

class ai:
	def __init__(self):	
		#this vector will contain the previously seen states, and the weight vector
		self.moves = []

	def chooseMove(self, board, player):
		features = getFeat(board, player)
		for i in range (0, len(self.moves)):
			if features == self.moves[i][0]:
				bestWeight = 0
				for j in range (0,9):
					if self.moves[i][0][j] > self.moves[i][0][bestWeight]:
						bestWeight = j
				return bestWeight
		return returnRandom(board)

	def train(self, hist, win):
		if win == True:
			for i in reversed(hist):
				found = False
				for j in range(0, len(self.moves)):
					if i[0] == self.moves[j][0]:
						self.moves[j][1][i[1]] += 1
						found = True
						break
				if found == False:
					tempWeight = []
					for h in range(0,9):
						if h == i[1]:
							tempWeight.append(1)
						else:
							tempWeight.append(0)
					self.moves.append([i[0], tempWeight])

		elif win == False:
			for i in hist:
				found = False
				for j in range(0, len(self.moves)):
					if i[0] == self.moves[j][0]:
						self.moves[j][1][i[1]] -= 1
						found = True
						break
				if found == False:
					tempWeight = []
					for h in range(0,9):
						if h == i[1]:
							tempWeight.append(-1)
						else:
							tempWeight.append(0)
					self.moves.append([i[0], tempWeight])




def returnRandom(board):
    options = []
    for i in range (0, 9):
        if board.grid[i][1] == False:
            options.append(i)
    return random.choice(options)

def getFeat(board, player):
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
	return markers

#def main():
#	board = [["X", True], [" ", False], ["O", True], [" ", False], ["X", True], ["O", True], [" ", False], [" ", False], [" ", False]]
#	p1 = "p1"
#	p2 = "p2"
#	p1m = getFeat(board, p1)
#	p2m = getFeat(board, p2)
#	print p1m
#	print p2m

#main()