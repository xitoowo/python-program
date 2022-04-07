# Обработка ввода и анимации
# События
# Взаимодействие пользователя с компьютером основано на событиях, любые действия производимые пользователем порождают
# события - движение мыши, нажатия клавиш, специальных кнопок. Внутри библиотеки PyGame есть инструменты для
# обратки событий, которые происходят внутри приложений.
#
# Мы с вами уже знакомы с методом получения всех произошедших событий - pygame.event.get(), который возвращает события,
# произошедшие с последнего обращения.
#
# Помимо событий выхода из приложения pygame.QUIT, есть множество других - например, нажатия клавиш pygame.KEYDOWN
# или отпускания pygame.KEYUP.
#
# Рассмотрим взаимодействие с событиями на примере небольшой программы, в которой по нажатию клавиш показывается квадрат

import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(40, 40, 120, 120)
color = (0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            color = (255, 255, 255)

    pygame.draw.rect(screen, color, rect, 0)
    pygame.display.flip()

# В данном блоке программа занимется обработкой нажатия клавиш. Сначала мы получаем список всех событий,
# после чего начинаем последовательно проверять их. Если одно из событий соответствует сигналу к завершению программы,
# закрываем окно. Если же это нажатие клавиши - перекрашиваем прямоугольник в белый цвет.
# События
#
# KEYDOWN
# При нажатии клавиш
#
# KEYUP
# При отпускании клавиш
#
# QUIT
# При нажатии кнопки закрытия программы
#
# MOUSEMOTION
# При движении мыши


# Обработка нажатий клавиш
# Когда мы нажимаем клавишу, в систему передаётся не только информация о том, что какая-то кнопка нажата, но и её код.
# Есть два способа получить нажатые клавиши:
# 1. pygame.event.get()
# 2. pygame.key.get_pressed()

# С первым мы уже знакомы, поэтому стоит внимательнее рассмотреть второй. Он позволяет получить список клавиш,
# которые нажаты в данный момент в виде кортежа булевых значений. Чтобы узнать нажата ли интересующая нас кнопка,
# необходимо проверить значение, которе содержится в данном кортеже:

# keys = pygame.key.get_pressed()
# if keys[pygame.K_RETURN]:
#     print("Нажата клавиша enter")


# Перемещение объектов
# Умея получать от пользователя ввод, мы можем реализовать движения наших фигур на экране:
import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(40, 40, 120, 120)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-40, 0)
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(40, 0)
            elif event.key == pygame.K_UP:
                rect.move_ip(0, -40)
            elif event.key == pygame.K_DOWN:
                rect.move_ip(0, 40)

    pygame.draw.rect(screen, (255, 0, 0), rect, 0)

    pygame.display.flip()

# Для движения объектов используются методы move() и move_ip(), которыми обладают объекты, созданные с помощью функций
# из pygame.draw. Первый создаёт новую фигуру такого же типа, находящуюся по заданному смещению,
# второй непосредственно изменяет положение имеющейся фигуры.
#
# Запустив данный код, вы можете заметить, что при перемещении фигуры от неё остаётся “след”. Это связано с тем,
# что при перемещении объекта, мы его не перемещаем на экране, а рисуем на новом месте поверх старого кадра.
#
# Чтобы избежать данной проблемы, надо добавить вызов метода fill() у нашего экрана, на котором мы рисуем и передать
# ему цвет, которым надо закрасить фон. Данное действие надо проводить каждый раз перед отрисовкой кадра:
# здесь могла быть ваша проверка событий
# screen.fill((0, 0, 0))
# pygame.draw.rect(screen, (255, 0, 0), rect, 0)
# pygame.display.flip()


# Использование спрайтов
# Спрайт - двумерное изображение, используемое в играх.
pygame.image.load(path)
# Функция для загрузки спрайта из картинки. Path - путь до изображения, возвращает объект типа Surface,
# который можно использовать для рисования.
#
# Для отрисовки спрайта на экране надо вызвать метод blit() у поверхности на которой производится отрисовка и
# передать объект спрайта вместе с координатами на которых необходимо отрисовать:

screen = pygame.display.set_mode((640, 480))
sprite = pygame.image.load("sprite.png")

screen.blit(sprite, (20, 20))
pygame.quit()
# Анимации
# В pygame анимации создаются при помощи набора спрайтов, которые последовательно отрисовываются:

animation_set = [pygame.image.load(f"r{i}.png") for i in range(1, 6)]

window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()
i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))
    window.blit(animation_set[i // 12], (100, 20))
    i += 1
    if i == 60:
        i = 0

    pygame.display.flip()
    clock.tick(60)

# Создаём список спрайтов, каждый из которых будет отдельным кадром анимации:
animation_set = [pygame.image.load(f"r{i}.png") for i in range(1, 6)]

# Создаём часы, для ограничения количества кадров в секунду:
clock = pygame.time.Clock()

# Вспомогательная переменная, которая поможет выбирать нужную анимацию в зависимости от номера кадра:
i = 0

# Выбор анимации в зависимости от номера кадра и его отрисовка:
window.blit(animation_set[i // 12], (100, 20))

# Изменение переменной, помогающей выбрать нужный кадр:
i += 1
if i == 60:
   i = 0

# Ограничение количества кадров в секунду, благодаря чему становится проще просчитывать
# анимации и синхронизировать события:
clock.tick(60)

# pygame.display.flip() обновляет весь экран
# pygame.display.update() обновляет часть экрана, при вызове без аргументов обновляет весь экран, как flip()