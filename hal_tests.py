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


# Classes
class Ball:
    def __init__(self, surface, color, ballX, ballY, heightB, widthB):
        self.surface = surface
        self.color = color
        self.ballX = ballX
        self.ballY = ballY
        self.heightB = heightB
        self.widthB = widthB

    def draw(self):
        p.draw.rect(self.surface, self.color, (self.ballX, self.ballY, self.heightB, self.widthB))

    def ballMovement(self):
        ballDirection = [random.randint(0, 1), random.randint(0, 1)]
        if ballDirection[0] == 0:
            self.ballX -= 0.5
        elif ballDirection[0] == 1:
            self.ballX += 0.5
        if ballDirection[1] == 0:
            self.ballY += 0.5
        elif ballDirection[1] == 1:
            self.ballY -= 0.5
        if self.ballX == 0:
            ballDirection[0] = 1
        if self.ballX == 1200:
            ballDirection[0] = 0
        
'''     def collide(self, selfCollide, surface, color):
            p.draw.rect(surface, color, (ballX + 2, ballY + 2, heightB + 5, widthB + 5))
            p.rect.colliderect(self, paddleP)
            if Pcollide == True:
                if ballDirection[0] == 0 and ballDirection[1] == 0:
                    ballDirection[1] = 1
                elif ballDirection[0] == 1 and ballDirection[1] == 0:
                    ballDirection[1] = 1
'''
    

class Paddle:
    def __init__(self, surface, color, paddleX, paddleY, heightP, widthP):
        self.surface = surface
        self.color = color
        self.paddleX = paddleX
        self.paddleY = paddleY
        self.heightP = heightP
        self.widthP = widthP

    def draw(self):
        p.draw.rect(self.surface, self.color, (self.paddleX, self.paddleY, self.heightP, self.widthP))

    def paddlePmovement(self):
        keys = p.key.get_pressed()
        if keys[p.K_d]:
            self.paddleX += 0.5
        if keys[p.K_a]:
            self.paddleX -= 0.5
        if self.paddleX < 0:
            self.paddleX = 0
        elif self.paddleX > 1000:
            self.paddleX = 1000
        else:
            p.Rect.move(self, (self.paddleX, 800))


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

