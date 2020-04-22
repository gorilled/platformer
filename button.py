import pygame

class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color

    def draw_button(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        if self.text != '':
            font = pygame.font.SysFont('freesansbold.ttf', 50)
            text = font.render(self.text, False, (0, 0, 0))
            window.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[0] < self.y + self.height:
                return True
            return False