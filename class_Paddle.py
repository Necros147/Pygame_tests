import random
import pygame as p

class Paddle:
    def __init__(self, surface, color, x, y, height, width):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        paddle = p.draw.rect(self.surface, self.color, (self.x, self.y, self.height, self.width))

    def draw(self):
        global paddle_main
        paddle_main = p.draw.rect(self.surface, self.color, (self.x, self.y, self.height, self.width))

    def paddleMovement(self):
        p.Rect.union(paddle_main, paddle)
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
