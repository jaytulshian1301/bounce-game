from GameArea import GameArea
from Bat import Bat
from Ball import Ball
import tkinter as tk
import time


class Game:
    def __init__(self):

        self.sheet = GameArea()
        self.bat = Bat(self.sheet)
        self.ball = Ball(self.sheet)
        self.gameOn = False
        self.startBounce = False

    def prephase(self):
        while(not self.startBounce):
            self.bat.move()
            self.ball.updatePos(self.bat.posX, self.ball.posY)
            self.ball.updateVelocityBat(self.bat.reflectedAngle())
            self.updateFrame()  # GUI Stuff
            time.sleep(0.01)

    def update(self):
        self.bat.move()
        self.ball.move()
        self.bounce(self.checkBounce())
        self.updateFrame()

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
        self.initiateFrame()
        self.prephase()
        # add the spacebar event handler and run the next line in that
        while(self.gameOn):
            self.update()
            time.sleep(0.01)

# Abstract Classes

    def initiateFrame(self):
        pass

    def updateFrame(self):
        pass
