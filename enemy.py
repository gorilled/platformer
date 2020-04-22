import pygame

class Enemy():
    def __init__(self, color, x, y, width, height, score, speed):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.score = score
        self.speed = speed

    def draw_and_play(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.height,self.width))
        self.x -= self.speed
        if self.x + self.height < 0:
            self.x = 500 + self.width
            self.score += 1
            self.speed += 0.1
        return self.score
