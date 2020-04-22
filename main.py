import pygame
from player import Player
from enemy import  Enemy
from button import Button
pygame.init()
window_height = 500
window_width = 500
window = pygame.display.set_mode((window_height, window_width))
pygame.display.set_caption("test game about square")
score = 0




player1 = Player(
    color=(255, 255, 255),
    x=40,
    y=460,
    width=40,
    height=40,
    jump_count=10
)
enemy1 = Enemy(
    color=(255, 0, 0),
    x=570,
    y=480,
    width=20,
    height=20,
    speed=5,
    score=score
)
button_start = Button(
    color=(255, 255, 255),
    x=50,
    y=250,
    width=400,
    height=50,
    text="начать игру"


)
button_options = Button(
    color =(255, 255, 255),
    x=50,
    y=325,
    width=400,
    height=50,
    text=('настройки')

)
button_exit = Button(
    color=(255, 255, 255),
    x=50,
    y=400,
    width=400,
    height=50,
    text=('выход')
)
def show_font(x, y):
    font = pygame.font.SysFont('freesansbold.ttf', 60, False)
    score = enemy1.score
    score_text = font.render(f"score:{score} ", False, (255, 255, 255))
    window.blit (score_text, (x, y))

def intro():
    while True:
        window.fill((0, 0, 0))
        pygame.time.delay(25)
        button_start.draw_button(window)
        button_options.draw_button(window)
        button_exit.draw_button(window)
        show_font(150, 200)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.is_over(pos):
                    game()
        pygame.display.update()

def game():
    player1.jump_count =10
    player1.x = 40
    player1.y = 460
    player1.height = 40
    player1.width = 40
    enemy1.x = 570
    enemy1.y = 480
    enemy1.width = 20
    enemy1.height = 20
    enemy1.speed = 5
    game_run = True
    while game_run:

        keys = pygame.key.get_pressed()
        pygame.time.delay(25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
        window.fill((0, 0, 0))
        if player1.x <= enemy1.x <= player1.x + player1.width and player1.y <= enemy1.y <= player1.y + player1.height or \
            player1.x <= enemy1.x <= player1.x + player1.width and player1.y <= enemy1.y <= player1.y:
            game_run = False
        enemy1.x -= enemy1.speed
        player1.draw_and_play(window)
        enemy1.draw_and_play(window)
        show_font(350, 350)
        pygame.display.update()

intro()

