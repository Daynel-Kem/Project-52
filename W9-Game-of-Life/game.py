class Game:
    x = 0
    y = 0
    gameBoard = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        for j in range(y):
            row = []
            for i in range(x):
                row.append(0)
            self.gameBoard.append(row)

    def print(self):
        for j in range(self.y):
            print(self.gameBoard[j])

    def aliveCells(self, cells):
        # Cells are pairs of ints indicating locations (x, y)
        for cell in cells:
            if cell[0] < self.x and cell[1] < self.y:
                self.gameBoard[cell[1]][cell[0]] = 1

    def nextGen(self, n):
        currentBoard = self.gameBoard
        for l in range(n):
            newBoard = currentBoard

            for y in range(self.y):
                for x in range(self.x):
                    neighbours = 0

                    if y > 0:
                        if x > 0:
                            neighbours += currentBoard[y - 1][x - 1]
                        if x < self.x - 1:
                            neighbours += currentBoard[y - 1][x + 1]
                        
                        neighbours += currentBoard[y - 1][x]
                        
                    if y < self.y - 1:
                        if x > 0:
                            neighbours += currentBoard[y + 1][x - 1]
                        if x < self.x - 1:                        
                            neighbours += currentBoard[y + 1][x + 1]
                        
                        neighbours += currentBoard[y + 1][x]
                    
                    if x > 0:
                        neighbours += currentBoard[y][x - 1]
                    if x < self.x - 1:
                        neighbours += currentBoard[y][x + 1]
                        
                    if currentBoard[y][x] == 1:
                        if neighbours <  2 or neighbours > 3:
                            newBoard[y][x] = 0
                    else:
                        if neighbours == 3:
                            newBoard[y][x] = 1
            currentBoard = newBoard
            self.gameBoard = newBoard
            self.print()
            print()
        self.gameBoard = newBoard



