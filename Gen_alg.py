from graphics import *
from random import randint
import time



class bot:
    def __init__(self, x, y, *args):
        self.energy = 30
        self.alive = True
        self.DNALength = 64
        self.x = x;
        self.y = y;
        self.oldx = x;
        self.oldy = y;
        self.color = 'blue'

        self.programCount = 0
        self.route = 5
        self.createNewBot = 0

        if (len(args) == 0):
            self.DNA = []
            self.createDNA()

        if (len(args) == 1):
            self.DNA = args[0]


    def createDNA(self):
        for i in range(self.DNALength):
            self.DNA.append(randint(0, self.DNALength - 1))
            #self.DNA.append(25)

    def mutation(self):
        mutationDNAcell = randint(0, self.DNALength - 1)
        self.DNA[mutationDNAcell] = randint(0, self.DNALength - 1)


    def move(self, dirmv, cellocp):
        x = self.x
        y = self.y
        oldx = x
        oldy = y

        if ((dirmv == 0) & (cellocp[x - 1][y - 1] == 0)):
            x -= 1
            y -= 1
        elif ((dirmv == 1) & (cellocp[x][y - 1] == 0)):
            y -= 1
        elif ((dirmv == 2) & (cellocp[x + 1][y - 1] == 0)):
            x += 1
            y -= 1
        elif ((dirmv == 3) & (cellocp[x + 1][y] == 0)):
            x += 1
        elif ((dirmv == 4) & (cellocp[x + 1][y + 1] == 0)):
            x += 1
            y += 1
        elif ((dirmv == 5) & (cellocp[x][y + 1] == 0)):
            y += 1
        elif ((dirmv == 6) & (cellocp[x - 1][y + 1] == 0)):
            x -= 1
            y += 1
        elif ((dirmv == 7) & (cellocp[x - 1][y] == 0)):
            x -= 1

        self.x = x
        self.y = y
        cellocp[oldx][oldy] = 0
        cellocp[self.x][self.y] = 1

    def act(self, celloccupancy):
        goout = False 
        self.createNewBot = 0
        while (goout != True) :
            theAct = self.DNA[self.programCount]
            if ((theAct >= 0) & (theAct < 8)):
                directionMovement = theAct + self.route
                directionMovement %= 8
                self.move(directionMovement, celloccupancy)
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
            elif ((theAct >= 40) & (theAct < 61)):
                self.programCount += (theAct - 1)
                #goout = True   
            elif ((theAct >= 61) & (theAct < 64)):
                goout = True    
            else :
                goout = True


            self.programCount += 1
            if (self.programCount > 63):
                self.programCount -= 64
            
    def showEnergy(self, window, cellsize):
        botInformation = Text(Point(self.x * cellsize + cellsize/2, self.y * cellsize + cellsize/2), self.energy)
        botInformation.setFill('white')
        botInformation.draw(window)

    def delOldBot(self, window, cellsize):
        p1 = Point(self.oldx * cellsize, self.oldy * cellsize)
        p2 = Point((self.oldx + 1) * cellsize, self.oldy * cellsize)
        p3 = Point((self.oldx + 1) * cellsize, (self.oldy + 1) * cellsize)
        p4 = Point(self.oldx * cellsize, (self.oldy + 1) * cellsize)

        verticles = [p1, p2, p3, p4]

        oldCell = Polygon(verticles)
        oldCell.setFill('white')
        #oldCell.setOutline('white')
        #oldCell.setWidth(1)

        oldCell.draw(window) 
        self.oldx = self.x
        self.oldy = self.y

    def drawNewBot(self, window, cellsize):
        p1 = Point(self.x * cellsize, self.y * cellsize)
        p2 = Point((self.x + 1) * cellsize, self.y * cellsize)
        p3 = Point((self.x + 1) * cellsize, (self.y + 1) * cellsize)
        p4 = Point(self.x * cellsize, (self.y + 1) * cellsize)

        verticles = [p1, p2, p3, p4]

        newCell = Polygon(verticles)
        newCell.setFill(self.color)
        #newCell.setOutline('black')
        #newCell.setWidth(1)

        newCell.draw(window) 

    def drawbot(self, window, cellsize):
        if ((self.oldx != self.x) | (self.oldy != self.y)):
            self.delOldBot(window, cellsize)
            self.drawNewBot(window, cellsize)
        #self.showEnergy(window, cellsize)    

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

        self.celloccupancy = [[0] * (self.ymax + 1) for i in range(self.xmax + 1)]
        for i in range(self.xmax + 1):
            self.celloccupancy[i][self.ymax] = 2 
        for j in range(self.ymax + 1):
            self.celloccupancy[self.xmax][j] = 2 
        self.celloccupancy[self.xmax][self.ymax] = 2 #just in case
        # 0 - free  1 - bot  2 - wall  3 - organics

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

    def preStart(self):
        message = Text(Point(self.width / 2, self.cellsize / 2), 'Click anywhere to start.')
        message.draw(self.window)
        self.window.getMouse()
        self.windowClear()

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
        self.celloccupancy[x][y] = 1

    def drawNotFreePoints(self):
        for i in range(self.xmax):
            for j in range(self.ymax):
                if (self.celloccupancy[i][j] != 0):
                    nfp = Point((i + 0.5) * self.cellsize, (j + 0.5) * self.cellsize)
                    nfp.setOutline('green')
                    nfp.draw(self.window)

    def drawField(self):
        #self.windowClear()
        for i in range(len(self.mybots)):
            thisBot = self.mybots[i]
            thisBot.drawbot(self.window, self.cellsize)
        #self.drawNotFreePoints()

    def botBirth(self, parentBot):
        parentBot.createNewBot = 0
        availableCells = []
        parx, pary = parentBot.x, parentBot.y 

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (([i, j] != [0, 0]) & (self.celloccupancy[parx + i][pary + j] == 0)):
                    availableCells.append([i, j])

        if (len(availableCells) > 0):
            parentBot.energy -= 40
            directionBirth = randint(0, len(availableCells) - 1)
            x = parx + availableCells[directionBirth][0]
            y = pary + availableCells[directionBirth][1]
            self.newbot(x, y)
            self.mybots[len(self.mybots) - 1].DNA = parentBot.DNA

            if(randint(1, 2) == 1):
                self.mybots[len(self.mybots) - 1].mutation()

        

    def killBot(self, targetBot):
        targetBot.energy = 0
        targetBot.alive = False
        targetBot.color = 'gray'
        self.celloccupancy[targetBot.x][targetBot.y] = 3

    def botsAction(self):
        for i in range(len(self.mybots)):
            if (self.mybots[i].alive):
                self.mybots[i].energy -= 6
                if (self.mybots[i].energy > 0):
                    self.mybots[i].act(self.celloccupancy)
                    if (self.mybots[i].createNewBot == 1):
                        self.botBirth(self.mybots[i])
                else :
                    self.killBot(self.mybots[i])

    def worldLoop(self):
        self.preStart()
        self.drawCells()
        outputFrequency = 1
        missedMoves = outputFrequency

        while (True):  
            if (missedMoves == outputFrequency):
                self.drawField()
                missedMoves = 0
                time.sleep(0.1)
            self.botsAction()
            missedMoves += 1

        self.pause()

    def start(self):
        self.newbot(40, 40)
        self.newbot(50, 50)
        self.newbot(60, 40)
        self.newbot(72, 35)

        self.worldLoop()
    

def main():
    gol = gen_alg()
    gol.createWindow(100, 80, 10)
    gol.start()



main()