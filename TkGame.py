import tkinter as tk
from Game import Game


class TkGame(Game):
    def __init__(self):
        super().__init__()

        def toggleStartBounce(e):
            self.startBounce = True
        self.win = tk.Tk()
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

    def initiateFrame(self):
        if(not self.ballitem or not self.batitem):
            ballcoords = self.ball.coords()
            self.ballitem = self.canvas.create_oval(
                ballcoords[0], ballcoords[1], ballcoords[2], ballcoords[3], fill="black")
            batcoords = self.bat.coords()
            self.batitem = self.canvas.create_rectangle(
                batcoords[0], batcoords[1], batcoords[2], batcoords[3], fill="purple")

    def updateFrame(self):
        self.canvas.coords(self.batitem, self.bat.posX-self.bat.length//2, self.bat.posY -
                           self.bat.breadth//2, self.bat.posX + self.bat.length//2, self.bat.posY + self.bat.breadth//2)
        self.canvas.coords(self.ballitem, self.ball.posX - self.ball.radius, self.ball.posY -
                           self.ball.radius, self.ball.posX + self.ball.radius, self.ball.posY + self.ball.radius)
        self.win.update()

    def startApp(self):
        self.sidebar.grid(row=0, column=0)
        self.canvas.grid(row=0, column=1)
        start = tk.Button(self.sidebar, text="Start", command=self.startGame)
        start.pack()
        stop = tk.Button(self.sidebar, text="Stop", command=self.endGame)
        stop.pack()

        self.win.mainloop()
