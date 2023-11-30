''' Class for Pong ball '''

import random
import pygame as p

# Variables
black = p.Color(0, 0, 0)
ball_direction = [random.randint(0, 1), random.randint(0, 1)]


class Ball:
    ''' Class for Pong ball '''
    def __init__(self, surface, color, x, y, height, width):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self):
        ''' Puts the Pong ball on the screen '''
        p.draw.rect(self.surface, self.color, (self.x, self.y, self.height, self.width))

    def ball_movement(self):
        ''' Moves the ball semi-randomly across the screen '''
        if ball_direction[0] == 0:
            self.x -= 0.5
        elif ball_direction[0] == 1:
            self.x += 0.5
        if ball_direction[1] == 0:
            self.y += 0.5
        elif ball_direction[1] == 1:
            self.y -= 0.5
        if self.x == 0:
            ball_direction[0] = 1
        if self.x == 1200:
            ball_direction[0] = 0
        
#     def collide(self, instance):
#        p.draw.rect(self.surface, black, (self.x + 2, self.y + 2, self.height + 5, self.width + 5))
#        collision = p.rect.colliderect(self, instance)
#        if collision == True:
#            if ball_direction[0] == 0 and ball_direction[1] == 0:
#                ball_direction[1] = 1
#            elif ball_direction[0] == 1 and ball_direction[1] == 0:
#                ball_direction[1] = 1

