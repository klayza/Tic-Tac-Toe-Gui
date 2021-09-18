# Clayton Wieberg
# Tic Tac Toe Gui
# 9/10/2021
from tkinter import *
import tkinter
import math
from tkinter import messagebox
import itertools
import random

import time

root = tkinter.Tk()
root.title("TicTacToe")
root.geometry("300x295")
root.configure(background='#523d3d')
bg = {"bg": "#553839"}
wincountx = 0
wincounto = 0

# Creates a global list of the spots on the board and returns that list
def spotInit(size):
    global spots
    counter = itertools.count(1)
    spots = [[next(counter) for i in range(size)] for x in range(size)]
    spots = [[str(x) for x in list] for list in spots]
    return spots

# Will update the board list
def spotUpdate(x, y, spots, turn, condition="none"):
    if condition == "return":
        return spots
    elif turn == "X":
        spots[x][y] = "X"
    elif turn == "O":
        spots[x][y] = "O"
    return spots

def winCount(wincountx1=0, wincounto1=0, code="none"):
    global wincountx
    global wincounto
    wincountx += wincountx1
    wincounto += wincounto1
    if code == "returnx":
        return wincountx
    if code == "returno":
        return wincounto


def adjustRes():
    root.geometry("")

def getSpots():
    return spots

# Clears window
def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()

# Will direct the user to either singleplayer or multiplayer, and decides if user is ready to begin
def isReady(boardsize, gamemode):
    if boardsize > 100:
        print("Bruh")
    elif boardsize % 2 != 1:
        print("Bruh")
    elif gamemode == "multiplayer":
        displaygameBoard("X", boardsize, spotInit(boardsize))
    else:
        displaygameBoard("X", boardsize, spotInit(boardsize), "singleplayer")


# Gets size of the entry widget and returns either 3 or what the user entered
def getSize(e1):
    try:
        size = int(e1.get())
    except:
        size = 3
    return size

# Displays main menu
def mainMenu():
    clearWindow()
    root.geometry("300x295")
    Label(root, text="Tic Tac Toe", font="Times-new-roman 23", background='dark orange', relief="raised").pack(pady="10", fill="x")
    Button(root, text="Single Player", width="12", height="4", command=lambda:isReady(getSize(e1), "singleplayer"), bg="dark gray").pack(fill="x", pady="3")
    Button(root, text="Multiplayer", width="12", height="4", command=lambda:isReady(getSize(e1), "multiplayer"), bg="dark gray").pack(fill="x", pady="3")
    Label(root, text="Enter Board Size Below:", width="12", height="2", bg="dark gray", relief="raised").pack(fill="x", pady="3")
    e1 = Entry(root, text="Board Size", width="12", bg="dark gray")
    e1.pack(fill="x", pady="8")

# Displays the board given turn, size, spots/board list and gamemode
def displaygameBoard(turn, size=3, spots=[], gamemode="multiplayer", wincountx=0, wincounto=0):
    clearWindow()
    adjustRes()

    size = size ** 2
    count = 1
    buttonList = [[] for i in range(int(math.sqrt(size)))]
    gamestatstext = "Player 1 Wins: " + str(winCount(wincountx, wincounto, code="returnx")) + "\nPlayer 2 Wins: " + str(winCount(wincountx, wincounto, code="returnx"))
    gamestats = Frame(root, width=100, height=50)
    gamestats.grid(columnspan=int(size), sticky="S")

    if gamemode == "singleplayer" and turn == "O":
        if checkWin(int(math.sqrt(size)), spots) == "tie":
            if messagebox.askyesno("Continue?", "It was a tie!\nDo you want to play again?"):
                displaygameBoard("X", int(math.sqrt(size)), spotInit(int(math.sqrt(size))), gamemode)
            else:
                exit()
        a = random.randint(0, int(math.sqrt(size) - 1))
        b = random.randint(0, int(math.sqrt(size) - 1))
        if isspotAvailable(a, b, spots):
            click(a, b, size, getSpots(), turn, gamemode)
        else:
            displaygameBoard(turn, int(math.sqrt(size)), spots, gamemode)

    if turn == "X":
        statuslabel = "Player One's Turn"
    elif turn == "O":
        statuslabel = "Player Two's Turn"

    Button(gamestats, text="Stats", bg="dark gray", command=lambda:messageBox(gamestatstext)).grid(column=2, row=0, padx=0)
    Label(gamestats, text=statuslabel).grid(column=1, row=0, padx=0)
    Button(gamestats, text="Home", bg="dark gray", command=lambda:mainMenu()).grid(column=0, row=0, padx=0)

    for x in range(int(math.sqrt(size))):
        for y in range(int(math.sqrt(size))):
            buttonList[x].append(Button(root, bg="dark gray", text=spots[x][y], width=8, height=4, activebackground="red"))
            buttonList[x][y].config(command=lambda row=x, column=y: click(row, column, size, spots, turn, gamemode))
            buttonList[x][y].grid(row=x + 1, column = y)
            count += 1

# Runs if is a button is clicked on the board
# Checks if a spot is available and if so will display the board and update the spots
def click(x, y, size, spots, turn, gamemode):
    print(x, y, size, spots, turn, gamemode)
    if isspotAvailable(x, y, spots):
        if turn == "X":
            displaygameBoard("O", (math.sqrt(size)), spotUpdate(x, y, spots, "X"), gamemode)
        else:
            displaygameBoard("X", (math.sqrt(size)), spotUpdate(x, y, spots, "O"), gamemode)
    print(x, y, size, spots, turn, gamemode)
    if checkWin(int(math.sqrt(size)), spots) == "Xwin":
        if messagebox.askyesno("Continue?", "Player one won!\nDo you want to play again?"):
            displaygameBoard("X", int(math.sqrt(size)), spotInit(int(math.sqrt(size))), gamemode, wincountx=1, wincounto=0)
        else:
            exit()
    if checkWin(int(math.sqrt(size)), spots) == "Owin":
        if messagebox.askyesno("Continue?", "Player two won!\nDo you want to play again?"):
            displaygameBoard("X", int(math.sqrt(size)), spotInit(int(math.sqrt(size))), gamemode, wincountx=0, wincounto=1)
        else:
            exit()
    if checkWin(int(math.sqrt(size)), spots) == "tie":
        if messagebox.askyesno("Continue?", "It was a tie!\nDo you want to play again?"):
            displaygameBoard("X", int(math.sqrt(size)), spotInit(int(math.sqrt(size))), gamemode)
        else:
            exit()
    else:
        if isspotAvailable(x, y, spots):
            if turn == "X":
                displaygameBoard("O", (math.sqrt(size)), spotUpdate(x, y, spots, "X"), gamemode)
            else:
                displaygameBoard("X", (math.sqrt(size)), spotUpdate(x, y, spots, "O"), gamemode)

# Given size and board list will return the outcome
def checkWin(size, spots):
    for letter in ["X", "O"]:
        dg = ""
        # Checks Horizontal
        for horizontal in spots:
            h = ""
            for char in horizontal:
                h += "".join(str(char))
                if h == letter * size:
                    return letter + "win"

        # Checks Vertical
        for i in range(size):
            v = ""
            for vertical in spots:
                 v += vertical[i]
                 if len(v) == size:
                     if v == letter * size:
                         return letter + "win"

        # Checks Diagonal Left-Right
        for i in range(size):
            dg += spots[i][i]
        if dg == letter * size:
            return letter + "win"

        # Checks Diagonal Right-Left
        i = iter(zip(range(0, size), range(size - 1, -1, -1)))
        dg = ""
        for a, b in i:
            dg += spots[a][b]
            if dg == letter * size:
                return letter + "win"

    # Checks if tie
    count = 0
    spts = ""
    variables = [str(p) for p in range(1, (size ** 2) + 1)]
    for row in spots:
        for char in row:
            spts += str(char)
            newspts = "".join(spts)
    for l in variables:
        if str(l) not in newspts:
            count += 1
            if count == size ** 2:
                return "tie"



# Checks if spot is taken by either X or O and will return False if taken and True if not taken
def isspotAvailable(x, y, spots):
    if spots[x][y] == "X":
        return False
    if spots[x][y] == "O":
        return False
    else:
        return True


def messageBox(text):
    messagebox.showinfo(title="Statisticts",  message=text)

mainMenu()
root.mainloop()
