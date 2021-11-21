
from GameArea import GameArea
import math


class Ball:

    def __init__(self, sheet: GameArea):
        self.radius = 20
        self.posX = 450
        self.posY = 680 - self.radius
        self.vy = 0
        self.vx = 0
        self.v = 0.1
        self.sheet = sheet

    # def updateTheta(self,momentum):
    #     self.theta = (88/27)*momentum
    #     ## converting theta to radians for easy use
    #     self.theta = self.theta*(math.pi/180)

    def updateVelocityBat(self, theta):
        newVY = -math.cos(theta)*self.v
        newVX = math.sin(theta)*self.v
        self.vx = newVX
        self.vy = newVY

    def updatePos(self, newPosX, newPosY):
        self.posX = newPosX
        self.posY = newPosY

    def move(self):
        self.posY += self.vy
        self.posY = min(self.sheet.height - self.radius, self.posY)
        self.posY = max(0, self.posY)
        self.posX += self.vx
        self.posX = max(0, self.posX)
        self.posX = min(self.sheet.width - self.radius, self.posX)
