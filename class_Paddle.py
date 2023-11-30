import random
import pygame as p

class Paddle:
    def __init__(self, surface, color, x, y, height, width):
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
            self.x += 0.5
        if keys[p.K_a]:
            self.x -= 0.5
        if self.x < 0:
            self.x = 0
        elif self.x > 1000:
            self.x = 1000
        else:
            p.Rect.move(paddle, (self.x, 800))
