from graphics import *
from random import randint



class bot:
    def __init__(self, x, y, *args):
        #type: 0 - new, 1 - old, 2 - mutant
        self.hp = 30
        self.maxhp = 99
        self.x = x;
        self.y = y;
        if (len(args) == 0):
            self.type = 0
            self.DNA = []
            self.createDNA()


    def createDNA(self):
        for i in range(64):
            self.DNA.append(randint(0, 63))

    def drawline(self, window, x1, y1, x2, y2):
        line = Line(Point(x1, y1), Point(x2, y2))
        line.setFill('blue')
        line.draw(window)

    def darwbot(self, window, cellsize):
        self.drawline(window, self.x * cellsize, self.y * cellsize, (self.x + 1) * cellsize, self.y * cellsize)


    def __str__(self):
        print(self.DNA)
        return 'hp = 30' 


class gen_alg:
    def __init__(self):
        self.cellsize = 10

    def createWindow(self, width, hight):
        self.width = width
        self.hight = hight
        self.window = GraphWin('Game Of Live', self.width, self.hight)
    
    def drawline(self, x1, y1, x2, y2):

        Line(Point(x1, y1), Point(x2, y2)).draw(self.window)

    def pause(self):
        message = Text(Point(self.width / 2, self.cellsize / 2), 'Click anywhere to quit.')
        message.draw(self.window)
        self.window.getMouse()
        self.window.close()

    def drawCells(self):
        x, y = 0, 0
        
        while (x <= self.width):
            self.drawline(x, 0, x, self.hight)
            x += self.cellsize

        while (y <= self.hight):
            self.drawline(0, y, self.width, y)
            y += self.cellsize


    def start(self):
        self.drawCells()  
        self.pause()
    

def main():
    gol = gen_alg()
    gol.createWindow(800, 600)
    gol.cellsize = 20
    gol.start()

    #newbot = bot()

    #print(newbot)



main()