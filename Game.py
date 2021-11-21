from GameArea import GameArea
from Bat import Bat
from Ball import Ball
import tkinter as tk


class Game:
    def __init__(self):
        def circleCoords():
            return self.ball.posX - self.ball.radius, self.ball.posY - self.ball.radius, self.ball.posX + self.ball.radius, self.ball.posY + self.ball.radius

        def rectangleCoords():
            return self.bat.posX-self.bat.length//2, self.bat.posY - self.bat.breadth//2, self.bat.posX + self.bat.length//2, self.bat.posY + self.bat.breadth//2

        def toggleStartBounce(e):
            self.startBounce = True
        self.win = tk.Tk()
        self.sheet = GameArea()
        self.bat = Bat(self.sheet)
        self.ball = Ball(self.sheet)
        self.gameOn = False
        self.startBounce = False
        self.canvas = tk.Canvas(
            self.win, height=self.sheet.height, width=self.sheet.width, bg="#fff")
        self.sidebar = tk.Frame(
            self.win, height=self.sheet.height, width=150, bg="#219ebc")
        self.sidebar.pack_propagate(0)
        self.win.geometry(f"{self.sheet.width + 150}x{self.sheet.height}")
        self.win.title("BOUNCE")
        x0, y0, x1, y1 = circleCoords()
        self.ballitem = self.canvas.create_oval(x0, y0, x1, y1)
        x0, y0, x1, y1 = rectangleCoords()
        self.batitem = self.canvas.create_rectangle(x0, y0, x1, y1)
        self.win.bind("<KeyPress-Left>", self.bat.leftArrowDown)
        self.win.bind("<KeyRelease-Left>", self.bat.leftArrowUp)
        self.win.bind("<KeyPress-Right>", self.bat.rightArrowDown)
        self.win.bind("<KeyRelease-Right>", self.bat.rightArrowUp)
        self.win.bind("<space>", toggleStartBounce)

    def prephase(self):
        while(not self.startBounce):
            self.bat.move()
            self.canvas.coords(self.batitem, self.bat.posX-self.bat.length//2, self.bat.posY -
                               self.bat.breadth//2, self.bat.posX + self.bat.length//2, self.bat.posY + self.bat.breadth//2)
            # Here ball should always be on top of the Bat. so it shouldn'vx move in verticle direction.
            self.ball.updatePos(self.bat.posX, self.ball.posY)
            self.canvas.coords(self.ballitem, self.ball.posX - self.ball.radius, self.ball.posY -
                               self.ball.radius, self.ball.posX + self.ball.radius, self.ball.posY + self.ball.radius)
            self.ball.updateVelocityBat(self.bat.reflectedAngle())
            self.win.update()

    def update(self):
        self.bat.move()
        self.canvas.coords(self.batitem, self.bat.posX-self.bat.length//2, self.bat.posY -
                           self.bat.breadth//2, self.bat.posX + self.bat.length//2, self.bat.posY + self.bat.breadth//2)
        self.ball.move()
        self.canvas.coords(self.ballitem, self.ball.posX - self.ball.radius, self.ball.posY -
                           self.ball.radius, self.ball.posX + self.ball.radius, self.ball.posY + self.ball.radius)
        self.bounce(self.checkBounce())
        self.win.update()

    def endGame(self):
        self.gameOn = False

    def bounce(self, key):
        def bounceWall(key):
            # key == 1, bounce from vertical wall
            if(key):
                self.ball.vx = -self.ball.vx
            # key = 0, bounce from horizontal wall
            else:
                self.ball.vy = -self.ball.vy

        def bounceBat():
            self.ball.updateVelocityBat(self.bat.reflectedAngle())

        if(key == "End"):
            self.endGame()
        elif(key == "Bat"):
            bounceBat()
        elif(key == "HWall"):
            bounceWall(0)
        elif(key == "VWall"):
            bounceWall(1)
        else:
            pass

    def checkBounce(self):
        def checkBatBounce():
            left = self.bat.posX - self.bat.length//2 - self.ball.radius
            right = self.bat.posX + self.bat.length//2 - self.ball.radius
            if((self.ball.posX >= left and self.ball.posX <= right) and self.ball.posY >= self.bat.posY - self.bat.breadth//2-self.ball.radius):
                return True

        if(self.ball.posY == self.sheet.height - self.ball.radius):
            return 'End'
        elif(checkBatBounce()):
            return 'Bat'

        elif(self.ball.posY <= 0 + self.ball.radius):
            return "HWall"
        elif(self.ball.posX <= 0 + self.ball.radius or self.ball.posX >= self.sheet.width - self.ball.radius):
            return "VWall"

    def startGame(self):
        self.gameOn = True
        self.prephase()
        # add the spacebar event handler and run the next line in that
        while(self.gameOn):
            self.update()

    def startApp(self):
        self.sidebar.grid(row=0, column=0)
        self.canvas.grid(row=0, column=1)
        start = tk.Button(self.sidebar, text="Start", command=self.startGame)
        start.pack()
        stop = tk.Button(self.sidebar, text="Stop", command=self.endGame)
        stop.pack()

        self.win.mainloop()
        ###############################

        # self.canvas.create_oval(game., fill='pink')
        # self.canvas.grid(row=0, column=1)

        # slab = Bat()
        # canvas.create_rectangle(slab.x0, slab.y0, slab.x1, slab.y1, fill="white")
        # canvas.grid(row=0, column=1)
