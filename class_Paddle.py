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
