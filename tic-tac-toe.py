import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.player = 0
        self.play()

    def play(self):
        playing = false
        while(playing):
            if(player == 0):
                player1()
                self.player = 1
            elif (player == 1):
                player2()
                self.player = 0

    def player1(self):
        self.grid

class Grid:
    def __init__(self):
        self.grid = []
        self.player = 0

        for i in range (0, 9):
            self.grid.append([" ", False])  #[move, taken]

    def show(self):
        print " " + self.grid[0][0] + " | " + self.grid[1][0] + " | " + self.grid[2][0] 
        print "-----------"
        print " " + self.grid[3][0] + " | " + self.grid[4][0] + " | " + self.grid[5][0]
        print "-----------"
        print " " + self.grid[6][0] + " | " + self.grid[7][0] + " | " + self.grid[8][0]

    def move(self, pos):        #Returns 0 for invalid move, 1 for continue playing, 2 for a game draw, or the player's piece for a win
        if self.player:
            if not(self.grid[pos][1]):
                self.grid[pos][0] = "O"
                self.grid[pos][1] = True
                self.player += 1
                return self.checkgrid()
            else:
                return 0
        else:
            if not(self.grid[pos][1]):
                self.grid[pos][0] = "X"
                self.grid[pos][1] = True
                self.player -= 1
                return self.checkgrid()
            else:
                return 0

    def checkgrid(self):
        for i in range (0, 3):  #check vertical
            if (self.grid[i][1] and self.grid[i][0] == self.grid[i+3][0] and self.grid[i+3][0] == self.grid[i+6][0]):
                print "Winner! Down"
                self.show()
                return self.grid[i][0]
        for i in (0, 3, 6):     #check horizontal
            if (self.grid[i][1] and self.grid[i][0] == self.grid[i+1][0] and self.grid[i+1][0] == self.grid[i+2][0]):
                print "Winner! Across"
                self.show()
                return self.grid[i][0]
        if (self.grid[0][1] and self.grid[0][0] == self.grid[4][0] and self.grid[4][0] == self.grid[8][0]):
            print "Winner! Diagonal 1"
            self.show()
            return self.grid[0][0]
        if (self.grid[2][1] and self.grid[2][0] == self.grid[4][0] and self.grid[4][0] == self.grid[6][0]):
            print "Winner! Diagonal 2"
            self.show()
            return self.grid[2][0]
        for i in range (0, 9):
            if not(self.grid[i][1]):
                break
            if i == 8:
                print "Draw!"
                self.show()
                return 2
        return 1

if __name__ == "__main__":
    test = Grid()
    print "Testing down:"
    test.move(3)
    test.move(6)
    test.move(1)
    test.move(2)
    test.move(4)
    test.move(5)
    test.move(7)

    test = Grid()
    print "Testing across:"
    test.move(0)
    test.move(4)
    test.move(6)
    test.move(3)
    test.move(1)
    test.move(5)

    test = Grid()
    print "Testing diagonal:"
    test.move(0)
    test.move(3)
    test.move(2)
    test.move(1)
    test.move(8)
    test.move(5)
    test.move(4)

    a = []
    for i in range (0, 9):
        a.append(i)

    for i in range (0, 5):
        print "Test", i
        tester = Grid()
        ret = 1
        random.shuffle(a)
        for j in a:
            if (ret == 1):
                ret = tester.move(j)
        print ret
