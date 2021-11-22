from math import ceil, pi
from GameArea import GameArea
import tkinter as tk


class Bat:
    def __init__(self, sheet: GameArea):
        self.sheet = sheet
        self.length = 130  # length must always be even
        self.breadth = 20  # breadth must always be even
        self.posX = self.sheet.width//2  # 450
        self.posY = self.sheet.height - self.breadth//2  # 690
        self.dx = 7
        self.momentum = 0

        # rangeMomentum is the whole range of momentum, ex: rangeMomentum = 20 then range will be from -(20//2) to (20//2)
        self.maxMomentum = ceil((self.sheet.width/2 - self.length)/self.dx)
        self.directionInput = None
        # max momentum of the bat can be 27 units i.e = ceil((width of game area - length of the bat)/dx)

    def reflectedAngle(self):
        deg = (80/self.maxMomentum)*self.momentum
        rad = deg*(pi/180)
        return rad

    def coords(self):
        return (self.posX - self.length//2, self.posY - self.breadth//2, self.posX + self.length//2, self.posY + self.breadth//2)

    def moveLeft(self):
        self.posX = self.posX - self.dx
        # self.posX = max(self.length/2, self.posX - self.dx)
        if(self.momentum > 0):
            self.momentum = 0
        self.momentum -= 1
        self.momentum = max(-self.maxMomentum, self.momentum)

    def moveRight(self):
        self.posX = self.posX + self.dx
        # self.posX = min(self.sheet.width - self.length/2, self.posX + self.dx)
        if(self.momentum < 0):
            self.momentum = 0
        self.momentum += 1
        self.momentum = min(self.momentum, self.maxMomentum)

    def stationary(self):
        if(self.momentum > 0):
            self.momentum -= 1
        elif(self.momentum < 0):
            self.momentum += 1
        else:
            self.momentum = 0
        # this is inaccurate, we must find the delay between the key event calls, if the delay between each key press is too low, then we must manipulate momentum range i.e increase or decrease the value 27.
        # whenever you are fixing the momentum, decrease the value of dx for smooth transition.

    def move(self):
        if(self.directionInput == "Left" and self.posX > self.length//2):
            self.moveLeft()
        elif(self.directionInput == "Right" and self.posX < self.sheet.width - self.length//2):
            self.moveRight()
        else:
            self.stationary()

    def rightArrowDown(self, e):
        self.directionInput = 'Right'

    def rightArrowUp(self, e):
        self.directionInput = None

    def leftArrowDown(self, e):
        self.directionInput = "Left"

    def leftArrowUp(self, e):
        self.directionInput = None
    # edge case handling, pressing multiple buttons at the same time
