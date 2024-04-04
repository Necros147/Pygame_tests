import pygame
from class_ball import Ball
from class_paddle import Paddle
from pygame.locals import *

# Logo, Title, and initialization
pygame.init()
screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()

white = pygame.Color(255, 255, 255)
navy = pygame.Color(0, 0, 100)
black = pygame.Color(0, 0, 0)
ai_score = 0
player_score = 0

paddle_player = Paddle(screen, white, 450, 800, 20, 300)
paddle_ai = Paddle(screen, white, 450, 75, 20, 300)
ball = Ball(screen, white, 20, 400, 20, 20)
zero = pygame.image.load("0.png")
one = pygame.image.load("1.jpeg")
two = pygame.image.load("2.png")
three = pygame.image.load("3.png")
four = pygame.image.load("4.png")
five = pygame.image.load("5.png")

# Main Loop
while True:
#    Logical Updates
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    paddle_player.movement()
    paddle_ai.ai_movement(ball)
    ball.ball_movement()
    ball.collide(paddle_player, paddle_ai)
    
    if ball.y >= 880:
        ai_score += 1
    if ball.y <= 1:
        player_score += 1

#    Background
    screen.fill(black)

#    Graphics Stuff
    paddle_player.make()
    paddle_ai.make()
    ball.make()
    
    if ai_score == 0:
        screen.blit(zero, (595, 10))
    elif ai_score == 1:
        screen.blit(one, (595, 10))
    elif ai_score == 2:
        screen.blit(two, (595, 10))
    elif ai_score == 3:
        screen.blit(three, (595, 10))
    elif ai_score == 4:
        screen.blit(four, (595, 10))
    elif ai_score == 5:
        screen.blit(five, (595, 10))
    elif ai_score == 6:
        print('Game Over, The AI Won')
        break

    if player_score == 0:
        screen.blit(zero, (595, 830))
    elif player_score == 1:
        screen.blit(one, (595, 830))
    elif player_score == 2:
        screen.blit(two, (595, 830))
    elif player_score == 3:
        screen.blit(three, (595, 830))
    elif player_score == 4:
        screen.blit(four, (595, 830))
    elif player_score == 5:
        screen.blit(five, (595, 830))
    elif player_score == 6:
        print('Congratulations, You Won!')
        break

    pygame.display.flip()
    clock.tick(60)

