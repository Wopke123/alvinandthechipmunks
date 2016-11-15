import tictactoe
import random

def getFeat(board):
	markers = []
	taken = []
	for i in range (0, 9):
		markers.append(board.grid[i][0])
		taken.append(board.grid[i][1])
	return markers, taken
	
def main():
	test = tictactoe.Grid()
	a = []
	for i in range (0, 9):
		a.append(i)
	print "Test"
	tester = tictactoe.Grid()
	ret = 1
	random.shuffle(a)
	for j in a:
		if (ret == 1):
			ret = tester.move(j)
			markers, taken = getFeat(tester)
			print markers
			print taken
	#print ret

main()