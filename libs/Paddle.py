from libs import canvas


class Paddle:
    def __init__(self, x1, y1, x2, y2, color):
        self.pos = None
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.circle()

    def circle(self):
        self.pos = canvas.coords(self.id)

    def restart(self):
        canvas.coords(self.id, self.x1, self.y1, self.x2, self.y2)
