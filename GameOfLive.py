from graphics import *
from random import randint

def face():
    win = GraphWin('Face', 200, 150) # give title and dimensions
    #win.yUp() # make right side up coordinates!

    head = Circle(Point(40,100), 25) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    label = Text(Point(100, 120), 'A face')
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close() 


class bot:
    def __init__(self, *args):
        #type: 0 - new, 1 - old, 2 - mutant
        self.hp = 30
        self.maxhp = 99
        if (len(args) == 0):
            self.type = 0
            self.DNA = []
            self.createDNA()


    def createDNA(self):
        for i in range(64):
            self.DNA.append(randint(0, 63))

    def __str__(self):
        print(self.DNA)
        return 'j'


class gameOfLive:
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


    def startGame(self):
        self.drawCells()  
        self.pause()
    

def main():
    gol = gameOfLive()
    gol.createWindow(800, 600)
    gol.cellsize = 20
    #gol.startGame()

    newbot = bot()

    print(newbot)



main()