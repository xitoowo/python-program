import random

import pygame

pygame.init()
# ширина окна
display_weight = 600
# высота окна
display_height = 600
# размер окна
# display = pygame.display.set_mode((800, 600))
display = pygame.display.set_mode((display_weight, display_height))

# Заголовок окна
pygame.display.set_caption('pySnake')

white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Вызов объекта кадров в секунду
clock = pygame.time.Clock()
snake_speed = 15

# None - шрифт по умолчанию
font_style = pygame.font.SysFont(None, 25)
score_style = pygame.font.SysFont('Calibri', 20)


def score(score):
    value = score_style.render('Your score: ' + str(score), True, yellow)
    display.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for sl in snake_list:
        pygame.draw.rect(display, blue, [sl[0], sl[1], snake_block, snake_block])


def message(msg, color):
    message = font_style.render(msg, True, color)
    display.blit(message, [display_weight / 6, display_height / 3])


def game_loop():
    game = True
    game_close = False

    # длина змейки
    snake_block = 10

    x = display_weight / 2
    y = display_height / 2

    x_change = 0
    y_change = 0

    food_x = round(random.randrange(0, display_weight - snake_block) / 10) * 10
    food_y = round(random.randrange(0, display_weight - snake_block) / 10) * 10

    snake_list = []
    snake_length = 1

    while game:
        while game_close:
            display.fill(white)
            message('You lost! Press Q-Quit or C-Play again!', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game = False
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_d:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_w:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_s:
                    y_change = snake_block
                    x_change = 0
        print(x)
        print(display_weight)
        print(y)
        print(display_height)
        if x >= display_weight or x < 0 or y >= display_height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        display.fill(white)

        pygame.draw.rect(display, green, [food_x, food_y, snake_block, snake_block])

        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for elem in snake_list[:-1]:
            if elem == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        score(snake_length - 1)

        pygame.display.flip()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, display_weight - snake_block) / 10) * 10
            food_y = round(random.randrange(0, display_height - snake_block) / 10) * 10
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
