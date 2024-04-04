import pygame, time
from class_ball import Ball
from pygame.locals import *

black = pygame.Color(0, 0, 0)

''' Class for pong paddle '''
class Paddle:
    def __init__(self, surface, color, x, y, height, width):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.rect.Rect((self.x, y, width, height))

    ''' Puts the paddle on the screen '''
    def make(self):
        pygame.draw.rect(self.surface, self.color,(self.rect))

    ''' Allows the player's paddle to move '''
    def movement(self):
        direction = 'DOWN'
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            direction = 'LEFT'
        if keys[pygame.K_d]:
            direction = 'RIGHT'
        if direction == 'LEFT':
            self.rect.move_ip(-4, 0)
        elif direction == 'RIGHT':
            self.rect.move_ip(4, 0)
        if self.x < 0:
            self.x += 4
            self.rect.move_ip(4, 0)
        elif self.x > 900:
            self.x -= 4
            self.rect.move_ip(-4, 0)

    ''' Allows the AI's paddle to move '''
    def ai_movement(self, instance):
        center = self.x + 150
        if instance.ballx < center:
            self.x -= 4
            self.rect.move_ip(-4, 0)
        if instance.ballx > center:
            self.x += 4
            self.rect.move_ip(4, 0)
        if self.x < 0:
            self.x += 4
            self.rect.move_ip(4, 0)
        elif self.x > 900:
            self.x -= 4
            self.rect.move_ip(-4, 0)
