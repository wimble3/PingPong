from tkinter import Tk, Canvas

scoreRed = 0
scoreGreen = 0
tk = Tk()
tk.resizable(0, 0)
tk.title('game')
canvas = Canvas(tk, width=600, height=500)
canvas.pack()
rectangleGreen = canvas.create_rectangle(0, 0, 300, 500)
rectangleRed = canvas.create_rectangle(300, 0, 610, 500)
GreenScore = canvas.create_text(150, 125, text=scoreGreen, font=('Arial', 25))
RedScore = canvas.create_text(450, 125, text=scoreRed, font=('Arial', 25))
