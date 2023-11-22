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
