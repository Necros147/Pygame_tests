import random, pygame

# Variables
ball_direction = [random.randint(0, 1), random.randint(0, 1)]
black = pygame.Color(0, 0, 0)


class Ball:
    def __init__(self, surface, color, x, y, height, width):
        self.surface = surface
        self.color = color
        self.ballx = x
        self.y = y
        self.height = height
        self.width = width

    def make(self):
        global ball
        coord_size = [self.ballx, self.y, self.height, self.width]
        ball = pygame.draw.rect(self.surface, self.color, (coord_size))

    def ball_movement(self):
        global ball_direction
        if ball_direction[0] == 0:
            self.ballx -= 3
        elif ball_direction[0] == 1:
            self.ballx += 3
        if ball_direction[1] == 0:
            self.y += 3
        elif ball_direction[1] == 1:
            self.y -= 3
        if self.ballx < 0:
            ball_direction[0] = 1
        if self.ballx > 1180:
            ball_direction[0] = 0
        if self.y < 0:
            self.ballx = 400
            self.y = 400
        if self.y > 880:
            self.ballx = 400
            self.y = 400
        
    def collide(self, instance, instance2):
        vals = [
            self.ballx + 1,
            self.y + 1,
            self.height + 2,
            self.width + 2,
            ]
        ball_collision = pygame.draw.rect(self.surface, black, (vals))
        collision = ball_collision.colliderect(instance)
        collision2 = ball_collision.colliderect(instance2)
        if collision == True:
            if ball_direction[0] == 0 and ball_direction[1] == 0:
                ball_direction[1] = 1
            elif ball_direction[0] == 1 and ball_direction[1] == 0:
                ball_direction[1] = 1
        elif collision2 == True:
            if ball_direction[0] == 0 and ball_direction[1] == 1:
                ball_direction[1] = 0
            elif ball_direction[0] == 1 and ball_direction[1] == 1:
                ball_direction[1] = 0
