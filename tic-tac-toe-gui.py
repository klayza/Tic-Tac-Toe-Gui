# Clayton Wieberg
# Tic Tac Toe Gui
# 9/10/2021
import tkinter
from tkinter import *
import math
from tkinter import messagebox

root = tkinter.Tk()
root.title("TicTacToe")
root.geometry("")
root.configure(background='dark gray')

bg = {"bg": "#353839"}

def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()

def isReady(boardsize, gamemode):
    if boardsize > 15:
        print("Bruh")
    else:
        displaygameBoard(boardsize)

def mainMenu():
    clearWindow()
    Label(root, text="Tic Tac Toe", font="Times-new-roman 30 bold", background='dark gray').pack(pady="10", padx="10")
    Button(root, text="Single Player", width="12", height="4").pack(fill="x", pady="3")
    Button(root, text="Multiplayer", width="12", height="4", command=lambda:isReady()).pack(fill="x", pady="3")     #Complete isReady Function
    Label(root, text="Enter Board Size:", width="12", height="4").pack(fill="x", pady="3")
    Entry(root, text="Board Size", width="12").pack(fill="x", pady="8")

def displaygameBoard(size=4**2):
    clearWindow()
    table = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    buttonList = [[] for i in range(int(math.sqrt(size)))]
    count = 1
    print(buttonList)

    gamestatstext = "Player 1 Wins: " + str(4) + "  Player 2 Wins: " + str(9)
    gamestats = Frame(root, width=100, height=50)
    gamestats.grid(columnspan=size, sticky="S")
    Button(gamestats, text="Stats", command=lambda:messageBox(gamestatstext)).pack(side="right", padx=5)
    Label(gamestats, text=gamestatstext).pack(pady=5)

    for x in range(int(math.sqrt(size))):
        for y in range(int(math.sqrt(size))):
            buttonList[x].append(Button(root, text=str(count), width=8, height=4, activebackground="red"))
            buttonList[x][y].config(command=lambda row=x, column=y: click(row, column))
            buttonList[x][y].grid(row=x + 1, column = y)
            count += 1

def click(x, y):
    print(x, y)

def isspotAvailable(x, y):
    if board[x][y] != "X" or board[x][y] != "Y":
        return True
    else:
        return False

def messageBox(text):
    messagebox.showinfo(root, title="Statisticts",  message=text)




mainMenu()
root.mainloop()
