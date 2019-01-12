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
        line.setWidth(3)
        line.draw(window)

    def drawbot(self, window, cellsize):
        self.p1 = Point(self.x * cellsize, self.y * cellsize)
        self.p2 = Point((self.x + 1) * cellsize, self.y * cellsize)
        self.p3 = Point((self.x + 1) * cellsize, (self.y + 1) * cellsize)
        self.p4 = Point(self.x * cellsize, (self.y + 1) * cellsize)

        self.verticles = [self.p1, self.p2, self.p3, self.p4]

        self.cell = Polygon(self.verticles)
        self.cell.setFill('blue')
        self.cell.setOutline('black')
        self.cell.setWidth(1)

        self.cell.draw(window)

    def __str__(self):
        print(self.DNA)
        return 'hp = 30' 


class gen_alg:
    def __init__(self):
        self.mybots = []
        self.cellsize = 10

    def createWindow(self, xmax, ymax, cellsize):
        self.cellsize = cellsize
        self.xmax = xmax
        self.ymax = ymax
        self.width = self.xmax * self.cellsize
        self.hight = self.ymax * self.cellsize
        self.window = GraphWin('Game Of Life', self.width, self.hight)
    
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

    def newbot(self, x, y):
        self.mybots.append(bot(x, y))


    def start(self):
        #self.drawCells() 
        self.newbot(2, 5)
        self.mybots[0].drawbot(self.window, self.cellsize) 
        self.pause()
    

def main():
    gol = gen_alg()
    gol.createWindow(40, 30, 20)
    gol.start()



main()