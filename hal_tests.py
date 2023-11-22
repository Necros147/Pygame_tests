# Turtle Graphics
# ~ import turtle as t

# ~ t.onscreenclick(t.reset())
# ~ def f():
    # ~ t.fd(10)
# ~ def fl():
    # ~ t.lt(10)
    # ~ t.fd(10)
# ~ def fr():
    # ~ t.rt(10)
    # ~ t.fd(10)
# ~ def bl():
    # ~ t.lt(10)
    # ~ t.bk(10)
# ~ def br():
    # ~ t.rt(10)
    # ~ t.bk(10)
# ~ def b():
    # ~ t.bk(10)
# ~ def l():
    # ~ t.lt(10)
# ~ def r():
    # ~ t.rt(10)

# ~ t.onkeypress(f, "w")
# ~ t.listen()

# ~ t.onkeypress(fl, "q")
# ~ t.listen()

# ~ t.onkeypress(fr, "e")
# ~ t.listen()

# ~ t.onkeypress(bl, "z")
# ~ t.listen()

# ~ t.onkeypress(br, "c")
# ~ t.listen()

# ~ t.onkeypress(b, "s")
# ~ t.listen()

# ~ t.onkeypress(r, "d")
# ~ t.listen()

# ~ t.onkeypress(l, "a")
# ~ t.listen()

# ~ t.mainloop()

#non-Turtle Graphics
import random
import pygame as p
from pygame.locals import *

# Logo, Title, and initialization
p.init()
screen = p.display.set_mode((1200, 900))
clock = p.time.Clock()

white = p.Color(255, 255, 255)
navy = p.Color(0, 0, 100)
# Main Loop
while True:
    for event in p.event.get():
        if event.type == QUIT:
            quit()
            raise SystemExit

    # Background
    screen.fill(navy)

    # Graphics Stuff
    paddleP = Paddle(screen, white, 20, 800, 300, 20)
    ball = Ball(screen, white, 20, 400, 20, 20)
    ball.draw()
    paddleP.draw()

    # Logical Updates
    for i in range(60):
        paddleP.paddlePmovement()
        ball.ballMovement()
#       ball.collide()

    p.display.flip()
    clock.tick(60)

