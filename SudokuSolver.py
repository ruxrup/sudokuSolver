from mimetypes import init


class solveSudoku:
    def __init__(self, board):
        self.b = board

    def solve(self):
        self.algo()

    def algo(self):
        empty = self.emptySpace()
        if empty == False:
            return True
        for value in range(1, 10):
            if self.valid(empty, value):
                self.b[empty[0]][empty[1]] = value
                if self.algo():
                    return True
                self.b[empty[0]][empty[1]] = 0
        return False

    def emptySpace(self):
        for x in range(len(self.b)):
            for y in range(len(self.b[0])):
                if self.b[x][y] == 0:
                    return [x, y]
        return False

    def valid(self, position, value):
        if value in self.b[position[0]]:
            return(False)
        for x in range(len(self.b)):
            if self.b[x][position[1]] == value:
                return(False)
        r, c = (position[0]//3)*3, (position[1]//3)*3
        for x in range(r, r+3):
            for y in range(c, c+3):
                if self.b[x][y] == value:
                    return False
        return True

    def showBoard(self):
        for x in range(len(self.b)):
            for y in range(len(self.b[0])):
                if y % 3 == 0 and y != 0:
                    print("|", end=' ')
                print(self.b[x][y], end=' ')
            print()
            if (x+1) % 3 == 0 and x != 0:
                print("---------------------")


board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]]

X = solveSudoku(board)

print("\n")
print("Unsolved Board:")
X.showBoard()

print("\n")

X.solve()
print("Solved Board:")
X.showBoard()
print("\n")
