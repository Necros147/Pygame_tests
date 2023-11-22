#Hangman Concepts
# ~ hmw_s = 'five'
# ~ blnk = ['?', '?', '?', '?']
# ~ print(''.join(blnk))
# ~ let = input('Select a letter: ')
# ~ index = [i for i ,e in enumerate(hmw_s) if e == let]
# ~ print("Index for Value", let+ ':', index)
# ~ for let in hmw_s:
    # ~ hmw_s = list(hmw_s)
    # ~ print(hmw_s.index(let))
    
#Binary Converter
# ~ binary = eval(input('Input binary: '))
# ~ print(bin(binary))
# ~ decimal = input('Input decimal: ')
# ~ print(int(decimal, 2))

#Number Guessing game
# ~ import random

# ~ num = random.randint(1, 100)
# ~ print('Try to guess the number in 20 tries')
# ~ if num > 50:
    # ~ print('The number is greater than 50')
    
# ~ elif num < 50:
    # ~ print('The number is less than 50')
    
# ~ for num_guesses in range(0, 21):
    # ~ guess = eval(input('What is your guess? '))

    # ~ if num < guess:
        # ~ print('The number is less than your guess')
    
    # ~ elif num > guess:
        # ~ print('The number is greater than your guess')
    
    # ~ else:
        # ~ print('Congratulations you guessed the number in', num_guesses, 'tries')
    
# ~ print('Game over, you did not guess the number in 20 tries')

#Turtle Graphics
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
import pygame as p
import random
from socket import *
from pygame.locals import *


#Logo, Title, and initialization
p.init()
screen = p.display.set_mode((1200,900))
clock = p.time.Clock()

white = p.Color(255, 255, 255)
navy = p.Color(0, 0, 100)
paddlePx = 20
ballX = 20
ballY = 500
#Main Loop
while True:
    for event in p.event.get():
        if event.type == QUIT:
            quit()
            raise SystemExit
               
    #Classes
    class Ball:
        def __init__(self,surface, color, ballX, ballY, heightB, widthB):
             self.surface = surface
             self.color = color
             self.ballX = ballX
             self.ballY = ballY
             self.heightB = heightB
             self.widthB = widthB
        
        
        def constructb(self, surface, color, ballX, ballY, heightB, widthB):
            self = p.draw.rect(surface, color, (ballX, ballY, heightB, widthB))
            
        def ballMovement(self, instance):
            ballDirection = [random.randint(0,1), random.randint(0,1)]
            if ballDirection[0] == 0:
                ballX -= 0.5
            elif ballDirection[0] == 1:
                ballX += 0.5
            if ballDirection[1] == 0:
                ballY += 0.5
            elif ballDirection[1] == 1:
                ballY -= 0.5
            if ballX == 0:
                ballDirection[0] = 1
            if ballX == 1200:
                ballDirection[0] = 0
        
        def collide(selfCollide, surface, color):
            selfCollide = p.draw.rect(surface, color, (ballX + 2, ballY + 2, heightB + 5, widthB + 5))
            Pcollide = p.rect.colliderect(self, paddleP)
            Ecollide = p.rect.colliderect(self, paddleE)
            if Pcollide == True:
                if ballDirection[0] == 0 and ballDirection[1] == 0:
                    ballDirection[1] = 1
                elif ballDirection[0] == 1 and ballDirection[1] == 0:
                    ballDirection[1] = 1
    
    class Paddle:
        def __init__(self,surface, color, paddleX, paddleY, heightP, widthP):
             self.surface = surface
             self.color = color
             self.paddleX = paddleX
             self.paddleY = paddleY
             self.heightP = heightP
             self.widthP = widthP
        
        def constructp(self, surface, color, paddleX, paddleY, heightP, widthP):
            self = p.draw.rect(surface, color, (paddleY, paddleY, heightP, widthP))
            
        def paddleP_movement():
            paddlePx = 20
            keys = p.key.get_pressed()
            if keys[p.K_d]:
                paddlePx += 0.5
            if keys[p.K_a]:
                paddlePx -= 0.5
            if paddlePx < 0:
                paddlePx = 0
            elif paddlePx > 1000:
                paddlePx = 1000
            else:
                p.Rect.move(paddleP, (paddlePx, 800))
        
    
    #Background
    screen.fill(navy)
    
    #Graphics Stuff
    paddleP = Paddle.constructp( Paddle, screen, white, 20, 800, 50, 300)
    ball = Ball.constructb( Ball, screen, white, 20, 400, 20, 20)
    



    #Logical Updates
    for i in range(60):
        Paddle.paddleP_movement()
        Ball.ballMovement
        Ball.collide
            
    
    p.display.flip()
    clock.tick(60)
    
