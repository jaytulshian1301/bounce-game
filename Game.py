from GameArea import GameArea
from Bat import Bat
from Ball import Ball
import tkinter as tk
import time


class Game:
    def __init__(self):

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
        self.batitem = None
        self.ballitem = None
        self.win.geometry(f"{self.sheet.width + 150}x{self.sheet.height}")
        self.win.title("BOUNCE")
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
            time.sleep(0.01)
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

        if("End" in key):
            self.endGame()
        if("Bat" in key):
            bounceBat()
        if("HWall" in key):
            bounceWall(0)
        if("VWall" in key):
            bounceWall(1)

    def checkBounce(self):
        l = []

        def checkBatBounce():
            left = self.bat.posX - self.bat.length//2 - self.ball.radius
            right = self.bat.posX + self.bat.length//2 - self.ball.radius
            if((self.ball.posX >= left and self.ball.posX <= right) and self.ball.posY >= self.bat.posY - self.bat.breadth//2-self.ball.radius):
                return True

        if(self.ball.posY >= self.sheet.height - self.ball.radius):
            l.append('End')

        if(checkBatBounce()):
            l.append('Bat')

        if(self.ball.posY <= 0 + self.ball.radius):
            l.append("HWall")
        if(self.ball.posX <= 0 + self.ball.radius or self.ball.posX >= self.sheet.width - self.ball.radius):
            l.append("VWall")
        return l

    def startGame(self):
        self.gameOn = True
        if(not self.ballitem or not self.batitem):
            ballcoords = self.ball.coords()
            self.ballitem = self.canvas.create_oval(
                ballcoords[0], ballcoords[1], ballcoords[2], ballcoords[3], fill="black")
            batcoords = self.bat.coords()
            self.batitem = self.canvas.create_rectangle(
                batcoords[0], batcoords[1], batcoords[2], batcoords[3], fill="purple")
        self.prephase()
        # add the spacebar event handler and run the next line in that
        while(self.gameOn):
            self.update()
            time.sleep(0.001)

    def startApp(self):
        self.sidebar.grid(row=0, column=0)
        self.canvas.grid(row=0, column=1)
        start = tk.Button(self.sidebar, text="Start", command=self.startGame)
        start.pack()
        stop = tk.Button(self.sidebar, text="Stop", command=self.endGame)
        stop.pack()

        self.win.mainloop()
