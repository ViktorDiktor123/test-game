# работа окончена
import pygame
import time

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

background = pygame.mixer.Sound('sounds/фон.wav')
background.set_volume(0.25)

jump = pygame.mixer.Sound('sounds/jump.wav')
death = pygame.mixer.Sound('sounds/kill.wav')
death.set_volume(0.05)

death_duration = death.get_length()

background.play(1)

RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (0, 170, 255)
BLUE = (0, 0, 255)
VIOLET = (150, 0, 255)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)

spawn = 1545
x_player = 200
y_player = 550
x_thorn = spawn
y_thorn = 550
points = 0
basic_y = 370
start_y = y_player
size = 80
tap = False
top = False
kill = False
angle = 0
kills = False
death_start_time = 0
points = 0
level = 1
v = 120
win = False
r = 10

player = pygame.image.load("sprites/player.png")
thorn = pygame.image.load("sprites/шипы.png")
backgrounds = pygame.image.load("sprites/фон.png")
backgrounds = pygame.transform.scale(backgrounds, (1545, 720))

font = pygame.font.SysFont(None, 36)
big = pygame.font.SysFont(None, 250)

screen_width, screen_height = 1545, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Test")

class sprites():
    def sprite(image, x, y, width, height, angle):
        player = pygame.transform.scale(image, (width, height))
        player = pygame.transform.rotate(player, angle)
        screen.blit(player, (x, y))
    def floor(screen, color, height, width):
        platform = pygame.draw.rect(screen, color, (0, 630, width, height))

running = True
while running:
    # Цвет экрана
    if level <= 250 / 50:
        screen.fill((level, level * 25, level * 50))
    else:
        screen.blit(backgrounds, (0, 0))
    
    plas = pygame.draw.rect(screen, RED, (600, 15, 10, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if top != True and win == False:
                if kill != True:
                    top = True
                    tap = True
                    jump.play()
                    
    if x_player + size >= x_thorn and x_player <= x_thorn or x_player + size >= x_thorn + 70 and x_player <= x_thorn + 70:
        if y_player + size >= y_thorn and y_player <= y_thorn or y_player + size >= y_thorn + 70 and y_player <= y_thorn + 70:
            kill = True
        else:
            if points < 50 * level and not win:
                points = points + 1 * (v / 120)
            else:
                level += 1
                v += 60
                points = 0
                x_thorn = spawn
    
    if kill == True and not win:
        background.stop()
        background.play()
        points = 0
        y_player = start_y
        x_thorn = spawn
        top = False
        tap = False
        kill = False
    
    # Спрайты
    sprites.sprite(player, x_player, y_player, size, size, angle)
    sprites.sprite(thorn, x_thorn, y_thorn, 80, 80, 0)
    sprites.floor(screen, ORANGE, 100, 1700)
    
    if x_thorn + 80 < 0:
        x_thorn = spawn
    else:
        x_thorn -= 10 * (v / 120)
    
    if tap:
        if y_player >= basic_y:
            y_player -= 10 * (min(v, 150) / 120)
        else:
            tap = False
    else:
        if y_player < start_y:
            y_player += 8 * (min(v, 150) / 120)
            if y_player > start_y:
                y_player = start_y
        else:
            top = False 
    
    if level == 6:
        text = big.render(f"You, ", True, VIOLET)
        screen.blit(text, (300, 100))
    elif level == 7:
        text = big.render(f"You, GOD?", True, VIOLET)
        screen.blit(text, (300, 100))
    elif level > 7 and level < 10:
        text = big.render(f"You 100%", True, VIOLET)
        screen.blit(text, (300, 50))
        text = big.render(f"new GOD", True, VIOLET)
        screen.blit(text, (300, 200))
    elif level == 10:
        v = 120
        win = True
    
    text = font.render(f"balls: {points}", True, RED)
    screen.blit(text, (15, 15))
    text = font.render(f"level: {level}", True, RED)
    screen.blit(text, (500, 15))
    
    if win == True:
        background.stop()
        pygame.draw.circle(screen, BLACK, (750, 500), r)
        if r > 800:
            text = font.render("Создатели:", True, YELLOW)
            screen.blit(text, (710, 45))
            text = font.render("Алексеев Виктор", True, YELLOW)
            screen.blit(text, (680, 65))
            text = font.render("Сценаристы:", True, YELLOW)
            screen.blit(text, (700, 85))
            text = font.render("Алексеев Виктор", True, YELLOW)
            screen.blit(text, (680, 105))
            text = font.render("Текстуры:", True, YELLOW)
            screen.blit(text, (720, 125))
            text = font.render("Неизвестный Пользователь", True, YELLOW)
            screen.blit(text, (620, 145))
            text = font.render("Первый проходитель:", True, YELLOW)
            screen.blit(text, (650, 165))
            text = font.render("Артём Рагозин", True, YELLOW)
            screen.blit(text, (690, 185))
        r += 10
    
    # FPS
    clock = pygame.time.Clock()
    clock.tick(v // 1.5)
    
    # Обновление дисплея
    pygame.display.flip()

# Окончание
pygame.quit()