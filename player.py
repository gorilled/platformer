import pygame


class Player():
    def __init__(self, color, x, y, width, height, jump_count):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_jump = False
        self.jump_count = jump_count

    def draw_and_play(self, window):
        keys = pygame.key.get_pressed()
        pygame.draw.rect(window, self.color, (self.x, self.y, self.height,self.width))
        if not self.is_jump:
            if keys[pygame.K_SPACE]:
                self.is_jump = True
        else:
            if self.jump_count >= -10:
                if self.jump_count < 0:
                    self.y += (self.jump_count ** 2) * 0.5
                else:
                    self.y -= (self.jump_count ** 2) * 0.5
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.is_jump = False
