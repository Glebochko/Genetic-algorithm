from graphics import *
from random import randint
import time



class bot:
    def __init__(self, x, y, *args):
        self.energy = 30
        self.maxhp = 99
        self.x = x;
        self.y = y;
        self.programCount = 0
        self.route = 5
        self.createNewBot = 0

        if (len(args) == 0):
            self.type = 0
            self.DNA = []
            self.createDNA()


    def createDNA(self):
        for i in range(64):
            self.DNA.append(randint(0, 63))
            #self.DNA.append(25)

    def act(self):
        goout = False
        self.createNewBot = 0
        while (goout != True) :
            theAct = self.DNA[self.programCount]
            if ((theAct >= 0) & (theAct < 8)):
                motion = theAct + self.route
                motion %= 8
                if ((motion == 6)|(motion == 7)|(motion == 0)):
                    self.x -= 1
                elif ((motion == 2)|(motion == 3)|(motion == 4)):
                    self.x += 1
                if ((motion == 0)|(motion == 1)|(motion == 2)):
                    self.y -= 1
                elif ((motion == 4)|(motion == 5)|(motion == 6)):
                    self.y += 1
                goout = True

            elif ((theAct >= 8) & (theAct < 16)):
                self.route += theAct
                self.route %= 8
                #goout = True
            elif ((theAct >= 16) & (theAct < 32)):
                self.energy += 10
                goout = True
            elif ((theAct >= 32) & (theAct < 40)):
                if (self.energy >= 80):
                    self.createNewBot = 1
                    goout = True
            elif ((theAct >= 40) & (theAct < 64)):
                self.programCount += theAct - 1
                #goout = True    
            else :
                goout = True


            self.programCount += 1
            if (self.programCount > 63):
                self.programCount -= 64
            

    def drawline(self, window, x1, y1, x2, y2):
        line = Line(Point(x1, y1), Point(x2, y2))
        line.setFill('blue')
        line.setWidth(3)
        line.draw(window)

    def showEnergy(self, window, cellsize):
        botInformation = Text(Point(self.x * cellsize + cellsize/2, self.y * cellsize + cellsize/2), self.energy)
        botInformation.setFill('white')
        botInformation.draw(window)

    def drawbot(self, window, cellsize):
        p1 = Point(self.x * cellsize, self.y * cellsize)
        p2 = Point((self.x + 1) * cellsize, self.y * cellsize)
        p3 = Point((self.x + 1) * cellsize, (self.y + 1) * cellsize)
        p4 = Point(self.x * cellsize, (self.y + 1) * cellsize)

        verticles = [p1, p2, p3, p4]

        cell = Polygon(verticles)
        cell.setFill('blue')
        cell.setOutline('black')
        cell.setWidth(1)

        cell.draw(window)
        self.showEnergy(window, cellsize)

    def __str__(self):
        print(self.DNA)
        return 'hp = 30' 


class gen_alg:
    def __init__(self):
        self.mybots = []
        self.cellsize = 10

    def createWindow(self, xmax, ymax, cellsize):
        self.bgcolor = 'white'
        self.cellsize = cellsize
        self.xmax = xmax
        self.ymax = ymax
        self.width = self.xmax * self.cellsize
        self.hight = self.ymax * self.cellsize
        self.window = GraphWin('Genetic algorithm', self.width, self.hight)
    
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

    def windowClear(self):
        p1 = Point(0, 0)
        p2 = Point(self.width, 0)
        p3 = Point(self.width, self.hight)
        p4 = Point(0, self.hight)

        verticles = [p1, p2, p3, p4]
        bg = Polygon(verticles)
        bg.setFill(self.bgcolor)
        bg.setOutline(self.bgcolor)

        bg.draw(self.window)

    def drawField(self):
        self.windowClear()
        for i in range(len(self.mybots)):
            self.mybots[i].drawbot(self.window, self.cellsize)

    def botsAction(self):
        for i in range(len(self.mybots)):
            self.mybots[i].energy -= 2
            self.mybots[i].act()
            if (self.mybots[i].createNewBot == 1):
                self.mybots[i].createNewBot = 0
                self.mybots[i].energy -= 40
                self.newbot(self.mybots[i].x + 1, self.mybots[i].y + 1)

    def worldLoop(self, n):
        self.window.getMouse()

        while (True):  
            self.drawField()
            self.botsAction()
            time.sleep(0.1)

        self.pause()

    def start(self):
        self.newbot(6, 5)
        self.newbot(8, 7)
        self.newbot(10, 6)
        self.newbot(12, 5)

        self.worldLoop(5)
    

def main():
    gol = gen_alg()
    gol.createWindow(40, 30, 20)
    gol.start()



main()