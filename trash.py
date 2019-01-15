
from random import randint

class ss():
    def __init__(self):
        self.celloccupancy = [[0] * 10 for i in range(10)]

    def act(self):
        x = 5
        y = 5
        availableCells = []

        if (self.celloccupancy[x - 1][y - 1] == 0):
            availableCells.append([- 1, - 1])
        if (self.celloccupancy[x][y - 1] == 0):
            availableCells.append([0, - 1])
        if (self.celloccupancy[x + 1][y - 1] == 0):
            availableCells.append([+ 1, - 1])
        if (self.celloccupancy[x + 1][y] == 0):
            availableCells.append([+ 1, 0])
        if (self.celloccupancy[x + 1][y + 1] == 0):
            availableCells.append([+ 1, + 1])
        if (self.celloccupancy[x][y + 1] == 0):
            availableCells.append([0, + 1])
        if (self.celloccupancy[x - 1][y + 1] == 0):
            availableCells.append([- 1, + 1])
        if (self.celloccupancy[x - 1][y] == 0):
            availableCells.append([- 1, 0])

        for i in range(len(availableCells)):
            print(availableCells[i])

    def act2(self):
        x = 5
        y = 5
        availableCells = []

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (([i, j] != [0, 0]) & (self.celloccupancy[x + i][y + j] == 0)):
                    availableCells.append([i, j])
                    print('k')

        #for i in range(len(availableCells)):
        #    print(availableCells[i])
        if (len(availableCells) > 0):
            print(availableCells[randint(0, len(availableCells) - 1)])



def main():
    x = ss()
    x.act2()

    
main()