import time

import pygame

pygame.init()
# ширина окна
display_weight = 600
# высота окна
display_height = 600
# размер окна
# display = pygame.display.set_mode((800, 600))
display = pygame.display.set_mode((display_weight, display_height))
pygame.display.update()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
game_over = False

# длина змейки
snake_block = 10

# Заголовок окна
pygame.display.set_caption('pySnake')

# x1 = 300
# y1 = 300
x1 = display_weight / 2
y1 = display_height / 2


x1_change = 0
y1_change = 0

# Вызов объекта кадров в секунду
clock = pygame.time.Clock()
snake_speed = 30

# None - шрифт по умолчанию
font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    message = font_style.render(msg, True, color)
    display.blit(message, [display_weight // 2, display_height // 2])


while not game_over:
    for event in pygame.event.get():
        # Event - любое событие
        # пример <Event(1024-MouseMotion {'pos': (399, 0), 'rel': (0, -1),
        # 'buttons': (0, 0, 0), 'touch': False, 'window': None})>
        # Если тип event'а выход, прекратить цикл
        if event.type == pygame.QUIT:
            game_over = True
        # Если event нажатие клавиши
        if event.type == pygame.KEYDOWN:
            # Если кнопка ==
            # изменение позиции
            if event.key == pygame.K_a:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_d:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_w:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_s:
                y1_change = snake_block
                x1_change = 0

    x1 += x1_change
    if x1 == 800 or x1 == 0:
        game_over = True
    y1 += y1_change
    if y1 == 600 or y1 == 0:
        game_over = True
    # фон окна
    display.fill(white)
    # pygame.draw.rect(окно, цвет, [позиция по ширине, позиция по высоте, ширина объекта, высота объекта])
    pygame.draw.rect(display, blue, [x1, y1, 10, 10])
    pygame.display.update()
    # Установка количества кадров в секунду
    clock.tick(snake_speed)

message('You lost', red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()
