from libs import tk, canvas
from libs.Ball import Ball
from libs.Paddle import Paddle


def move(event):
    if event.keysym == 'Up':
        if redPad.pos[1] > 5 and blackBall.restarting == 0:
            canvas.move(redPad.id, 0, -15)

    if event.keysym == 'Down' and blackBall.restarting == 0:
        if redPad.pos[3] < 499:
            canvas.move(redPad.id, 0, 15)

    if event.keysym == 'w' and blackBall.restarting == 0:
        if greenPad.pos[1] > 5:
            canvas.move(greenPad.id, 0, -15)

    if event.keysym == 's' and blackBall.restarting == 0:
        if greenPad.pos[3] < 499:
            canvas.move(greenPad.id, 0, 15)


if __name__ == '__main__':
    redPad = Paddle(600, 280, 590, 220, 'red')
    greenPad = Paddle(0, 280, 10, 220, 'green')
    blackBall = Ball(greenPad, redPad, 'red')
    canvas.bind_all('<KeyPress>', move)

    while blackBall.playing == 1:
        redPad.circle()
        greenPad.circle()
        blackBall.circle()

    tk.mainloop()
