from libs import *
import random
import time


class Ball:
    def __init__(self, paddle1, paddle2, color):
        self.pos = None
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.restarting = 0
        self.playing = 1
        self.id = canvas.create_oval(305, 255, 295, 245, fill='black')
        self.x = random.choice([-3, -2, -1, 1, 2, 3])
        self.y = random.choice([-3, 3])
        self.circle()

    def circle(self):
        global scoreRed, scoreGreen
        self.pos = canvas.coords(self.id)
        if self.pos[1] < 0:
            self.y = -1 * self.y
            if self.pos[1] > 0:
                self.x = -1 * self.x

        if self.pos[3] > 500:
            self.y = -1 * self.y
            if self.pos[3] < 0:
                self.x = -1 * self.x

        if self.pos[2] >= self.paddle2.pos[0] \
                and self.pos[3] > self.paddle2.pos[1] and self.pos[1] < self.paddle2.pos[3]:
            self.x = -1 * self.x

        if self.pos[0] <= self.paddle1.pos[2] \
                and self.pos[3] > self.paddle1.pos[1] and self.pos[1] < self.paddle1.pos[3]:
            self.x = -1 * self.x

        self.change_score()
        time.sleep(0.01)
        canvas.move(self.id, self.x, self.y)
        canvas.update()

    def restart(self):
        self.x = random.choice([-3, -2, -1, 1, 2, 3])
        self.y = random.choice([-4, 4, -5, 5])
        canvas.coords(self.id, 305, 255, 295, 245)

    def change_score(self):
        global scoreGreen, scoreRed
        if self.pos[0] <= 0 and self.playing == 1 or self.pos[2] > 600 and self.playing == 1:
            self.restarting = 1
            if self.pos[0] <= 300:
                scoreRed += 1
                canvas.itemconfig(RedScore, text=scoreRed)
            else:
                scoreGreen += 1
                canvas.itemconfig(GreenScore, text=scoreGreen)
            canvas.update()
            self.animation()

    def animation(self):
        for x in range(0, 10):
            time.sleep(0.2)
            canvas.itemconfig(self.id, fill=random.choice(['green', 'red', 'gray', 'cyan', 'blue', 'orange']))
            canvas.update()
        canvas.itemconfig(self.id, fill='black')
        if scoreRed < 2 and scoreGreen < 2:
            self.restart()
            self.paddle1.restart()
            self.paddle2.restart()
            self.restarting = 0
        else:
            self.playing = 0
            if scoreRed > scoreGreen:
                canvas.itemconfig(rectangleRed, fill='green')
                canvas.itemconfig(rectangleGreen, fill='red')
                canvas.itemconfig(RedScore, text='win')
                canvas.itemconfig(GreenScore, text='lose')
            else:
                canvas.itemconfig(rectangleGreen, fill='green')
                canvas.itemconfig(rectangleRed, fill='red')
                canvas.itemconfig(RedScore, text='lose')
                canvas.itemconfig(GreenScore, text='win')
            canvas.update()
